from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone

from .models import (
    GrammarLesson,
    GrammarLessonProgress,
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

    lessons = list(
        GrammarLesson.objects
        .filter(is_published=True)
        .order_by(
            "level",
            "order",
        )
    )

    progress_list = list(
        GrammarLessonProgress.objects
        .filter(
            user=request.user,
            lesson__in=lessons,
        )
    )

    progress_map = {
        progress.lesson_id: progress
        for progress in progress_list
    }

    lesson_cards = [
        {
            "lesson": lesson,
            "progress": progress_map.get(
                lesson.id
            ),
        }
        for lesson in lessons
    ]

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

    return render(
        request,
        "grammar/home.html",
        {
            "lesson_cards": lesson_cards,
            "total_xp": total_xp,
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
