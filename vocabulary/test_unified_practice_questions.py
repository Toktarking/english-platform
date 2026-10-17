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
                f"I can see ___ in the room."
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
        # не должно передаваться браузеру.
        self.assertNotIn(
            "correct",
            question,
        )

        self.assertNotIn(
            "word",
            question,
        )


    # =====================================================
    # LISTENING ANSWER CHECK
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


        letters = [
            item["letter"]
            for item in question["letters"]
        ]


        # Порядок случайный,
        # поэтому сравниваем состав букв.
        self.assertEqual(
            Counter(letters),
            Counter("apple"),
        )


        # ID каждой плитки должен
        # быть уникальным даже при
        # повторяющихся буквах.
        letter_ids = [
            item["id"]
            for item in question["letters"]
        ]

        self.assertEqual(
            len(letter_ids),
            len(set(letter_ids)),
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
            len(question["options"]),
            4,
        )

        self.assertIn(
            "apple",
            question["options"],
        )

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
            question["prompt"],
            "apple",
        )

        self.assertEqual(
            len(question["options"]),
            4,
        )


        option_ids = [
            option["word_id"]
            for option
            in question["options"]
        ]

        option_texts = [
            option["text"]
            for option
            in question["options"]
        ]


        self.assertIn(
            self.word1.id,
            option_ids,
        )

        self.assertIn(
            "яблоко",
            option_texts,
        )

        self.assertEqual(
            len(option_ids),
            len(set(option_ids)),
        )


        # Сервер принимает ID
        # выбранного варианта.

        self.assertTrue(
            check_unified_answer(
                self.session,
                self.word1.id,
            )
        )

        self.assertFalse(
            check_unified_answer(
                self.session,
                self.word2.id,
            )
        )


    # =====================================================
    # DECK 5
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
            question["prompt"],
            "яблоко",
        )

        self.assertEqual(
            len(question["options"]),
            4,
        )


        option_ids = [
            option["word_id"]
            for option
            in question["options"]
        ]

        option_texts = [
            option["text"]
            for option
            in question["options"]
        ]


        self.assertIn(
            self.word1.id,
            option_ids,
        )

        self.assertIn(
            "apple",
            option_texts,
        )

        self.assertEqual(
            len(option_ids),
            len(set(option_ids)),
        )


        self.assertTrue(
            check_unified_answer(
                self.session,
                str(
                    self.word1.id
                ),
            )
        )

        self.assertFalse(
            check_unified_answer(
                self.session,
                self.word3.id,
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