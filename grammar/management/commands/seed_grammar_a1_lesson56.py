from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 56: Comparative Structures."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=56,
            defaults={
                "title":
                    "Сравнительные конструкции: as…as, too, enough, so, such",

                "slug":
                    "comparative-structures-as-too-enough-so-such",

                "theory_text":
                    "Comparative structures: as...as, too, "
                    "enough, so and such.",

                "estimated_minutes":
                    20,

                "pass_score":
                    70,

                "xp_reward":
                    100,

                "is_published":
                    True,
            },
        )


        # =================================================
        # 10 MICRO RULES
        # =================================================

        sections = [

            {
                "order": 1,
                "title":
                    "AS…AS",

                "body":
                    """AS…AS показывает равенство.

as + adjective + as

She is as tall as her sister.

This car is as fast as mine.

С adverb:

He works as carefully as Anna.

Важно:

после AS используется
обычная форма adjective.

Не:

as taller as

Правильно:

as tall as""",
            },


            {
                "order": 2,
                "title":
                    "NOT AS…AS",

                "body":
                    """NOT AS…AS показывает,
что два объекта не равны.

This room is not
as large as that one.

My phone is not
as expensive as yours.

Tom is taller than Jack.

=

Jack is not
as tall as Tom.""",
            },


            {
                "order": 3,
                "title":
                    "AS MUCH / AS MANY",

                "body":
                    """С quantity:

AS MUCH + uncountable noun

as much time as

as much money as

AS MANY + plural noun

as many books as

as many students as

Пример:

I don't have
as much time as you.

She has as many books
as her brother.""",
            },


            {
                "order": 4,
                "title":
                    "TOO",

                "body":
                    """TOO означает:

слишком.

too + adjective/adverb

too expensive

too difficult

too quickly

Пример:

The coffee is too hot.

TOO часто показывает,
что есть проблема.

The coffee is too hot
to drink.""",
            },


            {
                "order": 5,
                "title":
                    "TOO MUCH / TOO MANY",

                "body":
                    """TOO MUCH:

с uncountable nouns.

too much work

too much money

too much information

TOO MANY:

с plural countable nouns.

too many people

too many mistakes

too many questions""",
            },


            {
                "order": 6,
                "title":
                    "ENOUGH",

                "body":
                    """ENOUGH = достаточно.

После adjective:

old enough

strong enough

warm enough

Перед noun:

enough time

enough money

enough chairs

Важно:

old enough

Не:

enough old""",
            },


            {
                "order": 7,
                "title":
                    "TOO / ENOUGH + TO",

                "body":
                    """Формулы:

too + adjective + to + V1

enough + noun

adjective + enough + to + V1

Примеры:

The box is too heavy
to carry.

He is old enough
to drive.

We have enough money
to travel.""",
            },


            {
                "order": 8,
                "title":
                    "SO",

                "body":
                    """SO усиливает adjective
или adverb.

so beautiful

so tired

so quickly

SO…THAT показывает результат.

The film was so boring
that I fell asleep.

She was so tired
that she couldn't work.""",
            },


            {
                "order": 9,
                "title":
                    "SUCH",

                "body":
                    """SUCH используется
с noun phrase.

such a beautiful city

such an interesting book

such friendly people

such useful information

SO:

so beautiful

SUCH:

such a beautiful city

Главное:

SO + adjective/adverb

SUCH + noun phrase""",
            },


            {
                "order": 10,
                "title":
                    "Как выбрать конструкцию",

                "body":
                    """Равенство?

→ as…as

Неравенство?

→ not as…as

Слишком?

→ too

Достаточно?

→ enough

Усиливаем adjective/adverb?

→ so

Усиливаем noun phrase?

→ such

Результат?

→ so…that / such…that""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = GrammarLessonSection.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "title":
                        data["title"],

                    "body":
                        data["body"],
                },
            )

            section_objects[
                data["order"]
            ] = section


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            # SECTION 1
            {
                "order": 1,
                "section": 1,
                "prompt":
                    "My brother is ___ tall as my father.",
                "options": [
                    "as",
                    "too",
                    "such",
                    "enough",
                ],
                "answer":
                    "as",
                "explanation":
                    "Равенство → AS + adjective + AS.",
            },

            {
                "order": 2,
                "section": 1,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "She is as tall as her sister.",
                    "She is as taller as her sister.",
                    "She is as tall than her sister.",
                    "She is so tall as her sister.",
                ],
                "answer":
                    "She is as tall as her sister.",
                "explanation":
                    "После AS используется обычная форма adjective.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "prompt":
                    "This book is not ___ interesting as that one.",
                "options": [
                    "as",
                    "too",
                    "such",
                    "enough",
                ],
                "answer":
                    "as",
                "explanation":
                    "NOT AS + adjective + AS.",
            },

            {
                "order": 4,
                "section": 2,
                "prompt":
                    "Tom is taller than Ben. Choose the equal meaning.",
                "options": [
                    "Ben is not as tall as Tom.",
                    "Ben is as tall as Tom.",
                    "Ben is too tall as Tom.",
                    "Ben is so tall as Tom.",
                ],
                "answer":
                    "Ben is not as tall as Tom.",
                "explanation":
                    "NOT AS…AS показывает неравенство.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "prompt":
                    "I don't have ___ much time as you.",
                "options": [
                    "as",
                    "too",
                    "so",
                    "enough",
                ],
                "answer":
                    "as",
                "explanation":
                    "TIME = uncountable → AS MUCH.",
            },

            {
                "order": 6,
                "section": 3,
                "prompt":
                    "She has ___ many books as her sister.",
                "options": [
                    "as",
                    "too",
                    "such",
                    "enough",
                ],
                "answer":
                    "as",
                "explanation":
                    "BOOKS = countable plural → AS MANY.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "prompt":
                    "The coffee is ___ hot to drink.",
                "options": [
                    "too",
                    "enough",
                    "such",
                    "as",
                ],
                "answer":
                    "too",
                "explanation":
                    "TOO HOT = слишком горячий.",
            },

            {
                "order": 8,
                "section": 4,
                "prompt":
                    "This task is ___ difficult for me.",
                "options": [
                    "too",
                    "enough",
                    "as",
                    "such a",
                ],
                "answer":
                    "too",
                "explanation":
                    "TOO + adjective показывает чрезмерность.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "prompt":
                    "I have ___ much work today.",
                "options": [
                    "too",
                    "too many",
                    "such a",
                    "enough many",
                ],
                "answer":
                    "too",
                "explanation":
                    "WORK = uncountable → TOO MUCH.",
            },

            {
                "order": 10,
                "section": 5,
                "prompt":
                    "There are ___ many people here.",
                "options": [
                    "too",
                    "too much",
                    "enough of",
                    "such a",
                ],
                "answer":
                    "too",
                "explanation":
                    "PEOPLE = plural countable → TOO MANY.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "prompt":
                    "The room is warm ___.",
                "options": [
                    "enough",
                    "too",
                    "such",
                    "so a",
                ],
                "answer":
                    "enough",
                "explanation":
                    "После adjective → WARM ENOUGH.",
            },

            {
                "order": 12,
                "section": 6,
                "prompt":
                    "We have ___ chairs for everyone.",
                "options": [
                    "enough",
                    "too",
                    "so",
                    "such",
                ],
                "answer":
                    "enough",
                "explanation":
                    "Перед noun → ENOUGH CHAIRS.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "prompt":
                    "He is ___ young to drive.",
                "options": [
                    "too",
                    "enough",
                    "such",
                    "as",
                ],
                "answer":
                    "too",
                "explanation":
                    "TOO + adjective + TO + V1.",
            },

            {
                "order": 14,
                "section": 7,
                "prompt":
                    "He is old ___ to drive.",
                "options": [
                    "enough",
                    "too",
                    "such",
                    "so",
                ],
                "answer":
                    "enough",
                "explanation":
                    "Adjective + ENOUGH + TO + V1.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "prompt":
                    "The film was ___ boring that I fell asleep.",
                "options": [
                    "so",
                    "such",
                    "too",
                    "enough",
                ],
                "answer":
                    "so",
                "explanation":
                    "SO + adjective + THAT.",
            },

            {
                "order": 16,
                "section": 8,
                "prompt":
                    "She was ___ tired that she couldn't work.",
                "options": [
                    "so",
                    "such a",
                    "too much",
                    "enough",
                ],
                "answer":
                    "so",
                "explanation":
                    "SO усиливает adjective TIRED.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "prompt":
                    "It was ___ interesting book.",
                "options": [
                    "such an",
                    "so an",
                    "too an",
                    "enough an",
                ],
                "answer":
                    "such an",
                "explanation":
                    "SUCH + AN + adjective + singular noun.",
            },

            {
                "order": 18,
                "section": 9,
                "prompt":
                    "They are ___ friendly people.",
                "options": [
                    "such",
                    "so",
                    "such a",
                    "too",
                ],
                "answer":
                    "such",
                "explanation":
                    "Plural noun phrase → SUCH FRIENDLY PEOPLE.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "prompt":
                    "Choose the correct pair.",
                "options": [
                    "so beautiful / such a beautiful city",
                    "such beautiful / so a beautiful city",
                    "so a beautiful / such beautiful city",
                    "too beautiful / enough a city",
                ],
                "answer":
                    "so beautiful / such a beautiful city",
                "explanation":
                    "SO + adjective; SUCH + noun phrase.",
            },

            {
                "order": 20,
                "section": 10,
                "prompt":
                    "Choose the correct TOO / ENOUGH pair.",
                "options": [
                    "too young to drive / old enough to drive",
                    "enough young to drive / too old enough",
                    "too young driving / enough old to drive",
                    "too enough young / old to enough drive",
                ],
                "answer":
                    "too young to drive / old enough to drive",
                "explanation":
                    "TOO + adjective + TO; adjective + ENOUGH + TO.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "This laptop is ___ expensive as mine.",
                "options": [
                    "as",
                    "too",
                    "such",
                    "enough",
                ],
                "answer":
                    "as",
                "explanation":
                    "AS + adjective + AS.",
            },

            {
                "order": 22,
                "prompt":
                    "My car is not ___ fast as yours.",
                "options": [
                    "as",
                    "too",
                    "so a",
                    "enough",
                ],
                "answer":
                    "as",
                "explanation":
                    "NOT AS…AS.",
            },

            {
                "order": 23,
                "prompt":
                    "There are ___ many mistakes in this report.",
                "options": [
                    "too",
                    "too much",
                    "enough of",
                    "such a",
                ],
                "answer":
                    "too",
                "explanation":
                    "MISTAKES = plural → TOO MANY.",
            },

            {
                "order": 24,
                "prompt":
                    "We don't have ___ money for the trip.",
                "options": [
                    "enough",
                    "too many",
                    "such",
                    "as many",
                ],
                "answer":
                    "enough",
                "explanation":
                    "ENOUGH ставится перед noun.",
            },

            {
                "order": 25,
                "prompt":
                    "The bag is ___ heavy for the child to carry.",
                "options": [
                    "too",
                    "enough",
                    "such",
                    "as",
                ],
                "answer":
                    "too",
                "explanation":
                    "TOO показывает чрезмерность.",
            },

            {
                "order": 26,
                "prompt":
                    "She is experienced ___ to manage the team.",
                "options": [
                    "enough",
                    "too",
                    "such",
                    "as",
                ],
                "answer":
                    "enough",
                "explanation":
                    "Adjective + ENOUGH + TO.",
            },

            {
                "order": 27,
                "prompt":
                    "The test was ___ difficult that many students failed.",
                "options": [
                    "so",
                    "such",
                    "too much",
                    "enough",
                ],
                "answer":
                    "so",
                "explanation":
                    "SO + adjective + THAT.",
            },

            {
                "order": 28,
                "prompt":
                    "It was ___ difficult test that many students failed.",
                "options": [
                    "such a",
                    "so",
                    "too a",
                    "enough a",
                ],
                "answer":
                    "such a",
                "explanation":
                    "SUCH + A + adjective + noun + THAT.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct MUCH / MANY pair.",
                "options": [
                    "as much time as / as many students as",
                    "as many time as / as much students as",
                    "too many information / too much people",
                    "enough many money / too much books",
                ],
                "answer":
                    "as much time as / as many students as",
                "explanation":
                    "MUCH → uncountable; MANY → plural countable.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "equality → as...as / excess → too / sufficiency → enough / adjective emphasis → so / noun phrase emphasis → such",
                    "equality → too / excess → enough / sufficiency → such / adjective emphasis → as / noun phrase emphasis → so",
                    "equality → such / excess → as...as / sufficiency → too / adjective emphasis → such / noun phrase emphasis → enough",
                    "equality → enough / excess → so / sufficiency → too / adjective emphasis → such a / noun phrase emphasis → as...as",
                ],
                "answer":
                    "equality → as...as / excess → too / sufficiency → enough / adjective emphasis → so / noun phrase emphasis → such",
                "explanation":
                    "Это основная система конструкций урока.",
            },

        ]


        all_exercises = (
            training
            +
            final_test
        )

        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

            if data["order"] <= 20:

                section = (
                    section_objects[
                        data["section"]
                    ]
                )

            else:

                section = None


            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "section":
                        section,

                    "exercise_type":
                        "choice",

                    "prompt":
                        data["prompt"],

                    "options":
                        data["options"],

                    "correct_answer":
                        data["answer"],

                    "explanation":
                        data["explanation"],

                    "is_published":
                        True,
                },
            )


        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        GrammarLessonSection.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=[
                item["order"]
                for item in sections
            ],
        ).delete()


        self.stdout.write(
            self.style.SUCCESS(
                "✅ Interactive A1 Lesson 56 seeded"
            )
        )

        self.stdout.write(
            f"Micro rules: "
            f"{lesson.sections.count()}"
        )

        self.stdout.write(
            "Training exercises: "
            f"{lesson.exercises.filter(section__isnull=False).count()}"
        )

        self.stdout.write(
            "Final test: "
            f"{lesson.exercises.filter(section__isnull=True).count()}"
        )
