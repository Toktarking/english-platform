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
    get_deck_ids,
    get_or_create_unified_practice,
    process_unified_answer,
)


User = get_user_model()


class UnifiedPracticeEngineTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="practice_test_user",
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
            code="test-group",
            name="Test Group",
            order=1,
            description="",
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
            source_id=900001,
            word="apple",
            translation_ru="яблоко",
            order=1,
        )

        self.word2 = self.create_word(
            source_id=900002,
            word="house",
            translation_ru="дом",
            order=2,
        )

        self.word3 = self.create_word(
            source_id=900003,
            word="water",
            translation_ru="вода",
            order=3,
        )


    def create_word(
        self,
        source_id,
        word,
        translation_ru,
        order,
    ):

        return VocabularyWord.objects.create(
            lesson=self.lesson,
            source_id=source_id,
            original_headword=word,
            word=word,
            sense="",
            part_of_speech="noun",
            translation_ru=translation_ru,
            translation_kz=translation_ru,
            example_en=f"This is {word}.",
            example_ru="Пример.",
            example_kz="Мысал.",
            context_sentence=f"I see ___ here.",
            context_wrong_options=[
                "book",
                "table",
                "chair",
            ],
            order=order,
            is_active=True,
        )


    # =====================================================
    # HELPERS
    # =====================================================

    def current_word_id(
        self,
        session,
    ):

        session.refresh_from_db()

        return int(
            session.current_queue[
                session.current_index
            ]
        )


    def answer(
        self,
        session,
        is_correct,
    ):

        word_id = self.current_word_id(
            session
        )

        process_unified_answer(
            session=session,
            word_id=word_id,
            is_correct=is_correct,
        )

        session.refresh_from_db()

        return word_id


    def answer_initial_by_ids(
        self,
        session,
        wrong_ids,
    ):

        wrong_ids = set(
            wrong_ids
        )

        while (
            session.phase
            ==
            UnifiedGroupPracticeSession
            .Phase
            .LISTENING_INITIAL
        ):

            word_id = self.current_word_id(
                session
            )

            self.answer(
                session,
                word_id not in wrong_ids,
            )


    # =====================================================
    # TEST 1
    # PERFECT INITIAL LISTENING
    # =====================================================

    def test_perfect_initial_listening_finishes_immediately(
        self,
    ):

        session = (
            get_or_create_unified_practice(
                user=self.user,
                group=self.group,
            )
        )

        while not session.is_completed:

            self.assertEqual(
                session.phase,
                (
                    UnifiedGroupPracticeSession
                    .Phase
                    .LISTENING_INITIAL
                ),
            )

            self.answer(
                session,
                True,
            )

        self.assertTrue(
            session.is_completed
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .COMPLETED
            ),
        )

        self.assertEqual(
            get_deck_ids(
                session,
                1,
            ),
            [],
        )

        self.assertEqual(
            get_deck_ids(
                session,
                5,
            ),
            [],
        )


    # =====================================================
    # TEST 2
    #
    # LISTENING WRONG
    # -> LETTER CORRECT
    # -> CONTEXT CORRECT
    # -> LISTENING CORRECT
    # -> WIN
    # =====================================================

    def test_basic_learning_route_without_deck5(
        self,
    ):

        session = (
            get_or_create_unified_practice(
                user=self.user,
                group=self.group,
            )
        )

        self.answer_initial_by_ids(
            session,
            wrong_ids=[
                self.word1.id,
            ],
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_FIRST
            ),
        )

        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    2,
                )
            ),
            {
                self.word1.id,
            },
        )

        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    3,
                )
            ),
            {
                self.word1.id,
            },
        )

        # Letter Construction
        self.answer(
            session,
            True,
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .CONTEXT_REVIEW
            ),
        )

        # Context
        self.answer(
            session,
            True,
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LISTENING_REVIEW
            ),
        )

        # Final Listening
        self.answer(
            session,
            True,
        )

        self.assertTrue(
            session.is_completed
        )

        self.assertEqual(
            get_deck_ids(
                session,
                5,
            ),
            [],
        )


    # =====================================================
    # TEST 3
    #
    # LETTER WRONG
    # -> DECK 4
    # -> DECK 4 CORRECT
    # -> DECK 2
    # -> DECK 3
    # -> DECK 1
    # =====================================================

    def test_deck4_returns_word_to_letter_review(
        self,
    ):

        session = (
            get_or_create_unified_practice(
                user=self.user,
                group=self.group,
            )
        )

        self.answer_initial_by_ids(
            session,
            wrong_ids=[
                self.word1.id,
            ],
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_FIRST
            ),
        )

        # Ошибка в первом Letter Construction.
        self.answer(
            session,
            False,
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_1
            ),
        )

        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    4,
                )
            ),
            {
                self.word1.id,
            },
        )

        # Deck 4 успешно.
        self.answer(
            session,
            True,
        )

        # Должен вернуться в Deck 2.
        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_REVIEW
            ),
        )

        self.assertEqual(
            get_deck_ids(
                session,
                5,
            ),
            [],
        )

        # Deck 2
        self.answer(
            session,
            True,
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .CONTEXT_REVIEW
            ),
        )

        # Deck 3
        self.answer(
            session,
            True,
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LISTENING_REVIEW
            ),
        )

        # Deck 1
        self.answer(
            session,
            True,
        )

        self.assertTrue(
            session.is_completed
        )


    # =====================================================
    # TEST 4
    #
    # DECK 5:
    # - накапливается;
    # - не очищается;
    # - ошибка перезапускает всю колоду;
    # - после идеального круга:
    #   Deck 5 -> Deck 2 + Deck 3 + Deck 1
    # =====================================================

    def test_deck5_is_permanent_and_restarts_on_error(
        self,
    ):

        session = (
            get_or_create_unified_practice(
                user=self.user,
                group=self.group,
            )
        )

        # Apple и House ошибочны в Listening.
        self.answer_initial_by_ids(
            session,
            wrong_ids=[
                self.word1.id,
                self.word2.id,
            ],
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_FIRST
            ),
        )

        # ---------------------------------------------
        # В первом Deck 2:
        #
        # apple -> wrong
        # house -> correct
        # ---------------------------------------------

        while (
            session.phase
            ==
            UnifiedGroupPracticeSession
            .Phase
            .LETTER_FIRST
        ):

            word_id = self.current_word_id(
                session
            )

            self.answer(
                session,
                (
                    word_id
                    !=
                    self.word1.id
                ),
            )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_1
            ),
        )

        # Только apple должна быть в Deck 4.
        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    4,
                )
            ),
            {
                self.word1.id,
            },
        )

        # Apple ошибочно в Deck 4.
        # Она впервые попадает в Deck 5.
        self.answer(
            session,
            False,
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_2
            ),
        )

        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    5,
                )
            ),
            {
                self.word1.id,
            },
        )

        # Первый идеальный проход Deck 5.
        self.answer(
            session,
            True,
        )

        # Deck 5 НЕ очищена.
        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    5,
                )
            ),
            {
                self.word1.id,
            },
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_REVIEW
            ),
        )

        # Apple успешно проходит Deck 2.
        self.answer(
            session,
            True,
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .CONTEXT_REVIEW
            ),
        )

        # ---------------------------------------------
        # В Context:
        #
        # apple -> correct
        # house -> wrong
        #
        # Теперь Deck 5 должна накопить
        # apple + house.
        # ---------------------------------------------

        while (
            session.phase
            ==
            UnifiedGroupPracticeSession
            .Phase
            .CONTEXT_REVIEW
        ):

            word_id = self.current_word_id(
                session
            )

            if (
                word_id
                ==
                self.word2.id
            ):

                self.answer(
                    session,
                    False,
                )

            else:

                self.answer(
                    session,
                    True,
                )


        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_2
            ),
        )

        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    5,
                )
            ),
            {
                self.word1.id,
                self.word2.id,
            },
        )


        # ---------------------------------------------
        # Проверяем перезапуск Deck 5.
        #
        # Первый ответ правильный.
        # Второй неправильный.
        # После ошибки current_index снова 0.
        # ---------------------------------------------

        self.answer(
            session,
            True,
        )

        mistakes_before = (
            session.mistake_count
        )

        self.answer(
            session,
            False,
        )

        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .MULTIPLE_CHOICE_2
            ),
        )

        self.assertEqual(
            session.current_index,
            0,
        )

        self.assertEqual(
            session.mistake_count,
            mistakes_before + 1,
        )

        self.assertEqual(
            set(
                session.current_queue
            ),
            {
                self.word1.id,
                self.word2.id,
            },
        )

        # Deck 5 всё ещё содержит оба слова.
        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    5,
                )
            ),
            {
                self.word1.id,
                self.word2.id,
            },
        )


        # ---------------------------------------------
        # Теперь проходим ВСЮ Deck 5 идеально.
        # ---------------------------------------------

        while (
            session.phase
            ==
            UnifiedGroupPracticeSession
            .Phase
            .MULTIPLE_CHOICE_2
        ):

            self.answer(
                session,
                True,
            )


        self.assertEqual(
            session.phase,
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_REVIEW
            ),
        )


        # Deck 5 НЕ очищена даже после
        # идеального прохождения.
        self.assertEqual(
            set(
                get_deck_ids(
                    session,
                    5,
                )
            ),
            {
                self.word1.id,
                self.word2.id,
            },
        )


        # И ВСЕ слова Deck 5 заново
        # отправлены в 2 -> 3 -> 1.
        self.assertTrue(
            {
                self.word1.id,
                self.word2.id,
            }
            .issubset(
                set(
                    get_deck_ids(
                        session,
                        2,
                    )
                )
            )
        )

        self.assertTrue(
            {
                self.word1.id,
                self.word2.id,
            }
            .issubset(
                set(
                    get_deck_ids(
                        session,
                        3,
                    )
                )
            )
        )

        self.assertTrue(
            {
                self.word1.id,
                self.word2.id,
            }
            .issubset(
                set(
                    get_deck_ids(
                        session,
                        1,
                    )
                )
            )
        )