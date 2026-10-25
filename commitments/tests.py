from datetime import timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from vocabulary.models import (
    UserCourse,
    VocabularyGroup,
    VocabularyLesson,
    VocabularyLevel,
)

from commitments.models import (
    CommitmentLedgerEntry,
    CommitmentMilestone,
    CommitmentPlan,
)
from commitments.services import (
    activate_commitment,
    award_completed_lesson,
    award_completed_unified_practice,
    create_commitment_draft,
)


User = get_user_model()


class CommitmentRewardTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.level = VocabularyLevel.objects.create(
            code="TEST",
            name="Test Level",
        )

        self.group = VocabularyGroup.objects.create(
            level=self.level,
            name="Test Group",
            order=1,
        )


        self.lesson = VocabularyLesson.objects.create(
            group=self.group,
            number=1,
            title="Lesson 1",
            order=1,
            is_active=True,
        )


        self.user_course = UserCourse.objects.create(
            user=self.user,
            level=self.level,
            duration_days=60,
        )

        self.plan = CommitmentPlan.objects.create(
            name="Test Commitment",
            level=self.level,
            duration_days=60,

            tuition_amount=Decimal("10000.00"),

            # В тестовом курсе:
            # 1 lesson × 100
            # 1 unified × 500
            refundable_amount=Decimal("600.00"),

            lesson_reward=Decimal("100.00"),
            unified_practice_reward=Decimal("500.00"),

            withdrawal_threshold=Decimal("500.00"),

            pause_days=3,
            late_grace_hours=72,
            late_reward_percent=50,

            terms_version="1.0",
            is_active=True,
        )

        self.commitment = create_commitment_draft(
            user_course=self.user_course,
            plan=self.plan,
            goal_text="Выучить английский",
            motivation_text="Для работы",
        )

        self.start_at = timezone.now()

        self.commitment = activate_commitment(
            commitment=self.commitment,
            signed_name="Test User",
            declaration_snapshot="Test declaration",
            start_at=self.start_at,
        )

    def test_activation_creates_milestones(self):
        milestones = self.commitment.milestones.all()

        self.assertEqual(
            milestones.count(),
            2,
        )

        lesson_count = milestones.filter(
            kind=CommitmentMilestone.Kind.LESSON
        ).count()

        practice_count = milestones.filter(
            kind=CommitmentMilestone.Kind.UNIFIED_PRACTICE
        ).count()

        self.assertEqual(lesson_count, 1)
        self.assertEqual(practice_count, 1)

    def test_lesson_reward_is_100(self):
        result = award_completed_lesson(
            user=self.user,
            lesson=self.lesson,
            completed_at=self.start_at + timedelta(hours=1),
        )

        self.assertTrue(result["awarded"])

        self.assertEqual(
            result["amount"],
            Decimal("100.00"),
        )

        self.commitment.refresh_from_db()

        self.assertEqual(
            self.commitment.earned_total,
            Decimal("100.00"),
        )

    def test_unified_practice_reward_is_500(self):
        result = award_completed_unified_practice(
            user=self.user,
            group=self.group,
            completed_at=self.start_at + timedelta(hours=1),
        )

        self.assertTrue(result["awarded"])

        self.assertEqual(
            result["amount"],
            Decimal("500.00"),
        )

        self.commitment.refresh_from_db()

        self.assertEqual(
            self.commitment.earned_total,
            Decimal("500.00"),
        )

    def test_lesson_cannot_be_rewarded_twice(self):
        first = award_completed_lesson(
            user=self.user,
            lesson=self.lesson,
            completed_at=self.start_at + timedelta(hours=1),
        )

        second = award_completed_lesson(
            user=self.user,
            lesson=self.lesson,
            completed_at=self.start_at + timedelta(hours=2),
        )

        self.assertTrue(first["awarded"])

        self.assertFalse(second["awarded"])

        self.assertEqual(
            second["reason"],
            "already_processed",
        )

        self.assertEqual(
            CommitmentLedgerEntry.objects.count(),
            1,
        )

        self.assertEqual(
            self.commitment.earned_total,
            Decimal("100.00"),
        )

    def test_late_reward_is_full(self):
        milestone = self.commitment.milestones.get(
            kind=CommitmentMilestone.Kind.LESSON,
        )

        completed_at = (
            milestone.checkpoint.due_at
            + timedelta(hours=24)
        )

        result = award_completed_lesson(
            user=self.user,
            lesson=self.lesson,
            completed_at=completed_at,
        )

        self.assertTrue(result["awarded"])

        self.assertEqual(
            result["amount"],
            Decimal("100.00"),
        )

        milestone.refresh_from_db()

        self.assertEqual(
            milestone.status,
            CommitmentMilestone.Status.EARNED,
        )

    def test_after_grace_period_reward_is_full(self):
        milestone = self.commitment.milestones.get(
            kind=CommitmentMilestone.Kind.LESSON,
        )

        completed_at = (
            milestone.checkpoint.grace_until
            + timedelta(hours=1)
        )

        result = award_completed_lesson(
            user=self.user,
            lesson=self.lesson,
            completed_at=completed_at,
        )

        self.assertFalse(result["awarded"])

        self.assertEqual(
            result["amount"],
            Decimal("100.00"),
        )

        milestone.refresh_from_db()

        self.assertEqual(
            milestone.status,
            CommitmentMilestone.Status.EARNED,
        )

        self.assertEqual(
            CommitmentLedgerEntry.objects.count(),
            0,
        )

    def test_full_test_course_returns_exactly_600(self):
        award_completed_lesson(
            user=self.user,
            lesson=self.lesson,
            completed_at=self.start_at + timedelta(hours=1),
        )

        award_completed_unified_practice(
            user=self.user,
            group=self.group,
            completed_at=self.start_at + timedelta(hours=2),
        )

        self.assertEqual(
            self.commitment.earned_total,
            Decimal("600.00"),
        )

        self.assertEqual(
            CommitmentLedgerEntry.objects.count(),
            2,
        )