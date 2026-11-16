from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 32: Present Perfect Continuous."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=32,

                defaults={
                    "title":
                        "Present Perfect Continuous",

                    "slug":
                        "present-perfect-continuous",

                    "theory_text":
                        "Present Perfect Continuous.",

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
                    "Что показывает Present Perfect Continuous?",

                "body":
                    """Present Perfect Continuous показывает процесс,
который начался раньше
и связан с настоящим.

I have been working for three hours.

Я начал работать три часа назад
и всё ещё работаю.

She has been studying since morning.

Она начала заниматься утром
и продолжает сейчас.

Главная идея:

началось раньше
→ длилось некоторое время
→ связано с настоящим.""",
            },


            {
                "order": 2,
                "title":
                    "Основная формула",

                "body":
                    """Формула:

HAVE / HAS + BEEN + verb-ing

Примеры:

I have been working.

We have been waiting.

She has been reading.

He has been sleeping.

Важно сохранить все части:

HAVE / HAS

+

BEEN

+

глагол с -ING.""",
            },


            {
                "order": 3,
                "title":
                    "HAVE BEEN или HAS BEEN?",

                "body":
                    """HAVE BEEN:

I
you
we
they

I have been working.

They have been waiting.

HAS BEEN:

he
she
it

He has been working.

She has been studying.

It has been raining.""",
            },


            {
                "order": 4,
                "title":
                    "Как добавить -ING?",

                "body":
                    """Обычно просто добавляем -ING:

work → working
read → reading
play → playing

Если глагол заканчивается на немую E:

write → writing
make → making

У некоторых коротких глаголов
последняя согласная удваивается:

run → running
sit → sitting

IE меняется на Y:

lie → lying.""",
            },


            {
                "order": 5,
                "title":
                    "Действие продолжается сейчас",

                "body":
                    """Это одно из главных применений времени.

I have been learning English
for six months.

→ начал шесть месяцев назад
и продолжаю сейчас.

We have been waiting
for an hour.

→ начали ждать час назад
и всё ещё ждём.

She has been working
since nine.

→ работает с девяти до сих пор.""",
            },


            {
                "order": 6,
                "title":
                    "FOR и SINCE",

                "body":
                    """FOR показывает продолжительность:

for two hours
for three days
for five years

I have been working
for two hours.

SINCE показывает начальную точку:

since Monday
since 2020
since morning
since five o'clock

She has been studying
since morning.

FOR = сколько времени

SINCE = с какого момента.""",
            },


            {
                "order": 7,
                "title":
                    "HOW LONG",

                "body":
                    """Чтобы спросить,
как долго продолжается действие:

HOW LONG + HAVE/HAS + subject
+ BEEN + verb-ing?

How long have you been waiting?

How long has she been studying?

Ответ:

I have been waiting
for twenty minutes.

She has been studying
since eight o'clock.""",
            },


            {
                "order": 8,
                "title":
                    "Процесс только что закончился",

                "body":
                    """Действие может уже закончиться,
но его результат виден сейчас.

You are wet.

Have you been walking in the rain?

Her eyes are red.

She has been crying.

The ground is wet.

It has been raining.

Здесь важен недавний процесс,
который объясняет ситуацию сейчас.""",
            },


            {
                "order": 9,
                "title":
                    "Отрицание и вопрос",

                "body":
                    """Отрицание:

HAVEN'T / HASN'T + BEEN + verb-ing

I haven't been sleeping well.

She hasn't been working recently.

Вопрос:

Have you been working?

Has she been studying?

Краткие ответы:

Yes, I have.
No, I haven't.

Yes, she has.
No, she hasn't.""",
            },


            {
                "order": 10,
                "title":
                    "Глаголы состояния",

                "body":
                    """Некоторые глаголы обычно
не используются в Continuous.

Например:

know
understand
like
love
want
need
believe
own

Поэтому:

I have known him for years.

Не:

I have been knowing him.

I have had this phone for two years.

Не:

I have been having this phone
в значении владения.""",
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
                    "I ___ English for six months.",

                "options": [
                    "have been learning",
                    "am learn since",
                    "have learned yesterday",
                    "been learning",
                ],

                "answer":
                    "have been learning",

                "explanation":
                    "Действие началось раньше и продолжается сейчас.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "We ___ for the bus for thirty minutes.",

                "options": [
                    "have been waiting",
                    "are waited",
                    "have waiting",
                    "waited since",
                ],

                "answer":
                    "have been waiting",

                "explanation":
                    "FOR THIRTY MINUTES показывает длительный процесс.",
            },


            # SECTION 2

            {
                "order": 3,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери правильную форму.",

                "options": [
                    "I",
                    "have",
                    "been",
                    "working",
                ],

                "answer":
                    "I have been working",

                "explanation":
                    "Формула: HAVE + BEEN + verb-ing.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She has been studying.",
                    "She has studying.",
                    "She been studying.",
                    "She has been study.",
                ],

                "answer":
                    "She has been studying.",

                "explanation":
                    "Нужны HAS + BEEN + STUDYING.",
            },


            # SECTION 3

            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "My brother ___ been working all day.",

                "options": [
                    "has",
                    "have",
                    "is",
                    "did",
                ],

                "answer":
                    "has",

                "explanation":
                    "My brother = HE → HAS BEEN.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "The children ___ been playing outside.",

                "options": [
                    "have",
                    "has",
                    "are",
                    "did",
                ],

                "answer":
                    "have",

                "explanation":
                    "The children = THEY → HAVE BEEN.",
            },


            # SECTION 4

            {
                "order": 7,
                "section": 4,
                "type": "fill",

                "prompt":
                    "write → ___",

                "options": [],

                "answer":
                    "writing",

                "explanation":
                    "Убираем немую E и добавляем -ING.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct -ING form of RUN.",

                "options": [
                    "running",
                    "runing",
                    "runeing",
                    "runned",
                ],

                "answer":
                    "running",

                "explanation":
                    "Последняя согласная удваивается: RUN → RUNNING.",
            },


            # SECTION 5

            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "She ___ since nine o'clock and is still at work.",

                "options": [
                    "has been working",
                    "worked yesterday",
                    "has work",
                    "is worked",
                ],

                "answer":
                    "has been working",

                "explanation":
                    "Работа началась раньше и продолжается сейчас.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "They ___ for an hour and are still waiting.",

                "options": [
                    "have been waiting",
                    "waited yesterday",
                    "have waited one person",
                    "are wait",
                ],

                "answer":
                    "have been waiting",

                "explanation":
                    "Действие продолжается до настоящего момента.",
            },


            # SECTION 6

            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "I have been studying ___ three hours.",

                "options": [
                    "for",
                    "since",
                    "ago",
                    "last",
                ],

                "answer":
                    "for",

                "explanation":
                    "THREE HOURS — продолжительность → FOR.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "She has been working ___ Monday.",

                "options": [
                    "since",
                    "for",
                    "ago",
                    "during",
                ],

                "answer":
                    "since",

                "explanation":
                    "MONDAY — начальная точка → SINCE.",
            },


            # SECTION 7

            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "How long ___ you been waiting?",

                "options": [
                    "have",
                    "has",
                    "did",
                    "are",
                ],

                "answer":
                    "have",

                "explanation":
                    "YOU → HAVE YOU BEEN WAITING?",
            },

            {
                "order": 14,
                "section": 7,
                "type": "build",

                "prompt":
                    "Собери вопрос.",

                "options": [
                    "How",
                    "long",
                    "has",
                    "she",
                    "been",
                    "studying",
                ],

                "answer":
                    "How long has she been studying",

                "explanation":
                    "HOW LONG + HAS + SHE + BEEN + STUDYING.",
            },


            # SECTION 8

            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "The ground is wet because it ___.",

                "options": [
                    "has been raining",
                    "has been rained",
                    "has raining",
                    "rained since",
                ],

                "answer":
                    "has been raining",

                "explanation":
                    "Мокрая земля — видимый результат недавнего дождя.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "You are out of breath. ___ you been running?",

                "options": [
                    "Have",
                    "Did",
                    "Are",
                    "Do",
                ],

                "answer":
                    "Have",

                "explanation":
                    "Текущий результат объясняется недавним процессом.",
            },


            # SECTION 9

            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "She ___ been sleeping well recently.",

                "options": [
                    "hasn't",
                    "doesn't",
                    "isn't",
                    "didn't",
                ],

                "answer":
                    "hasn't",

                "explanation":
                    "Отрицание: HASN'T BEEN + verb-ing.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "___ they been working all morning?",

                "options": [
                    "Have",
                    "Did",
                    "Are",
                    "Do",
                ],

                "answer":
                    "Have",

                "explanation":
                    "Вопрос: HAVE THEY BEEN WORKING?",
            },


            # SECTION 10

            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "I ___ him for ten years.",

                "options": [
                    "have known",
                    "have been knowing",
                    "am knowing",
                    "have know",
                ],

                "answer":
                    "have known",

                "explanation":
                    "KNOW — глагол состояния.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence about possession.",

                "options": [
                    "I have had this car for three years.",
                    "I have been having this car for three years.",
                    "I am having this car since 2023.",
                    "I have been had this car.",
                ],

                "answer":
                    "I have had this car for three years.",

                "explanation":
                    "HAVE в значении владения обычно не используется в Continuous.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "We ___ for you since ten o'clock.",

                "options": [
                    "have been waiting",
                    "have waiting",
                    "are waited",
                    "waited since",
                ],

                "answer":
                    "have been waiting",

                "explanation":
                    "SINCE + продолжающийся процесс → Present Perfect Continuous.",
            },

            {
                "order": 22,

                "prompt":
                    "Anna ___ English all afternoon.",

                "options": [
                    "has been studying",
                    "has studied three languages",
                    "has study",
                    "is studied",
                ],

                "answer":
                    "has been studying",

                "explanation":
                    "ALL AFTERNOON подчёркивает длительность процесса.",
            },

            {
                "order": 23,

                "prompt":
                    "Choose the correct structure.",

                "options": [
                    "They have been working.",
                    "They have working been.",
                    "They been have working.",
                    "They have been work.",
                ],

                "answer":
                    "They have been working.",

                "explanation":
                    "HAVE + BEEN + verb-ing.",
            },

            {
                "order": 24,

                "prompt":
                    "It ___ been snowing since morning.",

                "options": [
                    "has",
                    "have",
                    "is",
                    "did",
                ],

                "answer":
                    "has",

                "explanation":
                    "IT используется с HAS.",
            },

            {
                "order": 25,

                "prompt":
                    "How long ___ he been learning English?",

                "options": [
                    "has",
                    "have",
                    "did",
                    "is",
                ],

                "answer":
                    "has",

                "explanation":
                    "HE → HAS HE BEEN LEARNING?",
            },

            {
                "order": 26,

                "prompt":
                    "I have been working here ___ 2022.",

                "options": [
                    "since",
                    "for",
                    "ago",
                    "last",
                ],

                "answer":
                    "since",

                "explanation":
                    "2022 — начальная точка.",
            },

            {
                "order": 27,

                "prompt":
                    "They have been travelling ___ two weeks.",

                "options": [
                    "for",
                    "since",
                    "ago",
                    "from",
                ],

                "answer":
                    "for",

                "explanation":
                    "TWO WEEKS — продолжительность.",
            },

            {
                "order": 28,

                "prompt":
                    "Her eyes are red. She ___.",

                "options": [
                    "has been crying",
                    "has been cried",
                    "has crying",
                    "cried since",
                ],

                "answer":
                    "has been crying",

                "explanation":
                    "Видимый результат объясняется недавним процессом.",
            },

            {
                "order": 29,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "I haven't been sleeping well.",
                    "I don't been sleeping well.",
                    "I haven't been sleep well.",
                    "I am not been sleeping well.",
                ],

                "answer":
                    "I haven't been sleeping well.",

                "explanation":
                    "HAVEN'T + BEEN + verb-ing.",
            },

            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "She has been working since Monday.",
                    "She has been work since Monday.",
                    "She have been working since Monday.",
                    "She has working since Monday.",
                ],

                "answer":
                    "She has been working since Monday.",

                "explanation":
                    "HAS + BEEN + WORKING + SINCE + начальная точка.",
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
                "✅ Interactive A1 Lesson 32 seeded"
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
