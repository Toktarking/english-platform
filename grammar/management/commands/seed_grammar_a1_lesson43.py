from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 43: "
        "Comparatives and Superlatives."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=43,
            defaults={
                "title": "Степени сравнения прилагательных",
                "slug": "comparatives-and-superlatives",
                "theory_text": "Comparatives and Superlatives.",
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Три формы прилагательного",
                "body": """Прилагательное может использоваться в трёх формах:

обычная форма;

сравнительная степень;

превосходная степень.

Пример:

tall

taller

the tallest

Ещё пример:

interesting

more interesting

the most interesting""",
            },

            {
                "order": 2,
                "title": "Сравнительная степень",
                "body": """Сравнительная степень используется, когда сравниваются два человека, предмета или ситуации.

Примеры:

Tom is taller than Jack.

This book is more interesting than that one.

Today is colder than yesterday.

После сравнительной степени часто используется THAN:

taller than

faster than

more expensive than""",
            },

            {
                "order": 3,
                "title": "Короткие прилагательные: -ER",
                "body": """К коротким прилагательным обычно добавляется -ER.

Примеры:

tall → taller

small → smaller

long → longer

fast → faster

old → older

Если прилагательное заканчивается на E:

nice → nicer

large → larger

safe → safer""",
            },

            {
                "order": 4,
                "title": "Удвоение согласной и Y → I",
                "body": """В некоторых коротких прилагательных последняя согласная удваивается:

big → bigger

hot → hotter

thin → thinner

fat → fatter

Если прилагательное заканчивается на Y:

happy → happier

easy → easier

busy → busier

heavy → heavier""",
            },

            {
                "order": 5,
                "title": "Длинные прилагательные: MORE",
                "body": """С длинными прилагательными обычно используется:

more + adjective

Примеры:

more beautiful

more interesting

more expensive

more difficult

more important

Нельзя одновременно использовать MORE и -ER.

Неправильно:

more easier

more cheaper

more beautifuler

Правильно:

easier

cheaper

more beautiful""",
            },

            {
                "order": 6,
                "title": "Превосходная степень",
                "body": """Превосходная степень используется, когда один объект выделяется среди трёх и более.

Перед ней обычно используется THE.

Примеры:

the tallest

the biggest

the most beautiful

the best

Короткие прилагательные:

tall → the tallest

fast → the fastest

Длинные:

beautiful → the most beautiful

difficult → the most difficult""",
            },

            {
                "order": 7,
                "title": "Правописание в превосходной степени",
                "body": """Прилагательные на E:

nice → the nicest

large → the largest

Удвоение согласной:

big → the biggest

hot → the hottest

thin → the thinnest

Прилагательные на Y:

happy → the happiest

easy → the easiest

busy → the busiest

heavy → the heaviest""",
            },

            {
                "order": 8,
                "title": "Неправильные формы",
                "body": """Некоторые формы нужно запомнить.

good → better → the best

bad → worse → the worst

many/much → more → the most

little → less → the least

far → farther/further → the farthest/the furthest

Примеры:

This book is better than that one.

This is the worst result.

She has more experience than me.""",
            },

            {
                "order": 9,
                "title": "OLDER и ELDER",
                "body": """OLDER используется для людей и предметов.

My brother is older than me.

This building is older than that one.

ELDER обычно используется только для членов семьи перед существительным.

my elder brother

her elder sister

Но:

He is older than me.

Не:

He is elder than me.""",
            },

            {
                "order": 10,
                "title": "IN, OF и усиление сравнения",
                "body": """После превосходной степени:

IN используется с местом или группой.

the tallest in the class

the biggest city in Kazakhstan

OF используется с количеством или набором.

the best of the three

the most expensive of all

Сравнительную степень можно усиливать:

much better

far more interesting

a lot bigger

much easier

Для небольшой разницы:

a little bigger

slightly cheaper

a bit colder""",
            },

            {
                "order": 11,
                "title": "AS...AS и NOT AS...AS",
                "body": """Для равенства:

as + adjective + as

She is as tall as her sister.

This book is as interesting as that one.

Для неравенства:

not as + adjective + as

This task is not as difficult as that one.

My phone is not as expensive as yours.

Также можно использовать:

less + adjective

This book is less interesting.""",
            },

            {
                "order": 12,
                "title": "MORE, FEWER и LESS",
                "body": """Для сравнения количества:

MORE:

more books

more money

more time

FEWER используется с исчисляемыми существительными:

fewer students

fewer mistakes

fewer cars

LESS используется с неисчисляемыми:

less water

less money

less time

Примеры:

This class has fewer students.

I have less time today.""",
            },

            {
                "order": 13,
                "title": "Полезные конструкции",
                "body": """THE MORE..., THE MORE...

The more you study, the better you understand.

The earlier we leave, the sooner we arrive.

Постепенное изменение:

bigger and bigger

better and better

more and more expensive

ONE OF THE...

one of the best students

one of the largest cities

После one of the нужен существительное во множественном числе.""",
            },

            {
                "order": 14,
                "title": "Как выбрать форму",
                "body": """Сравниваются два объекта?

→ comparative

This car is faster than that one.

Один объект выделяется среди группы?

→ superlative

This is the fastest car here.

Короткое прилагательное?

→ обычно -er / -est

Длинное прилагательное?

→ more / the most

Неправильная форма?

Запомните:

good → better → the best

bad → worse → the worst

much/many → more → the most

little → less → the least""",
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
                "prompt": "This car is ___ than mine.",
                "options": [
                    "fast",
                    "faster",
                    "fastest",
                    "more faster",
                ],
                "answer": "faster",
                "explanation": (
                    "Fast — короткое прилагательное, "
                    "comparative: faster."
                ),
            },

            {
                "order": 2,
                "prompt": "She is ___ person in the office.",
                "options": [
                    "friendly",
                    "friendlier",
                    "the friendliest",
                    "the more friendly",
                ],
                "answer": "the friendliest",
                "explanation": (
                    "Один человек выделяется среди группы → superlative."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "This exercise is ___ than the previous one."
                ),
                "options": [
                    "difficult",
                    "difficulter",
                    "more difficult",
                    "the most difficult",
                ],
                "answer": "more difficult",
                "explanation": (
                    "Difficult — длинное прилагательное → more difficult."
                ),
            },

            {
                "order": 4,
                "prompt": "That was ___ film of the year.",
                "options": [
                    "more interesting",
                    "the most interesting",
                    "interestinger",
                    "the interestingest",
                ],
                "answer": "the most interesting",
                "explanation": (
                    "Superlative длинного прилагательного: "
                    "the most interesting."
                ),
            },

            {
                "order": 5,
                "prompt": "My bag is ___ than yours.",
                "options": [
                    "heavy",
                    "heavier",
                    "heaviest",
                    "more heavy",
                ],
                "answer": "heavier",
                "explanation": (
                    "Heavy → heavier: y меняется на i."
                ),
            },

            {
                "order": 6,
                "prompt": "This is ___ bag here.",
                "options": [
                    "heavier",
                    "the heaviest",
                    "more heavier",
                    "heaviest than",
                ],
                "answer": "the heaviest",
                "explanation": (
                    "Superlative: heavy → the heaviest."
                ),
            },

            {
                "order": 7,
                "prompt": "Today is ___ than Monday.",
                "options": [
                    "busy",
                    "busier",
                    "busiest",
                    "more busyer",
                ],
                "answer": "busier",
                "explanation": (
                    "Busy → busier."
                ),
            },

            {
                "order": 8,
                "prompt": "He is ___ student in the class.",
                "options": [
                    "bad",
                    "worse",
                    "the worst",
                    "the baddest",
                ],
                "answer": "the worst",
                "explanation": (
                    "Bad → worse → the worst."
                ),
            },

            {
                "order": 9,
                "prompt": "This answer is ___ than the first one.",
                "options": [
                    "good",
                    "better",
                    "best",
                    "more good",
                ],
                "answer": "better",
                "explanation": (
                    "Good → better."
                ),
            },

            {
                "order": 10,
                "prompt": "She has ___ experience than me.",
                "options": [
                    "many",
                    "more",
                    "most",
                    "the more",
                ],
                "answer": "more",
                "explanation": (
                    "Much/many → more."
                ),
            },

            {
                "order": 11,
                "prompt": "We have ___ time today.",
                "options": [
                    "less",
                    "least",
                    "fewer",
                    "the less",
                ],
                "answer": "less",
                "explanation": (
                    "Time — неисчисляемое существительное → less."
                ),
            },

            {
                "order": 12,
                "prompt": "This class has ___ students.",
                "options": [
                    "less",
                    "fewer",
                    "fewest than",
                    "little",
                ],
                "answer": "fewer",
                "explanation": (
                    "Students — исчисляемое множественное число → fewer."
                ),
            },

            {
                "order": 13,
                "prompt": "This room is not ___ large as that one.",
                "options": [
                    "so",
                    "as",
                    "more",
                    "than",
                ],
                "answer": "as",
                "explanation": (
                    "Конструкция: not as + adjective + as."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "The more you practise, the ___ you become."
                ),
                "options": [
                    "good",
                    "better",
                    "best",
                    "more good",
                ],
                "answer": "better",
                "explanation": (
                    "The + comparative, the + comparative."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "This is one of the ___ places in the city."
                ),
                "options": [
                    "beautiful",
                    "more beautiful",
                    "most beautiful",
                    "beautifullest",
                ],
                "answer": "most beautiful",
                "explanation": (
                    "One of the + superlative + plural noun."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct form.",
                "options": [
                    "more easier",
                    "easier",
                    "more easyer",
                    "the easier than",
                ],
                "answer": "easier",
                "explanation": (
                    "Нельзя использовать more и -er одновременно."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "He is more taller than me.",
                    "He is taller than me.",
                    "He is tallest than me.",
                    "He is taller that me.",
                ],
                "answer": "He is taller than me.",
                "explanation": (
                    "Comparative: taller + than."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She is tallest in the class.",
                    "She is the tallest in the class.",
                    "She is the most tallest in the class.",
                    "She is taller in all class.",
                ],
                "answer": "She is the tallest in the class.",
                "explanation": (
                    "Перед superlative обычно нужен the."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct irregular forms.",
                "options": [
                    "good → gooder → the goodest",
                    "good → better → the best",
                    "good → more good → the most good",
                    "good → best → better",
                ],
                "answer": "good → better → the best",
                "explanation": "Это неправильная форма.",
            },

            {
                "order": 20,
                "prompt": "Choose the correct sentence with ELDER/OLDER.",
                "options": [
                    "He is elder than me.",
                    "He is older than me.",
                    "This car is elder than mine.",
                    "He is more elder than me.",
                ],
                "answer": "He is older than me.",
                "explanation": (
                    "Older используется в сравнении с than."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "This book is much better.",
                    "This book is very better.",
                    "This book is more better.",
                    "This book is much best.",
                ],
                "answer": "This book is much better.",
                "explanation": (
                    "Much может усиливать comparative."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct equality sentence.",
                "options": [
                    "She is as tall than her sister.",
                    "She is as tall as her sister.",
                    "She is so taller as her sister.",
                    "She is as taller as her sister.",
                ],
                "answer": "She is as tall as her sister.",
                "explanation": (
                    "Равенство: as + adjective + as."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct IN/OF pair.",
                "options": [
                    (
                        "the tallest in the class / "
                        "the best of the three"
                    ),
                    (
                        "the tallest of the class / "
                        "the best in the three"
                    ),
                    (
                        "the tallest at the class / "
                        "the best from the three"
                    ),
                    (
                        "the taller in class / "
                        "the most best of three"
                    ),
                ],
                "answer": (
                    "the tallest in the class / "
                    "the best of the three"
                ),
                "explanation": (
                    "IN — место/группа; OF — набор или количество."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "tall → taller → the tallest / "
                        "beautiful → more beautiful → "
                        "the most beautiful / "
                        "bad → worse → the worst"
                    ),
                    (
                        "tall → more taller → most tallest / "
                        "beautiful → beautifuler → beautifulest / "
                        "bad → badder → baddest"
                    ),
                    (
                        "tall → tallest → taller / "
                        "beautiful → most beautiful → more beautiful / "
                        "bad → worst → worse"
                    ),
                    (
                        "tall → more tall → the most tall / "
                        "beautiful → beautifuller → "
                        "the beautifullest / "
                        "bad → more bad → most bad"
                    ),
                ],
                "answer": (
                    "tall → taller → the tallest / "
                    "beautiful → more beautiful → "
                    "the most beautiful / "
                    "bad → worse → the worst"
                ),
                "explanation": (
                    "Короткое adjective → -er/-est; "
                    "длинное → more/the most; "
                    "bad имеет неправильные формы."
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
                "✅ A1 Lesson 43 seeded: "
                "Comparatives and Superlatives"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
