import random

from django.utils import timezone

from .models import (
    UnifiedGroupPracticeSession,
    UnifiedGroupPracticeWordState,
    VocabularyWord,
)


# =========================================================
# WORDS
# =========================================================


def get_unified_group_words(group):

    return list(
        VocabularyWord.objects
        .filter(
            lesson__group=group,
            is_active=True,
        )
        .select_related(
            "lesson",
        )
        .order_by(
            "lesson__order",
            "order",
        )
    )


# =========================================================
# DECK IDS
# =========================================================


def get_deck_ids(
    session,
    deck_number,
):

    deck_fields = {
        1: "in_deck1",
        2: "in_deck2",
        3: "in_deck3",
        4: "in_deck4",
        5: "in_deck5",
    }

    field_name = deck_fields.get(
        deck_number
    )

    if not field_name:
        raise ValueError(
            "Unknown deck number."
        )

    return list(
        session.word_states
        .filter(
            **{
                field_name: True,
            }
        )
        .values_list(
            "word_id",
            flat=True,
        )
    )


# =========================================================
# SET PHASE
# =========================================================


def set_unified_phase(
    session,
    phase,
    word_ids,
    shuffle=True,
):

    word_ids = list(
        word_ids
    )

    if shuffle:
        random.shuffle(
            word_ids
        )

    session.phase = phase

    session.current_queue = (
        word_ids
    )

    session.current_index = 0

    session.save(
        update_fields=[
            "phase",
            "current_queue",
            "current_index",
            "mistake_count",
            "updated_at",

        ]
    )


# =========================================================
# FINISH
# =========================================================


def finish_unified_practice(
    session,
):

    session.phase = (
        UnifiedGroupPracticeSession
        .Phase
        .COMPLETED
    )

    session.is_completed = True

    session.current_queue = []

    session.current_index = 0

    session.completed_at = (
        timezone.now()
    )

    session.save(
        update_fields=[
            "phase",
            "is_completed",
            "current_queue",
            "current_index",
            "completed_at",
            "updated_at",
        ]
    )


# =========================================================
# INITIALIZE
# =========================================================


def initialize_unified_practice(
    session,
    words,
):

    # Удаляем состояния только V2.
    # Старые Practice 1–4 это не затрагивает.

    UnifiedGroupPracticeWordState.objects.filter(
        session=session,
    ).delete()


    # В начале ВСЕ слова находятся
    # только в Deck 1.

    UnifiedGroupPracticeWordState.objects.bulk_create(
        [
            UnifiedGroupPracticeWordState(
                session=session,
                word=word,
                in_deck1=True,
                in_deck2=False,
                in_deck3=False,
                in_deck4=False,
                in_deck5=False,
            )

            for word in words
        ]
    )


    initial_queue = [
        word.id
        for word in words
    ]

    random.shuffle(
        initial_queue
    )


    session.phase = (
        UnifiedGroupPracticeSession
        .Phase
        .LISTENING_INITIAL
    )

    session.current_queue = (
        initial_queue
    )

    session.current_index = 0

    session.mistake_count = 0

    session.is_completed = False

    session.completed_at = None

    session.save(
        update_fields=[
            "phase",
            "current_queue",
            "current_index",
            "mistake_count",
            "is_completed",
            "completed_at",
            "updated_at",
        ]
    )


# =========================================================
# GET / CREATE
# =========================================================


def get_or_create_unified_practice(
    user,
    group,
):

    session, created = (
        UnifiedGroupPracticeSession.objects
        .get_or_create(
            user=user,
            group=group,
        )
    )

    if created:

        words = (
            get_unified_group_words(
                group
            )
        )

        initialize_unified_practice(
            session,
            words,
        )

    return session


# =========================================================
# RESTART
# =========================================================


def restart_unified_practice(
    session,
):

    words = (
        get_unified_group_words(
            session.group
        )
    )

    initialize_unified_practice(
        session,
        words,
    )


# =========================================================
# OPENED
# =========================================================


def mark_unified_practice_opened(
    session,
):

    session.last_opened_at = (
        timezone.now()
    )

    session.save(
        update_fields=[
            "last_opened_at",
            "updated_at",
        ]
    )


# =========================================================
# START DECK 2 — FIRST
# =========================================================


def start_letter_first(
    session,
):

    word_ids = (
        get_deck_ids(
            session,
            2,
        )
    )

    if not word_ids:

        finish_unified_practice(
            session
        )

        return

    set_unified_phase(
        session,
        (
            UnifiedGroupPracticeSession
            .Phase
            .LETTER_FIRST
        ),
        word_ids,
    )


# =========================================================
# START DECK 4
# =========================================================


def start_multiple_choice_1(
    session,
):

    word_ids = (
        get_deck_ids(
            session,
            4,
        )
    )

    if not word_ids:

        start_letter_review(
            session
        )

        return

    set_unified_phase(
        session,
        (
            UnifiedGroupPracticeSession
            .Phase
            .MULTIPLE_CHOICE_1
        ),
        word_ids,
    )


# =========================================================
# START DECK 5
# =========================================================


def start_multiple_choice_2(
    session,
):

    # ВАЖНО:
    #
    # Deck 5 никогда не очищается.
    # Каждый запуск берёт ВСЕ слова,
    # которые когда-либо попали в неё.

    word_ids = (
        get_deck_ids(
            session,
            5,
        )
    )

    if not word_ids:

        start_letter_review(
            session
        )

        return

    set_unified_phase(
        session,
        (
            UnifiedGroupPracticeSession
            .Phase
            .MULTIPLE_CHOICE_2
        ),
        word_ids,
        shuffle=True,
    )


# =========================================================
# AFTER PERFECT DECK 5
# =========================================================


def complete_deck5_round(
    session,
):

    # Deck 5 НЕ очищаем.
    #
    # Все накопленные проблемные слова
    # должны снова пройти:
    #
    # Deck 2
    # -> Deck 3
    # -> Deck 1

    deck5_states = (
        session.word_states
        .filter(
            in_deck5=True,
        )
    )


    deck5_states.update(
        in_deck1=True,
        in_deck2=True,
        in_deck3=True,

        # Deck 4 больше не нужен
        # после успешного прохождения Deck 5.
        in_deck4=False,
    )


    start_letter_review(
        session
    )


# =========================================================
# START DECK 2 — REVIEW
# =========================================================


def start_letter_review(
    session,
):

    word_ids = (
        get_deck_ids(
            session,
            2,
        )
    )

    if not word_ids:

        start_context_review(
            session
        )

        return

    set_unified_phase(
        session,
        (
            UnifiedGroupPracticeSession
            .Phase
            .LETTER_REVIEW
        ),
        word_ids,
    )


# =========================================================
# START DECK 3
# =========================================================


def start_context_review(
    session,
):

    word_ids = (
        get_deck_ids(
            session,
            3,
        )
    )

    if not word_ids:

        start_listening_review(
            session
        )

        return

    set_unified_phase(
        session,
        (
            UnifiedGroupPracticeSession
            .Phase
            .CONTEXT_REVIEW
        ),
        word_ids,
    )


# =========================================================
# START DECK 1 — FINAL
# =========================================================


def start_listening_review(
    session,
):

    word_ids = (
        get_deck_ids(
            session,
            1,
        )
    )

    if not word_ids:

        finish_unified_practice(
            session
        )

        return

    set_unified_phase(
        session,
        (
            UnifiedGroupPracticeSession
            .Phase
            .LISTENING_REVIEW
        ),
        word_ids,
    )


# =========================================================
# CURRENT WORD VALIDATION
# =========================================================


def validate_current_word(
    session,
    word_id,
):

    if session.is_completed:

        raise ValueError(
            "Practice is already completed."
        )


    if (
        session.current_index
        >=
        len(
            session.current_queue
        )
    ):

        raise ValueError(
            "Invalid practice position."
        )


    expected_word_id = int(
        session.current_queue[
            session.current_index
        ]
    )


    if (
        int(word_id)
        !=
        expected_word_id
    ):

        raise ValueError(
            "This is not the current word."
        )


    return expected_word_id


# =========================================================
# SAVE NORMAL ADVANCE
# =========================================================


def advance_current_queue(
    session,
):

    session.current_index += 1

    session.save(
        update_fields=[
            "current_index",
            "mistake_count",
            "updated_at",
        ]
    )


# =========================================================
# MISTAKE
# =========================================================


def register_word_mistake(
    session,
    word_state,
):

    session.mistake_count += 1

    word_state.mistake_count += 1


# =========================================================
# MAIN ANSWER ENGINE
# =========================================================


def process_unified_answer(
    session,
    word_id,
    is_correct,
):

    validate_current_word(
        session,
        word_id,
    )


    word_state = (
        UnifiedGroupPracticeWordState.objects
        .select_for_update()
        .get(
            session=session,
            word_id=word_id,
        )
    )


    phase = (
        session.phase
    )


    # =====================================================
    # DECK 1
    # INITIAL LISTENING
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LISTENING_INITIAL
    ):

        if is_correct:

            # Знает слово на слух.
            # Убираем из Deck 1.

            word_state.in_deck1 = False

        else:

            # Ошибка:
            #
            # остаётся в Deck 1
            # + Deck 2
            # + Deck 3

            register_word_mistake(
                session,
                word_state,
            )

            word_state.in_deck1 = True
            word_state.in_deck2 = True
            word_state.in_deck3 = True


        word_state.save(
            update_fields=[
                "in_deck1",
                "in_deck2",
                "in_deck3",
                "mistake_count",
            ]
        )


        session.current_index += 1


        # Ещё есть слова первого круга.

        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

            return


        # Первый Listening завершён.

        deck2_ids = (
            get_deck_ids(
                session,
                2,
            )
        )


        # Все слова были правильными
        # с первой попытки.

        if not deck2_ids:

            finish_unified_practice(
                session
            )

            return


        start_letter_first(
            session
        )

        return


    # =====================================================
    # DECK 2
    # LETTER CONSTRUCTION — FIRST PASS
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LETTER_FIRST
    ):

        if is_correct:

            # Убираем из Deck 2.

            word_state.in_deck2 = False

        else:

            register_word_mistake(
                session,
                word_state,
            )

            # Остаётся в Deck 2.
            word_state.in_deck2 = True

            # И добавляется в Deck 4.
            word_state.in_deck4 = True


        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck4",
                "mistake_count",
            ]
        )


        session.current_index += 1


        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

            return


        # Весь первый Deck 2 завершён.

        deck4_ids = (
            get_deck_ids(
                session,
                4,
            )
        )


        if deck4_ids:

            start_multiple_choice_1(
                session
            )

        else:

            # Все Letter Construction
            # были правильными.
            #
            # Переходим сразу к Context.

            start_context_review(
                session
            )

        return


    # =====================================================
    # DECK 4
    # MULTIPLE CHOICE 1
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_1
    ):

        if is_correct:

            # Слово успешно прошло Deck 4.
            word_state.in_deck4 = False

        else:

            register_word_mistake(
                session,
                word_state,
            )

            # Остаётся в Deck 4.
            word_state.in_deck4 = True

            # И впервые попадает
            # в накопительную Deck 5.
            word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck4",
                "in_deck5",
                "mistake_count",
            ]
        )


        session.current_index += 1


        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

            return


        deck5_ids = (
            get_deck_ids(
                session,
                5,
            )
        )


        if deck5_ids:

            start_multiple_choice_2(
                session
            )

        else:

            # Deck 4 пройдена полностью.
            # Возвращаемся к Deck 2.

            start_letter_review(
                session
            )

        return


    # =====================================================
    # DECK 5
    # MULTIPLE CHOICE 2
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_2
    ):

        if not is_correct:

            register_word_mistake(
                session,
                word_state,
            )

            # Deck 5 накопительная.
            word_state.in_deck5 = True

            word_state.save(
                update_fields=[
                    "in_deck5",
                    "mistake_count",
                ]
            )


            # КЛЮЧЕВОЕ ПРАВИЛО:
            #
            # одна ошибка в Deck 5
            # полностью перезапускает
            # ВСЮ Deck 5 в новом
            # случайном порядке.

            start_multiple_choice_2(
                session
            )

            return


        # Правильный ответ.
        #
        # НИЧЕГО из Deck 5
        # не удаляем.

        session.current_index += 1


        if (
            session.current_index
            <
            len(
                session.current_queue
            )
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

            return


        # Вся накопительная Deck 5
        # пройдена без единой ошибки.

        complete_deck5_round(
            session
        )

        return


    # =====================================================
    # DECK 2
    # LETTER CONSTRUCTION — REVIEW
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LETTER_REVIEW
    ):

        if is_correct:

            word_state.in_deck2 = False

            word_state.save(
                update_fields=[
                    "in_deck2",
                ]
            )


            session.current_index += 1


            if (
                session.current_index
                <
                len(
                    session.current_queue
                )
            ):

                session.save(
                    update_fields=[
                        "current_index",
                        "mistake_count",
                        "updated_at",
                    ]
                )

                return


            start_context_review(
                session
            )

            return


        # Ошибка в повторном Deck 2.

        register_word_mistake(
            session,
            word_state,
        )

        # Слово остаётся в Deck 2.
        word_state.in_deck2 = True

        # И навсегда добавляется в Deck 5.
        word_state.in_deck5 = True

        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck5",
                "mistake_count",
            ]
        )


        # Немедленный переход в Deck 5.

        start_multiple_choice_2(
            session
        )

        return


    # =====================================================
    # DECK 3
    # CONTEXT
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .CONTEXT_REVIEW
    ):

        if is_correct:

            word_state.in_deck3 = False

            word_state.save(
                update_fields=[
                    "in_deck3",
                ]
            )


            session.current_index += 1


            if (
                session.current_index
                <
                len(
                    session.current_queue
                )
            ):

                session.save(
                    update_fields=[
                        "current_index",
                        "mistake_count",
                        "updated_at",
                    ]
                )

                return


            start_listening_review(
                session
            )

            return


        # Ошибка в Context.

        register_word_mistake(
            session,
            word_state,
        )

        # Остаётся в Deck 3.
        word_state.in_deck3 = True

        # Добавляется в постоянную Deck 5.
        word_state.in_deck5 = True

        word_state.save(
            update_fields=[
                "in_deck3",
                "in_deck5",
                "mistake_count",
            ]
        )


        # Немедленно Deck 5.

        start_multiple_choice_2(
            session
        )

        return


    # =====================================================
    # DECK 1
    # FINAL LISTENING
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LISTENING_REVIEW
    ):

        if is_correct:

            word_state.in_deck1 = False

            word_state.save(
                update_fields=[
                    "in_deck1",
                ]
            )


            session.current_index += 1


            if (
                session.current_index
                <
                len(
                    session.current_queue
                )
            ):

                session.save(
                    update_fields=[
                        "current_index",
                        "mistake_count",
                        "updated_at",
                    ]
                )

                return


            # Если Deck 1 действительно
            # полностью очищена — победа.

            remaining_deck1 = (
                get_deck_ids(
                    session,
                    1,
                )
            )


            if not remaining_deck1:

                finish_unified_practice(
                    session
                )

            else:

                start_listening_review(
                    session
                )

            return


        # Ошибка в финальном Listening.

        register_word_mistake(
            session,
            word_state,
        )

        # Слово остаётся в Deck 1.
        word_state.in_deck1 = True

        # И добавляется в постоянную Deck 5.
        word_state.in_deck5 = True

        word_state.save(
            update_fields=[
                "in_deck1",
                "in_deck5",
                "mistake_count",
            ]
        )


        # Немедленно возвращаемся
        # к полной Deck 5.

        start_multiple_choice_2(
            session
        )

        return


    raise ValueError(
        "Unknown unified practice phase."
    )


# =========================================================
# SERIALIZE
# =========================================================


def serialize_unified_practice(
    session,
):

    current_word_id = None

    if (
        not session.is_completed
        and
        session.current_queue
        and
        session.current_index
        <
        len(
            session.current_queue
        )
    ):

        current_word_id = int(
            session.current_queue[
                session.current_index
            ]
        )


    deck_counts = {

        1:
            session.word_states.filter(
                in_deck1=True
            ).count(),

        2:
            session.word_states.filter(
                in_deck2=True
            ).count(),

        3:
            session.word_states.filter(
                in_deck3=True
            ).count(),

        4:
            session.word_states.filter(
                in_deck4=True
            ).count(),

        5:
            session.word_states.filter(
                in_deck5=True
            ).count(),

    }


    return {

        "phase":
            session.phase,

        "current_word_id":
            current_word_id,

        "current_index":
            session.current_index,

        "queue_size":
            len(
                session.current_queue
            ),

        "deck1_count":
            deck_counts[1],

        "deck2_count":
            deck_counts[2],

        "deck3_count":
            deck_counts[3],

        "deck4_count":
            deck_counts[4],

        "deck5_count":
            deck_counts[5],

        "mistake_count":
            session.mistake_count,

        "is_completed":
            session.is_completed,

    }