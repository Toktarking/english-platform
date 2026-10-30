from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from grammar.models import (
    GrammarStudyPlan,
    GrammarStudyPlanItem,
    GrammarTopicAssessment,
)

from grammar.placement import (
    get_personal_plan,
)


def _review_days_count(total_days):
    """
    Reserve the final part of the preparation
    period for revision.

    14+ days -> 3 review days
    7-13 days -> 2 review days
    3-6 days -> 1 review day
    1-2 days -> 0 dedicated review days
    """

    if total_days >= 14:
        return 3

    if total_days >= 7:
        return 2

    if total_days >= 3:
        return 1

    return 0


def _pick_evenly(items, count):
    """
    Pick items from across the entire roadmap
    rather than only from its beginning.
    """

    items = list(items)

    if not items or count <= 0:
        return []

    if count >= len(items):
        return items

    if count == 1:
        return [
            items[len(items) // 2]
        ]

    selected = []

    last_index = len(items) - 1

    for position in range(count):

        index = round(
            position
            * last_index
            / (count - 1)
        )

        selected.append(
            items[index]
        )

    return selected


@transaction.atomic
def build_study_plan(
    user,
    exam_date,
    start_date=None,
):
    """
    Build a date-based study plan from the user's
    current Grammar Knowledge Map.

    LEARN has weight 2.
    REVIEW has weight 1.

    The final days are reserved for revision.
    """

    if start_date is None:
        start_date = timezone.localdate()

    if exam_date <= start_date:
        raise ValueError(
            "Exam date must be later than start date."
        )

    # Archive previous active plans.
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

    study_dates = [
        start_date
        + timedelta(days=index)

        for index in range(
            total_days
        )
    ]

    review_days_count = (
        _review_days_count(
            len(study_dates)
        )
    )

    # Keep at least one normal study day
    # whenever the user has topics to learn.
    if (
        source_items
        and
        len(study_dates) > 0
        and
        review_days_count
        >= len(study_dates)
    ):
        review_days_count = (
            len(study_dates)
            - 1
        )

    if review_days_count:

        core_dates = (
            study_dates[
                :-review_days_count
            ]
        )

        final_review_dates = (
            study_dates[
                -review_days_count:
            ]
        )

    else:

        core_dates = study_dates
        final_review_dates = []

    if source_items and not core_dates:
        core_dates = study_dates
        final_review_dates = []

    # -----------------------------------------
    # MAIN PLAN
    # -----------------------------------------

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

        if not core_dates:
            break

        if total_weight:

            date_index = int(
                cumulative_weight
                * len(core_dates)
                / total_weight
            )

        else:
            date_index = 0

        date_index = min(
            date_index,
            len(core_dates) - 1,
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
                    core_dates[
                        date_index
                    ]
                ),
                action=action,
                order=position,
            )
        )

        cumulative_weight += weight

    # -----------------------------------------
    # FINAL REVISION
    # -----------------------------------------

    if (
        final_review_dates
        and
        source_items
    ):

        max_final_topics = (
            len(final_review_dates)
            * 3
        )

        revision_topics = (
            _pick_evenly(
                source_items,
                min(
                    len(source_items),
                    max_final_topics,
                ),
            )
        )

        for position, topic in enumerate(
            revision_topics,
            start=1,
        ):

            date_index = (
                (position - 1)
                % len(final_review_dates)
            )

            plan_items.append(
                GrammarStudyPlanItem(
                    plan=plan,
                    lesson=topic.lesson,
                    scheduled_date=(
                        final_review_dates[
                            date_index
                        ]
                    ),
                    action=(
                        GrammarStudyPlanItem
                        .Action
                        .FINAL_REVIEW
                    ),
                    order=position,
                )
            )

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
    """
    Return every calendar day before the exam,
    including rest/reserve days.
    """

    items = list(
        plan.items
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

    calendar = []

    today = timezone.localdate()

    for index in range(
        total_days
    ):

        current_date = (
            plan.start_date
            + timedelta(days=index)
        )

        day_items = grouped.get(
            current_date,
            [],
        )

        if any(
            item.action
            ==
            GrammarStudyPlanItem
            .Action
            .FINAL_REVIEW

            for item in day_items
        ):

            phase = "FINAL_REVIEW"

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
