
from datetime import timedelta

from django.apps import apps
from django.db import transaction
from django.utils import timezone

from .models import DailyStudyPlan


def get_course_commitment(course):

    CourseCommitment = apps.get_model(
        "commitments",
        "CourseCommitment",
    )

    return (
        CourseCommitment.objects
        .filter(
            user_course=course,
        )
        .order_by("-id")
        .first()
    )


def get_pause_dates(course):

    commitment = (
        get_course_commitment(course)
    )

    if not commitment:
        return set()

    return set(
        commitment.pause_usages
        .values_list(
            "used_for_date",
            flat=True,
        )
    )


@transaction.atomic
def ensure_pause_days_for_past_gaps(
    course,
):
    """
    Автоматически расходует Pause Days
    на прошлые невыполненные календарные дни.

    Pause Day:
    - сохраняет streak;
    - streak не увеличивает;
    - задания не выполняет;
    - награду не начисляет;
    - материал остаётся в курсе.
    """

    commitment = (
        get_course_commitment(course)
    )

    if not commitment:
        return set()

    total = int(
        commitment.pause_days_total
        or 0
    )

    if total <= 0:
        return set()

    PauseUsage = apps.get_model(
        "commitments",
        "CommitmentPauseUsage",
    )

    today = timezone.localdate()

    start_date = (
        course.start_date
        or today
    )

    if commitment.start_at:

        try:
            commitment_start = (
                timezone.localtime(
                    commitment.start_at
                ).date()
            )
        except Exception:
            commitment_start = (
                commitment.start_at.date()
            )

        start_date = max(
            start_date,
            commitment_start,
        )

    end_date = (
        today
        -
        timedelta(days=1)
    )

    if course.target_date:
        end_date = min(
            end_date,
            course.target_date,
        )

    if end_date < start_date:
        return get_pause_dates(
            course
        )

    completed_dates = set(
        DailyStudyPlan.objects
        .filter(
            course=course,
            date__gte=start_date,
            date__lte=end_date,
            status=(
                DailyStudyPlan
                .Status
                .COMPLETED
            ),
        )
        .values_list(
            "date",
            flat=True,
        )
    )

    pause_dates = set(
        PauseUsage.objects
        .filter(
            commitment=commitment,
        )
        .values_list(
            "used_for_date",
            flat=True,
        )
    )

    remaining = max(
        total
        -
        len(pause_dates),
        0,
    )

    if remaining <= 0:
        return pause_dates

    cursor = start_date

    while cursor <= end_date:

        if cursor in completed_dates:

            cursor += timedelta(
                days=1
            )
            continue

        if cursor in pause_dates:

            cursor += timedelta(
                days=1
            )
            continue

        if remaining <= 0:
            break

        exists = (
            PauseUsage.objects
            .filter(
                commitment=commitment,
                used_for_date=cursor,
            )
            .exists()
        )

        if not exists:

            PauseUsage.objects.create(
                commitment=commitment,
                used_for_date=cursor,
            )

            pause_dates.add(
                cursor
            )

            remaining -= 1

        cursor += timedelta(
            days=1
        )

    return pause_dates
