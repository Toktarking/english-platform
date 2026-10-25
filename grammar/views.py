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

    sections = list(
        lesson.sections
        .all()
        .order_by("order")
    )

    exercises = list(
        lesson.exercises
        .filter(
            is_published=True
        )
        .order_by("order")
    )

    return render(
        request,
        "grammar/lesson.html",
        {
            "lesson": lesson,
            "progress": progress,
            "sections": sections,
            "exercises": exercises,
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

    exercises = list(
        lesson.exercises
        .filter(
            is_published=True
        )
        .order_by("order")
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

        if submitted == expected:
            correct += 1

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
            GrammarLessonProgress.Status.COMPLETED
        )

        # Идемпотентно:
        # повторное прохождение не удваивает XP.
        progress.xp_earned = lesson.xp_reward

        if not progress.completed_at:
            progress.completed_at = timezone.now()

    else:
        progress.status = (
            GrammarLessonProgress.Status.IN_PROGRESS
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

    return redirect(
        "grammar:lesson",
        slug=lesson.slug,
    )
