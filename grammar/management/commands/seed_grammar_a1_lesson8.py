from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 8: "
        "This, that, these, those."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=8,
            defaults={
                "title": (
                    "Указательные местоимения "
                    "THIS, THAT, THESE, THOSE"
                ),
                "slug": "this-that-these-those",
                "theory_text": (
                    "Demonstratives: this, that, "
                    "these, those."
                ),
                "estimated_minutes": 25,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое THIS, THAT, THESE, THOSE",
                "body": """Указательные местоимения помогают показать на человека, предмет или несколько предметов.

В английском используются четыре слова:

this — этот, эта, это;
that — тот, та, то;
these — эти;
those — те.

Выбор зависит от двух вещей:

1. предмет один или их несколько;
2. предмет находится близко или далеко.

Главная таблица:

Близко + один предмет → this

Далеко + один предмет → that

Близко + несколько предметов → these

Далеко + несколько предметов → those.""",
            },

            {
                "order": 2,
                "title": "THIS",
                "body": """This используется, когда предмет один и находится рядом с говорящим.

Примеры:

this book;
this phone;
this chair;
this apple.

Предложения:

This book is interesting.

This phone is new.

This is my bag.

Запомните:

THIS = один предмет + близко.""",
            },

            {
                "order": 3,
                "title": "THAT",
                "body": """That используется, когда предмет один и находится далеко от говорящего.

Примеры:

that house;
that car;
that tree;
that man.

Предложения:

That house is very old.

That car belongs to my brother.

That is our school.

Запомните:

THAT = один предмет + далеко.""",
            },

            {
                "order": 4,
                "title": "THESE",
                "body": """These используется, когда предметов несколько и они находятся рядом.

Примеры:

these books;
these apples;
these students;
these chairs.

Предложения:

These books are mine.

These apples are fresh.

These are my keys.

Запомните:

THESE = несколько предметов + близко.""",
            },

            {
                "order": 5,
                "title": "THOSE",
                "body": """Those используется, когда предметов несколько и они находятся далеко.

Примеры:

those houses;
those cars;
those people;
those mountains.

Предложения:

Those houses are new.

Those people are waiting for the bus.

Those are my friends.

Запомните:

THOSE = несколько предметов + далеко.""",
            },

            {
                "order": 6,
                "title": "Единственное и множественное число",
                "body": """После this и that используется существительное в единственном числе:

this book;
that student;
this apple;
that house.

После these и those используется множественное число:

these books;
those students;
these apples;
those houses.

Неправильно:

this books;
that students;
these book;
those student.

Важно:

this → these

that → those

Это отдельные формы, а не просто добавление окончания.""",
            },

            {
                "order": 7,
                "title": "IS или ARE",
                "body": """This и that обозначают один предмет, поэтому используются с is:

This is a book.

That is my car.

This is interesting.

That is our teacher.

These и those обозначают несколько предметов, поэтому используются с are:

These are books.

Those are my friends.

These are new.

Those are expensive.

Запомните:

this is;
that is;
these are;
those are.""",
            },

            {
                "order": 8,
                "title": "Перед существительным и самостоятельно",
                "body": """This, that, these и those могут стоять перед существительным:

this book;
that teacher;
these students;
those houses.

This book is useful.

Those houses are expensive.

Но они также могут использоваться самостоятельно:

This is mine.

That is expensive.

These are fresh.

Those are yours.

Сравните:

This book is mine.

This is mine.

Оба варианта правильные.""",
            },

            {
                "order": 9,
                "title": "Вопросы и краткие ответы",
                "body": """С одним предметом:

Is this ...?

Is that ...?

Примеры:

Is this your phone?

Is that your house?

Краткий ответ:

Yes, it is.

No, it isn't.

После того как предмет уже назван, в кратком ответе используется it.

С несколькими предметами:

Are these ...?

Are those ...?

Are these your keys?

Are those your children?

Краткий ответ:

Yes, they are.

No, they aren't.

Для нескольких предметов используется they.""",
            },

            {
                "order": 10,
                "title": "Отрицательные предложения",
                "body": """Отрицание с this и that:

This is not my bag.

This isn't my bag.

That is not our car.

That isn't our car.

Отрицание с these и those:

These are not my books.

These aren't my books.

Those are not our children.

Those aren't our children.

Запомните:

this/that → is not

these/those → are not.""",
            },

            {
                "order": 11,
                "title": "THIS и THAT со временем",
                "body": """This может относиться не только к физически близкому предмету, но и к текущему времени.

Примеры:

this week;
this month;
this year;
this morning.

I am very busy this week.

We moved here this year.

That может относиться к более далёкому или прошлому времени:

that day;
that year;
at that time;
that morning.

I remember that day.

We were living in London that year.

Также:

these days = в наши дни, сейчас

those days = в те дни, тогда.""",
            },

            {
                "order": 12,
                "title": "THIS при знакомстве и по телефону",
                "body": """При представлении человека часто используется:

This is ...

Примеры:

This is my wife, Aigul.

This is my friend, Marat.

This is our new teacher.

По телефону говорящий может сказать:

Hello, this is Marat.

This is Aigul speaking.

Чтобы спросить, кто говорит:

Who is this?

В телефонном разговоре this обычно относится к говорящему, а that — к собеседнику.""",
            },

            {
                "order": 13,
                "title": "THIS и THAT для ситуации",
                "body": """This и that могут относиться не к конкретному предмету, а ко всей ситуации.

THIS — текущая ситуация:

This is difficult.

This is a good idea.

This is not fair.

THAT — то, что уже сказали или что произошло:

That is true.

That was interesting.

That is a good question.

I did not know that.""",
            },

            {
                "order": 14,
                "title": "Как быстро выбрать правильное слово",
                "body": """Шаг 1. Сколько предметов?

Один:

this;
that.

Несколько:

these;
those.

Шаг 2. Где предмет?

Близко:

this;
these.

Далеко:

that;
those.

Примеры:

Одна ручка рядом:

This is a pen.

Одна ручка далеко:

That is a pen.

Несколько ручек рядом:

These are pens.

Несколько ручек далеко:

Those are pens.

И не забывайте:

this is;
that is;
these are;
those are.""",
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
                "prompt": "___ is my phone here on the table.",
                "options": ["These", "Those", "This", "They"],
                "answer": "This",
                "explanation": "Phone — один предмет и находится рядом.",
            },

            {
                "order": 2,
                "prompt": "___ is our school over there.",
                "options": ["This", "These", "Those", "That"],
                "answer": "That",
                "explanation": "School — один объект, находящийся далеко.",
            },

            {
                "order": 3,
                "prompt": "___ books here are mine.",
                "options": ["This", "That", "These", "It"],
                "answer": "These",
                "explanation": "Books — множественное число, предметы рядом.",
            },

            {
                "order": 4,
                "prompt": "___ mountains in the distance are beautiful.",
                "options": ["This", "Those", "That", "It"],
                "answer": "Those",
                "explanation": "Mountains — множественное число и находятся далеко.",
            },

            {
                "order": 5,
                "prompt": "___ this your bag?",
                "options": ["Are", "Is", "Am", "Be"],
                "answer": "Is",
                "explanation": "This обозначает один предмет: Is this...?",
            },

            {
                "order": 6,
                "prompt": "___ these your keys?",
                "options": ["Is", "Am", "Are", "Be"],
                "answer": "Are",
                "explanation": "These обозначает несколько предметов: Are these...?",
            },

            {
                "order": 7,
                "prompt": "Is that your car?",
                "options": [
                    "Yes, that is.",
                    "Yes, it is.",
                    "Yes, they are.",
                    "Yes, this is.",
                ],
                "answer": "Yes, it is.",
                "explanation": "Car — один предмет, поэтому в кратком ответе используется it.",
            },

            {
                "order": 8,
                "prompt": "Are those your books?",
                "options": [
                    "Yes, it is.",
                    "Yes, those is.",
                    "Yes, they are.",
                    "Yes, this is.",
                ],
                "answer": "Yes, they are.",
                "explanation": "Books — множественное число, поэтому используется they.",
            },

            {
                "order": 9,
                "prompt": "___ pen in my hand is blue.",
                "options": ["This", "These", "Those", "They"],
                "answer": "This",
                "explanation": "Pen — один предмет рядом.",
            },

            {
                "order": 10,
                "prompt": "___ building across the street is a bank.",
                "options": ["These", "Those", "That", "They"],
                "answer": "That",
                "explanation": "Building — один объект и находится дальше.",
            },

            {
                "order": 11,
                "prompt": "___ apples on the table are fresh.",
                "options": ["This", "These", "That", "It"],
                "answer": "These",
                "explanation": "Apples — несколько предметов рядом.",
            },

            {
                "order": 12,
                "prompt": "___ birds in the sky are flying south.",
                "options": ["This", "That", "Those", "It"],
                "answer": "Those",
                "explanation": "Birds — множественное число, и они находятся далеко.",
            },

            {
                "order": 13,
                "prompt": "___ is my brother, Marat.",
                "options": ["These", "This", "Those", "They"],
                "answer": "This",
                "explanation": "При представлении одного человека используется This is...",
            },

            {
                "order": 14,
                "prompt": "___ are my parents.",
                "options": ["This", "That", "It", "These"],
                "answer": "These",
                "explanation": "Parents — множественное число.",
            },

            {
                "order": 15,
                "prompt": "Is ___ your coat here?",
                "options": ["these", "those", "this", "they"],
                "answer": "this",
                "explanation": "Coat — один предмет рядом.",
            },

            {
                "order": 16,
                "prompt": "Are ___ your children over there?",
                "options": ["this", "that", "those", "it"],
                "answer": "those",
                "explanation": "Children — множественное число и находятся далеко.",
            },

            {
                "order": 17,
                "prompt": "___ is a very interesting question.",
                "options": ["Those", "These", "That", "They"],
                "answer": "That",
                "explanation": "That может относиться к сказанному или заданному вопросу.",
            },

            {
                "order": 18,
                "prompt": "I am very busy ___ week.",
                "options": ["those", "that", "this", "these"],
                "answer": "this",
                "explanation": "This week относится к текущей неделе.",
            },

            {
                "order": 19,
                "prompt": "Life was difficult in ___ days.",
                "options": ["this", "these", "those", "it"],
                "answer": "those",
                "explanation": "Those days означает «в те дни».",
            },

            {
                "order": 20,
                "prompt": "Who is ___? (on the phone)",
                "options": ["these", "this", "those", "they"],
                "answer": "this",
                "explanation": "По телефону используется выражение Who is this?",
            },

            {
                "order": 21,
                "prompt": "___ books are new, but those books are old.",
                "options": ["This", "These", "That", "It"],
                "answer": "These",
                "explanation": "Books — множественное число; противопоставление these / those.",
            },

            {
                "order": 22,
                "prompt": "Look at ___ house on the hill.",
                "options": ["these", "this", "those", "that"],
                "answer": "that",
                "explanation": "House — один объект, находящийся далеко.",
            },

            {
                "order": 23,
                "prompt": "Are these your documents?",
                "options": [
                    "Yes, it is.",
                    "Yes, this is.",
                    "Yes, they are.",
                    "Yes, these is.",
                ],
                "answer": "Yes, they are.",
                "explanation": "Documents — множественное число, поэтому they are.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "This are my books.",
                    "These is my books.",
                    "These are my books.",
                    "This is my books.",
                ],
                "answer": "These are my books.",
                "explanation": "Books — множественное число, поэтому нужны these + are.",
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
                "✅ A1 Lesson 8 seeded: "
                "THIS, THAT, THESE, THOSE"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
