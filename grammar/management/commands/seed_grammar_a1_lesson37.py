from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 37: BE GOING TO."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=37,

                defaults={
                    "title":
                        "BE GOING TO",

                    "slug":
                        "be-going-to",

                    "theory_text":
                        "BE GOING TO.",

                    "estimated_minutes":
                        20,

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
        # 10 MICRO RULES
        # =================================================

        sections = [

            {
                "order": 1,
                "title":
                    "Что означает BE GOING TO?",

                "body":
                    """BE GOING TO используется,
когда решение о будущем
уже существует.

I am going to study tonight.

She is going to buy a new phone.

Также BE GOING TO используется
для прогноза по видимым признакам:

Look at those clouds.

It is going to rain.

Главные идеи:

план;

намерение;

видимый прогноз.""",
            },


            {
                "order": 2,
                "title":
                    "Формула AM / IS / ARE + GOING TO",

                "body":
                    """Формула:

subject
+ AM / IS / ARE
+ GOING TO
+ base verb

I am going to work.

She is going to study.

They are going to travel.

Запомни:

I → am

he / she / it → is

you / we / they → are.""",
            },


            {
                "order": 3,
                "title":
                    "После GOING TO — первая форма",

                "body":
                    """После GOING TO
используется основная форма глагола.

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

going to to work.""",
            },


            {
                "order": 4,
                "title":
                    "Заранее принятый план",

                "body":
                    """BE GOING TO подходит,
если решение было принято
до момента речи.

I am going to visit
my parents this weekend.

She is going to start
a new course.

They are going to travel
next month.

План уже существовал раньше.""",
            },


            {
                "order": 5,
                "title":
                    "Намерение",

                "body":
                    """BE GOING TO также показывает
намерение.

I am going to learn English.

She is going to save money.

He is going to stop smoking.

They are going to move abroad.

Не обязательно,
что всё уже организовано.

Главное:

решение или намерение
уже есть.""",
            },


            {
                "order": 6,
                "title":
                    "Прогноз по видимым признакам",

                "body":
                    """BE GOING TO используется,
если уже видны признаки
будущего события.

Look at the clouds.

It is going to rain.

Be careful!

You are going to fall.

The glass is moving.

It is going to fall.

Есть видимое основание
для прогноза.""",
            },


            {
                "order": 7,
                "title":
                    "GOING TO или WILL?",

                "body":
                    """WILL:

решение принято прямо сейчас.

The phone is ringing.

I'll answer it.

GOING TO:

решение было принято раньше.

I'm going to call him tonight.

Сравни:

I'll buy some bread.

→ решил сейчас.

I'm going to buy some bread
after work.

→ уже планировал.""",
            },


            {
                "order": 8,
                "title":
                    "Прогноз: WILL или GOING TO?",

                "body":
                    """Если это просто мнение:

WILL.

I think it will rain tomorrow.

Если есть видимые признаки:

BE GOING TO.

Look at the sky.

It is going to rain.

Коротко:

мнение → WILL

доказательства сейчас
→ GOING TO.""",
            },


            {
                "order": 9,
                "title":
                    "Отрицание",

                "body":
                    """Отрицание строится через TO BE.

I am not going to work.

She isn't going to come.

They aren't going to travel.

Формула:

AM / IS / ARE + NOT
+ GOING TO + base verb

Не используем DON'T:

She doesn't going to come.

→ неправильно.""",
            },


            {
                "order": 10,
                "title":
                    "Вопросы",

                "body":
                    """В вопросе форма TO BE
ставится перед подлежащим.

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

            # SECTION 1

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ going to study tonight.",

                "options": [
                    "am",
                    "is",
                    "are",
                    "do",
                ],

                "answer":
                    "am",

                "explanation":
                    "I → AM GOING TO.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "She ___ going to buy a new laptop.",

                "options": [
                    "is",
                    "am",
                    "are",
                    "does",
                ],

                "answer":
                    "is",

                "explanation":
                    "SHE → IS GOING TO.",
            },


            # SECTION 2

            {
                "order": 3,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери предложение.",

                "options": [
                    "They",
                    "are",
                    "going",
                    "to",
                    "travel",
                ],

                "answer":
                    "They are going to travel",

                "explanation":
                    "THEY → ARE GOING TO + base verb.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "We ___ going to start soon.",

                "options": [
                    "are",
                    "is",
                    "am",
                    "do",
                ],

                "answer":
                    "are",

                "explanation":
                    "WE используется с ARE.",
            },


            # SECTION 3

            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "He is going to ___ English.",

                "options": [
                    "learn",
                    "learns",
                    "learned",
                    "learning",
                ],

                "answer":
                    "learn",

                "explanation":
                    "После GOING TO используется base verb.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "We are going to ___ dinner at seven.",

                "options": [
                    "have",
                    "has",
                    "had",
                    "having",
                ],

                "answer":
                    "have",

                "explanation":
                    "После GOING TO → HAVE.",
            },


            # SECTION 4

            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "I bought the tickets yesterday. We ___ travel next week.",

                "options": [
                    "are going to",
                    "will suddenly",
                    "did",
                    "have",
                ],

                "answer":
                    "are going to",

                "explanation":
                    "План был принят заранее.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She has already decided. She ___ start a new course.",

                "options": [
                    "is going to",
                    "will just decide now",
                    "does",
                    "has",
                ],

                "answer":
                    "is going to",

                "explanation":
                    "Решение уже принято → GOING TO.",
            },


            # SECTION 5

            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "I ___ learn Spanish next year.",

                "options": [
                    "am going to",
                    "am going learning",
                    "will to",
                    "do going to",
                ],

                "answer":
                    "am going to",

                "explanation":
                    "Намерение → BE GOING TO.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "He ___ stop smoking.",

                "options": [
                    "is going to",
                    "is going stopping",
                    "does going to",
                    "going to is",
                ],

                "answer":
                    "is going to",

                "explanation":
                    "Существующее намерение → GOING TO.",
            },


            # SECTION 6

            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Look at those black clouds. It ___.",

                "options": [
                    "is going to rain",
                    "will rain because I think only",
                    "is going rain",
                    "going to rains",
                ],

                "answer":
                    "is going to rain",

                "explanation":
                    "Есть видимые признаки дождя.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Be careful! You ___.",

                "options": [
                    "are going to fall",
                    "will fell",
                    "are going fall",
                    "going to falls",
                ],

                "answer":
                    "are going to fall",

                "explanation":
                    "Видим непосредственную опасность.",
            },


            # SECTION 7

            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "The phone is ringing. I ___ it.",

                "options": [
                    "will answer",
                    "am going to answer because I planned yesterday",
                    "will answered",
                    "am answer",
                ],

                "answer":
                    "will answer",

                "explanation":
                    "Решение принято прямо сейчас → WILL.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I decided this morning. I ___ call him tonight.",

                "options": [
                    "am going to",
                    "will suddenly",
                    "do",
                    "am call",
                ],

                "answer":
                    "am going to",

                "explanation":
                    "Решение принято заранее → GOING TO.",
            },


            # SECTION 8

            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "I think our team ___ win.",

                "options": [
                    "will",
                    "is going to because of opinion only",
                    "does",
                    "has",
                ],

                "answer":
                    "will",

                "explanation":
                    "Личное мнение → WILL.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Look at the score. Our team is playing much better. They ___ win.",

                "options": [
                    "are going to",
                    "will opinion",
                    "are going win",
                    "going to wins",
                ],

                "answer":
                    "are going to",

                "explanation":
                    "Есть текущие признаки → GOING TO.",
            },


            # SECTION 9

            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "She ___ going to work tomorrow.",

                "options": [
                    "isn't",
                    "doesn't",
                    "won't be to",
                    "not is",
                ],

                "answer":
                    "isn't",

                "explanation":
                    "Отрицание строится через ISN'T.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "They aren't going to sell the house.",
                    "They don't going to sell the house.",
                    "They aren't going to selling the house.",
                    "They won't going to sell the house.",
                ],

                "answer":
                    "They aren't going to sell the house.",

                "explanation":
                    "ARE NOT + GOING TO + base verb.",
            },


            # SECTION 10

            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "___ you going to call her?",

                "options": [
                    "Are",
                    "Do",
                    "Will",
                    "Did",
                ],

                "answer":
                    "Are",

                "explanation":
                    "Вопрос строится через форму TO BE.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Is he going to come?",

                "options": [
                    "Yes, he is.",
                    "Yes, he does.",
                    "Yes, he will going.",
                    "Yes, he has.",
                ],

                "answer":
                    "Yes, he is.",

                "explanation":
                    "Краткий ответ повторяет IS.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "My parents ___ going to visit us this weekend.",

                "options": [
                    "are",
                    "is",
                    "am",
                    "do",
                ],

                "answer":
                    "are",

                "explanation":
                    "MY PARENTS = THEY → ARE.",
            },

            {
                "order": 22,

                "prompt":
                    "Anna is going to ___ a new job.",

                "options": [
                    "find",
                    "finds",
                    "found",
                    "finding",
                ],

                "answer":
                    "find",

                "explanation":
                    "После GOING TO используется base verb.",
            },

            {
                "order": 23,

                "prompt":
                    "We have already made the decision. We ___ move next year.",

                "options": [
                    "are going to",
                    "will suddenly",
                    "are move",
                    "did",
                ],

                "answer":
                    "are going to",

                "explanation":
                    "Решение существовало заранее.",
            },

            {
                "order": 24,

                "prompt":
                    "Look at that child near the edge! He ___.",

                "options": [
                    "is going to fall",
                    "will fell",
                    "is going fall",
                    "going to falls",
                ],

                "answer":
                    "is going to fall",

                "explanation":
                    "Есть очевидный признак будущего события.",
            },

            {
                "order": 25,

                "prompt":
                    "The doorbell is ringing. — I ___ the door.",

                "options": [
                    "will open",
                    "am going to because I planned it yesterday",
                    "will opened",
                    "am open",
                ],

                "answer":
                    "will open",

                "explanation":
                    "Спонтанное решение → WILL.",
            },

            {
                "order": 26,

                "prompt":
                    "I think she ___ pass the exam.",

                "options": [
                    "will",
                    "is going to because no evidence is given",
                    "does",
                    "has",
                ],

                "answer":
                    "will",

                "explanation":
                    "Личное мнение → WILL.",
            },

            {
                "order": 27,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "I am not going to buy it.",
                    "I don't going to buy it.",
                    "I am not going to buying it.",
                    "I won't going to buy it.",
                ],

                "answer":
                    "I am not going to buy it.",

                "explanation":
                    "AM NOT + GOING TO + base verb.",
            },

            {
                "order": 28,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Are they going to travel?",
                    "Do they going to travel?",
                    "Will they going to travel?",
                    "Are they going to travelling?",
                ],

                "answer":
                    "Are they going to travel?",

                "explanation":
                    "ARE + subject + GOING TO + base verb?",
            },

            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "I'll answer the phone. / I'm going to visit my parents this weekend.",
                    "I'm going answer the phone. / I will going to visit my parents.",
                    "I'll answered the phone. / I'm going to visiting my parents.",
                    "I answer will the phone. / I going to visit my parents.",
                ],

                "answer":
                    "I'll answer the phone. / I'm going to visit my parents this weekend.",

                "explanation":
                    "WILL → решение сейчас; GOING TO → заранее принятый план.",
            },

            {
                "order": 30,

                "prompt":
                    "Choose the correct prediction pair.",

                "options": [
                    "I think it will rain. / Look at the clouds. It is going to rain.",
                    "I think it is going to because opinion rain. / Look at the clouds. It will opinion rain.",
                    "I think it will raining. / It is going to rains.",
                    "I think it rains tomorrow. / It going to rain.",
                ],

                "answer":
                    "I think it will rain. / Look at the clouds. It is going to rain.",

                "explanation":
                    "Мнение → WILL; видимые признаки → GOING TO.",
            },

        ]


        all_exercises = (
            training
            +
            final_test
        )


        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

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
                "✅ Interactive A1 Lesson 37 seeded"
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
