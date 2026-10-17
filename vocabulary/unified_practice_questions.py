import random

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
        .replace("’", "'")
        .replace("‘", "'")
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
        len(session.current_queue)
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

    group_words = list(
        VocabularyWord.objects
        .filter(
            lesson__group=session.group,
            is_active=True,
        )
        .exclude(
            id=current_word.id,
        )
    )

    random.shuffle(
        group_words
    )

    same_pos = [
        word
        for word in group_words
        if (
            word.part_of_speech
            ==
            current_word.part_of_speech
        )
    ]

    other_pos = [
        word
        for word in group_words
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


    # Если внутри группы недостаточно слов,
    # добавляем слова того же CEFR-уровня.

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
        for word in candidates
    }

    for word in level_words:

        if word.id in used_ids:
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
# LISTENING -> TYPE ENGLISH WORD
# =========================================================


def build_listening_question(
    session,
    word,
):

    audio_url = None

    if word.audio_file:

        try:
            audio_url = (
                word.audio_file.url
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


    # Буквы перемешиваем.
    #
    # Каждой букве даём уникальный ID,
    # потому что в слове могут быть
    # одинаковые буквы.

    letter_tokens = []

    for index, char in enumerate(
        source
    ):

        if char.isspace():
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


    # Pattern нужен интерфейсу,
    # чтобы видеть пробелы и дефисы,
    # но не само слово.

    pattern = ""

    for char in source:

        if char == " ":
            pattern += " "

        elif char == "-":
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
# CONTEXT
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


    # Если в context_wrong_options
    # оказалось меньше трёх вариантов,
    # дополняем словами из базы.

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
            word.context_sentence,

        "options":
            options,
    }


# =========================================================
# DECK 4
# MULTIPLE CHOICE 1
#
# ENGLISH -> RUSSIAN
# =========================================================


def build_multiple_choice_1(
    session,
    word,
):

    options = [
        {
            "word_id":
                word.id,

            "text":
                word.translation_ru,
        }
    ]


    used_translations = {
        normalize_text(
            word.translation_ru
        )
    }

    used_word_ids = {
        word.id
    }


    candidates = (
        get_candidate_words(
            session,
            word,
        )
    )


    for candidate in candidates:

        if candidate.id in used_word_ids:
            continue

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

        if normalized in used_translations:
            continue

        used_word_ids.add(
            candidate.id
        )

        used_translations.add(
            normalized
        )

        options.append(
            {
                "word_id":
                    candidate.id,

                "text":
                    translation,
            }
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

        "options":
            options,
    }


# =========================================================
# DECK 5
# MULTIPLE CHOICE 2
#
# RUSSIAN -> ENGLISH
# =========================================================


def build_multiple_choice_2(
    session,
    word,
):

    options = [
        {
            "word_id":
                word.id,

            "text":
                word.word,
        }
    ]


    used_words = {
        normalize_text(
            word.word
        )
    }

    used_word_ids = {
        word.id
    }


    candidates = (
        get_candidate_words(
            session,
            word,
        )
    )


    for candidate in candidates:

        if candidate.id in used_word_ids:
            continue

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

        used_word_ids.add(
            candidate.id
        )

        used_words.add(
            normalized
        )

        options.append(
            {
                "word_id":
                    candidate.id,

                "text":
                    english_word,
            }
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


    # -----------------------------------------------------
    # DECK 1
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # DECK 2
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # DECK 3
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # DECK 4
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # DECK 5
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # DECK 1
    # LISTENING
    # -----------------------------------------------------

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
            normalize_text(answer)
            ==
            normalize_text(word.word)
        )


    # -----------------------------------------------------
    # DECK 2
    # LETTER CONSTRUCTION
    # -----------------------------------------------------

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
            normalize_text(answer)
            ==
            normalize_text(word.word)
        )


    # -----------------------------------------------------
    # DECK 3
    # CONTEXT
    # -----------------------------------------------------

    if (
        phase
        ==
        UnifiedGroupPracticeSession
        .Phase
        .CONTEXT_REVIEW
    ):

        return (
            normalize_text(answer)
            ==
            normalize_text(word.word)
        )


    # -----------------------------------------------------
    # DECK 4 / DECK 5
    #
    # Клиент отправляет word_id
    # выбранного варианта.
    # -----------------------------------------------------

    if phase in [
        (
            UnifiedGroupPracticeSession
            .Phase
            .MULTIPLE_CHOICE_1
        ),
        (
            UnifiedGroupPracticeSession
            .Phase
            .MULTIPLE_CHOICE_2
        ),
    ]:

        try:

            selected_word_id = int(
                answer
            )

        except (
            TypeError,
            ValueError,
        ):

            return False


        return (
            selected_word_id
            ==
            word.id
        )


    raise ValueError(
        "Unknown unified practice phase."
    )