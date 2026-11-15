from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 5: quantity words."
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
                order=5,
                defaults={
                    "title":
                        "Much, many, a lot of, few, "
                        "a few, little, a little",

                    "slug":
                        "much-many-few-little",

                    "theory_text":
                        "Words of quantity.",

                    "estimated_minutes":
                        16,

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
        # 9 MICRO-RULES
        # =================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Сначала определи тип существительного",

                "body":
                    """Перед выбором слова количества сначала спроси:

существительное COUNTABLE или UNCOUNTABLE?

Countable plural:

books
students
friends
people
questions

Uncountable:

water
money
time
work
information

Сравни:

many books
much water

Не:

much books
many water

Это главное правило всего урока.""",
            },


            {
                "order": 2,

                "title":
                    "MANY — с исчисляемыми",

                "body":
                    """MANY означает «много» и используется с исчисляемыми существительными во множественном числе.

many books
many students
many questions
many people

Очень часто:

How many...?

How many students are there?

How many apples do you need?

Также MANY часто встречается в отрицаниях:

We don't have many chairs.

She doesn't ask many questions.""",
            },


            {
                "order": 3,

                "title":
                    "MUCH — с неисчисляемыми",

                "body":
                    """MUCH означает «много» и используется с неисчисляемыми существительными.

much money
much water
much time
much information
much work

Очень часто:

How much money do you need?

How much water do you drink?

В отрицаниях:

I don't have much money.

We don't have much time.

There isn't much milk.

Запомни:

How many books?

How much money?""",
            },


            {
                "order": 4,

                "title":
                    "A LOT OF — универсальный вариант",

                "body":
                    """A LOT OF можно использовать и с countable, и с uncountable nouns.

Countable:

a lot of books
a lot of students
a lot of people

Uncountable:

a lot of money
a lot of work
a lot of water

В обычных утвердительных предложениях A LOT OF часто звучит естественнее, чем MUCH:

I have a lot of work.

She has a lot of friends.

LOTS OF означает почти то же самое и звучит более разговорно.""",
            },


            {
                "order": 5,

                "title":
                    "A LOT OF или A LOT?",

                "body":
                    """Если после выражения идёт существительное:

a lot of + noun

We spent a lot of money.

She has a lot of friends.

Если существительного после него нет:

a lot

We spent a lot.

She travels a lot.

Не говорим:

a lot money

Правильно:

a lot of money.""",
            },


            {
                "order": 6,

                "title":
                    "A FEW и FEW",

                "body":
                    """Оба выражения используются только с countable plural nouns.

A FEW:

несколько;
немного, но количество есть.

I have a few friends.

We have a few chairs, so everyone can sit.

FEW:

мало;
почти нет;
недостаточно.

I have few friends.

We have few chairs, so some people must stand.

Главное различие — смысл.

A few → немного, но достаточно.

Few → слишком мало.""",
            },


            {
                "order": 7,

                "title":
                    "A LITTLE и LITTLE",

                "body":
                    """Оба выражения используются с uncountable nouns.

A LITTLE:

немного;
некоторое количество есть.

We have a little time.

There is a little milk.

LITTLE:

мало;
почти нет;
недостаточно.

We have little time, so we must hurry.

There is little milk, so we need to buy more.

A little → немного, но достаточно.

Little → слишком мало.""",
            },


            {
                "order": 8,

                "title":
                    "TOO MANY, TOO MUCH, SO MANY, SO MUCH",

                "body":
                    """TOO означает «слишком».

Countable plural:

too many people
too many questions
too many cars

Uncountable:

too much work
too much money
too much sugar

SO работает по той же схеме:

so many people
so many books

so much money
so much time

Сначала снова определяем тип существительного.""",
            },


            {
                "order": 9,

                "title":
                    "Главная схема выбора",

                "body":
                    """COUNTABLE PLURAL:

many
a few
few
a lot of

UNCOUNTABLE:

much
a little
little
a lot of

Если смысл «много»:

many books
much water
a lot of books
a lot of water

Если «немного, но есть»:

a few books
a little water

Если «мало, недостаточно»:

few books
little water

Всегда смотри и на тип существительного, и на смысл предложения.""",
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
                    "There are ___ students in the classroom.",

                "options": [
                    "much",
                    "many",
                    "little",
                    "a little",
                ],

                "answer":
                    "many",

                "explanation":
                    "Students — countable plural, поэтому MANY.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "We don't have ___ time.",

                "options": [
                    "many",
                    "much",
                    "a few",
                    "few",
                ],

                "answer":
                    "much",

                "explanation":
                    "Time — uncountable, поэтому MUCH.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "How ___ students are there in your group?",

                "options": [],

                "answer":
                    "many",

                "explanation":
                    "Students — исчисляемое существительное во множественном числе.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "We don't have ___ chairs.",

                "options": [
                    "much",
                    "many",
                    "little",
                    "a little",
                ],

                "answer":
                    "many",

                "explanation":
                    "Chairs — countable plural.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "How ___ water do you drink every day?",

                "options": [],

                "answer":
                    "much",

                "explanation":
                    "Water — uncountable.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "There isn't ___ milk in the fridge.",

                "options": [
                    "many",
                    "much",
                    "a few",
                    "few",
                ],

                "answer":
                    "much",

                "explanation":
                    "Milk — uncountable.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She has ___ friends.",

                "options": [
                    "a lot of",
                    "much",
                    "little",
                    "a little",
                ],

                "answer":
                    "a lot of",

                "explanation":
                    "A lot of можно использовать с countable plural.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "I have ___ work today.",

                "options": [
                    "many",
                    "a lot of",
                    "a few",
                    "few",
                ],

                "answer":
                    "a lot of",

                "explanation":
                    "Work — uncountable. В утверждении a lot of звучит естественно.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "We spent ___ money.",

                "options": [
                    "a lot",
                    "a lot of",
                    "many",
                    "a few",
                ],

                "answer":
                    "a lot of",

                "explanation":
                    "Перед существительным money нужно A LOT OF.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "We travelled ___ last year.",

                "options": [
                    "a lot",
                    "a lot of",
                    "many",
                    "much of",
                ],

                "answer":
                    "a lot",

                "explanation":
                    "После a lot здесь нет существительного.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "We have ___ chairs, so everyone can sit.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "a few",

                "explanation":
                    "Стульев немного, но их достаточно.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "We have ___ chairs, so some people must stand.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "few",

                "explanation":
                    "Стульев недостаточно, поэтому FEW.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Only ___ students failed, so the result was excellent.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "a few",

                "explanation":
                    "Небольшое количество студентов не сдало, но в целом результат хороший.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "We have ___ time, so let's discuss it.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "a little",

                "explanation":
                    "Времени немного, но достаточно.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "choice",

                "prompt":
                    "We have ___ time, so we must hurry.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "little",

                "explanation":
                    "Времени почти нет.",
            },


            {
                "order": 16,
                "section": 7,
                "type": "choice",

                "prompt":
                    "There is ___ milk left. You can make one cup of coffee.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "a little",

                "explanation":
                    "Молока немного, но его хватает.",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "There are too ___ people in this room.",

                "options": [
                    "much",
                    "many",
                    "little",
                    "a little",
                ],

                "answer":
                    "many",

                "explanation":
                    "People — countable plural: too many people.",
            },


            {
                "order": 18,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Don't add too ___ sugar.",

                "options": [
                    "many",
                    "much",
                    "few",
                    "a few",
                ],

                "answer":
                    "much",

                "explanation":
                    "Sugar — uncountable: too much sugar.",
            },


            {
                "order": 19,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Why are there so ___ questions?",

                "options": [
                    "much",
                    "many",
                    "little",
                    "a little",
                ],

                "answer":
                    "many",

                "explanation":
                    "Questions — countable plural.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "a few books / a little water",
                    "a little books / a few water",
                    "much books / many water",
                    "few water / little books",
                ],

                "answer":
                    "a few books / a little water",

                "explanation":
                    "A few идёт с countable plural, a little — с uncountable.",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "How ___ employees work in this company?",

                "options": [
                    "much",
                    "many",
                    "little",
                    "a little",
                ],

                "answer":
                    "many",

                "explanation":
                    "Employees — countable plural.",
            },


            {
                "order": 22,

                "prompt":
                    "How ___ information do we need?",

                "options": [
                    "many",
                    "much",
                    "a few",
                    "few",
                ],

                "answer":
                    "much",

                "explanation":
                    "Information — uncountable.",
            },


            {
                "order": 23,

                "prompt":
                    "She has ___ books at home.",

                "options": [
                    "a lot of",
                    "much",
                    "a little",
                    "little",
                ],

                "answer":
                    "a lot of",

                "explanation":
                    "A lot of подходит к countable plural.",
            },


            {
                "order": 24,

                "prompt":
                    "He works ___, but he doesn't earn much.",

                "options": [
                    "a lot",
                    "a lot of",
                    "many",
                    "few",
                ],

                "answer":
                    "a lot",

                "explanation":
                    "После a lot здесь нет существительного.",
            },


            {
                "order": 25,

                "prompt":
                    "I have ___ good friends, so I'm not alone.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "a few",

                "explanation":
                    "Friends — countable plural, и смысл положительный: несколько друзей есть.",
            },


            {
                "order": 26,

                "prompt":
                    "He has ___ friends and often feels lonely.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "few",

                "explanation":
                    "Friends — countable plural, а смысл отрицательный: друзей почти нет.",
            },


            {
                "order": 27,

                "prompt":
                    "We have ___ money, so we can buy the tickets.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "a little",

                "explanation":
                    "Money — uncountable; денег немного, но достаточно.",
            },


            {
                "order": 28,

                "prompt":
                    "We have ___ money, so we can't buy the tickets.",

                "options": [
                    "few",
                    "a few",
                    "little",
                    "a little",
                ],

                "answer":
                    "little",

                "explanation":
                    "Money — uncountable; денег недостаточно.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "too many cars / too much traffic",
                    "too much cars / too many traffic",
                    "too many cars / too many traffic",
                    "too much cars / too much traffic",
                ],

                "answer":
                    "too many cars / too much traffic",

                "explanation":
                    "Cars — countable plural; traffic — uncountable.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "We have a few questions and a little time.",
                    "We have a little questions and a few time.",
                    "We have much questions and many time.",
                    "We have little questions and few time.",
                ],

                "answer":
                    "We have a few questions and a little time.",

                "explanation":
                    "Questions — countable plural; time — uncountable.",
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
                "✅ Interactive A1 Lesson 5 seeded"
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
