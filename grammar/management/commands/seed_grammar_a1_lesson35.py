from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 35: Past Perfect Continuous."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=35,

                defaults={
                    "title":
                        "Past Perfect Continuous",

                    "slug":
                        "past-perfect-continuous",

                    "theory_text":
                        "Past Perfect Continuous: "
                        "HAD BEEN + verb-ing.",

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
                    "Процесс до момента в прошлом",

                "body":
                    """Past Perfect Continuous показывает процесс,
который начался раньше
и продолжался до другого момента
в прошлом.

I had been working for three hours
before he arrived.

Сначала:

я начал работать;

работал три часа.

Потом:

он пришёл.

Главная идея:

длительный процесс
→ до другого события в прошлом.""",
            },


            {
                "order": 2,
                "title":
                    "Формула HAD BEEN + -ING",

                "body":
                    """Формула:

HAD + BEEN + verb-ing

I had been working.

She had been studying.

They had been waiting.

HAD BEEN одинаково
для всех подлежащих:

I
you
he
she
it
we
they.""",
            },


            {
                "order": 3,
                "title":
                    "Как образуется -ING",

                "body":
                    """Обычно добавляем -ING:

work → working
read → reading
play → playing

Немая E исчезает:

write → writing
make → making

Иногда согласная удваивается:

run → running
sit → sitting

IE меняется на Y:

lie → lying.""",
            },


            {
                "order": 4,
                "title":
                    "FOR и SINCE",

                "body":
                    """FOR показывает продолжительность:

for two hours
for three days
for five years

I had been working
for three hours.

SINCE показывает начальную точку:

since morning
since Monday
since 2020

She had been studying
since morning.

FOR = сколько времени

SINCE = с какого момента.""",
            },


            {
                "order": 5,
                "title":
                    "BEFORE и WHEN",

                "body":
                    """Процесс происходил раньше,
а потом произошло другое событие.

I had been waiting
before the bus arrived.

I had been studying
when she called.

Позднее событие обычно стоит
в Past Simple:

arrived

called

started

came.""",
            },


            {
                "order": 6,
                "title":
                    "BY THE TIME",

                "body":
                    """BY THE TIME = к тому времени как.

By the time he arrived,
I had been waiting
for an hour.

К его приходу
процесс ожидания уже длился час.

Ещё пример:

By the time the lesson started,
we had been waiting
for twenty minutes.""",
            },


            {
                "order": 7,
                "title":
                    "Причина результата в прошлом",

                "body":
                    """Past Perfect Continuous
может объяснять состояние в прошлом.

She was tired because
she had been working all day.

He was wet because
he had been walking in the rain.

Her eyes were red because
she had been crying.

Процесс произошёл раньше
и объясняет прошлый результат.""",
            },


            {
                "order": 8,
                "title":
                    "HOW LONG",

                "body":
                    """Чтобы спросить о длительности:

HOW LONG + HAD + subject
+ BEEN + verb-ing?

How long had you been waiting?

How long had she been studying
before the exam?

Ответ:

I had been waiting
for an hour.

She had been studying
since morning.""",
            },


            {
                "order": 9,
                "title":
                    "Отрицание и вопрос",

                "body":
                    """Отрицание:

HADN'T BEEN + verb-ing

I hadn't been sleeping well.

She hadn't been working.

Вопрос:

Had you been waiting?

Had she been studying?

Краткие ответы:

Yes, I had.

No, I hadn't.

Yes, she had.

No, she hadn't.""",
            },


            {
                "order": 10,
                "title":
                    "Past Perfect или Continuous?",

                "body":
                    """Past Perfect:

HAD + V3

Важен результат или количество.

She had written five pages.

Past Perfect Continuous:

HAD BEEN + -ING

Важен процесс или длительность.

She had been writing
for two hours.

Простое правило:

сколько сделано?
→ Past Perfect

как долго?
→ Past Perfect Continuous.""",
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
                    "I ___ for two hours before she arrived.",

                "options": [
                    "had been working",
                    "have been working",
                    "was worked",
                    "had working",
                ],

                "answer":
                    "had been working",

                "explanation":
                    "Процесс длился до другого события в прошлом.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "They ___ for an hour before the bus came.",

                "options": [
                    "had been waiting",
                    "have waited",
                    "were waited",
                    "had waited an hour once",
                ],

                "answer":
                    "had been waiting",

                "explanation":
                    "Ожидание продолжалось до приезда автобуса.",
            },


            # SECTION 2

            {
                "order": 3,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери правильную форму.",

                "options": [
                    "She",
                    "had",
                    "been",
                    "studying",
                ],

                "answer":
                    "She had been studying",

                "explanation":
                    "Past Perfect Continuous = HAD BEEN + verb-ing.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "We had been travelling.",
                    "We had travelling.",
                    "We had been travel.",
                    "We were been travelling.",
                ],

                "answer":
                    "We had been travelling.",

                "explanation":
                    "Нужны все три части: HAD + BEEN + TRAVELLING.",
            },


            # SECTION 3

            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "write → ___",

                "options": [],

                "answer":
                    "writing",

                "explanation":
                    "WRITE → WRITING: немая E исчезает.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "Choose the correct -ING form of RUN.",

                "options": [
                    "running",
                    "runing",
                    "runned",
                    "runeing",
                ],

                "answer":
                    "running",

                "explanation":
                    "RUN → RUNNING: согласная удваивается.",
            },


            # SECTION 4

            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She had been working ___ three hours.",

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
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "He had been studying ___ morning.",

                "options": [
                    "since",
                    "for",
                    "ago",
                    "during",
                ],

                "answer":
                    "since",

                "explanation":
                    "MORNING — начальная точка → SINCE.",
            },


            # SECTION 5

            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "We had been talking when the teacher ___.",

                "options": [
                    "entered",
                    "had entered earlier for hours",
                    "has entered",
                    "enter",
                ],

                "answer":
                    "entered",

                "explanation":
                    "Позднее короткое событие → Past Simple.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "She had been sleeping before the phone ___.",

                "options": [
                    "rang",
                    "had rang",
                    "has rung",
                    "ring",
                ],

                "answer":
                    "rang",

                "explanation":
                    "Звонок произошёл после длительного процесса.",
            },


            # SECTION 6

            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "By the time I arrived, they ___ for forty minutes.",

                "options": [
                    "had been waiting",
                    "have been waiting",
                    "were waited",
                    "had waiting",
                ],

                "answer":
                    "had been waiting",

                "explanation":
                    "К моменту приезда процесс длился уже 40 минут.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "By the time the exam started, we ___ for an hour.",

                "options": [
                    "had been studying",
                    "have studied",
                    "were study",
                    "had studied one hour only",
                ],

                "answer":
                    "had been studying",

                "explanation":
                    "Процесс подготовки длился до начала экзамена.",
            },


            # SECTION 7

            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "She was tired because she ___ all day.",

                "options": [
                    "had been working",
                    "has been working",
                    "had worked five tasks",
                    "was worked",
                ],

                "answer":
                    "had been working",

                "explanation":
                    "Длительный процесс объясняет усталость в прошлом.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "His clothes were wet because he ___ in the rain.",

                "options": [
                    "had been walking",
                    "has walked",
                    "had walked one street",
                    "was walked",
                ],

                "answer":
                    "had been walking",

                "explanation":
                    "Процесс объясняет видимый прошлый результат.",
            },


            # SECTION 8

            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "How long ___ you been waiting before the doctor came?",

                "options": [
                    "had",
                    "have",
                    "did",
                    "were",
                ],

                "answer":
                    "had",

                "explanation":
                    "Вопрос: HOW LONG HAD YOU BEEN WAITING?",
            },

            {
                "order": 16,
                "section": 8,
                "type": "build",

                "prompt":
                    "Собери вопрос.",

                "options": [
                    "How",
                    "long",
                    "had",
                    "she",
                    "been",
                    "working",
                ],

                "answer":
                    "How long had she been working",

                "explanation":
                    "HOW LONG + HAD + subject + BEEN + verb-ing.",
            },


            # SECTION 9

            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "They ___ been waiting long before the taxi arrived.",

                "options": [
                    "hadn't",
                    "didn't",
                    "weren't",
                    "haven't",
                ],

                "answer":
                    "hadn't",

                "explanation":
                    "Отрицание = HADN'T BEEN + verb-ing.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "___ she been working before you called?",

                "options": [
                    "Had",
                    "Did",
                    "Was",
                    "Has",
                ],

                "answer":
                    "Had",

                "explanation":
                    "Вопрос Past Perfect Continuous начинается с HAD.",
            },


            # SECTION 10

            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "She ___ five pages before lunch.",

                "options": [
                    "had written",
                    "had been writing five pages for",
                    "had wrote",
                    "was written",
                ],

                "answer":
                    "had written",

                "explanation":
                    "FIVE PAGES — количество результата → Past Perfect.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "She ___ for two hours before lunch.",

                "options": [
                    "had been writing",
                    "had written two hours",
                    "was wrote",
                    "had writing",
                ],

                "answer":
                    "had been writing",

                "explanation":
                    "TWO HOURS — длительность → Past Perfect Continuous.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "Tom was exhausted because he ___ all night.",

                "options": [
                    "had been driving",
                    "has been driving",
                    "had driven three cars",
                    "was drove",
                ],

                "answer":
                    "had been driving",

                "explanation":
                    "Длительный процесс объясняет прошлое состояние.",
            },

            {
                "order": 22,

                "prompt":
                    "We ___ for two hours before the restaurant opened.",

                "options": [
                    "had been waiting",
                    "have waited",
                    "were waited",
                    "had waited two people",
                ],

                "answer":
                    "had been waiting",

                "explanation":
                    "FOR TWO HOURS → длительный процесс до прошлого события.",
            },

            {
                "order": 23,

                "prompt":
                    "Choose the correct structure.",

                "options": [
                    "He had been studying.",
                    "He had studying.",
                    "He had been study.",
                    "He was been studying.",
                ],

                "answer":
                    "He had been studying.",

                "explanation":
                    "HAD + BEEN + verb-ing.",
            },

            {
                "order": 24,

                "prompt":
                    "They had been living there ___ 2018.",

                "options": [
                    "since",
                    "for",
                    "ago",
                    "last",
                ],

                "answer":
                    "since",

                "explanation":
                    "2018 — начальная точка → SINCE.",
            },

            {
                "order": 25,

                "prompt":
                    "She had been learning English ___ four years.",

                "options": [
                    "for",
                    "since",
                    "ago",
                    "from",
                ],

                "answer":
                    "for",

                "explanation":
                    "FOUR YEARS — продолжительность → FOR.",
            },

            {
                "order": 26,

                "prompt":
                    "How long ___ they been travelling before they stopped?",

                "options": [
                    "had",
                    "have",
                    "were",
                    "did",
                ],

                "answer":
                    "had",

                "explanation":
                    "HOW LONG HAD THEY BEEN TRAVELLING?",
            },

            {
                "order": 27,

                "prompt":
                    "The streets were wet because it ___.",

                "options": [
                    "had been raining",
                    "has been raining",
                    "had rained three streets",
                    "was rain",
                ],

                "answer":
                    "had been raining",

                "explanation":
                    "Недавний длительный процесс объясняет прошлый результат.",
            },

            {
                "order": 28,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "I hadn't been sleeping well.",
                    "I didn't been sleeping well.",
                    "I hadn't been sleep well.",
                    "I wasn't been sleeping well.",
                ],

                "answer":
                    "I hadn't been sleeping well.",

                "explanation":
                    "HADN'T + BEEN + verb-ing.",
            },

            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "He had written six emails. / He had been writing for three hours.",
                    "He had been writing six emails. / He had written for three hours.",
                    "He had wrote six emails. / He had been wrote for three hours.",
                    "He was written six emails. / He had writing for three hours.",
                ],

                "answer":
                    "He had written six emails. / He had been writing for three hours.",

                "explanation":
                    "Количество → Past Perfect; длительность → Past Perfect Continuous.",
            },

            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "By the time she arrived, I had been working for two hours.",
                    "By the time she arrived, I have been working for two hours.",
                    "By the time she had arrived, I had been work for two hours.",
                    "By the time she arrives, I had working for two hours.",
                ],

                "answer":
                    "By the time she arrived, I had been working for two hours.",

                "explanation":
                    "Длительный процесс до другого события в прошлом → Past Perfect Continuous.",
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
                "✅ Interactive A1 Lesson 35 seeded"
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
