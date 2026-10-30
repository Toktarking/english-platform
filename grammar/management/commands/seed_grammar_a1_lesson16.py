from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 16: "
        "Have / Has and Have got / Has got."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=16,
            defaults={
                "title": (
                    "HAVE / HAS и "
                    "HAVE GOT / HAS GOT"
                ),
                "slug": "have-has-have-got",
                "theory_text": (
                    "Have / has and "
                    "have got / has got."
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
                "title": "Что означает HAVE",
                "body": """Have обычно переводится как:

иметь;

у кого-то есть;

обладать.

Примеры:

I have a car.

She has two children.

They have a large house.

В русском:

У меня есть книга.

В английском:

I have a book.

То есть владелец ставится в начало предложения.""",
            },

            {
                "order": 2,
                "title": "HAVE или HAS",
                "body": """Главная таблица:

I → have

you → have

he → has

she → has

it → has

we → have

they → have

Запомните:

I / you / we / they HAVE

he / she / it HAS

Примеры:

I have a question.

They have three children.

He has a car.

She has a good job.""",
            },

            {
                "order": 3,
                "title": "Как выбрать HAVE или HAS",
                "body": """Замените подлежащее местоимением.

My sister ___ a car.

My sister = she.

Значит:

My sister has a car.

Другой пример:

My parents ___ a car.

My parents = they.

Значит:

My parents have a car.

То же правило:

Marat = he → has

The house = it → has

The students = they → have.""",
            },

            {
                "order": 4,
                "title": "Что можно выражать через HAVE / HAS",
                "body": """Have / has используется не только с предметами.

Владение:

I have a laptop.

She has a new bag.

Семья:

I have a wife.

She has two brothers.

Внешность:

She has blue eyes.

He has dark hair.

Характеристики:

The house has large windows.

The book has ten chapters.

Состояния:

I have a headache.

She has a cold.

They have a problem.""",
            },

            {
                "order": 5,
                "title": "Артикли после HAVE / HAS",
                "body": """С одним исчисляемым предметом обычно нужен a/an:

I have a car.

She has a book.

He has an idea.

Неправильно:

I have car.

С множественным числом a/an не используется:

I have two books.

She has three sisters.

С неисчисляемыми:

We have some information.

They have enough money.

I have little time.

Нельзя:

an information;

a money.""",
            },

            {
                "order": 6,
                "title": "Отрицание: DON'T HAVE / DOESN'T HAVE",
                "body": """С I, you, we, they:

don't have

I don't have a car.

We don't have children.

They don't have any money.

С he, she, it:

doesn't have

He doesn't have a car.

She doesn't have children.

My brother doesn't have a job.

Важно:

после doesn't используется HAVE.

She has a car.

She doesn't have a car.

Неправильно:

She doesn't has a car.""",
            },

            {
                "order": 7,
                "title": "Вопросы с HAVE",
                "body": """С I, you, we, they:

Do + подлежащее + have...?

Do you have a car?

Do they have children?

Do we have enough time?

С he, she, it:

Does + подлежащее + have...?

Does he have a car?

Does she have children?

Does your brother have a job?

Важно:

Does she have...?

Не:

Does she has...?""",
            },

            {
                "order": 8,
                "title": "Краткие ответы с HAVE",
                "body": """Вопрос:

Do you have a car?

Ответы:

Yes, I do.

No, I don't.

Вопрос:

Does she have a car?

Ответы:

Yes, she does.

No, she doesn't.

В кратком ответе have обычно не повторяется.

Do they have children?

Yes, they do.

Does he have a job?

No, he doesn't.""",
            },

            {
                "order": 9,
                "title": "HAVE GOT / HAS GOT",
                "body": """Have got / has got обычно имеет то же значение владения, что и have / has.

Сравните:

I have a car.

I have got a car.

Оба означают:

У меня есть машина.

Формы:

I have got

you have got

he has got

she has got

it has got

we have got

they have got

Примеры:

I've got a question.

She's got a new job.

They've got three children.""",
            },

            {
                "order": 10,
                "title": "Отрицание с HAVE GOT",
                "body": """С I, you, we, they:

haven't got

I haven't got a car.

We haven't got much time.

They haven't got children.

С he, she, it:

hasn't got

He hasn't got a car.

She hasn't got any brothers.

The phone hasn't got a camera.

Важно:

с have got do/does не используются.

Правильно:

She hasn't got a car.

Неправильно:

She doesn't have got a car.""",
            },

            {
                "order": 11,
                "title": "Вопросы с HAVE GOT",
                "body": """В конструкции have got слово have или has ставится перед подлежащим.

Утверждение:

You have got a car.

Вопрос:

Have you got a car?

Примеры:

Have they got children?

Have we got enough time?

Has he got a car?

Has she got a job?

Has your brother got a phone?

Краткие ответы:

Have you got a car?

Yes, I have.

No, I haven't.

Has she got a car?

Yes, she has.

No, she hasn't.""",
            },

            {
                "order": 12,
                "title": "Не смешивайте две системы",
                "body": """Система 1 — обычный HAVE:

I have a car.

I don't have a car.

Do you have a car?

Yes, I do.

Система 2 — HAVE GOT:

I've got a car.

I haven't got a car.

Have you got a car?

Yes, I have.

Нельзя смешивать системы.

Для начального уровня лучше выбрать одну конструкцию и использовать её полностью.""",
            },

            {
                "order": 13,
                "title": "HAVE как действие",
                "body": """Have может означать не владение, а действие.

Полезные выражения:

have breakfast;

have lunch;

have dinner;

have a shower;

have a rest;

have a lesson;

have a good time.

Примеры:

I have breakfast at seven.

She has a shower every morning.

We have English on Monday.

They have a good time at parties.

В таком значении have got обычно не используется.

Неправильно:

I have got breakfast at seven.

Правильно:

I have breakfast at seven.""",
            },

            {
                "order": 14,
                "title": "Как выбрать конструкцию",
                "body": """Если говорим о владении, можно использовать две системы.

Система HAVE:

She has a car.

She doesn't have a car.

Does she have a car?

Yes, she does.

Система HAVE GOT:

She has got a car.

She hasn't got a car.

Has she got a car?

Yes, she has.

Если have означает действие:

have breakfast;

have a shower;

have a lesson;

используется обычная система do/does.

Does she have lunch at work?

Также не путайте have с have to:

I have to work tomorrow.

Have to означает «нужно / приходится» и будет отдельной темой.""",
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
                "prompt": "We ___ two children.",
                "options": ["has", "have", "having", "are have"],
                "answer": "have",
                "explanation": "We → have.",
            },

            {
                "order": 2,
                "prompt": "My sister ___ a new job.",
                "options": ["have", "has", "having", "is have"],
                "answer": "has",
                "explanation": "My sister = she, поэтому has.",
            },

            {
                "order": 3,
                "prompt": "The house ___ four bedrooms.",
                "options": ["have", "has", "is", "are"],
                "answer": "has",
                "explanation": "The house = it, поэтому has.",
            },

            {
                "order": 4,
                "prompt": "The students ___ many questions.",
                "options": ["has", "have", "is", "having"],
                "answer": "have",
                "explanation": "Students = they, поэтому have.",
            },

            {
                "order": 5,
                "prompt": "I don't ___ enough money.",
                "options": ["has", "have", "having", "had"],
                "answer": "have",
                "explanation": "После don't используется базовая форма have.",
            },

            {
                "order": 6,
                "prompt": "He doesn't ___ a driving licence.",
                "options": ["has", "have", "having", "had"],
                "answer": "have",
                "explanation": "После doesn't используется have, а не has.",
            },

            {
                "order": 7,
                "prompt": "___ you have any brothers?",
                "options": ["Does", "Do", "Are", "Have got"],
                "answer": "Do",
                "explanation": "В обычной конструкции have с you вопрос начинается с Do.",
            },

            {
                "order": 8,
                "prompt": "___ she have a car?",
                "options": ["Do", "Does", "Has", "Is"],
                "answer": "Does",
                "explanation": "She → Does she have...?",
            },

            {
                "order": 9,
                "prompt": "They have ___ a large house.",
                "options": ["get", "got", "gets", "getting"],
                "answer": "got",
                "explanation": "Конструкция: have got.",
            },

            {
                "order": 10,
                "prompt": "He has ___ blue eyes.",
                "options": ["get", "got", "getting", "gets"],
                "answer": "got",
                "explanation": "He has got blue eyes.",
            },

            {
                "order": 11,
                "prompt": "I ___ got a headache.",
                "options": ["has", "have", "am", "do"],
                "answer": "have",
                "explanation": "I → have got.",
            },

            {
                "order": 12,
                "prompt": "She ___ got a cold.",
                "options": ["have", "has", "does", "is"],
                "answer": "has",
                "explanation": "She → has got.",
            },

            {
                "order": 13,
                "prompt": "___ they got enough time?",
                "options": ["Has", "Have", "Do", "Are"],
                "answer": "Have",
                "explanation": "В конструкции have got вопрос: Have they got...?",
            },

            {
                "order": 14,
                "prompt": "Has your brother got a car?",
                "options": [
                    "No, he doesn't.",
                    "No, he hasn't.",
                    "No, he isn't.",
                    "No, he don't.",
                ],
                "answer": "No, he hasn't.",
                "explanation": "Вопрос с Has ... got? требует ответа с has/hasn't.",
            },

            {
                "order": 15,
                "prompt": "Does your brother have a car?",
                "options": [
                    "Yes, he has.",
                    "Yes, he does.",
                    "Yes, he is.",
                    "Yes, he have.",
                ],
                "answer": "Yes, he does.",
                "explanation": "Вопрос с Does ... have? требует краткого ответа с does.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "She doesn't has a car.",
                    "She doesn't have a car.",
                    "She don't have a car.",
                    "She isn't have a car.",
                ],
                "answer": "She doesn't have a car.",
                "explanation": "После doesn't используется базовая форма have.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct HAVE GOT negative.",
                "options": [
                    "She doesn't have got a car.",
                    "She hasn't got a car.",
                    "She doesn't has got a car.",
                    "She isn't got a car.",
                ],
                "answer": "She hasn't got a car.",
                "explanation": "В системе have got отрицание строится через hasn't got.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct HAVE GOT question.",
                "options": [
                    "Does she have got a car?",
                    "Has she got a car?",
                    "Does she got a car?",
                    "Is she got a car?",
                ],
                "answer": "Has she got a car?",
                "explanation": "В have got форма has ставится перед подлежащим.",
            },

            {
                "order": 19,
                "prompt": "Do they have children?",
                "options": [
                    "Yes, they have.",
                    "Yes, they do.",
                    "Yes, they are.",
                    "Yes, they has.",
                ],
                "answer": "Yes, they do.",
                "explanation": "Обычный have с Do требует ответа Yes, they do.",
            },

            {
                "order": 20,
                "prompt": "Have they got children?",
                "options": [
                    "Yes, they do.",
                    "Yes, they have.",
                    "Yes, they are.",
                    "Yes, they got.",
                ],
                "answer": "Yes, they have.",
                "explanation": "Have they got...? → Yes, they have.",
            },

            {
                "order": 21,
                "prompt": "Choose the correct sentence about breakfast.",
                "options": [
                    "I have got breakfast at seven.",
                    "I have breakfast at seven.",
                    "I am have breakfast at seven.",
                    "I has breakfast at seven.",
                ],
                "answer": "I have breakfast at seven.",
                "explanation": "Have breakfast — устойчивое выражение действия; have got здесь не используется.",
            },

            {
                "order": 22,
                "prompt": "___ she have lunch at work?",
                "options": ["Has", "Does", "Is", "Have"],
                "answer": "Does",
                "explanation": "Have lunch — обычное действие, поэтому вопрос строится через does.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "The dog have a long tail.",
                    "The dog has a long tail.",
                    "The dog is have a long tail.",
                    "The dog having a long tail.",
                ],
                "answer": "The dog has a long tail.",
                "explanation": "The dog = it, поэтому has.",
            },

            {
                "order": 24,
                "prompt": "Which pair uses one system consistently?",
                "options": [
                    "She has a car. / Has she got a car?",
                    "She has got a car. / Does she have got a car?",
                    "She has a car. / Does she have a car?",
                    "She has got a car. / Does she has a car?",
                ],
                "answer": "She has a car. / Does she have a car?",
                "explanation": "Это одна система: have/has + do/does. Не смешиваем её с have got.",
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
                "✅ A1 Lesson 16 seeded: "
                "HAVE / HAS и HAVE GOT / HAS GOT"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
