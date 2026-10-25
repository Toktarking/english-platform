from decimal import Decimal

from django.utils import timezone


from .models import (
    CommitmentRewardNotification,
    CourseCommitment,
)

def commitment_dashboard(request):
    if not request.user.is_authenticated:
        return {}

    commitment = (
        CourseCommitment.objects
        .select_related(
            "plan",
            "user_course",
            "user_course__level",
        )
        .filter(
            user_course__user=request.user,
            status=CourseCommitment.Status.ACTIVE,
        )
        .order_by("-created_at")
        .first()
    )

    if not commitment:
        return {
            "active_commitment": None,
        }

    today = timezone.localdate()

    if commitment.start_at:
        start_date = timezone.localtime(
            commitment.start_at
        ).date()

        elapsed_days = max(
            (today - start_date).days,
            0,
        )

        day_number = min(
            elapsed_days + 1,
            commitment.duration_days,
        )
    else:
        day_number = 1

    earned = commitment.earned_total
    available = commitment.available_balance

    if commitment.refundable_amount > 0:
        progress_percent = int(
            (
                earned
                / commitment.refundable_amount
            )
            * Decimal("100")
        )
    else:
        progress_percent = 0

    until_withdrawal = max(
        commitment.withdrawal_threshold - available,
        Decimal("0.00"),
    )


    reward_notification = (
        CommitmentRewardNotification.objects
        .select_related(
            "milestone",
            "milestone__lesson",
            "milestone__group",
        )
        .filter(
            commitment=commitment,
            is_seen=False,
        )
        .order_by("created_at")
        .first()
    )


    return {
        "active_commitment": commitment,
        "commitment_day_number": day_number,
        "commitment_progress_percent": progress_percent,
        "commitment_earned": earned,
        "commitment_available": available,
        "commitment_until_withdrawal": until_withdrawal,
        "commitment_pause_days_remaining": (
            commitment.pause_days_remaining
        ),
        "commitment_reward_notification": reward_notification,
    }