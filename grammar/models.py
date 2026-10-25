from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class GrammarLesson(models.Model):

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

    theory_text = models.TextField(
        blank=True
    )

    audio_file = models.FileField(
        upload_to="grammar/audio/",
        blank=True,
        null=True,
    )

    estimated_minutes = models.PositiveIntegerField(
        default=10
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
        return f"{self.level} · {self.order}. {self.title}"


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
