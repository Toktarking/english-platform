from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 60: Fractions, Decimals and Percentages."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=60,
            defaults={
                "title":
                    "Дроби, десятичные числа и проценты",

                "slug":
                    "fractions-decimals-percentages",

                "theory_text":
                    "Fractions, decimals, percentages, "
                    "ratios and numerical changes.",

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
                    "Обычные дроби",

                "body":
                    """В обычной дроби:

числитель читаем
cardinal number.

знаменатель читаем
ordinal number.

1/3
→ one third

1/5
→ one fifth

2/5
→ two fifths

Если numerator больше 1,
denominator обычно plural.""",
            },


            {
                "order": 2,
                "title":
                    "HALF и QUARTER",

                "body":
                    """Особые формы:

1/2
→ one half

1/4
→ one quarter

3/4
→ three quarters

Примеры:

Half of the class...

A quarter of the students...

Three quarters
of the work...""",
            },


            {
                "order": 3,
                "title":
                    "Mixed Numbers",

                "body":
                    """Mixed number содержит
целую и дробную часть.

Используем AND.

1 1/2
→ one and a half

2 1/3
→ two and one third

3 1/4
→ three and a quarter

5 2/3
→ five and two thirds.""",
            },


            {
                "order": 4,
                "title":
                    "Agreement после OF",

                "body":
                    """После fraction + OF
глагол зависит от noun.

Half of the work
is finished.

WORK = uncountable.

Half of the students
are absent.

STUDENTS = plural.

Смотрим на noun
после OF.""",
            },


            {
                "order": 5,
                "title":
                    "Decimals",

                "body":
                    """В английском decimal
обычно записывается через точку.

1.5
→ one point five

2.7
→ two point seven

3.14
→ three point one four

После POINT цифры
обычно читаются отдельно.

Не:

three point fourteen.""",
            },


            {
                "order": 6,
                "title":
                    "ZERO после POINT",

                "body":
                    """Нули после POINT
тоже читаются.

6.08

→ six point zero eight

0.125

→ zero point one two five

12.003

→ twelve point zero zero three

0.5 можно читать:

zero point five.""",
            },


            {
                "order": 7,
                "title":
                    "Percent",

                "body":
                    """Знак % читается:

per cent / percent.

5%
→ five per cent

25%
→ twenty-five per cent

100%
→ one hundred per cent

PERCENTAGE используется
без конкретного числа.

a high percentage

a small percentage.""",
            },


            {
                "order": 8,
                "title":
                    "BY и TO",

                "body":
                    """BY показывает,
НА СКОЛЬКО изменилось значение.

Sales increased by 10%.

= выросли на 10%.

TO показывает
НОВОЕ значение.

The rate increased to 10%.

= вырос до 10%.

BY ≠ TO.""",
            },


            {
                "order": 9,
                "title":
                    "FROM…TO",

                "body":
                    """FROM…TO показывает
начальное и конечное значения.

The rate increased
from 5% to 8%.

= вырос с 5% до 8%.

Другой пример:

Prices fell
from $20 to $15.

FROM = начало.

TO = результат.""",
            },


            {
                "order": 10,
                "title":
                    "Ratios и proportions",

                "body":
                    """Ratio:

3:2

→ three to two

4:1

→ four to one

One in five:

один из пяти.

One in five students...

Seven out of ten:

семь из десяти.

Seven out of ten
students passed.""",
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
                    "1/5 = ?",
                "options": [
                    "one fifth",
                    "one five",
                    "first five",
                    "one fifths",
                ],
                "answer":
                    "one fifth",
                "explanation":
                    "1/5 = ONE FIFTH.",
            },

            {
                "order": 2,
                "section": 1,
                "prompt":
                    "2/3 = ?",
                "options": [
                    "two thirds",
                    "two third",
                    "second thirds",
                    "two threes",
                ],
                "answer":
                    "two thirds",
                "explanation":
                    "Numerator больше 1 → denominator plural.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "prompt":
                    "1/2 = ?",
                "options": [
                    "one half",
                    "one second",
                    "one halves",
                    "half one",
                ],
                "answer":
                    "one half",
                "explanation":
                    "1/2 = ONE HALF.",
            },

            {
                "order": 4,
                "section": 2,
                "prompt":
                    "3/4 = ?",
                "options": [
                    "three quarters",
                    "three quarter",
                    "third quarters",
                    "three fourth one",
                ],
                "answer":
                    "three quarters",
                "explanation":
                    "3/4 = THREE QUARTERS.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "prompt":
                    "2 1/2 = ?",
                "options": [
                    "two and a half",
                    "two half",
                    "two point half",
                    "second and half",
                ],
                "answer":
                    "two and a half",
                "explanation":
                    "Mixed number → whole number + AND + fraction.",
            },

            {
                "order": 6,
                "section": 3,
                "prompt":
                    "3 1/4 = ?",
                "options": [
                    "three and a quarter",
                    "three quarter",
                    "third and one quarter",
                    "three point quarter",
                ],
                "answer":
                    "three and a quarter",
                "explanation":
                    "3 1/4 = THREE AND A QUARTER.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "prompt":
                    "Half of the work ___ finished.",
                "options": [
                    "is",
                    "are",
                    "were",
                    "have",
                ],
                "answer":
                    "is",
                "explanation":
                    "WORK = uncountable → singular verb.",
            },

            {
                "order": 8,
                "section": 4,
                "prompt":
                    "Half of the students ___ absent.",
                "options": [
                    "are",
                    "is",
                    "was",
                    "has",
                ],
                "answer":
                    "are",
                "explanation":
                    "STUDENTS = plural → ARE.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "prompt":
                    "3.14 = ?",
                "options": [
                    "three point one four",
                    "three point fourteen",
                    "three fourteen",
                    "three comma one four",
                ],
                "answer":
                    "three point one four",
                "explanation":
                    "После POINT цифры читаем отдельно.",
            },

            {
                "order": 10,
                "section": 5,
                "prompt":
                    "Choose the normal English decimal notation.",
                "options": [
                    "2.5",
                    "2,5",
                    "2:5",
                    "2/5",
                ],
                "answer":
                    "2.5",
                "explanation":
                    "В английской записи decimal separator — точка.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "prompt":
                    "6.08 = ?",
                "options": [
                    "six point zero eight",
                    "six point eight",
                    "six point eighty",
                    "six comma zero eight",
                ],
                "answer":
                    "six point zero eight",
                "explanation":
                    "ZERO после POINT нужно прочитать.",
            },

            {
                "order": 12,
                "section": 6,
                "prompt":
                    "0.125 = ?",
                "options": [
                    "zero point one two five",
                    "zero point one hundred twenty-five",
                    "one hundred twenty-five point zero",
                    "zero comma one two five",
                ],
                "answer":
                    "zero point one two five",
                "explanation":
                    "После POINT цифры читаются отдельно.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "prompt":
                    "75% = ?",
                "options": [
                    "seventy-five per cent",
                    "seventy-fifth per cent",
                    "seventy-five percentage",
                    "per cent seventy-five",
                ],
                "answer":
                    "seventy-five per cent",
                "explanation":
                    "Конкретное число + PER CENT.",
            },

            {
                "order": 14,
                "section": 7,
                "prompt":
                    "A high ___ of students passed.",
                "options": [
                    "percentage",
                    "per cent",
                    "percent number",
                    "percentages exactly",
                ],
                "answer":
                    "percentage",
                "explanation":
                    "Без конкретного числа используем PERCENTAGE.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "prompt":
                    "Sales increased ___ 10%.",
                "options": [
                    "by",
                    "to",
                    "from",
                    "at",
                ],
                "answer":
                    "by",
                "explanation":
                    "BY = величина изменения.",
            },

            {
                "order": 16,
                "section": 8,
                "prompt":
                    "The rate increased ___ 10%.",
                "options": [
                    "to",
                    "by",
                    "from",
                    "of",
                ],
                "answer":
                    "to",
                "explanation":
                    "TO = новое значение.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "prompt":
                    "The rate increased ___ 4% ___ 7%.",
                "options": [
                    "from / to",
                    "by / to",
                    "to / from",
                    "at / by",
                ],
                "answer":
                    "from / to",
                "explanation":
                    "Начальное и конечное значения → FROM…TO.",
            },

            {
                "order": 18,
                "section": 9,
                "prompt":
                    "Prices fell from $30 ___ $25.",
                "options": [
                    "to",
                    "by",
                    "from",
                    "of",
                ],
                "answer":
                    "to",
                "explanation":
                    "FROM $30 TO $25.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "prompt":
                    "4:1 is read:",
                "options": [
                    "four to one",
                    "four and one",
                    "four point one",
                    "one from four",
                ],
                "answer":
                    "four to one",
                "explanation":
                    "Ratio 4:1 → FOUR TO ONE.",
            },

            {
                "order": 20,
                "section": 10,
                "prompt":
                    "Seven out of ten students passed means:",
                "options": [
                    "7 из 10 студентов сдали",
                    "7 студентов из 100 сдали",
                    "10 из 7 студентов сдали",
                    "7% студентов сдали",
                ],
                "answer":
                    "7 из 10 студентов сдали",
                "explanation":
                    "SEVEN OUT OF TEN = семь из десяти.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "4/5 = ?",
                "options": [
                    "four fifths",
                    "four fifth",
                    "fourth five",
                    "four fives",
                ],
                "answer":
                    "four fifths",
                "explanation":
                    "Numerator > 1 → denominator plural.",
            },

            {
                "order": 22,
                "prompt":
                    "5 3/4 = ?",
                "options": [
                    "five and three quarters",
                    "five three quarter",
                    "fifth and three quarters",
                    "five point three quarters",
                ],
                "answer":
                    "five and three quarters",
                "explanation":
                    "Mixed number → FIVE AND THREE QUARTERS.",
            },

            {
                "order": 23,
                "prompt":
                    "Two thirds of the water ___ been used.",
                "options": [
                    "has",
                    "have",
                    "are",
                    "were",
                ],
                "answer":
                    "has",
                "explanation":
                    "WATER = uncountable → singular HAS.",
            },

            {
                "order": 24,
                "prompt":
                    "Two thirds of the employees ___ completed the training.",
                "options": [
                    "have",
                    "has",
                    "is",
                    "was",
                ],
                "answer":
                    "have",
                "explanation":
                    "EMPLOYEES = plural → HAVE.",
            },

            {
                "order": 25,
                "prompt":
                    "12.04 = ?",
                "options": [
                    "twelve point zero four",
                    "twelve point four",
                    "twelve point forty",
                    "twelve comma zero four",
                ],
                "answer":
                    "twelve point zero four",
                "explanation":
                    "После POINT читаем каждую цифру.",
            },

            {
                "order": 26,
                "prompt":
                    "40% = ?",
                "options": [
                    "forty per cent",
                    "fortieth per cent",
                    "forty percentage",
                    "per cent forty",
                ],
                "answer":
                    "forty per cent",
                "explanation":
                    "40% → FORTY PER CENT.",
            },

            {
                "order": 27,
                "prompt":
                    "Revenue increased ___ 8%. The 8% is the size of the change.",
                "options": [
                    "by",
                    "to",
                    "from",
                    "at",
                ],
                "answer":
                    "by",
                "explanation":
                    "BY показывает размер изменения.",
            },

            {
                "order": 28,
                "prompt":
                    "The unemployment rate fell ___ 7% ___ 5%.",
                "options": [
                    "from / to",
                    "by / to",
                    "to / from",
                    "from / by",
                ],
                "answer":
                    "from / to",
                "explanation":
                    "FROM = начальное значение; TO = конечное.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct PERCENT / PERCENTAGE pair.",
                "options": [
                    "twenty per cent / a high percentage",
                    "twenty percentage / a high per cent",
                    "twenty percentages / a high percent number",
                    "percentage twenty / per cent high",
                ],
                "answer":
                    "twenty per cent / a high percentage",
                "explanation":
                    "После конкретного числа → PER CENT; общее понятие → PERCENTAGE.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "1/2 → one half / 2/3 → two thirds / 2.75 → two point seven five / 25% → twenty-five per cent / 3:1 → three to one",
                    "1/2 → one second / 2/3 → two third / 2.75 → two point seventy-five / 25% → twenty-five percentage / 3:1 → three by one",
                    "1/2 → half one / 2/3 → second thirds / 2.75 → two comma seven five / 25% → per cent twenty-five / 3:1 → three and one",
                    "1/2 → first two / 2/3 → two three / 2.75 → two point seventy five / 25% → twenty-fifth per cent / 3:1 → one from three",
                ],
                "answer":
                    "1/2 → one half / 2/3 → two thirds / 2.75 → two point seven five / 25% → twenty-five per cent / 3:1 → three to one",
                "explanation":
                    "Это основные модели Fractions, Decimals, Percentages and Ratios.",
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
                "✅ Interactive A1 Lesson 60 seeded"
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
