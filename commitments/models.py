from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q, Sum


class CommitmentPlan(models.Model):
    """
    Шаблон Commitment Program.

    Например:
    A1 Commitment 60 Days
    - обучение: 10 000 ₸
    - возвратный депозит: 20 000 ₸
    - Lesson: 100 ₸
    - Unified Practice: 500 ₸
    """

    name = models.CharField(max_length=200)

    level = models.ForeignKey(
        "vocabulary.VocabularyLevel",
        on_delete=models.PROTECT,
        related_name="commitment_plans",
    )

    duration_days = models.PositiveIntegerField(default=60)

    tuition_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("10000.00"),
    )

    refundable_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("20000.00"),
    )

    lesson_reward = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("100.00"),
    )

    unified_practice_reward = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("500.00"),
    )

    withdrawal_threshold = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("5000.00"),
    )

    pause_days = models.PositiveSmallIntegerField(default=3)

    late_grace_hours = models.PositiveIntegerField(default=72)

    late_reward_percent = models.PositiveSmallIntegerField(
        default=50,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    terms_version = models.CharField(
        max_length=30,
        default="1.0",
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["level__code", "name"]

    @property
    def total_price(self):
        return self.tuition_amount + self.refundable_amount

    def __str__(self):
        return f"{self.name} — {self.level.code}"


class CourseCommitment(models.Model):

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        AWAITING_PAYMENT = "awaiting_payment", "Awaiting payment"
        ACTIVE = "active", "Active"
        COMPLETED = "completed", "Completed"
        EXPIRED = "expired", "Expired"
        CANCELLED = "cancelled", "Cancelled"

    user_course = models.OneToOneField(
        "vocabulary.UserCourse",
        on_delete=models.CASCADE,
        related_name="commitment",
    )

    plan = models.ForeignKey(
        CommitmentPlan,
        on_delete=models.PROTECT,
        related_name="commitments",
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    # --------------------------------------------------
    # Личная цель
    # --------------------------------------------------

    goal_text = models.TextField(blank=True)

    motivation_text = models.TextField(blank=True)

    # --------------------------------------------------
    # Декларация
    # --------------------------------------------------

    signed_name = models.CharField(
        max_length=200,
        blank=True,
    )

    declaration_snapshot = models.TextField(blank=True)

    terms_version = models.CharField(
        max_length=30,
        blank=True,
    )

    accepted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    # --------------------------------------------------
    # Зафиксированные финансовые условия
    # --------------------------------------------------

    tuition_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    refundable_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    lesson_reward = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    unified_practice_reward = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    withdrawal_threshold = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    pause_days_total = models.PositiveSmallIntegerField(
        default=0,
    )

    late_grace_hours = models.PositiveIntegerField(
        default=0,
    )

    late_reward_percent = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    # --------------------------------------------------
    # Срок
    # --------------------------------------------------

    duration_days = models.PositiveIntegerField(default=60)

    start_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    deadline_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return self.tuition_amount + self.refundable_amount

    @property
    def earned_total(self):
        value = self.ledger_entries.aggregate(
            total=Sum("amount")
        )["total"]

        return value or Decimal("0.00")

    @property
    def paid_total(self):
        value = self.withdrawals.filter(
            status=WithdrawalRequest.Status.PAID
        ).aggregate(
            total=Sum("amount")
        )["total"]

        return value or Decimal("0.00")

    @property
    def reserved_withdrawal_total(self):
        value = self.withdrawals.filter(
            status__in=[
                WithdrawalRequest.Status.PENDING,
                WithdrawalRequest.Status.PROCESSING,
            ]
        ).aggregate(
            total=Sum("amount")
        )["total"]

        return value or Decimal("0.00")

    @property
    def available_balance(self):
        balance = (
            self.earned_total
            - self.paid_total
            - self.reserved_withdrawal_total
        )

        return max(balance, Decimal("0.00"))

    @property
    def remaining_refundable(self):
        remaining = self.refundable_amount - self.earned_total
        return max(remaining, Decimal("0.00"))

    @property
    def pause_days_used(self):
        return self.pause_usages.count()

    @property
    def pause_days_remaining(self):
        return max(
            self.pause_days_total - self.pause_days_used,
            0,
        )

    def __str__(self):
        return (
            f"{self.user_course} — "
            f"{self.get_status_display()}"
        )


class CommitmentCheckpoint(models.Model):
    """
    Контрольная точка программы.

    Обычно одна checkpoint соответствует примерно одной неделе.
    Пользователь сам распределяет Lessons внутри этого периода.
    """

    commitment = models.ForeignKey(
        CourseCommitment,
        on_delete=models.CASCADE,
        related_name="checkpoints",
    )

    number = models.PositiveSmallIntegerField()

    starts_at = models.DateTimeField()

    due_at = models.DateTimeField()

    grace_until = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["number"]

        constraints = [
            models.UniqueConstraint(
                fields=["commitment", "number"],
                name="unique_commitment_checkpoint_number",
            ),
        ]

    def __str__(self):
        return (
            f"{self.commitment_id} — "
            f"Checkpoint {self.number}"
        )


class CommitmentMilestone(models.Model):

    class Kind(models.TextChoices):
        LESSON = "lesson", "Lesson"
        UNIFIED_PRACTICE = (
            "unified_practice",
            "Unified Practice",
        )

    class Status(models.TextChoices):
        LOCKED = "locked", "Locked"
        AVAILABLE = "available", "Available"
        EARNED = "earned", "Earned"
        LATE_EARNED = "late_earned", "Late earned"
        FORFEITED = "forfeited", "Forfeited"

    commitment = models.ForeignKey(
        CourseCommitment,
        on_delete=models.CASCADE,
        related_name="milestones",
    )

    checkpoint = models.ForeignKey(
        CommitmentCheckpoint,
        on_delete=models.PROTECT,
        related_name="milestones",
    )

    kind = models.CharField(
        max_length=30,
        choices=Kind.choices,
    )

    lesson = models.ForeignKey(
        "vocabulary.VocabularyLesson",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="commitment_milestones",
    )

    group = models.ForeignKey(
        "vocabulary.VocabularyGroup",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="commitment_milestones",
    )

    sequence_number = models.PositiveIntegerField()

    reward_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    earned_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.LOCKED,
    )

    educational_completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    rewarded_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sequence_number"]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "commitment",
                    "sequence_number",
                ],
                name="unique_commitment_milestone_sequence",
            ),

            models.UniqueConstraint(
                fields=[
                    "commitment",
                    "lesson",
                ],
                condition=Q(
                    kind="lesson",
                    lesson__isnull=False,
                ),
                name="unique_commitment_lesson_milestone",
            ),

            models.UniqueConstraint(
                fields=[
                    "commitment",
                    "group",
                ],
                condition=Q(
                    kind="unified_practice",
                    group__isnull=False,
                ),
                name="unique_commitment_group_milestone",
            ),

            models.CheckConstraint(
                condition=(
                    Q(
                        kind="lesson",
                        lesson__isnull=False,
                        group__isnull=True,
                    )
                    |
                    Q(
                        kind="unified_practice",
                        lesson__isnull=True,
                        group__isnull=False,
                    )
                ),
                name="valid_commitment_milestone_target",
            ),

            models.CheckConstraint(
                condition=Q(reward_amount__gte=0),
                name="commitment_reward_non_negative",
            ),

            models.CheckConstraint(
                condition=Q(earned_amount__gte=0),
                name="commitment_earned_non_negative",
            ),
        ]

    def __str__(self):
        if self.kind == self.Kind.LESSON:
            target = f"Lesson {self.lesson_id}"
        else:
            target = f"Group {self.group_id}"

        return (
            f"{self.sequence_number}. "
            f"{target} — "
            f"{self.reward_amount} ₸"
        )


class CommitmentLedgerEntry(models.Model):
    """
    Реально начисленные пользователю деньги.

    Одна milestone может создать максимум одну запись.
    """

    class Type(models.TextChoices):
        REWARD_EARNED = (
            "reward_earned",
            "Reward earned",
        )

        REWARD_LATE = (
            "reward_late",
            "Late reward",
        )

    commitment = models.ForeignKey(
        CourseCommitment,
        on_delete=models.CASCADE,
        related_name="ledger_entries",
    )

    milestone = models.OneToOneField(
        CommitmentMilestone,
        on_delete=models.PROTECT,
        related_name="ledger_entry",
    )

    entry_type = models.CharField(
        max_length=30,
        choices=Type.choices,
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

        constraints = [
            models.CheckConstraint(
                condition=Q(amount__gt=0),
                name="commitment_ledger_amount_positive",
            ),
        ]

    def __str__(self):
        return (
            f"{self.commitment_id} — "
            f"+{self.amount} ₸"
        )


class CommitmentPauseUsage(models.Model):
    """
    Использованный Pause Day.
    """

    commitment = models.ForeignKey(
        CourseCommitment,
        on_delete=models.CASCADE,
        related_name="pause_usages",
    )

    used_for_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["used_for_date"]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "commitment",
                    "used_for_date",
                ],
                name="unique_commitment_pause_date",
            ),
        ]

    def __str__(self):
        return (
            f"{self.commitment_id} — "
            f"Pause {self.used_for_date}"
        )


class WithdrawalRequest(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        PAID = "paid", "Paid"
        REJECTED = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"

    commitment = models.ForeignKey(
        CourseCommitment,
        on_delete=models.CASCADE,
        related_name="withdrawals",
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    provider_reference = models.CharField(
        max_length=255,
        blank=True,
    )

    admin_note = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    processed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

        constraints = [
            models.CheckConstraint(
                condition=Q(amount__gt=0),
                name="commitment_withdrawal_amount_positive",
            ),
        ]

    def __str__(self):
        return (
            f"{self.commitment_id} — "
            f"{self.amount} ₸ — "
            f"{self.get_status_display()}"
        )


class CommitmentRewardNotification(models.Model):
    """
    Одно визуальное уведомление на одно денежное достижение.

    Ledger отвечает за деньги.
    Эта модель — только за пользовательский reward moment.
    """

    commitment = models.ForeignKey(
        CourseCommitment,
        on_delete=models.CASCADE,
        related_name="reward_notifications",
    )

    milestone = models.OneToOneField(
        CommitmentMilestone,
        on_delete=models.CASCADE,
        related_name="reward_notification",
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    balance_before = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    balance_after = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    withdrawal_unlocked = models.BooleanField(
        default=False,
    )

    is_seen = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    seen_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return (
            f"{self.commitment_id} — "
            f"+{self.amount} ₸"
        )
