from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 17: "
        "Prepositions of place."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=17,
            defaults={
                "title": "Предлоги места",
                "slug": "prepositions-of-place",
                "theory_text": "Prepositions of place.",
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое предлоги места",
                "body": """Предлоги места показывают, где находится человек, животное или предмет.

Основные слова:

in — в, внутри;

on — на;

under — под;

behind — позади, за;

in front of — перед;

next to — рядом с;

between — между;

among — среди;

opposite — напротив;

near — около;

above — над;

below — ниже;

at — в определённой точке.""",
            },

            {
                "order": 2,
                "title": "IN",
                "body": """IN означает, что кто-то или что-то находится внутри пространства.

Примеры:

in the room;

in the box;

in the bag;

in the garden.

Предложения:

The children are in the room.

The keys are in the bag.

There is some milk in the fridge.

IN также используется с городами и странами:

in Kazakhstan;

in Astana;

in London;

in Europe.""",
            },

            {
                "order": 3,
                "title": "IN и транспорт",
                "body": """IN часто используется с небольшим личным транспортом:

in a car;

in a taxi.

Примеры:

She is in the car.

We are in a taxi.

Но если говорим о способе передвижения:

by car;

by taxi.

Сравните:

I go to work by car.

I am in the car.""",
            },

            {
                "order": 4,
                "title": "ON",
                "body": """ON означает, что предмет находится на поверхности и соприкасается с ней.

Примеры:

on the table;

on the floor;

on the wall;

on the shelf;

on the chair.

Предложения:

The book is on the table.

The picture is on the wall.

Your phone is on the chair.

Даже с вертикальной поверхностью используется ON:

a picture on the wall;

a notice on the door.""",
            },

            {
                "order": 5,
                "title": "ON и транспорт",
                "body": """С общественным транспортом часто используется ON:

on the bus;

on the train;

on the plane;

on the ship.

Примеры:

She is on the bus.

We met on the train.

There were many people on the plane.

Сравните:

in a car;

on a bus.""",
            },

            {
                "order": 6,
                "title": "UNDER, ABOVE и BELOW",
                "body": """UNDER означает «под», обычно прямо под предметом.

The cat is under the table.

My shoes are under the bed.

ABOVE означает «выше / над».

The picture is above the sofa.

The plane is above the clouds.

BELOW означает «ниже».

The shelf is below the picture.

The temperature is below zero.

Для начала:

under = прямо под;

below = ниже по уровню.""",
            },

            {
                "order": 7,
                "title": "BEHIND и IN FRONT OF",
                "body": """BEHIND означает:

за;

позади.

The garden is behind the house.

The child is behind the door.

Не путайте behind с after.

Behind показывает место.

After показывает время или последовательность.

IN FRONT OF означает «перед».

There is a tree in front of the house.

The students are waiting in front of the school.

Сравните:

behind = сзади;

in front of = спереди.""",
            },

            {
                "order": 8,
                "title": "NEXT TO и NEAR",
                "body": """NEXT TO означает «непосредственно рядом».

Примеры:

next to the bank;

next to the school;

next to me.

The pharmacy is next to the hospital.

The lamp is next to the bed.

NEAR означает:

рядом;

около;

недалеко от.

I live near the university.

There is a shop near our house.

Разница:

next to = прямо рядом;

near = недалеко.

Для начального уровня используйте:

near the school

а не:

near to the school.""",
            },

            {
                "order": 9,
                "title": "BETWEEN и AMONG",
                "body": """BETWEEN означает «между».

Обычно используется с двумя объектами.

Формула:

between A and B

Примеры:

between the bank and the café;

between two houses.

The pharmacy is between the bank and the shop.

AMONG означает «среди».

Обычно речь идёт о группе или множестве объектов.

among the students;

among the trees;

among friends.

Сравните:

between two houses;

among many houses.""",
            },

            {
                "order": 10,
                "title": "OPPOSITE",
                "body": """OPPOSITE означает «напротив».

Примеры:

opposite the school;

opposite the bank;

opposite my house.

Предложения:

The café is opposite the bank.

Our office is opposite the park.

She sat opposite me.

Сравните:

The car is in front of the house.

The bank is opposite the school.

In front of — непосредственно перед.

Opposite — напротив, часто через дорогу.""",
            },

            {
                "order": 11,
                "title": "AT",
                "body": """AT используется, когда место рассматривается как точка или конкретное место.

Примеры:

at home;

at work;

at school;

at the bus stop;

at the door;

at the station.

Предложения:

I am at home.

She is at work.

They are waiting at the bus stop.

Someone is at the door.

Сравните:

I am at school.
— школа как место деятельности.

I am in the school.
— внутри здания школы.""",
            },

            {
                "order": 12,
                "title": "Полезные выражения с местом",
                "body": """IN THE CORNER:

в углу комнаты.

There is a chair in the corner of the room.

AT THE CORNER:

на углу улицы.

There is a shop at the corner of the street.

ON THE LEFT:

The bank is on the left.

ON THE RIGHT:

The pharmacy is on the right.

TO THE LEFT OF:

The bank is to the left of the café.

TO THE RIGHT OF:

The shop is to the right of the school.""",
            },

            {
                "order": 13,
                "title": "THERE IS / THERE ARE + место",
                "body": """Предлоги места часто используются вместе с there is / there are.

Примеры:

There is a book on the table.

There is a cat under the chair.

There are two shops near the school.

There is a bank opposite the park.

There are some trees behind the house.

Формула:

There is / There are
+
предмет
+
предлог места
+
место

Пример:

There is a lamp next to the bed.""",
            },

            {
                "order": 14,
                "title": "WHERE и типичные ошибки",
                "body": """Чтобы спросить о месте, используется WHERE.

Where is the book?

It is on the table.

Where are the children?

They are in the garden.

Типичные ошибки:

Неправильно:

The book is in the table.

Правильно:

The book is on the table.

Неправильно:

The children are on the room.

Правильно:

The children are in the room.

Неправильно:

between the bank to the shop.

Правильно:

between the bank and the shop.

Неправильно:

in front the house.

Правильно:

in front of the house.""",
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
                "prompt": "The students are ___ the classroom.",
                "options": ["on", "in", "under", "opposite"],
                "answer": "in",
                "explanation": "Students находятся внутри комнаты, поэтому in.",
            },

            {
                "order": 2,
                "prompt": "The books are ___ the shelf.",
                "options": ["in", "on", "behind", "between"],
                "answer": "on",
                "explanation": "Книги находятся на поверхности полки.",
            },

            {
                "order": 3,
                "prompt": "The shoes are ___ the bed.",
                "options": ["under", "above", "opposite", "in front of"],
                "answer": "under",
                "explanation": "Under означает «под».",
            },

            {
                "order": 4,
                "prompt": "The garage is ___ the house.",
                "options": ["behind", "on", "between", "in"],
                "answer": "behind",
                "explanation": "Behind означает «позади / за».",
            },

            {
                "order": 5,
                "prompt": "The bus stop is ___ the school.",
                "options": ["next to", "under", "in", "above"],
                "answer": "next to",
                "explanation": "Next to означает «непосредственно рядом».",
            },

            {
                "order": 6,
                "prompt": "The bank is ___ the post office and the café.",
                "options": ["behind", "between", "on", "under"],
                "answer": "between",
                "explanation": "Между двумя объектами используется between.",
            },

            {
                "order": 7,
                "prompt": "The cinema is ___ the supermarket, across the street.",
                "options": ["opposite", "in", "below", "among"],
                "answer": "opposite",
                "explanation": "Across the street указывает на значение «напротив».",
            },

            {
                "order": 8,
                "prompt": "The picture is ___ the sofa.",
                "options": ["above", "under", "in", "among"],
                "answer": "above",
                "explanation": "Above означает «выше / над».",
            },

            {
                "order": 9,
                "prompt": "The village is ___ the mountain.",
                "options": ["below", "on", "opposite", "next to"],
                "answer": "below",
                "explanation": "Below означает «ниже по уровню».",
            },

            {
                "order": 10,
                "prompt": "She is waiting ___ the bus stop.",
                "options": ["at", "in", "on", "under"],
                "answer": "at",
                "explanation": "Bus stop рассматривается как конкретная точка: at the bus stop.",
            },

            {
                "order": 11,
                "prompt": "I am ___ home.",
                "options": ["in", "at", "on", "between"],
                "answer": "at",
                "explanation": "Устойчивое выражение: at home.",
            },

            {
                "order": 12,
                "prompt": "They are ___ the bus.",
                "options": ["in", "on", "at", "behind"],
                "answer": "on",
                "explanation": "С общественным транспортом используется on.",
            },

            {
                "order": 13,
                "prompt": "He is ___ the car.",
                "options": ["in", "on", "at", "under"],
                "answer": "in",
                "explanation": "С машиной обычно используется in the car.",
            },

            {
                "order": 14,
                "prompt": "The house is hidden ___ the trees.",
                "options": ["between", "among", "on", "opposite"],
                "answer": "among",
                "explanation": "Among используется среди группы объектов.",
            },

            {
                "order": 15,
                "prompt": "The child is standing ___ his parents.",
                "options": ["among", "between", "above", "near to"],
                "answer": "between",
                "explanation": "Между двумя людьми: between.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct phrase.",
                "options": [
                    "between the bank to the shop",
                    "between the bank and the shop",
                    "between the bank with the shop",
                    "between bank at shop",
                ],
                "answer": "between the bank and the shop",
                "explanation": "Правильная конструкция: between A and B.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "The book is in the table.",
                    "The book is on the table.",
                    "The book is at the table surface.",
                    "The book is under the table top.",
                ],
                "answer": "The book is on the table.",
                "explanation": "На поверхности используется on.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct phrase.",
                "options": [
                    "in front the house",
                    "in front at the house",
                    "in front of the house",
                    "front of the house",
                ],
                "answer": "in front of the house",
                "explanation": "Правильная конструкция: in front of.",
            },

            {
                "order": 19,
                "prompt": "The bank is ___ the café. It is directly beside it.",
                "options": ["near", "next to", "below", "among"],
                "answer": "next to",
                "explanation": "Next to означает непосредственно рядом.",
            },

            {
                "order": 20,
                "prompt": "There are two shops ___ the school.",
                "options": ["near", "near to", "on", "under"],
                "answer": "near",
                "explanation": "Для начального уровня используем near без to.",
            },

            {
                "order": 21,
                "prompt": "There is a cat ___ the chair.",
                "options": ["under", "among", "opposite", "at"],
                "answer": "under",
                "explanation": "Кошка находится прямо под стулом.",
            },

            {
                "order": 22,
                "prompt": "Where is the book? — It is ___ the table.",
                "options": ["on", "in", "among", "behind of"],
                "answer": "on",
                "explanation": "Книга лежит на поверхности стола.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "The children are on the room.",
                    "The children are in the room.",
                    "The children are at inside the room.",
                    "The children are under the room.",
                ],
                "answer": "The children are in the room.",
                "explanation": "Внутри пространства используется in.",
            },

            {
                "order": 24,
                "prompt": "Which sentence means 'Банк находится напротив школы'?",
                "options": [
                    "The bank is behind the school.",
                    "The bank is opposite the school.",
                    "The bank is among the school.",
                    "The bank is under the school.",
                ],
                "answer": "The bank is opposite the school.",
                "explanation": "Opposite означает «напротив».",
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
                "✅ A1 Lesson 17 seeded: "
                "Предлоги места"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
