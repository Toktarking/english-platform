from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 59: "
        "Ordinal Numbers and Dates."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=59,
            defaults={
                "title": "Порядковые числительные и даты",
                "slug": "ordinal-numbers-and-dates",
                "theory_text": (
                    "Ordinal numbers, dates, years, centuries "
                    "and sequence expressions."
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
                "title": "Что такое порядковые числительные",
                "body": """Порядковые числительные показывают место в последовательности.

Они отвечают на вопрос:

который по счёту?

Примеры:

the first lesson

the second student

the third floor

the twenty-first century

Сравните:

one, two, three
— количество

first, second, third
— порядок""",
            },

            {
                "order": 2,
                "title": "Основные формы",
                "body": """Первые формы нужно запомнить:

1 — first

2 — second

3 — third

4 — fourth

5 — fifth

6 — sixth

7 — seventh

8 — eighth

9 — ninth

10 — tenth

12 — twelfth

Особенно важны:

first

second

third

fifth

eighth

ninth

twelfth""",
            },

            {
                "order": 3,
                "title": "Десятки и составные формы",
                "body": """Если число заканчивается на -y:

-y → -ieth

20 — twentieth

30 — thirtieth

40 — fortieth

90 — ninetieth

В составном числе меняется только последняя часть:

21st — twenty-first

22nd — twenty-second

23rd — twenty-third

24th — twenty-fourth

42nd — forty-second

Не:

twentieth-first""",
            },

            {
                "order": 4,
                "title": "Окончания ST, ND, RD, TH",
                "body": """Основные сокращения:

1st

2nd

3rd

4th

Обычно:

числа на 1 → st

числа на 2 → nd

числа на 3 → rd

остальные → th

Но есть исключения:

11th

12th

13th

Не:

11st

12nd

13rd""",
            },

            {
                "order": 5,
                "title": "Артикль THE",
                "body": """Перед порядковыми числительными обычно используется THE.

Примеры:

the first lesson

the second chapter

the third student

the twenty-first century

Но если уже есть притяжательное слово:

my

your

his

her

our

their

THE не нужен.

Правильно:

my first job

her second child

Не:

my the first job""",
            },

            {
                "order": 6,
                "title": "FIRST, AT FIRST и THE FIRST",
                "body": """FIRST может означать:

сначала;

первым делом.

First, read the instructions.

AT FIRST означает:

сначала;

поначалу.

At first, I didn't understand the rule.

Обычно потом ситуация изменилась.

THE FIRST — порядковое числительное:

She was the first person to arrive.

Сравните:

First, open the file.

At first, the task seemed difficult.

She was the first student.""",
            },

            {
                "order": 7,
                "title": "NEXT / THE NEXT и LAST / THE LAST",
                "body": """NEXT без THE часто означает следующий по времени:

next week

next year

next Monday

THE NEXT — следующий элемент:

the next chapter

the next student

over the next three days

LAST без THE:

last week

last year

THE LAST:

the last question

the last chapter

the last student""",
            },

            {
                "order": 8,
                "title": "Как писать и читать даты",
                "body": """Британский порядок:

day + month + year

15 July 2026

Чтение:

the fifteenth of July

1 May:

the first of May

22 October:

the twenty-second of October

Американский порядок:

month + day + year

July 15, 2026

Чтение:

July fifteenth""",
            },

            {
                "order": 9,
                "title": "ON и IN с датами",
                "body": """С конкретным днём или датой используется ON:

on Monday

on 15 July

on the first of May

on July 15

С месяцем используется IN:

in July

in September

С годом:

in 2026

in 1998

С месяцем и годом:

in July 2026

Не:

in 15 July

Не:

on 2026""",
            },

            {
                "order": 10,
                "title": "Как читать годы",
                "body": """Годы до 2000 часто читаются парами:

1984 — nineteen eighty-four

1998 — nineteen ninety-eight

2000:

two thousand

2005:

two thousand and five

После 2010 часто возможны два варианта:

2026

twenty twenty-six

или:

two thousand and twenty-six

Первый вариант часто звучит естественнее.""",
            },

            {
                "order": 11,
                "title": "Века и десятилетия",
                "body": """Примеры веков:

1700s → the eighteenth century

1800s → the nineteenth century

1900s → the twentieth century

2000s → the twenty-first century

Десятилетия:

the 1960s

the 1990s

the 2020s

Важно:

апостроф не нужен.

Правильно:

the 1990s

Не:

the 1990's""",
            },

            {
                "order": 12,
                "title": "Возрастные периоды и годовщины",
                "body": """Возрастной период:

in his twenties

= от 20 до 29 лет.

Примеры:

She became a manager in her thirties.

He is in his sixties.

Дни рождения:

her thirtieth birthday

his eighteenth birthday

Годовщины:

their tenth wedding anniversary

the company's fiftieth anniversary""",
            },

            {
                "order": 13,
                "title": "Монархи, главы и события",
                "body": """Имена монархов читаются с порядковым числительным:

Elizabeth II

→ Elizabeth the Second

Henry VIII

→ Henry the Eighth

С событиями:

the First World War

the Fourth Industrial Revolution

С главами и уроками возможны два варианта:

Chapter Five

the fifth chapter

Lesson Ten

the tenth lesson""",
            },

            {
                "order": 14,
                "title": "THE FIRST TIME и главный алгоритм",
                "body": """Частая конструкция:

This is the first time + Present Perfect

Пример:

This is the first time I have visited London.

С прошлым:

It was the first time + Past Perfect

It was the first time I had travelled abroad.

Главный алгоритм:

количество?

→ cardinal number: one, two, three

место в последовательности?

→ ordinal number: first, second, third

конкретная дата?

→ ON

месяц или год?

→ IN

век?

→ ordinal number + century""",
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
                "prompt": "She was the ___ person to arrive.",
                "options": [
                    "one",
                    "first",
                    "oneth",
                    "once",
                ],
                "answer": "first",
                "explanation": (
                    "1st = first."
                ),
            },

            {
                "order": 2,
                "prompt": "This is my ___ visit to London.",
                "options": [
                    "two",
                    "second",
                    "twice",
                    "twoth",
                ],
                "answer": "second",
                "explanation": (
                    "Порядок → second."
                ),
            },

            {
                "order": 3,
                "prompt": "He finished ___ in the competition.",
                "options": [
                    "three",
                    "third",
                    "threeth",
                    "thirty",
                ],
                "answer": "third",
                "explanation": (
                    "3rd = third."
                ),
            },

            {
                "order": 4,
                "prompt": "The office is on the ___ floor.",
                "options": [
                    "five",
                    "fifth",
                    "fiveth",
                    "fiftieth",
                ],
                "answer": "fifth",
                "explanation": (
                    "5th = fifth."
                ),
            },

            {
                "order": 5,
                "prompt": "Her birthday is ___ 7 March.",
                "options": [
                    "in",
                    "on",
                    "at",
                    "by",
                ],
                "answer": "on",
                "explanation": (
                    "С конкретной датой используется on."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "The conference took place ___ March 2026."
                ),
                "options": [
                    "on",
                    "in",
                    "at",
                    "for",
                ],
                "answer": "in",
                "explanation": (
                    "С месяцем и годом используется in."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "The university was founded ___ 1972."
                ),
                "options": [
                    "on",
                    "at",
                    "in",
                    "since",
                ],
                "answer": "in",
                "explanation": (
                    "С годом используется in."
                ),
            },

            {
                "order": 8,
                "prompt": "The date 21 June is read:",
                "options": [
                    "the twenty-one of June",
                    "the twenty-first of June",
                    "June twenty-one-th",
                    "the twentieth-first of June",
                ],
                "answer": "the twenty-first of June",
                "explanation": (
                    "21st = twenty-first."
                ),
            },

            {
                "order": 9,
                "prompt": "The year 1998 is commonly read:",
                "options": [
                    "one thousand nine hundred ninety-eight only",
                    "nineteen ninety-eight",
                    "nineteen hundred ninety and eight",
                    "ninety-eight nineteen",
                ],
                "answer": "nineteen ninety-eight",
                "explanation": (
                    "Годы до 2000 часто читаются парами."
                ),
            },

            {
                "order": 10,
                "prompt": "The year 2026 can be read:",
                "options": [
                    "twenty twenty-six",
                    "two zero two six only",
                    "twenty-six twenty",
                    "two hundred twenty-six",
                ],
                "answer": "twenty twenty-six",
                "explanation": (
                    "2026 часто читается twenty twenty-six."
                ),
            },

            {
                "order": 11,
                "prompt": "The 1800s are:",
                "options": [
                    "the eighteenth century",
                    "the nineteenth century",
                    "the twentieth century",
                    "the seventeenth century",
                ],
                "answer": "the nineteenth century",
                "explanation": (
                    "1800-е относятся к nineteenth century."
                ),
            },

            {
                "order": 12,
                "prompt": "The 2000s belong to:",
                "options": [
                    "the twentieth century",
                    "the twenty-first century",
                    "the nineteenth century",
                    "the twenty-second century",
                ],
                "answer": "the twenty-first century",
                "explanation": (
                    "2000-е относятся к twenty-first century."
                ),
            },

            {
                "order": 13,
                "prompt": "The decade 1980–1989 is:",
                "options": [
                    "the nineteen eighties",
                    "the nineteen eighty",
                    "the eighteen nineties",
                    "the 1980's",
                ],
                "answer": "the nineteen eighties",
                "explanation": (
                    "1980s = the nineteen eighties."
                ),
            },

            {
                "order": 14,
                "prompt": "Henry VIII is read:",
                "options": [
                    "Henry Eight",
                    "Henry the Eighth",
                    "Henry Eightieth",
                    "Henry the Eight",
                ],
                "answer": "Henry the Eighth",
                "explanation": (
                    "Имена монархов читаются с ordinal number."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "This is the first time I ___ this city."
                ),
                "options": [
                    "visit",
                    "visited",
                    "have visited",
                    "had visit",
                ],
                "answer": "have visited",
                "explanation": (
                    "This is the first time + Present Perfect."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct form of 12th.",
                "options": [
                    "twelveth",
                    "twelfth",
                    "twelve-th",
                    "twelveth",
                ],
                "answer": "twelfth",
                "explanation": (
                    "12th = twelfth."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct form of 42nd.",
                "options": [
                    "forty-twoth",
                    "fortieth-two",
                    "forty-second",
                    "fourty-second",
                ],
                "answer": "forty-second",
                "explanation": (
                    "В составном ordinal меняется только последняя часть."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct abbreviation.",
                "options": [
                    "11st",
                    "11th",
                    "11rd",
                    "11nd",
                ],
                "answer": "11th",
                "explanation": (
                    "11, 12 и 13 — исключения: th."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "This is my the first job.",
                    "This is my first job.",
                    "This is the my first job.",
                    "This is my one job.",
                ],
                "answer": "This is my first job.",
                "explanation": (
                    "После притяжательного слова THE не нужен."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the correct FIRST / AT FIRST pair.",
                "options": [
                    (
                        "First, read the text. / "
                        "At first, I didn't understand it."
                    ),
                    (
                        "At first, read the text. / "
                        "First, I didn't understand it, but later I did."
                    ),
                    (
                        "The first, read the text. / "
                        "At first time, I didn't understand."
                    ),
                    (
                        "First, I didn't understand but later. / "
                        "At first, read the text."
                    ),
                ],
                "answer": (
                    "First, read the text. / "
                    "At first, I didn't understand it."
                ),
                "explanation": (
                    "First = первое действие; At first = начальное состояние."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct NEXT / THE NEXT pair.",
                "options": [
                    (
                        "next week / "
                        "the next chapter"
                    ),
                    (
                        "the next week always / "
                        "next the chapter"
                    ),
                    (
                        "next the week / "
                        "next chapter the"
                    ),
                    (
                        "the next Monday always / "
                        "the chapter next"
                    ),
                ],
                "answer": (
                    "next week / "
                    "the next chapter"
                ),
                "explanation": (
                    "Next week = следующий период; the next chapter = следующий элемент."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct LAST / THE LAST pair.",
                "options": [
                    (
                        "last year / "
                        "the last question"
                    ),
                    (
                        "the last year always / "
                        "last the question"
                    ),
                    (
                        "last the year / "
                        "last question the"
                    ),
                    (
                        "the year last / "
                        "question last"
                    ),
                ],
                "answer": (
                    "last year / "
                    "the last question"
                ),
                "explanation": (
                    "Last year = прошлый год; the last question = последний вопрос."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct date/preposition pair.",
                "options": [
                    (
                        "on 15 July / "
                        "in July / "
                        "in 2026"
                    ),
                    (
                        "in 15 July / "
                        "on July / "
                        "on 2026"
                    ),
                    (
                        "at 15 July / "
                        "on July / "
                        "at 2026"
                    ),
                    (
                        "on July 2026 / "
                        "at July / "
                        "on the year 2026"
                    ),
                ],
                "answer": (
                    "on 15 July / "
                    "in July / "
                    "in 2026"
                ),
                "explanation": (
                    "ON → конкретная дата; IN → месяц и год."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "1st → first / "
                        "2nd → second / "
                        "3rd → third / "
                        "21st → twenty-first / "
                        "1990s → no apostrophe / "
                        "1900s → twentieth century"
                    ),
                    (
                        "1st → oneth / "
                        "2nd → twoth / "
                        "3rd → threeth / "
                        "21st → twentieth-first / "
                        "1990s → 1990's / "
                        "1900s → nineteenth century"
                    ),
                    (
                        "1st → one / "
                        "2nd → twice / "
                        "3rd → three / "
                        "21st → twenty-oneth / "
                        "1990s → apostrophe required / "
                        "1900s → twenty-first century"
                    ),
                    (
                        "1st → firstly only / "
                        "2nd → two-th / "
                        "3rd → thirdth / "
                        "21st → twenty-one-th / "
                        "1990s → 1990's / "
                        "1900s → eighteenth century"
                    ),
                ],
                "answer": (
                    "1st → first / "
                    "2nd → second / "
                    "3rd → third / "
                    "21st → twenty-first / "
                    "1990s → no apostrophe / "
                    "1900s → twentieth century"
                ),
                "explanation": (
                    "Это основные правила ordinal numbers, "
                    "decades и centuries."
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
                "✅ A1 Lesson 59 seeded: Ordinal Numbers and Dates"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
