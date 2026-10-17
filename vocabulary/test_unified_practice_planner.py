from types import SimpleNamespace

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import (
    DailyStudyPlanItem,
    LessonPracticeProgress,
    UnifiedGroupPracticeSession,
    VocabularyGroup,
    VocabularyLesson,
    VocabularyLevel,
)

from .planner import (
    build_full_level_sequence,
    build_remaining_sequence,
)

from .views import (
    get_daily_item_url,
)


User = get_user_model()


class UnifiedPracticePlannerTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="planner_test_user",
            password="test-password-123",
        )


        self.level = VocabularyLevel.objects.create(
            code="A1",
            name="A1 Test",
            order=1,
            is_active=True,
        )


        # =================================================
        # GROUP 1
        # =================================================

        self.group1 = VocabularyGroup.objects.create(
            level=self.level,
            code="group-1",
            name="Group 1",
            order=1,
        )


        self.lesson1 = VocabularyLesson.objects.create(
            group=self.group1,
            number=1,
            global_number=1,
            title="Lesson 1",
            order=1,
            is_active=True,
        )


        self.lesson2 = VocabularyLesson.objects.create(
            group=self.group1,
            number=2,
            global_number=2,
            title="Lesson 2",
            order=2,
            is_active=True,
        )


        # =================================================
        # GROUP 2
        # =================================================

        self.group2 = VocabularyGroup.objects.create(
            level=self.level,
            code="group-2",
            name="Group 2",
            order=2,
        )


        self.lesson3 = VocabularyLesson.objects.create(
            group=self.group2,
            number=1,
            global_number=3,
            title="Lesson 1",
            order=1,
            is_active=True,
        )


        # Для planner нам достаточно объекта,
        # у которого есть user и level.
        #
        # build_remaining_sequence()
        # не требует сохранённого UserCourse.

        self.course = SimpleNamespace(
            user=self.user,
            level=self.level,
        )


    # =====================================================
    # FULL LEVEL SEQUENCE
    # =====================================================

    def test_full_sequence_has_one_unified_practice_per_group(
        self,
    ):

        sequence = build_full_level_sequence(
            self.level
        )


        # Group 1:
        # Lesson 1
        # Lesson 2
        # Unified Practice
        #
        # Group 2:
        # Lesson 1
        # Unified Practice

        self.assertEqual(
            len(sequence),
            5,
        )


        self.assertEqual(
            [
                item["type"]
                for item
                in sequence
            ],
            [
                "lesson",
                "lesson",
                "group_practice",
                "lesson",
                "group_practice",
            ],
        )


        practice_items = [
            item

            for item
            in sequence

            if (
                item["type"]
                ==
                "group_practice"
            )
        ]


        # Ровно по одному Unified Practice
        # на каждую группу.

        self.assertEqual(
            len(practice_items),
            2,
        )


        self.assertEqual(
            practice_items[0]["group"],
            self.group1,
        )


        self.assertEqual(
            practice_items[1]["group"],
            self.group2,
        )


        # practice_number остаётся только
        # как compatibility value.
        #
        # Старых Practice 1–4 больше нет.

        self.assertEqual(
            practice_items[0]["practice_number"],
            1,
        )


        self.assertEqual(
            practice_items[1]["practice_number"],
            1,
        )


    # =====================================================
    # ORDER INSIDE GROUP
    # =====================================================

    def test_unified_practice_is_after_all_group_lessons(
        self,
    ):

        sequence = build_full_level_sequence(
            self.level
        )


        group1_items = [
            item

            for item
            in sequence

            if (
                item["group"]
                ==
                self.group1
            )
        ]


        self.assertEqual(
            [
                item["type"]
                for item
                in group1_items
            ],
            [
                "lesson",
                "lesson",
                "group_practice",
            ],
        )


        self.assertEqual(
            group1_items[0]["lesson"],
            self.lesson1,
        )


        self.assertEqual(
            group1_items[1]["lesson"],
            self.lesson2,
        )


    # =====================================================
    # REMAINING SEQUENCE
    # NOTHING COMPLETED
    # =====================================================

    def test_remaining_sequence_contains_lessons_then_unified_practice(
        self,
    ):

        sequence = build_remaining_sequence(
            self.course
        )


        self.assertEqual(
            [
                item["type"]
                for item
                in sequence
            ],
            [
                "lesson",
                "lesson",
                "group_practice",
                "lesson",
                "group_practice",
            ],
        )


        self.assertEqual(
            sequence[0]["lesson"],
            self.lesson1,
        )


        self.assertEqual(
            sequence[1]["lesson"],
            self.lesson2,
        )


        self.assertEqual(
            sequence[2]["group"],
            self.group1,
        )


    # =====================================================
    # COMPLETED LESSON
    # =====================================================

    def test_completed_lesson_is_removed_but_unified_practice_remains(
        self,
    ):

        LessonPracticeProgress.objects.create(
            user=self.user,
            lesson=self.lesson1,
            stage1_completed=True,
            stage2_completed=True,
            stage3_completed=True,
            stage4_completed=True,
        )


        sequence = build_remaining_sequence(
            self.course
        )


        group1_items = [
            item

            for item
            in sequence

            if (
                item["group"]
                ==
                self.group1
            )
        ]


        # Lesson 1 завершён.
        #
        # Остались:
        # Lesson 2
        # Unified Practice

        self.assertEqual(
            len(group1_items),
            2,
        )


        self.assertEqual(
            group1_items[0]["type"],
            "lesson",
        )


        self.assertEqual(
            group1_items[0]["lesson"],
            self.lesson2,
        )


        self.assertEqual(
            group1_items[1]["type"],
            "group_practice",
        )


    # =====================================================
    # ALL LESSONS COMPLETED
    # =====================================================

    def test_after_all_lessons_only_unified_practice_remains(
        self,
    ):

        for lesson in [
            self.lesson1,
            self.lesson2,
        ]:

            LessonPracticeProgress.objects.create(
                user=self.user,
                lesson=lesson,
                stage1_completed=True,
                stage2_completed=True,
                stage3_completed=True,
                stage4_completed=True,
            )


        sequence = build_remaining_sequence(
            self.course
        )


        group1_items = [
            item

            for item
            in sequence

            if (
                item["group"]
                ==
                self.group1
            )
        ]


        self.assertEqual(
            len(group1_items),
            1,
        )


        self.assertEqual(
            group1_items[0]["type"],
            "group_practice",
        )


        self.assertEqual(
            group1_items[0]["practice_number"],
            1,
        )


    # =====================================================
    # UNIFIED PRACTICE COMPLETED
    # =====================================================

    def test_completed_group_disappears_from_remaining_sequence(
        self,
    ):

        # Завершаем оба Lessons первой группы.

        for lesson in [
            self.lesson1,
            self.lesson2,
        ]:

            LessonPracticeProgress.objects.create(
                user=self.user,
                lesson=lesson,
                stage1_completed=True,
                stage2_completed=True,
                stage3_completed=True,
                stage4_completed=True,
            )


        # Завершаем Unified Practice.

        UnifiedGroupPracticeSession.objects.create(
            user=self.user,
            group=self.group1,
            phase=(
                UnifiedGroupPracticeSession
                .Phase
                .COMPLETED
            ),
            is_completed=True,
        )


        sequence = build_remaining_sequence(
            self.course
        )


        # После полного завершения Group 1
        # следующий элемент уже относится
        # к Group 2.

        self.assertGreater(
            len(sequence),
            0,
        )


        self.assertEqual(
            sequence[0]["group"],
            self.group2,
        )


        self.assertEqual(
            sequence[0]["type"],
            "lesson",
        )


        # Group 1 вообще больше
        # не должна находиться в remaining.

        self.assertFalse(
            any(
                item["group"]
                ==
                self.group1

                for item
                in sequence
            )
        )


    # =====================================================
    # DAILY PLAN URL
    # =====================================================

    def test_group_practice_url_always_opens_unified_practice(
        self,
    ):

        # Даже если старый DailyStudyPlanItem
        # исторически имел practice_number=4,
        # ссылка теперь должна вести
        # только в Unified Practice.

        item = SimpleNamespace(
            item_type=(
                DailyStudyPlanItem
                .Type
                .GROUP_PRACTICE
            ),
            lesson=None,
            group=self.group1,
            practice_number=4,
        )


        url = get_daily_item_url(
            item
        )


        expected_url = reverse(
            "vocabulary:unified_group_practice",
            kwargs={
                "level_code":
                    self.level.code,

                "group_id":
                    self.group1.id,
            },
        )


        self.assertEqual(
            url,
            expected_url,
        )
