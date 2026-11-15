from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 17: Prepositions of place."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=17,

                defaults={
                    "title":
                        "Предлоги места",

                    "slug":
                        "prepositions-of-place",

                    "theory_text":
                        "Prepositions of place.",

                    "estimated_minutes":
                        18,

                    "pass_score":
                        70,

                    "xp_reward":
                        100,

                    "is_published":
                        True,
                },
            )
        )


        # ================================================
        # 10 MICRO-RULES
        # ================================================

        sections = [

            {
                "order": 1,

                "title":
                    "IN — внутри",

                "body":
                    """IN показывает, что человек или предмет находится внутри пространства.

in the room

in the box

in the bag

in the garden

Примеры:

The children are in the room.

The keys are in the bag.

There is milk in the fridge.

IN также используется с городами, странами и большими территориями:

in Kazakhstan

in Karaganda

in London

in Europe.""",
            },


            {
                "order": 2,

                "title":
                    "ON — на поверхности",

                "body":
                    """ON используется, когда предмет находится на поверхности.

on the table

on the floor

on the shelf

on the wall

Примеры:

The book is on the table.

The phone is on the chair.

The picture is on the wall.

Даже если поверхность вертикальная:

a picture on the wall

a notice on the door.""",
            },


            {
                "order": 3,

                "title":
                    "AT — конкретная точка",

                "body":
                    """AT часто показывает конкретное место как точку.

at home

at work

at school

at the bus stop

at the door

at the station

Примеры:

I am at home.

She is at work.

They are waiting at the bus stop.

Сравни:

I am at school.
Школа как место деятельности.

I am in the school.
Физически внутри здания.""",
            },


            {
                "order": 4,

                "title":
                    "Транспорт: IN или ON?",

                "body":
                    """С автомобилем и такси обычно:

in a car

in a taxi

She is in the car.

С общественным транспортом:

on a bus

on a train

on a plane

on a ship

We are on the bus.

Но когда говорим о способе передвижения:

by car

by bus

by train

Сравни:

I go to work by car.

I am in the car.""",
            },


            {
                "order": 5,

                "title":
                    "UNDER, ABOVE, BELOW",

                "body":
                    """UNDER = под.

The cat is under the table.

The shoes are under the bed.

ABOVE = выше / над.

The picture is above the sofa.

The plane is above the clouds.

BELOW = ниже.

The shelf is below the picture.

The temperature is below zero.

Для базового уровня:

UNDER → прямо под

BELOW → ниже по уровню.""",
            },


            {
                "order": 6,

                "title":
                    "BEHIND и IN FRONT OF",

                "body":
                    """BEHIND означает «за / позади».

The garden is behind the house.

The child is behind the door.

IN FRONT OF означает «перед».

There is a tree in front of the house.

The students are in front of the school.

Запомни полную конструкцию:

in front OF

Не:

in front the house.""",
            },


            {
                "order": 7,

                "title":
                    "NEXT TO, NEAR и OPPOSITE",

                "body":
                    """NEXT TO = непосредственно рядом.

The pharmacy is next to the hospital.

The lamp is next to the bed.

NEAR = недалеко от.

I live near the university.

There is a shop near our house.

Разница:

NEXT TO → прямо рядом

NEAR → недалеко

OPPOSITE = напротив.

The bank is opposite the school.

The café is opposite the park.""",
            },


            {
                "order": 8,

                "title":
                    "BETWEEN или AMONG?",

                "body":
                    """BETWEEN обычно используется между двумя объектами:

between the bank and the café

between two houses

The pharmacy is between the bank and the shop.

Формула:

between A and B

AMONG означает «среди» группы:

among the students

among the trees

among friends

Сравни:

between two houses

among many houses.""",
            },


            {
                "order": 9,

                "title":
                    "CORNER, LEFT и RIGHT",

                "body":
                    """IN THE CORNER = в углу помещения.

There is a chair in the corner of the room.

AT THE CORNER = на углу улицы.

There is a shop at the corner of the street.

Другие полезные выражения:

on the left

on the right

to the left of

to the right of

The bank is on the left.

The shop is to the right of the school.""",
            },


            {
                "order": 10,

                "title":
                    "WHERE + THERE IS / ARE",

                "body":
                    """Предлоги места часто используются вместе с THERE IS / THERE ARE.

There is a book on the table.

There is a cat under the chair.

There are two shops near the school.

There is a bank opposite the park.

Чтобы спросить о месте:

Where is the book?

It is on the table.

Where are the children?

They are in the garden.

Главный вопрос:

предмет внутри?
→ IN

на поверхности?
→ ON

в конкретной точке?
→ AT

рядом?
→ NEXT TO / NEAR

между?
→ BETWEEN.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects
                .update_or_create(
                    lesson=lesson,
                    order=data["order"],

                    defaults={
                        "title":
                            data["title"],

                        "body":
                            data["body"],
                    },
                )
            )

            section_objects[
                data["order"]
            ] = section


        # ================================================
        # 20 TRAINING EXERCISES
        # ================================================

        training = [

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "The students are ___ the classroom.",

                "options": [
                    "on",
                    "in",
                    "at",
                    "under",
                ],

                "answer":
                    "in",

                "explanation":
                    "Они находятся внутри комнаты → IN.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "My keys are ___ my bag.",

                "options": [
                    "in",
                    "on",
                    "above",
                    "opposite",
                ],

                "answer":
                    "in",

                "explanation":
                    "Ключи находятся внутри сумки → IN.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "The book is ___ the table.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "among",
                ],

                "answer":
                    "on",

                "explanation":
                    "Книга находится на поверхности → ON.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "There is a picture ___ the wall.",

                "options": [
                    "in",
                    "on",
                    "under",
                    "among",
                ],

                "answer":
                    "on",

                "explanation":
                    "С поверхностью стены используется ON.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "I am ___ home.",

                "options": [],

                "answer":
                    "at",

                "explanation":
                    "Устойчивое выражение: AT HOME.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "They are waiting ___ the bus stop.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "under",
                ],

                "answer":
                    "at",

                "explanation":
                    "Bus stop рассматривается как точка → AT.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She is ___ the car.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "above",
                ],

                "answer":
                    "in",

                "explanation":
                    "С машиной обычно IN THE CAR.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "We are ___ the train.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "under",
                ],

                "answer":
                    "on",

                "explanation":
                    "С поездом как общественным транспортом → ON.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "The cat is ___ the table.",

                "options": [
                    "under",
                    "above",
                    "opposite",
                    "among",
                ],

                "answer":
                    "under",

                "explanation":
                    "Кошка находится прямо под столом → UNDER.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "The picture is ___ the sofa.",

                "options": [
                    "above",
                    "below",
                    "in",
                    "among",
                ],

                "answer":
                    "above",

                "explanation":
                    "Картина расположена выше дивана → ABOVE.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "The garden is ___ the house.",

                "options": [
                    "behind",
                    "between",
                    "on",
                    "among",
                ],

                "answer":
                    "behind",

                "explanation":
                    "BEHIND означает «позади / за».",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Choose the correct phrase.",

                "options": [
                    "in front the house",
                    "in front of the house",
                    "in the front the house",
                    "front of house",
                ],

                "answer":
                    "in front of the house",

                "explanation":
                    "Правильная конструкция — IN FRONT OF.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "The pharmacy is directly beside the hospital. It is ___ the hospital.",

                "options": [
                    "near",
                    "next to",
                    "opposite",
                    "below",
                ],

                "answer":
                    "next to",

                "explanation":
                    "Непосредственно рядом → NEXT TO.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "The cinema is across the street from the bank. It is ___ the bank.",

                "options": [
                    "opposite",
                    "behind",
                    "among",
                    "under",
                ],

                "answer":
                    "opposite",

                "explanation":
                    "Через дорогу напротив → OPPOSITE.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "The café is ___ the bank and the pharmacy.",

                "options": [
                    "between",
                    "among",
                    "under",
                    "opposite",
                ],

                "answer":
                    "between",

                "explanation":
                    "Между двумя объектами → BETWEEN.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "The small house is hidden ___ the trees.",

                "options": [
                    "between",
                    "among",
                    "on",
                    "at",
                ],

                "answer":
                    "among",

                "explanation":
                    "Среди группы деревьев → AMONG.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "There is a chair ___ the corner of the room.",

                "options": [
                    "in",
                    "at",
                    "on",
                    "between",
                ],

                "answer":
                    "in",

                "explanation":
                    "В углу комнаты → IN THE CORNER.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "There is a café ___ the corner of King Street.",

                "options": [
                    "in",
                    "at",
                    "under",
                    "among",
                ],

                "answer":
                    "at",

                "explanation":
                    "На углу улицы → AT THE CORNER.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "There are two shops ___ the school.",

                "options": [
                    "near",
                    "near to",
                    "under",
                    "among",
                ],

                "answer":
                    "near",

                "explanation":
                    "Для базового варианта: NEAR THE SCHOOL.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "build",

                "prompt":
                    "Собери правильное предложение.",

                "options": [
                    "There",
                    "is",
                    "a",
                    "lamp",
                    "next",
                    "to",
                    "the",
                    "bed",
                ],

                "answer":
                    "There is a lamp next to the bed",

                "explanation":
                    "THERE IS + предмет + NEXT TO + место.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "The children are ___ the garden.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "above",
                ],

                "answer":
                    "in",

                "explanation":
                    "Они находятся внутри пространства сада → IN.",
            },


            {
                "order": 22,

                "prompt":
                    "Your phone is ___ the desk.",

                "options": [
                    "on",
                    "in",
                    "among",
                    "behind of",
                ],

                "answer":
                    "on",

                "explanation":
                    "Телефон находится на поверхности стола → ON.",
            },


            {
                "order": 23,

                "prompt":
                    "Someone is ___ the door.",

                "options": [
                    "at",
                    "in",
                    "on",
                    "between",
                ],

                "answer":
                    "at",

                "explanation":
                    "Устойчивая конструкция: AT THE DOOR.",
            },


            {
                "order": 24,

                "prompt":
                    "They are ___ the bus now.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "under",
                ],

                "answer":
                    "on",

                "explanation":
                    "С автобусом как общественным транспортом → ON.",
            },


            {
                "order": 25,

                "prompt":
                    "The shoes are ___ the bed.",

                "options": [
                    "under",
                    "above",
                    "opposite",
                    "among",
                ],

                "answer":
                    "under",

                "explanation":
                    "Обувь находится под кроватью → UNDER.",
            },


            {
                "order": 26,

                "prompt":
                    "There is a tree ___ the house, not behind it.",

                "options": [
                    "in front of",
                    "among",
                    "between",
                    "below",
                ],

                "answer":
                    "in front of",

                "explanation":
                    "Противоположность BEHIND здесь — IN FRONT OF.",
            },


            {
                "order": 27,

                "prompt":
                    "The bank is directly beside the hotel.",

                "options": [
                    "The bank is next to the hotel.",
                    "The bank is opposite the hotel.",
                    "The bank is among the hotel.",
                    "The bank is below the hotel.",
                ],

                "answer":
                    "The bank is next to the hotel.",

                "explanation":
                    "Directly beside = NEXT TO.",
            },


            {
                "order": 28,

                "prompt":
                    "The school is ___ the bank and the supermarket.",

                "options": [
                    "between",
                    "among",
                    "near to",
                    "under",
                ],

                "answer":
                    "between",

                "explanation":
                    "Два конкретных объекта → BETWEEN.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "The café is opposite the station.",
                    "The café is opposite to the station.",
                    "The café is in opposite the station.",
                    "The café is opposite of the station.",
                ],

                "answer":
                    "The café is opposite the station.",

                "explanation":
                    "Для базовой конструкции используется OPPOSITE без TO или OF.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct pair.",

                "options": [
                    "The book is on the table. / The keys are in the bag.",
                    "The book is in the table. / The keys are on the bag.",
                    "The book is at the table surface. / The keys are above the bag.",
                    "The book is among the table. / The keys are opposite the bag.",
                ],

                "answer":
                    "The book is on the table. / The keys are in the bag.",

                "explanation":
                    "На поверхности → ON; внутри → IN.",
            },

        ]


        valid_orders = []


        for data in (
            training
            +
            final_test
        ):

            valid_orders.append(
                data["order"]
            )


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
                        data.get(
                            "type",
                            "choice",
                        ),

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
                "✅ Interactive A1 Lesson 17 seeded"
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
