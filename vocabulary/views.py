import json
import random

from datetime import timedelta

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import (
    CourseSetupForm,
    RegistrationForm,
)

from .models import (
    DailyStudyPlan,
    DailyStudyPlanItem,
    GroupPracticeSession,
    GroupPracticeWordState,
    LessonPracticeProgress,
    UserCourse,
    UserWordProgress,
    VocabularyGroup,
    VocabularyLesson,
    VocabularyLevel,
    VocabularyWord,
)

from .planner import (
    build_registration_schedule_preview,
    build_remaining_sequence,
    calculate_course_preview,
    create_confirmed_course,
    get_or_create_today_plan,
    sync_daily_plan,
)

# =========================================================
# REGISTER
# =========================================================


def register_view(
    request,
):

    # =====================================================
    # ALREADY LOGGED IN
    # =====================================================

    if request.user.is_authenticated:

        has_course = (
            UserCourse.objects
            .filter(
                user=request.user,
            )
            .exists()
        )


        if has_course:

            return redirect(
                "vocabulary:home"
            )


        return redirect(
            "vocabulary:course_setup"
        )


    # =====================================================
    # POST
    # =====================================================

    if request.method == "POST":

        form = RegistrationForm(
            request.POST
        )


        if form.is_valid():

            user = (
                form.save()
            )


            login(
                request,
                user,
            )


            # После регистрации пользователь
            # ОБЯЗАТЕЛЬНО настраивает курс.

            return redirect(
                "vocabulary:course_setup"
            )


    # =====================================================
    # GET
    # =====================================================

    else:

        form = (
            RegistrationForm()
        )


    return render(
        request,
        "registration/register.html",
        {
            "form":
                form,
        },
    )


# =========================================================
# COURSE SETUP
# =========================================================


@login_required
def course_setup(
    request,
):
    """
    Первый экран после регистрации.

    Пользователь выбирает:

    - уровень;
    - за сколько календарных дней
      он хочет пройти уровень.

    Пока UserCourse НЕ создаётся.
    """


    # =====================================================
    # EXISTING COURSE
    # =====================================================

    existing_course = (
        UserCourse.objects
        .filter(
            user=request.user,
        )
        .select_related(
            "level",
        )
        .first()
    )


    initial = {}


    if existing_course:

        initial = {

            "level":
                existing_course.level,

            "duration_days":
                existing_course.duration_days,

        }

    else:

        # Если есть A1,
        # выбираем его автоматически.

        a1 = (
            VocabularyLevel.objects
            .filter(
                code__iexact="A1",
                is_active=True,
            )
            .first()
        )


        if a1:

            initial[
                "level"
            ] = a1


        initial[
            "duration_days"
        ] = 60


    # =====================================================
    # POST
    # =====================================================

    if request.method == "POST":

        form = CourseSetupForm(
            request.POST
        )


        if form.is_valid():

            level = (
                form.cleaned_data[
                    "level"
                ]
            )


            duration_days = (
                form.cleaned_data[
                    "duration_days"
                ]
            )


            # ---------------------------------------------
            # Сохраняем пока только во временную session.
            #
            # UserCourse здесь ещё НЕ создаётся.
            # ---------------------------------------------

            request.session[
                "course_setup_level_id"
            ] = level.id


            request.session[
                "course_setup_duration_days"
            ] = duration_days


            return redirect(
                "vocabulary:course_preview"
            )


    # =====================================================
    # GET
    # =====================================================

    else:

        form = CourseSetupForm(
            initial=initial
        )


    return render(
        request,
        "vocabulary/course_setup.html",
        {

            "form":
                form,

            "existing_course":
                existing_course,

        },
    )


# =========================================================
# COURSE PREVIEW
# =========================================================


@login_required
def course_preview(
    request,
):
    """
    Показывает рассчитанный план ДО подтверждения.

    Здесь UserCourse всё ещё
    не создаётся.
    """


    level_id = (
        request.session.get(
            "course_setup_level_id"
        )
    )


    duration_days = (
        request.session.get(
            "course_setup_duration_days"
        )
    )


    if (
        not level_id
        or
        not duration_days
    ):

        return redirect(
            "vocabulary:course_setup"
        )


    level = get_object_or_404(
        VocabularyLevel,
        id=level_id,
        is_active=True,
    )


    # =====================================================
    # SUMMARY
    # =====================================================

    preview = (
        calculate_course_preview(
            level=level,
            duration_days=duration_days,
        )
    )


    # =====================================================
    # FIRST DAYS PREVIEW
    # =====================================================

    schedule_preview = (
        build_registration_schedule_preview(
            level=level,
            duration_days=duration_days,
            preview_days=7,
        )
    )


    return render(
        request,
        "vocabulary/course_preview.html",
        {

            "level":
                level,

            "preview":
                preview,

            "schedule_days":
                schedule_preview[
                    "days"
                ],

        },
    )


# =========================================================
# COURSE CONFIRM
# =========================================================


@login_required
@require_POST
def course_confirm(
    request,
):
    """
    Только здесь создаётся UserCourse.
    """


    level_id = (
        request.session.get(
            "course_setup_level_id"
        )
    )


    duration_days = (
        request.session.get(
            "course_setup_duration_days"
        )
    )


    if (
        not level_id
        or
        not duration_days
    ):

        return redirect(
            "vocabulary:course_setup"
        )


    level = get_object_or_404(
        VocabularyLevel,
        id=level_id,
        is_active=True,
    )


    # =====================================================
    # CREATE COURSE
    # =====================================================

    (
        course,
        created,
        preview,
    ) = (
        create_confirmed_course(
            user=request.user,
            level=level,
            duration_days=duration_days,
        )
    )


    # =====================================================
    # CLEAR TEMPORARY SESSION
    # =====================================================

    request.session.pop(
        "course_setup_level_id",
        None,
    )


    request.session.pop(
        "course_setup_duration_days",
        None,
    )


    # Пока Daily Dashboard ещё не сделан,
    # после подтверждения отправляем
    # на страницу уровня.

    return redirect(
        "vocabulary:dashboard",
    )



# =========================================================
# ACTIVE COURSE
# =========================================================


def get_active_user_course(
    user,
):

    return (
        UserCourse.objects
        .filter(
            user=user,
            status=UserCourse.Status.ACTIVE,
        )
        .select_related(
            "level",
        )
        .first()
    )


# =========================================================
# DAILY ITEM URL
# =========================================================


def get_daily_item_url(
    item,
):

    # =====================================================
    # REVIEW
    # =====================================================

    if (
        item.item_type
        ==
        DailyStudyPlanItem.Type.REVIEW
    ):

        return reverse(
            "vocabulary:daily_review"
        )


    # =====================================================
    # LESSON
    # =====================================================

    if (
        item.item_type
        ==
        DailyStudyPlanItem.Type.LESSON
        and
        item.lesson
    ):

        return reverse(
            "vocabulary:lesson_detail",
            kwargs={
                "level_code":
                    item.lesson.group.level.code,

                "lesson_id":
                    item.lesson.id,
            },
        )


    # =====================================================
    # GROUP PRACTICE
    # =====================================================

    if (
        item.item_type
        ==
        DailyStudyPlanItem.Type.GROUP_PRACTICE
        and
        item.group
        and
        item.practice_number
    ):

        practice_urls = {

            1:
                "vocabulary:group_practice1",

            2:
                "vocabulary:group_practice2",

            3:
                "vocabulary:group_practice3",

            4:
                "vocabulary:group_practice4",

        }


        url_name = (
            practice_urls.get(
                item.practice_number
            )
        )


        if url_name:

            return reverse(
                url_name,
                kwargs={
                    "level_code":
                        item.group.level.code,

                    "group_id":
                        item.group.id,
                },
            )


    return reverse(
        "vocabulary:dashboard"
    )


# =========================================================
# STREAK
# =========================================================


def calculate_course_streak(
    course,
):

    today = (
        timezone.localdate()
    )


    completed_dates = set(

        DailyStudyPlan.objects
        .filter(
            course=course,
            status=(
                DailyStudyPlan
                .Status
                .COMPLETED
            ),
            date__lte=today,
        )
        .values_list(
            "date",
            flat=True,
        )

    )


    cursor = today


    # Если сегодняшний план ещё
    # не завершён, серия считается
    # до вчерашнего дня.

    if (
        cursor
        not in
        completed_dates
    ):

        cursor = (
            cursor
            -
            timedelta(
                days=1
            )
        )


    streak = 0


    while (
        cursor
        in
        completed_dates
    ):

        streak += 1

        cursor = (
            cursor
            -
            timedelta(
                days=1
            )
        )


    return streak


# =========================================================
# DASHBOARD
# =========================================================


@login_required
def dashboard(
    request,
):

    course = (
        get_active_user_course(
            request.user
        )
    )


    # =====================================================
    # NO ACTIVE COURSE
    # =====================================================

    if not course:

        return redirect(
            "vocabulary:course_setup"
        )


    # =====================================================
    # TODAY PLAN
    # =====================================================

    today_plan = (
        get_or_create_today_plan(
            course
        )
    )


    today_plan = (
        sync_daily_plan(
            today_plan
        )
    )


    # =====================================================
    # TODAY ITEMS
    # =====================================================

    plan_items = list(

        today_plan.items
        .select_related(
            "lesson",
            "lesson__group",
            "lesson__group__level",
            "group",
            "group__level",
        )
        .order_by(
            "order",
        )

    )


    dashboard_items = []


    for item in plan_items:

        item_data = {

            "id":
                item.id,

            "type":
                item.item_type,

            "status":
                item.status,

            "estimated_minutes":
                item.estimated_minutes,

            "url":
                get_daily_item_url(
                    item
                ),

        }


        # =================================================
        # REVIEW
        # =================================================

        if (
            item.item_type
            ==
            DailyStudyPlanItem.Type.REVIEW
        ):

            item_data.update(
                {

                    "icon":
                        "↻",

                    "title":
                        "Повторение слов",

                    "description":
                        (
                            f"{len(item.review_word_ids)} "
                            f"слов"
                        ),

                }
            )


        # =================================================
        # LESSON
        # =================================================

        elif (
            item.item_type
            ==
            DailyStudyPlanItem.Type.LESSON
            and
            item.lesson
        ):

            word_count = (
                item.lesson.words
                .filter(
                    is_active=True,
                )
                .count()
            )


            item_data.update(
                {

                    "icon":
                        "A",

                    "title":
                        (
                            f"Lesson "
                            f"{item.lesson.number}"
                        ),

                    "description":
                        (
                            f"{item.lesson.group.name}"
                            f" · "
                            f"{word_count} слов"
                            f" · "
                            f"4 этапа"
                        ),

                }
            )


        # =================================================
        # PRACTICE
        # =================================================

        elif (
            item.item_type
            ==
            DailyStudyPlanItem
            .Type
            .GROUP_PRACTICE
            and
            item.group
        ):

            practice_names = {

                1:
                    "Карточки",

                2:
                    "Выбор перевода",

                3:
                    "Соберите слово",

                4:
                    "Listening",

            }


            item_data.update(
                {

                    "icon":
                        "P",

                    "title":
                        (
                            f"Practice "
                            f"{item.practice_number}"
                        ),

                    "description":
                        (
                            f"{item.group.name}"
                            f" · "
                            f"{practice_names.get(item.practice_number, '')}"
                        ),

                }
            )


        dashboard_items.append(
            item_data
        )


    # =====================================================
    # NEXT ITEM
    # =====================================================

    next_item = None


    for item in plan_items:

        if (
            item.status
            !=
            DailyStudyPlanItem
            .Status
            .COMPLETED
        ):

            next_item = item

            break


    next_url = (
        get_daily_item_url(
            next_item
        )
        if next_item
        else None
    )


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

        for item in plan_items

    )


    # =====================================================
    # CURRENT GROUP
    # =====================================================

    remaining_sequence = (
        build_remaining_sequence(
            course
        )
    )


    current_group = None


    if remaining_sequence:

        current_group = (
            remaining_sequence[
                0
            ][
                "group"
            ]
        )


    current_group_data = None


    if current_group:

        group_lessons = (
            VocabularyLesson.objects
            .filter(
                group=current_group,
                is_active=True,
            )
        )


        group_total_lessons = (
            group_lessons.count()
        )


        group_completed_lessons = (

            LessonPracticeProgress.objects
            .filter(
                user=request.user,
                lesson__group=current_group,

                stage1_completed=True,
                stage2_completed=True,
                stage3_completed=True,
                stage4_completed=True,
            )
            .count()

        )


        group_completed_practices = (

            GroupPracticeSession.objects
            .filter(
                user=request.user,
                group=current_group,
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


        group_total_items = (
            group_total_lessons
            +
            4
        )


        group_completed_items = (
            group_completed_lessons
            +
            group_completed_practices
        )


        group_percent = (

            round(
                (
                    group_completed_items
                    /
                    group_total_items
                )
                *
                100
            )

            if group_total_items

            else 0
        )


        current_group_data = {

            "name":
                current_group.name,

            "completed_lessons":
                group_completed_lessons,

            "total_lessons":
                group_total_lessons,

            "completed_practices":
                group_completed_practices,

            "practices_unlocked":
                (
                    group_total_lessons > 0
                    and
                    group_completed_lessons
                    >=
                    group_total_lessons
                ),

            "progress_percent":
                group_percent,

        }


    # =====================================================
    # WORD PROGRESS
    # =====================================================

    studied_words = (

        UserWordProgress.objects
        .filter(
            user=request.user,
            word__lesson__group__level=(
                course.level
            ),
        )
        .exclude(
            status=(
                UserWordProgress
                .Status
                .NEW
            )
        )
        .values(
            "word_id"
        )
        .distinct()
        .count()

    )


    mastered_words = (

        UserWordProgress.objects
        .filter(
            user=request.user,
            word__lesson__group__level=(
                course.level
            ),
            status=(
                UserWordProgress
                .Status
                .MASTERED
            ),
        )
        .values(
            "word_id"
        )
        .distinct()
        .count()

    )


    # =====================================================
    # WEEK
    # =====================================================

    today = (
        timezone.localdate()
    )


    week_start = (
        today
        -
        timedelta(
            days=today.weekday()
        )
    )


    week_end = (
        week_start
        +
        timedelta(
            days=6
        )
    )


    saved_week_plans = {

        plan.date:
            plan

        for plan in (

            DailyStudyPlan.objects
            .filter(
                course=course,
                date__range=[
                    week_start,
                    week_end,
                ],
            )

        )

    }


    day_names = [
        "Пн",
        "Вт",
        "Ср",
        "Чт",
        "Пт",
        "Сб",
        "Вс",
    ]


    week_days = []


    week_completed = 0


    for index in range(
        7
    ):

        date = (
            week_start
            +
            timedelta(
                days=index
            )
        )


        saved_plan = (
            saved_week_plans.get(
                date
            )
        )


        status = "future"


        if (
            saved_plan
            and
            saved_plan.status
            ==
            DailyStudyPlan
            .Status
            .COMPLETED
        ):

            status = "completed"

            week_completed += 1


        elif date == today:

            status = "today"


        elif date < today:

            status = "missed"


        week_days.append(
            {

                "name":
                    day_names[
                        index
                    ],

                "date":
                    date,

                "status":
                    status,

            }
        )


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "course":
            course,

        "today_plan":
            today_plan,

        "dashboard_items":
            dashboard_items,

        "next_url":
            next_url,

        "has_activity":
            has_activity,

        "current_group":
            current_group_data,

        "studied_words":
            studied_words,

        "mastered_words":
            mastered_words,

        "streak":
            calculate_course_streak(
                course
            ),

        "week_days":
            week_days,

        "week_completed":
            week_completed,

        "today":
            today,

    }


    return render(
        request,
        "vocabulary/dashboard.html",
        context,
    )


# =========================================================
# START / CONTINUE TODAY
# =========================================================


@login_required
def dashboard_start(
    request,
):

    course = (
        get_active_user_course(
            request.user
        )
    )


    if not course:

        return redirect(
            "vocabulary:course_setup"
        )


    plan = (
        get_or_create_today_plan(
            course
        )
    )


    plan = (
        sync_daily_plan(
            plan
        )
    )


    next_item = (

        plan.items
        .exclude(
            status=(
                DailyStudyPlanItem
                .Status
                .COMPLETED
            )
        )
        .select_related(
            "lesson",
            "lesson__group",
            "lesson__group__level",
            "group",
            "group__level",
        )
        .order_by(
            "order",
        )
        .first()

    )


    if not next_item:

        return redirect(
            "vocabulary:dashboard"
        )


    return redirect(
        get_daily_item_url(
            next_item
        )
    )

# =========================================================
# VOCABULARY HOME
# =========================================================

def vocabulary_home(
    request,
):

    if request.user.is_authenticated:

        course = (
            UserCourse.objects
            .filter(
                user=request.user,
                status=(
                    UserCourse
                    .Status
                    .ACTIVE
                ),
            )
            .first()
        )


        if course:

            return redirect(
                "vocabulary:dashboard"
            )


        return redirect(
            "vocabulary:course_setup"
        )


    levels = (
        VocabularyLevel.objects
        .filter(
            is_active=True,
        )
        .annotate(
            group_count=Count(
                "groups",
                distinct=True,
            ),
            lesson_count=Count(
                "groups__lessons",
                distinct=True,
            ),
            word_count=Count(
                "groups__lessons__words",
                distinct=True,
            ),
        )
        .order_by(
            "order",
        )
    )


    return render(
        request,
        "vocabulary/home.html",
        {
            "levels":
                levels,
        },
    )

# =========================================================
# LEVEL
# =========================================================
# =========================================================
# LEVEL
# =========================================================




def level_detail(
    request,
    level_code,
):

    # =====================================================
    # ACTIVE COURSE USER
    # =====================================================
    #
    # Пользователь с активным курсом
    # не должен видеть каталог групп.
    # Его главный экран — Dashboard.

    if request.user.is_authenticated:

        active_course = (
            get_active_user_course(
                request.user
            )
        )

        if active_course:

            return redirect(
                "vocabulary:dashboard"
            )


    # =====================================================
    # LEVEL
    # =====================================================

    level = get_object_or_404(
        VocabularyLevel,
        code__iexact=level_code,
        is_active=True,
    )


    groups = (
        VocabularyGroup.objects
        .filter(
            level=level
        )
        .annotate(
            lesson_count=Count(
                "lessons",
                distinct=True,
            ),
            word_count=Count(
                "lessons__words",
                distinct=True,
            ),
        )
        .order_by(
            "order"
        )
    )


    total_words = sum(
        group.word_count
        for group in groups
    )


    total_lessons = sum(
        group.lesson_count
        for group in groups
    )


    context = {

        "level":
            level,

        "groups":
            groups,

        "total_words":
            total_words,

        "total_lessons":
            total_lessons,

    }


    return render(
        request,
        "vocabulary/level_detail.html",
        context,
    )

# =========================================================
# PRACTICE CARD DATA
# =========================================================


def get_practice_card_data(
    user,
    group,
    practice_number,
    total_words,
):

    data = {
        "number":
            practice_number,

        "started":
            False,

        "completed":
            False,

        "opened_count":
            0,

        "unopened_count":
            total_words,

        "deck1_count":
            0,

        "deck2_count":
            0,

        "deck3_count":
            0,

        "mistake_count":
            0,

        "last_opened_at":
            None,

        "completed_at":
            None,
    }

    if not user.is_authenticated:
        return data

    session = (
        GroupPracticeSession.objects
        .filter(
            user=user,
            group=group,
            practice_number=practice_number,
        )
        .first()
    )

    if not session:
        return data

    data["started"] = True

    data["completed"] = (
        session.is_completed
    )

    data["mistake_count"] = (
        session.mistake_count
    )

    data["last_opened_at"] = (
        session.last_opened_at
    )

    data["completed_at"] = (
        session.completed_at
    )

    deck_counts = {
        GroupPracticeWordState
        .Deck
        .UNOPENED:
            0,

        GroupPracticeWordState
        .Deck
        .DECK_1:
            0,

        GroupPracticeWordState
        .Deck
        .DECK_2:
            0,

        GroupPracticeWordState
        .Deck
        .DECK_3:
            0,
    }

    states = (
        session.word_states
        .values(
            "deck"
        )
        .annotate(
            count=Count(
                "id"
            )
        )
    )

    for state in states:

        deck_counts[
            state["deck"]
        ] = state["count"]

    unopened_count = (
        deck_counts[
            GroupPracticeWordState
            .Deck
            .UNOPENED
        ]
    )

    deck1_count = (
        deck_counts[
            GroupPracticeWordState
            .Deck
            .DECK_1
        ]
    )

    deck2_count = (
        deck_counts[
            GroupPracticeWordState
            .Deck
            .DECK_2
        ]
    )

    deck3_count = (
        deck_counts[
            GroupPracticeWordState
            .Deck
            .DECK_3
        ]
    )

    opened_count = (
        deck1_count
        +
        deck2_count
        +
        deck3_count
    )

    data.update(
        {
            "opened_count":
                opened_count,

            "unopened_count":
                unopened_count,

            "deck1_count":
                deck1_count,

            "deck2_count":
                deck2_count,

            "deck3_count":
                deck3_count,
        }
    )

    return data


# =========================================================
# GROUP
# =========================================================


def group_detail(
    request,
    level_code,
    group_id,
):

    # =====================================================
    # ACTIVE COURSE USER
    # =====================================================

    if request.user.is_authenticated:

        active_course = (
            get_active_user_course(
                request.user
            )
        )

        if active_course:

            return redirect(
                "vocabulary:dashboard"
            )


    level = get_object_or_404(
        VocabularyLevel,
        code__iexact=level_code,
        is_active=True,
    )

    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
        level=level,
    )

    lessons = list(
        group.lessons
        .filter(
            is_active=True
        )
        .annotate(
            word_count=Count(
                "words",
                distinct=True,
            )
        )
        .order_by(
            "order"
        )
    )

    total_words = sum(
        lesson.word_count
        for lesson in lessons
    )


    # =====================================================
    # GROUP PRACTICE CARDS
    # =====================================================

    practice_cards = []

    for practice_number in (
        1,
        2,
        3,
        4,
    ):

        practice_cards.append(
            get_practice_card_data(
                user=request.user,
                group=group,
                practice_number=practice_number,
                total_words=total_words,
            )
        )


    # =====================================================
    # LESSON PROGRESS
    # =====================================================

    progress_map = {}

    if request.user.is_authenticated:

        progress_records = (
            LessonPracticeProgress.objects
            .filter(
                user=request.user,
                lesson__group=group,
            )
        )

        progress_map = {
            progress.lesson_id:
                progress

            for progress
            in progress_records
        }


    for lesson in lessons:

        progress = progress_map.get(
            lesson.id
        )


        # =============================================
        # NEVER OPENED
        # =============================================

        if progress is None:

            lesson.practice_status = (
                "unopened"
            )

            lesson.practice_progress = (
                None
            )

            continue


        # =============================================
        # STATUS
        # =============================================

        if progress.is_perfect:

            status = (
                "perfect"
            )

        elif progress.is_completed:

            status = (
                "completed"
            )

        else:

            status = (
                "started"
            )


        lesson.practice_status = (
            status
        )


        lesson.practice_progress = {

            # =========================================
            # STAGE 1
            # =========================================

            "stage1_completed":
                progress.stage1_completed,

            "stage1_mistakes":
                progress.stage1_mistakes,

            "stage1_seconds":
                progress.stage1_seconds,


            # =========================================
            # STAGE 2
            # =========================================

            "stage2_completed":
                progress.stage2_completed,

            "stage2_mistakes":
                progress.stage2_mistakes,

            "stage2_seconds":
                progress.stage2_seconds,


            # =========================================
            # STAGE 3
            # =========================================

            "stage3_completed":
                progress.stage3_completed,

            "stage3_mistakes":
                progress.stage3_mistakes,

            "stage3_seconds":
                progress.stage3_seconds,


            # =========================================
            # STAGE 4
            # LISTENING
            # =========================================

            "stage4_completed":
                progress.stage4_completed,

            "stage4_mistakes":
                progress.stage4_mistakes,

            "stage4_seconds":
                progress.stage4_seconds,


            # =========================================
            # TOTAL
            # =========================================

            "total_mistakes":
                progress.total_mistakes,

            "total_seconds":
                progress.total_seconds,


            # =========================================
            # DATES
            # =========================================

            "first_opened_at":
                progress.first_opened_at,

            "last_opened_at":
                progress.last_opened_at,

            "completed_at":
                progress.completed_at,
        }


    context = {
        "level":
            level,

        "group":
            group,

        "lessons":
            lessons,

        "total_words":
            total_words,

        "practice_cards":
            practice_cards,
    }

    return render(
        request,
        "vocabulary/group_detail.html",
        context,
    )


# =========================================================
# LESSON
# =========================================================


def lesson_detail(
    request,
    level_code,
    lesson_id,
):

    # =====================================================
    # ACTIVE COURSE USER
    # =====================================================



    lesson = get_object_or_404(
        VocabularyLesson,
        id=lesson_id,
        group__level__code__iexact=level_code,
        is_active=True,
    )

    words = (
        lesson.words
        .filter(
            is_active=True
        )
        .order_by(
            "order"
        )
    )

    context = {
        "level":
            lesson.group.level,

        "group":
            lesson.group,

        "lesson":
            lesson,

        "words":
            words,

        "word_count":
            words.count(),
    }

    return render(
        request,
        "vocabulary/lesson_detail.html",
        context,
    )


# =========================================================
# LESSON PRACTICE
# CONTEXT HELPERS
# =========================================================


def clean_context_wrong_options(
    word,
):
    """
    Подготавливает неправильные варианты
    для третьего этапа урока.

    Удаляем:
    - пустые значения;
    - дубликаты;
    - само правильное слово.
    """

    raw_options = (
        word.context_wrong_options
        or []
    )

    if not isinstance(
        raw_options,
        list,
    ):

        return []

    correct_word = (
        word.word
        or ""
    ).strip().lower()

    result = []

    used = set()

    for option in raw_options:

        option = str(
            option
        ).strip()

        if not option:
            continue

        normalized = (
            option.lower()
        )

        if (
            normalized
            ==
            correct_word
        ):
            continue

        if (
            normalized
            in used
        ):
            continue

        used.add(
            normalized
        )

        result.append(
            option
        )

        if (
            len(
                result
            )
            ==
            3
        ):
            break

    return result


# =========================================================
# LESSON PRACTICE
# =========================================================


@login_required
def lesson_practice(
    request,
    level_code,
    lesson_id,
):

    lesson = get_object_or_404(
        VocabularyLesson,
        id=lesson_id,
        group__level__code__iexact=level_code,
        is_active=True,
    )

    level = (
        lesson.group.level
    )

    lesson_words = list(
        lesson.words
        .filter(
            is_active=True
        )
        .order_by(
            "order"
        )
    )

    lesson_word_ids = [
        word.id
        for word in lesson_words
    ]

    all_level_words = list(
        VocabularyWord.objects
        .filter(
            lesson__group__level=level,
            is_active=True,
        )
        .exclude(
            id__in=lesson_word_ids
        )
    )

    questions = []

    for word in lesson_words:

        # =================================================
        # STAGE 1
        # ENGLISH -> RUSSIAN
        # =================================================

        correct_answer = (
            word.translation_ru
            or ""
        ).strip()

        same_pos_words = [
            candidate

            for candidate
            in all_level_words

            if (
                candidate.part_of_speech
                ==
                word.part_of_speech
            )
        ]

        other_words = [
            candidate

            for candidate
            in all_level_words

            if (
                candidate.part_of_speech
                !=
                word.part_of_speech
            )
        ]

        random.shuffle(
            same_pos_words
        )

        random.shuffle(
            other_words
        )

        candidates = (
            same_pos_words
            +
            other_words
        )

        wrong_answers = []

        used_answers = {
            correct_answer.lower()
        }

        for candidate in candidates:

            translation = (
                candidate.translation_ru
                or ""
            ).strip()

            if not translation:
                continue

            normalized = (
                translation.lower()
            )

            if (
                normalized
                in used_answers
            ):
                continue

            used_answers.add(
                normalized
            )

            wrong_answers.append(
                translation
            )

            if (
                len(
                    wrong_answers
                )
                ==
                3
            ):
                break

        options = [
            correct_answer,
            *wrong_answers,
        ]

        random.shuffle(
            options
        )


        # =================================================
        # STAGE 3
        # CONTEXT
        # =================================================

        context_sentence = (
            word.context_sentence
            or ""
        ).strip()

        context_wrong_options = (
            clean_context_wrong_options(
                word
            )
        )


        # =================================================
        # STAGE 4
        # AUDIO
        # =================================================

        audio_url = None

        if (
            word.audio_file
        ):

            try:

                audio_url = (
                    word.audio_file.url
                )

            except ValueError:

                audio_url = None


        # =================================================
        # QUESTION DATA
        # =================================================

        questions.append(
            {
                "word_id":
                    word.id,

                "word":
                    word.word,

                "part_of_speech":
                    word.part_of_speech,


                # -----------------------------
                # STAGE 1
                # TRANSLATION
                # -----------------------------

                "correct":
                    correct_answer,

                "options":
                    options,


                # -----------------------------
                # EXAMPLE
                # -----------------------------

                "example":
                    word.example_en,


                # -----------------------------
                # STAGE 3
                # CONTEXT
                # -----------------------------

                "context_sentence":
                    context_sentence,

                "context_wrong_options":
                    context_wrong_options,


                # -----------------------------
                # STAGE 4
                # LISTENING
                # -----------------------------

                "audio_url":
                    audio_url,
            }
        )


    # =====================================================
    # LOAD / CREATE LESSON PRACTICE PROGRESS
    # =====================================================

    progress, created = (
        LessonPracticeProgress.objects
        .get_or_create(
            user=request.user,
            lesson=lesson,
        )
    )

    now = timezone.now()

    if (
        progress.first_opened_at
        is None
    ):

        progress.first_opened_at = (
            now
        )

    progress.last_opened_at = (
        now
    )

    progress.save(
        update_fields=[
            "first_opened_at",
            "last_opened_at",
            "updated_at",
        ]
    )


    saved_practice_state = (
        progress.practice_state

        if isinstance(
            progress.practice_state,
            dict,
        )

        else {}
    )


    return render(
        request,
        "vocabulary/practice.html",
        {
            "lesson":
                lesson,

            "group":
                lesson.group,

            "level":
                level,

            "questions":
                questions,

            "question_count":
                len(
                    questions
                ),

            # =============================================
            # RESTORE PRACTICE
            # =============================================

            "saved_current_stage":
                progress.current_stage,

            "saved_practice_state":
                saved_practice_state,

            "lesson_progress":
                {
                    "stage1_completed":
                        progress.stage1_completed,

                    "stage2_completed":
                        progress.stage2_completed,

                    "stage3_completed":
                        progress.stage3_completed,

                    "stage4_completed":
                        progress.stage4_completed,

                    "completed":
                        progress.is_completed,
                },
        },
    )



# =========================================================
# OLD LESSON ANSWER
# =========================================================


@login_required
@require_POST
def record_answer(
    request,
):

    try:

        data = json.loads(
            request.body
        )

        word_id = data.get(
            "word_id"
        )

        is_correct = data.get(
            "is_correct"
        )

        word = get_object_or_404(
            VocabularyWord,
            id=word_id,
        )

        progress, created = (
            UserWordProgress.objects
            .get_or_create(
                user=request.user,
                word=word,
            )
        )

        now = (
            timezone.now()
        )


        # =================================================
        # CORRECT
        # =================================================

        if is_correct:

            progress.correct_answers += 1

            already_scheduled = (
                progress.next_review
                is not None
                and
                progress.next_review
                >
                now
                and
                progress.status
                !=
                UserWordProgress
                .Status
                .LEARNING
            )

            if not already_scheduled:

                progress.repetitions += 1

                repetition = (
                    progress.repetitions
                )

                if repetition == 1:

                    interval = 1

                elif repetition == 2:

                    interval = 3

                elif repetition == 3:

                    interval = 7

                elif repetition == 4:

                    interval = 14

                else:

                    interval = 30

                progress.interval_days = (
                    interval
                )

                progress.next_review = (
                    now
                    +
                    timedelta(
                        days=interval
                    )
                )

                if repetition == 1:

                    progress.status = (
                        UserWordProgress
                        .Status
                        .LEARNING
                    )

                elif repetition < 5:

                    progress.status = (
                        UserWordProgress
                        .Status
                        .REVIEW
                    )

                else:

                    progress.status = (
                        UserWordProgress
                        .Status
                        .MASTERED
                    )


        # =================================================
        # WRONG
        # =================================================

        else:

            progress.wrong_answers += 1

            progress.repetitions = 0

            progress.interval_days = 0

            progress.status = (
                UserWordProgress
                .Status
                .LEARNING
            )

            progress.next_review = None

        progress.last_reviewed_at = (
            now
        )

        progress.save()

        return JsonResponse(
            {
                "success":
                    True,

                "status":
                    progress.status,

                "correct_answers":
                    progress.correct_answers,

                "wrong_answers":
                    progress.wrong_answers,

                "repetitions":
                    progress.repetitions,

                "interval_days":
                    progress.interval_days,

                "next_review":
                    (
                        progress
                        .next_review
                        .isoformat()

                        if progress.next_review

                        else None
                    ),
            }
        )

    except Exception as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=400,
        )


# =========================================================
# GROUP PRACTICE
# COMMON HELPERS
# =========================================================


def get_group_words(
    group,
):

    return list(
        VocabularyWord.objects
        .filter(
            lesson__group=group,
            is_active=True,
        )
        .select_related(
            "lesson"
        )
        .order_by(
            "lesson__order",
            "order",
        )
    )


def get_deck_word_ids(
    session,
    deck_number,
):

    return list(
        session.word_states
        .filter(
            deck=deck_number
        )
        .values_list(
            "word_id",
            flat=True,
        )
    )


def mark_practice_opened(
    session,
):

    session.last_opened_at = (
        timezone.now()
    )

    session.save(
        update_fields=[
            "last_opened_at",
            "updated_at",
        ]
    )


def set_practice_phase(
    session,
    phase,
    word_ids,
    shuffle=True,
):

    word_ids = list(
        word_ids
    )

    if shuffle:

        random.shuffle(
            word_ids
        )

    session.phase = (
        phase
    )

    session.current_queue = (
        word_ids
    )

    session.current_index = 0

    session.save(
        update_fields=[
            "phase",
            "current_queue",
            "current_index",
            "mistake_count",
            "updated_at",
        ]
    )


def finish_group_practice(
    session,
):

    session.phase = (
        GroupPracticeSession
        .Phase
        .COMPLETED
    )

    session.is_completed = True

    session.current_queue = []

    session.current_index = 0

    session.completed_at = (
        timezone.now()
    )

    session.save(
        update_fields=[
            "phase",
            "is_completed",
            "current_queue",
            "current_index",
            "mistake_count",
            "completed_at",
            "updated_at",
        ]
    )


def start_deck1_check(
    session,
):

    ids = get_deck_word_ids(
        session,
        GroupPracticeWordState
        .Deck
        .DECK_1,
    )

    if not ids:

        finish_group_practice(
            session
        )

        return

    set_practice_phase(
        session,
        GroupPracticeSession
        .Phase
        .DECK1_CHECK,
        ids,
        shuffle=True,
    )


def start_deck2_check(
    session,
):

    ids = get_deck_word_ids(
        session,
        GroupPracticeWordState
        .Deck
        .DECK_2,
    )

    if not ids:

        start_deck1_check(
            session
        )

        return

    set_practice_phase(
        session,
        GroupPracticeSession
        .Phase
        .DECK2_CHECK,
        ids,
        shuffle=True,
    )


def start_deck3(
    session,
):

    ids = get_deck_word_ids(
        session,
        GroupPracticeWordState
        .Deck
        .DECK_3,
    )

    if not ids:

        start_deck2_check(
            session
        )

        return

    set_practice_phase(
        session,
        GroupPracticeSession
        .Phase
        .DECK3,
        ids,
        shuffle=True,
    )


def initialize_group_practice(
    session,
    words,
):

    GroupPracticeWordState.objects.filter(
        session=session,
    ).delete()

    GroupPracticeWordState.objects.bulk_create(
        [
            GroupPracticeWordState(
                session=session,
                word=word,
                deck=(
                    GroupPracticeWordState
                    .Deck
                    .UNOPENED
                ),
            )

            for word in words
        ]
    )

    session.phase = (
        GroupPracticeSession
        .Phase
        .INITIAL
    )

    session.current_queue = [
        word.id
        for word in words
    ]

    session.current_index = 0

    session.mistake_count = 0

    session.is_completed = False

    session.completed_at = None

    session.save(
        update_fields=[
            "phase",
            "current_queue",
            "current_index",
            "mistake_count",
            "is_completed",
            "completed_at",
            "updated_at",
        ]
    )


def get_or_create_group_practice(
    user,
    group,
    practice_number,
    words,
):

    session, created = (
        GroupPracticeSession.objects
        .get_or_create(
            user=user,
            group=group,
            practice_number=practice_number,
        )
    )

    if created:

        initialize_group_practice(
            session,
            words,
        )

    return session


def serialize_practice(
    session,
):

    decks = list(
        session.word_states
        .values_list(
            "deck",
            flat=True,
        )
    )

    counts = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
    }

    for deck in decks:

        counts[deck] = (
            counts.get(
                deck,
                0,
            )
            +
            1
        )

    current_word_id = None

    if (
        not session.is_completed
        and
        session.current_queue
        and
        session.current_index
        <
        len(
            session.current_queue
        )
    ):

        current_word_id = int(
            session.current_queue[
                session.current_index
            ]
        )

    if session.phase in [
        GroupPracticeSession
        .Phase
        .INITIAL,

        GroupPracticeSession
        .Phase
        .DECK1_CHECK,
    ]:

        current_deck = 1

    elif session.phase in [
        GroupPracticeSession
        .Phase
        .DECK2_FIRST,

        GroupPracticeSession
        .Phase
        .DECK2_CHECK,
    ]:

        current_deck = 2

    elif (
        session.phase
        ==
        GroupPracticeSession
        .Phase
        .DECK3
    ):

        current_deck = 3

    else:

        current_deck = None

    return {
        "phase":
            session.phase,

        "current_deck":
            current_deck,

        "current_index":
            session.current_index,

        "queue_size":
            len(
                session.current_queue
            ),

        "current_word_id":
            current_word_id,

        "deck1_count":
            counts[1],

        "deck2_count":
            counts[2],

        "deck3_count":
            counts[3],

        "unopened_count":
            counts[0],

        "mistake_count":
            session.mistake_count,

        "is_completed":
            session.is_completed,
    }


# =========================================================
# COMMON DECK ANSWER ENGINE
# =========================================================


def process_deck_answer(
    session,
    word_id,
    knows_word,
):

    if (
        session.current_index
        >=
        len(
            session.current_queue
        )
    ):

        raise ValueError(
            "Invalid practice position."
        )

    expected_word_id = int(
        session.current_queue[
            session.current_index
        ]
    )

    if (
        int(
            word_id
        )
        !=
        expected_word_id
    ):

        raise ValueError(
            "This is not the current word."
        )

    word_state = (
        GroupPracticeWordState.objects
        .select_for_update()
        .get(
            session=session,
            word_id=word_id,
        )
    )

    if not knows_word:

        session.mistake_count += 1

    phase = (
        session.phase
    )


    # =====================================================
    # INITIAL
    # =====================================================

    if (
        phase
        ==
        GroupPracticeSession
        .Phase
        .INITIAL
    ):

        if knows_word:

            word_state.deck = (
                GroupPracticeWordState
                .Deck
                .DECK_1
            )

        else:

            word_state.deck = (
                GroupPracticeWordState
                .Deck
                .DECK_2
            )

        word_state.save(
            update_fields=[
                "deck",
            ]
        )

        session.current_index += 1

        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

        else:

            deck2_ids = (
                get_deck_word_ids(
                    session,
                    GroupPracticeWordState
                    .Deck
                    .DECK_2,
                )
            )

            if deck2_ids:

                set_practice_phase(
                    session,
                    GroupPracticeSession
                    .Phase
                    .DECK2_FIRST,
                    deck2_ids,
                    shuffle=True,
                )

            else:

                start_deck1_check(
                    session
                )

        return


    # =====================================================
    # FIRST DECK 2
    # =====================================================

    if (
        phase
        ==
        GroupPracticeSession
        .Phase
        .DECK2_FIRST
    ):

        if not knows_word:

            word_state.deck = (
                GroupPracticeWordState
                .Deck
                .DECK_3
            )

            word_state.save(
                update_fields=[
                    "deck",
                ]
            )

        session.current_index += 1

        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

        else:

            deck3_ids = (
                get_deck_word_ids(
                    session,
                    GroupPracticeWordState
                    .Deck
                    .DECK_3,
                )
            )

            if deck3_ids:

                start_deck3(
                    session
                )

            else:

                start_deck1_check(
                    session
                )

        return


    # =====================================================
    # DECK 3
    # =====================================================

    if (
        phase
        ==
        GroupPracticeSession
        .Phase
        .DECK3
    ):

        if not knows_word:

            start_deck3(
                session
            )

            return

        session.current_index += 1

        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

        else:

            start_deck2_check(
                session
            )

        return


    # =====================================================
    # DECK 2 CHECK
    # =====================================================

    if (
        phase
        ==
        GroupPracticeSession
        .Phase
        .DECK2_CHECK
    ):

        if not knows_word:

            word_state.deck = (
                GroupPracticeWordState
                .Deck
                .DECK_3
            )

            word_state.save(
                update_fields=[
                    "deck",
                ]
            )

            start_deck3(
                session
            )

            return

        session.current_index += 1

        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

        else:

            start_deck1_check(
                session
            )

        return


    # =====================================================
    # DECK 1 CHECK
    # =====================================================

    if (
        phase
        ==
        GroupPracticeSession
        .Phase
        .DECK1_CHECK
    ):

        if not knows_word:

            word_state.deck = (
                GroupPracticeWordState
                .Deck
                .DECK_3
            )

            word_state.save(
                update_fields=[
                    "deck",
                ]
            )

            start_deck3(
                session
            )

            return

        session.current_index += 1

        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

        else:

            finish_group_practice(
                session
            )

        return

    raise ValueError(
        "Unknown practice phase."
    )


# =========================================================
# PRACTICE 1
# =========================================================


@login_required
def group_practice1(
    request,
    level_code,
    group_id,
):

    level = get_object_or_404(
        VocabularyLevel,
        code__iexact=level_code,
        is_active=True,
    )

    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
        level=level,
    )

    words = get_group_words(
        group
    )

    session = (
        get_or_create_group_practice(
            user=request.user,
            group=group,
            practice_number=1,
            words=words,
        )
    )

    mark_practice_opened(
        session
    )

    word_data = [
        {
            "id":
                word.id,

            "word":
                word.word,

            "part_of_speech":
                word.part_of_speech,

            "translation_ru":
                word.translation_ru,

            "translation_kz":
                word.translation_kz,
        }

        for word in words
    ]

    practice_state = (
        serialize_practice(
            session
        )
    )

    return render(
        request,
        "vocabulary/group_practice1.html",
        {
            "level":
                level,

            "group":
                group,

            "words":
                words,

            "word_count":
                len(
                    words
                ),

            "word_data":
                word_data,

            "practice_state":
                practice_state,
        },
    )


# =========================================================
# PRACTICE 1 ANSWER
# =========================================================


@login_required
@require_POST
@transaction.atomic
def group_practice1_answer(
    request,
    group_id,
):

    try:

        data = json.loads(
            request.body
        )

        word_id = int(
            data[
                "word_id"
            ]
        )

        knows_word = bool(
            data[
                "knows_word"
            ]
        )

        session = (
            GroupPracticeSession.objects
            .select_for_update()
            .get(
                user=request.user,
                group_id=group_id,
                practice_number=1,
                is_completed=False,
            )
        )

        process_deck_answer(
            session=session,
            word_id=word_id,
            knows_word=knows_word,
        )

        session.refresh_from_db()

        return JsonResponse(
            {
                "success":
                    True,

                "state":
                    serialize_practice(
                        session
                    ),
            }
        )

    except (
        GroupPracticeSession
        .DoesNotExist
    ):

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    "Practice 1 session not found.",
            },
            status=404,
        )

    except ValueError as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=409,
        )

    except Exception as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=400,
        )


# =========================================================
# PRACTICE 1 RESTART
# =========================================================


@login_required
@require_POST
@transaction.atomic
def group_practice1_restart(
    request,
    group_id,
):

    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
    )

    session = (
        GroupPracticeSession.objects
        .select_for_update()
        .get(
            user=request.user,
            group=group,
            practice_number=1,
        )
    )

    words = get_group_words(
        group
    )

    initialize_group_practice(
        session,
        words,
    )

    session.refresh_from_db()

    return JsonResponse(
        {
            "success":
                True,

            "state":
                serialize_practice(
                    session
                ),
        }
    )


# =========================================================
# PRACTICE 2
# =========================================================


def build_practice2_question(
    session,
):

    if session.is_completed:
        return None

    if (
        not session.current_queue
        or
        session.current_index
        >=
        len(
            session.current_queue
        )
    ):

        return None

    current_word_id = int(
        session.current_queue[
            session.current_index
        ]
    )

    current_word = get_object_or_404(
        VocabularyWord,
        id=current_word_id,
        is_active=True,
    )

    correct_translation = (
        current_word.translation_ru
        or ""
    ).strip()

    group_candidates = list(
        VocabularyWord.objects
        .filter(
            lesson__group=session.group,
            is_active=True,
        )
        .exclude(
            id=current_word.id,
        )
    )

    random.shuffle(
        group_candidates
    )

    same_pos_candidates = [
        word

        for word
        in group_candidates

        if (
            word.part_of_speech
            ==
            current_word.part_of_speech
        )
    ]

    other_candidates = [
        word

        for word
        in group_candidates

        if (
            word.part_of_speech
            !=
            current_word.part_of_speech
        )
    ]

    random.shuffle(
        same_pos_candidates
    )

    random.shuffle(
        other_candidates
    )

    candidates = (
        same_pos_candidates
        +
        other_candidates
    )

    level_candidates = list(
        VocabularyWord.objects
        .filter(
            lesson__group__level=(
                session.group.level
            ),
            is_active=True,
        )
        .exclude(
            id=current_word.id,
        )
    )

    random.shuffle(
        level_candidates
    )

    candidates.extend(
        level_candidates
    )

    options = [
        {
            "id":
                current_word.id,

            "translation":
                correct_translation,
        }
    ]

    used_translations = {
        correct_translation.lower()
    }

    used_word_ids = {
        current_word.id
    }

    for candidate in candidates:

        if (
            candidate.id
            in used_word_ids
        ):
            continue

        translation = (
            candidate.translation_ru
            or ""
        ).strip()

        if not translation:
            continue

        normalized = (
            translation.lower()
        )

        if (
            normalized
            in used_translations
        ):
            continue

        used_word_ids.add(
            candidate.id
        )

        used_translations.add(
            normalized
        )

        options.append(
            {
                "id":
                    candidate.id,

                "translation":
                    translation,
            }
        )

        if (
            len(
                options
            )
            ==
            4
        ):

            break

    random.shuffle(
        options
    )

    return {
        "word_id":
            current_word.id,

        "word":
            current_word.word,

        "part_of_speech":
            current_word.part_of_speech,

        "options":
            options,
    }


def serialize_practice2(
    session,
):

    state = serialize_practice(
        session
    )

    state[
        "question"
    ] = build_practice2_question(
        session
    )

    return state


# =========================================================
# PRACTICE 2 PAGE
# =========================================================


@login_required
def group_practice2(
    request,
    level_code,
    group_id,
):

    level = get_object_or_404(
        VocabularyLevel,
        code__iexact=level_code,
        is_active=True,
    )

    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
        level=level,
    )

    words = get_group_words(
        group
    )

    session = (
        get_or_create_group_practice(
            user=request.user,
            group=group,
            practice_number=2,
            words=words,
        )
    )

    mark_practice_opened(
        session
    )

    practice_state = (
        serialize_practice2(
            session
        )
    )

    return render(
        request,
        "vocabulary/group_practice2.html",
        {
            "level":
                level,

            "group":
                group,

            "word_count":
                len(
                    words
                ),

            "practice_state":
                practice_state,
        },
    )


# =========================================================
# PRACTICE 2 ANSWER
# =========================================================


@login_required
@require_POST
@transaction.atomic
def group_practice2_answer(
    request,
    group_id,
):

    try:

        data = json.loads(
            request.body
        )

        word_id = int(
            data[
                "word_id"
            ]
        )

        selected_word_id = int(
            data[
                "selected_word_id"
            ]
        )

        session = (
            GroupPracticeSession.objects
            .select_for_update()
            .get(
                user=request.user,
                group_id=group_id,
                practice_number=2,
                is_completed=False,
            )
        )

        if (
            session.current_index
            >=
            len(
                session.current_queue
            )
        ):

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        "Invalid practice position.",
                },
                status=409,
            )

        expected_word_id = int(
            session.current_queue[
                session.current_index
            ]
        )

        if (
            word_id
            !=
            expected_word_id
        ):

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        "This is not the current word.",
                },
                status=409,
            )

        selected_word_exists = (
            VocabularyWord.objects
            .filter(
                id=selected_word_id,
                lesson__group_id=group_id,
                is_active=True,
            )
            .exists()
        )

        if not selected_word_exists:

            group = (
                session.group
            )

            selected_word_exists = (
                VocabularyWord.objects
                .filter(
                    id=selected_word_id,
                    lesson__group__level=(
                        group.level
                    ),
                    is_active=True,
                )
                .exists()
            )

        if not selected_word_exists:

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        "Invalid answer option.",
                },
                status=400,
            )

        is_correct = (
            selected_word_id
            ==
            expected_word_id
        )

        process_deck_answer(
            session=session,
            word_id=word_id,
            knows_word=is_correct,
        )

        session.refresh_from_db()

        return JsonResponse(
            {
                "success":
                    True,

                "answer":
                    {
                        "is_correct":
                            is_correct,

                        "selected_word_id":
                            selected_word_id,

                        "correct_word_id":
                            expected_word_id,
                    },

                "state":
                    serialize_practice2(
                        session
                    ),
            }
        )

    except (
        GroupPracticeSession
        .DoesNotExist
    ):

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    "Practice 2 session not found.",
            },
            status=404,
        )

    except ValueError as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=409,
        )

    except Exception as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=400,
        )


# =========================================================
# PRACTICE 2 RESTART
# =========================================================


@login_required
@require_POST
@transaction.atomic
def group_practice2_restart(
    request,
    group_id,
):

    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
    )

    session = (
        GroupPracticeSession.objects
        .select_for_update()
        .get(
            user=request.user,
            group=group,
            practice_number=2,
        )
    )

    words = get_group_words(
        group
    )

    initialize_group_practice(
        session,
        words,
    )

    session.refresh_from_db()

    return JsonResponse(
        {
            "success":
                True,

            "state":
                serialize_practice2(
                    session
                ),
        }
    )


# =========================================================
# PRACTICE 3
# BUILD ENGLISH WORD FROM LETTERS
# =========================================================


MIN_PRACTICE3_LETTERS = 8


def normalize_practice3_word(
    value,
):

    return "".join(
        character.lower()

        for character
        in value

        if character.isalpha()
    )


def build_practice3_pattern(
    word,
):

    pattern = []

    for character in word:

        if character.isalpha():

            pattern.append(
                {
                    "type":
                        "slot",
                }
            )

        elif character.isspace():

            pattern.append(
                {
                    "type":
                        "separator",

                    "value":
                        " ",
                }
            )

        else:

            pattern.append(
                {
                    "type":
                        "separator",

                    "value":
                        character,
                }
            )

    return pattern


def build_practice3_question(
    session,
):

    if session.is_completed:

        return None

    if (
        not session.current_queue
        or
        session.current_index
        >=
        len(
            session.current_queue
        )
    ):

        return None

    current_word_id = int(
        session.current_queue[
            session.current_index
        ]
    )

    current_word = get_object_or_404(
        VocabularyWord,
        id=current_word_id,
        is_active=True,
    )

    target = (
        normalize_practice3_word(
            current_word.word
        )
    )

    target_letters = list(
        target
    )

    letter_bank = (
        target_letters.copy()
    )

    extra_letters_pool = (
        "etaoinshrdlucmfwypvbgkjqxz"
    )

    while (
        len(
            letter_bank
        )
        <
        MIN_PRACTICE3_LETTERS
    ):

        extra_letter = random.choice(
            extra_letters_pool
        )

        letter_bank.append(
            extra_letter
        )

    random.shuffle(
        letter_bank
    )

    letter_tiles = [
        {
            "id":
                index,

            "letter":
                letter,
        }

        for index, letter
        in enumerate(
            letter_bank
        )
    ]

    return {
        "word_id":
            current_word.id,

        "translation_ru":
            current_word.translation_ru,

        "part_of_speech":
            current_word.part_of_speech,

        "slot_count":
            len(
                target_letters
            ),

        "pattern":
            build_practice3_pattern(
                current_word.word
            ),

        "letters":
            letter_tiles,
    }


def serialize_practice3(
    session,
):

    state = serialize_practice(
        session
    )

    state[
        "question"
    ] = build_practice3_question(
        session
    )

    return state


# =========================================================
# PRACTICE 3 PAGE
# =========================================================


@login_required
def group_practice3(
    request,
    level_code,
    group_id,
):

    level = get_object_or_404(
        VocabularyLevel,
        code__iexact=level_code,
        is_active=True,
    )

    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
        level=level,
    )

    words = get_group_words(
        group
    )

    session = (
        get_or_create_group_practice(
            user=request.user,
            group=group,
            practice_number=3,
            words=words,
        )
    )

    mark_practice_opened(
        session
    )

    practice_state = (
        serialize_practice3(
            session
        )
    )

    return render(
        request,
        "vocabulary/group_practice3.html",
        {
            "level":
                level,

            "group":
                group,

            "word_count":
                len(
                    words
                ),

            "practice_state":
                practice_state,
        },
    )


# =========================================================
# PRACTICE 3 ANSWER
# =========================================================


@login_required
@require_POST
@transaction.atomic
def group_practice3_answer(
    request,
    group_id,
):

    try:

        data = json.loads(
            request.body
        )

        word_id = int(
            data[
                "word_id"
            ]
        )

        user_answer = str(
            data.get(
                "answer",
                "",
            )
        )

        session = (
            GroupPracticeSession.objects
            .select_for_update()
            .get(
                user=request.user,
                group_id=group_id,
                practice_number=3,
                is_completed=False,
            )
        )

        if (
            session.current_index
            >=
            len(
                session.current_queue
            )
        ):

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        "Invalid practice position.",
                },
                status=409,
            )

        expected_word_id = int(
            session.current_queue[
                session.current_index
            ]
        )

        if (
            word_id
            !=
            expected_word_id
        ):

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        "This is not the current word.",
                },
                status=409,
            )

        word = get_object_or_404(
            VocabularyWord,
            id=expected_word_id,
            is_active=True,
        )

        normalized_answer = (
            normalize_practice3_word(
                user_answer
            )
        )

        normalized_correct = (
            normalize_practice3_word(
                word.word
            )
        )

        is_correct = (
            normalized_answer
            ==
            normalized_correct
        )

        process_deck_answer(
            session=session,
            word_id=word_id,
            knows_word=is_correct,
        )

        session.refresh_from_db()

        return JsonResponse(
            {
                "success":
                    True,

                "answer":
                    {
                        "is_correct":
                            is_correct,

                        "correct_word":
                            word.word,
                    },

                "state":
                    serialize_practice3(
                        session
                    ),
            }
        )

    except (
        GroupPracticeSession
        .DoesNotExist
    ):

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    "Practice 3 session not found.",
            },
            status=404,
        )

    except ValueError as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=409,
        )

    except Exception as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=400,
        )


# =========================================================
# PRACTICE 3 RESTART
# =========================================================


@login_required
@require_POST
@transaction.atomic
def group_practice3_restart(
    request,
    group_id,
):

    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
    )

    session = (
        GroupPracticeSession.objects
        .select_for_update()
        .get(
            user=request.user,
            group=group,
            practice_number=3,
        )
    )

    words = get_group_words(
        group
    )

    initialize_group_practice(
        session,
        words,
    )

    session.refresh_from_db()

    return JsonResponse(
        {
            "success":
                True,

            "state":
                serialize_practice3(
                    session
                ),
        }
    )



# =========================================================
# LESSON PRACTICE STATE
# =========================================================


LESSON_PRACTICE_STAGES = {
    "choice",
    "spelling",
    "context",
    "listening",
    "completed",
}


def sanitize_lesson_practice_state(
    lesson,
    raw_state,
):

    if not isinstance(
        raw_state,
        dict,
    ):

        return {}


    valid_word_ids = set(

        lesson.words
        .filter(
            is_active=True,
        )
        .values_list(
            "id",
            flat=True,
        )

    )


    result = {}


    for stage_name in [
        "choice",
        "spelling",
        "context",
        "listening",
    ]:

        raw_stage = (
            raw_state.get(
                stage_name,
                {},
            )
        )


        if not isinstance(
            raw_stage,
            dict,
        ):

            continue


        # =============================================
        # QUEUE
        # =============================================

        queue = []


        for value in (
            raw_stage.get(
                "queue",
                [],
            )
            or []
        ):

            try:

                word_id = int(
                    value
                )

            except (
                TypeError,
                ValueError,
            ):

                continue


            if (
                word_id
                in
                valid_word_ids
            ):

                # Дубликаты здесь разрешены:
                # неправильное слово может быть
                # снова добавлено в очередь.

                queue.append(
                    word_id
                )


        # =============================================
        # LEARNED
        # =============================================

        learned = []


        for value in (
            raw_stage.get(
                "learned",
                [],
            )
            or []
        ):

            try:

                word_id = int(
                    value
                )

            except (
                TypeError,
                ValueError,
            ):

                continue


            if (
                word_id
                in
                valid_word_ids
                and
                word_id
                not in learned
            ):

                learned.append(
                    word_id
                )


        # =============================================
        # INDEX
        # =============================================

        try:

            index = int(
                raw_stage.get(
                    "index",
                    0,
                )
            )

        except (
            TypeError,
            ValueError,
        ):

            index = 0


        index = max(
            0,
            min(
                index,
                len(
                    queue
                ),
            ),
        )


        # =============================================
        # MISTAKES
        # =============================================

        try:

            mistakes = int(
                raw_stage.get(
                    "mistakes",
                    0,
                )
            )

        except (
            TypeError,
            ValueError,
        ):

            mistakes = 0


        mistakes = max(
            0,
            mistakes,
        )


        # =============================================
        # ELAPSED TIME
        # =============================================

        try:

            elapsed_seconds = int(
                raw_stage.get(
                    "elapsed_seconds",
                    0,
                )
            )

        except (
            TypeError,
            ValueError,
        ):

            elapsed_seconds = 0


        elapsed_seconds = max(
            0,
            elapsed_seconds,
        )


        result[
            stage_name
        ] = {

            "queue":
                queue,

            "index":
                index,

            "learned":
                learned,

            "mistakes":
                mistakes,

            "elapsed_seconds":
                elapsed_seconds,

        }


    return result

# =========================================================
# LESSON PRACTICE PROGRESS
# =========================================================

@login_required
@require_POST
@transaction.atomic
def lesson_practice_progress(
    request,
    lesson_id,
):

    try:

        lesson = get_object_or_404(
            VocabularyLesson,
            id=lesson_id,
            is_active=True,
        )


        data = json.loads(
            request.body
        )


        action = (
            data.get(
                "action"
            )
        )


        progress, created = (
            LessonPracticeProgress.objects
            .select_for_update()
            .get_or_create(
                user=request.user,
                lesson=lesson,
            )
        )


        now = (
            timezone.now()
        )


        # =================================================
        # OPEN
        # =================================================

        if action == "open":

            if (
                progress.first_opened_at
                is None
            ):

                progress.first_opened_at = (
                    now
                )


            progress.last_opened_at = (
                now
            )


            progress.save(
                update_fields=[
                    "first_opened_at",
                    "last_opened_at",
                    "updated_at",
                ]
            )


            return JsonResponse(
                {
                    "success":
                        True,

                    "current_stage":
                        progress.current_stage,

                    "practice_state":
                        progress.practice_state,

                    "completed":
                        progress.is_completed,

                    "perfect":
                        progress.is_perfect,

                    "total_mistakes":
                        progress.total_mistakes,

                    "total_seconds":
                        progress.total_seconds,

                    "stages": {

                        "stage1":
                            progress.stage1_completed,

                        "stage2":
                            progress.stage2_completed,

                        "stage3":
                            progress.stage3_completed,

                        "stage4":
                            progress.stage4_completed,

                    },
                }
            )


        # =================================================
        # SAVE CURRENT STATE
        # После каждого вопроса.
        # =================================================

        if action == "save_state":

            current_stage = str(
                data.get(
                    "current_stage",
                    progress.current_stage,
                )
            )


            if (
                current_stage
                not in
                LESSON_PRACTICE_STAGES
            ):

                return JsonResponse(
                    {
                        "success":
                            False,

                        "error":
                            "Invalid practice stage.",
                    },
                    status=400,
                )


            raw_state = (
                data.get(
                    "state",
                    {},
                )
            )


            clean_state = (
                sanitize_lesson_practice_state(
                    lesson,
                    raw_state,
                )
            )


            progress.current_stage = (
                current_stage
            )

            progress.practice_state = (
                clean_state
            )


            if (
                progress.first_opened_at
                is None
            ):

                progress.first_opened_at = (
                    now
                )


            progress.last_opened_at = (
                now
            )


            progress.save(
                update_fields=[
                    "current_stage",
                    "practice_state",
                    "first_opened_at",
                    "last_opened_at",
                    "updated_at",
                ]
            )


            return JsonResponse(
                {
                    "success":
                        True,

                    "current_stage":
                        progress.current_stage,

                    "practice_state":
                        progress.practice_state,
                }
            )


        # =================================================
        # RESTART LESSON
        # =================================================

        if action == "restart":

            progress.current_stage = (
                LessonPracticeProgress
                .Stage
                .CHOICE
            )

            progress.practice_state = {}


            progress.stage1_completed = (
                False
            )

            progress.stage1_mistakes = 0
            progress.stage1_seconds = 0


            progress.stage2_completed = (
                False
            )

            progress.stage2_mistakes = 0
            progress.stage2_seconds = 0


            progress.stage3_completed = (
                False
            )

            progress.stage3_mistakes = 0
            progress.stage3_seconds = 0


            progress.stage4_completed = (
                False
            )

            progress.stage4_mistakes = 0
            progress.stage4_seconds = 0


            progress.completed_at = None

            progress.last_opened_at = (
                now
            )


            if (
                progress.first_opened_at
                is None
            ):

                progress.first_opened_at = (
                    now
                )


            progress.save()


            return JsonResponse(
                {
                    "success":
                        True,

                    "current_stage":
                        progress.current_stage,

                    "practice_state":
                        {},

                    "completed":
                        False,

                    "perfect":
                        False,

                    "total_mistakes":
                        0,

                    "total_seconds":
                        0,
                }
            )


        # =================================================
        # STAGE COMPLETE
        # =================================================

        if action == "stage_complete":

            stage = int(
                data.get(
                    "stage",
                    0,
                )
            )


            mistakes = max(
                0,
                int(
                    data.get(
                        "mistakes",
                        0,
                    )
                ),
            )


            seconds = max(
                0,
                int(
                    data.get(
                        "seconds",
                        0,
                    )
                ),
            )


            # При завершении этапа frontend
            # может одновременно передать
            # последнее состояние.

            if (
                "state"
                in data
            ):

                progress.practice_state = (
                    sanitize_lesson_practice_state(
                        lesson,
                        data.get(
                            "state",
                            {},
                        ),
                    )
                )


            if (
                progress.first_opened_at
                is None
            ):

                progress.first_opened_at = (
                    now
                )


            progress.last_opened_at = (
                now
            )


            # =============================================
            # STAGE 1
            # =============================================

            if stage == 1:

                progress.stage1_completed = (
                    True
                )

                progress.stage1_mistakes = (
                    mistakes
                )

                progress.stage1_seconds = (
                    seconds
                )

                progress.current_stage = (
                    LessonPracticeProgress
                    .Stage
                    .SPELLING
                )


            # =============================================
            # STAGE 2
            # =============================================

            elif stage == 2:

                progress.stage2_completed = (
                    True
                )

                progress.stage2_mistakes = (
                    mistakes
                )

                progress.stage2_seconds = (
                    seconds
                )

                progress.current_stage = (
                    LessonPracticeProgress
                    .Stage
                    .CONTEXT
                )


            # =============================================
            # STAGE 3
            # =============================================

            elif stage == 3:

                progress.stage3_completed = (
                    True
                )

                progress.stage3_mistakes = (
                    mistakes
                )

                progress.stage3_seconds = (
                    seconds
                )

                progress.current_stage = (
                    LessonPracticeProgress
                    .Stage
                    .LISTENING
                )


            # =============================================
            # STAGE 4
            # =============================================

            elif stage == 4:

                progress.stage4_completed = (
                    True
                )

                progress.stage4_mistakes = (
                    mistakes
                )

                progress.stage4_seconds = (
                    seconds
                )

                progress.current_stage = (
                    LessonPracticeProgress
                    .Stage
                    .COMPLETED
                )


            else:

                return JsonResponse(
                    {
                        "success":
                            False,

                        "error":
                            "Invalid stage.",
                    },
                    status=400,
                )


            # =============================================
            # FULL LESSON COMPLETE
            # =============================================

            if (
                progress.stage1_completed
                and
                progress.stage2_completed
                and
                progress.stage3_completed
                and
                progress.stage4_completed
            ):

                progress.completed_at = (
                    now
                )

                progress.current_stage = (
                    LessonPracticeProgress
                    .Stage
                    .COMPLETED
                )

            else:

                progress.completed_at = (
                    None
                )


            progress.save()


            return JsonResponse(
                {
                    "success":
                        True,

                    "stage":
                        stage,

                    "current_stage":
                        progress.current_stage,

                    "practice_state":
                        progress.practice_state,

                    "completed":
                        progress.is_completed,

                    "perfect":
                        progress.is_perfect,

                    "total_mistakes":
                        progress.total_mistakes,

                    "total_seconds":
                        progress.total_seconds,

                    "stages": {

                        "stage1": {
                            "completed":
                                progress.stage1_completed,

                            "mistakes":
                                progress.stage1_mistakes,

                            "seconds":
                                progress.stage1_seconds,
                        },

                        "stage2": {
                            "completed":
                                progress.stage2_completed,

                            "mistakes":
                                progress.stage2_mistakes,

                            "seconds":
                                progress.stage2_seconds,
                        },

                        "stage3": {
                            "completed":
                                progress.stage3_completed,

                            "mistakes":
                                progress.stage3_mistakes,

                            "seconds":
                                progress.stage3_seconds,
                        },

                        "stage4": {
                            "completed":
                                progress.stage4_completed,

                            "mistakes":
                                progress.stage4_mistakes,

                            "seconds":
                                progress.stage4_seconds,
                        },

                    },
                }
            )


        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    "Unknown action.",
            },
            status=400,
        )


    except json.JSONDecodeError:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    "Invalid JSON.",
            },
            status=400,
        )


    except (
        TypeError,
        ValueError,
    ) as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=400,
        )


    except Exception as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=400,
        )

# =========================================================
# PRACTICE 4
# LISTENING -> TYPE ENGLISH WORD
# =========================================================


def normalize_practice4_answer(
    value,
):
    """
    Нормализация ответа для Listening.

    Разрешаем:
    - разный регистр;
    - лишние пробелы;
    - разные варианты апострофа;
    - разные варианты дефиса.

    Но НЕ удаляем пробелы и дефисы полностью,
    потому что пользователь должен написать
    слово/выражение правильно.
    """

    value = str(
        value
        or
        ""
    )

    value = (
        value
        .strip()
        .lower()
    )

    # Curly apostrophes -> normal apostrophe
    value = (
        value
        .replace(
            "’",
            "'",
        )
        .replace(
            "‘",
            "'",
        )
    )

    # Different dashes -> normal hyphen
    for dash in [
        "‐",
        "-",
        "‒",
        "–",
        "—",
    ]:

        value = value.replace(
            dash,
            "-",
        )

    # Multiple spaces -> one space
    value = " ".join(
        value.split()
    )

    return value


def build_practice4_question(
    session,
):

    if session.is_completed:

        return None


    if (
        not session.current_queue
        or
        session.current_index
        >=
        len(
            session.current_queue
        )
    ):

        return None


    current_word_id = int(
        session.current_queue[
            session.current_index
        ]
    )


    current_word = get_object_or_404(
        VocabularyWord,
        id=current_word_id,
        is_active=True,
    )


    # =====================================================
    # AUDIO URL
    # =====================================================

    audio_url = None


    if current_word.audio_file:

        try:

            audio_url = (
                current_word
                .audio_file
                .url
            )

        except ValueError:

            audio_url = None


    return {

        "word_id":
            current_word.id,

        "audio_url":
            audio_url,

        "has_audio":
            bool(
                audio_url
            ),

    }


def serialize_practice4(
    session,
):

    state = serialize_practice(
        session
    )


    state[
        "question"
    ] = build_practice4_question(
        session
    )


    return state


# =========================================================
# PRACTICE 4 PAGE
# =========================================================


@login_required
def group_practice4(
    request,
    level_code,
    group_id,
):

    level = get_object_or_404(
        VocabularyLevel,
        code__iexact=level_code,
        is_active=True,
    )


    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
        level=level,
    )


    words = get_group_words(
        group
    )


    session = (
        get_or_create_group_practice(
            user=request.user,
            group=group,
            practice_number=4,
            words=words,
        )
    )


    mark_practice_opened(
        session
    )


    practice_state = (
        serialize_practice4(
            session
        )
    )


    return render(
        request,
        "vocabulary/group_practice4.html",
        {
            "level":
                level,

            "group":
                group,

            "word_count":
                len(
                    words
                ),

            "practice_state":
                practice_state,
        },
    )


# =========================================================
# PRACTICE 4 ANSWER
# =========================================================


@login_required
@require_POST
@transaction.atomic
def group_practice4_answer(
    request,
    group_id,
):

    try:

        data = json.loads(
            request.body
        )


        word_id = int(
            data[
                "word_id"
            ]
        )


        user_answer = str(
            data.get(
                "answer",
                "",
            )
        )


        session = (
            GroupPracticeSession.objects
            .select_for_update()
            .get(
                user=request.user,
                group_id=group_id,
                practice_number=4,
                is_completed=False,
            )
        )


        # =================================================
        # CURRENT POSITION
        # =================================================

        if (
            session.current_index
            >=
            len(
                session.current_queue
            )
        ):

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        "Invalid practice position.",
                },
                status=409,
            )


        expected_word_id = int(
            session.current_queue[
                session.current_index
            ]
        )


        if (
            word_id
            !=
            expected_word_id
        ):

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        "This is not the current word.",
                },
                status=409,
            )


        # =================================================
        # WORD
        # =================================================

        word = get_object_or_404(
            VocabularyWord,
            id=expected_word_id,
            is_active=True,
        )


        # =================================================
        # CHECK ANSWER
        # =================================================

        normalized_answer = (
            normalize_practice4_answer(
                user_answer
            )
        )


        normalized_correct = (
            normalize_practice4_answer(
                word.word
            )
        )


        is_correct = (
            normalized_answer
            ==
            normalized_correct
        )


        # =================================================
        # DECK ENGINE
        # =================================================

        process_deck_answer(
            session=session,
            word_id=word_id,
            knows_word=is_correct,
        )


        session.refresh_from_db()


        # =================================================
        # RESPONSE
        # =================================================

        return JsonResponse(
            {
                "success":
                    True,

                "answer":
                    {
                        "is_correct":
                            is_correct,

                        "correct_word":
                            word.word,

                        "translation_ru":
                            word.translation_ru,

                        "part_of_speech":
                            word.part_of_speech,
                    },

                "state":
                    serialize_practice4(
                        session
                    ),
            }
        )


    except (
        GroupPracticeSession
        .DoesNotExist
    ):

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    "Practice 4 session not found.",
            },
            status=404,
        )


    except ValueError as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=409,
        )


    except Exception as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(
                        error
                    ),
            },
            status=400,
        )


# =========================================================
# PRACTICE 4 RESTART
# =========================================================


@login_required
@require_POST
@transaction.atomic
def group_practice4_restart(
    request,
    group_id,
):

    group = get_object_or_404(
        VocabularyGroup,
        id=group_id,
    )


    session = (
        GroupPracticeSession.objects
        .select_for_update()
        .get(
            user=request.user,
            group=group,
            practice_number=4,
        )
    )


    words = get_group_words(
        group
    )


    initialize_group_practice(
        session,
        words,
    )


    mark_practice_opened(
        session
    )


    session.refresh_from_db()


    return JsonResponse(
        {
            "success":
                True,

            "state":
                serialize_practice4(
                    session
                ),
        }
    )


# =========================================================
# DAILY REVIEW
# =========================================================


@login_required
def daily_review(
    request,
):

    course = (
        get_active_user_course(
            request.user
        )
    )


    if not course:

        return redirect(
            "vocabulary:course_setup"
        )


    plan = (
        get_or_create_today_plan(
            course
        )
    )


    plan = (
        sync_daily_plan(
            plan
        )
    )


    review_item = (

        plan.items
        .filter(
            item_type=(
                DailyStudyPlanItem
                .Type
                .REVIEW
            )
        )
        .exclude(
            status=(
                DailyStudyPlanItem
                .Status
                .COMPLETED
            )
        )
        .first()

    )


    if not review_item:

        return redirect(
            "vocabulary:dashboard_start"
        )


    word_ids = (
        review_item.review_word_ids
        or
        []
    )


    words_by_id = {

        word.id:
            word

        for word in (

            VocabularyWord.objects
            .filter(
                id__in=word_ids,
                is_active=True,
            )

        )

    }


    words = [

        words_by_id[
            word_id
        ]

        for word_id in word_ids

        if word_id
        in
        words_by_id

    ]


    if not words:

        review_item.status = (
            DailyStudyPlanItem
            .Status
            .COMPLETED
        )

        review_item.completed_at = (
            timezone.now()
        )

        review_item.save(
            update_fields=[
                "status",
                "completed_at",
                "updated_at",
            ]
        )


        return redirect(
            "vocabulary:dashboard_start"
        )


    if (
        review_item.status
        ==
        DailyStudyPlanItem
        .Status
        .PLANNED
    ):

        review_item.status = (
            DailyStudyPlanItem
            .Status
            .IN_PROGRESS
        )

        review_item.started_at = (
            timezone.now()
        )

        review_item.save(
            update_fields=[
                "status",
                "started_at",
                "updated_at",
            ]
        )


    review_data = [

        {

            "id":
                word.id,

            "word":
                word.word,

            "part_of_speech":
                word.part_of_speech,

            "translation_ru":
                word.translation_ru,

            "example_en":
                word.example_en,

        }

        for word in words

    ]


    return render(
        request,
        "vocabulary/daily_review.html",
        {

            "course":
                course,

            "plan":
                plan,

            "review_item":
                review_item,

            "review_data":
                review_data,

            "word_count":
                len(
                    review_data
                ),

        },
    )

