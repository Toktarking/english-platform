from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 15: There is / There are."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=15,

                defaults={
                    "title":
                        "Конструкция THERE IS / THERE ARE",

                    "slug":
                        "there-is-there-are",

                    "theory_text":
                        "There is / There are.",

                    "estimated_minutes":
                        17,

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
                    "Что означает THERE IS / THERE ARE?",

                "body":
                    """THERE IS / THERE ARE сообщает, что где-то что-то есть или находится.

There is a book on the table.

There are three students in the room.

There is some milk in the fridge.

В этой конструкции THERE обычно не переводится буквально как «там».

Вся конструкция означает:

есть;
находится;
имеется.""",
            },


            {
                "order": 2,

                "title":
                    "Один предмет → THERE IS",

                "body":
                    """THERE IS используется с одним человеком или предметом.

There is a chair in the room.

There is a teacher at the door.

There is a problem.

С одним исчисляемым существительным обычно нужен определитель:

a book

an apple

my phone

the teacher

Не:

There is book.

А:

There is a book.""",
            },


            {
                "order": 3,

                "title":
                    "Много предметов → THERE ARE",

                "body":
                    """THERE ARE используется с существительными во множественном числе.

There are two books on the table.

There are many students in the room.

There are some apples in the bag.

There are no chairs here.

Главная схема:

singular → THERE IS

plural → THERE ARE.""",
            },


            {
                "order": 4,

                "title":
                    "Неисчисляемые → THERE IS",

                "body":
                    """С неисчисляемыми существительными используется THERE IS.

There is some water.

There is a little milk.

There is no information.

There is a lot of work.

Почему IS?

Потому что uncountable nouns грамматически обычно не имеют формы множественного числа.

Примеры:

water
money
information
milk
work.""",
            },


            {
                "order": 5,

                "title":
                    "SOME и ANY",

                "body":
                    """В утверждении часто используется SOME:

There are some books.

There is some juice.

В вопросах обычно ANY:

Are there any books?

Is there any juice?

В отрицаниях тоже ANY:

There aren't any books.

There isn't any juice.

Коротко:

утверждение → SOME

вопрос → ANY

отрицание → ANY.""",
            },


            {
                "order": 6,

                "title":
                    "Отрицание: ISN'T / AREN'T",

                "body":
                    """Отрицание:

There isn't...

There aren't...

Примеры:

There isn't a bank here.

There isn't any milk.

There aren't any students.

Также можно использовать NO:

There is no milk.

There are no students.

Сравни:

There isn't any milk.

There is no milk.

Оба варианта означают отсутствие.

Не используй двойное отрицание:

There isn't no milk. ❌""",
            },


            {
                "order": 7,

                "title":
                    "Вопросы: IS THERE? / ARE THERE?",

                "body":
                    """Для вопроса IS или ARE ставится перед THERE.

There is a bank nearby.

→ Is there a bank nearby?

There are shops nearby.

→ Are there shops nearby?

Схема:

IS THERE
+ singular / uncountable?

ARE THERE
+ plural?

Примеры:

Is there any milk?

Are there any students?

Are there many shops?""",
            },


            {
                "order": 8,

                "title":
                    "Краткие ответы",

                "body":
                    """Если вопрос начинается с IS THERE:

Is there a problem?

Yes, there is.

No, there isn't.

Если вопрос начинается с ARE THERE:

Are there any questions?

Yes, there are.

No, there aren't.

Важно:

Не:

Yes, it is.

А:

Yes, there is.

В кратком ответе сохраняется THERE.""",
            },


            {
                "order": 9,

                "title":
                    "HOW MANY / HOW MUCH",

                "body":
                    """С countable plural:

HOW MANY + noun + ARE THERE?

How many students are there?

How many books are there?

С uncountable:

HOW MUCH + noun + IS THERE?

How much water is there?

How much money is there?

Не:

How many are there students?

А:

How many students are there?""",
            },


            {
                "order": 10,

                "title":
                    "THERE IS или HAVE?",

                "body":
                    """THERE IS / ARE сообщает о наличии или местонахождении:

There is a car outside.

Снаружи стоит машина.

HAVE / HAS показывает принадлежность:

I have a car.

У меня есть машина.

После первого упоминания можно использовать IT / THEY:

There is a book on the table.

It is mine.

There are two books on the table.

They are mine.

Если перечисляются разные предметы, для базового уровня ориентируемся на первый:

There is a book and two pens.

There are two books and a pen.""",
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
                    "There ___ a teacher in the classroom.",

                "options": [
                    "are",
                    "is",
                    "am",
                    "have",
                ],

                "answer":
                    "is",

                "explanation":
                    "Teacher — один человек → THERE IS.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "There ___ three students outside.",

                "options": [
                    "is",
                    "are",
                    "am",
                    "has",
                ],

                "answer":
                    "are",

                "explanation":
                    "Students — множественное число → THERE ARE.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "There is book on the desk.",
                    "There are a book on the desk.",
                    "There is a book on the desk.",
                    "There have a book on the desk.",
                ],

                "answer":
                    "There is a book on the desk.",

                "explanation":
                    "Один countable noun требует THERE IS + A/AN.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "fill",

                "prompt":
                    "There ___ an apple in the bag.",

                "options": [],

                "answer":
                    "is",

                "explanation":
                    "An apple — один предмет → IS.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "There ___ many cars outside.",

                "options": [],

                "answer":
                    "are",

                "explanation":
                    "Cars — plural → ARE.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "There ___ a few chairs in the room.",

                "options": [
                    "is",
                    "are",
                    "am",
                    "has",
                ],

                "answer":
                    "are",

                "explanation":
                    "A few chairs — множественное число.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "There ___ some coffee in the cup.",

                "options": [
                    "are",
                    "is",
                    "be",
                    "have",
                ],

                "answer":
                    "is",

                "explanation":
                    "COFFEE — uncountable → THERE IS.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "There ___ a little water left.",

                "options": [
                    "are",
                    "is",
                    "have",
                    "be",
                ],

                "answer":
                    "is",

                "explanation":
                    "WATER — uncountable → IS.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "There are ___ books on the shelf.",

                "options": [
                    "some",
                    "any",
                    "much",
                    "a little",
                ],

                "answer":
                    "some",

                "explanation":
                    "Это утвердительное предложение → SOME.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Is there ___ juice in the fridge?",

                "options": [
                    "some",
                    "any",
                    "many",
                    "a few",
                ],

                "answer":
                    "any",

                "explanation":
                    "Обычный вопрос → ANY.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "There isn't ___ sugar.",

                "options": [
                    "some",
                    "any",
                    "many",
                    "a few",
                ],

                "answer":
                    "any",

                "explanation":
                    "В отрицании обычно используется ANY.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "There isn't no milk.",
                    "There isn't any milk.",
                    "There don't have milk.",
                    "There isn't some milk.",
                ],

                "answer":
                    "There isn't any milk.",

                "explanation":
                    "ISN'T + NO создаёт неправильное двойное отрицание.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "___ there a hospital near here?",

                "options": [
                    "Are",
                    "Is",
                    "Do",
                    "Does",
                ],

                "answer":
                    "Is",

                "explanation":
                    "Hospital — singular → IS THERE?",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "___ there any shops nearby?",

                "options": [
                    "Is",
                    "Are",
                    "Do",
                    "Does",
                ],

                "answer":
                    "Are",

                "explanation":
                    "Shops — plural → ARE THERE?",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Is there a problem?",

                "options": [
                    "Yes, there is.",
                    "Yes, it is.",
                    "Yes, there are.",
                    "Yes, it does.",
                ],

                "answer":
                    "Yes, there is.",

                "explanation":
                    "IS THERE...? → YES, THERE IS.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Are there any questions?",

                "options": [
                    "No, there isn't.",
                    "No, there aren't.",
                    "No, they aren't.",
                    "No, it isn't.",
                ],

                "answer":
                    "No, there aren't.",

                "explanation":
                    "ARE THERE...? → NO, THERE AREN'T.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "How many rooms ___ there in the house?",

                "options": [
                    "is",
                    "are",
                    "do",
                    "does",
                ],

                "answer":
                    "are",

                "explanation":
                    "HOW MANY + plural noun + ARE THERE?",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "How much money ___ there in the account?",

                "options": [
                    "are",
                    "is",
                    "do",
                    "does",
                ],

                "answer":
                    "is",

                "explanation":
                    "MONEY — uncountable → HOW MUCH ... IS THERE?",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Which sentence describes location, not possession?",

                "options": [
                    "I have a car.",
                    "She has a phone.",
                    "There is a car outside.",
                    "They have two children.",
                ],

                "answer":
                    "There is a car outside.",

                "explanation":
                    "THERE IS сообщает о наличии или местонахождении.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "There are two books on the table. ___ are mine.",

                "options": [
                    "It",
                    "They",
                    "There",
                    "It is",
                ],

                "answer":
                    "They",

                "explanation":
                    "BOOKS — plural, после первого упоминания используем THEY.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "There ___ a new café near my house.",

                "options": [
                    "are",
                    "is",
                    "have",
                    "am",
                ],

                "answer":
                    "is",

                "explanation":
                    "A new café — singular → THERE IS.",
            },


            {
                "order": 22,

                "prompt":
                    "There ___ five people in the room.",

                "options": [
                    "is",
                    "are",
                    "has",
                    "be",
                ],

                "answer":
                    "are",

                "explanation":
                    "Five people — plural → THERE ARE.",
            },


            {
                "order": 23,

                "prompt":
                    "There ___ some information in the email.",

                "options": [
                    "are",
                    "is",
                    "have",
                    "be",
                ],

                "answer":
                    "is",

                "explanation":
                    "INFORMATION — uncountable → THERE IS.",
            },


            {
                "order": 24,

                "prompt":
                    "Are there ___ restaurants near the hotel?",

                "options": [
                    "some",
                    "any",
                    "much",
                    "a little",
                ],

                "answer":
                    "any",

                "explanation":
                    "Обычный вопрос → ANY.",
            },


            {
                "order": 25,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "There aren't no chairs.",
                    "There aren't any chairs.",
                    "There isn't any chairs.",
                    "There don't have chairs.",
                ],

                "answer":
                    "There aren't any chairs.",

                "explanation":
                    "CHAIRS — plural → AREN'T; после отрицания подходит ANY.",
            },


            {
                "order": 26,

                "prompt":
                    "___ there any water in the bottle?",

                "options": [
                    "Are",
                    "Is",
                    "Do",
                    "Does",
                ],

                "answer":
                    "Is",

                "explanation":
                    "WATER — uncountable → IS THERE?",
            },


            {
                "order": 27,

                "prompt":
                    "Are there two bathrooms?",

                "options": [
                    "Yes, there are.",
                    "Yes, they are.",
                    "Yes, there is.",
                    "Yes, it is.",
                ],

                "answer":
                    "Yes, there are.",

                "explanation":
                    "ARE THERE...? → YES, THERE ARE.",
            },


            {
                "order": 28,

                "prompt":
                    "___ students are there in your class?",

                "options": [
                    "How much",
                    "How many",
                    "How often",
                    "Which much",
                ],

                "answer":
                    "How many",

                "explanation":
                    "STUDENTS — countable plural → HOW MANY.",
            },


            {
                "order": 29,

                "prompt":
                    "___ time is there before the lesson?",

                "options": [
                    "How many",
                    "How much",
                    "How often",
                    "How several",
                ],

                "answer":
                    "How much",

                "explanation":
                    "TIME здесь uncountable → HOW MUCH.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct pair.",

                "options": [
                    "There is a dog outside. / It is very friendly.",
                    "There are a dog outside. / They is very friendly.",
                    "There is dogs outside. / It are very friendly.",
                    "There have a dog outside. / There is friendly.",
                ],

                "answer":
                    "There is a dog outside. / It is very friendly.",

                "explanation":
                    "Первое упоминание — THERE IS; затем singular DOG заменяется на IT.",
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
                "✅ Interactive A1 Lesson 15 seeded"
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
