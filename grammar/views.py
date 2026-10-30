from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone

from .models import (
    GrammarAssessmentQuestion,
    GrammarBlock,
    GrammarLesson,
    GrammarLessonProgress,
    GrammarPlacementAttempt,
    GrammarTopicAssessment,
)

from .placement import (
    get_knowledge_summary,
    get_next_question,
    get_personal_plan,
    record_answer,
    start_placement,
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
def grammar_home(request):

    total_xp = (
        GrammarLessonProgress.objects
        .filter(
            user=request.user,
            status=(
                GrammarLessonProgress
                .Status
                .COMPLETED
            ),
        )
        .aggregate(
            total=Sum("xp_earned")
        )
        ["total"]
        or 0
    )

    active_attempt = (
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

    completed_placement = (
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

    # First Grammar visit:
    # do not show a catalogue of 60 lessons.
    if not completed_placement:

        return render(
            request,
            "grammar/home.html",
            {
                "needs_placement": True,
                "active_attempt": active_attempt,
                "total_xp": total_xp,
            },
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

    assessments = {
        item.lesson_id: item
        for item in (
            GrammarTopicAssessment.objects
            .filter(
                user=request.user,
                lesson__level="A1",
                lesson__order__range=(1, 60),
            )
            .select_related(
                "lesson",
                "lesson__block",
            )
        )
    }

    blocks = (
        GrammarBlock.objects
        .filter(
            level="A1",
            is_published=True,
        )
        .order_by("order")
    )

    block_rows = []

    for block in blocks:

        lessons = list(
            block.lessons
            .filter(
                level="A1",
                order__range=(1, 60),
                is_published=True,
            )
            .order_by("order")
        )

        statuses = [
            assessments[lesson.id].status
            for lesson in lessons
            if lesson.id in assessments
        ]

        known = sum(
            1
            for status in statuses
            if status in {
                GrammarTopicAssessment
                .Status
                .PROVISIONAL_MASTERED,

                GrammarTopicAssessment
                .Status
                .MASTERED,
            }
        )

        review = statuses.count(
            GrammarTopicAssessment.Status.REVIEW
        )

        learn = statuses.count(
            GrammarTopicAssessment.Status.LEARN
        )

        unknown = statuses.count(
            GrammarTopicAssessment.Status.UNKNOWN
        )

        total = len(lessons)

        percent = (
            round(
                known
                / total
                * 100
            )
            if total
            else 0
        )

        block_rows.append(
            {
                "block": block,
                "total": total,
                "known": known,
                "review": review,
                "learn": learn,
                "unknown": unknown,
                "percent": percent,
            }
        )

    return render(
        request,
        "grammar/home.html",
        {
            "needs_placement": False,
            "total_xp": total_xp,
            "placement": completed_placement,
            "plan_items": plan_items,
            "plan_count": len(plan_items),
            "next_item": next_item,
            "block_rows": block_rows,
        },
    )


@login_required
def grammar_lesson(request, slug):

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

    return render(
        request,
        "grammar/lesson.html",
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

    progress, _ = (
        GrammarLessonProgress.objects
        .get_or_create(
            user=request.user,
            lesson=lesson,
        )
    )

    if not progress.started_at:
        progress.started_at = timezone.now()

    total = len(exercises)
    correct = 0

    wrong_results = []

    for exercise in exercises:

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

        is_correct = (
            submitted == expected
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
