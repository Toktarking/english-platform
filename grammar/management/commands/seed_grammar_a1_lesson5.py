from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 5: "
        "Much, many, a lot of, few, a few, "
        "little, a little."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=5,
            defaults={
                "title": (
                    "Much, many, a lot of, few, "
                    "a few, little, a little"
                ),
                "slug": "much-many-few-little",
                "theory_text": (
                    "Words of quantity."
                ),
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        # ==================================================
        # THEORY
        # ==================================================

        sections = [

            {
                "order": 1,
                "title": "Как выбрать слово количества",
                "body": """В английском языке выбор слова количества зависит от существительного.

Сравните:

many books — много книг;
much water — много воды.

Books можно посчитать, поэтому используем many.

Water нельзя посчитать как отдельные предметы, поэтому используем much.

Неправильно:

much books;
many water.

Поэтому сначала определите:

1. существительное исчисляемое или неисчисляемое;
2. какое значение нужно: много, немного или мало.""",
            },

            {
                "order": 2,
                "title": "Many",
                "body": """Many означает «много».

Используется с исчисляемыми существительными во множественном числе.

Формула:

many + countable plural noun

Примеры:

many books;
many students;
many questions;
many people;
many problems.

There are many books in the library.

Many students study English.

She has many friends.

Особенно важно:

How many...?

How many students are there?
How many apples do you need?
How many lessons do you have today?

Many также часто используется в отрицаниях:

We do not have many chairs.
She does not ask many questions.""",
            },

            {
                "order": 3,
                "title": "Much",
                "body": """Much тоже означает «много».

Но much используется с неисчисляемыми существительными.

Формула:

much + uncountable noun

Примеры:

much money;
much water;
much time;
much information;
much work.

How much money do you need?

How much water do you drink?

Do we have much time?

В отрицаниях:

I do not have much money.
We do not have much time.
There is not much milk in the fridge.

Запомните:

How many books?
How much money?""",
            },

            {
                "order": 4,
                "title": "Much в утверждениях",
                "body": """В обычной разговорной речи much реже используется в простых утвердительных предложениях.

Менее естественно:

I have much work.

Более естественно:

I have a lot of work.

Но much нормально используется после:

too;
so;
very;
as.

Примеры:

I have too much work.

She spends so much money.

Thank you very much.""",
            },

            {
                "order": 5,
                "title": "A lot of и lots of",
                "body": """A lot of означает «много».

Главное преимущество: его можно использовать и с исчисляемыми, и с неисчисляемыми существительными.

Countable:

a lot of books;
a lot of students;
a lot of people.

Uncountable:

a lot of money;
a lot of water;
a lot of information;
a lot of work.

В утверждениях a lot of звучит очень естественно:

She has a lot of friends.
We bought a lot of food.
He spends a lot of money.

Lots of имеет такое же значение, но немного более разговорное:

lots of books;
lots of time;
lots of people.""",
            },

            {
                "order": 6,
                "title": "A lot и a lot of",
                "body": """Нужно различать:

a lot of + существительное

и

a lot — без существительного.

Примеры:

We spent a lot of money.
— Мы потратили много денег.

We spent a lot.
— Мы много потратили.

Неправильно:

We spent a lot money.

Правильно:

We spent a lot of money.""",
            },

            {
                "order": 7,
                "title": "A few",
                "body": """A few используется только с исчисляемыми существительными во множественном числе.

A few означает:

несколько;
немного;
есть некоторое количество.

Обычно смысл положительный.

Примеры:

I have a few friends.
— У меня есть несколько друзей.

We have a few questions.
— У нас есть несколько вопросов.

She stayed for a few days.

Количество небольшое, но оно есть и часто его достаточно.""",
            },

            {
                "order": 8,
                "title": "Few",
                "body": """Few тоже используется с исчисляемыми существительными во множественном числе.

Но значение другое:

мало;
почти нет;
недостаточно.

Обычно смысл отрицательный.

Примеры:

I have few friends.
— У меня мало друзей.

Few students understood the lesson.

We have few chairs.

Сравните:

I have a few friends.
— Несколько друзей есть.

I have few friends.
— Друзей почти нет.

Это различие часто проверяется в тестах.""",
            },

            {
                "order": 9,
                "title": "A little",
                "body": """A little используется с неисчисляемыми существительными.

Означает:

немного;
некоторое количество есть.

Обычно смысл положительный.

Примеры:

I have a little money.

There is a little milk in the fridge.

We have a little time.

Количество маленькое, но его достаточно или оно хотя бы существует.""",
            },

            {
                "order": 10,
                "title": "Little",
                "body": """Little используется с неисчисляемыми существительными.

Little означает:

мало;
почти нет;
недостаточно.

Обычно значение отрицательное.

Примеры:

I have little money.

There is little water left.

We have little time.

Сравните:

We have a little time.
— У нас есть немного времени.

We have little time.
— У нас почти нет времени.

She knows a little English.
— Она немного знает английский.

She knows little English.
— Она почти не знает английский.""",
            },

            {
                "order": 11,
                "title": "Главная таблица",
                "body": """Запомните:

MANY
исчисляемые, множественное число
many books

MUCH
неисчисляемые
much money

A LOT OF
оба типа
a lot of books
a lot of money

A FEW
исчисляемые
несколько, немного
a few books

FEW
исчисляемые
мало, почти нет
few books

A LITTLE
неисчисляемые
немного
a little water

LITTLE
неисчисляемые
мало, почти нет
little water""",
            },

            {
                "order": 12,
                "title": "Как выбрать правильный вариант",
                "body": """Шаг 1.

Посмотрите на существительное.

There are ___ books.

Books — исчисляемое множественное число.

Возможны:

many;
a lot of;
a few;
few.

Шаг 2.

Определите смысл.

Если «много»:

many books;
a lot of books.

Если «несколько»:

a few books.

Если «мало, почти нет»:

few books.

Теперь:

We have ___ time.

Time — неисчисляемое.

Если «много»:

much time;
a lot of time.

Если «немного»:

a little time.

Если «мало, почти нет»:

little time.""",
            },

            {
                "order": 13,
                "title": "Too many / too much / so many / so much",
                "body": """Too означает «слишком».

TOO MANY используется с исчисляемыми:

too many people;
too many questions;
too many cars.

TOO MUCH используется с неисчисляемыми:

too much money;
too much work;
too much sugar.

Примеры:

There are too many people in the room.

I have too much work.

SO MANY:

so many books;
so many people;
so many problems.

SO MUCH:

so much money;
so much time;
so much information.

Why are there so many people here?

She has so much work today.""",
            },

            {
                "order": 14,
                "title": "Как смысл предложения помогает",
                "body": """Иногда оба варианта грамматически подходят, поэтому нужно понимать смысл.

A FEW / FEW

We have a few chairs, so everyone can sit down.

Стульев немного, но достаточно.

We have few chairs, so some people must stand.

Стульев недостаточно.

A LITTLE / LITTLE

We have a little time, so let us discuss the problem.

Время есть.

We have little time, so we must hurry.

Времени почти нет.

Типичные ошибки:

many money ❌
a lot of money ✅

much books ❌
many books ✅

a lot students ❌
a lot of students ✅

a few water ❌
a little water ✅

a little questions ❌
a few questions ✅""",
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

        # ==================================================
        # PRACTICE — 24 QUESTIONS
        # ==================================================

        exercises = [

            {
                "order": 1,
                "prompt": "There are ___ students in the classroom.",
                "options": ["much", "many", "little", "a little"],
                "answer": "many",
                "explanation": "Students — исчисляемое существительное во множественном числе.",
            },

            {
                "order": 2,
                "prompt": "We do not have ___ time.",
                "options": ["many", "a few", "much", "few"],
                "answer": "much",
                "explanation": "Time — неисчисляемое существительное.",
            },

            {
                "order": 3,
                "prompt": "She has ___ friends in London.",
                "options": ["a little", "much", "a few", "little"],
                "answer": "a few",
                "explanation": "Friends — исчисляемое. A few означает, что несколько друзей есть.",
            },

            {
                "order": 4,
                "prompt": "There is ___ milk in the fridge. We can make some coffee.",
                "options": ["a little", "a few", "few", "many"],
                "answer": "a little",
                "explanation": "Milk неисчисляемое. Молока немного, но его достаточно.",
            },

            {
                "order": 5,
                "prompt": "There is ___ milk in the fridge. We need to buy more.",
                "options": ["a little", "little", "a few", "many"],
                "answer": "little",
                "explanation": "Молока почти нет, поэтому нужно купить ещё.",
            },

            {
                "order": 6,
                "prompt": "We went shopping and spent ___ money.",
                "options": ["many", "a lot", "a lot of", "a few"],
                "answer": "a lot of",
                "explanation": "Перед существительным money нужно a lot of.",
            },

            {
                "order": 7,
                "prompt": "Only ___ students passed the examination. The result was disappointing.",
                "options": ["a few", "few", "a little", "much"],
                "answer": "few",
                "explanation": "Результат разочаровывает, значит студентов было мало.",
            },

            {
                "order": 8,
                "prompt": "I speak ___ English, so I can help you.",
                "options": ["little", "few", "a little", "a few"],
                "answer": "a little",
                "explanation": "English здесь неисчисляемое понятие. Некоторое знание есть.",
            },

            {
                "order": 9,
                "prompt": "How ___ students are there in your group?",
                "options": ["much", "many", "little", "a little"],
                "answer": "many",
                "explanation": "How many используется с исчисляемыми существительными.",
            },

            {
                "order": 10,
                "prompt": "How ___ water do you drink every day?",
                "options": ["many", "a few", "much", "few"],
                "answer": "much",
                "explanation": "Water — неисчисляемое: How much water?",
            },

            {
                "order": 11,
                "prompt": "We have ___ apples. You can take one.",
                "options": ["a few", "a little", "much", "little"],
                "answer": "a few",
                "explanation": "Apples — исчисляемое, и яблок достаточно.",
            },

            {
                "order": 12,
                "prompt": "We have ___ apples, so we cannot make an apple pie.",
                "options": ["a few", "few", "a little", "much"],
                "answer": "few",
                "explanation": "Яблок недостаточно, поэтому few.",
            },

            {
                "order": 13,
                "prompt": "There is ___ coffee left. Would you like some?",
                "options": ["a few", "many", "a little", "few"],
                "answer": "a little",
                "explanation": "Coffee неисчисляемое, и некоторое количество осталось.",
            },

            {
                "order": 14,
                "prompt": "There is ___ coffee left. We need to make more.",
                "options": ["a little", "little", "a few", "many"],
                "answer": "little",
                "explanation": "Кофе почти не осталось.",
            },

            {
                "order": 15,
                "prompt": "She has ___ work today.",
                "options": ["many", "a lot of", "a few", "few"],
                "answer": "a lot of",
                "explanation": "Work — неисчисляемое. В утверждении a lot of звучит естественно.",
            },

            {
                "order": 16,
                "prompt": "There were too ___ people in the room.",
                "options": ["much", "little", "many", "a little"],
                "answer": "many",
                "explanation": "People — исчисляемое множественное число: too many people.",
            },

            {
                "order": 17,
                "prompt": "Do not add too ___ salt.",
                "options": ["many", "much", "a few", "few"],
                "answer": "much",
                "explanation": "Salt — неисчисляемое: too much salt.",
            },

            {
                "order": 18,
                "prompt": "Only ___ people knew the answer, but at least someone answered correctly.",
                "options": ["few", "a few", "little", "a little"],
                "answer": "a few",
                "explanation": "Несколько людей всё-таки знали ответ, поэтому a few.",
            },

            {
                "order": 19,
                "prompt": "We have ___ chairs, so everyone can sit down.",
                "options": ["few", "a few", "little", "a little"],
                "answer": "a few",
                "explanation": "Стульев немного, но их достаточно.",
            },

            {
                "order": 20,
                "prompt": "We have ___ chairs, so some people must stand.",
                "options": ["few", "a few", "little", "a little"],
                "answer": "few",
                "explanation": "Стульев недостаточно.",
            },

            {
                "order": 21,
                "prompt": "We have ___ time, so let us discuss the problem.",
                "options": ["few", "a few", "little", "a little"],
                "answer": "a little",
                "explanation": "Времени немного, но оно есть.",
            },

            {
                "order": 22,
                "prompt": "We have ___ time, so we must hurry.",
                "options": ["few", "a few", "little", "a little"],
                "answer": "little",
                "explanation": "Времени почти нет.",
            },

            {
                "order": 23,
                "prompt": "She spends so ___ money on clothes.",
                "options": ["many", "much", "few", "a few"],
                "answer": "much",
                "explanation": "Money — неисчисляемое: so much money.",
            },

            {
                "order": 24,
                "prompt": "Why are there so ___ people here?",
                "options": ["much", "many", "little", "a little"],
                "answer": "many",
                "explanation": "People — исчисляемое множественное число: so many people.",
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
                "✅ A1 Lesson 5 seeded: "
                "Much, many, a lot of, few, "
                "a few, little, a little"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
