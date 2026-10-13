from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone


# =========================================================
# УРОВЕНЬ CEFR
# =========================================================


class VocabularyLevel(models.Model):

    code = models.CharField(
        max_length=2,
        unique=True,
    )

    name = models.CharField(
        max_length=50,
    )

    order = models.PositiveSmallIntegerField(
        default=1,
    )

    is_active = models.BooleanField(
        default=True,
    )


    class Meta:

        ordering = [
            "order",
        ]


    def __str__(self):

        return self.code


# =========================================================
# ТЕМАТИЧЕСКАЯ ГРУППА
# =========================================================


class VocabularyGroup(models.Model):

    level = models.ForeignKey(
        VocabularyLevel,
        on_delete=models.CASCADE,
        related_name="groups",
    )

    code = models.CharField(
        max_length=20,
    )

    name = models.CharField(
        max_length=150,
    )

    order = models.PositiveSmallIntegerField(
        default=1,
    )

    description = models.TextField(
        blank=True,
    )


    class Meta:

        ordering = [
            "level__order",
            "order",
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "level",
                    "code",
                ],
                name="unique_group_per_level",
            ),

        ]


    def __str__(self):

        return (
            f"{self.level.code} — "
            f"{self.name}"
        )


# =========================================================
# УРОК
# =========================================================


class VocabularyLesson(models.Model):

    group = models.ForeignKey(
        VocabularyGroup,
        on_delete=models.CASCADE,
        related_name="lessons",
    )

    number = models.PositiveSmallIntegerField()

    global_number = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=150,
        blank=True,
    )

    order = models.PositiveSmallIntegerField(
        default=1,
    )

    is_active = models.BooleanField(
        default=True,
    )


    class Meta:

        ordering = [
            "group__order",
            "order",
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "group",
                    "number",
                ],
                name="unique_lesson_per_group",
            ),

        ]


    def __str__(self):

        return (
            f"{self.group.level.code} — "
            f"{self.group.name} — "
            f"Lesson {self.number}"
        )


# =========================================================
# СЛОВО
# =========================================================


class VocabularyWord(models.Model):

    lesson = models.ForeignKey(
        VocabularyLesson,
        on_delete=models.CASCADE,
        related_name="words",
    )


    # =====================================================
    # AUDIO
    # =====================================================

    audio_file = models.FileField(
        upload_to="vocabulary_audio/",
        blank=True,
        null=True,
    )


    # =====================================================
    # SOURCE
    # =====================================================

    source_id = models.PositiveIntegerField(
        unique=True,
    )

    original_headword = models.CharField(
        max_length=200,
        blank=True,
    )


    # =====================================================
    # WORD
    # =====================================================

    word = models.CharField(
        max_length=100,
    )

    sense = models.CharField(
        max_length=200,
        blank=True,
    )

    part_of_speech = models.CharField(
        max_length=50,
        blank=True,
    )


    # =====================================================
    # TRANSLATIONS
    # =====================================================

    translation_ru = models.CharField(
        max_length=250,
    )

    translation_kz = models.CharField(
        max_length=250,
    )


    # =====================================================
    # EXAMPLES
    # =====================================================

    example_en = models.TextField()

    example_ru = models.TextField()

    example_kz = models.TextField()


    # =====================================================
    # CONTEXT PRACTICE
    # LESSON STAGE 3
    # =====================================================

    context_sentence = models.TextField(
        blank=True,
        default="",
    )

    context_wrong_options = models.JSONField(
        default=list,
        blank=True,
    )


    # =====================================================
    # SYSTEM
    # =====================================================

    order = models.PositiveSmallIntegerField(
        default=1,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        ordering = [
            "lesson__group__order",
            "lesson__order",
            "order",
        ]


    def __str__(self):

        return self.word


# =========================================================
# ПРОГРЕСС ПОЛЬЗОВАТЕЛЯ ПО СЛОВУ
# =========================================================


class UserWordProgress(models.Model):

    class Status(models.TextChoices):

        NEW = (
            "new",
            "New",
        )

        LEARNING = (
            "learning",
            "Learning",
        )

        REVIEW = (
            "review",
            "Review",
        )

        MASTERED = (
            "mastered",
            "Mastered",
        )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="word_progress",
    )

    word = models.ForeignKey(
        VocabularyWord,
        on_delete=models.CASCADE,
        related_name="user_progress",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    correct_answers = models.PositiveIntegerField(
        default=0,
    )

    wrong_answers = models.PositiveIntegerField(
        default=0,
    )

    repetitions = models.PositiveIntegerField(
        default=0,
    )

    interval_days = models.PositiveIntegerField(
        default=0,
    )

    next_review = models.DateTimeField(
        null=True,
        blank=True,
    )

    last_reviewed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "user",
                    "word",
                ],
                name="unique_user_word_progress",
            ),

        ]


    def __str__(self):

        return (
            f"{self.user} — "
            f"{self.word.word} — "
            f"{self.status}"
        )


# =========================================================
# GROUP PRACTICE SESSION
# =========================================================


class GroupPracticeSession(models.Model):

    class Phase(models.TextChoices):

        INITIAL = (
            "initial",
            "Initial",
        )

        DECK2_FIRST = (
            "deck2_first",
            "Deck 2 First",
        )

        DECK3 = (
            "deck3",
            "Deck 3",
        )

        DECK2_CHECK = (
            "deck2_check",
            "Deck 2 Check",
        )

        DECK1_CHECK = (
            "deck1_check",
            "Deck 1 Check",
        )

        COMPLETED = (
            "completed",
            "Completed",
        )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="group_practice_sessions",
    )

    group = models.ForeignKey(
        VocabularyGroup,
        on_delete=models.CASCADE,
        related_name="practice_sessions",
    )

    practice_number = models.PositiveSmallIntegerField(
        default=1,
    )

    phase = models.CharField(
        max_length=30,
        choices=Phase.choices,
        default=Phase.INITIAL,
    )

    last_opened_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    # =====================================================
    # CURRENT QUEUE
    # =====================================================

    current_queue = models.JSONField(
        default=list,
        blank=True,
    )

    current_index = models.PositiveIntegerField(
        default=0,
    )


    # =====================================================
    # STATISTICS
    # =====================================================

    mistake_count = models.PositiveIntegerField(
        default=0,
    )

    is_completed = models.BooleanField(
        default=False,
    )


    # =====================================================
    # DATES
    # =====================================================

    started_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "user",
                    "group",
                    "practice_number",
                ],
                name="unique_user_group_practice",
            ),

            models.CheckConstraint(
                condition=(
                    models.Q(
                        practice_number__gte=1
                    )
                    &
                    models.Q(
                        practice_number__lte=4
                    )
                ),
                name="group_practice_number_between_1_and_4",
            ),

        ]


    def __str__(self):

        return (
            f"{self.user} — "
            f"{self.group} — "
            f"Practice {self.practice_number}"
        )


# =========================================================
# GROUP PRACTICE WORD STATE
# =========================================================


class GroupPracticeWordState(models.Model):

    class Deck(models.IntegerChoices):

        UNOPENED = (
            0,
            "Не открыто",
        )

        DECK_1 = (
            1,
            "Колода 1",
        )

        DECK_2 = (
            2,
            "Колода 2",
        )

        DECK_3 = (
            3,
            "Колода 3",
        )


    session = models.ForeignKey(
        GroupPracticeSession,
        on_delete=models.CASCADE,
        related_name="word_states",
    )

    word = models.ForeignKey(
        VocabularyWord,
        on_delete=models.CASCADE,
        related_name="practice_states",
    )

    deck = models.PositiveSmallIntegerField(
        choices=Deck.choices,
        default=Deck.UNOPENED,
    )


    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "session",
                    "word",
                ],
                name="unique_word_in_practice_session",
            ),

        ]


    def __str__(self):

        return (
            f"{self.session.user} — "
            f"{self.word.word} — "
            f"{self.get_deck_display()}"
        )


# =========================================================
# LESSON PRACTICE PROGRESS
# =========================================================


class LessonPracticeProgress(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lesson_practice_progress",
    )

    lesson = models.ForeignKey(
        VocabularyLesson,
        on_delete=models.CASCADE,
        related_name="user_practice_progress",
    )


    # =====================================================
    # STAGE 1
    # TRANSLATION
    # =====================================================

    stage1_completed = models.BooleanField(
        default=False,
    )

    stage1_mistakes = models.PositiveIntegerField(
        default=0,
    )

    stage1_seconds = models.PositiveIntegerField(
        default=0,
    )


    # =====================================================
    # STAGE 2
    # SPELLING
    # =====================================================

    stage2_completed = models.BooleanField(
        default=False,
    )

    stage2_mistakes = models.PositiveIntegerField(
        default=0,
    )

    stage2_seconds = models.PositiveIntegerField(
        default=0,
    )


    # =====================================================
    # STAGE 3
    # CONTEXT
    # =====================================================

    stage3_completed = models.BooleanField(
        default=False,
    )

    stage3_mistakes = models.PositiveIntegerField(
        default=0,
    )

    stage3_seconds = models.PositiveIntegerField(
        default=0,
    )


    # =====================================================
    # STAGE 4
    # LISTENING
    # =====================================================

    stage4_completed = models.BooleanField(
        default=False,
    )

    stage4_mistakes = models.PositiveIntegerField(
        default=0,
    )

    stage4_seconds = models.PositiveIntegerField(
        default=0,
    )


    # =====================================================
    # DATES
    # =====================================================

    first_opened_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    last_opened_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "user",
                    "lesson",
                ],
                name="unique_user_lesson_practice_progress",
            ),

        ]


    def __str__(self):

        return (
            f"{self.user} — "
            f"Lesson {self.lesson.number}"
        )


    # =====================================================
    # COMPLETED
    # =====================================================

    @property
    def is_completed(self):

        return (
            self.stage1_completed
            and
            self.stage2_completed
            and
            self.stage3_completed
            and
            self.stage4_completed
        )


    # =====================================================
    # TOTAL MISTAKES
    # =====================================================

    @property
    def total_mistakes(self):

        return (
            self.stage1_mistakes
            +
            self.stage2_mistakes
            +
            self.stage3_mistakes
            +
            self.stage4_mistakes
        )


    # =====================================================
    # TOTAL TIME
    # =====================================================

    @property
    def total_seconds(self):

        return (
            self.stage1_seconds
            +
            self.stage2_seconds
            +
            self.stage3_seconds
            +
            self.stage4_seconds
        )


    # =====================================================
    # PERFECT
    # =====================================================

    @property
    def is_perfect(self):

        return (
            self.is_completed
            and
            self.total_mistakes == 0
        )


# =========================================================
# USER COURSE
# ПОДТВЕРЖДЁННЫЙ ПЛАН ПРОХОЖДЕНИЯ УРОВНЯ
# =========================================================


class UserCourse(models.Model):

    class Status(models.TextChoices):

        ACTIVE = (
            "active",
            "Active",
        )

        PAUSED = (
            "paused",
            "Paused",
        )

        COMPLETED = (
            "completed",
            "Completed",
        )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="vocabulary_courses",
    )


    level = models.ForeignKey(
        VocabularyLevel,
        on_delete=models.CASCADE,
        related_name="user_courses",
    )


    # =====================================================
    # COURSE DURATION
    # =====================================================

    # Пользователь занимается каждый день.
    #
    # Например:
    #
    # A1 за 60 календарных дней.

    duration_days = models.PositiveIntegerField()


    # =====================================================
    # DATES
    # =====================================================

    start_date = models.DateField(
        default=timezone.localdate,
    )


    # Рассчитывается автоматически:
    #
    # start_date + duration_days - 1

    target_date = models.DateField(
        null=True,
        blank=True,
    )


    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    # =====================================================
    # INITIAL PLAN ESTIMATE
    # =====================================================

    # Среднее количество Lessons,
    # которое нужно проходить в день.
    #
    # Это первоначальная ориентировочная
    # величина.
    #
    # Например:
    #
    # 100 Lessons / 60 дней = 1.67

    estimated_lessons_per_day = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )


    # Предварительная оценка
    # продолжительности одного дня.
    #
    # Позже планировщик сможет
    # корректировать её по реальной
    # скорости пользователя.

    estimated_minutes_per_day = models.PositiveIntegerField(
        default=0,
    )


    # =====================================================
    # STATUS
    # =====================================================

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )


    # UserCourse создаём только ПОСЛЕ того,
    # как пользователь увидел рассчитанный
    # план и нажал:
    #
    # "Подтвердить план"

    confirmed_at = models.DateTimeField(
        default=timezone.now,
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

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "user",
                    "level",
                ],
                name="unique_user_vocabulary_level",
            ),

            models.CheckConstraint(
                condition=models.Q(
                    duration_days__gte=1
                ),
                name="course_duration_days_gte_1",
            ),

        ]


    def save(
        self,
        *args,
        **kwargs,
    ):

        if (
            self.start_date
            and
            self.duration_days
        ):

            self.target_date = (
                self.start_date
                +
                timedelta(
                    days=(
                        self.duration_days
                        -
                        1
                    )
                )
            )

        super().save(
            *args,
            **kwargs,
        )


    def __str__(self):

        return (
            f"{self.user} — "
            f"{self.level.code} — "
            f"{self.duration_days} days"
        )


    # =====================================================
    # COURSE STRUCTURE
    # =====================================================

    @property
    def total_groups(self):

        return (
            VocabularyGroup.objects
            .filter(
                level=self.level,
            )
            .count()
        )


    @property
    def total_lessons(self):

        return (
            VocabularyLesson.objects
            .filter(
                group__level=self.level,
                is_active=True,
            )
            .count()
        )


    @property
    def total_words(self):

        return (
            VocabularyWord.objects
            .filter(
                lesson__group__level=self.level,
                is_active=True,
            )
            .count()
        )


    @property
    def total_group_practices(self):

        # Для каждой группы:
        #
        # Practice 1
        # Practice 2
        # Practice 3
        # Practice 4

        return (
            self.total_groups
            *
            4
        )


    # =====================================================
    # COMPLETED LESSONS
    # =====================================================

    @property
    def completed_lessons(self):

        return (
            LessonPracticeProgress.objects
            .filter(
                user=self.user,
                lesson__group__level=self.level,

                stage1_completed=True,
                stage2_completed=True,
                stage3_completed=True,
                stage4_completed=True,
            )
            .count()
        )


    # =====================================================
    # REMAINING LESSONS
    # =====================================================

    @property
    def remaining_lessons(self):

        return max(
            0,
            (
                self.total_lessons
                -
                self.completed_lessons
            ),
        )


    # =====================================================
    # COMPLETED GROUP PRACTICES
    # =====================================================

    @property
    def completed_group_practices(self):

        return (
            GroupPracticeSession.objects
            .filter(
                user=self.user,
                group__level=self.level,

                practice_number__in=[
                    1,
                    2,
                    3,
                    4,
                ],

                is_completed=True,
            )
            .count()
        )


    # =====================================================
    # REMAINING GROUP PRACTICES
    # =====================================================

    @property
    def remaining_group_practices(self):

        return max(
            0,
            (
                self.total_group_practices
                -
                self.completed_group_practices
            ),
        )


    # =====================================================
    # COMPLETED GROUPS
    # =====================================================

    @property
    def completed_groups(self):

        completed_count = 0


        groups = (
            VocabularyGroup.objects
            .filter(
                level=self.level,
            )
            .order_by(
                "order"
            )
        )


        for group in groups:

            lessons = (
                VocabularyLesson.objects
                .filter(
                    group=group,
                    is_active=True,
                )
            )


            lesson_count = (
                lessons.count()
            )


            completed_lesson_count = (
                LessonPracticeProgress.objects
                .filter(
                    user=self.user,
                    lesson__in=lessons,

                    stage1_completed=True,
                    stage2_completed=True,
                    stage3_completed=True,
                    stage4_completed=True,
                )
                .count()
            )


            practices_completed = (
                GroupPracticeSession.objects
                .filter(
                    user=self.user,
                    group=group,

                    practice_number__in=[
                        1,
                        2,
                        3,
                        4,
                    ],

                    is_completed=True,
                )
                .count()
            )


            if (
                lesson_count > 0
                and
                completed_lesson_count
                ==
                lesson_count
                and
                practices_completed
                ==
                4
            ):

                completed_count += 1


        return completed_count


    # =====================================================
    # COURSE PROGRESS
    # =====================================================

    @property
    def progress_percent(self):

        total = (
            self.total_lessons
            +
            self.total_group_practices
        )


        if total == 0:

            return 0


        completed = (
            self.completed_lessons
            +
            self.completed_group_practices
        )


        return round(
            (
                completed
                /
                total
            )
            *
            100,
            1,
        )


    # =====================================================
    # CURRENT DAY
    # =====================================================

    @property
    def current_day_number(self):

        today = (
            timezone.localdate()
        )


        if (
            today
            <
            self.start_date
        ):

            return 0


        day_number = (
            (
                today
                -
                self.start_date
            ).days
            +
            1
        )


        return min(
            day_number,
            self.duration_days,
        )


    # =====================================================
    # DAYS REMAINING
    # =====================================================

    @property
    def remaining_days(self):

        today = (
            timezone.localdate()
        )


        if (
            not self.target_date
        ):

            return 0


        if (
            today
            >
            self.target_date
        ):

            return 0


        return (
            (
                self.target_date
                -
                today
            ).days
            +
            1
        )


    # =====================================================
    # COURSE FINISHED
    # =====================================================

    @property
    def is_completed(self):

        return (
            self.completed_lessons
            >=
            self.total_lessons
            and
            self.completed_group_practices
            >=
            self.total_group_practices
        )


# =========================================================
# DAILY STUDY PLAN
# ПЛАН КОНКРЕТНОГО КАЛЕНДАРНОГО ДНЯ
# =========================================================


class DailyStudyPlan(models.Model):

    class Status(models.TextChoices):

        PLANNED = (
            "planned",
            "Planned",
        )

        IN_PROGRESS = (
            "in_progress",
            "In progress",
        )

        COMPLETED = (
            "completed",
            "Completed",
        )

        MISSED = (
            "missed",
            "Missed",
        )


    course = models.ForeignKey(
        UserCourse,
        on_delete=models.CASCADE,
        related_name="daily_plans",
    )


    # Пользователь должен заниматься
    # каждый календарный день.

    date = models.DateField()


    # День курса:
    #
    # 1 / 60
    # 2 / 60
    # ...
    # 60 / 60

    day_number = models.PositiveIntegerField(
        default=1,
    )


    # Примерное время сегодняшнего плана.

    estimated_minutes = models.PositiveIntegerField(
        default=0,
    )


    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNED,
    )


    started_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    created_at = models.DateTimeField(
        auto_now_add=True,
    )


    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        ordering = [
            "-date",
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "course",
                    "date",
                ],
                name="unique_daily_plan_per_course",
            ),

            models.CheckConstraint(
                condition=models.Q(
                    day_number__gte=1
                ),
                name="daily_plan_day_number_gte_1",
            ),

        ]


    def __str__(self):

        return (
            f"{self.course.user} — "
            f"{self.course.level.code} — "
            f"Day {self.day_number} — "
            f"{self.date}"
        )


    # =====================================================
    # ITEM COUNT
    # =====================================================

    @property
    def item_count(self):

        return (
            self.items.count()
        )


    # =====================================================
    # COMPLETED ITEMS
    # =====================================================

    @property
    def completed_item_count(self):

        return (
            self.items
            .filter(
                status=(
                    DailyStudyPlanItem
                    .Status
                    .COMPLETED
                )
            )
            .count()
        )


    # =====================================================
    # PROGRESS
    # =====================================================

    @property
    def progress_percent(self):

        total = (
            self.item_count
        )


        if total == 0:

            return 0


        return round(
            (
                self.completed_item_count
                /
                total
            )
            *
            100,
            1,
        )


    # =====================================================
    # COMPLETED
    # =====================================================

    @property
    def is_completed(self):

        return (
            self.status
            ==
            self.Status.COMPLETED
        )


# =========================================================
# DAILY STUDY PLAN ITEM
# ОДНО ЗАДАНИЕ В ПЛАНЕ ДНЯ
# =========================================================


class DailyStudyPlanItem(models.Model):

    class Type(models.TextChoices):

        # Повторение ранее изученных слов.

        REVIEW = (
            "review",
            "Review",
        )


        # Новый или незавершённый Lesson.

        LESSON = (
            "lesson",
            "Lesson",
        )


        # Practice после завершения
        # всех Lessons текущей группы.

        GROUP_PRACTICE = (
            "group_practice",
            "Group Practice",
        )


    class Status(models.TextChoices):

        PLANNED = (
            "planned",
            "Planned",
        )

        IN_PROGRESS = (
            "in_progress",
            "In progress",
        )

        COMPLETED = (
            "completed",
            "Completed",
        )


    plan = models.ForeignKey(
        DailyStudyPlan,
        on_delete=models.CASCADE,
        related_name="items",
    )


    item_type = models.CharField(
        max_length=30,
        choices=Type.choices,
    )


    # =====================================================
    # LESSON
    # =====================================================

    lesson = models.ForeignKey(
        VocabularyLesson,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="daily_plan_items",
    )


    # =====================================================
    # GROUP PRACTICE
    # =====================================================

    group = models.ForeignKey(
        VocabularyGroup,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="daily_plan_items",
    )


    # 1 / 2 / 3 / 4

    practice_number = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )


    # =====================================================
    # REVIEW
    # =====================================================

    # Слова, которые назначены
    # на повторение именно сегодня.

    review_word_ids = models.JSONField(
        default=list,
        blank=True,
    )


    # =====================================================
    # ORDER
    # =====================================================

    # Например:
    #
    # 1. Review
    # 2. Lesson
    # 3. Lesson
    #
    # Или:
    #
    # 1. Review
    # 2. Practice 1
    # 3. Practice 2

    order = models.PositiveSmallIntegerField(
        default=1,
    )


    estimated_minutes = models.PositiveIntegerField(
        default=0,
    )


    # =====================================================
    # STATUS
    # =====================================================

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNED,
    )


    started_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    created_at = models.DateTimeField(
        auto_now_add=True,
    )


    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        ordering = [
            "order",
            "id",
        ]

        constraints = [

            # Если это Practice,
            # его номер может быть только 1–4.
            #
            # Для Lesson и Review practice_number = NULL.

            models.CheckConstraint(
                condition=(
                    models.Q(
                        practice_number__isnull=True
                    )
                    |
                    (
                        models.Q(
                            practice_number__gte=1
                        )
                        &
                        models.Q(
                            practice_number__lte=4
                        )
                    )
                ),
                name="daily_item_practice_number_1_to_4",
            ),

        ]


    def __str__(self):

        if (
            self.item_type
            ==
            self.Type.LESSON
            and
            self.lesson
        ):

            return (
                f"{self.plan.date} — "
                f"Lesson "
                f"{self.lesson.number}"
            )


        if (
            self.item_type
            ==
            self.Type.GROUP_PRACTICE
            and
            self.group
        ):

            return (
                f"{self.plan.date} — "
                f"{self.group.name} — "
                f"Practice "
                f"{self.practice_number}"
            )


        if (
            self.item_type
            ==
            self.Type.REVIEW
        ):

            return (
                f"{self.plan.date} — "
                f"Review — "
                f"{len(self.review_word_ids)} words"
            )


        return (
            f"{self.plan.date} — "
            f"{self.item_type}"
        )