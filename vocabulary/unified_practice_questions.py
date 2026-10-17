import random
import re

from .models import (
    UnifiedGroupPracticeSession,
    VocabularyWord,
)


# =========================================================
# NORMALIZATION
# =========================================================


def normalize_text(value):
    """
    Нормализация текстового ответа.

    Разрешаем:
    - разный регистр;
    - лишние пробелы;
    - разные апострофы;
    - разные виды дефиса.
    """

    value = str(
        value
        or ""
    )

    value = (
        value
        .strip()
        .lower()
    )

    value = (
        value
        .replace(
            "’",
            "'",
        )
        .replace(
            "‘",
            "'",
        )
    )

    for dash in [
        "‐",
        "-",
        "‒",
        "–",
        "—",
    ]:

        value = value.replace(
            dash,
            "-",
        )

    value = " ".join(
        value.split()
    )

    return value


# =========================================================
# CONTEXT SENTENCE
# =========================================================


def mask_context_sentence(
    sentence,
    word,
):

    sentence = str(
        sentence
        or ""
    ).strip()

    word = str(
        word
        or ""
    ).strip()


    if not sentence:
        return ""


    # Если пропуск уже есть,
    # оставляем предложение как есть.

    if re.search(
        r"_{3,}",
        sentence,
    ):

        return sentence


    if not word:
        return sentence


    # Ищем первое вхождение слова
    # без учёта регистра.
    #
    # Такой вариант работает и
    # для слов с дефисами/апострофами.

    pattern = re.compile(
        rf"(?<!\w)"
        rf"{re.escape(word)}"
        rf"(?!\w)",
        flags=re.IGNORECASE,
    )


    masked_sentence, count = (
        pattern.subn(
            "___",
            sentence,
            count=1,
        )
    )


    if count:

        return masked_sentence


    return sentence


# =========================================================
# CURRENT WORD
# =========================================================


def get_current_unified_word(
    session,
):

    if session.is_completed:
        return None


    if not session.current_queue:
        return None


    if (
        session.current_index
        >=
        len(
            session.current_queue
        )
    ):

        return None


    word_id = int(
        session.current_queue[
            session.current_index
        ]
    )


    return (
        VocabularyWord.objects
        .filter(
            id=word_id,
            is_active=True,
        )
        .first()
    )


# =========================================================
# DISTRACTOR WORDS
# =========================================================


def get_candidate_words(
    session,
    current_word,
):

    # =====================================================
    # WORDS FROM CURRENT GROUP
    # =====================================================

    group_words = list(
        VocabularyWord.objects
        .filter(
            lesson__group=(
                session.group
            ),
            is_active=True,
        )
        .exclude(
            id=current_word.id,
        )
    )


    random.shuffle(
        group_words
    )


    # Сначала стараемся использовать
    # слова той же части речи.

    same_pos = [
        word

        for word
        in group_words

        if (
            word.part_of_speech
            ==
            current_word.part_of_speech
        )
    ]


    other_pos = [
        word

        for word
        in group_words

        if (
            word.part_of_speech
            !=
            current_word.part_of_speech
        )
    ]


    random.shuffle(
        same_pos
    )

    random.shuffle(
        other_pos
    )


    candidates = (
        same_pos
        +
        other_pos
    )


    # =====================================================
    # FALLBACK:
    # WORDS FROM SAME CEFR LEVEL
    # =====================================================

    level_words = list(
        VocabularyWord.objects
        .filter(
            lesson__group__level=(
                session.group.level
            ),
            is_active=True,
        )
        .exclude(
            id=current_word.id,
        )
    )


    random.shuffle(
        level_words
    )


    used_ids = {
        word.id

        for word
        in candidates
    }


    for word in level_words:

        if (
            word.id
            in
            used_ids
        ):

            continue


        used_ids.add(
            word.id
        )


        candidates.append(
            word
        )


    return candidates


# =========================================================
# DECK 1
#
# LISTENING
# AUDIO -> TYPE ENGLISH WORD
# =========================================================


def build_listening_question(
    session,
    word,
):

    audio_url = None


    if word.audio_file:

        try:

            audio_url = (
                word
                .audio_file
                .url
            )

        except ValueError:

            audio_url = None


    return {

        "type":
            "listening",

        "deck":
            1,

        "word_id":
            word.id,

        "audio_url":
            audio_url,

    }


# =========================================================
# DECK 2
#
# LETTER CONSTRUCTION
# =========================================================


def build_letter_question(
    session,
    word,
):

    source = (
        word.word
        or ""
    ).strip()


    # =====================================================
    # LETTER TOKENS
    # =====================================================
    #
    # Каждая буква имеет уникальный ID.
    #
    # Это важно для слов с повторяющимися
    # буквами:
    #
    # apple -> p и p должны быть
    # разными плитками.
    #
    # Пробелы и дефисы не превращаем
    # в отдельные плитки.

    letter_tokens = []


    for index, char in enumerate(
        source
    ):

        if (
            char.isspace()
            or
            char in [
                "-",
                "‐",
                "‒",
                "–",
                "—",
            ]
        ):

            continue


        letter_tokens.append(
            {

                "id":
                    f"{word.id}-{index}",

                "letter":
                    char,

            }
        )


    random.shuffle(
        letter_tokens
    )


    # =====================================================
    # WORD PATTERN
    # =====================================================
    #
    # Например:
    #
    # apple
    # _____
    #
    # ice cream
    # ___ _____
    #
    # part-time
    # ____-____

    pattern = ""


    for char in source:

        if char.isspace():

            pattern += " "


        elif char in [
            "-",
            "‐",
            "‒",
            "–",
            "—",
        ]:

            pattern += "-"


        else:

            pattern += "_"


    return {

        "type":
            "letters",

        "deck":
            2,

        "word_id":
            word.id,

        "translation":
            word.translation_ru,

        "pattern":
            pattern,

        "letters":
            letter_tokens,

    }


# =========================================================
# DECK 3
#
# CONTEXT
# CHOOSE CORRECT ENGLISH WORD
# =========================================================


def build_context_question(
    session,
    word,
):

    correct_word = (
        word.word
        or ""
    ).strip()


    options = [
        correct_word
    ]


    used = {
        normalize_text(
            correct_word
        )
    }


    # =====================================================
    # CURATED WRONG OPTIONS
    # =====================================================

    wrong_options = (
        word.context_wrong_options
        or []
    )


    if isinstance(
        wrong_options,
        list,
    ):

        for option in wrong_options:

            option = str(
                option
                or ""
            ).strip()


            if not option:
                continue


            normalized = (
                normalize_text(
                    option
                )
            )


            if normalized in used:
                continue


            used.add(
                normalized
            )


            options.append(
                option
            )


            if len(options) == 4:
                break


    # =====================================================
    # FALLBACK DISTRACTORS
    # =====================================================
    #
    # Если для слова в базе нет
    # трёх контекстных distractors,
    # берём дополнительные слова.

    if len(options) < 4:

        candidates = (
            get_candidate_words(
                session,
                word,
            )
        )


        for candidate in candidates:

            option = (
                candidate.word
                or ""
            ).strip()


            if not option:
                continue


            normalized = (
                normalize_text(
                    option
                )
            )


            if normalized in used:
                continue


            used.add(
                normalized
            )


            options.append(
                option
            )


            if len(options) == 4:
                break


    random.shuffle(
        options
    )


    return {

        "type":
            "context",

        "deck":
            3,

        "word_id":
            word.id,

        "sentence":
            mask_context_sentence(
                word.context_sentence,
                word.word,
            ),

        "options":
            options,

    }


# =========================================================
# DECK 4
#
# MULTIPLE CHOICE 1
# ENGLISH -> RUSSIAN
# =========================================================


def build_multiple_choice_1(
    session,
    word,
):

    correct_translation = (
        word.translation_ru
        or ""
    ).strip()


    options = [
        correct_translation
    ]


    used_translations = {
        normalize_text(
            correct_translation
        )
    }


    candidates = (
        get_candidate_words(
            session,
            word,
        )
    )


    for candidate in candidates:

        translation = (
            candidate.translation_ru
            or ""
        ).strip()


        if not translation:
            continue


        normalized = (
            normalize_text(
                translation
            )
        )


        if (
            normalized
            in
            used_translations
        ):

            continue


        used_translations.add(
            normalized
        )


        options.append(
            translation
        )


        if len(options) == 4:
            break


    random.shuffle(
        options
    )


    return {

        "type":
            "multiple_choice_1",

        "deck":
            4,

        "word_id":
            word.id,

        "prompt":
            word.word,

        # В браузер передаём только
        # текст вариантов.
        #
        # ID правильного варианта
        # здесь больше нет.

        "options":
            options,

    }


# =========================================================
# DECK 5
#
# MULTIPLE CHOICE 2
# RUSSIAN -> ENGLISH
# =========================================================


def build_multiple_choice_2(
    session,
    word,
):

    correct_word = (
        word.word
        or ""
    ).strip()


    options = [
        correct_word
    ]


    used_words = {
        normalize_text(
            correct_word
        )
    }


    candidates = (
        get_candidate_words(
            session,
            word,
        )
    )


    for candidate in candidates:

        english_word = (
            candidate.word
            or ""
        ).strip()


        if not english_word:
            continue


        normalized = (
            normalize_text(
                english_word
            )
        )


        if normalized in used_words:
            continue


        used_words.add(
            normalized
        )


        options.append(
            english_word
        )


        if len(options) == 4:
            break


    random.shuffle(
        options
    )


    return {

        "type":
            "multiple_choice_2",

        "deck":
            5,

        "word_id":
            word.id,

        "prompt":
            word.translation_ru,

        # Как и в Deck 4,
        # только текст вариантов.

        "options":
            options,

    }


# =========================================================
# CURRENT QUESTION
# =========================================================


def build_unified_question(
    session,
):

    word = (
        get_current_unified_word(
            session
        )
    )


    if word is None:
        return None


    phase = session.phase


    # =====================================================
    # DECK 1
    # =====================================================

    if phase in [
        (
            UnifiedGroupPracticeSession
            .Phase
            .LISTENING_INITIAL
        ),
        (
            UnifiedGroupPracticeSession
            .Phase
            .LISTENING_REVIEW
        ),
    ]:

        return build_listening_question(
            session,
            word,
        )


    # =====================================================
    # DECK 2
    # =====================================================

    if phase in [
        (
            UnifiedGroupPracticeSession
            .Phase
            .LETTER_FIRST
        ),
        (
            UnifiedGroupPracticeSession
            .Phase
            .LETTER_REVIEW
        ),
    ]:

        return build_letter_question(
            session,
            word,
        )


    # =====================================================
    # DECK 3
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .CONTEXT_REVIEW
    ):

        return build_context_question(
            session,
            word,
        )


    # =====================================================
    # DECK 4
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_1
    ):

        return build_multiple_choice_1(
            session,
            word,
        )


    # =====================================================
    # DECK 5
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_2
    ):

        return build_multiple_choice_2(
            session,
            word,
        )


    return None


# =========================================================
# SERVER-SIDE ANSWER CHECK
# =========================================================


def check_unified_answer(
    session,
    answer,
):

    word = (
        get_current_unified_word(
            session
        )
    )


    if word is None:

        raise ValueError(
            "Current word not found."
        )


    phase = session.phase


    # =====================================================
    # DECK 1
    #
    # LISTENING
    # USER TYPES ENGLISH WORD
    # =====================================================

    if phase in [
        (
            UnifiedGroupPracticeSession
            .Phase
            .LISTENING_INITIAL
        ),
        (
            UnifiedGroupPracticeSession
            .Phase
            .LISTENING_REVIEW
        ),
    ]:

        return (
            normalize_text(
                answer
            )
            ==
            normalize_text(
                word.word
            )
        )


    # =====================================================
    # DECK 2
    #
    # LETTER CONSTRUCTION
    # =====================================================

    if phase in [
        (
            UnifiedGroupPracticeSession
            .Phase
            .LETTER_FIRST
        ),
        (
            UnifiedGroupPracticeSession
            .Phase
            .LETTER_REVIEW
        ),
    ]:

        return (
            normalize_text(
                answer
            )
            ==
            normalize_text(
                word.word
            )
        )


    # =====================================================
    # DECK 3
    #
    # CONTEXT
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .CONTEXT_REVIEW
    ):

        return (
            normalize_text(
                answer
            )
            ==
            normalize_text(
                word.word
            )
        )


    # =====================================================
    # DECK 4
    #
    # ENGLISH -> RUSSIAN
    #
    # Пользователь отправляет текст
    # выбранного русского перевода.
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_1
    ):

        return (
            normalize_text(
                answer
            )
            ==
            normalize_text(
                word.translation_ru
            )
        )


    # =====================================================
    # DECK 5
    #
    # RUSSIAN -> ENGLISH
    #
    # Пользователь отправляет текст
    # выбранного английского слова.
    # =====================================================

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .MULTIPLE_CHOICE_2
    ):

        return (
            normalize_text(
                answer
            )
            ==
            normalize_text(
                word.word
            )
        )


    # =====================================================
    # UNKNOWN PHASE
    # =====================================================

    raise ValueError(
        "Unknown unified practice phase."
    )