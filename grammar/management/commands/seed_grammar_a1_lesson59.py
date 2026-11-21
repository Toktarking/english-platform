from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 59: Ordinal Numbers and Dates."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=59,
            defaults={
                "title":
                    "Порядковые числительные и даты",

                "slug":
                    "ordinal-numbers-and-dates",

                "theory_text":
                    "Ordinal numbers, dates, years, "
                    "centuries and sequence expressions.",

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
                    "FIRST, SECOND, THIRD",

                "body":
                    """Ordinal numbers показывают
порядок.

1st — first

2nd — second

3rd — third

4th — fourth

5th — fifth

Примеры:

the first lesson

the second floor

the third student

Обычно перед ordinal
используется THE.""",
            },


            {
                "order": 2,
                "title":
                    "Окончание -TH",

                "body":
                    """Большинство ordinal numbers
образуются с -TH.

four → fourth

six → sixth

seven → seventh

ten → tenth

Но некоторые формы
нужно запомнить:

five → fifth

eight → eighth

nine → ninth

twelve → twelfth""",
            },


            {
                "order": 3,
                "title":
                    "20th, 30th, 40th",

                "body":
                    """Если число заканчивается
на -Y:

-y → -ieth

20 → twentieth

30 → thirtieth

40 → fortieth

50 → fiftieth

90 → ninetieth

Важно:

fortieth

не fourtieth.""",
            },


            {
                "order": 4,
                "title":
                    "21st, 22nd, 23rd",

                "body":
                    """В составных числах
меняется только последняя часть.

21st
→ twenty-first

22nd
→ twenty-second

23rd
→ twenty-third

24th
→ twenty-fourth

42nd
→ forty-second

Не:

twentieth-first.""",
            },


            {
                "order": 5,
                "title":
                    "ST / ND / RD / TH",

                "body":
                    """Сокращения:

1st

2nd

3rd

4th

Обычно:

1 → st

2 → nd

3 → rd

остальные → th

Но:

11th

12th

13th

Это исключения.""",
            },


            {
                "order": 6,
                "title":
                    "THE и possessives",

                "body":
                    """Обычно:

the first lesson

the second chapter

Но после possessive
THE не нужен.

my first job

her second child

our third lesson

Не:

my the first job

Правильно:

my first job.""",
            },


            {
                "order": 7,
                "title":
                    "Даты",

                "body":
                    """В британском варианте:

15 July

читаем:

the fifteenth of July

1 May:

the first of May

22 October:

the twenty-second of October

С конкретной датой:

ON

on 15 July

on the first of May.""",
            },


            {
                "order": 8,
                "title":
                    "ON и IN",

                "body":
                    """ON:

с конкретным днём
или датой.

on Monday

on 7 March

on 15 July 2026

IN:

с месяцем или годом.

in March

in July 2026

in 2026

Не:

in 15 July.""",
            },


            {
                "order": 9,
                "title":
                    "Годы и века",

                "body":
                    """Годы:

1998
→ nineteen ninety-eight

2026
→ twenty twenty-six

Века:

1800s
→ nineteenth century

1900s
→ twentieth century

2000s
→ twenty-first century

Century всегда ordinal.""",
            },


            {
                "order": 10,
                "title":
                    "FIRST / AT FIRST / THE FIRST",

                "body":
                    """FIRST:

первое действие.

First, read the text.

AT FIRST:

поначалу.

At first,
I didn't understand.

THE FIRST:

первый по порядку.

She was the first
student to arrive.

Это три разные конструкции.""",
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
                    "She was the ___ person to arrive.",
                "options": [
                    "first",
                    "one",
                    "oneth",
                    "once",
                ],
                "answer":
                    "first",
                "explanation":
                    "1st = FIRST.",
            },

            {
                "order": 2,
                "section": 1,
                "prompt":
                    "He finished ___ in the competition.",
                "options": [
                    "third",
                    "three",
                    "threeth",
                    "thirty",
                ],
                "answer":
                    "third",
                "explanation":
                    "3rd = THIRD.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "prompt":
                    "Choose the correct form of 5th.",
                "options": [
                    "fifth",
                    "fiveth",
                    "fivth",
                    "five-th",
                ],
                "answer":
                    "fifth",
                "explanation":
                    "5th = FIFTH.",
            },

            {
                "order": 4,
                "section": 2,
                "prompt":
                    "Choose the correct form of 12th.",
                "options": [
                    "twelfth",
                    "twelveth",
                    "twelvth",
                    "twelve-th",
                ],
                "answer":
                    "twelfth",
                "explanation":
                    "12th = TWELFTH.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "prompt":
                    "20th = ?",
                "options": [
                    "twentieth",
                    "twentyth",
                    "twentyeth",
                    "twenty-th",
                ],
                "answer":
                    "twentieth",
                "explanation":
                    "TWENTY → TWENTIETH.",
            },

            {
                "order": 6,
                "section": 3,
                "prompt":
                    "40th = ?",
                "options": [
                    "fortieth",
                    "fourtieth",
                    "fortyth",
                    "fortyeth",
                ],
                "answer":
                    "fortieth",
                "explanation":
                    "40th = FORTIETH.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "prompt":
                    "21st = ?",
                "options": [
                    "twenty-first",
                    "twentieth-first",
                    "twenty-oneth",
                    "twenty-one",
                ],
                "answer":
                    "twenty-first",
                "explanation":
                    "Меняется только последняя часть.",
            },

            {
                "order": 8,
                "section": 4,
                "prompt":
                    "42nd = ?",
                "options": [
                    "forty-second",
                    "fortieth-two",
                    "fourty-second",
                    "forty-twoth",
                ],
                "answer":
                    "forty-second",
                "explanation":
                    "42nd = FORTY-SECOND.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "prompt":
                    "Choose the correct abbreviation for eleven.",
                "options": [
                    "11th",
                    "11st",
                    "11nd",
                    "11rd",
                ],
                "answer":
                    "11th",
                "explanation":
                    "11 — исключение → 11TH.",
            },

            {
                "order": 10,
                "section": 5,
                "prompt":
                    "Choose the correct abbreviation for twenty-three.",
                "options": [
                    "23rd",
                    "23th",
                    "23nd",
                    "23st",
                ],
                "answer":
                    "23rd",
                "explanation":
                    "23 заканчивается на 3 → RD.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "This is my first job.",
                    "This is my the first job.",
                    "This is the my first job.",
                    "This is my one-th job.",
                ],
                "answer":
                    "This is my first job.",
                "explanation":
                    "После MY артикль THE не нужен.",
            },

            {
                "order": 12,
                "section": 6,
                "prompt":
                    "Choose the correct phrase.",
                "options": [
                    "her second child",
                    "her the second child",
                    "the her second child",
                    "her two-th child",
                ],
                "answer":
                    "her second child",
                "explanation":
                    "Possessive заменяет THE.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "prompt":
                    "15 July is read:",
                "options": [
                    "the fifteenth of July",
                    "the fifteen of July",
                    "July the fifteen-th",
                    "the fifty of July",
                ],
                "answer":
                    "the fifteenth of July",
                "explanation":
                    "В дате используем ordinal number.",
            },

            {
                "order": 14,
                "section": 7,
                "prompt":
                    "22 October is read:",
                "options": [
                    "the twenty-second of October",
                    "the twenty-two of October",
                    "the twentieth-two of October",
                    "October twenty-twoth",
                ],
                "answer":
                    "the twenty-second of October",
                "explanation":
                    "22nd = TWENTY-SECOND.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "prompt":
                    "Her birthday is ___ 7 March.",
                "options": [
                    "on",
                    "in",
                    "at",
                    "for",
                ],
                "answer":
                    "on",
                "explanation":
                    "Конкретная дата → ON.",
            },

            {
                "order": 16,
                "section": 8,
                "prompt":
                    "The course starts ___ September 2026.",
                "options": [
                    "in",
                    "on",
                    "at",
                    "by",
                ],
                "answer":
                    "in",
                "explanation":
                    "Month + year → IN.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "prompt":
                    "1998 is commonly read:",
                "options": [
                    "nineteen ninety-eight",
                    "nineteen eight-nine",
                    "one nine ninety-eight",
                    "ninety-eight nineteen",
                ],
                "answer":
                    "nineteen ninety-eight",
                "explanation":
                    "Годы до 2000 часто читаются парами.",
            },

            {
                "order": 18,
                "section": 9,
                "prompt":
                    "The 1900s are:",
                "options": [
                    "the twentieth century",
                    "the nineteenth century",
                    "the twenty-first century",
                    "the eighteenth century",
                ],
                "answer":
                    "the twentieth century",
                "explanation":
                    "1900–1999 относятся к twentieth century.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "prompt":
                    "___, read the instructions.",
                "options": [
                    "First",
                    "At first",
                    "The first",
                    "Firstly the",
                ],
                "answer":
                    "First",
                "explanation":
                    "FIRST показывает первое действие.",
            },

            {
                "order": 20,
                "section": 10,
                "prompt":
                    "___, I didn't like the course, but later I enjoyed it.",
                "options": [
                    "At first",
                    "First",
                    "The first",
                    "First time",
                ],
                "answer":
                    "At first",
                "explanation":
                    "AT FIRST = поначалу, затем ситуация изменилась.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "Choose the correct form of 8th.",
                "options": [
                    "eighth",
                    "eightth",
                    "eigth",
                    "eight-th",
                ],
                "answer":
                    "eighth",
                "explanation":
                    "8th = EIGHTH.",
            },

            {
                "order": 22,
                "prompt":
                    "31st = ?",
                "options": [
                    "thirty-first",
                    "thirtieth-first",
                    "thirty-oneth",
                    "thirty-one",
                ],
                "answer":
                    "thirty-first",
                "explanation":
                    "В составном ordinal меняется последняя часть.",
            },

            {
                "order": 23,
                "prompt":
                    "Choose the correct abbreviation for twelve.",
                "options": [
                    "12th",
                    "12nd",
                    "12st",
                    "12rd",
                ],
                "answer":
                    "12th",
                "explanation":
                    "12 — исключение → 12TH.",
            },

            {
                "order": 24,
                "prompt":
                    "Choose the correct phrase.",
                "options": [
                    "our third lesson",
                    "our the third lesson",
                    "the our third lesson",
                    "our three-th lesson",
                ],
                "answer":
                    "our third lesson",
                "explanation":
                    "После OUR артикль THE не нужен.",
            },

            {
                "order": 25,
                "prompt":
                    "1 May is read:",
                "options": [
                    "the first of May",
                    "the one of May",
                    "the oneth of May",
                    "May the one-th",
                ],
                "answer":
                    "the first of May",
                "explanation":
                    "1st = FIRST.",
            },

            {
                "order": 26,
                "prompt":
                    "The meeting is ___ 18 November.",
                "options": [
                    "on",
                    "in",
                    "at",
                    "from",
                ],
                "answer":
                    "on",
                "explanation":
                    "Конкретная дата → ON.",
            },

            {
                "order": 27,
                "prompt":
                    "The company was founded ___ 2005.",
                "options": [
                    "in",
                    "on",
                    "at",
                    "for",
                ],
                "answer":
                    "in",
                "explanation":
                    "Год → IN.",
            },

            {
                "order": 28,
                "prompt":
                    "The 2000s belong to:",
                "options": [
                    "the twenty-first century",
                    "the twentieth century",
                    "the nineteenth century",
                    "the twenty-second century",
                ],
                "answer":
                    "the twenty-first century",
                "explanation":
                    "2000–2099 относятся к twenty-first century.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct FIRST / AT FIRST / THE FIRST sequence.",
                "options": [
                    "First, open the book. / At first, it seemed difficult. / She was the first student.",
                    "At first, open the book. / First, it seemed difficult but later changed. / She was first the student.",
                    "The first, open the book. / At first time, it seemed difficult. / She was a first student.",
                    "First the, open the book. / The first, it seemed difficult. / She was at first student.",
                ],
                "answer":
                    "First, open the book. / At first, it seemed difficult. / She was the first student.",
                "explanation":
                    "FIRST = первое действие; AT FIRST = поначалу; THE FIRST = первый по порядку.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "1st → first / 2nd → second / 3rd → third / 21st → twenty-first / date → on 15 July / year → in 2026",
                    "1st → oneth / 2nd → twoth / 3rd → threeth / 21st → twentieth-first / date → in 15 July / year → on 2026",
                    "1st → one / 2nd → twice / 3rd → three / 21st → twenty-oneth / date → at 15 July / year → on 2026",
                    "1st → firstly / 2nd → two-th / 3rd → thirdth / 21st → twenty-one-th / date → in the 15 July / year → at 2026",
                ],
                "answer":
                    "1st → first / 2nd → second / 3rd → third / 21st → twenty-first / date → on 15 July / year → in 2026",
                "explanation":
                    "Это основные правила Ordinal Numbers and Dates.",
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
                "✅ Interactive A1 Lesson 59 seeded"
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
