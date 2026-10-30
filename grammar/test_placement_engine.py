from django.contrib.auth import get_user_model
from django.test import TestCase

from grammar.models import (
    GrammarAssessmentQuestion,
    GrammarBlock,
    GrammarExercise,
    GrammarLesson,
    GrammarPlacementAttempt,
    GrammarTopicAssessment,
)
from grammar.placement import (
    get_knowledge_summary,
    get_personal_plan,
    get_screening_questions,
    record_answer,
    start_placement,
)


class GrammarPlacementEngineTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()

        cls.user = User.objects.create_user(
            username="placement-test-user",
            password="test-password",
        )

        lesson_order = 1

        for block_order in range(1, 11):
            block = GrammarBlock.objects.create(
                level="A1",
                title=f"Block {block_order}",
                slug=f"block-{block_order}",
                order=block_order,
                description="Test block",
                is_published=True,
            )

            block_lessons = []

            for _ in range(6):
                lesson = GrammarLesson.objects.create(
                    level="A1",
                    order=lesson_order,
                    title=f"Lesson {lesson_order}",
                    slug=f"lesson-{lesson_order}",
                    block=block,
                    theory_text="Test theory",
                    estimated_minutes=10,
                    pass_score=70,
                    xp_reward=100,
                    is_published=True,
                )

                block_lessons.append(lesson)

                exercises = []

                for question_order in range(1, 5):
                    exercise = GrammarExercise.objects.create(
                        lesson=lesson,
                        order=question_order,
                        exercise_type=GrammarExercise.Type.CHOICE,
                        prompt=(
                            f"Lesson {lesson_order} "
                            f"question {question_order}"
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

                    exercises.append(exercise)

                # Two topic diagnostic questions.
                for priority, exercise in enumerate(
                    exercises[:2],
                    start=1,
                ):
                    GrammarAssessmentQuestion.objects.create(
                        exercise=exercise,
                        role=(
                            GrammarAssessmentQuestion.Role.TOPIC
                        ),
                        priority=priority,
                        is_active=True,
                    )

                # Two checkpoint candidates.
                for priority, exercise in enumerate(
                    exercises[2:],
                    start=1,
                ):
                    GrammarAssessmentQuestion.objects.create(
                        exercise=exercise,
                        role=(
                            GrammarAssessmentQuestion.Role.CHECKPOINT
                        ),
                        priority=priority,
                        is_active=True,
                    )

                lesson_order += 1

            # Four screening questions from four
            # different lessons in the block.
            for priority, lesson in enumerate(
                block_lessons[:4],
                start=1,
            ):
                exercise = lesson.exercises.get(
                    order=3,
                )

                GrammarAssessmentQuestion.objects.create(
                    exercise=exercise,
                    role=(
                        GrammarAssessmentQuestion.Role.SCREENING
                    ),
                    priority=priority,
                    is_active=True,
                )

    def test_adaptive_placement_flow(self):
        attempt = start_placement(self.user)

        self.assertEqual(
            attempt.stage,
            GrammarPlacementAttempt.Stage.SCREENING,
        )

        screening = list(
            get_screening_questions()
        )

        self.assertEqual(
            len(screening),
            40,
        )

        questions_by_block = {}

        for question in screening:
            block_order = (
                question.exercise.lesson.block.order
            )

            questions_by_block.setdefault(
                block_order,
                [],
            ).append(question)

        # Desired block results:
        #
        # Block 1 -> 4/4
        # Block 2 -> 3/4
        # Block 3 -> 2/4
        # Block 4 -> 1/4
        # Blocks 5-10 -> 4/4
        target_correct = {
            1: 4,
            2: 3,
            3: 2,
            4: 1,
            5: 4,
            6: 4,
            7: 4,
            8: 4,
            9: 4,
            10: 4,
        }

        for block_order in range(1, 11):
            questions = questions_by_block[
                block_order
            ]

            correct_limit = target_correct[
                block_order
            ]

            for index, question in enumerate(
                questions
            ):
                selected_answer = (
                    "A"
                    if index < correct_limit
                    else "B"
                )

                record_answer(
                    attempt=attempt,
                    assessment_question=question,
                    selected_answer=selected_answer,
                )

        attempt.refresh_from_db()

        self.assertEqual(
            attempt.stage,
            GrammarPlacementAttempt.Stage.TOPIC,
        )

        summary = get_knowledge_summary(
            self.user
        )

        self.assertEqual(
            summary[
                GrammarTopicAssessment.Status
                .PROVISIONAL_MASTERED
            ],
            47,
        )

        self.assertEqual(
            summary[
                GrammarTopicAssessment.Status.UNKNOWN
            ],
            7,
        )

        self.assertEqual(
            summary[
                GrammarTopicAssessment.Status.LEARN
            ],
            6,
        )

        unknown_topics = list(
            GrammarTopicAssessment.objects
            .filter(
                user=self.user,
                status=GrammarTopicAssessment.Status.UNKNOWN,
            )
            .select_related("lesson")
            .order_by("lesson__order")
        )

        self.assertEqual(
            len(unknown_topics),
            7,
        )

        # Topic 1:
        # 1/2 -> REVIEW
        #
        # Topic 2:
        # 0/2 -> LEARN
        #
        # Other 5:
        # 2/2 -> MASTERED

        for topic_index, topic in enumerate(
            unknown_topics
        ):
            questions = list(
                GrammarAssessmentQuestion.objects
                .filter(
                    role=GrammarAssessmentQuestion.Role.TOPIC,
                    exercise__lesson=topic.lesson,
                    is_active=True,
                )
                .order_by(
                    "priority",
                    "pk",
                )
            )

            self.assertEqual(
                len(questions),
                2,
            )

            if topic_index == 0:
                selected_answers = [
                    "A",
                    "B",
                ]

            elif topic_index == 1:
                selected_answers = [
                    "B",
                    "B",
                ]

            else:
                selected_answers = [
                    "A",
                    "A",
                ]

            for question, selected_answer in zip(
                questions,
                selected_answers,
            ):
                record_answer(
                    attempt=attempt,
                    assessment_question=question,
                    selected_answer=selected_answer,
                )

        attempt.refresh_from_db()

        self.assertEqual(
            attempt.status,
            GrammarPlacementAttempt.Status.COMPLETED,
        )

        self.assertEqual(
            attempt.stage,
            GrammarPlacementAttempt.Stage.COMPLETE,
        )

        self.assertEqual(
            attempt.total_questions,
            54,
        )

        final_summary = get_knowledge_summary(
            self.user
        )

        self.assertEqual(
            final_summary[
                GrammarTopicAssessment.Status
                .PROVISIONAL_MASTERED
            ],
            47,
        )

        self.assertEqual(
            final_summary[
                GrammarTopicAssessment.Status.REVIEW
            ],
            1,
        )

        self.assertEqual(
            final_summary[
                GrammarTopicAssessment.Status.LEARN
            ],
            7,
        )

        self.assertEqual(
            final_summary[
                GrammarTopicAssessment.Status.MASTERED
            ],
            5,
        )

        self.assertEqual(
            final_summary[
                GrammarTopicAssessment.Status.UNKNOWN
            ],
            0,
        )

        plan = list(
            get_personal_plan(
                self.user
            )
        )

        self.assertEqual(
            len(plan),
            8,
        )

    def test_new_attempt_abandons_old_attempt(self):
        old_attempt = start_placement(
            self.user
        )

        new_attempt = start_placement(
            self.user
        )

        old_attempt.refresh_from_db()

        self.assertEqual(
            old_attempt.status,
            GrammarPlacementAttempt.Status.ABANDONED,
        )

        self.assertEqual(
            new_attempt.status,
            GrammarPlacementAttempt.Status.IN_PROGRESS,
        )
