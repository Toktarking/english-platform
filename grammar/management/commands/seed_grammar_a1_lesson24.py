from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 24: Past Simple with WAS/WERE."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=24,

                defaults={
                    "title":
                        "Past Simple с глаголом TO BE: "
                        "WAS и WERE",

                    "slug":
                        "past-simple-was-were",

                    "theory_text":
                        "Past Simple with was and were.",

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


        sections = [

            {
                "order": 1,

                "title":
                    "WAS и WERE = TO BE в прошлом",

                "body":
                    """WAS и WERE — прошедшие формы AM / IS / ARE.

Настоящее:

I am tired.

Прошлое:

I was tired yesterday.

Настоящее:

They are at home.

Прошлое:

They were at home last night.

WAS / WERE используются для:

состояния;

места;

возраста;

профессии или роли;

погоды и времени в прошлом.""",
            },


            {
                "order": 2,

                "title":
                    "Кто с WAS, а кто с WERE?",

                "body":
                    """Главная схема:

I → WAS

he → WAS

she → WAS

it → WAS

you → WERE

we → WERE

they → WERE

Примеры:

I was busy.

She was tired.

It was cold.

You were late.

We were ready.

They were at school.

Важно:

YOU всегда используется с WERE.""",
            },


            {
                "order": 3,

                "title":
                    "Состояние, место и возраст",

                "body":
                    """Состояние:

I was tired yesterday.

She was happy.

They were busy.

Место:

I was at home.

She was in Astana.

We were at university.

Возраст:

I was ten years old.

She was five.

В английском возраст выражается через TO BE.

Не:

I had ten years.

А:

I was ten years old.""",
            },


            {
                "order": 4,

                "title":
                    "Профессия, погода и время",

                "body":
                    """Профессия или роль:

He was a teacher.

She was a student.

They were doctors.

Погода:

It was cold yesterday.

It was sunny last weekend.

Время:

It was late.

It was five o'clock.

Схема:

subject + WAS/WERE + description.""",
            },


            {
                "order": 5,

                "title":
                    "Маркеры прошлого и AGO",

                "body":
                    """Частые маркеры Past Simple:

yesterday

last night

last week

last year

two days ago

a week ago

in 2020

when I was a child

AGO означает «назад» и ставится после периода времени.

Правильно:

two days ago

three weeks ago

a year ago

Не:

ago two days.""",
            },


            {
                "order": 6,

                "title":
                    "Отрицание: WASN'T / WEREN'T",

                "body":
                    """Отрицание строится без DID.

WAS NOT → WASN'T

I wasn't tired.

She wasn't at home.

WERE NOT → WEREN'T

We weren't ready.

They weren't at school.

Формула:

subject
+ wasn't / weren't
+ description.

Не:

She didn't was tired.

А:

She wasn't tired.""",
            },


            {
                "order": 7,

                "title":
                    "Вопросы и краткие ответы",

                "body":
                    """В вопросе WAS / WERE ставится перед подлежащим.

She was at home.

→ Was she at home?

They were tired.

→ Were they tired?

Краткие ответы:

Was she at home?

Yes, she was.

No, she wasn't.

Were they busy?

Yes, they were.

No, they weren't.

DID здесь не нужен.""",
            },


            {
                "order": 8,

                "title":
                    "WHERE, WHY и HOW WAS...?",

                "body":
                    """Специальный вопрос:

question word
+ WAS / WERE
+ subject?

Where were you yesterday?

Why was she tired?

When were they at home?

HOW WAS...? часто означает:

Как прошёл...?
Каким был...?

How was your day?

It was good.

How were the exams?

They were difficult.""",
            },


            {
                "order": 9,

                "title":
                    "WAS BORN и THERE WAS / WERE",

                "body":
                    """Рождение:

I was born in Kazakhstan.

She was born in 2000.

They were born in the same year.

Вопрос:

Where were you born?

When was she born?

Также:

THERE WAS → singular / uncountable

There was a problem.

There was some water.

THERE WERE → plural

There were many students.

There were two cars.""",
            },


            {
                "order": 10,

                "title":
                    "WAS/WERE или обычный глагол?",

                "body":
                    """WAS / WERE используются с:

прилагательным;

местом;

профессией;

возрастом.

He was tired.

He was at work.

She was a teacher.

Но если это действие, нужен обычный Past Simple.

He worked yesterday.

She studied English.

Не:

He was worked yesterday.

Сравни:

He was at work yesterday.
→ он был на работе

He worked yesterday.
→ он работал.""",
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


        training = [

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "Yesterday I ___ very tired.",

                "options": [
                    "am",
                    "was",
                    "were",
                    "did",
                ],

                "answer":
                    "was",

                "explanation":
                    "I → WAS в прошедшем времени.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "Last night they ___ at home.",

                "options": [
                    "was",
                    "were",
                    "are",
                    "did",
                ],

                "answer":
                    "were",

                "explanation":
                    "THEY → WERE.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "My sister ___ busy yesterday.",

                "options": [
                    "were",
                    "was",
                    "did",
                    "is",
                ],

                "answer":
                    "was",

                "explanation":
                    "My sister = SHE → WAS.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "fill",

                "prompt":
                    "You ___ late yesterday.",

                "options": [],

                "answer":
                    "were",

                "explanation":
                    "YOU всегда используется с WERE.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "When I was a child, I ___ eight years old.",

                "options": [
                    "had",
                    "was",
                    "were",
                    "did",
                ],

                "answer":
                    "was",

                "explanation":
                    "Возраст выражается через TO BE → I WAS.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "We ___ at the cinema last night.",

                "options": [
                    "was",
                    "were",
                    "did",
                    "are",
                ],

                "answer":
                    "were",

                "explanation":
                    "WE → WERE; здесь речь о месте.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "My grandfather ___ a teacher.",

                "options": [
                    "were",
                    "was",
                    "did",
                    "worked",
                ],

                "answer":
                    "was",

                "explanation":
                    "Профессия после TO BE → WAS A TEACHER.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "It ___ very cold last weekend.",

                "options": [
                    "were",
                    "was",
                    "did",
                    "are",
                ],

                "answer":
                    "was",

                "explanation":
                    "Погода: IT → WAS.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Two days ___, I was in Astana.",

                "options": [
                    "ago",
                    "last",
                    "before ago",
                    "yesterday",
                ],

                "answer":
                    "ago",

                "explanation":
                    "Правильный порядок: TWO DAYS AGO.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct time expression.",

                "options": [
                    "ago three weeks",
                    "three weeks ago",
                    "three ago weeks",
                    "last ago three weeks",
                ],

                "answer":
                    "three weeks ago",

                "explanation":
                    "AGO ставится после периода времени.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "She ___ at home yesterday.",

                "options": [
                    "wasn't",
                    "didn't was",
                    "weren't",
                    "didn't be",
                ],

                "answer":
                    "wasn't",

                "explanation":
                    "SHE → WASN'T. DID не используется.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "They ___ ready for the exam.",

                "options": [
                    "wasn't",
                    "weren't",
                    "didn't were",
                    "not were",
                ],

                "answer":
                    "weren't",

                "explanation":
                    "THEY → WEREN'T.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "___ your father at work yesterday?",

                "options": [
                    "Did",
                    "Was",
                    "Were",
                    "Does",
                ],

                "answer":
                    "Was",

                "explanation":
                    "Your father = HE → WAS.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Were the students tired?",

                "options": [
                    "No, they didn't.",
                    "No, they weren't.",
                    "No, they wasn't.",
                    "No, they aren't.",
                ],

                "answer":
                    "No, they weren't.",

                "explanation":
                    "WERE THEY...? → NO, THEY WEREN'T.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "build",

                "prompt":
                    "Собери правильный вопрос.",

                "options": [
                    "Where",
                    "were",
                    "you",
                    "yesterday",
                ],

                "answer":
                    "Where were you yesterday",

                "explanation":
                    "Question word + WERE + YOU.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "How ___ your trip?",

                "options": [
                    "were",
                    "was",
                    "did",
                    "is",
                ],

                "answer":
                    "was",

                "explanation":
                    "TRIP — singular → HOW WAS YOUR TRIP?",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "I ___ born in Kazakhstan.",

                "options": [
                    "were",
                    "was",
                    "did",
                    "am",
                ],

                "answer":
                    "was",

                "explanation":
                    "Правильная конструкция: I WAS BORN.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "There ___ many people at the meeting.",

                "options": [
                    "was",
                    "were",
                    "did",
                    "is",
                ],

                "answer":
                    "were",

                "explanation":
                    "MANY PEOPLE → THERE WERE.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the sentence meaning «Он был на работе вчера».",

                "options": [
                    "He worked yesterday.",
                    "He was at work yesterday.",
                    "He was work yesterday.",
                    "He did at work yesterday.",
                ],

                "answer":
                    "He was at work yesterday.",

                "explanation":
                    "AT WORK описывает место → WAS AT WORK.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the sentence describing an action.",

                "options": [
                    "She was worked yesterday.",
                    "She worked yesterday.",
                    "She was work yesterday.",
                    "She did worked yesterday.",
                ],

                "answer":
                    "She worked yesterday.",

                "explanation":
                    "WORK — действие, поэтому используется обычный Past Simple.",
            },

        ]


        final_test = [

            {
                "order": 21,

                "prompt":
                    "My parents ___ in Almaty last week.",

                "options": [
                    "was",
                    "were",
                    "did",
                    "are",
                ],

                "answer":
                    "were",

                "explanation":
                    "My parents = THEY → WERE.",
            },


            {
                "order": 22,

                "prompt":
                    "The weather ___ beautiful yesterday.",

                "options": [
                    "were",
                    "was",
                    "did",
                    "is",
                ],

                "answer":
                    "was",

                "explanation":
                    "THE WEATHER = IT → WAS.",
            },


            {
                "order": 23,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "We didn't were busy.",
                    "We weren't busy.",
                    "We wasn't busy.",
                    "We didn't be busy.",
                ],

                "answer":
                    "We weren't busy.",

                "explanation":
                    "WE → WEREN'T; DID не нужен.",
            },


            {
                "order": 24,

                "prompt":
                    "___ she at school yesterday?",

                "options": [
                    "Did",
                    "Was",
                    "Were",
                    "Does",
                ],

                "answer":
                    "Was",

                "explanation":
                    "SHE → WAS; в вопросе WAS ставится первым.",
            },


            {
                "order": 25,

                "prompt":
                    "Were you tired after work?",

                "options": [
                    "Yes, I was.",
                    "Yes, I were.",
                    "Yes, I did.",
                    "Yes, I am.",
                ],

                "answer":
                    "Yes, I was.",

                "explanation":
                    "В ответе на WERE YOU...? говорим YES, I WAS.",
            },


            {
                "order": 26,

                "prompt":
                    "Why ___ he angry yesterday?",

                "options": [
                    "were",
                    "was",
                    "did",
                    "does",
                ],

                "answer":
                    "was",

                "explanation":
                    "HE → WAS: WHY WAS HE...?",
            },


            {
                "order": 27,

                "prompt":
                    "Where ___ you born?",

                "options": [
                    "was",
                    "were",
                    "did",
                    "are",
                ],

                "answer":
                    "were",

                "explanation":
                    "YOU → WERE: WHERE WERE YOU BORN?",
            },


            {
                "order": 28,

                "prompt":
                    "There ___ some milk in the fridge.",

                "options": [
                    "were",
                    "was",
                    "did",
                    "have",
                ],

                "answer":
                    "was",

                "explanation":
                    "MILK — uncountable → THERE WAS.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "He was tired after work.",
                    "He did tired after work.",
                    "He were tired after work.",
                    "He was be tired after work.",
                ],

                "answer":
                    "He was tired after work.",

                "explanation":
                    "Прилагательное TIRED используется после WAS.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct pair.",

                "options": [
                    "He was at work yesterday. / He worked yesterday.",
                    "He did at work yesterday. / He was worked yesterday.",
                    "He were at work yesterday. / He did worked yesterday.",
                    "He was work yesterday. / He was working yesterday as Past Simple.",
                ],

                "answer":
                    "He was at work yesterday. / He worked yesterday.",

                "explanation":
                    "WAS AT WORK описывает место; WORKED описывает действие.",
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
                "✅ Interactive A1 Lesson 24 seeded"
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
