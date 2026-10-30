from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 12: "
        "Present Simple negatives."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=12,
            defaults={
                "title": "Отрицания в Present Simple",
                "slug": "present-simple-negatives",
                "theory_text": (
                    "Present Simple negatives: "
                    "don't and doesn't."
                ),
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Как сказать «не» в Present Simple",
                "body": """С обычными глаголами отрицание в Present Simple образуется при помощи:

do not;

does not.

Сокращённые формы:

don't;

doesn't.

Сравните:

I work.
I do not work.

She works.
She does not work.

Важно:

для обычного глагола нельзя просто добавить not.

Неправильно:

I not work.

Правильно:

I don't work.""",
            },

            {
                "order": 2,
                "title": "DO NOT / DON'T",
                "body": """Do not используется с:

I;

you;

we;

they;

подлежащими во множественном числе.

Примеры:

I do not work on Sundays.

You do not understand me.

We do not live in Astana.

They do not study English.

The children do not play outside.

В разговорной речи чаще используется сокращение:

do not = don't

I don't smoke.

We don't have much time.

They don't watch television.""",
            },

            {
                "order": 3,
                "title": "DOES NOT / DOESN'T",
                "body": """Does not используется с:

he;

she;

it;

одним человеком;

одним предметом;

одним животным.

Примеры:

He does not work here.

She does not speak French.

It does not work.

Marat does not live in Almaty.

The shop does not open on Sundays.

Сокращение:

does not = doesn't

He doesn't smoke.

She doesn't drive.

The phone doesn't work.""",
            },

            {
                "order": 4,
                "title": "После DOESN'T глагол теряет -S",
                "body": """Это главное правило урока.

После:

do not;

don't;

does not;

doesn't

основной глагол используется в начальной форме.

Сравните:

She works.

She doesn't work.

Неправильно:

She doesn't works.

Почему?

Потому что показатель третьего лица -s уже находится в слове does.

То же самое:

He lives.
He doesn't live.

She watches TV.
She doesn't watch TV.

He studies English.
He doesn't study English.""",
            },

            {
                "order": 5,
                "title": "HAVE после DOESN'T",
                "body": """В утверждении:

She has a car.

Но в отрицании:

She doesn't have a car.

Неправильно:

She doesn't has a car.

После doesn't используется исходная форма:

have.

Сравните:

He has a job.

He doesn't have a job.

My brother has a car.

My brother doesn't have a car.""",
            },

            {
                "order": 6,
                "title": "Формула отрицания",
                "body": """Для I, you, we, they:

Подлежащее + don't + глагол

Примеры:

I don't work.

You don't understand.

We don't agree.

They don't live here.

Для he, she, it:

Подлежащее + doesn't + глагол

Примеры:

He doesn't work.

She doesn't understand.

It doesn't open.

My father doesn't drive.""",
            },

            {
                "order": 7,
                "title": "Present Simple и TO BE",
                "body": """С глаголом to be do/does не используются.

Если есть:

am;
is;
are,

отрицание образуется при помощи not.

Правильно:

I am not tired.

She is not at home.

They are not ready.

Неправильно:

I don't am tired.

She doesn't be at home.

They don't are ready.

С обычным глаголом:

I don't work here.

She doesn't live here.

They don't study English.

Сравните:

She is not busy.

She doesn't work today.""",
            },

            {
                "order": 8,
                "title": "HAVE и HAVE GOT",
                "body": """В современном английском с have как обычным глаголом удобно использовать:

I don't have a car.

She doesn't have a car.

They don't have children.

Для тестов это безопасная и понятная форма.

Существует также конструкция have got:

I have got a car.

She has got a car.

Отрицание:

I haven't got a car.

She hasn't got a car.

Сравните:

She doesn't have a car.

She hasn't got a car.

Значение одинаковое, но грамматическая конструкция разная.""",
            },

            {
                "order": 9,
                "title": "Частые отрицательные выражения",
                "body": """Полезно запомнить готовые конструкции.

DON'T KNOW:

I don't know.

We don't know the answer.

DOESN'T LIKE:

He doesn't like coffee.

She doesn't like cold weather.

DON'T UNDERSTAND:

I don't understand.

They don't understand English.

DOESN'T WORK:

The phone doesn't work.

This method doesn't work.

The machine doesn't work properly.""",
            },

            {
                "order": 10,
                "title": "NEVER",
                "body": """Never означает «никогда».

Never уже имеет отрицательное значение.

Поэтому дополнительное don't или doesn't не нужно.

Правильно:

I never smoke.

She never drinks coffee.

They never arrive late.

Неправильно:

I don't never smoke.

She doesn't never drink coffee.

Сравните:

I don't smoke.
— Я не курю.

I never smoke.
— Я никогда не курю.""",
            },

            {
                "order": 11,
                "title": "Наречия частотности в отрицании",
                "body": """Наречия частотности обычно ставятся после don't/doesn't и перед основным глаголом.

Примеры:

I don't usually work on Sundays.

She doesn't often watch television.

They don't always agree.

Но never используется без don't/doesn't и обычно стоит перед глаголом:

I never eat fast food.

He never comes late.

She never drives at night.""",
            },

            {
                "order": 12,
                "title": "Типичные ошибки",
                "body": """Неправильно:

He doesn't works here.

Правильно:

He doesn't work here.

Неправильно:

She don't speak English.

Правильно:

She doesn't speak English.

Неправильно:

They doesn't live here.

Правильно:

They don't live here.

Неправильно:

He doesn't has a car.

Правильно:

He doesn't have a car.

Неправильно:

She doesn't tired.

Правильно:

She isn't tired.""",
            },

            {
                "order": 13,
                "title": "Как построить отрицание",
                "body": """Шаг 1. Найдите подлежащее.

My brother works here.

My brother = he.

Шаг 2. Выберите doesn't.

My brother doesn't...

Шаг 3. Верните основной глагол в начальную форму.

works → work

Итог:

My brother doesn't work here.

Другой пример:

My parents live in Astana.

My parents = they.

Используем don't:

My parents don't live in Astana.""",
            },

            {
                "order": 14,
                "title": "Главное правило",
                "body": """Запомните две основные группы.

I / YOU / WE / THEY:

don't + глагол

I don't work.

They don't live here.

HE / SHE / IT:

doesn't + глагол

He doesn't work.

She doesn't live here.

После doesn't глагол всегда возвращается в начальную форму.

She works.

She doesn't work.

He studies.

He doesn't study.

She has.

She doesn't have.""",
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
                "prompt": "I ___ work on Sundays.",
                "options": ["doesn't", "don't", "am not", "not"],
                "answer": "don't",
                "explanation": "С I используется don't.",
            },

            {
                "order": 2,
                "prompt": "She ___ work on Sundays.",
                "options": ["don't", "isn't", "doesn't", "not"],
                "answer": "doesn't",
                "explanation": "С she используется doesn't.",
            },

            {
                "order": 3,
                "prompt": "They ___ live here.",
                "options": ["doesn't", "don't", "aren't live", "not"],
                "answer": "don't",
                "explanation": "They → don't.",
            },

            {
                "order": 4,
                "prompt": "He doesn't ___ English.",
                "options": ["speaks", "speaking", "speak", "spoke"],
                "answer": "speak",
                "explanation": "После doesn't используется начальная форма speak.",
            },

            {
                "order": 5,
                "prompt": "My sister doesn't ___ television.",
                "options": ["watches", "watch", "watching", "watched"],
                "answer": "watch",
                "explanation": "После doesn't форма watches возвращается к watch.",
            },

            {
                "order": 6,
                "prompt": "She doesn't ___ a car.",
                "options": ["has", "have", "having", "had"],
                "answer": "have",
                "explanation": "После doesn't используется исходная форма have.",
            },

            {
                "order": 7,
                "prompt": "The phone ___ work.",
                "options": ["don't", "doesn't", "isn't", "aren't"],
                "answer": "doesn't",
                "explanation": "The phone = it, поэтому doesn't.",
            },

            {
                "order": 8,
                "prompt": "We ___ understand this rule.",
                "options": ["doesn't", "don't", "aren't", "isn't"],
                "answer": "don't",
                "explanation": "We → don't.",
            },

            {
                "order": 9,
                "prompt": "My wife ___ drink coffee.",
                "options": ["don't", "doesn't", "isn't", "aren't"],
                "answer": "doesn't",
                "explanation": "My wife = she, поэтому doesn't.",
            },

            {
                "order": 10,
                "prompt": "They don't ___ in Almaty.",
                "options": ["lives", "live", "living", "lived"],
                "answer": "live",
                "explanation": "После don't используется начальная форма live.",
            },

            {
                "order": 11,
                "prompt": "She doesn't ___ in Almaty.",
                "options": ["lives", "live", "living", "lived"],
                "answer": "live",
                "explanation": "После doesn't окончание -s исчезает.",
            },

            {
                "order": 12,
                "prompt": "My brother doesn't ___ English.",
                "options": ["studies", "study", "studying", "studied"],
                "answer": "study",
                "explanation": "Studies → doesn't study.",
            },

            {
                "order": 13,
                "prompt": "The shop doesn't ___ at eight.",
                "options": ["opens", "open", "opening", "opened"],
                "answer": "open",
                "explanation": "После doesn't используется open.",
            },

            {
                "order": 14,
                "prompt": "The students don't ___ many questions.",
                "options": ["asks", "ask", "asking", "asked"],
                "answer": "ask",
                "explanation": "Students = they; после don't используется ask.",
            },

            {
                "order": 15,
                "prompt": "My teacher doesn't ___ late.",
                "options": ["comes", "come", "coming", "came"],
                "answer": "come",
                "explanation": "Comes → doesn't come.",
            },

            {
                "order": 16,
                "prompt": "She doesn't ___ a new phone.",
                "options": ["has", "have", "having", "had"],
                "answer": "have",
                "explanation": "После doesn't используется have, а не has.",
            },

            {
                "order": 17,
                "prompt": "I ___ know the answer.",
                "options": ["doesn't", "don't", "am not", "isn't"],
                "answer": "don't",
                "explanation": "Know — обычный глагол; с I используется don't.",
            },

            {
                "order": 18,
                "prompt": "The machine ___ work properly.",
                "options": ["don't", "doesn't", "isn't", "aren't"],
                "answer": "doesn't",
                "explanation": "The machine = it, поэтому doesn't.",
            },

            {
                "order": 19,
                "prompt": "We ___ usually eat fast food.",
                "options": ["doesn't", "don't", "aren't", "isn't"],
                "answer": "don't",
                "explanation": "We → don't. Usually стоит перед основным глаголом.",
            },

            {
                "order": 20,
                "prompt": "He ___ drinks coffee.",
                "options": [
                    "doesn't never",
                    "never",
                    "don't never",
                    "not never",
                ],
                "answer": "never",
                "explanation": "Never уже имеет отрицательное значение, поэтому doesn't не нужен.",
            },

            {
                "order": 21,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She don't like coffee.",
                    "She doesn't likes coffee.",
                    "She doesn't like coffee.",
                    "She isn't like coffee.",
                ],
                "answer": "She doesn't like coffee.",
                "explanation": "She → doesn't, а основной глагол остаётся в форме like.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I am not understand.",
                    "I don't understand.",
                    "I doesn't understand.",
                    "I not understand.",
                ],
                "answer": "I don't understand.",
                "explanation": "Understand — обычный смысловой глагол, поэтому используется don't.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "She doesn't tired.",
                    "She don't tired.",
                    "She isn't tired.",
                    "She doesn't be tired.",
                ],
                "answer": "She isn't tired.",
                "explanation": "Tired используется с to be: She is tired → She isn't tired.",
            },

            {
                "order": 24,
                "prompt": "He has a new job. Choose the correct negative form.",
                "options": [
                    "He doesn't has a new job.",
                    "He don't have a new job.",
                    "He doesn't have a new job.",
                    "He isn't have a new job.",
                ],
                "answer": "He doesn't have a new job.",
                "explanation": "Has в отрицании меняется на doesn't have.",
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
                "✅ A1 Lesson 12 seeded: "
                "Отрицания в Present Simple"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
