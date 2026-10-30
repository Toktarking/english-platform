from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 37: "
        "BE GOING TO."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=37,
            defaults={
                "title": "BE GOING TO",
                "slug": "be-going-to",
                "theory_text": "BE GOING TO.",
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что означает BE GOING TO",
                "body": """BE GOING TO используется, когда мы говорим:

о заранее принятом плане;

о намерении;

о решении, которое было принято до момента речи;

о прогнозе по очевидным признакам.

Примеры:

I am going to study tonight.

She is going to buy a new phone.

Look at those clouds.
It is going to rain.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Формула:

subject + am/is/are + going to + base verb

Примеры:

I am going to work.

She is going to study.

They are going to travel.

We are going to buy a car.

Главное:

I → am going to

he/she/it → is going to

you/we/they → are going to""",
            },

            {
                "order": 3,
                "title": "После GOING TO — первая форма",
                "body": """После GOING TO используется основная форма глагола.

Правильно:

going to work

going to study

going to buy

going to be

going to have

Неправильно:

going to works

going to studied

going to buying

going to to work

Пример:

She is going to work tomorrow.""",
            },

            {
                "order": 4,
                "title": "Заранее принятый план",
                "body": """BE GOING TO используется, если решение существовало до момента речи.

Пример:

I am going to visit my parents this weekend.

Человек решил это заранее.

Другие примеры:

She is going to start a new course.

We are going to renovate the apartment.

They are going to travel next month.

He is going to look for a new job.""",
            },

            {
                "order": 5,
                "title": "Намерение",
                "body": """BE GOING TO также выражает намерение.

Примеры:

I am going to learn English.

She is going to lose weight.

They are going to save money.

He is going to stop smoking.

Действие ещё может быть не организовано полностью.

Но решение или намерение уже существует.""",
            },

            {
                "order": 6,
                "title": "Прогноз по видимым признакам",
                "body": """BE GOING TO используется, когда есть очевидные признаки будущего события.

Пример:

Look at the clouds.
It is going to rain.

Другие примеры:

Be careful!
You are going to fall.

That glass is going to break.

The baby is going to cry.

The car is moving too fast.
It is going to crash.""",
            },

            {
                "order": 7,
                "title": "BE GOING TO или WILL",
                "body": """WILL часто используется для спонтанного решения.

The phone is ringing.
I'll answer it.

BE GOING TO — для заранее принятого плана.

I'm going to call him tonight.

Сравните:

I'll buy some bread.
— решил сейчас.

I'm going to buy some bread after work.
— планировал заранее.""",
            },

            {
                "order": 8,
                "title": "Прогноз: WILL или GOING TO",
                "body": """WILL часто используется для мнения.

I think it will rain tomorrow.

Это личное предположение.

BE GOING TO используется, если есть видимые признаки.

Look at the sky.
It is going to rain.

Сравните:

I think she will win.
— мнение.

She is playing much better.
She is going to win.
— есть основания для прогноза.""",
            },

            {
                "order": 9,
                "title": "Отрицание",
                "body": """Отрицательная форма:

subject + am/is/are not going to + base verb

Примеры:

I am not going to work today.

She isn't going to come.

They aren't going to travel.

We aren't going to buy it.

Отрицание может означать:

отказ от плана;

намерение не делать что-то;

прогноз отрицательного события.""",
            },

            {
                "order": 10,
                "title": "Вопросы и краткие ответы",
                "body": """В вопросе AM / IS / ARE ставится перед подлежащим.

Формула:

Am/Is/Are + subject + going to + verb?

Примеры:

Are you going to work?

Is she going to call?

Are they going to travel?

Is it going to rain?

Краткие ответы:

Yes, she is.

No, she isn't.

Yes, they are.

No, they aren't.""",
            },

            {
                "order": 11,
                "title": "Специальные вопросы",
                "body": """Формула:

Question word + am/is/are + subject + going to + verb?

Примеры:

What are you going to do?

Where is she going to stay?

When are they going to arrive?

Why is he going to leave?

How are we going to solve this problem?

WHO как подлежащее:

Who is going to help us?""",
            },

            {
                "order": 12,
                "title": "GOING TO BE и GOING TO HAVE",
                "body": """После GOING TO используется первая форма.

С BE:

It is going to be difficult.

She is going to be busy.

They are going to be late.

Не:

It is going to is difficult.

С HAVE:

We are going to have dinner.

She is going to have a meeting.

Не:

She is going to has a meeting.""",
            },

            {
                "order": 13,
                "title": "GOING TO и другие формы будущего",
                "body": """BE GOING TO:

намерение или план.

I'm going to visit my doctor next week.

Present Continuous:

конкретная договорённость.

I'm seeing my doctor on Monday at ten.

Present Simple:

расписание.

The train leaves at six.

BE GOING TO:

личный план.

We are going to take the six o'clock train.""",
            },

            {
                "order": 14,
                "title": "Как выбрать BE GOING TO",
                "body": """Шаг 1.

План был принят раньше?

→ BE GOING TO

I'm going to start a new course.

Шаг 2.

Есть намерение?

→ BE GOING TO

She is going to learn to drive.

Шаг 3.

Есть видимые признаки?

→ BE GOING TO

Look at the baby.
He is going to cry.

Шаг 4.

Решение принято прямо сейчас?

→ WILL

I'll answer the phone.

Шаг 5.

Это просто мнение?

→ часто WILL

I think they will win.""",
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
                "prompt": "We ___ going to start soon.",
                "options": ["is", "are", "am", "do"],
                "answer": "are",
                "explanation": "We используется с are.",
            },

            {
                "order": 2,
                "prompt": "My brother ___ going to buy a car.",
                "options": ["am", "is", "are", "does"],
                "answer": "is",
                "explanation": "My brother = he, поэтому is.",
            },

            {
                "order": 3,
                "prompt": "I am going to ___ English.",
                "options": [
                    "study",
                    "studied",
                    "studying",
                    "studies",
                ],
                "answer": "study",
                "explanation": "После going to используется первая форма.",
            },

            {
                "order": 4,
                "prompt": "She isn't going to ___ tonight.",
                "options": [
                    "works",
                    "worked",
                    "work",
                    "working",
                ],
                "answer": "work",
                "explanation": "После going to → base verb.",
            },

            {
                "order": 5,
                "prompt": "___ you going to call him?",
                "options": ["Do", "Are", "Will", "Did"],
                "answer": "Are",
                "explanation": "Вопрос строится через форму TO BE.",
            },

            {
                "order": 6,
                "prompt": "Is she going to travel?",
                "options": [
                    "Yes, she is.",
                    "Yes, she does.",
                    "Yes, she will.",
                    "Yes, she has.",
                ],
                "answer": "Yes, she is.",
                "explanation": "Краткий ответ повторяет форму is.",
            },

            {
                "order": 7,
                "prompt": "What ___ you going to do?",
                "options": ["do", "are", "will", "did"],
                "answer": "are",
                "explanation": "What are you going to do?",
            },

            {
                "order": 8,
                "prompt": "Where ___ he going to stay?",
                "options": ["does", "is", "will", "has"],
                "answer": "is",
                "explanation": "He → is.",
            },

            {
                "order": 9,
                "prompt": "Who ___ going to help us?",
                "options": [
                    "are",
                    "is",
                    "does",
                    "will be to",
                ],
                "answer": "is",
                "explanation": "Who как подлежащее обычно использует is.",
            },

            {
                "order": 10,
                "prompt": "Look at that glass. It ___ fall.",
                "options": [
                    "will think",
                    "is going to",
                    "does",
                    "has",
                ],
                "answer": "is going to",
                "explanation": "Есть очевидный признак будущего события.",
            },

            {
                "order": 11,
                "prompt": (
                    "I have already decided. "
                    "I ___ start a new course."
                ),
                "options": [
                    "will suddenly",
                    "am going to",
                    "do",
                    "have",
                ],
                "answer": "am going to",
                "explanation": "Решение было принято заранее.",
            },

            {
                "order": 12,
                "prompt": "The phone is ringing. I ___ answer it.",
                "options": [
                    "am going to yesterday",
                    "will",
                    "have",
                    "did",
                ],
                "answer": "will",
                "explanation": "Спонтанное решение → will.",
            },

            {
                "order": 13,
                "prompt": "I think they ___ win.",
                "options": [
                    "are going to because I think only",
                    "will",
                    "do",
                    "did",
                ],
                "answer": "will",
                "explanation": "Прогноз основан на мнении → will.",
            },

            {
                "order": 14,
                "prompt": "Be careful! You ___ fall.",
                "options": [
                    "will opinion",
                    "are going to",
                    "do",
                    "have",
                ],
                "answer": "are going to",
                "explanation": "Есть очевидная непосредственная опасность.",
            },

            {
                "order": 15,
                "prompt": "They aren't going to ___ the house.",
                "options": [
                    "sells",
                    "sold",
                    "sell",
                    "selling",
                ],
                "answer": "sell",
                "explanation": "После going to используется первая форма.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I going to study.",
                    "I am going to study.",
                    "I am going study.",
                    "I am going to studying.",
                ],
                "answer": "I am going to study.",
                "explanation": "Нужна форма am + going to + base verb.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She are going to call.",
                    "She is going to call.",
                    "She is going to calls.",
                    "She does going to call.",
                ],
                "answer": "She is going to call.",
                "explanation": "She → is going to + call.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "She doesn't going to call.",
                    "She isn't going to call.",
                    "She not going to calls.",
                    "She won't going to call.",
                ],
                "answer": "She isn't going to call.",
                "explanation": "Отрицание строится через TO BE + not.",
            },

            {
                "order": 19,
                "prompt": "Choose the correct question.",
                "options": [
                    "Does she going to come?",
                    "Is she going to come?",
                    "Will she going to come?",
                    "Is she going to comes?",
                ],
                "answer": "Is she going to come?",
                "explanation": "Is + subject + going to + base verb?",
            },

            {
                "order": 20,
                "prompt": "Choose the correct sentence with BE.",
                "options": [
                    "It is going to is difficult.",
                    "It is going to be difficult.",
                    "It is going to being difficult.",
                    "It going to be difficult.",
                ],
                "answer": "It is going to be difficult.",
                "explanation": "После going to используется base form be.",
            },

            {
                "order": 21,
                "prompt": "Choose the correct sentence with HAVE.",
                "options": [
                    "She is going to has a meeting.",
                    "She is going to have a meeting.",
                    "She is going to having a meeting.",
                    "She going to have a meeting.",
                ],
                "answer": "She is going to have a meeting.",
                "explanation": "После going to используется have.",
            },

            {
                "order": 22,
                "prompt": "Which sentence describes an arrangement?",
                "options": [
                    "I'm going to see my doctor sometime next week.",
                    "I'm seeing my doctor on Monday at ten.",
                    "I think I will see my doctor.",
                    "The doctor sees me yesterday.",
                ],
                "answer": "I'm seeing my doctor on Monday at ten.",
                "explanation": "Конкретная договорённость → Present Continuous.",
            },

            {
                "order": 23,
                "prompt": "Choose the best pair.",
                "options": [
                    (
                        "The phone is ringing. I'll answer it. / "
                        "I'm going to call him tonight."
                    ),
                    (
                        "The phone is ringing. I'm going to yesterday answer it. / "
                        "I will going to call him."
                    ),
                    (
                        "The phone rings. I did answer tomorrow. / "
                        "I'm going call him tonight."
                    ),
                    (
                        "The phone is ringing. I will to answer. / "
                        "I'm going to calling him."
                    ),
                ],
                "answer": (
                    "The phone is ringing. I'll answer it. / "
                    "I'm going to call him tonight."
                ),
                "explanation": (
                    "Will → спонтанное решение; "
                    "going to → заранее принятый план."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the correct prediction pair.",
                "options": [
                    (
                        "I think it will rain. / "
                        "Look at the clouds. It is going to rain."
                    ),
                    (
                        "I think it is going to because opinion rain. / "
                        "Look at the clouds. It will opinion rain."
                    ),
                    (
                        "I think it will raining. / "
                        "It is going to rains."
                    ),
                    (
                        "I think it rains tomorrow yesterday. / "
                        "It going to rain."
                    ),
                ],
                "answer": (
                    "I think it will rain. / "
                    "Look at the clouds. It is going to rain."
                ),
                "explanation": (
                    "Will → мнение; going to → видимые признаки."
                ),
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
                "✅ A1 Lesson 37 seeded: BE GOING TO"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
