from django.contrib import admin




from .models import (
    UserWordProgress,
    VocabularyGroup,
    VocabularyLesson,
    VocabularyLevel,
    VocabularyWord,
)


@admin.register(VocabularyLevel)
class VocabularyLevelAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )


@admin.register(VocabularyGroup)
class VocabularyGroupAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "order",
    )

    list_filter = (
        "level",
    )

    search_fields = (
        "name",
    )


@admin.register(VocabularyLesson)
class VocabularyLessonAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "group",
        "global_number",
        "order",
        "is_active",
    )

    list_filter = (
        "group__level",
        "group",
    )


@admin.register(VocabularyWord)
class VocabularyWordAdmin(admin.ModelAdmin):
    list_display = (
        "word",
        "part_of_speech",
        "lesson",
        "translation_ru",
        "translation_kz",
    )

    list_filter = (
        "lesson__group__level",
        "lesson__group",
        "part_of_speech",
    )

    search_fields = (
        "word",
        "translation_ru",
        "translation_kz",
    )


@admin.register(UserWordProgress)
class UserWordProgressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "word",
        "status",
        "correct_answers",
        "wrong_answers",
        "repetitions",
        "interval_days",
        "next_review",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "user__username",
        "word__word",
    )