from collections import defaultdict
from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from vocabulary.models import UserCourse

from .models import (
    GrammarBlock,
    GrammarBlockPracticeProgress,
    GrammarDailyProgress,
    GrammarLesson,
    GrammarLessonProgress,
    GrammarStudyPlan,
    GrammarStudyPlanItem,
)


GRAMMAR_LEVEL = "A1"

PRACTICE_BLOCK_ORDERS = {
    1,
    2,
    3,
}

PRACTICE_ESTIMATED_MINUTES = 20


def get_active_vocabulary_course(user):

    return (
        UserCourse.objects
        .filter(
            user=user,
            status=UserCourse.Status.ACTIVE,
        )
        .order_by(
            "-created_at"
        )
        .first()
    )


def get_active_study_plan(user):

    return (
        GrammarStudyPlan.objects
        .filter(
            user=user,
            status=(
                GrammarStudyPlan
                .Status
                .ACTIVE
            ),
        )
        .order_by(
            "-created_at"
        )
        .first()
    )


def get_published_grammar_lessons(
    level=GRAMMAR_LEVEL,
):

    return (
        GrammarLesson.objects
        .filter(
            level=level,
            is_published=True,
            order__range=(1, 60),
        )
        .select_related(
            "block"
        )
        .order_by(
            "order"
        )
    )


def get_completed_lesson_ids(
    user,
    level=GRAMMAR_LEVEL,
):

    return set(
        GrammarLessonProgress.objects
        .filter(
            user=user,
            lesson__level=level,
            lesson__order__range=(1, 60),
            status=(
                GrammarLessonProgress
                .Status
                .COMPLETED
            ),
        )
        .values_list(
            "lesson_id",
            flat=True,
        )
    )


def get_completed_practice_block_ids(
    user,
    level=GRAMMAR_LEVEL,
):

    return set(
        GrammarBlockPracticeProgress.objects
        .filter(
            user=user,
            block__level=level,
            is_completed=True,
        )
        .values_list(
            "block_id",
            flat=True,
        )
    )


def get_first_incomplete_lesson(
    user,
    level=GRAMMAR_LEVEL,
):

    completed_ids = (
        get_completed_lesson_ids(
            user=user,
            level=level,
        )
    )

    return (
        get_published_grammar_lessons(
            level=level,
        )
        .exclude(
            id__in=completed_ids,
        )
        .first()
    )


def get_required_grammar_step(
    user,
    level=GRAMMAR_LEVEL,
):
    """
    Единая последовательность Grammar:

    Lessons 1-10
    Practice 1

    Lessons 11-20
    Practice 2

    Lessons 21-29
    Practice 3

    Lesson 30...
    """

    completed_lessons = (
        get_completed_lesson_ids(
            user=user,
            level=level,
        )
    )

    completed_practices = (
        get_completed_practice_block_ids(
            user=user,
            level=level,
        )
    )

    blocks = (
        GrammarBlock.objects
        .filter(
            level=level,
            is_published=True,
        )
        .prefetch_related(
            "lessons"
        )
        .order_by(
            "order"
        )
    )

    for block in blocks:

        lessons = list(
            block.lessons
            .filter(
                level=level,
                is_published=True,
            )
            .order_by(
                "order"
            )
        )

        for lesson in lessons:

            if (
                lesson.id
                not in completed_lessons
            ):

                return {
                    "type":
                        "lesson",

                    "lesson":
                        lesson,

                    "block":
                        block,
                }

        if (
            block.order
            in PRACTICE_BLOCK_ORDERS

            and

            block.id
            not in completed_practices
        ):

            return {
                "type":
                    "practice",

                "block":
                    block,
            }

    return {
        "type":
            "complete",
    }


def _date_range(
    start_date,
    end_date,
):

    if end_date < start_date:

        return [
            start_date
        ]

    total_days = (
        end_date
        -
        start_date
    ).days + 1

    return [
        start_date
        +
        timedelta(
            days=index
        )

        for index in range(
            total_days
        )
    ]


def _count_full_remaining_tasks(
    user,
    level=GRAMMAR_LEVEL,
):
    """
    Считает весь оставшийся объём Grammar A1,
    включая временно скрытые Lessons.

    Это нужно, чтобы скрытые Lessons 30–60
    не растягивали готовые Lessons 1–29
    на весь срок курса.
    """

    completed_lessons = (
        get_completed_lesson_ids(
            user=user,
            level=level,
        )
    )

    completed_practices = (
        get_completed_practice_block_ids(
            user=user,
            level=level,
        )
    )


    lesson_count = (
        GrammarLesson.objects
        .filter(
            level=level,
            order__range=(1, 60),
        )
        .exclude(
            id__in=completed_lessons,
        )
        .count()
    )


    practice_count = (
        GrammarBlock.objects
        .filter(
            level=level,
            order__in=PRACTICE_BLOCK_ORDERS,
        )
        .exclude(
            id__in=completed_practices,
        )
        .count()
    )


    return (
        lesson_count
        +
        practice_count
    )


def _spread_tasks_across_dates(
    tasks,
    dates,
    reference_task_count=None,
):

    if not tasks:

        return []

    if not dates:

        dates = [
            timezone.localdate()
        ]


    available_task_count = len(
        tasks
    )


    # ВАЖНО:
    # denominator может учитывать также
    # пока скрытые будущие Lessons.
    #
    # Благодаря этому опубликованные Lessons
    # не растягиваются на весь срок курса.
    total_tasks = max(
        available_task_count,
        reference_task_count
        or available_task_count,
    )


    total_dates = len(
        dates
    )

    result = []


    for index, task in enumerate(
        tasks
    ):

        date_index = int(
            index
            *
            total_dates
            /
            total_tasks
        )

        date_index = min(
            date_index,
            total_dates - 1,
        )


        result.append(
            (
                task,
                dates[
                    date_index
                ],
            )
        )


    return result


def _build_remaining_task_sequence(
    user,
    level=GRAMMAR_LEVEL,
):

    completed_lessons = (
        get_completed_lesson_ids(
            user=user,
            level=level,
        )
    )

    completed_practices = (
        get_completed_practice_block_ids(
            user=user,
            level=level,
        )
    )

    blocks = (
        GrammarBlock.objects
        .filter(
            level=level,
            is_published=True,
        )
        .prefetch_related(
            "lessons"
        )
        .order_by(
            "order"
        )
    )

    sequence = []

    for block in blocks:

        lessons = list(
            block.lessons
            .filter(
                level=level,
                is_published=True,
            )
            .order_by(
                "order"
            )
        )

        for lesson in lessons:

            if (
                lesson.id
                in completed_lessons
            ):
                continue

            sequence.append(
                {
                    "type":
                        "lesson",

                    "lesson":
                        lesson,

                    "block":
                        block,

                    "estimated_minutes":
                        lesson.estimated_minutes,
                }
            )

        if (
            block.order
            in PRACTICE_BLOCK_ORDERS

            and

            block.id
            not in completed_practices

            and

            lessons
        ):

            sequence.append(
                {
                    "type":
                        "practice",

                    "lesson":
                        lessons[-1],

                    "block":
                        block,

                    "estimated_minutes":
                        PRACTICE_ESTIMATED_MINUTES,
                }
            )

    return sequence


@transaction.atomic
def sync_grammar_plan(
    user,
    level=GRAMMAR_LEVEL,
):

    course = (
        get_active_vocabulary_course(
            user
        )
    )

    if course is None:

        return None


    today = (
        timezone.localdate()
    )


    plan = (
        get_active_study_plan(
            user
        )
    )


    if plan is None:

        grammar_start = today

        grammar_target = (
            grammar_start
            +
            timedelta(
                days=max(
                    0,
                    course.duration_days - 1,
                )
            )
        )

        plan = (
            GrammarStudyPlan.objects
            .create(
                user=user,
                start_date=grammar_start,
                exam_date=grammar_target,
                status=(
                    GrammarStudyPlan
                    .Status
                    .ACTIVE
                ),
            )
        )


    if today > plan.exam_date:

        plan.start_date = today

        plan.exam_date = (
            today
            +
            timedelta(
                days=max(
                    0,
                    course.duration_days - 1,
                )
            )
        )

        plan.save(
            update_fields=[
                "start_date",
                "exam_date",
                "updated_at",
            ]
        )


    completed_lessons = (
        get_completed_lesson_ids(
            user=user,
            level=level,
        )
    )

    completed_practices = (
        get_completed_practice_block_ids(
            user=user,
            level=level,
        )
    )


    # =====================================================
    # СОХРАНЯЕМ ЗАВЕРШЁННУЮ ИСТОРИЮ
    # =====================================================

    delete_ids = []

    existing_items = (
        plan.items
        .select_related(
            "lesson",
            "lesson__block",
        )
        .all()
    )


    for item in existing_items:

        if (
            item.action
            ==
            GrammarStudyPlanItem
            .Action
            .FINAL_REVIEW
        ):

            block_id = (
                item.lesson.block_id
            )

            completed = (
                block_id
                in completed_practices
            )

        else:

            completed = (
                item.lesson_id
                in completed_lessons
            )


        if not completed:

            delete_ids.append(
                item.id
            )


    if delete_ids:

        plan.items.filter(
            id__in=delete_ids
        ).delete()


    # =====================================================
    # ОСТАВШИЕСЯ LESSON + PRACTICE
    # =====================================================

    sequence = (
        _build_remaining_task_sequence(
            user=user,
            level=level,
        )
    )


    if not sequence:

        return plan


    dates = (
        _date_range(
            today,
            plan.exam_date,
        )
    )


    full_remaining_task_count = (
        _count_full_remaining_tasks(
            user=user,
            level=level,
        )
    )


    distribution = (
        _spread_tasks_across_dates(
            tasks=sequence,
            dates=dates,
            reference_task_count=(
                full_remaining_task_count
            ),
        )
    )


    plan_items = []


    for position, (
        task,
        scheduled_date,
    ) in enumerate(
        distribution,
        start=1,
    ):

        if (
            task["type"]
            ==
            "practice"
        ):

            action = (
                GrammarStudyPlanItem
                .Action
                .FINAL_REVIEW
            )

        else:

            action = (
                GrammarStudyPlanItem
                .Action
                .LEARN
            )


        plan_items.append(
            GrammarStudyPlanItem(
                plan=plan,

                # Для Practice технически сохраняем
                # последний Lesson блока.
                # Само задание определяется через action.
                lesson=task[
                    "lesson"
                ],

                scheduled_date=
                    scheduled_date,

                action=action,

                order=position,
            )
        )


    GrammarStudyPlanItem.objects.bulk_create(
        plan_items
    )


    return plan


def _serialize_plan_item(
    item,
    completed_lessons,
    completed_practices,
    required_step,
):

    if (
        item.action
        ==
        GrammarStudyPlanItem
        .Action
        .FINAL_REVIEW
    ):

        block = (
            item.lesson.block
        )

        completed = (
            block.id
            in completed_practices
        )

        is_next = (
            required_step[
                "type"
            ]
            ==
            "practice"

            and

            required_step[
                "block"
            ].id
            ==
            block.id
        )

        question_count = (
            18
            if block.order == 3
            else 20
        )

        return {
            "type":
                "practice",

            "item":
                item,

            "block":
                block,

            "completed":
                completed,

            "is_next":
                is_next,

            "locked":
                (
                    not completed
                    and
                    not is_next
                ),

            "estimated_minutes":
                PRACTICE_ESTIMATED_MINUTES,

            "question_count":
                question_count,
        }


    lesson = (
        item.lesson
    )

    completed = (
        lesson.id
        in completed_lessons
    )

    is_next = (
        required_step[
            "type"
        ]
        ==
        "lesson"

        and

        required_step[
            "lesson"
        ].id
        ==
        lesson.id
    )


    return {
        "type":
            "lesson",

        "item":
            item,

        "lesson":
            lesson,

        "block":
            lesson.block,

        "completed":
            completed,

        "is_next":
            is_next,

        "locked":
            (
                not completed
                and
                not is_next
            ),

        "estimated_minutes":
            lesson.estimated_minutes,
    }



def update_grammar_daily_progress(
    user,
    target_date=None,
):
    """
    День Grammar считается завершённым
    только если выполнены ВСЕ задания,
    запланированные на этот день.

    Vocabulary здесь никак не учитывается.
    """

    if target_date is None:

        target_date = (
            timezone.localdate()
        )


    plan = (
        get_active_study_plan(
            user
        )
    )


    if plan is None:

        return None


    items = list(
        plan.items
        .filter(
            scheduled_date=target_date,
        )
        .select_related(
            "lesson",
            "lesson__block",
        )
        .order_by(
            "order"
        )
    )


    if not items:

        return None


    completed_lessons = (
        get_completed_lesson_ids(
            user=user,
        )
    )


    completed_practices = (
        get_completed_practice_block_ids(
            user=user,
        )
    )


    completed_count = 0


    for item in items:

        if (
            item.action
            ==
            GrammarStudyPlanItem
            .Action
            .FINAL_REVIEW
        ):

            is_done = (
                item.lesson.block_id
                in completed_practices
            )

        else:

            is_done = (
                item.lesson_id
                in completed_lessons
            )


        if is_done:

            completed_count += 1


    required_count = len(
        items
    )


    all_done = (
        required_count > 0

        and

        completed_count
        ==
        required_count
    )


    progress, _ = (
        GrammarDailyProgress.objects
        .get_or_create(
            user=user,
            date=target_date,
            defaults={
                "required_count":
                    required_count,

                "completed_count":
                    completed_count,

                "is_completed":
                    all_done,

                "completed_at":
                    (
                        timezone.now()
                        if all_done
                        else None
                    ),
            },
        )
    )


    progress.required_count = (
        required_count
    )

    progress.completed_count = (
        completed_count
    )


    # Уже закрытый день назад не откатываем.
    if (
        all_done
        and
        not progress.is_completed
    ):

        progress.is_completed = True

        progress.completed_at = (
            timezone.now()
        )


    progress.save(
        update_fields=[
            "required_count",
            "completed_count",
            "is_completed",
            "completed_at",
            "updated_at",
        ]
    )


    return progress



def get_today_grammar_rows(
    plan,
):

    if plan is None:

        return []


    completed_lessons = (
        get_completed_lesson_ids(
            user=plan.user,
        )
    )

    completed_practices = (
        get_completed_practice_block_ids(
            user=plan.user,
        )
    )

    required_step = (
        get_required_grammar_step(
            plan.user
        )
    )


    items = (
        plan.items
        .filter(
            scheduled_date=(
                timezone.localdate()
            ),
        )
        .select_related(
            "lesson",
            "lesson__block",
        )
        .order_by(
            "order"
        )
    )


    return [
        _serialize_plan_item(
            item=item,
            completed_lessons=
                completed_lessons,
            completed_practices=
                completed_practices,
            required_step=
                required_step,
        )

        for item in items
    ]


def get_grammar_calendar(
    plan,
):

    if plan is None:

        return []


    today = (
        timezone.localdate()
    )


    completed_lessons = (
        get_completed_lesson_ids(
            user=plan.user,
        )
    )

    completed_practices = (
        get_completed_practice_block_ids(
            user=plan.user,
        )
    )

    required_step = (
        get_required_grammar_step(
            plan.user
        )
    )


    dates = (
        _date_range(
            plan.start_date,
            max(
                plan.exam_date,
                today,
            ),
        )
    )


    items_by_date = defaultdict(
        list
    )


    items = (
        plan.items
        .select_related(
            "lesson",
            "lesson__block",
        )
        .order_by(
            "scheduled_date",
            "order",
        )
    )


    for item in items:

        items_by_date[
            item.scheduled_date
        ].append(
            item
        )


    calendar = []


    for index, current_date in enumerate(
        dates,
        start=1,
    ):

        rows = []

        estimated_minutes = 0


        for item in items_by_date[
            current_date
        ]:

            row = (
                _serialize_plan_item(
                    item=item,
                    completed_lessons=
                        completed_lessons,
                    completed_practices=
                        completed_practices,
                    required_step=
                        required_step,
                )
            )

            rows.append(
                row
            )

            estimated_minutes += (
                row[
                    "estimated_minutes"
                ]
            )


        total_count = len(
            rows
        )


        completed_count = sum(
            1

            for row in rows

            if row[
                "completed"
            ]
        )


        if total_count == 0:

            status = "REST"

        elif (
            completed_count
            ==
            total_count
        ):

            status = "COMPLETED"

        elif current_date == today:

            status = "TODAY"

        elif current_date < today:

            status = "MISSED"

        else:

            status = "UPCOMING"


        calendar.append(
            {
                "date":
                    current_date,

                "day_number":
                    index,

                "items":
                    rows,

                "status":
                    status,

                "is_today":
                    (
                        current_date
                        ==
                        today
                    ),

                "total_count":
                    total_count,

                "completed_count":
                    completed_count,

                "estimated_minutes":
                    estimated_minutes,
            }
        )


    return calendar
