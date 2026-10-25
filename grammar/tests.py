from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import (
    GrammarLesson,
    GrammarLessonProgress,
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
                is_published=True,
            )
        )

    def test_grammar_home(self):

        self.client.login(
            username="grammar_test_user",
            password="test-password-123",
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
            "Articles A and AN",
        )

    def test_open_lesson_creates_progress(self):

        self.client.login(
            username="grammar_test_user",
            password="test-password-123",
        )

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

    def test_complete_lesson(self):

        self.client.login(
            username="grammar_test_user",
            password="test-password-123",
        )

        self.client.post(
            reverse(
                "grammar:complete",
                kwargs={
                    "slug": self.lesson.slug,
                },
            ),
            {
                "score": 90,
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
            GrammarLessonProgress.Status.COMPLETED,
        )

        self.assertEqual(
            progress.score,
            90,
        )
