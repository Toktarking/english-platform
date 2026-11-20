import json

from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Sum
from django.http import JsonResponse
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import (
    GrammarAssessmentQuestion,
    GrammarBlock,
    GrammarBlockPracticeProgress,
    GrammarDailyProgress,
    GrammarLesson,
    GrammarLessonProgress,
    GrammarPlacementAttempt,
    GrammarStudyPlan,
    GrammarStudyPlanItem,
    GrammarTopicAssessment,
)

from .placement import (
    get_knowledge_summary,
    get_next_question,
    get_personal_plan,
    record_answer,
    start_placement,
)


from .course_plan import (
    get_active_vocabulary_course,
    get_first_incomplete_lesson,
    get_grammar_calendar,
    get_required_grammar_step,
    get_today_grammar_rows,
    sync_grammar_plan,
    update_grammar_daily_progress,
)

from .study_plan import (
    build_study_plan,
    get_active_study_plan,
    get_plan_calendar,
)


from .exam_practice import (
    get_current_exam_question,
    get_exam_state,
    start_exam_session,
    submit_exam_answer,
)


def _lesson_content(lesson):

    sections = list(
        lesson.sections
        .all()
        .order_by("order")
    )

    exercises = list(
        lesson.exercises
        .filter(is_published=True)
        .order_by("order")
    )

    return sections, exercises


def _review_session_key(lesson):

    return (
        f"grammar_attempt_review_"
        f"{lesson.id}"
    )




@login_required
def placement_disabled(request):

    return redirect(
        "grammar:home"
    )


@login_required
def grammar_home(request):

    today = (
        timezone.localdate()
    )

    course = (
        get_active_vocabulary_course(
            request.user
        )
    )


    if course is None:

        return render(
            request,
            "grammar/home.html",
            {
                "needs_course": True,
                "today": today,
            },
        )


    plan = (
        sync_grammar_plan(
            request.user
        )
    )


    today_rows = (
        get_today_grammar_rows(
            plan
        )
        if plan
        else []
    )


    today_total = len(
        today_rows
    )


    today_completed = sum(
        1
        for row in today_rows
        if row["completed"]
    )


    today_minutes = sum(
        row["estimated_minutes"]
        for row in today_rows
    )


    today_percent = (
        round(
            today_completed
            /
            today_total
            *
            100
        )
        if today_total
        else 100
    )


    if plan:

        grammar_day_number = max(
            1,
            (
                today
                -
                plan.start_date
            ).days
            +
            1,
        )

    else:

        grammar_day_number = 1


    next_row = next(
        (
            row
            for row in today_rows
            if row["is_next"]
        ),
        None,
    )


    next_url = None


    if next_row:

        if (
            next_row["type"]
            ==
            "practice"
        ):

            next_url = (
                reverse(
                    "grammar:block_practice",
                    kwargs={
                        "block_order":
                            next_row[
                                "block"
                            ].order,
                    },
                )
                +
                "?new=1"
            )

        else:

            next_url = reverse(
                "grammar:lesson",
                kwargs={
                    "slug":
                        next_row[
                            "lesson"
                        ].slug,
                },
            )


    return render(
        request,
        "grammar/home.html",
        {
            "needs_course": False,

            "today":
                today,

            "plan":
                plan,

            "today_rows":
                today_rows,

            "today_total":
                today_total,

            "today_completed":
                today_completed,

            "today_minutes":
                today_minutes,

            "today_percent":
                today_percent,

            "grammar_day_number":
                grammar_day_number,

            "next_url":
                next_url,

            "has_activity":
                today_completed > 0,
        },
    )

@login_required
def grammar_lesson(request, slug):

    lesson = get_object_or_404(
        GrammarLesson,
        slug=slug,
        is_published=True,
    )

    # REQUIRED GRAMMAR ORDER

    existing_progress = (
        GrammarLessonProgress.objects
        .filter(
            user=request.user,
            lesson=lesson,
        )
        .first()
    )


    already_completed = (
        existing_progress is not None

        and

        existing_progress.status
        ==
        GrammarLessonProgress
        .Status
        .COMPLETED
    )


    if not already_completed:

        required_step = (
            get_required_grammar_step(
                request.user
            )
        )


        if (
            required_step[
                "type"
            ]
            ==
            "practice"
        ):

            return redirect(
                "grammar:home"
            )


        if (
            required_step[
                "type"
            ]
            ==
            "lesson"
        ):

            required_lesson = (
                required_step[
                    "lesson"
                ]
            )


            if (
                lesson.id
                !=
                required_lesson.id
            ):

                return redirect(
                    "grammar:lesson",
                    slug=(
                        required_lesson.slug
                    ),
                )


    progress, _ = (
        GrammarLessonProgress.objects
        .get_or_create(
            user=request.user,
            lesson=lesson,
        )
    )

    if (
        progress.status
        ==
        GrammarLessonProgress.Status.NOT_STARTED
    ):
        progress.status = (
            GrammarLessonProgress.Status.IN_PROGRESS
        )

        progress.started_at = timezone.now()

        progress.save(
            update_fields=[
                "status",
                "started_at",
                "updated_at",
            ]
        )

    sections, exercises = (
        _lesson_content(lesson)
    )

    final_test_exercises = [
        exercise
        for exercise in exercises
        if exercise.section_id is None
    ]


    # =====================================================
    # RESUME INTERACTIVE LESSON
    # =====================================================

    training_exercises = [
        exercise
        for exercise in exercises
        if exercise.section_id is not None
    ]

    training_step_count = (
        len(sections)
        +
        len(training_exercises)
    )


    if training_step_count > 0:

        saved_step_index = min(
            progress.current_step_index,
            training_step_count - 1,
        )

    else:

        saved_step_index = 0


    start_with_final = (
        request.GET.get("final")
        == "1"
    )

    start_with_practice = (
        request.GET.get("practice")
        == "1"
    )

    attempt_result = (
        request.session.pop(
            _review_session_key(lesson),
            None,
        )
    )

    wrong_results = []

    if attempt_result:

        wrong_results = (
            attempt_result.pop(
                "wrong_results",
                [],
            )
        )

    # Если пользователь уже прошёл всю тренировку
    # и вернулся позже с другого устройства,
    # сразу продолжаем с Final Test.
    if (
        not attempt_result

        and

        progress.status
        !=
        GrammarLessonProgress.Status.COMPLETED

        and

        training_step_count > 0

        and

        progress.current_step_index
        >=
        training_step_count
    ):

        return redirect(
            "grammar:final_test",
            slug=lesson.slug,
        )


    template_name = (
        "grammar/lesson_interactive.html"
        if 1 <= lesson.order <= 50
        else
        "grammar/lesson.html"
    )

    return render(
        request,
        template_name,
        {
            "lesson": lesson,
            "progress": progress,
            "sections": sections,
            "exercises": exercises,

            "start_with_practice":
                start_with_practice,

            "attempt_result":
                attempt_result,

            "wrong_results":
                wrong_results,

            "final_test_exercises":
                final_test_exercises,

            "saved_step_index":
                saved_step_index,

            "start_with_final":
                start_with_final,
        },
    )


@login_required
@require_POST
@transaction.atomic
def grammar_lesson_study_progress(
    request,
    slug,
):

    lesson = get_object_or_404(
        GrammarLesson,
        slug=slug,
        is_published=True,
    )


    try:

        data = json.loads(
            request.body
        )

        requested_index = int(
            data.get(
                "current_step_index",
                0,
            )
        )

    except (
        json.JSONDecodeError,
        TypeError,
        ValueError,
    ):

        return JsonResponse(
            {
                "success": False,
                "error": "Invalid progress data.",
            },
            status=400,
        )


    section_count = (
        lesson.sections.count()
    )

    training_exercise_count = (
        lesson.exercises
        .filter(
            is_published=True,
            section__isnull=False,
        )
        .count()
    )


    total_steps = (
        section_count
        +
        training_exercise_count
    )


    if total_steps <= 0:

        return JsonResponse(
            {
                "success": False,
                "error": "Lesson has no training steps.",
            },
            status=400,
        )


    # total_steps разрешён как специальное значение:
    # пользователь полностью прошёл training
    # и следующим экраном должен быть Final Test.
    requested_index = max(
        0,
        min(
            requested_index,
            total_steps,
        ),
    )


    progress, _ = (
        GrammarLessonProgress.objects
        .select_for_update()
        .get_or_create(
            user=request.user,
            lesson=lesson,
        )
    )


    if (
        progress.status
        !=
        GrammarLessonProgress.Status.COMPLETED
    ):

        # Прогресс не откатываем назад.
        # Пользователь может нажимать "назад" для просмотра,
        # но при новом входе продолжит с самой дальней точки.
        progress.current_step_index = max(
            progress.current_step_index,
            requested_index,
        )

        progress.max_seen_step_index = max(
            progress.max_seen_step_index,
            requested_index,
        )


        if (
            progress.status
            ==
            GrammarLessonProgress.Status.NOT_STARTED
        ):

            progress.status = (
                GrammarLessonProgress.Status.IN_PROGRESS
            )


        if progress.started_at is None:

            progress.started_at = (
                timezone.now()
            )


        progress.save()


    return JsonResponse(
        {
            "success": True,

            "current_step_index":
                progress.current_step_index,

            "max_seen_step_index":
                progress.max_seen_step_index,

            "training_finished":
                (
                    progress.current_step_index
                    >=
                    total_steps
                ),
        }
    )


@login_required
def grammar_final_test(
    request,
    slug,
):

    lesson = get_object_or_404(
        GrammarLesson,
        slug=slug,
        is_published=True,
    )

    progress, _ = (
        GrammarLessonProgress.objects
        .get_or_create(
            user=request.user,
            lesson=lesson,
        )
    )

    if (
        progress.status
        ==
        GrammarLessonProgress
        .Status
        .COMPLETED
    ):

        return redirect(
            "grammar:lesson",
            slug=lesson.slug,
        )

    final_test_exercises = list(
        lesson.exercises
        .filter(
            is_published=True,
            section__isnull=True,
        )
        .order_by("order")
    )

    if not final_test_exercises:

        return redirect(
            "grammar:lesson",
            slug=lesson.slug,
        )

    return render(
        request,
        "grammar/final_test.html",
        {
            "lesson":
                lesson,

            "progress":
                progress,

            "final_test_exercises":
                final_test_exercises,
        },
    )


@login_required
def complete_lesson(request, slug):

    lesson = get_object_or_404(
        GrammarLesson,
        slug=slug,
        is_published=True,
    )

    if request.method != "POST":
        return redirect(
            "grammar:lesson",
            slug=lesson.slug,
        )

    _, exercises = (
        _lesson_content(lesson)
    )

    final_test_exercises = [
        exercise
        for exercise in exercises
        if exercise.section_id is None
    ]

    scored_exercises = (
        final_test_exercises
        or
        exercises
    )

    progress, _ = (
        GrammarLessonProgress.objects
        .get_or_create(
            user=request.user,
            lesson=lesson,
        )
    )

    if not progress.started_at:
        progress.started_at = timezone.now()

    total = len(scored_exercises)
    correct = 0

    wrong_results = []

    for exercise in scored_exercises:

        submitted = (
            request.POST
            .get(
                f"answer_{exercise.id}",
                "",
            )
            .strip()
        )

        expected = (
            exercise.correct_answer
            .strip()
        )

        normalized_submitted = (
            " ".join(
                submitted
                .casefold()
                .split()
            )
        )

        normalized_expected = (
            " ".join(
                expected
                .casefold()
                .split()
            )
        )

        is_correct = (
            normalized_submitted
            ==
            normalized_expected
        )

        if is_correct:

            correct += 1

        else:

            wrong_results.append(
                {
                    "order":
                        exercise.order,

                    "prompt":
                        exercise.prompt,

                    "submitted":
                        (
                            submitted
                            or
                            "Нет ответа"
                        ),

                    "correct_answer":
                        expected,

                    "explanation":
                        exercise.explanation,
                }
            )

    score = (
        round(
            correct
            / total
            * 100
        )
        if total
        else 0
    )

    passed = (
        total > 0
        and
        score >= lesson.pass_score
    )

    progress.score = score
    progress.correct_answers = correct
    progress.total_questions = total

    if passed:

        progress.status = (
            GrammarLessonProgress
            .Status
            .COMPLETED
        )

        progress.xp_earned = (
            lesson.xp_reward
        )

        if not progress.completed_at:
            progress.completed_at = (
                timezone.now()
            )

    else:

        progress.status = (
            GrammarLessonProgress
            .Status
            .IN_PROGRESS
        )

        progress.xp_earned = 0
        progress.completed_at = None

    progress.save(
        update_fields=[
            "status",
            "score",
            "correct_answers",
            "total_questions",
            "xp_earned",
            "started_at",
            "completed_at",
            "updated_at",
        ]
    )

    # Grammar day counts only when ALL
    # scheduled Grammar tasks are completed.
    if passed:

        update_grammar_daily_progress(
            request.user
        )


    # Sync successful lesson with Knowledge Map
    # and remove its normal task from the active Daily Plan.
    if passed:

        GrammarTopicAssessment.objects.update_or_create(
            user=request.user,
            lesson=lesson,
            defaults={
                "status": (
                    GrammarTopicAssessment
                    .Status
                    .MASTERED
                ),
                "source": (
                    GrammarTopicAssessment
                    .Source
                    .LESSON
                ),
                "correct_answers": correct,
                "total_questions": total,
            },
        )



    # Сохраняем результат одной попытки.
    # После redirect страница сможет показать,
    # где именно пользователь ошибся.
    request.session[
        _review_session_key(lesson)
    ] = {
        "passed":
            passed,

        "score":
            score,

        "correct":
            correct,

        "total":
            total,

        "wrong_results":
            wrong_results,
    }

    return redirect(
        "grammar:lesson",
        slug=lesson.slug,
    )

@login_required
def grammar_placement(request):

    attempt = (
        GrammarPlacementAttempt.objects
        .filter(
            user=request.user,
            status=(
                GrammarPlacementAttempt
                .Status
                .IN_PROGRESS
            ),
        )
        .order_by("-started_at")
        .first()
    )

    if attempt is None:

        completed = (
            GrammarPlacementAttempt.objects
            .filter(
                user=request.user,
                status=(
                    GrammarPlacementAttempt
                    .Status
                    .COMPLETED
                ),
            )
            .order_by("-completed_at")
            .first()
        )

        if completed:
            return redirect(
                "grammar:placement_result"
            )

        return render(
            request,
            "grammar/placement.html",
            {
                "mode": "intro",
            },
        )

    question = get_next_question(
        attempt
    )

    attempt.refresh_from_db()

    if question is None:
        return redirect(
            "grammar:placement_result"
        )

    if (
        attempt.stage
        ==
        GrammarPlacementAttempt
        .Stage
        .SCREENING
    ):

        answered = (
            attempt.answers
            .filter(
                assessment_question__role=(
                    "SCREENING"
                ),
            )
            .count()
        )

        stage_total = 40

        progress_pct = round(
            answered
            / stage_total
            * 100
        )

        phase_title = (
            "Этап 1 · Базовая диагностика"
        )

        progress_text = (
            f"{answered + 1} из {stage_total}"
        )

        context_label = (
            f"Блок "
            f"{question.exercise.lesson.block.order}"
            f" · "
            f"{question.exercise.lesson.block.title}"
        )

    else:

        answered = (
            attempt.answers
            .filter(
                assessment_question__role="TOPIC",
            )
            .count()
        )

        unresolved_topics = (
            GrammarTopicAssessment.objects
            .filter(
                user=request.user,
                status=(
                    GrammarTopicAssessment
                    .Status
                    .UNKNOWN
                ),
            )
            .count()
        )

        resolved_topics = (
            GrammarTopicAssessment.objects
            .filter(
                user=request.user,
                source=(
                    GrammarTopicAssessment
                    .Source
                    .PLACEMENT_TOPIC
                ),
            )
            .count()
        )

        stage_total = (
            unresolved_topics
            + resolved_topics
        ) * 2

        if stage_total < answered + 1:
            stage_total = answered + 1

        progress_pct = (
            round(
                answered
                / stage_total
                * 100
            )
            if stage_total
            else 0
        )

        phase_title = (
            "Этап 2 · Уточнение слабых тем"
        )

        progress_text = (
            f"{answered + 1} из {stage_total}"
            if stage_total
            else
            f"Вопрос {answered + 1}"
        )

        context_label = (
            question.exercise.lesson.title
        )

    return render(
        request,
        "grammar/placement.html",
        {
            "mode": "question",
            "attempt": attempt,
            "question": question,
            "exercise": question.exercise,
            "phase_title": phase_title,
            "progress_text": progress_text,
            "progress_pct": progress_pct,
            "context_label": context_label,
        },
    )


@login_required
def start_grammar_placement(request):

    if request.method != "POST":
        return redirect(
            "grammar:placement"
        )

    start_placement(
        request.user
    )

    return redirect(
        "grammar:placement"
    )


@login_required
def answer_grammar_placement(request):

    if request.method != "POST":
        return redirect(
            "grammar:placement"
        )

    attempt = get_object_or_404(
        GrammarPlacementAttempt,
        pk=request.POST.get("attempt_id"),
        user=request.user,
        status=(
            GrammarPlacementAttempt
            .Status
            .IN_PROGRESS
        ),
    )

    assessment_question = get_object_or_404(
        GrammarAssessmentQuestion,
        pk=request.POST.get("question_id"),
        is_active=True,
    )

    current_question = get_next_question(
        attempt
    )

    if current_question is None:
        return redirect(
            "grammar:placement_result"
        )

    # Prevent skipping or answering another question.
    if (
        current_question.id
        != assessment_question.id
    ):
        return redirect(
            "grammar:placement"
        )

    selected_answer = (
        request.POST
        .get(
            "answer",
            "",
        )
        .strip()
    )

    allowed_answers = [
        str(option)
        for option in (
            current_question
            .exercise
            .options
        )
    ]

    if selected_answer not in allowed_answers:
        return redirect(
            "grammar:placement"
        )

    record_answer(
        attempt=attempt,
        assessment_question=current_question,
        selected_answer=selected_answer,
    )

    attempt.refresh_from_db()

    if (
        attempt.status
        ==
        GrammarPlacementAttempt
        .Status
        .COMPLETED
    ):
        return redirect(
            "grammar:placement_result"
        )

    return redirect(
        "grammar:placement"
    )


@login_required
def grammar_placement_result(request):

    attempt = (
        GrammarPlacementAttempt.objects
        .filter(
            user=request.user,
            status=(
                GrammarPlacementAttempt
                .Status
                .COMPLETED
            ),
        )
        .order_by("-completed_at")
        .first()
    )

    if attempt is None:
        return redirect(
            "grammar:placement"
        )

    summary = get_knowledge_summary(
        request.user
    )

    mastered = (
        summary.get(
            GrammarTopicAssessment
            .Status
            .MASTERED,
            0,
        )
        +
        summary.get(
            GrammarTopicAssessment
            .Status
            .PROVISIONAL_MASTERED,
            0,
        )
    )

    review = summary.get(
        GrammarTopicAssessment.Status.REVIEW,
        0,
    )

    learn = summary.get(
        GrammarTopicAssessment.Status.LEARN,
        0,
    )

    plan_items = list(
        get_personal_plan(
            request.user
        )
    )

    next_item = (
        plan_items[0]
        if plan_items
        else None
    )

    plan_groups = []

    blocks = (
        GrammarBlock.objects
        .filter(
            level="A1",
            is_published=True,
        )
        .order_by("order")
    )

    for block in blocks:

        items = [
            item
            for item in plan_items
            if (
                item.lesson.block_id
                == block.id
            )
        ]

        if items:
            plan_groups.append(
                {
                    "block": block,
                    "items": items,
                }
            )

    return render(
        request,
        "grammar/placement.html",
        {
            "mode": "result",
            "attempt": attempt,
            "mastered": mastered,
            "review": review,
            "learn": learn,
            "plan_count": len(plan_items),
            "plan_groups": plan_groups,
            "next_item": next_item,
        },
    )







@login_required
def grammar_plan_setup(request):

    course = (
        get_active_vocabulary_course(
            request.user
        )
    )

    if course is None:

        return redirect(
            "vocabulary:course_setup"
        )

    sync_grammar_plan(
        request.user
    )

    return redirect(
        "grammar:plan"
    )


@login_required
def grammar_plan(request):

    plan = (
        sync_grammar_plan(
            request.user
        )
    )


    if plan is None:

        return redirect(
            "vocabulary:course_setup"
        )


    calendar = (
        get_grammar_calendar(
            plan
        )
    )


    today = (
        timezone.localdate()
    )


    today_day = next(
        (
            day

            for day in calendar

            if day["is_today"]
        ),
        None,
    )


    days_remaining = max(
        0,
        (
            plan.exam_date
            -
            today
        ).days
        +
        1,
    )


    completed_ids = set(
        GrammarLessonProgress.objects
        .filter(
            user=request.user,
            lesson__level="A1",
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


    total_lessons = (
        GrammarLesson.objects
        .filter(
            level="A1",
            order__range=(1, 60),
            is_published=True,
        )
        .count()
    )


    remaining_lessons = max(
        0,
        (
            total_lessons
            -
            len(completed_ids)
        ),
    )


    return render(
        request,
        "grammar/study_plan.html",
        {
            "plan":
                plan,

            "calendar":
                calendar,

            "today_day":
                today_day,

            "days_remaining":
                days_remaining,

            "remaining_lessons":
                remaining_lessons,

            "total_days":
                len(calendar),
        },
    )


@login_required
def grammar_exam_practice(request):

    state = get_exam_state(
        request
    )

    if not state:

        return render(
            request,
            "grammar/exam_practice.html",
            {
                "mode": "intro",
            },
        )

    question = (
        get_current_exam_question(
            request
        )
    )

    if question is None:

        total = len(
            state.get(
                "question_ids",
                [],
            )
        )

        correct = state.get(
            "correct",
            0,
        )

        score = (
            round(
                correct
                / total
                * 100
            )
            if total
            else 0
        )

        wrong_answers = [
            answer
            for answer in state.get(
                "answers",
                [],
            )
            if (
                not answer.get(
                    "is_correct"
                )
            )
        ]

        return render(
            request,
            "grammar/exam_practice.html",
            {
                "mode": "result",
                "correct": correct,
                "total": total,
                "score": score,
                "wrong_answers":
                    wrong_answers,
            },
        )

    total = len(
        state.get(
            "question_ids",
            [],
        )
    )

    index = state.get(
        "index",
        0,
    )

    progress_pct = (
        round(
            index
            / total
            * 100
        )
        if total
        else 0
    )

    return render(
        request,
        "grammar/exam_practice.html",
        {
            "mode": "question",
            "exercise": question,
            "question_number":
                index + 1,
            "total": total,
            "progress_pct":
                progress_pct,
        },
    )


@login_required
def start_grammar_exam_practice(
    request
):

    if request.method != "POST":

        return redirect(
            "grammar:exam_practice"
        )

    start_exam_session(
        request,
        count=20,
    )

    return redirect(
        "grammar:exam_practice"
    )


@login_required
def answer_grammar_exam_practice(
    request
):

    if request.method != "POST":

        return redirect(
            "grammar:exam_practice"
        )

    question = (
        get_current_exam_question(
            request
        )
    )

    if question is None:

        return redirect(
            "grammar:exam_practice"
        )

    selected_answer = (
        request.POST
        .get(
            "answer",
            "",
        )
        .strip()
    )

    if not selected_answer:

        return redirect(
            "grammar:exam_practice"
        )

    try:

        submit_exam_answer(
            request,
            selected_answer,
        )

    except ValueError:

        return redirect(
            "grammar:exam_practice"
        )

    return redirect(
        "grammar:exam_practice"
    )



@login_required
def grammar_balance(request):

    completed = (
        GrammarLessonProgress.objects
        .filter(
            user=request.user,
            lesson__level="A1",
            lesson__order__range=(1, 60),
            status=(
                GrammarLessonProgress
                .Status
                .COMPLETED
            ),
        )
    )


    total_xp = (
        completed
        .aggregate(
            total=Sum(
                "xp_earned"
            )
        )
        ["total"]
        or 0
    )


    possible_xp = (
        GrammarLesson.objects
        .filter(
            level="A1",
            order__range=(1, 60),
            is_published=True,
        )
        .aggregate(
            total=Sum(
                "xp_reward"
            )
        )
        ["total"]
        or 0
    )


    recent = (
        completed
        .select_related(
            "lesson",
            "lesson__block",
        )
        .order_by(
            "-completed_at"
        )[:10]
    )


    return render(
        request,
        "grammar/balance.html",
        {
            "total_xp":
                total_xp,

            "possible_xp":
                possible_xp,

            "completed_lessons":
                completed.count(),

            "recent":
                recent,
        },
    )


@login_required
def grammar_rewards(request):

    completed_lessons = (
        GrammarLessonProgress.objects
        .filter(
            user=request.user,
            lesson__level="A1",
            lesson__order__range=(1, 60),
            status=(
                GrammarLessonProgress
                .Status
                .COMPLETED
            ),
        )
        .count()
    )


    total_xp = (
        GrammarLessonProgress.objects
        .filter(
            user=request.user,
            lesson__level="A1",
            status=(
                GrammarLessonProgress
                .Status
                .COMPLETED
            ),
        )
        .aggregate(
            total=Sum(
                "xp_earned"
            )
        )
        ["total"]
        or 0
    )


    completed_practices = set(
        GrammarBlockPracticeProgress.objects
        .filter(
            user=request.user,
            is_completed=True,
            block__level="A1",
        )
        .values_list(
            "block__order",
            flat=True,
        )
    )


    rewards = [
        {
            "icon": "🌱",
            "title": "Первый шаг",
            "description": "Завершить первый Grammar Lesson",
            "unlocked": completed_lessons >= 1,
            "progress": f"{min(completed_lessons, 1)}/1",
        },
        {
            "icon": "⚡",
            "title": "Разгон",
            "description": "Завершить 5 Grammar Lessons",
            "unlocked": completed_lessons >= 5,
            "progress": f"{min(completed_lessons, 5)}/5",
        },
        {
            "icon": "📘",
            "title": "Первый блок",
            "description": "Завершить 10 Grammar Lessons",
            "unlocked": completed_lessons >= 10,
            "progress": f"{min(completed_lessons, 10)}/10",
        },
        {
            "icon": "🎯",
            "title": "Practice 1",
            "description": "Пройти первый Grammar Practice",
            "unlocked": 1 in completed_practices,
            "progress": (
                "1/1"
                if 1 in completed_practices
                else "0/1"
            ),
        },
        {
            "icon": "🔥",
            "title": "20 тем",
            "description": "Завершить 20 Grammar Lessons",
            "unlocked": completed_lessons >= 20,
            "progress": f"{min(completed_lessons, 20)}/20",
        },
        {
            "icon": "🏆",
            "title": "Practice 2",
            "description": "Пройти второй Grammar Practice",
            "unlocked": 2 in completed_practices,
            "progress": (
                "1/1"
                if 2 in completed_practices
                else "0/1"
            ),
        },
        {
            "icon": "🚀",
            "title": "30 тем",
            "description": "Завершить половину курса Grammar",
            "unlocked": completed_lessons >= 30,
            "progress": f"{min(completed_lessons, 30)}/30",
        },
        {
            "icon": "💎",
            "title": "Practice 3",
            "description": "Пройти третий Grammar Practice",
            "unlocked": 3 in completed_practices,
            "progress": (
                "1/1"
                if 3 in completed_practices
                else "0/1"
            ),
        },
        {
            "icon": "👑",
            "title": "Grammar Master",
            "description": "Завершить все 60 Grammar Lessons",
            "unlocked": completed_lessons >= 60,
            "progress": f"{min(completed_lessons, 60)}/60",
        },
    ]


    unlocked_count = sum(
        1
        for reward in rewards
        if reward["unlocked"]
    )


    return render(
        request,
        "grammar/rewards.html",
        {
            "rewards":
                rewards,

            "unlocked_count":
                unlocked_count,

            "reward_count":
                len(rewards),

            "total_xp":
                total_xp,
        },
    )


@login_required
def grammar_profile(request):

    today = (
        timezone.localdate()
    )


    # =====================================================
    # LESSON PROGRESS
    # =====================================================

    completed = (
        GrammarLessonProgress.objects
        .filter(
            user=request.user,
            lesson__level="A1",
            lesson__order__range=(1, 60),
            status=(
                GrammarLessonProgress
                .Status
                .COMPLETED
            ),
        )
    )


    completed_lessons = (
        completed.count()
    )


    total_lessons = (
        GrammarLesson.objects
        .filter(
            level="A1",
            order__range=(1, 60),
            is_published=True,
        )
        .count()
    )


    lesson_percent = (
        round(
            completed_lessons
            /
            total_lessons
            *
            100
        )
        if total_lessons
        else 0
    )


    stats = (
        completed
        .aggregate(
            total_xp=Sum(
                "xp_earned"
            ),

            avg_score=Avg(
                "score"
            ),
        )
    )


    total_xp = (
        stats[
            "total_xp"
        ]
        or 0
    )


    avg_score = round(
        stats[
            "avg_score"
        ]
        or 0
    )


    # =====================================================
    # PRACTICE PROGRESS
    # =====================================================

    practices_completed = (
        GrammarBlockPracticeProgress.objects
        .filter(
            user=request.user,
            block__level="A1",
            block__order__in=[
                1,
                2,
                3,
            ],
            is_completed=True,
        )
        .count()
    )


    total_practices = 3


    # =====================================================
    # DAYS REMAINING
    # =====================================================

    plan = (
        sync_grammar_plan(
            request.user
        )
    )


    days_remaining = 0


    if plan:

        days_remaining = max(
            0,
            (
                plan.exam_date
                -
                today
            ).days
            +
            1,
        )


    # =====================================================
    # COMPLETED GRAMMAR DAYS
    #
    # День попадает сюда только после выполнения
    # ВСЕГО Grammar-плана этого дня.
    # Vocabulary не участвует.
    # =====================================================

    activity_dates = set(
        GrammarDailyProgress.objects
        .filter(
            user=request.user,
            is_completed=True,
        )
        .values_list(
            "date",
            flat=True,
        )
    )


    # Проверим сегодняшний день на случай,
    # если пользователь только что всё завершил.
    today_progress = (
        update_grammar_daily_progress(
            request.user,
            target_date=today,
        )
    )


    if (
        today_progress is not None
        and
        today_progress.is_completed
    ):

        activity_dates.add(
            today
        )


    # =====================================================
    # STREAK
    # =====================================================

    streak = 0


    cursor = today


    # Если сегодня ещё не было Grammar,
    # разрешаем streak продолжаться со вчера.
    if (
        cursor
        not in activity_dates
    ):

        cursor = (
            cursor
            -
            timedelta(
                days=1
            )
        )


    while (
        cursor
        in activity_dates
    ):

        streak += 1

        cursor = (
            cursor
            -
            timedelta(
                days=1
            )
        )


    # =====================================================
    # CURRENT WEEK
    # Monday -> Sunday
    # =====================================================

    week_start = (
        today
        -
        timedelta(
            days=today.weekday()
        )
    )


    week_days = []


    weekday_names = [
        "Пн",
        "Вт",
        "Ср",
        "Чт",
        "Пт",
        "Сб",
        "Вс",
    ]


    for index in range(
        7
    ):

        current_date = (
            week_start
            +
            timedelta(
                days=index
            )
        )


        completed_day = (
            current_date
            in activity_dates
        )


        if completed_day:

            state = "completed"

        elif current_date == today:

            state = "today"

        elif current_date < today:

            state = "missed"

        else:

            state = "future"


        week_days.append(
            {
                "name":
                    weekday_names[
                        index
                    ],

                "date":
                    current_date,

                "state":
                    state,

                "completed":
                    completed_day,

                "is_today":
                    (
                        current_date
                        ==
                        today
                    ),
            }
        )


    week_completed = sum(
        1

        for day in week_days

        if day[
            "completed"
        ]
    )


    return render(
        request,
        "grammar/profile.html",
        {
            "completed_lessons":
                completed_lessons,

            "total_lessons":
                total_lessons,

            "lesson_percent":
                lesson_percent,

            "total_xp":
                total_xp,

            "avg_score":
                avg_score,

            "practices_completed":
                practices_completed,

            "total_practices":
                total_practices,

            "days_remaining":
                days_remaining,

            "streak":
                streak,

            "week_days":
                week_days,

            "week_completed":
                week_completed,
        },
    )
