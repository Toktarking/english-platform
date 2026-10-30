from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 60: "
        "Fractions and Decimals."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=60,
            defaults={
                "title": "Дробные и десятичные числительные",
                "slug": "fractions-decimals-percentages",
                "theory_text": (
                    "Fractions, decimals, percentages, "
                    "ratios and numerical changes."
                ),
                "estimated_minutes": 50,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое дроби",
                "body": """Дробь показывает часть целого.

Примеры:

1/2 — one half

1/3 — one third

3/4 — three quarters

2/5 — two fifths

В дроби 3/5:

3 — numerator, числитель.

5 — denominator, знаменатель.

Основное правило:

числитель читается количественным числительным;

знаменатель — порядковым.""",
            },

            {
                "order": 2,
                "title": "Основные дроби",
                "body": """Если числитель равен 1:

1/2 — one half

1/3 — one third

1/4 — one quarter

1/5 — one fifth

1/6 — one sixth

1/8 — one eighth

1/10 — one tenth

Особенно запомните:

1/2 → one half

1/4 → one quarter

Также возможно:

one fourth

Но one quarter употребляется очень часто.""",
            },

            {
                "order": 3,
                "title": "Числитель больше одного",
                "body": """Если числитель больше одного, знаменатель обычно ставится во множественное число.

Примеры:

2/3 — two thirds

3/4 — three quarters

4/5 — four fifths

7/10 — seven tenths

Сравните:

1/3 — one third

2/3 — two thirds

1/5 — one fifth

3/5 — three fifths

Не:

two third

Правильно:

two thirds""",
            },

            {
                "order": 4,
                "title": "HALF, QUARTER и OF",
                "body": """HALF:

1/2 — one half

Half of the students passed.

Также:

half the students

QUARTER:

1/4 — one quarter

3/4 — three quarters

A quarter of the students...

Three quarters of the population...

Частая модель:

fraction + of + noun

one third of the class

two thirds of the population

three quarters of the work""",
            },

            {
                "order": 5,
                "title": "Смешанные числа",
                "body": """Смешанное число содержит целую и дробную части.

Используется AND.

Примеры:

1 1/2 — one and a half

2 1/3 — two and one third

3 1/4 — three and a quarter

5 2/3 — five and two thirds

После one and a half существительное обычно plural:

one and a half hours

two and a half days

Также естественно:

an hour and a half""",
            },

            {
                "order": 6,
                "title": "Согласование после дробей",
                "body": """Глагол зависит от существительного после OF.

Неисчисляемое или singular:

Half of the work is finished.

Two thirds of the water has been used.

One quarter of the building was damaged.

Plural noun:

Half of the students are absent.

Two thirds of the students have passed.

One quarter of the employees were absent.

Смотрите не на дробь, а на существительное после OF.""",
            },

            {
                "order": 7,
                "title": "Десятичные дроби",
                "body": """В английском десятичные числа записываются через точку.

Правильно:

2.5

Не:

2,5

Точка читается:

point

Примеры:

1.5 — one point five

2.7 — two point seven

3.14 — three point one four

9.99 — nine point nine nine

После POINT цифры обычно читаются отдельно.""",
            },

            {
                "order": 8,
                "title": "ZERO и цифры после POINT",
                "body": """Примеры:

6.08 — six point zero eight

10.47 — ten point four seven

0.125 — zero point one two five

12.003 — twelve point zero zero three

Число 0.5 можно читать:

zero point five

или:

point five

Для учебных заданий безопаснее:

zero point five

В британском английском также встречается:

nought point five""",
            },

            {
                "order": 9,
                "title": "Десятичные числа с существительными",
                "body": """После decimal number, отличного от единицы, существительное обычно ставится во множественном числе.

Примеры:

1.5 kilometres

0.5 litres

2.5 kilograms

Большие значения:

2.5 million

1.2 billion

3.75 thousand

После точного числа:

million

billion

thousand

обычно остаются без -s.

Правильно:

2.5 million people

Не:

2.5 millions people""",
            },

            {
                "order": 10,
                "title": "Проценты",
                "body": """Знак % читается:

per cent / percent

Примеры:

5% — five per cent

20% — twenty per cent

75% — seventy-five per cent

100% — one hundred per cent

После конкретного числа используется:

per cent

Не:

twenty percentage

PERCENTAGE используется в общем смысле:

a high percentage

a small percentage

What percentage passed?""",
            },

            {
                "order": 11,
                "title": "BY, TO и FROM…TO",
                "body": """BY показывает величину изменения.

Sales increased by 10%.

= продажи выросли на 10%.

TO показывает новое значение.

The rate increased to 10%.

= показатель вырос до 10%.

FROM…TO показывает начальное и конечное значения.

The rate increased from 5% to 8%.

Важно:

by 10% → на 10%

to 10% → до 10%

from 5% to 8% → с 5% до 8%""",
            },

            {
                "order": 12,
                "title": "Процент и процентные пункты",
                "body": """Percentage points и percent — не одно и то же.

Если показатель вырос:

с 20% до 25%,

изменение составляет:

5 percentage points.

Относительный рост:

25%.

Для базового уровня важно различать:

increased by five per cent

increased by five percentage points

increased from twenty to twenty-five per cent.""",
            },

            {
                "order": 13,
                "title": "RATIO и пропорции",
                "body": """Соотношение 3:2 читается:

three to two

Пример:

The ratio of men to women was three to two.

ONE IN FIVE:

один из пяти.

One in five students works part-time.

TWO OUT OF TEN:

двое из десяти.

Two out of ten participants disagreed.

Также:

Seven out of ten students passed.""",
            },

            {
                "order": 14,
                "title": "Главный алгоритм",
                "body": """Обычная дробь?

Числитель → cardinal number.

Знаменатель → ordinal number.

Если числитель больше 1:

знаменатель → plural.

2/3 → two thirds.

Смешанное число?

Используйте AND:

2 1/2 → two and a half.

Decimal?

Используйте POINT и читайте цифры отдельно:

2.75 → two point seven five.

Процент?

25% → twenty-five per cent.

Изменение?

BY → на

TO → до

FROM…TO → с…до

Ratio?

3:2 → three to two.""",
            },

        ]

        for data in sections:
            GrammarLessonSection.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "title": data["title"],
                    "body": data["body"],
                },
            )

        exercises = [

            {
                "order": 1,
                "prompt": "1/5:",
                "options": [
                    "one five",
                    "one fifth",
                    "first five",
                    "one five-th",
                ],
                "answer": "one fifth",
                "explanation": (
                    "Числитель cardinal, знаменатель ordinal."
                ),
            },

            {
                "order": 2,
                "prompt": "4/7:",
                "options": [
                    "four seventh",
                    "four sevenths",
                    "fourth seven",
                    "four sevens",
                ],
                "answer": "four sevenths",
                "explanation": (
                    "Числитель больше одного → denominator plural."
                ),
            },

            {
                "order": 3,
                "prompt": "1/4:",
                "options": [
                    "one quarter",
                    "one quarters",
                    "first quarter only as time",
                    "one fourths",
                ],
                "answer": "one quarter",
                "explanation": (
                    "1/4 обычно читается one quarter."
                ),
            },

            {
                "order": 4,
                "prompt": "5 1/2:",
                "options": [
                    "five and a half",
                    "five half",
                    "fifth and half",
                    "five point half",
                ],
                "answer": "five and a half",
                "explanation": (
                    "В mixed number используется and."
                ),
            },

            {
                "order": 5,
                "prompt": "6.09:",
                "options": [
                    "six point nine",
                    "six point zero nine",
                    "six point ninety",
                    "six comma zero nine",
                ],
                "answer": "six point zero nine",
                "explanation": (
                    "После point цифры читаются отдельно."
                ),
            },

            {
                "order": 6,
                "prompt": "0.125:",
                "options": [
                    "zero point one two five",
                    "zero point one hundred twenty-five",
                    "one hundred twenty-five point zero",
                    "zero comma one two five",
                ],
                "answer": "zero point one two five",
                "explanation": (
                    "Decimal digits после point читаются отдельно."
                ),
            },

            {
                "order": 7,
                "prompt": "75%:",
                "options": [
                    "seventy-five per cent",
                    "seventy-fifth per cent",
                    "seventy-five percentages",
                    "per cent seventy-five",
                ],
                "answer": "seventy-five per cent",
                "explanation": (
                    "После конкретного числа используется per cent."
                ),
            },

            {
                "order": 8,
                "prompt": "A high ___ of students passed.",
                "options": [
                    "per cent",
                    "percentage",
                    "percentages exactly",
                    "percent number",
                ],
                "answer": "percentage",
                "explanation": (
                    "Без конкретного числа: a high percentage."
                ),
            },

            {
                "order": 9,
                "prompt": "Sales increased ___ ten per cent.",
                "options": [
                    "to",
                    "by",
                    "from",
                    "at",
                ],
                "answer": "by",
                "explanation": (
                    "BY показывает величину изменения."
                ),
            },

            {
                "order": 10,
                "prompt": "The rate increased ___ 5% ___ 8%.",
                "options": [
                    "by / to",
                    "from / to",
                    "at / from",
                    "to / by",
                ],
                "answer": "from / to",
                "explanation": (
                    "Начальное и конечное значения → from...to."
                ),
            },

            {
                "order": 11,
                "prompt": "Half of the work ___ complete.",
                "options": [
                    "are",
                    "is",
                    "were",
                    "have",
                ],
                "answer": "is",
                "explanation": (
                    "Work неисчисляемое → singular verb."
                ),
            },

            {
                "order": 12,
                "prompt": "Half of the students ___ absent.",
                "options": [
                    "is",
                    "are",
                    "was",
                    "has",
                ],
                "answer": "are",
                "explanation": (
                    "Students plural → are."
                ),
            },

            {
                "order": 13,
                "prompt": "One in five students ___ part-time.",
                "options": [
                    "work",
                    "works",
                    "working",
                    "have worked always",
                ],
                "answer": "works",
                "explanation": (
                    "One in five students = one student out of every five."
                ),
            },

            {
                "order": 14,
                "prompt": "2.5 million:",
                "options": [
                    "two point five millions",
                    "two point five million",
                    "two and five million",
                    "two fifth million",
                ],
                "answer": "two point five million",
                "explanation": (
                    "После точного числа million не получает -s."
                ),
            },

            {
                "order": 15,
                "prompt": "At least 30% means:",
                "options": [
                    "не более 30%",
                    "ровно 30%",
                    "не менее 30%",
                    "около 30% обязательно",
                ],
                "answer": "не менее 30%",
                "explanation": (
                    "At least = не менее."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct reading of 3/4.",
                "options": [
                    "three quarter",
                    "three quarters",
                    "third quarters",
                    "three fourth one",
                ],
                "answer": "three quarters",
                "explanation": (
                    "3/4 = three quarters."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct reading of 3.14.",
                "options": [
                    "three point fourteen",
                    "three point one four",
                    "three fourteen",
                    "three comma one four",
                ],
                "answer": "three point one four",
                "explanation": (
                    "После point цифры читаются отдельно."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct decimal notation in English.",
                "options": [
                    "2,5",
                    "2.5",
                    "2:5",
                    "2/5 for decimal",
                ],
                "answer": "2.5",
                "explanation": (
                    "В английской записи decimal separator — точка."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct mixed-number phrase.",
                "options": [
                    "one and a half hour",
                    "one and a half hours",
                    "one half and hour",
                    "one and half hours",
                ],
                "answer": "one and a half hours",
                "explanation": (
                    "После one and a half обычно plural noun."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the correct ratio reading for 4:1.",
                "options": [
                    "four and one",
                    "four to one",
                    "four point one",
                    "one from four",
                ],
                "answer": "four to one",
                "explanation": (
                    "Ratio 4:1 → four to one."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct PERCENT / PERCENTAGE pair.",
                "options": [
                    (
                        "twenty per cent / "
                        "a high percentage"
                    ),
                    (
                        "twenty percentage / "
                        "a high per cent"
                    ),
                    (
                        "twenty percentages / "
                        "a high percent number"
                    ),
                    (
                        "percentage twenty / "
                        "per cent high"
                    ),
                ],
                "answer": (
                    "twenty per cent / "
                    "a high percentage"
                ),
                "explanation": (
                    "После числа → per cent; "
                    "общее значение → percentage."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct BY / TO meaning pair.",
                "options": [
                    (
                        "increase by 5% = increase на 5% / "
                        "increase to 5% = increase до 5%"
                    ),
                    (
                        "increase by 5% = increase до 5% / "
                        "increase to 5% = increase на 5%"
                    ),
                    (
                        "by and to always mean the same",
                    ),
                    (
                        "by is only for time / to is only for place",
                    ),
                ],
                "answer": (
                    "increase by 5% = increase на 5% / "
                    "increase to 5% = increase до 5%"
                ),
                "explanation": (
                    "BY = величина изменения; TO = новое значение."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct fraction/agreement pair.",
                "options": [
                    (
                        "Two thirds of the work is complete. / "
                        "Two thirds of the students are ready."
                    ),
                    (
                        "Two thirds of the work are complete. / "
                        "Two thirds of the students is ready."
                    ),
                    (
                        "Two third of the work is complete. / "
                        "Two third of the students are ready."
                    ),
                    (
                        "Two thirds of the work be complete. / "
                        "Two thirds of the students be ready."
                    ),
                ],
                "answer": (
                    "Two thirds of the work is complete. / "
                    "Two thirds of the students are ready."
                ),
                "explanation": (
                    "Verb agreement зависит от noun после OF."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "1/2 → one half / "
                        "2/3 → two thirds / "
                        "2 1/2 → two and a half / "
                        "2.75 → two point seven five / "
                        "25% → twenty-five per cent / "
                        "3:1 → three to one"
                    ),
                    (
                        "1/2 → one second / "
                        "2/3 → two third / "
                        "2 1/2 → two point half / "
                        "2.75 → two point seventy-five / "
                        "25% → twenty-five percentage / "
                        "3:1 → three by one"
                    ),
                    (
                        "1/2 → half one / "
                        "2/3 → second thirds / "
                        "2 1/2 → second and half / "
                        "2.75 → two comma seven five / "
                        "25% → per cent twenty-five / "
                        "3:1 → three and one"
                    ),
                    (
                        "1/2 → first two / "
                        "2/3 → two three / "
                        "2 1/2 → two halves / "
                        "2.75 → two point seventy five / "
                        "25% → twenty-fifth per cent / "
                        "3:1 → one from three"
                    ),
                ],
                "answer": (
                    "1/2 → one half / "
                    "2/3 → two thirds / "
                    "2 1/2 → two and a half / "
                    "2.75 → two point seven five / "
                    "25% → twenty-five per cent / "
                    "3:1 → three to one"
                ),
                "explanation": (
                    "Это основные модели fractions, decimals, "
                    "percentages и ratios."
                ),
            },

        ]

        for data in exercises:
            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "exercise_type": GrammarExercise.Type.CHOICE,
                    "prompt": data["prompt"],
                    "options": data["options"],
                    "correct_answer": data["answer"],
                    "explanation": data["explanation"],
                    "is_published": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ A1 Lesson 60 seeded: Fractions and Decimals"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
