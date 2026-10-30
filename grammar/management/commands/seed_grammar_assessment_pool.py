from django.core.management.base import (
    BaseCommand,
    CommandError,
)

from grammar.models import (
    GrammarAssessmentQuestion,
    GrammarBlock,
    GrammarExercise,
    GrammarLesson,
)


def pick_evenly(items, count):
    """
    Pick `count` unique items spread through a list.
    """
    items = list(items)

    if len(items) < count:
        raise CommandError(
            f"Need at least {count} candidates, "
            f"got {len(items)}"
        )

    if count == 1:
        return [items[len(items) // 2]]

    positions = []

    for i in range(count):
        raw = i * (len(items) - 1) / (count - 1)
        position = round(raw)

        if position not in positions:
            positions.append(position)

    # Extremely defensive fallback.
    if len(positions) < count:
        for position in range(len(items)):
            if position not in positions:
                positions.append(position)

            if len(positions) == count:
                break

    return [
        items[position]
        for position in positions[:count]
    ]


class Command(BaseCommand):
    help = (
        "Create diagnostic question mappings for "
        "A1 Grammar Lessons 1-60."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help=(
                "Delete existing A1 assessment mappings "
                "for lessons 1-60 before rebuilding."
            ),
        )

    def handle(self, *args, **options):

        lessons = list(
            GrammarLesson.objects.filter(
                level="A1",
                order__range=(1, 60),
                is_published=True,
            )
            .select_related("block")
            .order_by("order")
        )

        if len(lessons) != 60:
            raise CommandError(
                f"Expected 60 published A1 lessons, "
                f"got {len(lessons)}"
            )

        missing_blocks = [
            lesson.order
            for lesson in lessons
            if lesson.block_id is None
        ]

        if missing_blocks:
            raise CommandError(
                "Lessons without GrammarBlock: "
                + ", ".join(
                    map(str, missing_blocks)
                )
            )

        if options["reset"]:
            deleted, _ = (
                GrammarAssessmentQuestion.objects
                .filter(
                    exercise__lesson__level="A1",
                    exercise__lesson__order__range=(1, 60),
                )
                .delete()
            )

            self.stdout.write(
                f"🧹 Reset assessment mappings: {deleted}"
            )

        # -----------------------------------------
        # TOPIC DIAGNOSIS
        # Exactly 2 questions per lesson.
        # -----------------------------------------

        for lesson in lessons:

            exercises = list(
                GrammarExercise.objects.filter(
                    lesson=lesson,
                    is_published=True,
                ).order_by("order")
            )

            if len(exercises) < 4:
                raise CommandError(
                    f"Lesson {lesson.order} has only "
                    f"{len(exercises)} published exercises"
                )

            topic_questions = pick_evenly(
                exercises,
                2,
            )

            for priority, exercise in enumerate(
                topic_questions,
                start=1,
            ):
                GrammarAssessmentQuestion.objects.update_or_create(
                    exercise=exercise,
                    role=GrammarAssessmentQuestion.Role.TOPIC,
                    defaults={
                        "priority": priority,
                        "is_active": True,
                    },
                )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ Topic pool: 2 questions × 60 lessons"
            )
        )

        # -----------------------------------------
        # CHECKPOINT POOL
        # 2 candidate questions per lesson.
        # Later a checkpoint can draw a mixed
        # sample from the whole block.
        # -----------------------------------------

        for lesson in lessons:

            exercises = list(
                GrammarExercise.objects.filter(
                    lesson=lesson,
                    is_published=True,
                ).order_by("order")
            )

            count = len(exercises)

            positions = [
                max(0, count // 3),
                min(count - 1, (count * 2) // 3),
            ]

            if positions[0] == positions[1]:
                positions[1] = count - 1

            selected = []

            for position in positions:
                exercise = exercises[position]

                if exercise not in selected:
                    selected.append(exercise)

            if len(selected) < 2:
                for exercise in exercises:
                    if exercise not in selected:
                        selected.append(exercise)

                    if len(selected) == 2:
                        break

            for priority, exercise in enumerate(
                selected[:2],
                start=1,
            ):
                GrammarAssessmentQuestion.objects.update_or_create(
                    exercise=exercise,
                    role=GrammarAssessmentQuestion.Role.CHECKPOINT,
                    defaults={
                        "priority": priority,
                        "is_active": True,
                    },
                )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ Checkpoint pool: 2 questions × 60 lessons"
            )
        )

        # -----------------------------------------
        # BLOCK SCREENING
        # Exactly 4 questions per block.
        # Questions are spread across all exercises
        # inside the block.
        # -----------------------------------------

        blocks = list(
            GrammarBlock.objects.filter(
                level="A1",
                is_published=True,
            ).order_by("order")
        )

        if len(blocks) != 10:
            raise CommandError(
                f"Expected 10 A1 GrammarBlocks, "
                f"got {len(blocks)}"
            )

        for block in blocks:

            candidates = list(
                GrammarExercise.objects.filter(
                    lesson__block=block,
                    lesson__level="A1",
                    lesson__order__range=(1, 60),
                    lesson__is_published=True,
                    is_published=True,
                )
                .select_related("lesson")
                .order_by(
                    "lesson__order",
                    "order",
                )
            )

            screening_questions = pick_evenly(
                candidates,
                4,
            )

            for priority, exercise in enumerate(
                screening_questions,
                start=1,
            ):
                GrammarAssessmentQuestion.objects.update_or_create(
                    exercise=exercise,
                    role=GrammarAssessmentQuestion.Role.SCREENING,
                    defaults={
                        "priority": priority,
                        "is_active": True,
                    },
                )

            selected_text = ", ".join(
                (
                    f"L{exercise.lesson.order}"
                    f"/Q{exercise.order}"
                )
                for exercise in screening_questions
            )

            self.stdout.write(
                f"✅ Block {block.order}: "
                f"{selected_text}"
            )

        # -----------------------------------------
        # FINAL VERIFICATION
        # -----------------------------------------

        screening_count = (
            GrammarAssessmentQuestion.objects.filter(
                role=GrammarAssessmentQuestion.Role.SCREENING,
                is_active=True,
                exercise__lesson__level="A1",
                exercise__lesson__order__range=(1, 60),
            ).count()
        )

        topic_count = (
            GrammarAssessmentQuestion.objects.filter(
                role=GrammarAssessmentQuestion.Role.TOPIC,
                is_active=True,
                exercise__lesson__level="A1",
                exercise__lesson__order__range=(1, 60),
            ).count()
        )

        checkpoint_count = (
            GrammarAssessmentQuestion.objects.filter(
                role=GrammarAssessmentQuestion.Role.CHECKPOINT,
                is_active=True,
                exercise__lesson__level="A1",
                exercise__lesson__order__range=(1, 60),
            ).count()
        )

        if screening_count != 40:
            raise CommandError(
                f"Expected 40 screening questions, "
                f"got {screening_count}"
            )

        if topic_count != 120:
            raise CommandError(
                f"Expected 120 topic questions, "
                f"got {topic_count}"
            )

        if checkpoint_count != 120:
            raise CommandError(
                f"Expected 120 checkpoint questions, "
                f"got {checkpoint_count}"
            )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "✅ Grammar assessment pool ready"
            )
        )

        self.stdout.write(
            f"Screening: {screening_count}"
        )
        self.stdout.write(
            f"Topic diagnosis: {topic_count}"
        )
        self.stdout.write(
            f"Checkpoint candidates: {checkpoint_count}"
        )
