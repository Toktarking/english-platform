from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 58: Cardinal Numbers."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=58,
            defaults={
                "title":
                    "Количественные числительные",

                "slug":
                    "cardinal-numbers",

                "theory_text":
                    "Cardinal numbers: numbers, quantities, "
                    "age, money and large numbers.",

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
                    "Числа 0–19",

                "body":
                    """Основные числа нужно
хорошо запомнить.

0 — zero
1 — one
2 — two
3 — three
10 — ten

Особые формы:

11 — eleven
12 — twelve
13 — thirteen
15 — fifteen
18 — eighteen

Важно:

15 = fifteen

не fiveteen.""",
            },


            {
                "order": 2,
                "title":
                    "Десятки",

                "body":
                    """Основные десятки:

20 — twenty
30 — thirty
40 — forty
50 — fifty
60 — sixty
70 — seventy
80 — eighty
90 — ninety

Особенно запомни:

40 = forty

Не:

fourty.""",
            },


            {
                "order": 3,
                "title":
                    "Числа 21–99",

                "body":
                    """Числа между десятками
обычно пишутся через дефис.

21 — twenty-one

37 — thirty-seven

45 — forty-five

99 — ninety-nine

Схема:

tens + ones

thirty + seven
→ thirty-seven.""",
            },


            {
                "order": 4,
                "title":
                    "HUNDRED",

                "body":
                    """После точного числа
HUNDRED остаётся без -s.

100 — one hundred

200 — two hundred

500 — five hundred

Правильно:

three hundred students

Не:

three hundreds students.

125:

one hundred and twenty-five.""",
            },


            {
                "order": 5,
                "title":
                    "THOUSAND / MILLION",

                "body":
                    """После точного числа:

thousand
million
billion

тоже не получают -s.

2,000

two thousand

3,000,000

three million

Не:

two thousands

three millions.""",
            },


            {
                "order": 6,
                "title":
                    "THOUSANDS OF",

                "body":
                    """Если точного числа нет,
используем plural + OF.

hundreds of people

thousands of students

millions of dollars

Сравни:

two thousand students
— точное число

thousands of students
— много, но нет точного числа.""",
            },


            {
                "order": 7,
                "title":
                    "Возраст",

                "body":
                    """После BE:

number + years old

She is ten years old.

He is twenty years old.

Перед noun:

number-year-old + noun

a ten-year-old child

a twenty-year-old student

Важно:

перед noun слово YEAR
остаётся singular.""",
            },


            {
                "order": 8,
                "title":
                    "HOW MANY / HOW MUCH",

                "body":
                    """HOW MANY:

с countable plural nouns.

How many students?

How many books?

HOW MUCH:

с uncountable nouns.

How much money?

How much water?

Также HOW MUCH
используем для цены.

How much is this book?""",
            },


            {
                "order": 9,
                "title":
                    "NUMBER / AMOUNT",

                "body":
                    """NUMBER используется
с countable nouns.

the number of students

the number of cars

AMOUNT используется
с uncountable nouns.

the amount of money

the amount of information

Также:

a number of students
= несколько студентов.""",
            },


            {
                "order": 10,
                "title":
                    "A NUMBER OF / THE NUMBER OF",

                "body":
                    """A NUMBER OF + plural noun
обычно требует plural verb.

A number of students
are absent.

THE NUMBER OF означает
количество как один показатель.

The number of students
is increasing.

Главное:

a number of → plural verb

the number of → singular verb.""",
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
                    "Choose the correct spelling for 15.",
                "options": [
                    "fifteen",
                    "fiveteen",
                    "fivteen",
                    "fiftyeen",
                ],
                "answer":
                    "fifteen",
                "explanation":
                    "15 = FIFTEEN.",
            },

            {
                "order": 2,
                "section": 1,
                "prompt":
                    "Choose the correct spelling for 18.",
                "options": [
                    "eighteen",
                    "eightteen",
                    "eightyteen",
                    "eigten",
                ],
                "answer":
                    "eighteen",
                "explanation":
                    "18 = EIGHTEEN.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "prompt":
                    "Choose the correct spelling for 40.",
                "options": [
                    "forty",
                    "fourty",
                    "fourti",
                    "fortee",
                ],
                "answer":
                    "forty",
                "explanation":
                    "40 = FORTY, без U.",
            },

            {
                "order": 4,
                "section": 2,
                "prompt":
                    "Choose the correct spelling for 80.",
                "options": [
                    "eighty",
                    "eightty",
                    "eigthty",
                    "eightyteen",
                ],
                "answer":
                    "eighty",
                "explanation":
                    "80 = EIGHTY.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "prompt":
                    "37 = ?",
                "options": [
                    "thirty-seven",
                    "thirty seven",
                    "thirteen-seven",
                    "three-seven",
                ],
                "answer":
                    "thirty-seven",
                "explanation":
                    "Числа 21–99 обычно пишутся через дефис.",
            },

            {
                "order": 6,
                "section": 3,
                "prompt":
                    "64 = ?",
                "options": [
                    "sixty-four",
                    "sixteen-four",
                    "sixty fourty",
                    "six-four",
                ],
                "answer":
                    "sixty-four",
                "explanation":
                    "60 + 4 → SIXTY-FOUR.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "prompt":
                    "300 students = ?",
                "options": [
                    "three hundred students",
                    "three hundreds students",
                    "three hundred of students",
                    "three hundreds of student",
                ],
                "answer":
                    "three hundred students",
                "explanation":
                    "После точного числа HUNDRED без -s.",
            },

            {
                "order": 8,
                "section": 4,
                "prompt":
                    "406 = ?",
                "options": [
                    "four hundred and six",
                    "four hundreds and six",
                    "four hundred sixes",
                    "four thousand and six",
                ],
                "answer":
                    "four hundred and six",
                "explanation":
                    "Точное число → HUNDRED без -s.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "prompt":
                    "5,000 = ?",
                "options": [
                    "five thousand",
                    "five thousands",
                    "five thousand of",
                    "five-thousands",
                ],
                "answer":
                    "five thousand",
                "explanation":
                    "После точного числа THOUSAND без -s.",
            },

            {
                "order": 10,
                "section": 5,
                "prompt":
                    "2,000,000 = ?",
                "options": [
                    "two million",
                    "two millions",
                    "two million of",
                    "two millions of",
                ],
                "answer":
                    "two million",
                "explanation":
                    "После точного числа MILLION без -s.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "prompt":
                    "___ of people use the internet every day.",
                "options": [
                    "Millions",
                    "Million",
                    "Three millions",
                    "Million of",
                ],
                "answer":
                    "Millions",
                "explanation":
                    "Неточное количество → MILLIONS OF.",
            },

            {
                "order": 12,
                "section": 6,
                "prompt":
                    "Choose the correct approximate phrase.",
                "options": [
                    "thousands of students",
                    "thousand students",
                    "three thousands students",
                    "thousands students",
                ],
                "answer":
                    "thousands of students",
                "explanation":
                    "Неточное количество → THOUSANDS OF.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "prompt":
                    "The boy is ___.",
                "options": [
                    "ten years old",
                    "ten-year-old",
                    "ten-years-old",
                    "ten year olds",
                ],
                "answer":
                    "ten years old",
                "explanation":
                    "После BE → YEARS OLD.",
            },

            {
                "order": 14,
                "section": 7,
                "prompt":
                    "He is a ___ student.",
                "options": [
                    "twenty-year-old",
                    "twenty-years-old",
                    "twenty years old",
                    "twenty-year-olds",
                ],
                "answer":
                    "twenty-year-old",
                "explanation":
                    "Перед noun → NUMBER-YEAR-OLD.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "prompt":
                    "___ students are in the room?",
                "options": [
                    "How many",
                    "How much",
                    "How amount",
                    "How number",
                ],
                "answer":
                    "How many",
                "explanation":
                    "STUDENTS = countable plural → HOW MANY.",
            },

            {
                "order": 16,
                "section": 8,
                "prompt":
                    "___ money do you need?",
                "options": [
                    "How much",
                    "How many",
                    "How number",
                    "How few many",
                ],
                "answer":
                    "How much",
                "explanation":
                    "MONEY = uncountable → HOW MUCH.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "prompt":
                    "Choose the correct phrase.",
                "options": [
                    "the number of students",
                    "the amount of students",
                    "the much of students",
                    "the numbers amount students",
                ],
                "answer":
                    "the number of students",
                "explanation":
                    "Countable plural → NUMBER.",
            },

            {
                "order": 18,
                "section": 9,
                "prompt":
                    "Choose the correct phrase.",
                "options": [
                    "the amount of information",
                    "the number of information",
                    "the many of information",
                    "the amounts number information",
                ],
                "answer":
                    "the amount of information",
                "explanation":
                    "INFORMATION = uncountable → AMOUNT.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "prompt":
                    "A number of students ___ absent today.",
                "options": [
                    "are",
                    "is",
                    "was",
                    "has",
                ],
                "answer":
                    "are",
                "explanation":
                    "A NUMBER OF + plural noun → plural verb.",
            },

            {
                "order": 20,
                "section": 10,
                "prompt":
                    "The number of students ___ increasing.",
                "options": [
                    "is",
                    "are",
                    "were",
                    "have",
                ],
                "answer":
                    "is",
                "explanation":
                    "THE NUMBER OF → singular verb.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "Choose the correct spelling for 50.",
                "options": [
                    "fifty",
                    "fivety",
                    "fiftye",
                    "fivty",
                ],
                "answer":
                    "fifty",
                "explanation":
                    "50 = FIFTY.",
            },

            {
                "order": 22,
                "prompt":
                    "92 = ?",
                "options": [
                    "ninety-two",
                    "nineteen-two",
                    "ninety twoo",
                    "nine-two",
                ],
                "answer":
                    "ninety-two",
                "explanation":
                    "90 + 2 → NINETY-TWO.",
            },

            {
                "order": 23,
                "prompt":
                    "700 workers = ?",
                "options": [
                    "seven hundred workers",
                    "seven hundreds workers",
                    "seven hundred of workers",
                    "seven hundreds of workers",
                ],
                "answer":
                    "seven hundred workers",
                "explanation":
                    "Exact number → HUNDRED без -s.",
            },

            {
                "order": 24,
                "prompt":
                    "12,000 people = ?",
                "options": [
                    "twelve thousand people",
                    "twelve thousands people",
                    "twelve thousand of people",
                    "twelve thousands of people",
                ],
                "answer":
                    "twelve thousand people",
                "explanation":
                    "Exact number → THOUSAND без -s.",
            },

            {
                "order": 25,
                "prompt":
                    "Choose the correct approximate phrase.",
                "options": [
                    "hundreds of cars",
                    "hundred of cars",
                    "two hundreds cars",
                    "hundreds cars",
                ],
                "answer":
                    "hundreds of cars",
                "explanation":
                    "Без точного числа → HUNDREDS OF.",
            },

            {
                "order": 26,
                "prompt":
                    "She is a ___ child.",
                "options": [
                    "five-year-old",
                    "five-years-old",
                    "five years old",
                    "five-year-olds",
                ],
                "answer":
                    "five-year-old",
                "explanation":
                    "Перед noun → FIVE-YEAR-OLD.",
            },

            {
                "order": 27,
                "prompt":
                    "___ books did you buy?",
                "options": [
                    "How many",
                    "How much",
                    "How amount",
                    "How number",
                ],
                "answer":
                    "How many",
                "explanation":
                    "BOOKS = countable plural.",
            },

            {
                "order": 28,
                "prompt":
                    "Choose the correct pair.",
                "options": [
                    "the number of cars / the amount of money",
                    "the amount of cars / the number of money",
                    "the number of information / the amount of students",
                    "the amount of books / the number of water",
                ],
                "answer":
                    "the number of cars / the amount of money",
                "explanation":
                    "NUMBER → countable; AMOUNT → uncountable.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct verb pair.",
                "options": [
                    "A number of workers are absent. / The number of workers is growing.",
                    "A number of workers is absent. / The number of workers are growing.",
                    "A number of workers was always plural. / The number of workers have growing.",
                    "A number of workers has absent. / The number of workers were growing.",
                ],
                "answer":
                    "A number of workers are absent. / The number of workers is growing.",
                "explanation":
                    "A NUMBER OF → plural; THE NUMBER OF → singular.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "40 → forty / 35 → thirty-five / 300 → three hundred / 4,000 → four thousand / approximate → thousands of",
                    "40 → fourty / 35 → thirty five always / 300 → three hundreds / 4,000 → four thousands / approximate → thousand of",
                    "40 → forty / 35 → thirteen-five / 300 → three hundred of / 4,000 → four thousand of / approximate → thousands people",
                    "40 → fourty / 35 → thirty-fifth / 300 → three hundreds / 4,000 → four-thousands / approximate → three thousands",
                ],
                "answer":
                    "40 → forty / 35 → thirty-five / 300 → three hundred / 4,000 → four thousand / approximate → thousands of",
                "explanation":
                    "Это основные правила Cardinal Numbers.",
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
                "✅ Interactive A1 Lesson 58 seeded"
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
