from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonProgress,
    GrammarLessonSection,
)


class GrammarLessonTests(TestCase):

    def setUp(self):

        User = get_user_model()

        self.user = User.objects.create_user(
            username="grammar_test_user",
            password="test-password-123",
        )

        self.lesson = (
            GrammarLesson.objects.create(
                title="Articles A and AN",
                slug="articles-a-an",
                level="A1",
                order=1,
                theory_text="Test theory",
                pass_score=70,
                xp_reward=100,
                is_published=True,
            )
        )

        self.section = (
            GrammarLessonSection.objects.create(
                lesson=self.lesson,
                order=1,
                title="A and AN",
                body="Test section",
            )
        )

        self.exercise1 = (
            GrammarExercise.objects.create(
                lesson=self.lesson,
                section=self.section,
                order=1,
                prompt="___ book",
                options=[
                    "a",
                    "an",
                ],
                correct_answer="a",
            )
        )

        self.exercise2 = (
            GrammarExercise.objects.create(
                lesson=self.lesson,
                section=self.section,
                order=2,
                prompt="___ apple",
                options=[
                    "a",
                    "an",
                ],
                correct_answer="an",
            )
        )

    def login(self):

        return self.client.login(
            username="grammar_test_user",
            password="test-password-123",
        )

    def test_grammar_home(self):

        self.login()

        response = self.client.get(
            reverse("grammar:home")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Articles A and AN",
        )

    def test_open_lesson_creates_progress(self):

        self.login()

        response = self.client.get(
            reverse(
                "grammar:lesson",
                kwargs={
                    "slug": self.lesson.slug,
                },
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        progress = (
            GrammarLessonProgress.objects.get(
                user=self.user,
                lesson=self.lesson,
            )
        )

        self.assertEqual(
            progress.status,
            GrammarLessonProgress.Status.IN_PROGRESS,
        )

    def test_correct_answers_complete_lesson_and_award_xp(
        self
    ):

        self.login()

        response = self.client.post(
            reverse(
                "grammar:complete",
                kwargs={
                    "slug": self.lesson.slug,
                },
            ),
            {
                f"answer_{self.exercise1.id}":
                    "a",

                f"answer_{self.exercise2.id}":
                    "an",
            },
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        progress = (
            GrammarLessonProgress.objects.get(
                user=self.user,
                lesson=self.lesson,
            )
        )

        self.assertEqual(
            progress.status,
            GrammarLessonProgress.Status.COMPLETED,
        )

        self.assertEqual(
            progress.score,
            100,
        )

        self.assertEqual(
            progress.xp_earned,
            100,
        )

    def test_failed_attempt_does_not_award_xp(
        self
    ):

        self.login()

        self.client.post(
            reverse(
                "grammar:complete",
                kwargs={
                    "slug": self.lesson.slug,
                },
            ),
            {
                f"answer_{self.exercise1.id}":
                    "a",

                f"answer_{self.exercise2.id}":
                    "a",
            },
        )

        progress = (
            GrammarLessonProgress.objects.get(
                user=self.user,
                lesson=self.lesson,
            )
        )

        self.assertEqual(
            progress.status,
            GrammarLessonProgress.Status.IN_PROGRESS,
        )

        self.assertEqual(
            progress.score,
            50,
        )

        self.assertEqual(
            progress.xp_earned,
            0,
        )
