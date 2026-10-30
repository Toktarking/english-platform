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
                prompt="This is ___ book.",
                options=[
                    "a",
                    "an",
                ],
                correct_answer="a",
                explanation=(
                    "Book begins with "
                    "a consonant sound."
                ),
            )
        )

        self.exercise2 = (
            GrammarExercise.objects.create(
                lesson=self.lesson,
                section=self.section,
                order=2,
                prompt="This is ___ apple.",
                options=[
                    "a",
                    "an",
                ],
                correct_answer="an",
                explanation=(
                    "Apple begins with "
                    "a vowel sound."
                ),
            )
        )

    def login(self):

        return self.client.login(
            username="grammar_test_user",
            password="test-password-123",
        )

    def test_home(self):
        self.client.force_login(
            self.user
        )

        response = self.client.get(
            reverse("grammar:home")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Определим ваши знания грамматики",
        )

    def test_open_lesson_creates_progress(
        self
    ):

        self.login()

        response = self.client.get(
            reverse(
                "grammar:lesson",
                kwargs={
                    "slug":
                        self.lesson.slug,
                },
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        progress = (
            GrammarLessonProgress.objects
            .get(
                user=self.user,
                lesson=self.lesson,
            )
        )

        self.assertEqual(
            progress.status,
            GrammarLessonProgress
            .Status
            .IN_PROGRESS,
        )

    def test_pass_completes_and_awards_xp(
        self
    ):

        self.login()

        response = self.client.post(
            reverse(
                "grammar:complete",
                kwargs={
                    "slug":
                        self.lesson.slug,
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
            GrammarLessonProgress.objects
            .get(
                user=self.user,
                lesson=self.lesson,
            )
        )

        self.assertEqual(
            progress.status,
            GrammarLessonProgress
            .Status
            .COMPLETED,
        )

        self.assertEqual(
            progress.score,
            100,
        )

        self.assertEqual(
            progress.xp_earned,
            100,
        )

    def test_failed_attempt_shows_review(
        self
    ):

        self.login()

        response = self.client.post(
            reverse(
                "grammar:complete",
                kwargs={
                    "slug":
                        self.lesson.slug,
                },
            ),
            {
                f"answer_{self.exercise1.id}":
                    "a",

                f"answer_{self.exercise2.id}":
                    "a",
            },
            follow=True,
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Почти получилось",
        )

        self.assertContains(
            response,
            "Разбор ошибок",
        )

        self.assertContains(
            response,
            "Apple begins with",
        )

        progress = (
            GrammarLessonProgress.objects
            .get(
                user=self.user,
                lesson=self.lesson,
            )
        )

        self.assertEqual(
            progress.status,
            GrammarLessonProgress
            .Status
            .IN_PROGRESS,
        )

        self.assertEqual(
            progress.score,
            50,
        )

        self.assertEqual(
            progress.xp_earned,
            0,
        )

    def test_retry_can_start_at_practice(
        self
    ):

        self.login()

        response = self.client.get(
            reverse(
                "grammar:lesson",
                kwargs={
                    "slug":
                        self.lesson.slug,
                },
            )
            + "?practice=1"
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "startWithPractice",
        )


    def test_passed_attempt_still_shows_mistake_review(
        self
    ):

        self.login()

        # 1 из 2 = 50%.
        # Для этого теста делаем проходным 50%.
        self.lesson.pass_score = 50
        self.lesson.save(
            update_fields=[
                "pass_score",
            ]
        )

        response = self.client.post(
            reverse(
                "grammar:complete",
                kwargs={
                    "slug":
                        self.lesson.slug,
                },
            ),
            {
                f"answer_{self.exercise1.id}":
                    "a",

                f"answer_{self.exercise2.id}":
                    "a",
            },
            follow=True,
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        progress = (
            GrammarLessonProgress.objects
            .get(
                user=self.user,
                lesson=self.lesson,
            )
        )

        self.assertEqual(
            progress.status,
            GrammarLessonProgress
            .Status
            .COMPLETED,
        )

        self.assertEqual(
            progress.score,
            50,
        )

        self.assertEqual(
            progress.xp_earned,
            100,
        )

        self.assertContains(
            response,
            "Где были ошибки",
        )

        self.assertContains(
            response,
            "This is ___ apple.",
        )

        self.assertContains(
            response,
            "Apple begins with",
        )
