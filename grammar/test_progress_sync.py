from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from grammar.models import (
    GrammarBlock,
    GrammarExercise,
    GrammarLesson,
    GrammarStudyPlan,
    GrammarStudyPlanItem,
    GrammarTopicAssessment,
)


class GrammarLessonKnowledgeSyncTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        User = get_user_model()

        cls.user = User.objects.create_user(
            username="grammar-sync-user",
            password="test-password",
        )

        cls.block = GrammarBlock.objects.create(
            level="A1",
            title="Sync Block",
            slug="sync-block",
            order=1,
            description="Test",
            is_published=True,
        )

        cls.lesson = GrammarLesson.objects.create(
            block=cls.block,
            level="A1",
            order=1,
            title="Sync Lesson",
            slug="sync-lesson",
            theory_text="Theory",
            estimated_minutes=10,
            pass_score=70,
            xp_reward=100,
            is_published=True,
        )

        cls.exercise = GrammarExercise.objects.create(
            lesson=cls.lesson,
            order=1,
            exercise_type=(
                GrammarExercise.Type.CHOICE
            ),
            prompt="Choose A.",
            options=[
                "A",
                "B",
                "C",
                "D",
            ],
            correct_answer="A",
            explanation="A is correct.",
            is_published=True,
        )

        GrammarTopicAssessment.objects.create(
            user=cls.user,
            lesson=cls.lesson,
            status=(
                GrammarTopicAssessment
                .Status
                .LEARN
            ),
            source=(
                GrammarTopicAssessment
                .Source
                .PLACEMENT_TOPIC
            ),
            correct_answers=0,
            total_questions=2,
        )

        plan = GrammarStudyPlan.objects.create(
            user=cls.user,
            start_date=timezone.localdate(),
            exam_date=(
                timezone.localdate()
                + timedelta(days=20)
            ),
            status=(
                GrammarStudyPlan
                .Status
                .ACTIVE
            ),
        )

        GrammarStudyPlanItem.objects.create(
            plan=plan,
            lesson=cls.lesson,
            scheduled_date=timezone.localdate(),
            action=(
                GrammarStudyPlanItem
                .Action
                .LEARN
            ),
            order=1,
        )

    def test_passed_lesson_becomes_mastered(self):

        self.client.force_login(
            self.user
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
                f"answer_{self.exercise.id}":
                    "A",
            },
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        assessment = (
            GrammarTopicAssessment.objects
            .get(
                user=self.user,
                lesson=self.lesson,
            )
        )

        self.assertEqual(
            assessment.status,
            GrammarTopicAssessment
            .Status
            .MASTERED,
        )

        self.assertEqual(
            assessment.source,
            GrammarTopicAssessment
            .Source
            .LESSON,
        )

        self.assertTrue(
            GrammarStudyPlanItem.objects
            .filter(
                plan__user=self.user,
                lesson=self.lesson,
                action__in=[
                    GrammarStudyPlanItem
                    .Action
                    .LEARN,

                    GrammarStudyPlanItem
                    .Action
                    .REVIEW,
                ],
            )
            .exists()
        )
