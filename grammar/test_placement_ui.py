from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from grammar.models import (
    GrammarPlacementAttempt,
)


class GrammarPlacementUITests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()

        cls.user = User.objects.create_user(
            username="placement-ui-user",
            password="test-password",
        )

    def setUp(self):
        self.client.force_login(
            self.user
        )

    def test_placement_route_is_not_lesson_slug(self):
        url = reverse(
            "grammar:placement"
        )

        match = resolve(url)

        self.assertEqual(
            match.url_name,
            "placement",
        )

    def test_first_grammar_visit_shows_placement_gate(self):
        response = self.client.get(
            reverse(
                "grammar:home"
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Определим ваши знания грамматики",
        )

    def test_placement_intro_page(self):
        response = self.client.get(
            reverse(
                "grammar:placement"
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Начать диагностику",
        )

    def test_start_placement_creates_attempt(self):
        response = self.client.post(
            reverse(
                "grammar:placement_start"
            )
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertEqual(
            GrammarPlacementAttempt.objects
            .filter(
                user=self.user,
                status=(
                    GrammarPlacementAttempt
                    .Status
                    .IN_PROGRESS
                ),
            )
            .count(),
            1,
        )

    def test_result_without_completed_attempt_redirects(self):
        response = self.client.get(
            reverse(
                "grammar:placement_result"
            )
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertEqual(
            response.url,
            reverse(
                "grammar:placement"
            ),
        )
