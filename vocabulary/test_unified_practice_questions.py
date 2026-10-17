from collections import Counter

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import (
    UnifiedGroupPracticeSession,
    VocabularyGroup,
    VocabularyLesson,
    VocabularyLevel,
    VocabularyWord,
)

from .unified_practice import (
    get_or_create_unified_practice,
)

from .unified_practice_questions import (
    build_unified_question,
    check_unified_answer,
)


User = get_user_model()


class UnifiedPracticeQuestionTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="question_test_user",
            password="test-password-123",
        )

        self.level = VocabularyLevel.objects.create(
            code="A1",
            name="A1 Test",
            order=1,
            is_active=True,
        )

        self.group = VocabularyGroup.objects.create(
            level=self.level,
            code="question-test",
            name="Question Test",
            order=1,
        )

        self.lesson = VocabularyLesson.objects.create(
            group=self.group,
            number=1,
            global_number=1,
            title="Test Lesson",
            order=1,
            is_active=True,
        )

        self.word1 = self.create_word(
            910001,
            "apple",
            "яблоко",
            1,
        )

        self.word2 = self.create_word(
            910002,
            "house",
            "дом",
            2,
        )

        self.word3 = self.create_word(
            910003,
            "water",
            "вода",
            3,
        )

        self.word4 = self.create_word(
            910004,
            "book",
            "книга",
            4,
        )

        self.word5 = self.create_word(
            910005,
            "chair",
            "стул",
            5,
        )

        self.session = (
            get_or_create_unified_practice(
                user=self.user,
                group=self.group,
            )
        )


    def create_word(
        self,
        source_id,
        word,
        translation,
        order,
    ):

        return VocabularyWord.objects.create(
            lesson=self.lesson,
            source_id=source_id,
            original_headword=word,
            word=word,
            sense="",
            part_of_speech="noun",
            translation_ru=translation,
            translation_kz=translation,
            example_en=f"This is {word}.",
            example_ru="Пример.",
            example_kz="Мысал.",
            context_sentence=(
                "I can see ___ in the room."
            ),
            context_wrong_options=[
                "table",
                "window",
                "door",
            ],
            order=order,
            is_active=True,
        )


    # =====================================================
    # HELPER
    # =====================================================

    def set_question(
        self,
        phase,
        word,
    ):

        self.session.phase = phase

        self.session.current_queue = [
            word.id
        ]

        self.session.current_index = 0

        self.session.is_completed = False

        self.session.save(
            update_fields=[
                "phase",
                "current_queue",
                "current_index",
                "is_completed",
                "updated_at",
            ]
        )


    # =====================================================
    # DECK 1
    # LISTENING
    # =====================================================

    def test_listening_question(
        self,
    ):

        self.set_question(
            (
                UnifiedGroupPracticeSession
                .Phase
                .LISTENING_INITIAL
            ),
            self.word1,
        )

        question = (
            build_unified_question(
                self.session
            )
        )

        self.assertEqual(
            question["type"],
            "listening",
        )

        self.assertEqual(
            question["deck"],
            1,
        )

        self.assertEqual(
            question["word_id"],
            self.word1.id,
        )

        self.assertIn(
            "audio_url",
            question,
        )

        # Правильное слово специально
        # не передаётся браузеру.
        self.assertNotIn(
            "correct",
            question,
        )

        self.assertNotIn(
            "word",
            question,
        )


    # =====================================================
    # DECK 1
    # SERVER-SIDE ANSWER CHECK
    # =====================================================

    def test_listening_answer_is_checked_on_server(
        self,
    ):

        self.set_question(
            (
                UnifiedGroupPracticeSession
                .Phase
                .LISTENING_INITIAL
            ),
            self.word1,
        )

        self.assertTrue(
            check_unified_answer(
                self.session,
                "apple",
            )
        )

        # Регистр и лишние пробелы
        # не должны влиять.
        self.assertTrue(
            check_unified_answer(
                self.session,
                "  APPLE  ",
            )
        )

        self.assertFalse(
            check_unified_answer(
                self.session,
                "house",
            )
        )


    # =====================================================
    # DECK 2
    # LETTER CONSTRUCTION
    # =====================================================
    def test_letter_question(
        self,
    ):

        self.set_question(
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_FIRST
            ),
            self.word1,
        )


        question = (
            build_unified_question(
                self.session
            )
        )


        # =================================================
        # BASIC QUESTION DATA
        # =================================================

        self.assertEqual(
            question["type"],
            "letters",
        )


        self.assertEqual(
            question["deck"],
            2,
        )


        self.assertEqual(
            question["word_id"],
            self.word1.id,
        )


        self.assertEqual(
            question["translation"],
            "яблоко",
        )


        self.assertEqual(
            question["pattern"],
            "_____",
        )


        # =================================================
        # SLOT COUNT
        # =================================================
        #
        # Пользователь должен выбрать
        # ровно столько букв,
        # сколько букв в правильном слове.
        #
        # apple = 5 букв.

        self.assertEqual(
            question["slot_count"],
            5,
        )


        # =================================================
        # LETTER TILES
        # =================================================

        letters = [
            item["letter"]

            for item
            in question["letters"]
        ]


        # Для коротких слов показываем
        # минимум 8 плиток.
        #
        # apple имеет 5 букв,
        # поэтому добавляются
        # ещё 3 случайные буквы.

        self.assertEqual(
            len(
                letters
            ),
            8,
        )


        # =================================================
        # REQUIRED LETTERS
        # =================================================
        #
        # Все буквы правильного слова
        # обязательно должны присутствовать.
        #
        # При этом дополнительные
        # отвлекающие буквы разрешены.

        actual_counts = Counter(
            letters
        )


        expected_counts = Counter(
            "apple"
        )


        for (
            letter,
            expected_count,
        ) in expected_counts.items():

            self.assertGreaterEqual(
                actual_counts[
                    letter
                ],
                expected_count,
            )


        # =================================================
        # UNIQUE TILE IDS
        # =================================================
        #
        # Каждая плитка должна иметь
        # собственный уникальный ID.
        #
        # Это особенно важно для слов,
        # где одна буква встречается
        # несколько раз.
        #
        # Например:
        #
        # apple -> две разные плитки "p".

        letter_ids = [
            item["id"]

            for item
            in question["letters"]
        ]


        self.assertEqual(
            len(
                letter_ids
            ),
            len(
                set(
                    letter_ids
                )
            ),
        )


        # =================================================
        # SERVER-SIDE ANSWER CHECK
        # =================================================

        self.assertTrue(
            check_unified_answer(
                self.session,
                "apple",
            )
        )


        self.assertTrue(
            check_unified_answer(
                self.session,
                " APPLE ",
            )
        )


        self.assertFalse(
            check_unified_answer(
                self.session,
                "aple",
            )
        )


    # =====================================================
    # DECK 3
    # CONTEXT
    # =====================================================

    def test_context_question(
        self,
    ):

        self.set_question(
            (
                UnifiedGroupPracticeSession
                .Phase
                .CONTEXT_REVIEW
            ),
            self.word1,
        )

        question = (
            build_unified_question(
                self.session
            )
        )

        self.assertEqual(
            question["type"],
            "context",
        )

        self.assertEqual(
            question["deck"],
            3,
        )

        self.assertEqual(
            question["word_id"],
            self.word1.id,
        )

        self.assertEqual(
            question["sentence"],
            (
                "I can see ___ "
                "in the room."
            ),
        )

        self.assertEqual(
            len(
                question["options"]
            ),
            4,
        )

        self.assertIn(
            "apple",
            question["options"],
        )


        # Все четыре варианта должны
        # быть уникальными.
        self.assertEqual(
            len(
                set(
                    option.lower()
                    for option
                    in question["options"]
                )
            ),
            4,
        )


        self.assertTrue(
            check_unified_answer(
                self.session,
                "apple",
            )
        )

        self.assertFalse(
            check_unified_answer(
                self.session,
                "door",
            )
        )


    # =====================================================
    # DECK 4
    # MULTIPLE CHOICE 1
    #
    # ENGLISH -> RUSSIAN
    # =====================================================

    def test_multiple_choice_1(
        self,
    ):

        self.set_question(
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_1
            ),
            self.word1,
        )

        question = (
            build_unified_question(
                self.session
            )
        )

        self.assertEqual(
            question["type"],
            "multiple_choice_1",
        )

        self.assertEqual(
            question["deck"],
            4,
        )

        self.assertEqual(
            question["word_id"],
            self.word1.id,
        )

        self.assertEqual(
            question["prompt"],
            "apple",
        )

        self.assertEqual(
            len(
                question["options"]
            ),
            4,
        )


        # Теперь options — это только
        # строки, а не объекты с word_id.
        #
        # Браузер не получает ID
        # правильного варианта.

        self.assertTrue(
            all(
                isinstance(
                    option,
                    str,
                )
                for option
                in question["options"]
            )
        )


        self.assertIn(
            "яблоко",
            question["options"],
        )


        # Все переводы должны
        # быть уникальными.
        self.assertEqual(
            len(
                set(
                    option.lower()
                    for option
                    in question["options"]
                )
            ),
            4,
        )


        # Сервер проверяет сам текст
        # выбранного перевода.

        self.assertTrue(
            check_unified_answer(
                self.session,
                "яблоко",
            )
        )

        self.assertTrue(
            check_unified_answer(
                self.session,
                "  ЯБЛОКО  ",
            )
        )

        self.assertFalse(
            check_unified_answer(
                self.session,
                "дом",
            )
        )


    # =====================================================
    # DECK 5
    # MULTIPLE CHOICE 2
    #
    # RUSSIAN -> ENGLISH
    # =====================================================

    def test_multiple_choice_2(
        self,
    ):

        self.set_question(
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_2
            ),
            self.word1,
        )

        question = (
            build_unified_question(
                self.session
            )
        )

        self.assertEqual(
            question["type"],
            "multiple_choice_2",
        )

        self.assertEqual(
            question["deck"],
            5,
        )

        self.assertEqual(
            question["word_id"],
            self.word1.id,
        )

        self.assertEqual(
            question["prompt"],
            "яблоко",
        )

        self.assertEqual(
            len(
                question["options"]
            ),
            4,
        )


        # Как и в Deck 4,
        # браузер получает только
        # текст вариантов.

        self.assertTrue(
            all(
                isinstance(
                    option,
                    str,
                )
                for option
                in question["options"]
            )
        )


        self.assertIn(
            "apple",
            question["options"],
        )


        # Все английские варианты
        # должны быть уникальными.
        self.assertEqual(
            len(
                set(
                    option.lower()
                    for option
                    in question["options"]
                )
            ),
            4,
        )


        self.assertTrue(
            check_unified_answer(
                self.session,
                "apple",
            )
        )

        self.assertTrue(
            check_unified_answer(
                self.session,
                " APPLE ",
            )
        )

        self.assertFalse(
            check_unified_answer(
                self.session,
                "water",
            )
        )


    # =====================================================
    # FINAL STATE
    # =====================================================

    def test_completed_session_has_no_question(
        self,
    ):

        self.session.is_completed = True

        self.session.phase = (
            UnifiedGroupPracticeSession
            .Phase
            .COMPLETED
        )

        self.session.current_queue = []

        self.session.current_index = 0

        self.session.save()


        question = (
            build_unified_question(
                self.session
            )
        )

        self.assertIsNone(
            question
        )