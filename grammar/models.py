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


class GrammarAssessmentQuestion(models.Model):
    class Role(models.TextChoices):
        SCREENING = "SCREENING", "Screening"
        TOPIC = "TOPIC", "Topic diagnosis"
        CHECKPOINT = "CHECKPOINT", "Block checkpoint"

    exercise = models.ForeignKey(
        "GrammarExercise",
        on_delete=models.CASCADE,
        related_name="assessment_links",
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        db_index=True,
    )
    priority = models.PositiveSmallIntegerField(
        default=100,
    )
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = [
            "role",
            "priority",
            "exercise__lesson__order",
            "exercise__order",
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["exercise", "role"],
                name="uniq_grammar_assessment_exercise_role",
            ),
        ]

    def __str__(self):
        return (
            f"{self.role} · "
            f"Lesson {self.exercise.lesson.order} · "
            f"Q{self.exercise.order}"
        )


class GrammarPlacementAttempt(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        COMPLETED = "COMPLETED", "Completed"
        ABANDONED = "ABANDONED", "Abandoned"

    class Stage(models.TextChoices):
        SCREENING = "SCREENING", "Block screening"
        TOPIC = "TOPIC", "Topic diagnosis"
        COMPLETE = "COMPLETE", "Complete"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="grammar_placement_attempts",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.IN_PROGRESS,
        db_index=True,
    )
    stage = models.CharField(
        max_length=20,
        choices=Stage.choices,
        default=Stage.SCREENING,
        db_index=True,
    )

    correct_answers = models.PositiveSmallIntegerField(
        default=0,
    )
    total_questions = models.PositiveSmallIntegerField(
        default=0,
    )

    started_at = models.DateTimeField(
        auto_now_add=True,
    )
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        return (
            f"Grammar placement #{self.pk} · "
            f"{self.user} · {self.status}"
        )


class GrammarPlacementAnswer(models.Model):
    attempt = models.ForeignKey(
        "GrammarPlacementAttempt",
        on_delete=models.CASCADE,
        related_name="answers",
    )
    assessment_question = models.ForeignKey(
        "GrammarAssessmentQuestion",
        on_delete=models.CASCADE,
        related_name="placement_answers",
    )

    selected_answer = models.TextField()
    is_correct = models.BooleanField(
        default=False,
        db_index=True,
    )

    answered_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["answered_at"]
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "attempt",
                    "assessment_question",
                ],
                name="uniq_grammar_placement_attempt_question",
            ),
        ]

    def __str__(self):
        return (
            f"Attempt {self.attempt_id} · "
            f"Question {self.assessment_question_id} · "
            f"{'correct' if self.is_correct else 'wrong'}"
        )


class GrammarTopicAssessment(models.Model):
    class Status(models.TextChoices):
        UNKNOWN = "UNKNOWN", "Unknown"
        PROVISIONAL_MASTERED = (
            "PROVISIONAL_MASTERED",
            "Provisionally mastered",
        )
        REVIEW = "REVIEW", "Review"
        LEARN = "LEARN", "Learn"
        MASTERED = "MASTERED", "Mastered"

    class Source(models.TextChoices):
        PLACEMENT_SCREENING = (
            "PLACEMENT_SCREENING",
            "Placement screening",
        )
        PLACEMENT_TOPIC = (
            "PLACEMENT_TOPIC",
            "Placement topic diagnosis",
        )
        CHECKPOINT = "CHECKPOINT", "Checkpoint"
        LESSON = "LESSON", "Lesson"
        REVIEW = "REVIEW", "Review"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="grammar_topic_assessments",
    )
    lesson = models.ForeignKey(
        "GrammarLesson",
        on_delete=models.CASCADE,
        related_name="topic_assessments",
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.UNKNOWN,
        db_index=True,
    )

    correct_answers = models.PositiveSmallIntegerField(
        default=0,
    )
    total_questions = models.PositiveSmallIntegerField(
        default=0,
    )

    source = models.CharField(
        max_length=30,
        choices=Source.choices,
        default=Source.PLACEMENT_SCREENING,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "lesson__order",
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "lesson"],
                name="uniq_grammar_topic_assessment_user_lesson",
            ),
        ]

    def __str__(self):
        return (
            f"{self.user} · "
            f"Lesson {self.lesson.order} · "
            f"{self.status}"
        )


class GrammarStudyPlan(models.Model):

    class Status(models.TextChoices):

        ACTIVE = (
            "ACTIVE",
            "Active",
        )

        ARCHIVED = (
            "ARCHIVED",
            "Archived",
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="grammar_study_plans",
    )

    start_date = models.DateField()

    exam_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
        db_index=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = [
            "-created_at",
        ]

    def __str__(self):

        return (
            f"{self.user} · "
            f"{self.start_date} → "
            f"{self.exam_date}"
        )


class GrammarStudyPlanItem(models.Model):

    class Action(models.TextChoices):

        LEARN = (
            "LEARN",
            "Learn",
        )

        REVIEW = (
            "REVIEW",
            "Review",
        )

        FINAL_REVIEW = (
            "FINAL_REVIEW",
            "Final review",
        )

    plan = models.ForeignKey(
        GrammarStudyPlan,
        on_delete=models.CASCADE,
        related_name="items",
    )

    lesson = models.ForeignKey(
        "GrammarLesson",
        on_delete=models.CASCADE,
        related_name="study_plan_items",
    )

    scheduled_date = models.DateField(
        db_index=True,
    )

    action = models.CharField(
        max_length=20,
        choices=Action.choices,
    )

    order = models.PositiveIntegerField(
        default=1,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = [
            "scheduled_date",
            "order",
            "lesson__order",
        ]

    def __str__(self):

        return (
            f"{self.scheduled_date} · "
            f"{self.action} · "
            f"{self.lesson}"
        )
