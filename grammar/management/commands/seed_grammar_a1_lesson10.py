from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 10: TO BE — am, is, are."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=10,
                defaults={
                    "title":
                        "Глагол TO BE в настоящем времени: "
                        "AM, IS, ARE",

                    "slug":
                        "to-be-am-is-are",

                    "theory_text":
                        "Present tense of TO BE: am, is, are.",

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
                    "Почему в английском нужен TO BE?",

                "body":
                    """TO BE может означать:

быть;
находиться;
являться.

В русском настоящего «быть» часто не видно:

Я студент.
Она дома.
Они заняты.

В английском глагол нужен:

I am a student.

She is at home.

They are busy.

Не:

I a student.

She at home.

They busy.""",
            },


            {
                "order": 2,
                "title":
                    "Главная таблица AM, IS, ARE",

                "body":
                    """Запомни три группы:

I → AM

he / she / it → IS

you / we / they → ARE

Полная система:

I am

you are

he is

she is

it is

we are

they are

Если вместо подлежащего можно сказать HE / SHE / IT → IS.

Если можно сказать THEY → ARE.""",
            },


            {
                "order": 3,
                "title":
                    "Когда используется TO BE?",

                "body":
                    """TO BE часто нужен, если после него стоит:

профессия:

I am a teacher.

состояние или прилагательное:

She is happy.

We are ready.

место:

He is at home.

The children are outside.

возраст:

My son is one year old.

национальность:

She is British.

То есть TO BE связывает подлежащее с описанием, состоянием, местом или характеристикой.""",
            },


            {
                "order": 4,
                "title":
                    "Погода, время и возраст",

                "body":
                    """Для погоды часто используется IT IS:

It is cold.

It is hot.

It is sunny.

Для времени:

It is five o'clock.

It is late.

Возраст выражается через TO BE:

I am twenty years old.

She is ten.

My son is one year old.

Не:

I have twenty years.

А:

I am twenty years old.""",
            },


            {
                "order": 5,
                "title":
                    "Сокращённые формы",

                "body":
                    """В речи часто используются сокращения:

I am → I'm

you are → you're

he is → he's

she is → she's

it is → it's

we are → we're

they are → they're

Примеры:

I'm tired.

He's a doctor.

She's at home.

It's cold.

We're ready.

They're busy.

Полная и сокращённая форма означают одно и то же.""",
            },


            {
                "order": 6,
                "title":
                    "Как сделать отрицание",

                "body":
                    """Для отрицания просто добавляем NOT после TO BE:

I am not tired.

He is not at home.

They are not ready.

Сокращения:

I'm not

isn't

aren't

Примеры:

She isn't busy.

We aren't late.

Важно:

стандартной формы amn't обычно нет.

Говорим:

I'm not.""",
            },


            {
                "order": 7,
                "title":
                    "Как сделать вопрос",

                "body":
                    """В вопросе AM / IS / ARE переносится перед подлежащим.

Утверждение:

She is at home.

Вопрос:

Is she at home?

Примеры:

Am I late?

Is he a doctor?

Is it cold?

Are you ready?

Are they students?

Формула:

AM / IS / ARE + subject + ... ?""",
            },


            {
                "order": 8,
                "title":
                    "Краткие и специальные вопросы",

                "body":
                    """Краткий ответ повторяет TO BE:

Are you ready?

Yes, I am.

No, I'm not.

Is he at home?

Yes, he is.

No, he isn't.

В положительном кратком ответе обычно не сокращаем:

не:

Yes, I'm.

а:

Yes, I am.

Специальный вопрос:

Where are you?

Where is the book?

How old is she?

Why are they late?

What is this?

Who is he?""",
            },


            {
                "order": 9,
                "title":
                    "TO BE или обычный глагол?",

                "body":
                    """Очень важно не ставить AM / IS / ARE перед обычным смысловым глаголом.

TO BE:

He is a teacher.

She is tired.

They are at home.

Обычный глагол:

I work at a university.

She speaks English.

They live in Astana.

Не:

I am work.

She is speaks English.

They are live in Astana.

Сравни:

He is a teacher.
Teacher — профессия.

He works at a school.
Works — действие.

Это одна из самых частых ошибок у начинающих.""",
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
                    "I ___ a student.",

                "options": [
                    "is",
                    "are",
                    "am",
                    "be",
                ],

                "answer":
                    "am",

                "explanation":
                    "В английском TO BE обязателен: I AM.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "She ___ at home.",

                "options": [
                    "am",
                    "is",
                    "are",
                    "be",
                ],

                "answer":
                    "is",

                "explanation":
                    "She → IS.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "They ___ ready.",

                "options": [],

                "answer":
                    "are",

                "explanation":
                    "They → ARE.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "The book ___ interesting.",

                "options": [
                    "am",
                    "are",
                    "is",
                    "be",
                ],

                "answer":
                    "is",

                "explanation":
                    "Book — один предмет → IT → IS.",
            },


            {
                "order": 5,
                "section": 2,
                "type": "choice",

                "prompt":
                    "The students ___ in the classroom.",

                "options": [
                    "is",
                    "am",
                    "are",
                    "be",
                ],

                "answer":
                    "are",

                "explanation":
                    "Students — множественное число → ARE.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "My wife ___ a teacher.",

                "options": [
                    "are",
                    "is",
                    "am",
                    "be",
                ],

                "answer":
                    "is",

                "explanation":
                    "My wife — один человек → SHE → IS.",
            },


            {
                "order": 7,
                "section": 3,
                "type": "choice",

                "prompt":
                    "We ___ happy today.",

                "options": [
                    "am",
                    "is",
                    "are",
                    "be",
                ],

                "answer":
                    "are",

                "explanation":
                    "WE → ARE.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "___ is cold today.",

                "options": [
                    "He",
                    "She",
                    "It",
                    "They",
                ],

                "answer":
                    "It",

                "explanation":
                    "Для погоды используется IT.",
            },


            {
                "order": 9,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence about age.",

                "options": [
                    "I have twenty years.",
                    "I am twenty years old.",
                    "I is twenty years old.",
                    "I do twenty years old.",
                ],

                "answer":
                    "I am twenty years old.",

                "explanation":
                    "Возраст в английском выражается через TO BE.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct contraction: She is tired.",

                "options": [
                    "She's tired.",
                    "She're tired.",
                    "She'm tired.",
                    "She tired.",
                ],

                "answer":
                    "She's tired.",

                "explanation":
                    "SHE IS → SHE'S.",
            },


            {
                "order": 11,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct contraction: They are busy.",

                "options": [
                    "They're busy.",
                    "They's busy.",
                    "They'm busy.",
                    "Their busy.",
                ],

                "answer":
                    "They're busy.",

                "explanation":
                    "THEY ARE → THEY'RE.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "fill",

                "prompt":
                    "I ___ not tired.",

                "options": [],

                "answer":
                    "am",

                "explanation":
                    "Правильно: I AM NOT.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "He not is at home.",
                    "He isn't at home.",
                    "He don't is at home.",
                    "He aren't at home.",
                ],

                "answer":
                    "He isn't at home.",

                "explanation":
                    "HE → IS → ISN'T.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "___ she a doctor?",

                "options": [
                    "Am",
                    "Are",
                    "Is",
                    "Does",
                ],

                "answer":
                    "Is",

                "explanation":
                    "В вопросе IS ставится перед SHE.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "build",

                "prompt":
                    "Собери вопрос.",

                "options": [
                    "Are",
                    "they",
                    "at",
                    "home",
                ],

                "answer":
                    "Are they at home",

                "explanation":
                    "В вопросе ARE стоит перед THEY.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Are you ready?",

                "options": [
                    "Yes, I'm.",
                    "Yes, I am.",
                    "Yes, you are.",
                    "Yes, I is.",
                ],

                "answer":
                    "Yes, I am.",

                "explanation":
                    "В положительном кратком ответе используем YES, I AM.",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Is Marat at home?",

                "options": [
                    "Yes, he is.",
                    "Yes, he's.",
                    "Yes, he are.",
                    "Yes, it is.",
                ],

                "answer":
                    "Yes, he is.",

                "explanation":
                    "Положительный краткий ответ: YES, HE IS.",
            },


            {
                "order": 18,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Where ___ my keys?",

                "options": [
                    "is",
                    "am",
                    "are",
                    "does",
                ],

                "answer":
                    "are",

                "explanation":
                    "Keys — множественное число → WHERE ARE.",
            },


            {
                "order": 19,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She is speaks English.",
                    "She speaks English.",
                    "She are speak English.",
                    "She is speak English.",
                ],

                "answer":
                    "She speaks English.",

                "explanation":
                    "SPEAKS — обычный смысловой глагол. IS перед ним не нужен.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "He is a teacher. / He works at a school.",
                    "He a teacher. / He is works at a school.",
                    "He are a teacher. / He works is at a school.",
                    "He is teacher. / He is work at school.",
                ],

                "answer":
                    "He is a teacher. / He works at a school.",

                "explanation":
                    "Профессия требует TO BE; действие WORKS используется без IS.",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "My parents ___ at home.",

                "options": [
                    "is",
                    "am",
                    "are",
                    "be",
                ],

                "answer":
                    "are",

                "explanation":
                    "Parents — множественное число → ARE.",
            },


            {
                "order": 22,

                "prompt":
                    "This book ___ very useful.",

                "options": [
                    "am",
                    "are",
                    "is",
                    "do",
                ],

                "answer":
                    "is",

                "explanation":
                    "Book — единственное число → IS.",
            },


            {
                "order": 23,

                "prompt":
                    "It ___ five o'clock.",

                "options": [
                    "am",
                    "is",
                    "are",
                    "does",
                ],

                "answer":
                    "is",

                "explanation":
                    "Для времени используется IT IS.",
            },


            {
                "order": 24,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "We isn't late.",
                    "We aren't late.",
                    "We don't are late.",
                    "We not late.",
                ],

                "answer":
                    "We aren't late.",

                "explanation":
                    "WE → ARE → AREN'T.",
            },


            {
                "order": 25,

                "prompt":
                    "___ your sister at work?",

                "options": [
                    "Are",
                    "Is",
                    "Am",
                    "Does",
                ],

                "answer":
                    "Is",

                "explanation":
                    "Your sister — один человек → IS.",
            },


            {
                "order": 26,

                "prompt":
                    "How old ___ your children?",

                "options": [
                    "is",
                    "are",
                    "am",
                    "do",
                ],

                "answer":
                    "are",

                "explanation":
                    "Children — множественное число → ARE.",
            },


            {
                "order": 27,

                "prompt":
                    "Are the students ready?",

                "options": [
                    "No, they isn't.",
                    "No, they aren't.",
                    "No, they don't.",
                    "No, they not.",
                ],

                "answer":
                    "No, they aren't.",

                "explanation":
                    "THEY → ARE → AREN'T.",
            },


            {
                "order": 28,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I am from Kazakhstan.",
                    "I is from Kazakhstan.",
                    "I are from Kazakhstan.",
                    "I from Kazakhstan.",
                ],

                "answer":
                    "I am from Kazakhstan.",

                "explanation":
                    "I всегда используется с AM.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "They are live in Astana.",
                    "They live in Astana.",
                    "They is live in Astana.",
                    "They are lives in Astana.",
                ],

                "answer":
                    "They live in Astana.",

                "explanation":
                    "LIVE — обычный смысловой глагол, поэтому ARE перед ним не нужен.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct option.",

                "options": [
                    "She is tired, but she works today.",
                    "She tired, but she is works today.",
                    "She is tired, but she is work today.",
                    "She are tired, but she works is today.",
                ],

                "answer":
                    "She is tired, but she works today.",

                "explanation":
                    "TIRED требует TO BE, а WORKS — обычный смысловой глагол.",
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
                "✅ Interactive A1 Lesson 10 seeded"
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
