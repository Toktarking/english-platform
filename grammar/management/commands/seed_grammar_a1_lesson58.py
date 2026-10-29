from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 58: "
        "Cardinal Numbers."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=58,
            defaults={
                "title": "Количественные числительные",
                "slug": "cardinal-numbers",
                "theory_text": (
                    "Cardinal numbers: numbers, quantities, "
                    "age, money and large numbers."
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
                "title": "Что такое количественные числительные",
                "body": """Количественные числительные отвечают на вопрос:

сколько?

По-английски:

How many?

How much?

Примеры:

one student

two books

ten people

one hundred dollars

three thousand kilometres

Они используются для количества, возраста, денег, расстояния, статистики и других числовых значений.""",
            },

            {
                "order": 2,
                "title": "Числа от 0 до 19",
                "body": """Основные числа:

0 — zero

1 — one

2 — two

3 — three

4 — four

5 — five

6 — six

7 — seven

8 — eight

9 — nine

10 — ten

Особые формы нужно запомнить:

11 — eleven

12 — twelve

13 — thirteen

15 — fifteen

18 — eighteen

Не:

fiveteen

Правильно:

fifteen""",
            },

            {
                "order": 3,
                "title": "Десятки и числа 21–99",
                "body": """Десятки:

20 — twenty

30 — thirty

40 — forty

50 — fifty

60 — sixty

70 — seventy

80 — eighty

90 — ninety

Особенно запомните:

forty

не fourty.

Числа от 21 до 99 обычно пишутся через дефис:

twenty-one

thirty-seven

forty-five

ninety-nine""",
            },

            {
                "order": 4,
                "title": "13 и 30: не путайте",
                "body": """Важно различать:

thirteen — 13

thirty — 30

fourteen — 14

forty — 40

fifteen — 15

fifty — 50

sixteen — 16

sixty — 60

В числах 13–19 ударение часто падает на последний слог:

thirTEEN

fifTEEN

В десятках чаще на первый:

THIRty

FIFty""",
            },

            {
                "order": 5,
                "title": "HUNDRED",
                "body": """Примеры:

100 — one hundred

200 — two hundred

500 — five hundred

После точного числа HUNDRED не получает -s.

Правильно:

three hundred students

Не:

three hundreds students

В британском английском часто используется AND:

125

one hundred and twenty-five

406

four hundred and six""",
            },

            {
                "order": 6,
                "title": "THOUSAND, MILLION, BILLION",
                "body": """После точного числа:

thousand

million

billion

не получают окончание -s.

Правильно:

two thousand

three million

five billion

Не:

two thousands

three millions

Примеры:

5,200

five thousand two hundred

12,450

twelve thousand four hundred and fifty

3,000,000

three million""",
            },

            {
                "order": 7,
                "title": "HUNDREDS OF и THOUSANDS OF",
                "body": """Если точное количество НЕ указано, используются:

hundreds of

thousands of

millions of

billions of

Примеры:

Hundreds of people attended.

Thousands of students applied.

Millions of dollars were spent.

Сравните:

two hundred students
— точное количество

hundreds of students
— приблизительно большое количество

Не:

two hundreds of students""",
            },

            {
                "order": 8,
                "title": "Как читать большие числа",
                "body": """Большое число удобно делить справа налево на группы по три цифры.

Пример:

12,345,678

12 million

345 thousand

678

Читаем:

twelve million three hundred and forty-five thousand six hundred and seventy-eight

Другие примеры:

1,250

one thousand two hundred and fifty

25,600

twenty-five thousand six hundred""",
            },

            {
                "order": 9,
                "title": "Возраст",
                "body": """Для возраста используется:

be + number + years old

Примеры:

I am twenty-eight years old.

She is ten years old.

He is thirty-two years old.

Можно короче:

She is ten.

Перед существительным возраст становится compound adjective:

a ten-year-old child

a twenty-year-old student

Важно:

year остаётся в единственном числе.

Не:

a ten-years-old child""",
            },

            {
                "order": 10,
                "title": "Деньги, телефоны и номера",
                "body": """Деньги:

five dollars

ten euros

two thousand tenge

$5.50:

five dollars fifty

или:

five dollars and fifty cents

Телефонные номера обычно читаются по цифрам:

205

two zero five

или:

two oh five

Также возможно:

double

700455

seven double zero four double five

Номера автобусов и комнат могут читаться по-разному:

bus 205

bus two oh five""",
            },

            {
                "order": 11,
                "title": "Годы, время и температура",
                "body": """Годы часто читаются особым образом:

1998 — nineteen ninety-eight

2000 — two thousand

2005 — two thousand and five

2010 — twenty ten

2026 — twenty twenty-six

Время:

3:15 — three fifteen

7:30 — seven thirty

Температура:

20°C — twenty degrees Celsius

-5°C — minus five degrees""",
            },

            {
                "order": 12,
                "title": "HOW MANY и HOW MUCH",
                "body": """HOW MANY используется с исчисляемыми существительными:

How many students are there?

How many books did you buy?

HOW MUCH используется:

с неисчисляемыми существительными;

для цены.

Примеры:

How much money do you need?

How much water do you drink?

How much is this book?

Также:

number → countable nouns

amount → uncountable nouns""",
            },

            {
                "order": 13,
                "title": "A NUMBER OF и THE NUMBER OF",
                "body": """A NUMBER OF означает:

несколько;

ряд;

некоторое количество.

После него plural noun и обычно plural verb:

A number of students were absent.

THE NUMBER OF означает:

количество.

Глагол обычно в единственном числе:

The number of students is increasing.

Сравните:

A number of students were...

The number of students is...""",
            },

            {
                "order": 14,
                "title": "Главный алгоритм",
                "body": """Проверьте:

1. Это точное число?

После hundred/thousand/million/billion нет -s:

five thousand

two million

2. Количество неточное?

Используйте:

hundreds of

thousands of

millions of

3. Число 21–99?

Используйте дефис:

twenty-five

4. Возраст после BE?

twenty years old

5. Возраст перед noun?

a twenty-year-old student

6. A number of?

plural verb

7. The number of?

singular verb""",
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
                "prompt": "Как правильно пишется число 15?",
                "options": [
                    "fiveteen",
                    "fifteen",
                    "fiftyeen",
                    "fivteen",
                ],
                "answer": "fifteen",
                "explanation": "15 = fifteen.",
            },

            {
                "order": 2,
                "prompt": "Как правильно пишется число 80?",
                "options": [
                    "eightty",
                    "eighty",
                    "eigty",
                    "eighti",
                ],
                "answer": "eighty",
                "explanation": "80 = eighty.",
            },

            {
                "order": 3,
                "prompt": "37:",
                "options": [
                    "thirty-seven",
                    "thirteen-seven",
                    "thirty seven",
                    "three-seven",
                ],
                "answer": "thirty-seven",
                "explanation": (
                    "Составные числа 21–99 обычно пишутся через дефис."
                ),
            },

            {
                "order": 4,
                "prompt": "406:",
                "options": [
                    "four hundred and six",
                    "four hundreds six",
                    "four hundred sixes",
                    "four thousands and six",
                ],
                "answer": "four hundred and six",
                "explanation": (
                    "После точного числа hundred остаётся без -s."
                ),
            },

            {
                "order": 5,
                "prompt": "5,200:",
                "options": [
                    "five thousands two hundred",
                    "five thousand two hundred",
                    "five thousand and two hundreds",
                    "five millions two hundred",
                ],
                "answer": "five thousand two hundred",
                "explanation": (
                    "После five используется thousand без -s."
                ),
            },

            {
                "order": 6,
                "prompt": "12,450:",
                "options": [
                    "twelve thousand four hundred and fifty",
                    "twelve thousands four hundreds fifty",
                    "one two four five zero",
                    "twelve million four hundred fifty",
                ],
                "answer": "twelve thousand four hundred and fifty",
                "explanation": (
                    "Правильное чтение большого числа."
                ),
            },

            {
                "order": 7,
                "prompt": "3,000,000:",
                "options": [
                    "three millions",
                    "three million",
                    "three million of",
                    "millions three",
                ],
                "answer": "three million",
                "explanation": (
                    "После точного числа million не получает -s."
                ),
            },

            {
                "order": 8,
                "prompt": "___ of students use the library.",
                "options": [
                    "Thousand",
                    "Thousands",
                    "Three thousands",
                    "Thousand of",
                ],
                "answer": "Thousands",
                "explanation": (
                    "Неточное большое количество → thousands of."
                ),
            },

            {
                "order": 9,
                "prompt": "The university has ___ students.",
                "options": [
                    "ten thousands",
                    "ten thousand",
                    "ten thousand of",
                    "ten-thousands",
                ],
                "answer": "ten thousand",
                "explanation": (
                    "Точное число → ten thousand без -s."
                ),
            },

            {
                "order": 10,
                "prompt": "She is a ___ girl.",
                "options": [
                    "six-years-old",
                    "six-year-old",
                    "six years old",
                    "six-years old",
                ],
                "answer": "six-year-old",
                "explanation": (
                    "Перед noun: number-year-old; year остаётся singular."
                ),
            },

            {
                "order": 11,
                "prompt": "The girl is ___.",
                "options": [
                    "six-year-old",
                    "six years old",
                    "six-years-old",
                    "six year olds",
                ],
                "answer": "six years old",
                "explanation": (
                    "После BE: six years old."
                ),
            },

            {
                "order": 12,
                "prompt": "Ten kilometres ___ a long distance to walk.",
                "options": [
                    "are",
                    "is",
                    "be",
                    "were always",
                ],
                "answer": "is",
                "explanation": (
                    "Расстояние воспринимается как единое количество."
                ),
            },

            {
                "order": 13,
                "prompt": "A number of students ___ absent.",
                "options": [
                    "was",
                    "were",
                    "is",
                    "has",
                ],
                "answer": "were",
                "explanation": (
                    "A number of + plural noun → plural verb."
                ),
            },

            {
                "order": 14,
                "prompt": "The number of students ___ increasing.",
                "options": [
                    "are",
                    "is",
                    "were",
                    "have",
                ],
                "answer": "is",
                "explanation": (
                    "The number of = количество → singular verb."
                ),
            },

            {
                "order": 15,
                "prompt": "2 × 8 = 16",
                "options": [
                    "Two plus eight equals sixteen.",
                    "Two times eight equals sixteen.",
                    "Two divided by eight equals sixteen.",
                    "Two minus eight equals sixteen.",
                ],
                "answer": "Two times eight equals sixteen.",
                "explanation": (
                    "× читается times или multiplied by."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct spelling.",
                "options": [
                    "fourty",
                    "forty",
                    "fourti",
                    "fourtye",
                ],
                "answer": "forty",
                "explanation": "40 = forty, не fourty.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct exact-number phrase.",
                "options": [
                    "three hundreds students",
                    "three hundred students",
                    "three hundreds of students",
                    "three hundred of students",
                ],
                "answer": "three hundred students",
                "explanation": (
                    "После точного числа hundred без -s и без of."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct approximate phrase.",
                "options": [
                    "thousands people",
                    "thousands of people",
                    "three thousands people",
                    "thousand of people",
                ],
                "answer": "thousands of people",
                "explanation": (
                    "Неточное количество → thousands of."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct age pair.",
                "options": [
                    (
                        "She is twenty years old. / "
                        "She is a twenty-year-old student."
                    ),
                    (
                        "She has twenty years. / "
                        "She is a twenty-years-old student."
                    ),
                    (
                        "She is twenty-year-old. / "
                        "She is a twenty years old student."
                    ),
                    (
                        "She has twenty years old. / "
                        "She is twenty-years student."
                    ),
                ],
                "answer": (
                    "She is twenty years old. / "
                    "She is a twenty-year-old student."
                ),
                "explanation": (
                    "После BE → years old; перед noun → year-old."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the correct HOW MANY / HOW MUCH pair.",
                "options": [
                    (
                        "How many students? / "
                        "How much money?"
                    ),
                    (
                        "How much students? / "
                        "How many money?"
                    ),
                    (
                        "How many water? / "
                        "How much books?"
                    ),
                    (
                        "How much people? / "
                        "How many information?"
                    ),
                ],
                "answer": (
                    "How many students? / "
                    "How much money?"
                ),
                "explanation": (
                    "Many → countable; much → uncountable."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct NUMBER / AMOUNT pair.",
                "options": [
                    (
                        "the number of students / "
                        "the amount of information"
                    ),
                    (
                        "the amount of students / "
                        "the number of information"
                    ),
                    (
                        "the number of water / "
                        "the amount of books"
                    ),
                    (
                        "the amount of people / "
                        "the number of money"
                    ),
                ],
                "answer": (
                    "the number of students / "
                    "the amount of information"
                ),
                "explanation": (
                    "Number → countable; amount → uncountable."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct year reading.",
                "options": [
                    "2026 — twenty twenty-six",
                    "2026 — two zero two six only",
                    "2026 — twenty hundreds twenty-six",
                    "2026 — two thousands twenty-six only",
                ],
                "answer": "2026 — twenty twenty-six",
                "explanation": (
                    "Годы 2010+ часто читаются как twenty + number."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct exact/approximate pair.",
                "options": [
                    (
                        "five million dollars / "
                        "millions of dollars"
                    ),
                    (
                        "five millions dollars / "
                        "million of dollars"
                    ),
                    (
                        "five million of dollars / "
                        "millions dollars"
                    ),
                    (
                        "five millions of dollars / "
                        "million dollars approximately"
                    ),
                ],
                "answer": (
                    "five million dollars / "
                    "millions of dollars"
                ),
                "explanation": (
                    "Точное число → million; "
                    "неточное количество → millions of."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "40 → forty / "
                        "25 → twenty-five / "
                        "300 → three hundred / "
                        "5,000 → five thousand / "
                        "2,000,000 → two million / "
                        "approximate → thousands of"
                    ),
                    (
                        "40 → fourty / "
                        "25 → twenty five always / "
                        "300 → three hundreds / "
                        "5,000 → five thousands / "
                        "2,000,000 → two millions / "
                        "approximate → thousand people"
                    ),
                    (
                        "40 → fourty / "
                        "25 → twenty-five / "
                        "300 → three hundred of / "
                        "5,000 → five thousand of / "
                        "2,000,000 → two millions / "
                        "approximate → three thousands"
                    ),
                    (
                        "40 → forty / "
                        "25 → twentyfifth / "
                        "300 → three hundreds / "
                        "5,000 → five-thousand / "
                        "2,000,000 → two million of / "
                        "approximate → thousands people"
                    ),
                ],
                "answer": (
                    "40 → forty / "
                    "25 → twenty-five / "
                    "300 → three hundred / "
                    "5,000 → five thousand / "
                    "2,000,000 → two million / "
                    "approximate → thousands of"
                ),
                "explanation": (
                    "Это основные правила написания "
                    "и употребления cardinal numbers."
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
                "✅ A1 Lesson 58 seeded: Cardinal Numbers"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
