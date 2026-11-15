from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 8: this, that, these, those."
    )


    def handle(
        self,
        *args,
        **options,
    ):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=8,

                defaults={
                    "title":
                        "Указательные местоимения "
                        "THIS, THAT, THESE, THOSE",

                    "slug":
                        "this-that-these-those",

                    "theory_text":
                        "Demonstratives: this, that, "
                        "these, those.",

                    "estimated_minutes":
                        14,

                    "pass_score":
                        70,

                    "xp_reward":
                        100,

                    "is_published":
                        True,
                },
            )
        )


        # =================================================
        # 8 MICRO-RULES
        # =================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Главная схема: близко или далеко?",

                "body":
                    """Нужно определить две вещи:

1. Один предмет или несколько?
2. Близко он или далеко?

Главная схема:

THIS
один + близко

THAT
один + далеко

THESE
несколько + близко

THOSE
несколько + далеко

Примеры:

this book
эта книга рядом

that house
тот дом далеко

these keys
эти ключи рядом

those mountains
те горы далеко.""",
            },


            {
                "order": 2,

                "title":
                    "THIS и THAT — один предмет",

                "body":
                    """THIS используется с одним предметом рядом:

this phone
this chair
this apple

This phone is mine.

THAT используется с одним предметом дальше:

that car
that tree
that building

That car is expensive.

Запомни:

THIS = singular + near

THAT = singular + far.""",
            },


            {
                "order": 3,

                "title":
                    "THESE и THOSE — несколько предметов",

                "body":
                    """THESE используется с несколькими предметами рядом:

these books
these apples
these students

These books are mine.

THOSE — с несколькими предметами далеко:

those houses
those people
those mountains

Those houses are new.

Запомни:

THESE = plural + near

THOSE = plural + far.""",
            },


            {
                "order": 4,

                "title":
                    "THIS IS, THAT IS, THESE ARE, THOSE ARE",

                "body":
                    """THIS и THAT обозначают один предмет, поэтому:

this is

that is

This is my bag.

That is our school.

THESE и THOSE обозначают несколько предметов:

these are

those are

These are my keys.

Those are my friends.

Не:

these is

those is

this are.""",
            },


            {
                "order": 5,

                "title":
                    "Перед существительным или самостоятельно",

                "body":
                    """Эти слова могут стоять перед существительным:

this book

that teacher

these students

those houses

Но могут использоваться и самостоятельно:

This is mine.

That is expensive.

These are fresh.

Those are yours.

Сравни:

This book is mine.

This is mine.""",
            },


            {
                "order": 6,

                "title":
                    "Вопросы, ответы и отрицания",

                "body":
                    """Один предмет:

Is this your phone?

Is that your car?

Краткий ответ:

Yes, it is.

No, it isn't.

Несколько предметов:

Are these your keys?

Are those your books?

Ответ:

Yes, they are.

No, they aren't.

Отрицание:

This isn't my bag.

That isn't our car.

These aren't my books.

Those aren't our children.""",
            },


            {
                "order": 7,

                "title":
                    "THIS и THAT могут говорить о времени",

                "body":
                    """THIS часто относится к текущему времени:

this week

this month

this year

this morning

I am busy this week.

THAT может относиться к более далёкому или прошлому времени:

that day

that year

at that time

I remember that day.

Также:

these days
в наши дни

those days
в те дни.""",
            },


            {
                "order": 8,

                "title":
                    "Телефон, знакомство и целая ситуация",

                "body":
                    """При представлении человека:

This is my friend, Marat.

This is our new teacher.

По телефону:

Hello, this is Aigul.

Who is this?

THIS может относиться к текущей ситуации:

This is difficult.

This is a good idea.

THAT часто относится к тому, что уже сказали:

That is true.

That is a good question.

I didn't know that.

То есть THIS и THAT используются не только для физических предметов.""",
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


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "___ is my phone here on the table.",

                "options": [
                    "These",
                    "Those",
                    "This",
                    "They",
                ],

                "answer":
                    "This",

                "explanation":
                    "Phone — один предмет рядом.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "___ mountains in the distance are beautiful.",

                "options": [
                    "This",
                    "That",
                    "These",
                    "Those",
                ],

                "answer":
                    "Those",

                "explanation":
                    "Mountains — несколько объектов далеко.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "___ pen in my hand is blue.",

                "options": [
                    "This",
                    "These",
                    "Those",
                    "They",
                ],

                "answer":
                    "This",

                "explanation":
                    "Pen — один предмет рядом.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Look at ___ house on the hill.",

                "options": [
                    "these",
                    "this",
                    "those",
                    "that",
                ],

                "answer":
                    "that",

                "explanation":
                    "House — один объект далеко.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "___ apples here are fresh.",

                "options": [
                    "This",
                    "These",
                    "That",
                    "It",
                ],

                "answer":
                    "These",

                "explanation":
                    "Apples — несколько предметов рядом.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "___ people over there are waiting for the bus.",

                "options": [
                    "This",
                    "That",
                    "These",
                    "Those",
                ],

                "answer":
                    "Those",

                "explanation":
                    "People — множественное число, находятся далеко.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "fill",

                "prompt":
                    "___ this your bag?",

                "options": [],

                "answer":
                    "Is",

                "explanation":
                    "THIS обозначает один предмет → IS.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "fill",

                "prompt":
                    "___ these your keys?",

                "options": [],

                "answer":
                    "Are",

                "explanation":
                    "THESE обозначает несколько предметов → ARE.",
            },


            {
                "order": 9,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "This are my books.",
                    "These is my books.",
                    "These are my books.",
                    "This is my books.",
                ],

                "answer":
                    "These are my books.",

                "explanation":
                    "BOOKS — множественное число, поэтому THESE ARE.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Which sentence is correct?",

                "options": [
                    "This book is mine.",
                    "This books is mine.",
                    "These book is mine.",
                    "Those book are mine.",
                ],

                "answer":
                    "This book is mine.",

                "explanation":
                    "THIS используется с существительным в единственном числе.",
            },


            {
                "order": 11,
                "section": 5,
                "type": "build",

                "prompt":
                    "Собери правильное предложение.",

                "options": [
                    "Those",
                    "are",
                    "yours",
                ],

                "answer":
                    "Those are yours",

                "explanation":
                    "THOSE может использоваться самостоятельно с ARE.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Is that your car?",

                "options": [
                    "Yes, that is.",
                    "Yes, it is.",
                    "Yes, they are.",
                    "Yes, this is.",
                ],

                "answer":
                    "Yes, it is.",

                "explanation":
                    "Car — один предмет, поэтому в кратком ответе IT.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Are those your books?",

                "options": [
                    "Yes, it is.",
                    "Yes, those is.",
                    "Yes, they are.",
                    "Yes, this is.",
                ],

                "answer":
                    "Yes, they are.",

                "explanation":
                    "Books — множественное число, поэтому THEY.",
            },


            {
                "order": 14,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "These isn't my shoes.",
                    "These aren't my shoes.",
                    "These not my shoes.",
                    "This aren't my shoes.",
                ],

                "answer":
                    "These aren't my shoes.",

                "explanation":
                    "THESE требует ARE / AREN'T.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I am very busy ___ week.",

                "options": [
                    "those",
                    "that",
                    "this",
                    "these",
                ],

                "answer":
                    "this",

                "explanation":
                    "THIS WEEK относится к текущей неделе.",
            },


            {
                "order": 16,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Life was different in ___ days.",

                "options": [
                    "this",
                    "these",
                    "those",
                    "it",
                ],

                "answer":
                    "those",

                "explanation":
                    "THOSE DAYS означает «в те дни».",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "___ is my brother, Marat.",

                "options": [
                    "These",
                    "This",
                    "Those",
                    "They",
                ],

                "answer":
                    "This",

                "explanation":
                    "При представлении одного человека используется THIS IS.",
            },


            {
                "order": 18,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Who is ___? (on the phone)",

                "options": [
                    "these",
                    "this",
                    "those",
                    "they",
                ],

                "answer":
                    "this",

                "explanation":
                    "По телефону обычно спрашивают WHO IS THIS?",
            },


            {
                "order": 19,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Someone says: 'English grammar is difficult.' You agree: '___ is true.'",

                "options": [
                    "These",
                    "Those",
                    "That",
                    "They",
                ],

                "answer":
                    "That",

                "explanation":
                    "THAT может относиться к тому, что только что было сказано.",
            },


            {
                "order": 20,
                "section": 8,
                "type": "choice",

                "prompt":
                    "You have a new idea right now. You say: '___ is a good idea.'",

                "options": [
                    "This",
                    "Those",
                    "These",
                    "They",
                ],

                "answer":
                    "This",

                "explanation":
                    "THIS может обозначать текущую ситуацию или идею.",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "___ notebook here belongs to me.",

                "options": [
                    "This",
                    "That",
                    "These",
                    "Those",
                ],

                "answer":
                    "This",

                "explanation":
                    "Notebook — один предмет рядом.",
            },


            {
                "order": 22,

                "prompt":
                    "___ building over there is our university.",

                "options": [
                    "This",
                    "These",
                    "Those",
                    "That",
                ],

                "answer":
                    "That",

                "explanation":
                    "Building — один объект далеко.",
            },


            {
                "order": 23,

                "prompt":
                    "___ flowers here are beautiful.",

                "options": [
                    "This",
                    "That",
                    "These",
                    "It",
                ],

                "answer":
                    "These",

                "explanation":
                    "Flowers — несколько предметов рядом.",
            },


            {
                "order": 24,

                "prompt":
                    "Look at ___ cars across the street.",

                "options": [
                    "this",
                    "that",
                    "these",
                    "those",
                ],

                "answer":
                    "those",

                "explanation":
                    "Cars — множественное число и находятся далеко.",
            },


            {
                "order": 25,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "That are my teacher.",
                    "That is my teacher.",
                    "Those is my teacher.",
                    "These is my teacher.",
                ],

                "answer":
                    "That is my teacher.",

                "explanation":
                    "THAT обозначает один объект и требует IS.",
            },


            {
                "order": 26,

                "prompt":
                    "Are these your documents?",

                "options": [
                    "Yes, it is.",
                    "Yes, this is.",
                    "Yes, they are.",
                    "Yes, these is.",
                ],

                "answer":
                    "Yes, they are.",

                "explanation":
                    "Documents — множественное число, поэтому THEY ARE.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "That aren't my car.",
                    "That isn't my car.",
                    "Those isn't my car.",
                    "That not my car.",
                ],

                "answer":
                    "That isn't my car.",

                "explanation":
                    "THAT требует IS / ISN'T.",
            },


            {
                "order": 28,

                "prompt":
                    "We are working very hard ___ month.",

                "options": [
                    "this",
                    "that",
                    "these",
                    "those",
                ],

                "answer":
                    "this",

                "explanation":
                    "THIS MONTH означает текущий месяц.",
            },


            {
                "order": 29,

                "prompt":
                    "I remember ___ days very well.",

                "options": [
                    "this",
                    "that",
                    "these",
                    "those",
                ],

                "answer":
                    "those",

                "explanation":
                    "THOSE DAYS относится к прошлому периоду.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "This is my bag, and those are my shoes.",
                    "These is my bag, and that are my shoes.",
                    "This are my bag, and those is my shoes.",
                    "Those is my bag, and this are my shoes.",
                ],

                "answer":
                    "This is my bag, and those are my shoes.",

                "explanation":
                    "THIS + singular + IS; THOSE + plural + ARE.",
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
                "✅ Interactive A1 Lesson 8 seeded"
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
