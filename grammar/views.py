from django.contrib.auth.decorators import login_required
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

    lessons = (
        GrammarLesson.objects
        .filter(is_published=True)
        .order_by(
            "level",
            "order",
        )
    )

    progress_map = {
        progress.lesson_id: progress
        for progress in (
            GrammarLessonProgress.objects
            .filter(
                user=request.user,
                lesson__in=lessons,
            )
        )
    }

    lesson_cards = []

    for lesson in lessons:
        lesson_cards.append(
            {
                "lesson": lesson,
                "progress": progress_map.get(
                    lesson.id
                ),
            }
        )

    return render(
        request,
        "grammar/home.html",
        {
            "lesson_cards": lesson_cards,
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
        == GrammarLessonProgress.Status.NOT_STARTED
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

    return render(
        request,
        "grammar/lesson.html",
        {
            "lesson": lesson,
            "progress": progress,
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

    progress, _ = (
        GrammarLessonProgress.objects
        .get_or_create(
            user=request.user,
            lesson=lesson,
        )
    )

    try:
        score = int(
            request.POST.get(
                "score",
                100,
            )
        )
    except (TypeError, ValueError):
        score = 100

    score = max(
        0,
        min(
            score,
            100,
        ),
    )

    progress.status = (
        GrammarLessonProgress.Status.COMPLETED
    )

    progress.score = score

    if not progress.started_at:
        progress.started_at = timezone.now()

    progress.completed_at = timezone.now()

    progress.save(
        update_fields=[
            "status",
            "score",
            "started_at",
            "completed_at",
            "updated_at",
        ]
    )

    return redirect(
        "grammar:lesson",
        slug=lesson.slug,
    )
