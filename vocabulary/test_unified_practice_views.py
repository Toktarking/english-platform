import json

from django.contrib.auth import get_user_model
from django.test import (
    RequestFactory,
    TestCase,
)

from .models import (
    UnifiedGroupPracticeSession,
    VocabularyGroup,
    VocabularyLesson,
    VocabularyLevel,
    VocabularyWord,
)

from .unified_practice_views import (
    unified_practice_answer,
    unified_practice_restart,
    unified_practice_state,
)


User = get_user_model()


class UnifiedPracticeApiTests(TestCase):

    def setUp(self):

        self.factory = RequestFactory()

        self.user = User.objects.create_user(
            username="api_test_user",
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
            code="api-test-group",
            name="API Test Group",
            order=1,
        )

        self.lesson = VocabularyLesson.objects.create(
            group=self.group,
            number=1,
            global_number=1,
            title="API Test Lesson",
            order=1,
            is_active=True,
        )

        self.words = [
            self.create_word(
                source_id=920001,
                word="apple",
                translation_ru="яблоко",
                order=1,
            ),
            self.create_word(
                source_id=920002,
                word="house",
                translation_ru="дом",
                order=2,
            ),
            self.create_word(
                source_id=920003,
                word="water",
                translation_ru="вода",
                order=3,
            ),
            self.create_word(
                source_id=920004,
                word="book",
                translation_ru="книга",
                order=4,
            ),
        ]


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
            context_sentence=(
                "I can see ___ here."
            ),
            context_wrong_options=[
                "table",
                "chair",
                "door",
            ],
            order=order,
            is_active=True,
        )


    # =====================================================
    # REQUEST HELPERS
    # =====================================================

    def get_state(self):

        request = self.factory.get(
            "/unified-practice/"
        )

        request.user = self.user

        response = unified_practice_state(
            request,
            level_code=self.level.code,
            group_id=self.group.id,
        )

        return (
            response,
            json.loads(
                response.content
            ),
        )


    def post_answer(
        self,
        word_id,
        answer,
    ):

        request = self.factory.post(
            "/unified-practice/answer/",
            data=json.dumps(
                {
                    "word_id":
                        word_id,

                    "answer":
                        answer,
                }
            ),
            content_type="application/json",
        )

        request.user = self.user

        response = unified_practice_answer(
            request,
            group_id=self.group.id,
        )

        return (
            response,
            json.loads(
                response.content
            ),
        )


    def post_restart(self):

        request = self.factory.post(
            "/unified-practice/restart/",
            data="{}",
            content_type="application/json",
        )

        request.user = self.user

        response = unified_practice_restart(
            request,
            group_id=self.group.id,
        )

        return (
            response,
            json.loads(
                response.content
            ),
        )


    # =====================================================
    # TEST 1
    # OPEN / CONTINUE
    # =====================================================

    def test_state_endpoint_creates_session(
        self,
    ):

        response, data = (
            self.get_state()
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTrue(
            data["success"]
        )

        self.assertEqual(
            data["group"]["id"],
            self.group.id,
        )

        self.assertEqual(
            data["group"]["level"],
            "A1",
        )

        self.assertEqual(
            data["state"]["phase"],
            (
                UnifiedGroupPracticeSession
                .Phase
                .LISTENING_INITIAL
            ),
        )

        self.assertEqual(
            data["state"]["deck1_count"],
            4,
        )

        self.assertEqual(
            data["state"]["deck2_count"],
            0,
        )

        self.assertEqual(
            data["state"]["deck5_count"],
            0,
        )

        self.assertEqual(
            data["state"]["question"]["deck"],
            1,
        )

        self.assertEqual(
            data["state"]["question"]["type"],
            "listening",
        )

        self.assertTrue(
            UnifiedGroupPracticeSession.objects
            .filter(
                user=self.user,
                group=self.group,
            )
            .exists()
        )


    # =====================================================
    # TEST 2
    #
    # SERVER CHECKS LISTENING ANSWER
    # =====================================================

    def test_answer_endpoint_checks_answer_on_server(
        self,
    ):

        response, data = (
            self.get_state()
        )

        word_id = (
            data["state"]
            ["question"]
            ["word_id"]
        )

        current_word = (
            VocabularyWord.objects
            .get(
                id=word_id
            )
        )

        response, data = (
            self.post_answer(
                word_id=word_id,
                answer=current_word.word,
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTrue(
            data["success"]
        )

        self.assertTrue(
            data["answer"]["is_correct"]
        )

        self.assertEqual(
            data["answer"]["word_id"],
            current_word.id,
        )

        self.assertEqual(
            data["answer"]["correct_word"],
            current_word.word,
        )


    # =====================================================
    # TEST 3
    #
    # ONE INITIAL ERROR
    # -> DECK 2
    # =====================================================

    def test_initial_error_routes_word_to_deck2(
        self,
    ):

        response, data = (
            self.get_state()
        )

        first_word_id = (
            data["state"]
            ["question"]
            ["word_id"]
        )

        failed_word_id = (
            first_word_id
        )


        # Первый ответ специально неправильный.

        response, data = (
            self.post_answer(
                word_id=first_word_id,
                answer=(
                    "definitely-not-"
                    "the-correct-word"
                ),
            )
        )

        self.assertFalse(
            data["answer"]["is_correct"]
        )


        # Остальные слова Initial Listening
        # отвечаем правильно.

        while (
            data["state"]["phase"]
            ==
            UnifiedGroupPracticeSession
            .Phase
            .LISTENING_INITIAL
        ):

            question = (
                data["state"]["question"]
            )

            word = (
                VocabularyWord.objects
                .get(
                    id=question["word_id"]
                )
            )

            response, data = (
                self.post_answer(
                    word_id=word.id,
                    answer=word.word,
                )
            )


        self.assertEqual(
            data["state"]["phase"],
            (
                UnifiedGroupPracticeSession
                .Phase
                .LETTER_FIRST
            ),
        )

        self.assertEqual(
            data["state"]["deck2_count"],
            1,
        )

        self.assertEqual(
            data["state"]["deck3_count"],
            1,
        )

        self.assertEqual(
            data["state"]["question"]["deck"],
            2,
        )

        self.assertEqual(
            data["state"]["question"]["word_id"],
            failed_word_id,
        )

        self.assertEqual(
            data["state"]["mistake_count"],
            1,
        )


    # =====================================================
    # TEST 4
    #
    # PERFECT INITIAL LISTENING
    # -> COMPLETED
    # =====================================================

    def test_perfect_initial_round_completes_practice(
        self,
    ):

        response, data = (
            self.get_state()
        )


        while not data["state"]["is_completed"]:

            question = (
                data["state"]["question"]
            )

            word = (
                VocabularyWord.objects
                .get(
                    id=question["word_id"]
                )
            )

            response, data = (
                self.post_answer(
                    word_id=word.id,
                    answer=word.word,
                )
            )


        self.assertTrue(
            data["state"]["is_completed"]
        )

        self.assertEqual(
            data["state"]["phase"],
            (
                UnifiedGroupPracticeSession
                .Phase
                .COMPLETED
            ),
        )

        self.assertIsNone(
            data["state"]["question"]
        )

        self.assertEqual(
            data["state"]["deck1_count"],
            0,
        )


    # =====================================================
    # TEST 5
    # STALE / WRONG WORD ID
    # =====================================================

    def test_answer_rejects_non_current_word(
        self,
    ):

        response, data = (
            self.get_state()
        )

        current_word_id = (
            data["state"]
            ["question"]
            ["word_id"]
        )

        wrong_word = next(
            word
            for word in self.words
            if (
                word.id
                !=
                current_word_id
            )
        )

        response, data = (
            self.post_answer(
                word_id=wrong_word.id,
                answer=wrong_word.word,
            )
        )

        self.assertEqual(
            response.status_code,
            409,
        )

        self.assertFalse(
            data["success"]
        )

        self.assertEqual(
            data["error"],
            (
                "This is not "
                "the current word."
            ),
        )


    # =====================================================
    # TEST 6
    # RESTART
    # =====================================================

    def test_restart_resets_unified_practice(
        self,
    ):

        response, data = (
            self.get_state()
        )

        word_id = (
            data["state"]
            ["question"]
            ["word_id"]
        )

        # Создаём ошибку.

        response, data = (
            self.post_answer(
                word_id=word_id,
                answer="wrong-answer",
            )
        )


        response, data = (
            self.post_restart()
        )


        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTrue(
            data["success"]
        )

        self.assertEqual(
            data["state"]["phase"],
            (
                UnifiedGroupPracticeSession
                .Phase
                .LISTENING_INITIAL
            ),
        )

        self.assertFalse(
            data["state"]["is_completed"]
        )

        self.assertEqual(
            data["state"]["mistake_count"],
            0,
        )

        self.assertEqual(
            data["state"]["deck1_count"],
            4,
        )

        self.assertEqual(
            data["state"]["deck2_count"],
            0,
        )

        self.assertEqual(
            data["state"]["deck3_count"],
            0,
        )

        self.assertEqual(
            data["state"]["deck4_count"],
            0,
        )

        self.assertEqual(
            data["state"]["deck5_count"],
            0,
        )

        self.assertEqual(
            data["state"]["question"]["deck"],
            1,
        )