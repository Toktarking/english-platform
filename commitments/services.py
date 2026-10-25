from datetime import timedelta
from decimal import Decimal
from math import ceil

from django.db import transaction
from django.utils import timezone

from vocabulary.models import (
    UserCourse,
    VocabularyGroup,
    VocabularyLesson,
)

from .models import (
    CommitmentCheckpoint,
    CommitmentLedgerEntry,
    CommitmentMilestone,
    CommitmentPlan,
    CourseCommitment,
    CommitmentRewardNotification,
)


# =========================================================
# EXCEPTIONS
# =========================================================


class CommitmentError(Exception):
    pass


class CommitmentConfigurationError(CommitmentError):
    pass


class CommitmentAlreadyExistsError(CommitmentError):
    pass


# =========================================================
# COURSE SEQUENCE
# =========================================================

def build_commitment_learning_sequence(level):
    """
    Финансовая последовательность курса:

    Group 1:
        Lesson 1
        Lesson 2
        ...
        Unified Practice

    Group 2:
        ...

    VocabularyGroup в текущей модели не имеет is_active.
    """

    sequence = []

    groups = (
        VocabularyGroup.objects
        .filter(level=level)
        .order_by("order", "id")
    )

    for group in groups:

        lessons = (
            VocabularyLesson.objects
            .filter(
                group=group,
                is_active=True,
            )
            .order_by("id")
        )

        for lesson in lessons:
            sequence.append({
                "kind": CommitmentMilestone.Kind.LESSON,
                "lesson": lesson,
                "group": None,
            })

        sequence.append({
            "kind": CommitmentMilestone.Kind.UNIFIED_PRACTICE,
            "lesson": None,
            "group": group,
        })

    return sequence

# =========================================================
# ECONOMIC VALIDATION
# =========================================================


def calculate_expected_refundable_amount(plan):
    """
    Считает, сколько денег реально получится вернуть
    по текущей структуре курса.
    """

    sequence = build_commitment_learning_sequence(
        plan.level
    )

    total = Decimal("0.00")

    for item in sequence:

        if item["kind"] == CommitmentMilestone.Kind.LESSON:
            total += plan.lesson_reward

        elif (
            item["kind"]
            == CommitmentMilestone.Kind.UNIFIED_PRACTICE
        ):
            total += plan.unified_practice_reward

    return total


def validate_commitment_plan(plan):
    """
    Проверяем, что экономика программы сходится.

    Например:

    100 Lessons × 100 ₸ = 10 000 ₸
    20 Unified × 500 ₸ = 10 000 ₸

    Итого = 20 000 ₸.
    """

    if not plan.is_active:
        raise CommitmentConfigurationError(
            "Commitment Plan is not active."
        )

    expected = calculate_expected_refundable_amount(
        plan
    )

    if expected != plan.refundable_amount:
        raise CommitmentConfigurationError(
            (
                "Commitment Plan economics do not match. "
                f"Configured refundable amount: "
                f"{plan.refundable_amount} ₸. "
                f"Actual milestone rewards: "
                f"{expected} ₸."
            )
        )

    return True


# =========================================================
# DRAFT
# =========================================================


@transaction.atomic
def create_commitment_draft(
    *,
    user_course,
    plan,
    goal_text="",
    motivation_text="",
):
    """
    Создаёт черновик Commitment.

    На этом этапе:
    - деньги ещё не активны;
    - дедлайн не запущен;
    - milestones ещё не создаются.
    """

    if CourseCommitment.objects.filter(
        user_course=user_course
    ).exists():
        raise CommitmentAlreadyExistsError(
            "This course already has a commitment."
        )

    if user_course.level_id != plan.level_id:
        raise CommitmentConfigurationError(
            "Commitment Plan level does not match UserCourse."
        )

    validate_commitment_plan(plan)

    commitment = CourseCommitment.objects.create(
        user_course=user_course,
        plan=plan,

        status=CourseCommitment.Status.DRAFT,

        goal_text=goal_text,
        motivation_text=motivation_text,

        # Snapshot экономических условий
        tuition_amount=plan.tuition_amount,
        refundable_amount=plan.refundable_amount,
        lesson_reward=plan.lesson_reward,
        unified_practice_reward=(
            plan.unified_practice_reward
        ),
        withdrawal_threshold=(
            plan.withdrawal_threshold
        ),

        pause_days_total=plan.pause_days,

        late_grace_hours=(
            plan.late_grace_hours
        ),

        late_reward_percent=(
            plan.late_reward_percent
        ),

        duration_days=user_course.duration_days,

        terms_version=plan.terms_version,
    )

    return commitment


# =========================================================
# CHECKPOINTS
# =========================================================


def _build_checkpoints(commitment):
    """
    Делит 60-дневную программу на интервалы
    примерно по 7 дней.

    Количество checkpoints зависит от duration_days:
    8 × 7 дней + последний короткий период.
    """

    if not commitment.start_at:
        raise CommitmentConfigurationError(
            "Commitment has no start date."
        )

    total_days = commitment.duration_days
    checkpoint_count = ceil(total_days / 7)

    checkpoints = []

    for number in range(
        1,
        checkpoint_count + 1,
    ):

        start_day = (number - 1) * 7
        end_day = min(
            number * 7,
            total_days,
        )

        starts_at = (
            commitment.start_at
            + timedelta(days=start_day)
        )

        due_at = (
            commitment.start_at
            + timedelta(days=end_day)
        )

        # Последний checkpoint не должен
        # выходить за дедлайн самого курса.
        if commitment.deadline_at:
            due_at = min(
                due_at,
                commitment.deadline_at,
            )

        grace_until = (
            due_at
            + timedelta(
                hours=commitment.late_grace_hours
            )
        )

        checkpoints.append(
            CommitmentCheckpoint(
                commitment=commitment,
                number=number,
                starts_at=starts_at,
                due_at=due_at,
                grace_until=grace_until,
            )
        )

    CommitmentCheckpoint.objects.bulk_create(
        checkpoints
    )

    return list(
        commitment.checkpoints
        .all()
        .order_by("number")
    )


# =========================================================
# MILESTONES
# =========================================================


def _build_milestones(
    commitment,
    checkpoints,
):
    """
    Автоматически создаёт все денежные milestones.

    Для текущего A1 ожидаем:

    100 Lessons
    +
    20 Unified Practice
    =
    120 milestones
    """

    sequence = build_commitment_learning_sequence(
        commitment.plan.level
    )

    if not sequence:
        raise CommitmentConfigurationError(
            "Course has no learning items."
        )

    milestone_count = len(sequence)
    checkpoint_count = len(checkpoints)

    milestones = []

    for index, item in enumerate(
        sequence,
        start=1,
    ):

        # Равномерно распределяем весь учебный путь
        # между checkpoint'ами.
        checkpoint_index = min(
            (
                (index - 1)
                * checkpoint_count
                // milestone_count
            ),
            checkpoint_count - 1,
        )

        checkpoint = checkpoints[
            checkpoint_index
        ]

        if (
            item["kind"]
            == CommitmentMilestone.Kind.LESSON
        ):
            reward = commitment.lesson_reward

        else:
            reward = (
                commitment
                .unified_practice_reward
            )

        # Первый период доступен сразу.
        # Будущие milestones пока LOCKED.
        if checkpoint.number == 1:
            status = (
                CommitmentMilestone
                .Status
                .AVAILABLE
            )
        else:
            status = (
                CommitmentMilestone
                .Status
                .LOCKED
            )

        milestones.append(
            CommitmentMilestone(
                commitment=commitment,
                checkpoint=checkpoint,

                kind=item["kind"],

                lesson=item["lesson"],
                group=item["group"],

                sequence_number=index,

                reward_amount=reward,

                status=status,
            )
        )

    CommitmentMilestone.objects.bulk_create(
        milestones
    )

    return list(
        commitment.milestones
        .all()
        .order_by("sequence_number")
    )


# =========================================================
# DECLARATION + ACTIVATION
# =========================================================


@transaction.atomic
def activate_commitment(
    *,
    commitment,
    signed_name,
    declaration_snapshot,
    start_at=None,
):
    """
    Активирует Commitment после того,
    как пользователь принял декларацию.

    Пока платёжной системы нет,
    эту функцию можно использовать
    как TEST activation.
    """

    commitment = (
        CourseCommitment.objects
        .select_for_update()
        .select_related(
            "plan",
            "user_course",
        )
        .get(pk=commitment.pk)
    )

    if commitment.status != CourseCommitment.Status.DRAFT:
        raise CommitmentError(
            "Only draft commitment can be activated."
        )

    if not signed_name.strip():
        raise CommitmentError(
            "Signed name is required."
        )

    if not declaration_snapshot.strip():
        raise CommitmentError(
            "Declaration snapshot is required."
        )

    validate_commitment_plan(
        commitment.plan
    )

    # В production Commitment использует тот же
    # календарь, что и UserCourse.
    #
    # start_at оставляем как override только для тестов,
    # чтобы unit-тесты могли управлять временем.
    if start_at is None:
        from datetime import datetime, time

        course = commitment.user_course
        current_tz = timezone.get_current_timezone()

        start_at = timezone.make_aware(
            datetime.combine(
                course.start_date,
                time.min,
            ),
            current_tz,
        )

        deadline_at = timezone.make_aware(
            datetime.combine(
                course.target_date,
                time.max,
            ),
            current_tz,
        )

        commitment.duration_days = (
            course.duration_days
        )

    else:
        # Явный start_at используется тестами.
        deadline_at = (
            start_at
            + timedelta(
                days=commitment.duration_days
            )
        )

    commitment.signed_name = signed_name.strip()

    commitment.declaration_snapshot = (
        declaration_snapshot
    )

    commitment.accepted_at = timezone.now()

    commitment.start_at = start_at
    commitment.deadline_at = deadline_at

    commitment.status = (
        CourseCommitment.Status.ACTIVE
    )

    commitment.save(
        update_fields=[
            "signed_name",
            "declaration_snapshot",
            "accepted_at",
            "start_at",
            "deadline_at",
            "duration_days",
            "status",
            "updated_at",
        ]
    )

    checkpoints = _build_checkpoints(
        commitment
    )

    milestones = _build_milestones(
        commitment,
        checkpoints,
    )

    # Финальная финансовая страховка.
    actual_reward_total = sum(
        (
            milestone.reward_amount
            for milestone in milestones
        ),
        Decimal("0.00"),
    )

    if (
        actual_reward_total
        != commitment.refundable_amount
    ):
        raise CommitmentConfigurationError(
            (
                "Generated milestone total "
                "does not match refundable amount. "
                f"{actual_reward_total} != "
                f"{commitment.refundable_amount}"
            )
        )

    # Legacy-пользователь мог начать обучение
    # раньше появления Commitment.
    #
    # Уже выполненные задания между start_date курса
    # и accepted_at получают полную награду.
    backfill_legacy_progress(
        commitment
    )

    return commitment



# =========================================================
# EXISTING COMMITMENT SCHEDULE ALIGNMENT
# =========================================================


@transaction.atomic
def align_commitment_schedule_with_course(
    commitment,
):
    """
    Выравнивает уже существующий Commitment
    по календарю UserCourse.

    Milestone ID, Ledger и уже заработанные суммы
    не изменяются.
    """

    from datetime import datetime, time

    commitment = (
        CourseCommitment.objects
        .select_for_update()
        .select_related(
            "user_course",
        )
        .get(pk=commitment.pk)
    )

    course = commitment.user_course
    current_tz = timezone.get_current_timezone()

    start_at = timezone.make_aware(
        datetime.combine(
            course.start_date,
            time.min,
        ),
        current_tz,
    )

    deadline_at = timezone.make_aware(
        datetime.combine(
            course.target_date,
            time.max,
        ),
        current_tz,
    )

    commitment.start_at = start_at
    commitment.deadline_at = deadline_at
    commitment.duration_days = course.duration_days

    commitment.save(
        update_fields=[
            "start_at",
            "deadline_at",
            "duration_days",
            "updated_at",
        ]
    )

    checkpoints = list(
        commitment.checkpoints
        .select_for_update()
        .order_by("number")
    )

    for checkpoint in checkpoints:

        start_day = (
            checkpoint.number - 1
        ) * 7

        end_day = min(
            checkpoint.number * 7,
            commitment.duration_days,
        )

        checkpoint.starts_at = (
            start_at
            + timedelta(
                days=start_day
            )
        )

        checkpoint.due_at = min(
            (
                start_at
                + timedelta(
                    days=end_day
                )
            ),
            deadline_at,
        )

        checkpoint.grace_until = (
            checkpoint.due_at
            + timedelta(
                hours=(
                    commitment
                    .late_grace_hours
                )
            )
        )

        checkpoint.save(
            update_fields=[
                "starts_at",
                "due_at",
                "grace_until",
            ]
        )

    # После смены дат открываем те checkpoints,
    # время которых уже наступило.
    sync_commitment_milestones(
        commitment
    )

    return commitment


# =========================================================
# STATUS SYNCHRONIZATION
# =========================================================


@transaction.atomic
def sync_commitment_milestones(
    commitment,
    *,
    now=None,
):
    """
    Открывает milestones текущего периода.

    Пока эта функция НЕ списывает деньги
    и НЕ делает milestone FORFEITED.

    Financial expiration добавим отдельно,
    когда подключим реальные начисления.
    """

    now = now or timezone.now()

    commitment = (
        CourseCommitment.objects
        .select_for_update()
        .get(pk=commitment.pk)
    )

    if (
        commitment.status
        != CourseCommitment.Status.ACTIVE
    ):
        return commitment

    current_checkpoints = (
        CommitmentCheckpoint.objects
        .filter(
            commitment=commitment,
            starts_at__lte=now,
        )
        .values_list(
            "id",
            flat=True,
        )
    )

    CommitmentMilestone.objects.filter(
        commitment=commitment,
        checkpoint_id__in=current_checkpoints,
        status=CommitmentMilestone.Status.LOCKED,
    ).update(
        status=CommitmentMilestone.Status.AVAILABLE
    )

    return commitment


# =========================================================
# REWARD ENGINE
# =========================================================


def _get_reward_result(*, milestone, completed_at):
    """
    Возвращает полную награду независимо
    от даты выполнения.

    Штрафов за опоздание нет.

    Важно:
    award_milestone ожидает три поля:
    status, amount и entry_type.
    """

    return {
        "status":
            CommitmentMilestone
            .Status
            .EARNED,

        "amount":
            milestone.reward_amount,

        "entry_type":
            "reward_earned",
    }






@transaction.atomic
def award_milestone(
    *,
    milestone,
    completed_at=None,
):
    """
    Центральная функция начисления.

    Безопасна для повторного вызова:
    один milestone нельзя оплатить дважды.
    """

    completed_at = completed_at or timezone.now()

    milestone = (
        CommitmentMilestone.objects
        .select_for_update()
        .select_related(
            "commitment",
            "checkpoint",
        )
        .get(pk=milestone.pk)
    )

    commitment = milestone.commitment

    if commitment.status != CourseCommitment.Status.ACTIVE:
        return {
            "awarded": False,
            "reason": "commitment_not_active",
            "amount": Decimal("0.00"),
            "milestone": milestone,
        }

    # Уже был окончательно обработан.
    if milestone.status in [
        CommitmentMilestone.Status.EARNED,
        CommitmentMilestone.Status.LATE_EARNED,
        CommitmentMilestone.Status.FORFEITED,
    ]:
        return {
            "awarded": False,
            "reason": "already_processed",
            "amount": milestone.earned_amount,
            "milestone": milestone,
        }

    result = _get_reward_result(
        milestone=milestone,
        completed_at=completed_at,
    )

    milestone.educational_completed_at = completed_at
    milestone.rewarded_at = completed_at
    milestone.status = result["status"]
    milestone.earned_amount = result["amount"]

    milestone.save(
        update_fields=[
            "educational_completed_at",
            "rewarded_at",
            "status",
            "earned_amount",
        ]
    )

    # FORFEITED не создаёт положительную запись
    # в денежном ledger.

    if result["amount"] > 0:
        ledger_entry, ledger_created = (
            CommitmentLedgerEntry.objects.get_or_create(
                milestone=milestone,
                defaults={
                    "commitment": commitment,
                    "entry_type": result["entry_type"],
                    "amount": result["amount"],
                },
            )
        )

        if ledger_created:
            balance_after = commitment.earned_total

            balance_before = max(
                balance_after - result["amount"],
                Decimal("0.00"),
            )

            withdrawal_unlocked = (
                balance_before < commitment.withdrawal_threshold
                <= balance_after
            )

            CommitmentRewardNotification.objects.create(
                commitment=commitment,
                milestone=milestone,
                amount=result["amount"],
                balance_before=balance_before,
                balance_after=balance_after,
                withdrawal_unlocked=withdrawal_unlocked,
            )



    return {
        "awarded": result["amount"] > 0,
        "reason": (
            "rewarded"
            if result["amount"] > 0
            else "deadline_expired"
        ),
        "amount": result["amount"],
        "milestone": milestone,
    }


# =========================================================
# LESSON REWARD
# =========================================================


@transaction.atomic
def award_completed_lesson(
    *,
    user,
    lesson,
    completed_at=None,
):
    """
    Начисляет возврат за завершённый Lesson.

    Эту функцию вызываем только из backend
    после того, как существующая логика Vocabulary
    действительно завершила Lesson.
    """

    milestone = (
        CommitmentMilestone.objects
        .select_related(
            "commitment",
            "checkpoint",
        )
        .filter(
            commitment__user_course__user=user,
            commitment__status=CourseCommitment.Status.ACTIVE,
            lesson=lesson,
            kind=CommitmentMilestone.Kind.LESSON,
        )
        .first()
    )

    # Пользователь может проходить обычный курс
    # без Commitment Program.
    if milestone is None:
        return {
            "awarded": False,
            "reason": "no_active_commitment",
            "amount": Decimal("0.00"),
            "milestone": None,
        }

    return award_milestone(
        milestone=milestone,
        completed_at=completed_at,
    )


# =========================================================
# UNIFIED PRACTICE REWARD
# =========================================================


@transaction.atomic
def award_completed_unified_practice(
    *,
    user,
    group,
    completed_at=None,
):
    """
    Начисляет возврат за завершённый Unified Practice.
    """

    milestone = (
        CommitmentMilestone.objects
        .select_related(
            "commitment",
            "checkpoint",
        )
        .filter(
            commitment__user_course__user=user,
            commitment__status=CourseCommitment.Status.ACTIVE,
            group=group,
            kind=(
                CommitmentMilestone
                .Kind
                .UNIFIED_PRACTICE
            ),
        )
        .first()
    )

    if milestone is None:
        return {
            "awarded": False,
            "reason": "no_active_commitment",
            "amount": Decimal("0.00"),
            "milestone": None,
        }

    return award_milestone(
        milestone=milestone,
        completed_at=completed_at,
    )



# =========================================================
# LEGACY PROGRESS BACKFILL
# =========================================================


@transaction.atomic
def backfill_legacy_progress(
    commitment,
):
    """
    Начисляет полную награду за учебный прогресс,
    который был выполнен:

        после старта UserCourse
        И
        до принятия Commitment.

    Это нужно только для legacy-пользователей,
    которые начали учиться до появления
    обязательного Commitment onboarding.

    Важно:
    - никаких late/forfeited штрафов;
    - награда всегда 100%;
    - старый прогресс ДО начала текущего курса
      не учитывается;
    - повторный запуск безопасен;
    - popup-уведомления не создаются.
    """

    from datetime import datetime, time
    from decimal import Decimal

    from vocabulary.models import (
        LessonPracticeProgress,
        UnifiedGroupPracticeSession,
    )

    commitment = (
        CourseCommitment.objects
        .select_for_update()
        .select_related(
            "user_course",
        )
        .get(pk=commitment.pk)
    )

    if (
        commitment.status
        != CourseCommitment.Status.ACTIVE
    ):
        return {
            "processed": 0,
            "amount": Decimal("0.00"),
            "items": [],
            "reason": "commitment_not_active",
        }

    if not commitment.accepted_at:
        return {
            "processed": 0,
            "amount": Decimal("0.00"),
            "items": [],
            "reason": "no_accepted_at",
        }

    course = commitment.user_course
    user = course.user

    course_start = timezone.make_aware(
        datetime.combine(
            course.start_date,
            time.min,
        ),
        timezone.get_current_timezone(),
    )

    cutoff = commitment.accepted_at

    # -----------------------------------------------------
    # Фактический прогресс пользователя
    # -----------------------------------------------------

    lesson_progress = {
        progress.lesson_id: progress
        for progress in (
            LessonPracticeProgress.objects
            .filter(
                user=user,
                completed_at__isnull=False,
                completed_at__gte=course_start,
                completed_at__lt=cutoff,
            )
        )
    }

    unified_progress = {
        session.group_id: session
        for session in (
            UnifiedGroupPracticeSession.objects
            .filter(
                user=user,
                is_completed=True,
                completed_at__isnull=False,
                completed_at__gte=course_start,
                completed_at__lt=cutoff,
            )
        )
    }

    milestones = (
        CommitmentMilestone.objects
        .select_for_update()
        .filter(
            commitment=commitment,
        )
        .select_related(
            "lesson__group",
            "group",
        )
        .order_by(
            "sequence_number",
        )
    )

    processed = 0
    total_amount = Decimal("0.00")
    items = []

    rewarded_at = timezone.now()

    for milestone in milestones:

        # Уже существует денежная запись —
        # никогда не платим второй раз.
        if (
            CommitmentLedgerEntry.objects
            .filter(
                milestone=milestone,
            )
            .exists()
        ):
            continue

        # Дополнительная защита.
        if milestone.earned_amount > 0:
            continue

        completed_at = None
        label = None

        # -------------------------------------------------
        # LESSON
        # -------------------------------------------------

        if (
            milestone.kind
            ==
            CommitmentMilestone.Kind.LESSON
            and
            milestone.lesson_id
        ):

            progress = lesson_progress.get(
                milestone.lesson_id
            )

            if progress is None:
                continue

            completed_at = progress.completed_at

            label = (
                f"{milestone.lesson.group.name} / "
                f"Lesson {milestone.lesson.number}"
            )

        # -------------------------------------------------
        # UNIFIED PRACTICE
        # -------------------------------------------------

        elif (
            milestone.kind
            ==
            CommitmentMilestone.Kind.UNIFIED_PRACTICE
            and
            milestone.group_id
        ):

            session = unified_progress.get(
                milestone.group_id
            )

            if session is None:
                continue

            completed_at = session.completed_at

            label = (
                f"{milestone.group.name} / "
                "Unified Practice"
            )

        else:
            continue

        amount = milestone.reward_amount

        # Legacy progress всегда оплачивается полностью.
        milestone.educational_completed_at = (
            completed_at
        )

        # rewarded_at показывает момент,
        # когда backfill реально был произведён.
        milestone.rewarded_at = rewarded_at

        milestone.status = (
            CommitmentMilestone.Status.EARNED
        )

        milestone.earned_amount = amount

        milestone.save(
            update_fields=[
                "educational_completed_at",
                "rewarded_at",
                "status",
                "earned_amount",
            ]
        )

        ledger_entry, created = (
            CommitmentLedgerEntry.objects
            .get_or_create(
                milestone=milestone,
                defaults={
                    "commitment": commitment,
                    "entry_type": (
                        CommitmentLedgerEntry
                        .Type
                        .REWARD_EARNED
                    ),
                    "amount": amount,
                },
            )
        )

        if not created:
            continue

        processed += 1
        total_amount += amount

        items.append({
            "milestone_id": milestone.id,
            "label": label,
            "completed_at": completed_at,
            "amount": amount,
        })

    return {
        "processed": processed,
        "amount": total_amount,
        "items": items,
        "reason": "completed",
    }
