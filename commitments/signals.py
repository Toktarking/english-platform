from django.db.models.signals import post_save
from django.dispatch import receiver

from vocabulary.models import (
    LessonPracticeProgress,
    UnifiedGroupPracticeSession,
)

from .services import (
    award_completed_lesson,
    award_completed_unified_practice,
)


@receiver(post_save, sender=LessonPracticeProgress)
def reward_completed_lesson(sender, instance, **kwargs):
    """
    Начисляем возврат только когда завершены
    все четыре стадии Lesson.

    Повторные save безопасны:
    reward engine не начислит деньги дважды.
    """

    is_completed = (
        instance.stage1_completed
        and instance.stage2_completed
        and instance.stage3_completed
        and instance.stage4_completed
    )

    if not is_completed:
        return

    award_completed_lesson(
        user=instance.user,
        lesson=instance.lesson,
    )


@receiver(post_save, sender=UnifiedGroupPracticeSession)
def reward_completed_unified_practice(
    sender,
    instance,
    **kwargs,
):
    """
    Начисляем возврат после полного
    завершения Unified Practice.
    """

    if not instance.is_completed:
        return

    award_completed_unified_practice(
        user=instance.user,
        group=instance.group,
    )