from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from grammar.exam_practice import (
    build_exam_question_ids,
)

from grammar.models import (
    GrammarBlock,
    GrammarExercise,
    GrammarLesson,
    GrammarTopicAssessment,
)


class GrammarExamPracticeTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        User = get_user_model()

        cls.user = User.objects.create_user(
            username="mixed-exam-user",
            password="test-password",
        )

        block = GrammarBlock.objects.create(
            level="A1",
            title="Exam Block",
            slug="exam-block",
            order=1,
            description="Test",
            is_published=True,
        )

        for lesson_order in range(
            1,
            21,
        ):

            lesson = GrammarLesson.objects.create(
                block=block,
                level="A1",
                order=lesson_order,
                title=(
                    f"Exam Lesson "
                    f"{lesson_order}"
                ),
                slug=(
                    f"exam-lesson-"
                    f"{lesson_order}"
                ),
                theory_text="Theory",
                estimated_minutes=10,
                pass_score=70,
                xp_reward=100,
                is_published=True,
            )

            for question_order in range(
                1,
                3,
            ):

                GrammarExercise.objects.create(
                    lesson=lesson,
                    order=question_order,
                    exercise_type=(
                        GrammarExercise
                        .Type
                        .CHOICE
                    ),
                    prompt=(
                        f"Question "
                        f"{lesson_order}-"
                        f"{question_order}"
                    ),
                    options=[
                        "A",
                        "B",
                        "C",
                        "D",
                    ],
                    correct_answer="A",
                    explanation="Test",
                    is_published=True,
                )

            status = (
                GrammarTopicAssessment
                .Status
                .LEARN
                if lesson_order <= 10
                else
                GrammarTopicAssessment
                .Status
                .MASTERED
            )

            GrammarTopicAssessment.objects.create(
                user=cls.user,
                lesson=lesson,
                status=status,
                source=(
                    GrammarTopicAssessment
                    .Source
                    .PLACEMENT_TOPIC
                ),
            )

    def test_builds_20_unique_questions(self):

        ids = build_exam_question_ids(
            self.user,
            count=20,
        )

        self.assertEqual(
            len(ids),
            20,
        )

        self.assertEqual(
            len(set(ids)),
            20,
        )

    def test_exam_intro(self):

        self.client.force_login(
            self.user
        )

        response = self.client.get(
            reverse(
                "grammar:exam_practice"
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "20 смешанных вопросов",
        )

    def test_start_creates_exam_session(self):

        self.client.force_login(
            self.user
        )

        response = self.client.post(
            reverse(
                "grammar:exam_practice_start"
            )
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        state = (
            self.client.session.get(
                "grammar_mixed_exam_practice"
            )
        )

        self.assertIsNotNone(
            state
        )

        self.assertEqual(
            len(
                state[
                    "question_ids"
                ]
            ),
            20,
        )
