from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from grammar.models import (
    GrammarBlock,
    GrammarLesson,
    GrammarPlacementAttempt,
    GrammarStudyPlan,
    GrammarStudyPlanItem,
    GrammarTopicAssessment,
)

from grammar.study_plan import (
    build_study_plan,
    get_plan_calendar,
)


class GrammarStudyPlanTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        User = get_user_model()

        cls.user = User.objects.create_user(
            username="daily-plan-user",
            password="test-password",
        )

        cls.block = GrammarBlock.objects.create(
            level="A1",
            title="Daily Plan Block",
            slug="daily-plan-block",
            order=1,
            description="Test",
            is_published=True,
        )

        cls.lessons = []

        for order in range(1, 5):

            lesson = GrammarLesson.objects.create(
                block=cls.block,
                level="A1",
                order=order,
                title=f"Plan Lesson {order}",
                slug=f"plan-lesson-{order}",
                theory_text="Theory",
                estimated_minutes=10,
                pass_score=70,
                xp_reward=100,
                is_published=True,
            )

            cls.lessons.append(
                lesson
            )

        statuses = [
            GrammarTopicAssessment.Status.LEARN,
            GrammarTopicAssessment.Status.LEARN,
            GrammarTopicAssessment.Status.REVIEW,
            GrammarTopicAssessment.Status.REVIEW,
        ]

        for lesson, status in zip(
            cls.lessons,
            statuses,
        ):

            GrammarTopicAssessment.objects.create(
                user=cls.user,
                lesson=lesson,
                status=status,
                source=(
                    GrammarTopicAssessment
                    .Source
                    .PLACEMENT_TOPIC
                ),
                correct_answers=0,
                total_questions=2,
            )

        GrammarPlacementAttempt.objects.create(
            user=cls.user,
            status=(
                GrammarPlacementAttempt
                .Status
                .COMPLETED
            ),
            stage=(
                GrammarPlacementAttempt
                .Stage
                .COMPLETE
            ),
            correct_answers=40,
            total_questions=40,
            completed_at=timezone.now(),
        )

    def test_build_20_day_plan(self):

        today = timezone.localdate()

        exam_date = (
            today
            + timedelta(days=20)
        )

        plan = build_study_plan(
            user=self.user,
            exam_date=exam_date,
            start_date=today,
        )

        self.assertEqual(
            plan.status,
            GrammarStudyPlan.Status.ACTIVE,
        )

        self.assertEqual(
            plan.exam_date,
            exam_date,
        )

        calendar = get_plan_calendar(
            plan
        )

        self.assertEqual(
            len(calendar),
            20,
        )

        self.assertEqual(
            calendar[0]["date"],
            today,
        )

        self.assertEqual(
            calendar[-1]["date"],
            exam_date
            - timedelta(days=1),
        )

        self.assertEqual(
            plan.items.filter(
                action=(
                    GrammarStudyPlanItem
                    .Action
                    .LEARN
                ),
            ).count(),
            2,
        )

        self.assertEqual(
            plan.items.filter(
                action=(
                    GrammarStudyPlanItem
                    .Action
                    .REVIEW
                ),
            ).count(),
            2,
        )

        self.assertGreater(
            plan.items.filter(
                action=(
                    GrammarStudyPlanItem
                    .Action
                    .FINAL_REVIEW
                ),
            ).count(),
            0,
        )

    def test_rebuild_archives_old_plan(self):

        today = timezone.localdate()

        old_plan = build_study_plan(
            user=self.user,
            exam_date=(
                today
                + timedelta(days=20)
            ),
            start_date=today,
        )

        new_plan = build_study_plan(
            user=self.user,
            exam_date=(
                today
                + timedelta(days=15)
            ),
            start_date=today,
        )

        old_plan.refresh_from_db()

        self.assertEqual(
            old_plan.status,
            GrammarStudyPlan.Status.ARCHIVED,
        )

        self.assertEqual(
            new_plan.status,
            GrammarStudyPlan.Status.ACTIVE,
        )

    def test_plan_setup_view_creates_plan(self):

        self.client.force_login(
            self.user
        )

        exam_date = (
            timezone.localdate()
            + timedelta(days=20)
        )

        response = self.client.post(
            reverse(
                "grammar:plan_setup"
            ),
            {
                "exam_date":
                    exam_date.isoformat(),
            },
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertEqual(
            response.url,
            reverse(
                "grammar:plan"
            ),
        )

        self.assertTrue(
            GrammarStudyPlan.objects
            .filter(
                user=self.user,
                status=(
                    GrammarStudyPlan
                    .Status
                    .ACTIVE
                ),
            )
            .exists()
        )
