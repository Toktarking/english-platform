import json

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import (
    require_GET,
    require_POST,
)

from .models import (
    UnifiedGroupPracticeSession,
    VocabularyGroup,
    VocabularyLevel,
)

from .unified_practice import (
    get_or_create_unified_practice,
    mark_unified_practice_opened,
    process_unified_answer,
    restart_unified_practice,
    serialize_unified_practice,
)

from .unified_practice_questions import (
    build_unified_question,
    check_unified_answer,
    get_current_unified_word,
)


# =========================================================
# COMPLETE STATE
# =========================================================


def serialize_complete_unified_state(
    session,
):

    state = serialize_unified_practice(
        session
    )

    state["question"] = (
        build_unified_question(
            session
        )
    )

    return state



# =========================================================
# UNIFIED PRACTICE PAGE
# =========================================================


@login_required
@require_GET
def unified_practice_page(
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

    return render(
        request,
        "vocabulary/group_practice.html",
        {
            "level":
                level,

            "group":
                group,
        },
    )

# =========================================================
# GET STATE / OPEN / CONTINUE
# =========================================================


@login_required
@require_GET
@transaction.atomic
def unified_practice_state(
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


    session = (
        get_or_create_unified_practice(
            user=request.user,
            group=group,
        )
    )


    # Блокируем существующую сессию
    # на время чтения/обновления состояния.

    session = (
        UnifiedGroupPracticeSession.objects
        .select_for_update()
        .get(
            pk=session.pk,
        )
    )


    mark_unified_practice_opened(
        session
    )


    return JsonResponse(
        {
            "success":
                True,

            "group":
                {
                    "id":
                        group.id,

                    "code":
                        group.code,

                    "name":
                        group.name,

                    "level":
                        level.code,
                },

            "state":
                serialize_complete_unified_state(
                    session
                ),
        }
    )


# =========================================================
# ANSWER
# =========================================================


@login_required
@require_POST
@transaction.atomic
def unified_practice_answer(
    request,
    group_id,
):

    try:

        data = json.loads(
            request.body.decode(
                "utf-8"
            )
        )


        word_id = int(
            data[
                "word_id"
            ]
        )


        user_answer = data.get(
            "answer",
            "",
        )


        # -------------------------------------------------
        # LOCK SESSION
        # -------------------------------------------------

        session = (
            UnifiedGroupPracticeSession.objects
            .select_for_update()
            .select_related(
                "group",
                "group__level",
            )
            .get(
                user=request.user,
                group_id=group_id,
            )
        )


        if session.is_completed:

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        (
                            "Practice is already "
                            "completed."
                        ),
                },
                status=409,
            )


        # -------------------------------------------------
        # CURRENT WORD
        # -------------------------------------------------

        current_word = (
            get_current_unified_word(
                session
            )
        )


        if current_word is None:

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        "Current word not found.",
                },
                status=409,
            )


        if (
            current_word.id
            !=
            word_id
        ):

            return JsonResponse(
                {
                    "success":
                        False,

                    "error":
                        (
                            "This is not "
                            "the current word."
                        ),
                },
                status=409,
            )


        # -------------------------------------------------
        # SERVER-SIDE CHECK
        # -------------------------------------------------

        is_correct = (
            check_unified_answer(
                session,
                user_answer,
            )
        )


        # Сохраняем данные ответа ДО перехода
        # к следующему слову / Deck.

        answer_feedback = {
            "is_correct":
                is_correct,

            "word_id":
                current_word.id,

            "correct_word":
                current_word.word,

            "translation_ru":
                current_word.translation_ru,

            "translation_kz":
                current_word.translation_kz,

            "part_of_speech":
                current_word.part_of_speech,

            "context_sentence":
                current_word.context_sentence,
        }


        # -------------------------------------------------
        # DECK ENGINE
        # -------------------------------------------------

        process_unified_answer(
            session=session,
            word_id=word_id,
            is_correct=is_correct,
        )


        session.refresh_from_db()


        # -------------------------------------------------
        # RESPONSE
        # -------------------------------------------------

        return JsonResponse(
            {
                "success":
                    True,

                "answer":
                    answer_feedback,

                "state":
                    serialize_complete_unified_state(
                        session
                    ),
            }
        )


    except (
        json.JSONDecodeError,
        UnicodeDecodeError,
        KeyError,
        TypeError,
        ValueError,
    ) as error:

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    str(error)
                    or
                    "Invalid request data.",
            },
            status=400,
        )


    except (
        UnifiedGroupPracticeSession
        .DoesNotExist
    ):

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    (
                        "Unified practice "
                        "session not found."
                    ),
            },
            status=404,
        )


# =========================================================
# RESTART
# =========================================================


@login_required
@require_POST
@transaction.atomic
def unified_practice_restart(
    request,
    group_id,
):

    try:

        session = (
            UnifiedGroupPracticeSession.objects
            .select_for_update()
            .select_related(
                "group",
                "group__level",
            )
            .get(
                user=request.user,
                group_id=group_id,
            )
        )


        restart_unified_practice(
            session
        )


        session.refresh_from_db()


        mark_unified_practice_opened(
            session
        )


        return JsonResponse(
            {
                "success":
                    True,

                "state":
                    serialize_complete_unified_state(
                        session
                    ),
            }
        )


    except (
        UnifiedGroupPracticeSession
        .DoesNotExist
    ):

        return JsonResponse(
            {
                "success":
                    False,

                "error":
                    (
                        "Unified practice "
                        "session not found."
                    ),
            },
            status=404,
        )