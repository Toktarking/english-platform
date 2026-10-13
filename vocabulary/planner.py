from __future__ import annotations

import math

from collections import defaultdict
from datetime import timedelta
from decimal import Decimal, ROUND_HALF_UP

from django.db import transaction
from django.db.models import Count, Q
from django.utils import timezone

from .models import (
    DailyStudyPlan,
    DailyStudyPlanItem,
    GroupPracticeSession,
    LessonPracticeProgress,
    UserCourse,
    UserWordProgress,
    VocabularyGroup,
    VocabularyLesson,
    VocabularyLevel,
)


# =========================================================
# PLANNER SETTINGS
# =========================================================


# ---------------------------------------------------------
# LESSON
# ---------------------------------------------------------
#
# Lesson состоит из четырёх этапов:
#
# 1. Translation
# 2. Spelling
# 3. Context
# 4. Listening
#
# Поэтому оцениваем длительность Lesson
# по количеству слов.
#
# 80 секунд на одно слово:
#
# 9 слов ≈ 12 минут
# 10 слов ≈ 14 минут
#
# Но Lesson не может оцениваться
# меньше чем в 10 минут.


LESSON_SECONDS_PER_WORD = 80

MIN_LESSON_MINUTES = 10


# ---------------------------------------------------------
# GROUP PRACTICE
# ---------------------------------------------------------
#
# ВАЖНО:
#
# Practice может занимать до 30 минут.
#
# Поэтому при построении плана
# каждый Practice оцениваем именно
# в 30 минут.
#
# Это консервативная оценка,
# чтобы не обещать пользователю
# слишком лёгкий курс.


GROUP_PRACTICE_MINUTES = 30


# ---------------------------------------------------------
# REVIEW
# ---------------------------------------------------------
#
# В среднем одно повторение слова
# оцениваем в 15 секунд.
#
# Review НЕ входит в первоначальную
# длительность курса, потому что
# заранее невозможно знать,
# сколько слов конкретный пользователь
# будет забывать.


REVIEW_SECONDS_PER_WORD = 15


# ---------------------------------------------------------
# MAX DAILY CONTENT
# ---------------------------------------------------------
#
# Если пользователь выбрал слишком
# короткий срок, программа не должна
# автоматически назначать ему,
# например, 4 часа заданий.
#
# 120 минут — верхняя граница
# нового материала + Group Practice.
#
# Review считается отдельно.
#
# При превышении этого значения
# интерфейс сможет показать:
#
# "Выбранный срок слишком интенсивный."


MAX_DAILY_CONTENT_MINUTES = 120


# =========================================================
# BASIC HELPERS
# =========================================================


def validate_duration_days(
    duration_days,
):

    try:

        duration_days = int(
            duration_days
        )

    except (
        TypeError,
        ValueError,
    ):

        raise ValueError(
            "Количество дней должно быть числом."
        )


    if duration_days < 1:

        raise ValueError(
            "Количество дней должно быть больше 0."
        )


    return duration_days


# =========================================================
# LESSON TIME
# =========================================================


def estimate_lesson_minutes(
    lesson,
):
    """
    Оценивает длительность одного Lesson.

    Используем количество активных слов.

    Например:

    10 слов × 80 секунд
    = 800 секунд
    ≈ 14 минут.
    """

    word_count = getattr(
        lesson,
        "active_word_count",
        None,
    )


    if word_count is None:

        word_count = (
            lesson.words
            .filter(
                is_active=True,
            )
            .count()
        )


    if word_count <= 0:

        return MIN_LESSON_MINUTES


    estimated = math.ceil(
        (
            word_count
            *
            LESSON_SECONDS_PER_WORD
        )
        /
        60
    )


    return max(
        MIN_LESSON_MINUTES,
        estimated,
    )


# =========================================================
# REVIEW TIME
# =========================================================


def estimate_review_minutes(
    word_count,
):

    word_count = max(
        0,
        int(
            word_count
            or
            0
        ),
    )


    if word_count == 0:

        return 0


    return max(
        1,
        math.ceil(
            (
                word_count
                *
                REVIEW_SECONDS_PER_WORD
            )
            /
            60
        ),
    )


# =========================================================
# INTENSITY
# =========================================================


def get_intensity(
    minutes_per_day,
):

    if minutes_per_day <= 30:

        return {
            "code": "comfortable",
            "label": "Комфортный",
        }


    if minutes_per_day <= 60:

        return {
            "code": "balanced",
            "label": "Средний",
        }


    if minutes_per_day <= 90:

        return {
            "code": "intensive",
            "label": "Интенсивный",
        }


    return {
        "code": "very_intensive",
        "label": "Очень интенсивный",
    }


# =========================================================
# FULL LEVEL SEQUENCE
# =========================================================


def build_full_level_sequence(
    level,
):
    """
    Полный маршрут уровня.

    ВАЖНО:

    Для каждой группы:

        Lessons
            ↓
        Practice 1
            ↓
        Practice 2
            ↓
        Practice 3
            ↓
        Practice 4
            ↓
        следующая группа

    Таким образом Practice никогда
    не появляется раньше Lessons.
    """

    sequence = []


    groups = (
        VocabularyGroup.objects
        .filter(
            level=level,
        )
        .order_by(
            "order",
        )
    )


    for group in groups:

        lessons = (
            VocabularyLesson.objects
            .filter(
                group=group,
                is_active=True,
            )
            .annotate(
                active_word_count=Count(
                    "words",
                    filter=Q(
                        words__is_active=True
                    ),
                    distinct=True,
                )
            )
            .order_by(
                "order",
            )
        )


        # =================================================
        # LESSONS
        # =================================================

        for lesson in lessons:

            sequence.append(
                {
                    "type":
                        "lesson",

                    "group":
                        group,

                    "lesson":
                        lesson,

                    "estimated_minutes":
                        estimate_lesson_minutes(
                            lesson
                        ),
                }
            )


        # =================================================
        # PRACTICE 1–4
        # =================================================

        for practice_number in [
            1,
            2,
            3,
            4,
        ]:

            sequence.append(
                {
                    "type":
                        "group_practice",

                    "group":
                        group,

                    "practice_number":
                        practice_number,

                    "estimated_minutes":
                        GROUP_PRACTICE_MINUTES,
                }
            )


    return sequence


# =========================================================
# COURSE PREVIEW
# BEFORE USER CONFIRMS PLAN
# =========================================================


def calculate_course_preview(
    level,
    duration_days,
    start_date=None,
):
    """
    Используется ДО создания UserCourse.

    Например пользователь выбрал:

        A1
        60 дней

    Мы показываем ему рассчитанную
    нагрузку, а уже потом он нажимает:

        "Подтвердить план"
    """

    duration_days = (
        validate_duration_days(
            duration_days
        )
    )


    if start_date is None:

        start_date = (
            timezone.localdate()
        )


    sequence = (
        build_full_level_sequence(
            level
        )
    )


    lesson_items = [
        item
        for item in sequence
        if (
            item["type"]
            ==
            "lesson"
        )
    ]


    practice_items = [
        item
        for item in sequence
        if (
            item["type"]
            ==
            "group_practice"
        )
    ]


    total_lesson_minutes = sum(
        item[
            "estimated_minutes"
        ]
        for item in lesson_items
    )


    total_practice_minutes = sum(
        item[
            "estimated_minutes"
        ]
        for item in practice_items
    )


    total_course_minutes = (
        total_lesson_minutes
        +
        total_practice_minutes
    )


    estimated_minutes_per_day = (
        math.ceil(
            total_course_minutes
            /
            duration_days
        )
        if duration_days
        else
        0
    )


    total_lessons = len(
        lesson_items
    )


    total_practices = len(
        practice_items
    )


    total_groups = (
        VocabularyGroup.objects
        .filter(
            level=level,
        )
        .count()
    )


    total_words = (
        level.groups
        .filter(
            lessons__is_active=True,
            lessons__words__is_active=True,
        )
        .values(
            "lessons__words__id"
        )
        .distinct()
        .count()
    )


    estimated_lessons_per_day = (

        Decimal(
            total_lessons
        )
        /
        Decimal(
            duration_days
        )

    ).quantize(
        Decimal(
            "0.01"
        ),
        rounding=ROUND_HALF_UP,
    )


    target_date = (
        start_date
        +
        timedelta(
            days=(
                duration_days
                -
                1
            )
        )
    )


    intensity = (
        get_intensity(
            estimated_minutes_per_day
        )
    )


    required_minimum_days = (
        math.ceil(
            total_course_minutes
            /
            MAX_DAILY_CONTENT_MINUTES
        )
        if total_course_minutes
        else
        1
    )


    is_too_intensive = (
        estimated_minutes_per_day
        >
        MAX_DAILY_CONTENT_MINUTES
    )


    return {

        "level":
            level,

        "level_code":
            level.code,

        "duration_days":
            duration_days,

        "start_date":
            start_date,

        "target_date":
            target_date,


        # =============================================
        # COURSE
        # =============================================

        "total_words":
            total_words,

        "total_groups":
            total_groups,

        "total_lessons":
            total_lessons,

        "total_practices":
            total_practices,


        # =============================================
        # TIME
        # =============================================

        "total_lesson_minutes":
            total_lesson_minutes,

        "total_practice_minutes":
            total_practice_minutes,

        "total_course_minutes":
            total_course_minutes,

        "estimated_minutes_per_day":
            estimated_minutes_per_day,

        "estimated_week_minutes":
            estimated_minutes_per_day
            *
            7,

        "estimated_lessons_per_day":
            estimated_lessons_per_day,


        # =============================================
        # INTENSITY
        # =============================================

        "intensity_code":
            intensity[
                "code"
            ],

        "intensity_label":
            intensity[
                "label"
            ],

        "is_too_intensive":
            is_too_intensive,

        "required_minimum_days":
            required_minimum_days,

    }


# =========================================================
# SERIALIZE TASK
# FOR PREVIEW / TEMPLATE
# =========================================================


def serialize_sequence_item(
    item,
):

    if (
        item["type"]
        ==
        "lesson"
    ):

        lesson = (
            item[
                "lesson"
            ]
        )

        group = (
            item[
                "group"
            ]
        )


        return {

            "type":
                "lesson",

            "title":
                (
                    f"Lesson "
                    f"{lesson.number}"
                ),

            "group_id":
                group.id,

            "group_name":
                group.name,

            "lesson_id":
                lesson.id,

            "lesson_number":
                lesson.number,

            "estimated_minutes":
                item[
                    "estimated_minutes"
                ],
        }


    group = (
        item[
            "group"
        ]
    )


    practice_number = (
        item[
            "practice_number"
        ]
    )


    return {

        "type":
            "group_practice",

        "title":
            (
                f"Practice "
                f"{practice_number}"
            ),

        "group_id":
            group.id,

        "group_name":
            group.name,

        "practice_number":
            practice_number,

        "estimated_minutes":
            item[
                "estimated_minutes"
            ],
    }


# =========================================================
# SELECT TASKS FOR ONE DAY
# =========================================================


def select_tasks_for_budget(
    sequence,
    minute_budget,
):
    """
    Берёт последовательные задания
    до достижения дневной нагрузки.

    ВАЖНО:

    Задания нельзя переставлять.

    Если следующим идёт Practice,
    мы НЕ можем перепрыгнуть через него
    к следующей группе.

    Даже если дневной budget = 20 минут,
    а Practice = 30 минут,
    Practice всё равно назначается целиком.
    """

    selected = []

    total_minutes = 0


    for item in sequence:

        if (
            selected
            and
            total_minutes
            >=
            minute_budget
        ):

            break


        selected.append(
            item
        )


        total_minutes += (
            item[
                "estimated_minutes"
            ]
        )


    return (
        selected,
        total_minutes,
    )


# =========================================================
# REGISTRATION SCHEDULE PREVIEW
# =========================================================


def build_registration_schedule_preview(
    level,
    duration_days,
    preview_days=7,
    start_date=None,
):
    """
    Показывает пользователю пример
    первых дней курса до подтверждения.

    Ничего в базу НЕ сохраняет.
    """

    duration_days = (
        validate_duration_days(
            duration_days
        )
    )


    if start_date is None:

        start_date = (
            timezone.localdate()
        )


    course_preview = (
        calculate_course_preview(
            level=level,
            duration_days=duration_days,
            start_date=start_date,
        )
    )


    sequence = list(
        build_full_level_sequence(
            level
        )
    )


    days = []


    max_preview_days = min(
        preview_days,
        duration_days,
    )


    for day_offset in range(
        max_preview_days
    ):

        if not sequence:

            break


        days_left = max(
            1,
            (
                duration_days
                -
                day_offset
            ),
        )


        remaining_minutes = sum(
            item[
                "estimated_minutes"
            ]
            for item in sequence
        )


        raw_budget = math.ceil(
            remaining_minutes
            /
            days_left
        )


        minute_budget = min(
            raw_budget,
            MAX_DAILY_CONTENT_MINUTES,
        )


        selected, selected_minutes = (
            select_tasks_for_budget(
                sequence=sequence,
                minute_budget=minute_budget,
            )
        )


        selected_count = len(
            selected
        )


        sequence = sequence[
            selected_count:
        ]


        days.append(
            {
                "day_number":
                    day_offset
                    +
                    1,

                "date":
                    start_date
                    +
                    timedelta(
                        days=day_offset
                    ),

                "estimated_minutes":
                    selected_minutes,

                "items":
                    [
                        serialize_sequence_item(
                            item
                        )
                        for item in selected
                    ],
            }
        )


    return {

        "summary":
            course_preview,

        "days":
            days,

    }


# =========================================================
# CREATE CONFIRMED COURSE
# =========================================================


@transaction.atomic
def create_confirmed_course(
    user,
    level,
    duration_days,
    start_date=None,
):
    """
    Вызывается только после:

        "Подтвердить план"
    """

    duration_days = (
        validate_duration_days(
            duration_days
        )
    )


    if start_date is None:

        start_date = (
            timezone.localdate()
        )


    preview = (
        calculate_course_preview(
            level=level,
            duration_days=duration_days,
            start_date=start_date,
        )
    )


    course, created = (
        UserCourse.objects
        .update_or_create(
            user=user,
            level=level,

            defaults={

                "duration_days":
                    duration_days,

                "start_date":
                    start_date,

                "target_date":
                    preview[
                        "target_date"
                    ],

                "estimated_lessons_per_day":
                    preview[
                        "estimated_lessons_per_day"
                    ],

                "estimated_minutes_per_day":
                    preview[
                        "estimated_minutes_per_day"
                    ],

                "status":
                    UserCourse
                    .Status
                    .ACTIVE,

                "confirmed_at":
                    timezone.now(),
            },
        )
    )


    return (
        course,
        created,
        preview,
    )


# =========================================================
# COMPLETION STATE
# =========================================================


def get_course_completion_state(
    course,
):
    """
    Загружает выполненные Lessons
    и Group Practice одним набором данных.
    """

    completed_lesson_ids = set(

        LessonPracticeProgress.objects
        .filter(
            user=course.user,
            lesson__group__level=course.level,

            stage1_completed=True,
            stage2_completed=True,
            stage3_completed=True,
            stage4_completed=True,
        )
        .values_list(
            "lesson_id",
            flat=True,
        )

    )


    completed_practices = defaultdict(
        set
    )


    practice_rows = (
        GroupPracticeSession.objects
        .filter(
            user=course.user,
            group__level=course.level,
            is_completed=True,
            practice_number__in=[
                1,
                2,
                3,
                4,
            ],
        )
        .values_list(
            "group_id",
            "practice_number",
        )
    )


    for (
        group_id,
        practice_number,
    ) in practice_rows:

        completed_practices[
            group_id
        ].add(
            practice_number
        )


    return {
        "completed_lesson_ids":
            completed_lesson_ids,

        "completed_practices":
            completed_practices,
    }


# =========================================================
# REMAINING COURSE SEQUENCE
# =========================================================


def build_remaining_sequence(
    course,
):
    """
    Строит оставшийся маршрут курса.

    Последовательность всегда:

        незавершённые Lessons
        текущей группы
            ↓
        Practice 1
            ↓
        Practice 2
            ↓
        Practice 3
            ↓
        Practice 4
            ↓
        следующая группа

    Практики уже завершённые
    повторно в план не попадают.
    """

    state = (
        get_course_completion_state(
            course
        )
    )


    completed_lesson_ids = (
        state[
            "completed_lesson_ids"
        ]
    )


    completed_practices = (
        state[
            "completed_practices"
        ]
    )


    sequence = []


    groups = (
        VocabularyGroup.objects
        .filter(
            level=course.level,
        )
        .order_by(
            "order",
        )
    )


    for group in groups:

        lessons = list(

            VocabularyLesson.objects
            .filter(
                group=group,
                is_active=True,
            )
            .annotate(
                active_word_count=Count(
                    "words",
                    filter=Q(
                        words__is_active=True
                    ),
                    distinct=True,
                )
            )
            .order_by(
                "order",
            )

        )


        # =================================================
        # REMAINING LESSONS
        # =================================================

        for lesson in lessons:

            if (
                lesson.id
                in
                completed_lesson_ids
            ):

                continue


            sequence.append(
                {
                    "type":
                        "lesson",

                    "group":
                        group,

                    "lesson":
                        lesson,

                    "estimated_minutes":
                        estimate_lesson_minutes(
                            lesson
                        ),
                }
            )


        # =================================================
        # REMAINING PRACTICES
        # =================================================
        #
        # В sequence они идут ПОСЛЕ Lessons.
        #
        # Следовательно даже если сейчас
        # Lessons ещё не закончены,
        # план не сможет поставить Practice
        # раньше них.

        completed_numbers = (
            completed_practices[
                group.id
            ]
        )


        for practice_number in [
            1,
            2,
            3,
            4,
        ]:

            if (
                practice_number
                in
                completed_numbers
            ):

                continue


            sequence.append(
                {
                    "type":
                        "group_practice",

                    "group":
                        group,

                    "practice_number":
                        practice_number,

                    "estimated_minutes":
                        GROUP_PRACTICE_MINUTES,
                }
            )


    return sequence


# =========================================================
# REMAINING COURSE LOAD
# =========================================================


def calculate_remaining_course_load(
    course,
):

    sequence = (
        build_remaining_sequence(
            course
        )
    )


    remaining_minutes = sum(
        item[
            "estimated_minutes"
        ]
        for item in sequence
    )


    remaining_days = max(
        1,
        course.remaining_days,
    )


    required_minutes_per_day = (
        math.ceil(
            remaining_minutes
            /
            remaining_days
        )
        if remaining_minutes
        else
        0
    )


    recommended_extra_days = 0


    if (
        required_minutes_per_day
        >
        MAX_DAILY_CONTENT_MINUTES
    ):

        recommended_days = (
            math.ceil(
                remaining_minutes
                /
                MAX_DAILY_CONTENT_MINUTES
            )
        )


        recommended_extra_days = max(
            0,
            (
                recommended_days
                -
                remaining_days
            ),
        )


    return {

        "remaining_items":
            len(
                sequence
            ),

        "remaining_minutes":
            remaining_minutes,

        "remaining_days":
            course.remaining_days,

        "required_minutes_per_day":
            required_minutes_per_day,

        "is_too_intensive":
            (
                required_minutes_per_day
                >
                MAX_DAILY_CONTENT_MINUTES
            ),

        "recommended_extra_days":
            recommended_extra_days,

    }


# =========================================================
# DUE REVIEW WORDS
# =========================================================


def get_due_review_word_ids(
    course,
):
    """
    Слова, которые уже изучались
    и должны быть повторены сегодня.

    NEW сюда не попадают.
    """

    now = (
        timezone.now()
    )


    return list(

        UserWordProgress.objects
        .filter(
            user=course.user,
            word__lesson__group__level=course.level,
            word__is_active=True,

            next_review__isnull=False,
            next_review__lte=now,
        )
        .exclude(
            status=(
                UserWordProgress
                .Status
                .NEW
            )
        )
        .order_by(
            "next_review",
        )
        .values_list(
            "word_id",
            flat=True,
        )

    )


# =========================================================
# OLD DAILY PLANS
# =========================================================


def mark_old_plans_missed(
    course,
):

    today = (
        timezone.localdate()
    )


    (
        DailyStudyPlan.objects
        .filter(
            course=course,
            date__lt=today,
        )
        .exclude(
            status=(
                DailyStudyPlan
                .Status
                .COMPLETED
            )
        )
        .update(
            status=(
                DailyStudyPlan
                .Status
                .MISSED
            )
        )
    )


# =========================================================
# GENERATE TODAY PLAN
# =========================================================


@transaction.atomic
def get_or_create_today_plan(
    course,
):
    """
    Главная функция ежедневного планировщика.

    Каждый раз, когда пользователь
    заходит на главную страницу:

        get_or_create_today_plan(course)

    Если план уже существует —
    возвращаем его.

    Если нет —
    создаём автоматически.
    """

    today = (
        timezone.localdate()
    )


    # =====================================================
    # OLD DAYS
    # =====================================================

    mark_old_plans_missed(
        course
    )


    # =====================================================
    # EXISTING TODAY PLAN
    # =====================================================

    existing_plan = (

        DailyStudyPlan.objects
        .filter(
            course=course,
            date=today,
        )
        .first()

    )


    if existing_plan:

        sync_daily_plan(
            existing_plan
        )

        return existing_plan


    # =====================================================
    # DAY NUMBER
    # =====================================================

    day_number = max(
        1,
        (
            (
                today
                -
                course.start_date
            ).days
            +
            1
        ),
    )


    # =====================================================
    # COURSE FINISHED
    # =====================================================

    remaining_sequence = (
        build_remaining_sequence(
            course
        )
    )


    due_review_word_ids = (
        get_due_review_word_ids(
            course
        )
    )


    if (
        not remaining_sequence
        and
        not due_review_word_ids
    ):

        plan = (
            DailyStudyPlan.objects
            .create(
                course=course,
                date=today,
                day_number=day_number,
                estimated_minutes=0,

                status=(
                    DailyStudyPlan
                    .Status
                    .COMPLETED
                ),

                completed_at=(
                    timezone.now()
                ),
            )
        )


        if (
            course.status
            !=
            UserCourse
            .Status
            .COMPLETED
        ):

            course.status = (
                UserCourse
                .Status
                .COMPLETED
            )

            course.completed_at = (
                timezone.now()
            )

            course.save(
                update_fields=[
                    "status",
                    "completed_at",
                    "updated_at",
                ]
            )


        return plan


    # =====================================================
    # REMAINING COURSE MINUTES
    # =====================================================

    remaining_minutes = sum(
        item[
            "estimated_minutes"
        ]
        for item in remaining_sequence
    )


    # =====================================================
    # REMAINING DAYS
    # =====================================================

    remaining_days = max(
        1,
        course.remaining_days,
    )


    # =====================================================
    # TODAY CONTENT BUDGET
    # =====================================================

    raw_content_budget = (
        math.ceil(
            remaining_minutes
            /
            remaining_days
        )
        if remaining_minutes
        else
        0
    )


    content_budget = min(
        raw_content_budget,
        MAX_DAILY_CONTENT_MINUTES,
    )


    # =====================================================
    # SELECT CONTENT
    # =====================================================

    selected_content = []

    selected_content_minutes = 0


    if remaining_sequence:

        (
            selected_content,
            selected_content_minutes,
        ) = (
            select_tasks_for_budget(
                sequence=remaining_sequence,
                minute_budget=max(
                    1,
                    content_budget,
                ),
            )
        )


    # =====================================================
    # REVIEW
    # =====================================================

    review_minutes = (
        estimate_review_minutes(
            len(
                due_review_word_ids
            )
        )
    )


    total_estimated_minutes = (
        review_minutes
        +
        selected_content_minutes
    )


    # =====================================================
    # CREATE PLAN
    # =====================================================

    plan = (
        DailyStudyPlan.objects
        .create(
            course=course,
            date=today,
            day_number=day_number,

            estimated_minutes=(
                total_estimated_minutes
            ),

            status=(
                DailyStudyPlan
                .Status
                .PLANNED
            ),
        )
    )


    order = 1


    # =====================================================
    # ITEM 1
    # REVIEW
    # =====================================================

    if due_review_word_ids:

        DailyStudyPlanItem.objects.create(

            plan=plan,

            item_type=(
                DailyStudyPlanItem
                .Type
                .REVIEW
            ),

            review_word_ids=(
                due_review_word_ids
            ),

            order=order,

            estimated_minutes=(
                review_minutes
            ),
        )


        order += 1


    # =====================================================
    # LESSONS / PRACTICES
    # =====================================================

    for item in selected_content:

        if (
            item["type"]
            ==
            "lesson"
        ):

            DailyStudyPlanItem.objects.create(

                plan=plan,

                item_type=(
                    DailyStudyPlanItem
                    .Type
                    .LESSON
                ),

                lesson=(
                    item[
                        "lesson"
                    ]
                ),

                order=order,

                estimated_minutes=(
                    item[
                        "estimated_minutes"
                    ]
                ),
            )


        elif (
            item["type"]
            ==
            "group_practice"
        ):

            DailyStudyPlanItem.objects.create(

                plan=plan,

                item_type=(
                    DailyStudyPlanItem
                    .Type
                    .GROUP_PRACTICE
                ),

                group=(
                    item[
                        "group"
                    ]
                ),

                practice_number=(
                    item[
                        "practice_number"
                    ]
                ),

                order=order,

                estimated_minutes=(
                    item[
                        "estimated_minutes"
                    ]
                ),
            )


        order += 1


    return plan


# =========================================================
# SYNC DAILY PLAN
# =========================================================


@transaction.atomic
def sync_daily_plan(
    plan,
):
    """
    Проверяет фактический прогресс
    пользователя и обновляет статусы
    DailyStudyPlanItem.

    Например пользователь закончил
    Lesson не через кнопку Daily Plan,
    а через обычную страницу Lesson.

    План всё равно поймёт,
    что Lesson уже выполнен.
    """

    now = (
        timezone.now()
    )


    today = (
        timezone.localdate()
    )


    items = list(
        plan.items
        .select_related(
            "lesson",
            "group",
        )
        .all()
    )


    for item in items:

        # =================================================
        # LESSON
        # =================================================

        if (
            item.item_type
            ==
            DailyStudyPlanItem
            .Type
            .LESSON
            and
            item.lesson
        ):

            progress = (

                LessonPracticeProgress.objects
                .filter(
                    user=plan.course.user,
                    lesson=item.lesson,
                )
                .first()

            )


            if (
                progress
                and
                progress.is_completed
            ):

                if (
                    item.status
                    !=
                    DailyStudyPlanItem
                    .Status
                    .COMPLETED
                ):

                    item.status = (
                        DailyStudyPlanItem
                        .Status
                        .COMPLETED
                    )

                    item.completed_at = (
                        progress.completed_at
                        or
                        now
                    )

                    item.save(
                        update_fields=[
                            "status",
                            "completed_at",
                            "updated_at",
                        ]
                    )


            elif (
                progress
                and
                progress.first_opened_at
            ):

                if (
                    item.status
                    ==
                    DailyStudyPlanItem
                    .Status
                    .PLANNED
                ):

                    item.status = (
                        DailyStudyPlanItem
                        .Status
                        .IN_PROGRESS
                    )

                    item.started_at = (
                        progress.first_opened_at
                    )

                    item.save(
                        update_fields=[
                            "status",
                            "started_at",
                            "updated_at",
                        ]
                    )


        # =================================================
        # GROUP PRACTICE
        # =================================================

        elif (
            item.item_type
            ==
            DailyStudyPlanItem
            .Type
            .GROUP_PRACTICE
            and
            item.group
            and
            item.practice_number
        ):

            session = (

                GroupPracticeSession.objects
                .filter(
                    user=plan.course.user,
                    group=item.group,

                    practice_number=(
                        item.practice_number
                    ),
                )
                .first()

            )


            if (
                session
                and
                session.is_completed
            ):

                if (
                    item.status
                    !=
                    DailyStudyPlanItem
                    .Status
                    .COMPLETED
                ):

                    item.status = (
                        DailyStudyPlanItem
                        .Status
                        .COMPLETED
                    )

                    item.completed_at = (
                        session.completed_at
                        or
                        now
                    )

                    item.save(
                        update_fields=[
                            "status",
                            "completed_at",
                            "updated_at",
                        ]
                    )


            elif (
                session
                and
                session.last_opened_at
            ):

                if (
                    item.status
                    ==
                    DailyStudyPlanItem
                    .Status
                    .PLANNED
                ):

                    item.status = (
                        DailyStudyPlanItem
                        .Status
                        .IN_PROGRESS
                    )

                    item.started_at = (
                        session.last_opened_at
                    )

                    item.save(
                        update_fields=[
                            "status",
                            "started_at",
                            "updated_at",
                        ]
                    )


        # =================================================
        # REVIEW
        # =================================================

        elif (
            item.item_type
            ==
            DailyStudyPlanItem
            .Type
            .REVIEW
        ):

            word_ids = (
                item.review_word_ids
                or
                []
            )


            if word_ids:

                completed_reviews = (

                    UserWordProgress.objects
                    .filter(
                        user=plan.course.user,
                        word_id__in=word_ids,

                        last_reviewed_at__gte=(
                            plan.created_at
                        ),
                    )
                    .values(
                        "word_id"
                    )
                    .distinct()
                    .count()

                )


                if (
                    completed_reviews
                    >=
                    len(
                        set(
                            word_ids
                        )
                    )
                ):

                    if (
                        item.status
                        !=
                        DailyStudyPlanItem
                        .Status
                        .COMPLETED
                    ):

                        item.status = (
                            DailyStudyPlanItem
                            .Status
                            .COMPLETED
                        )

                        item.completed_at = (
                            now
                        )

                        item.save(
                            update_fields=[
                                "status",
                                "completed_at",
                                "updated_at",
                            ]
                        )


    # =====================================================
    # REFRESH ITEMS
    # =====================================================

    items = list(
        plan.items.all()
    )


    # =====================================================
    # EMPTY PLAN
    # =====================================================

    if not items:

        plan.status = (
            DailyStudyPlan
            .Status
            .COMPLETED
        )

        plan.completed_at = (
            plan.completed_at
            or
            now
        )

        plan.save(
            update_fields=[
                "status",
                "completed_at",
                "updated_at",
            ]
        )

        return plan


    # =====================================================
    # ALL COMPLETE
    # =====================================================

    all_completed = all(

        item.status
        ==
        DailyStudyPlanItem
        .Status
        .COMPLETED

        for item in items

    )


    if all_completed:

        plan.status = (
            DailyStudyPlan
            .Status
            .COMPLETED
        )

        plan.completed_at = (
            plan.completed_at
            or
            now
        )


        if not plan.started_at:

            plan.started_at = (
                plan.created_at
            )


        plan.save(
            update_fields=[
                "status",
                "started_at",
                "completed_at",
                "updated_at",
            ]
        )


        return plan


    # =====================================================
    # MISSED
    # =====================================================

    if (
        plan.date
        <
        today
    ):

        plan.status = (
            DailyStudyPlan
            .Status
            .MISSED
        )

        plan.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )


        return plan


    # =====================================================
    # IN PROGRESS
    # =====================================================

    has_activity = any(

        item.status
        in [
            DailyStudyPlanItem
            .Status
            .IN_PROGRESS,

            DailyStudyPlanItem
            .Status
            .COMPLETED,
        ]

        for item in items

    )


    if has_activity:

        plan.status = (
            DailyStudyPlan
            .Status
            .IN_PROGRESS
        )


        if not plan.started_at:

            plan.started_at = (
                now
            )


        plan.save(
            update_fields=[
                "status",
                "started_at",
                "updated_at",
            ]
        )


    else:

        plan.status = (
            DailyStudyPlan
            .Status
            .PLANNED
        )

        plan.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )


    return plan


# =========================================================
# WEEK PREVIEW
# =========================================================


def build_week_preview(
    course,
    days=7,
):
    """
    Примерный план ближайших дней.

    НЕ сохраняет будущие DailyStudyPlan.

    Это только прогноз.

    Почему:
    завтра план может измениться,
    если пользователь сегодня:
    - сделал больше;
    - сделал меньше;
    - допустил много ошибок;
    - пропустил занятие.
    """

    days = max(
        1,
        int(
            days
        ),
    )


    today = (
        timezone.localdate()
    )


    sequence = list(
        build_remaining_sequence(
            course
        )
    )


    preview = []


    remaining_calendar_days = max(
        1,
        course.remaining_days,
    )


    max_days = min(
        days,
        remaining_calendar_days,
    )


    for offset in range(
        max_days
    ):

        if not sequence:

            break


        days_left = max(
            1,
            (
                remaining_calendar_days
                -
                offset
            ),
        )


        remaining_minutes = sum(
            item[
                "estimated_minutes"
            ]
            for item in sequence
        )


        raw_budget = (
            math.ceil(
                remaining_minutes
                /
                days_left
            )
        )


        budget = min(
            raw_budget,
            MAX_DAILY_CONTENT_MINUTES,
        )


        selected, minutes = (
            select_tasks_for_budget(
                sequence=sequence,
                minute_budget=budget,
            )
        )


        sequence = sequence[
            len(
                selected
            ):
        ]


        preview.append(
            {
                "date":
                    today
                    +
                    timedelta(
                        days=offset
                    ),

                "day_number":
                    (
                        course.current_day_number
                        +
                        offset
                    ),

                "estimated_content_minutes":
                    minutes,

                "items":
                    [
                        serialize_sequence_item(
                            item
                        )
                        for item in selected
                    ],
            }
        )


    return preview