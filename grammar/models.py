from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class GrammarBlock(models.Model):
    level = models.CharField(
        max_length=10,
        default="A1",
        db_index=True,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120)
    order = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["level", "order"]
        constraints = [
            models.UniqueConstraint(
                fields=["level", "order"],
                name="uniq_grammar_block_level_order",
            ),
            models.UniqueConstraint(
                fields=["level", "slug"],
                name="uniq_grammar_block_level_slug",
            ),
        ]

    def __str__(self):
        return f"{self.level} · Block {self.order} · {self.title}"


class GrammarLesson(models.Model):
    block = models.ForeignKey(
        "GrammarBlock",
        on_delete=models.SET_NULL,
        related_name="lessons",
        null=True,
        blank=True,
    )


    class Level(models.TextChoices):
        A1 = "A1", "A1"
        A2 = "A2", "A2"
        B1 = "B1", "B1"
        B2 = "B2", "B2"

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
    )

    level = models.CharField(
        max_length=10,
        choices=Level.choices,
        default=Level.A1,
    )

    order = models.PositiveIntegerField(
        default=1
    )

    # Оставляем для совместимости / короткого описания.
    theory_text = models.TextField(
        blank=True
    )

    # Можно использовать для полного аудио всего урока.
    audio_file = models.FileField(
        upload_to="grammar/audio/",
        blank=True,
        null=True,
    )

    estimated_minutes = models.PositiveIntegerField(
        default=10
    )

    pass_score = models.PositiveSmallIntegerField(
        default=70,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    # Пока это НЕ деньги Commitment.
    xp_reward = models.PositiveIntegerField(
        default=100
    )

    is_published = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "level",
            "order",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "level",
                    "order",
                ],
                name="unique_grammar_lesson_level_order",
            ),
        ]

    def __str__(self):
        return (
            f"{self.level} · "
            f"{self.order}. "
            f"{self.title}"
        )


class GrammarLessonSection(models.Model):

    lesson = models.ForeignKey(
        GrammarLesson,
        on_delete=models.CASCADE,
        related_name="sections",
    )

    order = models.PositiveIntegerField()

    title = models.CharField(
        max_length=200
    )

    body = models.TextField()

    # Позволит использовать уже записанные
    # отдельные аудиофрагменты.
    audio_file = models.FileField(
        upload_to="grammar/audio/sections/",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = [
            "order",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "lesson",
                    "order",
                ],
                name="unique_grammar_section_order",
            ),
        ]

    def __str__(self):
        return (
            f"{self.lesson} · "
            f"{self.order}. "
            f"{self.title}"
        )


class GrammarExercise(models.Model):

    class Type(models.TextChoices):
        CHOICE = (
            "choice",
            "Choose one",
        )

    lesson = models.ForeignKey(
        GrammarLesson,
        on_delete=models.CASCADE,
        related_name="exercises",
    )

    section = models.ForeignKey(
        GrammarLessonSection,
        on_delete=models.SET_NULL,
        related_name="exercises",
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField()

    exercise_type = models.CharField(
        max_length=30,
        choices=Type.choices,
        default=Type.CHOICE,
    )

    prompt = models.TextField()

    # Например:
    # ["a", "an", "the", "—"]
    options = models.JSONField(
        default=list
    )

    correct_answer = models.CharField(
        max_length=500
    )

    explanation = models.TextField(
        blank=True
    )

    is_published = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = [
            "order",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "lesson",
                    "order",
                ],
                name="unique_grammar_exercise_order",
            ),
        ]

    def __str__(self):
        return (
            f"{self.lesson} · "
            f"Exercise {self.order}"
        )


class GrammarLessonProgress(models.Model):

    class Status(models.TextChoices):
        NOT_STARTED = (
            "not_started",
            "Not started",
        )
        IN_PROGRESS = (
            "in_progress",
            "In progress",
        )
        COMPLETED = (
            "completed",
            "Completed",
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="grammar_progress",
    )

    lesson = models.ForeignKey(
        GrammarLesson,
        on_delete=models.CASCADE,
        related_name="user_progress",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_STARTED,
    )

    score = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    correct_answers = models.PositiveIntegerField(
        default=0
    )

    total_questions = models.PositiveIntegerField(
        default=0
    )

    # Награда внутри Grammar.
    # Не связана с CommitmentLedgerEntry.
    xp_earned = models.PositiveIntegerField(
        default=0
    )

    started_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    completed_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "user",
                    "lesson",
                ],
                name="unique_user_grammar_lesson_progress",
            ),
        ]

    def __str__(self):
        return (
            f"{self.user} · "
            f"{self.lesson} · "
            f"{self.status}"
        )
