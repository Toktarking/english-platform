from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 36: Future Simple with WILL."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=36,

                defaults={
                    "title":
                        "Future Simple с WILL",

                    "slug":
                        "future-simple-will",

                    "theory_text":
                        "Future Simple with WILL.",

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
                    "Что такое Future Simple?",

                "body":
                    """Future Simple говорит о будущем.

Основной помощник:

WILL

Примеры:

I will call you tomorrow.

She will help us.

They will come later.

WILL часто используется для:

будущего действия;

решения в момент речи;

обещания;

предположения.""",
            },


            {
                "order": 2,
                "title":
                    "Формула WILL + глагол",

                "body":
                    """Формула:

subject + WILL + base verb

I will work.

She will come.

They will study.

WILL одинаков для всех:

I
you
he
she
it
we
they

После WILL не меняем глагол.""",
            },


            {
                "order": 3,
                "title":
                    "После WILL — только первая форма",

                "body":
                    """После WILL используется
основная форма глагола.

Правильно:

will go

will work

will study

will be

will have

Неправильно:

will goes

will worked

will studying

will to go.""",
            },


            {
                "order": 4,
                "title":
                    "Спонтанное решение",

                "body":
                    """WILL часто используется,
когда решение принимается прямо сейчас.

The phone is ringing.

I'll answer it.

I'm thirsty.

I'll get some water.

Someone is at the door.

I'll open it.

Это не заранее подготовленный план.""",
            },


            {
                "order": 5,
                "title":
                    "Обещание и помощь",

                "body":
                    """WILL используется в обещаниях.

I will help you.

I won't tell anyone.

I promise I'll call you.

Также WILL подходит
для предложения помощи.

I'll carry your bag.

I'll explain the rule.

I'll open the window.""",
            },


            {
                "order": 6,
                "title":
                    "Прогноз и мнение",

                "body":
                    """WILL часто используется
для прогноза или мнения.

I think it will rain.

She will probably come.

I believe they will win.

I'm sure he will understand.

Полезные слова:

I think

probably

maybe

perhaps

I'm sure.""",
            },


            {
                "order": 7,
                "title":
                    "Отрицание WON'T",

                "body":
                    """WILL NOT сокращается до:

WON'T

Формула:

subject + WON'T + base verb

I won't come.

She won't work tomorrow.

They won't agree.

После WON'T тоже нужна
первая форма глагола.

Не:

won't goes.""",
            },


            {
                "order": 8,
                "title":
                    "Вопросы с WILL",

                "body":
                    """В вопросе WILL ставится
перед подлежащим.

Will you come?

Will she help us?

Will they arrive soon?

Краткие ответы:

Yes, I will.

No, I won't.

Yes, she will.

No, she won't.""",
            },


            {
                "order": 9,
                "title":
                    "WHEN и IF: без WILL",

                "body":
                    """После WHEN и IF
в придаточной части будущего
обычно используем Present Simple.

Правильно:

I will call you when I arrive.

If it rains,
we will stay home.

Не:

when I will arrive

if it will rain

WILL остаётся в главной части.""",
            },


            {
                "order": 10,
                "title":
                    "WILL или заранее подготовленный план?",

                "body":
                    """WILL особенно подходит,
если:

решение принято сейчас;

это обещание;

это помощь;

это прогноз.

I'll answer the phone.

I will help you.

I think she will pass.

Если план уже был подготовлен заранее,
обычно используется BE GOING TO
или Present Continuous.

Эту разницу разберём дальше.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects.update_or_create(
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
                    "I ___ call you tomorrow.",

                "options": [
                    "will",
                    "am will",
                    "did",
                    "have",
                ],

                "answer":
                    "will",

                "explanation":
                    "Future Simple использует WILL.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "They ___ arrive later.",

                "options": [
                    "will",
                    "are will",
                    "do",
                    "have",
                ],

                "answer":
                    "will",

                "explanation":
                    "Будущее действие → WILL.",
            },


            # SECTION 2

            {
                "order": 3,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери предложение.",

                "options": [
                    "She",
                    "will",
                    "help",
                    "us",
                ],

                "answer":
                    "She will help us",

                "explanation":
                    "subject + WILL + base verb.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "We will study tomorrow.",
                    "We will studies tomorrow.",
                    "We are will study tomorrow.",
                    "We will studied tomorrow.",
                ],

                "answer":
                    "We will study tomorrow.",

                "explanation":
                    "После WILL используется основная форма STUDY.",
            },


            # SECTION 3

            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "My brother will ___ home soon.",

                "options": [
                    "come",
                    "comes",
                    "came",
                    "coming",
                ],

                "answer":
                    "come",

                "explanation":
                    "После WILL нужна первая форма COME.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "She will ___ busy tomorrow.",

                "options": [
                    "be",
                    "is",
                    "was",
                    "being",
                ],

                "answer":
                    "be",

                "explanation":
                    "После WILL используется BE.",
            },


            # SECTION 4

            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "The phone is ringing. I ___ it.",

                "options": [
                    "will answer",
                    "answered yesterday",
                    "am answer",
                    "will answered",
                ],

                "answer":
                    "will answer",

                "explanation":
                    "Решение принято прямо сейчас.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "It's cold in here. I ___ the window.",

                "options": [
                    "will close",
                    "closed tomorrow",
                    "will closed",
                    "am close",
                ],

                "answer":
                    "will close",

                "explanation":
                    "Спонтанное решение → WILL.",
            },


            # SECTION 5

            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Don't worry. I ___ you.",

                "options": [
                    "will help",
                    "helped tomorrow",
                    "will helped",
                    "am help",
                ],

                "answer":
                    "will help",

                "explanation":
                    "Предложение помощи → WILL.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "I promise I ___ anyone.",

                "options": [
                    "won't tell",
                    "don't told",
                    "won't told",
                    "am not tell",
                ],

                "answer":
                    "won't tell",

                "explanation":
                    "Отрицательное обещание → WON'T + base verb.",
            },


            # SECTION 6

            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "I think it ___ rain tomorrow.",

                "options": [
                    "will",
                    "did",
                    "has",
                    "is rain",
                ],

                "answer":
                    "will",

                "explanation":
                    "I THINK + прогноз → WILL.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "She will probably ___ the exam.",

                "options": [
                    "pass",
                    "passes",
                    "passed",
                    "passing",
                ],

                "answer":
                    "pass",

                "explanation":
                    "После WILL используется PASS.",
            },


            # SECTION 7

            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "He ___ be late.",

                "options": [
                    "won't",
                    "doesn't will",
                    "isn't will",
                    "not will",
                ],

                "answer":
                    "won't",

                "explanation":
                    "Отрицание Future Simple = WON'T.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "They won't come.",
                    "They won't comes.",
                    "They don't will come.",
                    "They won't came.",
                ],

                "answer":
                    "They won't come.",

                "explanation":
                    "WON'T + base verb.",
            },


            # SECTION 8

            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "___ she call us later?",

                "options": [
                    "Will",
                    "Does",
                    "Is",
                    "Has",
                ],

                "answer":
                    "Will",

                "explanation":
                    "Вопрос начинается с WILL.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Will they come?",

                "options": [
                    "Yes, they will.",
                    "Yes, they do.",
                    "Yes, they are.",
                    "Yes, they'll.",
                ],

                "answer":
                    "Yes, they will.",

                "explanation":
                    "Краткий ответ: YES, THEY WILL.",
            },


            # SECTION 9

            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "I will call you when I ___ home.",

                "options": [
                    "get",
                    "will get",
                    "got",
                    "getting",
                ],

                "answer":
                    "get",

                "explanation":
                    "После WHEN для будущего используется Present Simple.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "If it ___ tomorrow, we will stay home.",

                "options": [
                    "rains",
                    "will rain",
                    "rain will",
                    "rained yesterday",
                ],

                "answer":
                    "rains",

                "explanation":
                    "После IF → Present Simple.",
            },


            # SECTION 10

            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "The doorbell is ringing. Which is the best response?",

                "options": [
                    "I'll open the door.",
                    "I am going to open it; I planned this yesterday.",
                    "I opened it tomorrow.",
                    "I will opened it.",
                ],

                "answer":
                    "I'll open the door.",

                "explanation":
                    "Решение принято в момент речи → WILL.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Which sentence is a prediction?",

                "options": [
                    "I think our team will win.",
                    "I bought the tickets yesterday.",
                    "I am meeting him at six; it is arranged.",
                    "I visited them last week.",
                ],

                "answer":
                    "I think our team will win.",

                "explanation":
                    "Мнение о будущем → WILL.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "We ___ see you next week.",

                "options": [
                    "will",
                    "are will",
                    "did",
                    "have",
                ],

                "answer":
                    "will",

                "explanation":
                    "Future Simple = WILL + base verb.",
            },

            {
                "order": 22,

                "prompt":
                    "He will ___ more time tomorrow.",

                "options": [
                    "have",
                    "has",
                    "had",
                    "having",
                ],

                "answer":
                    "have",

                "explanation":
                    "После WILL используется HAVE.",
            },

            {
                "order": 23,

                "prompt":
                    "I forgot my pen. — Don't worry, I ___ you mine.",

                "options": [
                    "will lend",
                    "lent tomorrow",
                    "will lent",
                    "am lend",
                ],

                "answer":
                    "will lend",

                "explanation":
                    "Спонтанное предложение помощи → WILL.",
            },

            {
                "order": 24,

                "prompt":
                    "I promise I ___ late.",

                "options": [
                    "won't be",
                    "won't am",
                    "don't will be",
                    "won't was",
                ],

                "answer":
                    "won't be",

                "explanation":
                    "WON'T + BE.",
            },

            {
                "order": 25,

                "prompt":
                    "I believe people ___ live longer in the future.",

                "options": [
                    "will",
                    "did",
                    "are live",
                    "have",
                ],

                "answer":
                    "will",

                "explanation":
                    "BELIEVE + прогноз → WILL.",
            },

            {
                "order": 26,

                "prompt":
                    "___ you help me with this bag?",

                "options": [
                    "Will",
                    "Do will",
                    "Are",
                    "Did",
                ],

                "answer":
                    "Will",

                "explanation":
                    "WILL ставится перед подлежащим.",
            },

            {
                "order": 27,

                "prompt":
                    "Will Anna join us?",

                "options": [
                    "No, she won't.",
                    "No, she doesn't will.",
                    "No, she isn't.",
                    "No, she won't joins.",
                ],

                "answer":
                    "No, she won't.",

                "explanation":
                    "Краткий отрицательный ответ = WON'T.",
            },

            {
                "order": 28,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I'll text you when I arrive.",
                    "I'll text you when I will arrive.",
                    "I'll text you when I arrived tomorrow.",
                    "I'll text you when I arriving.",
                ],

                "answer":
                    "I'll text you when I arrive.",

                "explanation":
                    "После WHEN → Present Simple.",
            },

            {
                "order": 29,

                "prompt":
                    "Choose the correct conditional sentence.",

                "options": [
                    "If she calls, I will tell her.",
                    "If she will call, I will tell her.",
                    "If she calls, I will tells her.",
                    "If she called yesterday, I will told her.",
                ],

                "answer":
                    "If she calls, I will tell her.",

                "explanation":
                    "IF + Present Simple; главная часть + WILL.",
            },

            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "I think she will probably come.",
                    "I think she will probably comes.",
                    "I think she probably will came.",
                    "I think she will to come.",
                ],

                "answer":
                    "I think she will probably come.",

                "explanation":
                    "WILL + probably + base verb.",
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
                "✅ Interactive A1 Lesson 36 seeded"
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
