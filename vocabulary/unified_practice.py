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
# AVAILABLE MECHANICS
# =========================================================


def get_unified_available_stage_count(
    user,
    group,
):

    completed_unified = (
        UnifiedGroupPracticeSession.objects
        .filter(
            user=user,
            group__level=group.level,
            is_completed=True,
        )
        .count()
    )

    return min(
        4,
        1 + completed_unified,
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

    # TWO_STAGE_UNIFIED_INIT
    #
    # Когда открыты только:
    # Spelling + Multiple Choice
    #
    # Используем существующие boolean-поля:
    #
    # in_deck2 = логическая Колода 1 / Spelling
    # in_deck4 = логическая Колода 2 / Multiple Choice
    # in_deck5 = логическая Колода 3 / cumulative MC

    available_stage_count = (
        get_unified_available_stage_count(
            session.user,
            session.group,
        )
    )


    if available_stage_count == 2:

        UnifiedGroupPracticeWordState.objects.filter(
            session=session,
        ).delete()


        UnifiedGroupPracticeWordState.objects.bulk_create(
            [
                UnifiedGroupPracticeWordState(
                    session=session,
                    word=word,

                    in_deck1=False,

                    # ВСЕ слова начинают здесь.
                    in_deck2=True,

                    in_deck3=False,

                    # Колода ошибок Spelling.
                    in_deck4=False,

                    # Накопительная колода.
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


        # Начинаем именно со Spelling.
        session.phase = (
            UnifiedGroupPracticeSession
            .Phase
            .LETTER_FIRST
        )

        session.current_queue = initial_queue
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

        return


    UnifiedGroupPracticeWordState.objects.filter(
        session=session,
    ).delete()


    # =====================================================
    # THREE_STAGE_UNIFIED_INIT
    #
    # Practice 3:
    #
    # Logical Deck 1 = Context
    # Logical Deck 2 = Spelling
    # Logical Deck 3 = Multiple Choice
    # Logical Deck 4 = Persistent Multiple Choice loop
    #
    # Physical fields:
    #
    # in_deck1 = Context
    # in_deck2 = Spelling
    # in_deck3 = review marker
    # in_deck4 = Multiple Choice
    # in_deck5 = persistent error loop
    # =====================================================

    if (
        get_unified_available_stage_count(
            session.user,
            session.group,
        )
        ==
        3
    ):

        UnifiedGroupPracticeWordState.objects.filter(
            session=session,
        ).delete()


        UnifiedGroupPracticeWordState.objects.bulk_create(
            [
                UnifiedGroupPracticeWordState(

                    session=session,
                    word=word,

                    # Все слова начинают
                    # в Context.
                    in_deck1=True,

                    # Spelling.
                    in_deck2=False,

                    # Служебный marker:
                    # False = первый Context,
                    # True = финальный Context.
                    in_deck3=False,

                    # Multiple Choice.
                    in_deck4=False,

                    # Накопительная loop-колода.
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


        # Начинаем с Context.
        session.phase = (
            UnifiedGroupPracticeSession
            .Phase
            .CONTEXT_REVIEW
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

        return


    # =====================================================
    # FOUR_STAGE_UNIFIED_INIT
    #
    # Practice 4:
    #
    # 1. Listening
    # 2. Context
    # 3. Spelling
    # 4. Multiple Choice
    # 5. Hard Multiple Choice
    # =====================================================

    if (
        get_unified_available_stage_count(
            session.user,
            session.group,
        )
        ==
        4
    ):

        UnifiedGroupPracticeWordState.objects.filter(
            session=session,
        ).delete()

        UnifiedGroupPracticeWordState.objects.bulk_create(
            [
                UnifiedGroupPracticeWordState(
                    session=session,
                    word=word,

                    # Listening.
                    in_deck1=True,

                    # Context.
                    in_deck2=False,

                    # Spelling / Context review marker.
                    in_deck3=False,

                    # Normal Choice.
                    in_deck4=False,

                    # Hard Choice.
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

        session.current_queue = initial_queue
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

        return


    available_stage_count = (
        get_unified_available_stage_count(
            session.user,
            session.group,
        )
    )


    UnifiedGroupPracticeWordState.objects.bulk_create(
        [
            UnifiedGroupPracticeWordState(
                session=session,
                word=word,

                # Listening доступен только после 3 Practice.
                in_deck1=(
                    available_stage_count >= 4
                ),

                # Spelling после 1 Practice.
                in_deck2=(
                    available_stage_count >= 2
                ),

                # Context после 2 Practice.
                in_deck3=(
                    available_stage_count >= 3
                ),

                # Choice доступен всегда.
                in_deck4=True,

                # Error Review начинается пустым.
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


    # Новая логика:
    # Unified Practice всегда начинается с Choice.
    session.phase = (
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_1
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

    available_stage_count = (
        get_unified_available_stage_count(
            session.user,
            session.group,
        )
    )


    deck5_states = (
        session.word_states
        .filter(
            in_deck5=True,
        )
    )


    deck5_states.update(
        # Возвращаем слово только в открытые режимы.
        in_deck1=(
            available_stage_count >= 4
        ),

        in_deck2=(
            available_stage_count >= 2
        ),

        in_deck3=(
            available_stage_count >= 3
        ),

        in_deck4=False,
    )


    # Если открыт только Choice,
    # после строгого повторения ошибок Practice завершена.
    if available_stage_count <= 1:

        finish_unified_practice(
            session
        )

        return


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
# TWO-STAGE UNIFIED PRACTICE
#
# Колода 1 = Spelling
# Колода 2 = Multiple Choice
# Колода 3 = cumulative Multiple Choice
# =========================================================


def process_two_stage_unified_answer(
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


    phase = session.phase


    # =====================================================
    # КОЛОДА 1
    # SPELLING — ПЕРВЫЙ КРУГ
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LETTER_FIRST
    ):

        if is_correct:

            # Правильно:
            # полностью убираем слово.
            word_state.in_deck2 = False

        else:

            register_word_mistake(
                session,
                word_state,
            )

            # Ошибка:
            # убираем из Колоды 1
            # и добавляем в Колоду 2.
            word_state.in_deck2 = False
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
            len(session.current_queue)
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

            return


        # Все Spelling закончились.
        deck2_ids = get_deck_ids(
            session,
            4,
        )


        if deck2_ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .MULTIPLE_CHOICE_1
                ),
                deck2_ids,
                shuffle=True,
            )

        else:

            # Все слова были правильными
            # с первой попытки.
            finish_unified_practice(
                session
            )

        return


    # =====================================================
    # КОЛОДА 2
    # MULTIPLE CHOICE
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_1
    ):

        if is_correct:

            # Правильно:
            # возвращаем в Колоду 1.
            word_state.in_deck4 = False
            word_state.in_deck2 = True

        else:

            register_word_mistake(
                session,
                word_state,
            )

            # Ошибка:
            # убираем из Колоды 2
            # и добавляем в Колоду 3.
            word_state.in_deck4 = False
            word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck4",
                "in_deck5",
                "mistake_count",
            ]
        )


        session.current_index += 1


        if (
            session.current_index
            <
            len(session.current_queue)
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

            return


        # Сначала идём в Колоду 3,
        # если там есть хоть одно слово.
        deck3_ids = get_deck_ids(
            session,
            5,
        )


        if deck3_ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .MULTIPLE_CHOICE_2
                ),
                deck3_ids,
                shuffle=True,
            )

            return


        # Если Колода 3 пустая —
        # возвращаемся в Колоду 1.
        deck1_ids = get_deck_ids(
            session,
            2,
        )


        if deck1_ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .LETTER_REVIEW
                ),
                deck1_ids,
                shuffle=True,
            )

        else:

            finish_unified_practice(
                session
            )

        return


    # =====================================================
    # КОЛОДА 3
    # НАКОПИТЕЛЬНЫЙ MULTIPLE CHOICE
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

            # Из Колоды 3 слова
            # никогда не удаляем.
            word_state.in_deck5 = True

            word_state.save(
                update_fields=[
                    "in_deck5",
                    "mistake_count",
                ]
            )


            # ОДНА ошибка —
            # вся Колода 3 заново.
            deck3_ids = get_deck_ids(
                session,
                5,
            )

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .MULTIPLE_CHOICE_2
                ),
                deck3_ids,
                shuffle=True,
            )

            return


        # Правильно:
        # слово всё равно остаётся
        # в накопительной Колоде 3.
        session.current_index += 1


        if (
            session.current_index
            <
            len(session.current_queue)
        ):

            session.save(
                update_fields=[
                    "current_index",
                    "mistake_count",
                    "updated_at",
                ]
            )

            return


        # ВЕСЬ круг Колоды 3
        # выполнен без ошибок.
        #
        # Добавляем все слова
        # обратно в Колоду 1.
        deck3_ids = get_deck_ids(
            session,
            5,
        )


        session.word_states.filter(
            word_id__in=deck3_ids,
        ).update(
            in_deck2=True,
        )


        # Boolean исключает дубликаты автоматически.
        deck1_ids = get_deck_ids(
            session,
            2,
        )


        if deck1_ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .LETTER_REVIEW
                ),
                deck1_ids,
                shuffle=True,
            )

        else:

            finish_unified_practice(
                session
            )

        return


    # =====================================================
    # КОЛОДА 1
    # SPELLING — ПОВТОР
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LETTER_REVIEW
    ):

        if is_correct:

            # Правильно:
            # слово уходит из Колоды 1.
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
                len(session.current_queue)
            ):

                session.save(
                    update_fields=[
                        "current_index",
                        "mistake_count",
                        "updated_at",
                    ]
                )

                return


            remaining = get_deck_ids(
                session,
                2,
            )


            if remaining:

                set_unified_phase(
                    session,
                    (
                        UnifiedGroupPracticeSession
                        .Phase
                        .LETTER_REVIEW
                    ),
                    remaining,
                    shuffle=True,
                )

            else:

                finish_unified_practice(
                    session
                )

            return


        # Ошибка в Колоде 1:
        #
        # слово остаётся в Колоде 1,
        # добавляется в Колоду 3,
        # и пользователь СРАЗУ
        # снова проходит всю Колоду 3.

        register_word_mistake(
            session,
            word_state,
        )

        word_state.in_deck2 = True
        word_state.in_deck5 = True

        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck5",
                "mistake_count",
            ]
        )


        deck3_ids = get_deck_ids(
            session,
            5,
        )


        set_unified_phase(
            session,
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_2
            ),
            deck3_ids,
            shuffle=True,
        )

        return


    raise ValueError(
        "Unknown phase for two-stage Unified Practice."
    )


# =========================================================
# MAIN ANSWER ENGINE
# =========================================================


# =========================================================
# PRACTICE 3 — THREE AVAILABLE MECHANICS
#
# LOGICAL FLOW:
#
# Deck 1 = Context
# Deck 2 = Spelling
# Deck 3 = Multiple Choice
# Deck 4 = persistent Multiple Choice loop
#
# Physical fields:
#
# deck1 -> in_deck1
# deck2 -> in_deck2
# marker -> in_deck3
# deck3 -> in_deck4
# deck4 -> in_deck5
# =========================================================


def process_three_stage_unified_answer(
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
    # LOGICAL DECK 1 — CONTEXT
    #
    # Эта же фаза используется:
    #
    # 1. В самом начале Practice.
    # 2. В финальном Context после Spelling.
    #
    # in_deck3 выступает marker:
    #
    # False -> первый Context.
    # True  -> финальный Context.
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .CONTEXT_REVIEW
    ):

        is_final_context = (
            word_state.in_deck3
        )


        # -------------------------------------------------
        # CORRECT
        # -------------------------------------------------

        if is_correct:

            # Убираем из Context.
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


            # =============================================
            # FINальный Context
            # =============================================

            if is_final_context:

                remaining_context = (
                    get_deck_ids(
                        session,
                        1,
                    )
                )


                if remaining_context:

                    set_unified_phase(
                        session,
                        (
                            UnifiedGroupPracticeSession
                            .Phase
                            .CONTEXT_REVIEW
                        ),
                        remaining_context,
                        shuffle=True,
                    )

                else:

                    finish_unified_practice(
                        session
                    )

                return


            # =============================================
            # Первый Context закончен.
            #
            # Ошибочные слова находятся
            # в Spelling.
            # =============================================

            spelling_ids = (
                get_deck_ids(
                    session,
                    2,
                )
            )


            if spelling_ids:

                set_unified_phase(
                    session,
                    (
                        UnifiedGroupPracticeSession
                        .Phase
                        .LETTER_FIRST
                    ),
                    spelling_ids,
                    shuffle=True,
                )

            else:

                # Все слова Context были
                # правильными с первого раза.
                finish_unified_practice(
                    session
                )

            return


        # -------------------------------------------------
        # WRONG
        # -------------------------------------------------

        register_word_mistake(
            session,
            word_state,
        )


        # =============================================
        # ПЕРВЫЙ CONTEXT
        #
        # Wrong -> Spelling
        # =============================================

        if not is_final_context:

            word_state.in_deck1 = False
            word_state.in_deck2 = True

            word_state.save(
                update_fields=[
                    "in_deck1",
                    "in_deck2",
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


            spelling_ids = (
                get_deck_ids(
                    session,
                    2,
                )
            )


            if spelling_ids:

                set_unified_phase(
                    session,
                    (
                        UnifiedGroupPracticeSession
                        .Phase
                        .LETTER_FIRST
                    ),
                    spelling_ids,
                    shuffle=True,
                )

            else:

                finish_unified_practice(
                    session
                )

            return


        # =============================================
        # ФИНАЛЬНЫЙ CONTEXT
        #
        # Wrong -> persistent Deck 4
        # и СРАЗУ туда.
        # =============================================

        word_state.in_deck1 = False

        word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck1",
                "in_deck5",
                "mistake_count",
            ]
        )


        deck4_ids = (
            get_deck_ids(
                session,
                5,
            )
        )


        set_unified_phase(
            session,
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_2
            ),
            deck4_ids,
            shuffle=True,
        )

        return


    # =====================================================
    # LOGICAL DECK 2 — SPELLING
    # FIRST PASS
    #
    # Correct -> Context
    # Wrong   -> Deck 3 MC
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LETTER_FIRST
    ):

        if is_correct:

            # Убираем из Spelling.
            word_state.in_deck2 = False

            # Отправляем в Context.
            word_state.in_deck1 = True

            # Marker:
            # это уже финальный Context.
            word_state.in_deck3 = True

        else:

            register_word_mistake(
                session,
                word_state,
            )

            # Убираем из Spelling.
            word_state.in_deck2 = False

            # В обычный Multiple Choice.
            word_state.in_deck4 = True


        word_state.save(
            update_fields=[
                "in_deck1",
                "in_deck2",
                "in_deck3",
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


        # Сначала Deck 3 MC.
        mc_ids = (
            get_deck_ids(
                session,
                4,
            )
        )


        if mc_ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .MULTIPLE_CHOICE_1
                ),
                mc_ids,
                shuffle=True,
            )

            return


        # Если ошибок Spelling не было —
        # сразу Context.
        context_ids = (
            get_deck_ids(
                session,
                1,
            )
        )


        if context_ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .CONTEXT_REVIEW
                ),
                context_ids,
                shuffle=True,
            )

        else:

            finish_unified_practice(
                session
            )

        return


    # =====================================================
    # LOGICAL DECK 3 — MULTIPLE CHOICE
    #
    # Correct -> Spelling
    # Wrong   -> persistent Deck 4
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_1
    ):

        if is_correct:

            # Убираем из MC.
            word_state.in_deck4 = False

            # Возвращаем в Spelling.
            word_state.in_deck2 = True

        else:

            register_word_mistake(
                session,
                word_state,
            )

            # Убираем из Deck 3.
            word_state.in_deck4 = False

            # Навсегда добавляем
            # в накопительную Deck 4.
            word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck2",
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


        # Если появилась persistent Deck 4 —
        # сначала обязательно она.
        deck4_ids = (
            get_deck_ids(
                session,
                5,
            )
        )


        if deck4_ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .MULTIPLE_CHOICE_2
                ),
                deck4_ids,
                shuffle=True,
            )

            return


        # Иначе переходим к Spelling.
        spelling_ids = (
            get_deck_ids(
                session,
                2,
            )
        )


        if spelling_ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .LETTER_REVIEW
                ),
                spelling_ids,
                shuffle=True,
            )

        else:

            context_ids = (
                get_deck_ids(
                    session,
                    1,
                )
            )

            if context_ids:

                set_unified_phase(
                    session,
                    (
                        UnifiedGroupPracticeSession
                        .Phase
                        .CONTEXT_REVIEW
                    ),
                    context_ids,
                    shuffle=True,
                )

            else:

                finish_unified_practice(
                    session
                )

        return


    # =====================================================
    # LOGICAL DECK 4
    # PERSISTENT MULTIPLE CHOICE LOOP
    #
    # Слова из неё НЕ удаляются.
    #
    # Любая ошибка:
    # вся Deck 4 сначала.
    #
    # Весь круг правильно:
    # ВСЕ слова Deck 4 -> Spelling.
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


            # Слово остаётся
            # в persistent Deck 4.
            word_state.in_deck5 = True


            word_state.save(
                update_fields=[
                    "in_deck5",
                    "mistake_count",
                ]
            )


            # Одна ошибка =
            # полный restart Deck 4.
            deck4_ids = (
                get_deck_ids(
                    session,
                    5,
                )
            )


            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .MULTIPLE_CHOICE_2
                ),
                deck4_ids,
                shuffle=True,
            )

            return


        # Correct.
        #
        # Из Deck 4 ничего не удаляем.

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


        # Вся Deck 4 пройдена
        # без единой ошибки.
        deck4_ids = (
            get_deck_ids(
                session,
                5,
            )
        )


        # Все persistent слова
        # добавляем в Spelling.
        #
        # Boolean автоматически
        # исключает дубликаты.
        session.word_states.filter(
            word_id__in=deck4_ids,
        ).update(
            in_deck2=True,
        )


        spelling_ids = (
            get_deck_ids(
                session,
                2,
            )
        )


        set_unified_phase(
            session,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_REVIEW
            ),
            spelling_ids,
            shuffle=True,
        )

        return


    # =====================================================
    # LOGICAL DECK 2 — SPELLING REVIEW
    #
    # Correct -> Context
    # Wrong   -> persistent Deck 4
    #           + немедленный переход туда
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LETTER_REVIEW
    ):

        if is_correct:

            # Убираем из Spelling.
            word_state.in_deck2 = False

            # Отправляем в Context.
            word_state.in_deck1 = True

            # Это финальный Context.
            word_state.in_deck3 = True

            # ВАЖНО:
            # если слово пришло сюда из накопительной
            # Deck 4 и пользователь правильно выполнил
            # Spelling, слово больше не считается
            # проблемным и удаляется из Deck 4.
            word_state.in_deck5 = False


            word_state.save(
                update_fields=[
                    "in_deck1",
                    "in_deck2",
                    "in_deck3",
                    "in_deck5",
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


            # Все слова Spelling
            # выполнены правильно.
            context_ids = (
                get_deck_ids(
                    session,
                    1,
                )
            )


            if context_ids:

                set_unified_phase(
                    session,
                    (
                        UnifiedGroupPracticeSession
                        .Phase
                        .CONTEXT_REVIEW
                    ),
                    context_ids,
                    shuffle=True,
                )

            else:

                finish_unified_practice(
                    session
                )

            return


        # -------------------------------------------------
        # WRONG
        # -------------------------------------------------

        register_word_mistake(
            session,
            word_state,
        )


        # Переносим из Spelling
        # в persistent Deck 4.
        word_state.in_deck2 = False

        word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck5",
                "mistake_count",
            ]
        )


        # И СРАЗУ запускаем
        # всю накопительную Deck 4.
        deck4_ids = (
            get_deck_ids(
                session,
                5,
            )
        )


        set_unified_phase(
            session,
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_2
            ),
            deck4_ids,
            shuffle=True,
        )

        return


    raise ValueError(
        "Unknown phase for three-stage Unified Practice."
    )



def process_four_stage_unified_answer(
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

    phase = session.phase

    # -----------------------------------------------------
    # Physical state:
    #
    # in_deck1 = Listening
    #
    # in_deck2=True, in_deck3=False
    # = first Context
    #
    # in_deck2=False, in_deck3=True
    # = Spelling
    #
    # in_deck2=True, in_deck3=True
    # = Context review
    #
    # in_deck4 = normal Choice
    # in_deck5 = Hard Choice
    # -----------------------------------------------------

    def spelling_ids():

        return list(
            session.word_states
            .filter(
                in_deck3=True,
                in_deck2=False,
            )
            .values_list(
                "word_id",
                flat=True,
            )
        )


    def initial_context_ids():

        return list(
            session.word_states
            .filter(
                in_deck2=True,
                in_deck3=False,
            )
            .values_list(
                "word_id",
                flat=True,
            )
        )


    def review_context_ids():

        return list(
            session.word_states
            .filter(
                in_deck2=True,
                in_deck3=True,
            )
            .values_list(
                "word_id",
                flat=True,
            )
        )


    def start_listening_review_4():

        ids = get_deck_ids(
            session,
            1,
        )

        if ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .LISTENING_REVIEW
                ),
                ids,
                shuffle=True,
            )

        else:

            finish_unified_practice(
                session
            )


    def start_context_review_4():

        ids = review_context_ids()

        if ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .CONTEXT_REVIEW
                ),
                ids,
                shuffle=True,
            )

        else:

            start_listening_review_4()


    def start_spelling_review_4():

        ids = spelling_ids()

        if ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .LETTER_REVIEW
                ),
                ids,
                shuffle=True,
            )

        else:

            start_context_review_4()


    def start_hard_4():

        ids = get_deck_ids(
            session,
            5,
        )

        if ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .MULTIPLE_CHOICE_2
                ),
                ids,
                shuffle=True,
            )

        else:

            start_spelling_review_4()


    # =====================================================
    # DECK 1
    # LISTENING — FIRST PASS
    #
    # Correct -> слово выходит.
    # Wrong   -> Context.
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LISTENING_INITIAL
    ):

        if is_correct:

            word_state.in_deck1 = False

        else:

            register_word_mistake(
                session,
                word_state,
            )

            # Listening остаётся незакрытым.
            word_state.in_deck1 = True

            # Первый Context.
            word_state.in_deck2 = True
            word_state.in_deck3 = False


        word_state.save(
            update_fields=[
                "in_deck1",
                "in_deck2",
                "in_deck3",
                "mistake_count",
            ]
        )


        advance_current_queue(
            session
        )


        if (
            session.current_index
            <
            len(session.current_queue)
        ):

            return


        ids = initial_context_ids()


        if ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .CONTEXT_REVIEW
                ),
                ids,
                shuffle=True,
            )

        else:

            finish_unified_practice(
                session
            )


        return


    # =====================================================
    # DECK 2
    # CONTEXT
    #
    # Первый Context:
    # Correct -> Listening review.
    # Wrong   -> Spelling.
    #
    # Context review:
    # Correct -> Listening review.
    # Wrong   -> Hard Choice.
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .CONTEXT_REVIEW
    ):

        is_review_context = (
            word_state.in_deck3
        )


        if is_correct:

            word_state.in_deck2 = False


            if is_review_context:

                word_state.in_deck3 = False


            word_state.save(
                update_fields=[
                    "in_deck2",
                    "in_deck3",
                ]
            )


            advance_current_queue(
                session
            )


            if (
                session.current_index
                <
                len(session.current_queue)
            ):

                return


            if is_review_context:

                start_listening_review_4()

                return


            ids = spelling_ids()


            if ids:

                set_unified_phase(
                    session,
                    (
                        UnifiedGroupPracticeSession
                        .Phase
                        .LETTER_FIRST
                    ),
                    ids,
                    shuffle=True,
                )

            else:

                start_listening_review_4()


            return


        register_word_mistake(
            session,
            word_state,
        )


        # -------------------------------------------------
        # FIRST CONTEXT WRONG
        # -> Spelling
        # -------------------------------------------------

        if not is_review_context:

            word_state.in_deck2 = False
            word_state.in_deck3 = True


            word_state.save(
                update_fields=[
                    "in_deck2",
                    "in_deck3",
                    "mistake_count",
                ]
            )


            advance_current_queue(
                session
            )


            if (
                session.current_index
                <
                len(session.current_queue)
            ):

                return


            ids = spelling_ids()


            if ids:

                set_unified_phase(
                    session,
                    (
                        UnifiedGroupPracticeSession
                        .Phase
                        .LETTER_FIRST
                    ),
                    ids,
                    shuffle=True,
                )

            else:

                start_listening_review_4()


            return


        # -------------------------------------------------
        # REVIEW CONTEXT WRONG
        # -> Hard Choice immediately
        # -------------------------------------------------

        word_state.in_deck2 = False
        word_state.in_deck3 = False
        word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck3",
                "in_deck5",
                "mistake_count",
            ]
        )


        start_hard_4()

        return


    # =====================================================
    # DECK 3
    # SPELLING — FIRST PASS
    #
    # Correct -> Context review.
    # Wrong   -> Choice.
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LETTER_FIRST
    ):

        if is_correct:

            # Context review marker.
            word_state.in_deck2 = True
            word_state.in_deck3 = True

        else:

            register_word_mistake(
                session,
                word_state,
            )

            word_state.in_deck2 = False
            word_state.in_deck3 = False
            word_state.in_deck4 = True


        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck3",
                "in_deck4",
                "mistake_count",
            ]
        )


        advance_current_queue(
            session
        )


        if (
            session.current_index
            <
            len(session.current_queue)
        ):

            return


        ids = get_deck_ids(
            session,
            4,
        )


        if ids:

            set_unified_phase(
                session,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .MULTIPLE_CHOICE_1
                ),
                ids,
                shuffle=True,
            )

        else:

            start_context_review_4()


        return


    # =====================================================
    # DECK 4
    # NORMAL CHOICE
    #
    # Correct -> Spelling review.
    # Wrong   -> Hard Choice.
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_1
    ):

        if is_correct:

            word_state.in_deck4 = False

            # Возвращаем в Spelling.
            word_state.in_deck2 = False
            word_state.in_deck3 = True

        else:

            register_word_mistake(
                session,
                word_state,
            )

            word_state.in_deck4 = False
            word_state.in_deck2 = False
            word_state.in_deck3 = False
            word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck3",
                "in_deck4",
                "in_deck5",
                "mistake_count",
            ]
        )


        advance_current_queue(
            session
        )


        if (
            session.current_index
            <
            len(session.current_queue)
        ):

            return


        if get_deck_ids(
            session,
            5,
        ):

            start_hard_4()

        else:

            start_spelling_review_4()


        return


    # =====================================================
    # DECK 5
    # HARD CHOICE
    #
    # Одна ошибка -> вся колода сначала.
    #
    # Идеальный круг -> Spelling.
    #
    # Слово НЕ удаляется из Hard здесь.
    # Оно удалится только после
    # правильного Spelling.
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

            word_state.in_deck5 = True


            word_state.save(
                update_fields=[
                    "in_deck5",
                    "mistake_count",
                ]
            )


            start_hard_4()

            return


        advance_current_queue(
            session
        )


        if (
            session.current_index
            <
            len(session.current_queue)
        ):

            return


        ids = get_deck_ids(
            session,
            5,
        )


        session.word_states.filter(
            word_id__in=ids,
        ).update(
            in_deck2=False,
            in_deck3=True,
            in_deck4=False,
        )


        start_spelling_review_4()

        return


    # =====================================================
    # SPELLING REVIEW
    #
    # Correct:
    # -> удаляем из Hard Choice
    # -> Context
    #
    # Wrong:
    # -> Hard Choice immediately
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .LETTER_REVIEW
    ):

        if is_correct:

            word_state.in_deck2 = True
            word_state.in_deck3 = True

            # КЛЮЧЕВОЕ ПРАВИЛО.
            word_state.in_deck5 = False


            word_state.save(
                update_fields=[
                    "in_deck2",
                    "in_deck3",
                    "in_deck5",
                ]
            )


            advance_current_queue(
                session
            )


            if (
                session.current_index
                <
                len(session.current_queue)
            ):

                return


            start_context_review_4()

            return


        register_word_mistake(
            session,
            word_state,
        )


        word_state.in_deck2 = False
        word_state.in_deck3 = False
        word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck2",
                "in_deck3",
                "in_deck5",
                "mistake_count",
            ]
        )


        start_hard_4()

        return


    # =====================================================
    # FINAL LISTENING
    #
    # Correct -> слово окончательно выходит.
    # Wrong   -> Hard Choice immediately.
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


            advance_current_queue(
                session
            )


            if (
                session.current_index
                <
                len(session.current_queue)
            ):

                return


            start_listening_review_4()

            return


        register_word_mistake(
            session,
            word_state,
        )


        word_state.in_deck1 = True
        word_state.in_deck2 = False
        word_state.in_deck3 = False
        word_state.in_deck4 = False
        word_state.in_deck5 = True


        word_state.save(
            update_fields=[
                "in_deck1",
                "in_deck2",
                "in_deck3",
                "in_deck4",
                "in_deck5",
                "mistake_count",
            ]
        )


        start_hard_4()

        return


    raise ValueError(
        "Unknown phase for four-stage Unified Practice."
    )

def process_unified_answer(
    session,
    word_id,
    is_correct,
):

    # TWO_STAGE_UNIFIED_ROUTE

    if (
        get_unified_available_stage_count(
            session.user,
            session.group,
        )
        ==
        2
    ):

        return process_two_stage_unified_answer(
            session=session,
            word_id=word_id,
            is_correct=is_correct,
        )


    # THREE_STAGE_UNIFIED_ROUTE

    if (
        get_unified_available_stage_count(
            session.user,
            session.group,
        )
        ==
        3
    ):

        return process_three_stage_unified_answer(
            session=session,
            word_id=word_id,
            is_correct=is_correct,
        )



    # FOUR_STAGE_UNIFIED_ROUTE

    if (
        get_unified_available_stage_count(
            session.user,
            session.group,
        )
        ==
        4
    ):

        return process_four_stage_unified_answer(
            session=session,
            word_id=word_id,
            is_correct=is_correct,
        )


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

        "available_stage_count":
            get_unified_available_stage_count(
                session.user,
                session.group,
            ),

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