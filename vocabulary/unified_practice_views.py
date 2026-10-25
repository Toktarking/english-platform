import json

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (
    require_GET,
    require_POST,
)

from .models import (
    LessonPracticeProgress,
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
# TRIAL GUEST ACCESS
# =========================================================


TRIAL_GUEST_SESSION_KEY = (
    "trial_guest_user_id"
)


def _is_trial_guest(
    request,
):
    if not request.user.is_authenticated:
        return False

    guest_id = (
        request.session.get(
            TRIAL_GUEST_SESSION_KEY
        )
    )

    return (
        guest_id
        ==
        request.user.id
    )


def _get_trial_group():
    """
    Первая группа активного A1.
    """

    level = (
        VocabularyLevel.objects
        .filter(
            code__iexact="A1",
            is_active=True,
        )
        .first()
    )

    if level is None:
        return None

    return (
        VocabularyGroup.objects
        .filter(
            level=level,
        )
        .order_by(
            "order",
            "id",
        )
        .first()
    )


def _trial_unified_access_allowed(
    request,
    group_id,
):
    """
    Unified Practice разрешена guest только:
    - для первой группы A1;
    - после завершения всех Lessons этой группы.
    """

    if not _is_trial_guest(request):
        return True

    trial_group = (
        _get_trial_group()
    )

    if trial_group is None:
        return False

    if (
        trial_group.id
        !=
        int(group_id)
    ):
        return False

    lesson_ids = list(
        trial_group.lessons
        .filter(
            is_active=True,
        )
        .values_list(
            "id",
            flat=True,
        )
    )

    if not lesson_ids:
        return False

    completed_count = (
        LessonPracticeProgress.objects
        .filter(
            user=request.user,
            lesson_id__in=lesson_ids,
            completed_at__isnull=False,
        )
        .values(
            "lesson_id"
        )
        .distinct()
        .count()
    )

    return (
        completed_count
        ==
        len(lesson_ids)
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

    # TRIAL_GATE_UNIFIED_PAGE
    if (
        _is_trial_guest(request)
        and
        not _trial_unified_access_allowed(
            request,
            group_id,
        )
    ):
        return redirect(
            "vocabulary:trial_dashboard"
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

    # TRIAL_GATE_UNIFIED_STATE
    if (
        _is_trial_guest(request)
        and
        not _trial_unified_access_allowed(
            request,
            group_id,
        )
    ):
        return JsonResponse(
            {
                "success": False,
                "error": "Trial access denied.",
            },
            status=403,
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

    # TRIAL_GATE_UNIFIED_ANSWER
    if (
        _is_trial_guest(request)
        and
        not _trial_unified_access_allowed(
            request,
            group_id,
        )
    ):
        return JsonResponse(
            {
                "success": False,
                "error": "Trial access denied.",
            },
            status=403,
        )


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

    # TRIAL_GATE_UNIFIED_RESTART
    if (
        _is_trial_guest(request)
        and
        not _trial_unified_access_allowed(
            request,
            group_id,
        )
    ):
        return JsonResponse(
            {
                "success": False,
                "error": "Trial access denied.",
            },
            status=403,
        )


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