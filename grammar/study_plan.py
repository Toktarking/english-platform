from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from grammar.models import (
    GrammarLessonProgress,
    GrammarStudyPlan,
    GrammarStudyPlanItem,
    GrammarTopicAssessment,
)

from grammar.placement import (
    get_personal_plan,
)


def get_exam_days_count(total_days):
    """
    Reserve the last preparation days
    for mixed exam-style practice.

    14+ days -> 3 exam-practice days
    7-13 days -> 2
    3-6 days -> 1
    1-2 days -> 0
    """

    if total_days >= 14:
        return 3

    if total_days >= 7:
        return 2

    if total_days >= 3:
        return 1

    return 0


@transaction.atomic
def build_study_plan(
    user,
    exam_date,
    start_date=None,
):
    """
    Build the personal Grammar calendar.

    LEARN = weight 2
    REVIEW = weight 1

    Final preparation days are reserved
    for Mixed Exam Practice.
    """

    if start_date is None:
        start_date = timezone.localdate()

    if exam_date <= start_date:
        raise ValueError(
            "Exam date must be later than start date."
        )

    GrammarStudyPlan.objects.filter(
        user=user,
        status=GrammarStudyPlan.Status.ACTIVE,
    ).update(
        status=GrammarStudyPlan.Status.ARCHIVED,
    )

    plan = GrammarStudyPlan.objects.create(
        user=user,
        start_date=start_date,
        exam_date=exam_date,
        status=GrammarStudyPlan.Status.ACTIVE,
    )

    source_items = list(
        get_personal_plan(
            user
        )
    )

    total_days = (
        exam_date
        - start_date
    ).days

    preparation_dates = [
        start_date
        + timedelta(days=index)

        for index in range(total_days)
    ]

    exam_days_count = (
        get_exam_days_count(
            total_days
        )
    )

    if exam_days_count:
        study_dates = (
            preparation_dates[
                :-exam_days_count
            ]
        )
    else:
        study_dates = (
            preparation_dates
        )

    # If preparation is extremely short,
    # always retain a study day.
    if source_items and not study_dates:
        study_dates = preparation_dates

    weights = []

    for item in source_items:

        if (
            item.status
            ==
            GrammarTopicAssessment
            .Status
            .LEARN
        ):
            weight = 2

        else:
            weight = 1

        weights.append(
            weight
        )

    total_weight = sum(
        weights
    )

    cumulative_weight = 0

    plan_items = []

    for position, (
        topic,
        weight,
    ) in enumerate(
        zip(
            source_items,
            weights,
        ),
        start=1,
    ):

        if not study_dates:
            break

        if total_weight:

            date_index = int(
                cumulative_weight
                * len(study_dates)
                / total_weight
            )

        else:
            date_index = 0

        date_index = min(
            date_index,
            len(study_dates) - 1,
        )

        if (
            topic.status
            ==
            GrammarTopicAssessment
            .Status
            .LEARN
        ):

            action = (
                GrammarStudyPlanItem
                .Action
                .LEARN
            )

        else:

            action = (
                GrammarStudyPlanItem
                .Action
                .REVIEW
            )

        plan_items.append(
            GrammarStudyPlanItem(
                plan=plan,
                lesson=topic.lesson,
                scheduled_date=(
                    study_dates[
                        date_index
                    ]
                ),
                action=action,
                order=position,
            )
        )

        cumulative_weight += weight

    GrammarStudyPlanItem.objects.bulk_create(
        plan_items
    )

    return plan


def get_active_study_plan(user):

    return (
        GrammarStudyPlan.objects
        .filter(
            user=user,
            status=GrammarStudyPlan.Status.ACTIVE,
        )
        .order_by("-created_at")
        .first()
    )


def get_plan_calendar(plan):

    items = list(
        plan.items
        .exclude(
            action=(
                GrammarStudyPlanItem
                .Action
                .FINAL_REVIEW
            ),
        )
        .select_related(
            "lesson",
            "lesson__block",
        )
        .order_by(
            "scheduled_date",
            "order",
            "lesson__order",
        )
    )

    completed_lesson_ids = set(
        GrammarLessonProgress.objects
        .filter(
            user=plan.user,
            status=(
                GrammarLessonProgress
                .Status
                .COMPLETED
            ),
            completed_at__gte=plan.created_at,
        )
        .values_list(
            "lesson_id",
            flat=True,
        )
    )

    for item in items:

        item.is_completed = (
            item.lesson_id
            in completed_lesson_ids
        )

    grouped = {}

    for item in items:

        grouped.setdefault(
            item.scheduled_date,
            [],
        ).append(
            item
        )

    total_days = (
        plan.exam_date
        - plan.start_date
    ).days

    exam_days_count = (
        get_exam_days_count(
            total_days
        )
    )

    if exam_days_count:

        first_exam_day = (
            plan.exam_date
            - timedelta(
                days=exam_days_count
            )
        )

    else:

        first_exam_day = None

    today = timezone.localdate()

    calendar = []

    for index in range(total_days):

        current_date = (
            plan.start_date
            + timedelta(days=index)
        )

        day_items = grouped.get(
            current_date,
            [],
        )

        if (
            first_exam_day
            and
            current_date >= first_exam_day
        ):

            phase = "EXAM"

        elif (
            day_items
            and
            all(
                getattr(
                    item,
                    "is_completed",
                    False,
                )
                for item in day_items
            )
        ):

            phase = "COMPLETED"

        elif day_items:

            phase = "STUDY"

        else:

            phase = "REST"

        calendar.append(
            {
                "number": index + 1,
                "date": current_date,
                "items": day_items,
                "phase": phase,
                "is_today": (
                    current_date
                    == today
                ),
                "is_past": (
                    current_date
                    < today
                ),
            }
        )

    return calendar
