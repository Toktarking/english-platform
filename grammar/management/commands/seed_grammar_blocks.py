from django.core.management.base import BaseCommand, CommandError

from grammar.models import GrammarBlock, GrammarLesson


BLOCKS = [
    {
        "order": 1,
        "title": "Foundations",
        "slug": "foundations",
        "description": (
            "Articles, nouns, quantifiers, pronouns, "
            "demonstratives, reflexive pronouns and TO BE."
        ),
        "start": 1,
        "end": 10,
    },
    {
        "order": 2,
        "title": "Basic Sentences",
        "slug": "basic-sentences",
        "description": (
            "Present Simple, questions, there is/are, "
            "have/has, prepositions, imperatives and can/could."
        ),
        "start": 11,
        "end": 20,
    },
    {
        "order": 3,
        "title": "Present & Past",
        "slug": "present-and-past",
        "description": (
            "Present Continuous, Present Simple vs Continuous, "
            "Past Simple and Past Continuous."
        ),
        "start": 21,
        "end": 29,
    },
    {
        "order": 4,
        "title": "Perfect Tenses",
        "slug": "perfect-tenses",
        "description": (
            "Present Perfect, Present Perfect Continuous, "
            "Past Perfect and Past Perfect Continuous."
        ),
        "start": 30,
        "end": 35,
    },
    {
        "order": 5,
        "title": "Future & Modals",
        "slug": "future-and-modals",
        "description": (
            "Future with will, going to, future arrangements, "
            "Future Continuous, Future Perfect and modal verbs."
        ),
        "start": 36,
        "end": 40,
    },
    {
        "order": 6,
        "title": "Verb & Description Structures",
        "slug": "verb-and-description-structures",
        "description": (
            "Passive Voice, Infinitive and Gerund, comparisons, "
            "adjectives, adverbs and -ed/-ing adjectives."
        ),
        "start": 41,
        "end": 45,
    },
    {
        "order": 7,
        "title": "Conditionals",
        "slug": "conditionals",
        "description": (
            "Zero, First, Second and Third Conditionals, "
            "Wish and If only."
        ),
        "start": 46,
        "end": 50,
    },
    {
        "order": 8,
        "title": "Complex Sentences",
        "slug": "complex-sentences",
        "description": (
            "Reported Speech, question types, Question Tags "
            "and Relative Pronouns."
        ),
        "start": 51,
        "end": 54,
    },
    {
        "order": 9,
        "title": "Word & Comparison Structures",
        "slug": "word-and-comparison-structures",
        "description": (
            "Word Formation, comparative structures "
            "and the Possessive Case."
        ),
        "start": 55,
        "end": 57,
    },
    {
        "order": 10,
        "title": "Numbers & Dates",
        "slug": "numbers-and-dates",
        "description": (
            "Cardinal numbers, ordinal numbers, dates, "
            "fractions, decimals and percentages."
        ),
        "start": 58,
        "end": 60,
    },
]


class Command(BaseCommand):
    help = "Create A1 grammar blocks and assign lessons 1-60."

    def handle(self, *args, **options):

        expected_orders = set(range(1, 61))

        existing_orders = set(
            GrammarLesson.objects.filter(
                level="A1",
                order__range=(1, 60),
            ).values_list(
                "order",
                flat=True,
            )
        )

        missing = sorted(expected_orders - existing_orders)

        if missing:
            raise CommandError(
                "Missing A1 GrammarLesson orders: "
                + ", ".join(map(str, missing))
            )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ All A1 lessons 1-60 exist"
            )
        )

        for data in BLOCKS:

            block, created = GrammarBlock.objects.update_or_create(
                level="A1",
                order=data["order"],
                defaults={
                    "title": data["title"],
                    "slug": data["slug"],
                    "description": data["description"],
                    "is_published": True,
                },
            )

            updated = GrammarLesson.objects.filter(
                level="A1",
                order__gte=data["start"],
                order__lte=data["end"],
            ).update(
                block=block,
            )

            expected_count = (
                data["end"]
                - data["start"]
                + 1
            )

            if updated != expected_count:
                raise CommandError(
                    f"Block {data['order']} expected "
                    f"{expected_count} lessons, got {updated}"
                )

            action = "created" if created else "updated"

            self.stdout.write(
                f"✅ Block {data['order']}: "
                f"{data['title']} "
                f"({data['start']}-{data['end']}) "
                f"[{action}]"
            )

        blocks_count = GrammarBlock.objects.filter(
            level="A1",
        ).count()

        assigned_count = GrammarLesson.objects.filter(
            level="A1",
            order__range=(1, 60),
            block__isnull=False,
        ).count()

        if blocks_count != 10:
            raise CommandError(
                f"Expected 10 A1 blocks, got {blocks_count}"
            )

        if assigned_count != 60:
            raise CommandError(
                f"Expected 60 assigned lessons, "
                f"got {assigned_count}"
            )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "✅ Grammar roadmap seeded successfully"
            )
        )

        self.stdout.write(
            f"Blocks: {blocks_count}"
        )

        self.stdout.write(
            f"Assigned lessons: {assigned_count}"
        )
