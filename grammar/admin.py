from django.contrib import admin

from .models import (
    GrammarLesson,
    GrammarLessonProgress,
)


@admin.register(GrammarLesson)
class GrammarLessonAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "title",
        "level",
        "is_published",
        "estimated_minutes",
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


@admin.register(GrammarLessonProgress)
class GrammarLessonProgressAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "lesson",
        "status",
        "score",
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
