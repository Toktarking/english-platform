from django.contrib import admin

from .models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonProgress,
    GrammarLessonSection,
)


class GrammarLessonSectionInline(
    admin.StackedInline
):
    model = GrammarLessonSection
    extra = 0


class GrammarExerciseInline(
    admin.StackedInline
):
    model = GrammarExercise
    extra = 0


@admin.register(GrammarLesson)
class GrammarLessonAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "title",
        "level",
        "pass_score",
        "xp_reward",
        "is_published",
    )

    list_filter = (
        "level",
        "is_published",
    )

    search_fields = (
        "title",
        "slug",
    )

    prepopulated_fields = {
        "slug": (
            "title",
        ),
    }

    inlines = [
        GrammarLessonSectionInline,
        GrammarExerciseInline,
    ]


@admin.register(GrammarLessonSection)
class GrammarLessonSectionAdmin(
    admin.ModelAdmin
):
    list_display = (
        "lesson",
        "order",
        "title",
    )


@admin.register(GrammarExercise)
class GrammarExerciseAdmin(
    admin.ModelAdmin
):
    list_display = (
        "lesson",
        "order",
        "exercise_type",
        "is_published",
    )

    list_filter = (
        "exercise_type",
        "is_published",
    )


@admin.register(GrammarLessonProgress)
class GrammarLessonProgressAdmin(
    admin.ModelAdmin
):
    list_display = (
        "user",
        "lesson",
        "status",
        "score",
        "xp_earned",
        "completed_at",
    )

    list_filter = (
        "status",
        "lesson__level",
    )

    search_fields = (
        "user__username",
        "lesson__title",
    )
