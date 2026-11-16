from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 33: Present Perfect vs "
        "Present Perfect Continuous."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=33,

                defaults={
                    "title":
                        "Present Perfect и "
                        "Present Perfect Continuous",

                    "slug":
                        "present-perfect-vs-perfect-continuous",

                    "theory_text":
                        "Present Perfect vs "
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
                    "Результат или процесс?",

                "body":
                    """Оба времени связывают прошлое
с настоящим.

Present Perfect:

I have written five emails.

Важен результат:
пять писем готовы.

Present Perfect Continuous:

I have been writing emails
for two hours.

Важен процесс:
я занимаюсь этим уже два часа.

Главный вопрос:

что важнее —
результат или процесс?""",
            },


            {
                "order": 2,

                "title":
                    "Формы двух времён",

                "body":
                    """Present Perfect:

HAVE / HAS + V3

I have finished.

She has written.

Present Perfect Continuous:

HAVE / HAS + BEEN + verb-ing

I have been working.

She has been studying.

Запомни:

результат → HAVE/HAS + V3

процесс → HAVE/HAS BEEN + -ING""",
            },


            {
                "order": 3,

                "title":
                    "Готовый результат",

                "body":
                    """Если действие завершено
и важен готовый результат:

Present Perfect.

I have cleaned the room.

→ комната убрана.

She has written the report.

→ отчёт готов.

They have repaired the car.

→ машина отремонтирована.""",
            },


            {
                "order": 4,

                "title":
                    "Процесс и длительность",

                "body":
                    """Если важен процесс
или его длительность:

Present Perfect Continuous.

I have been working
for three hours.

She has been studying
since morning.

They have been waiting
for a long time.

Часто встречаются:

for
since
all day
all morning""",
            },


            {
                "order": 5,

                "title":
                    "HOW MANY или HOW LONG?",

                "body":
                    """HOW MANY спрашивает
о количестве результата.

How many emails
have you written?

→ сколько писем готово?

HOW LONG спрашивает
о длительности процесса.

How long
have you been writing?

→ как долго длится процесс?

Количество → Present Perfect.

Длительность → чаще Continuous.""",
            },


            {
                "order": 6,

                "title":
                    "Видимый результат процесса",

                "body":
                    """Иногда действие только что закончилось,
но его результат видно сейчас.

Тогда часто используется
Present Perfect Continuous.

Your clothes are dirty.

You have been working
in the garden.

Her eyes are red.

She has been crying.

The ground is wet.

It has been raining.""",
            },


            {
                "order": 7,

                "title":
                    "READ, WRITE, CLEAN",

                "body":
                    """Сравни:

I have read the book.

→ книга прочитана.

I have been reading the book.

→ я читал её некоторое время.

She has written the report.

→ отчёт готов.

She has been writing the report.

→ важен процесс написания.""",
            },


            {
                "order": 8,

                "title":
                    "FOR и SINCE могут быть с обоими",

                "body":
                    """С некоторыми длительными действиями
возможны оба времени.

I have worked here
for five years.

I have been working here
for five years.

Оба варианта возможны.

Present Perfect сильнее показывает факт.

Continuous сильнее подчёркивает
сам процесс и длительность.""",
            },


            {
                "order": 9,

                "title":
                    "Глаголы состояния",

                "body":
                    """Глаголы состояния обычно
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

Правильно:

I have known him
for ten years.

He has owned this house
since 2020.

Не:

I have been knowing him.""",
            },


            {
                "order": 10,

                "title":
                    "Как быстро выбрать время",

                "body":
                    """Спроси себя:

Готов результат?

→ Present Perfect

I have finished the work.

Сколько сделано?

→ Present Perfect

I have written five pages.

Как долго идёт процесс?

→ Present Perfect Continuous

I have been writing
for two hours.

Это глагол состояния?

→ Present Perfect

I have known her for years.""",
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
                    "I ___ five emails today.",

                "options": [
                    "have written",
                    "have been writing five",
                    "have wrote",
                    "am writing since",
                ],

                "answer":
                    "have written",

                "explanation":
                    "Пять готовых писем — результат и количество.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ emails for two hours.",

                "options": [
                    "have been writing",
                    "have written two hours",
                    "have wrote",
                    "am written",
                ],

                "answer":
                    "have been writing",

                "explanation":
                    "FOR TWO HOURS показывает длительность процесса.",
            },


            # SECTION 2

            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct Present Perfect form.",

                "options": [
                    "She has finished.",
                    "She has been finish.",
                    "She have finished.",
                    "She has finishing.",
                ],

                "answer":
                    "She has finished.",

                "explanation":
                    "Present Perfect = HAS + V3.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери Present Perfect Continuous.",

                "options": [
                    "She",
                    "has",
                    "been",
                    "studying",
                ],

                "answer":
                    "She has been studying",

                "explanation":
                    "Формула: HAS + BEEN + verb-ing.",
            },


            # SECTION 3

            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "The report is ready. She ___ it.",

                "options": [
                    "has written",
                    "has been writing only",
                    "has wrote",
                    "is write",
                ],

                "answer":
                    "has written",

                "explanation":
                    "Отчёт готов — важен завершённый результат.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "The room is clean now. We ___ it.",

                "options": [
                    "have cleaned",
                    "have been cleaning only",
                    "have clean",
                    "are cleaned",
                ],

                "answer":
                    "have cleaned",

                "explanation":
                    "Комната уже убрана — результат готов.",
            },


            # SECTION 4

            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "They ___ for three hours.",

                "options": [
                    "have been working",
                    "have worked three tasks",
                    "worked since",
                    "have work",
                ],

                "answer":
                    "have been working",

                "explanation":
                    "FOR THREE HOURS подчёркивает длительность.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She ___ since early morning.",

                "options": [
                    "has been studying",
                    "has studied three exams",
                    "studies yesterday",
                    "has study",
                ],

                "answer":
                    "has been studying",

                "explanation":
                    "SINCE EARLY MORNING подчёркивает процесс.",
            },


            # SECTION 5

            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "How many pages ___ you ___?",

                "options": [
                    "have / written",
                    "have / been writing",
                    "did / written",
                    "are / written",
                ],

                "answer":
                    "have / written",

                "explanation":
                    "HOW MANY спрашивает количество готовых страниц.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "How long ___ you ___?",

                "options": [
                    "have / been waiting",
                    "have / waited five people",
                    "did / been waiting",
                    "are / waited",
                ],

                "answer":
                    "have / been waiting",

                "explanation":
                    "HOW LONG спрашивает длительность процесса.",
            },


            # SECTION 6

            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Your clothes are dirty. You ___ in the garden.",

                "options": [
                    "have been working",
                    "have worked three gardens",
                    "have work",
                    "are worked",
                ],

                "answer":
                    "have been working",

                "explanation":
                    "Грязная одежда — видимый результат процесса.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Her eyes are red because she ___.",

                "options": [
                    "has been crying",
                    "has cried three tears",
                    "has cry",
                    "is cried",
                ],

                "answer":
                    "has been crying",

                "explanation":
                    "Красные глаза — след недавнего процесса.",
            },


            # SECTION 7

            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I ___ the book. I know how it ends.",

                "options": [
                    "have read",
                    "have been reading only",
                    "have been read",
                    "have reading",
                ],

                "answer":
                    "have read",

                "explanation":
                    "Книга прочитана — важен результат.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I ___ the book all afternoon.",

                "options": [
                    "have been reading",
                    "have read three books",
                    "have been read",
                    "am read",
                ],

                "answer":
                    "have been reading",

                "explanation":
                    "ALL AFTERNOON подчёркивает процесс.",
            },


            # SECTION 8

            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "She ___ here for five years.",

                "options": [
                    "has worked",
                    "has been working",
                    "both are possible",
                    "worked and still works only",
                ],

                "answer":
                    "both are possible",

                "explanation":
                    "С WORK обе формы возможны, если работа продолжается.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Which sentence emphasizes duration more strongly?",

                "options": [
                    "I have been working here for five years.",
                    "I worked here yesterday.",
                    "I have finished five tasks.",
                    "I work here every Monday.",
                ],

                "answer":
                    "I have been working here for five years.",

                "explanation":
                    "Continuous сильнее подчёркивает длительность процесса.",
            },


            # SECTION 9

            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "I ___ her for ten years.",

                "options": [
                    "have known",
                    "have been knowing",
                    "am knowing",
                    "have know",
                ],

                "answer":
                    "have known",

                "explanation":
                    "KNOW — stative verb, Continuous обычно не используется.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "He ___ this apartment since 2021.",

                "options": [
                    "has owned",
                    "has been owning",
                    "is owning since",
                    "has own",
                ],

                "answer":
                    "has owned",

                "explanation":
                    "OWN — глагол состояния.",
            },


            # SECTION 10

            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "She ___ six pages.",

                "options": [
                    "has written",
                    "has been writing six pages for",
                    "has wrote",
                    "has writing",
                ],

                "answer":
                    "has written",

                "explanation":
                    "SIX PAGES — количество готового результата.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "She ___ for two hours.",

                "options": [
                    "has been writing",
                    "has written two hours",
                    "has wrote",
                    "is written",
                ],

                "answer":
                    "has been writing",

                "explanation":
                    "FOR TWO HOURS — длительность процесса.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "We ___ ten exercises so far.",

                "options": [
                    "have completed",
                    "have been completing ten",
                    "have complete",
                    "are completing since",
                ],

                "answer":
                    "have completed",

                "explanation":
                    "TEN EXERCISES — количество готового результата.",
            },

            {
                "order": 22,

                "prompt":
                    "We ___ since nine o'clock.",

                "options": [
                    "have been studying",
                    "have studied ten lessons",
                    "have study",
                    "are studied",
                ],

                "answer":
                    "have been studying",

                "explanation":
                    "SINCE NINE показывает длительный процесс.",
            },

            {
                "order": 23,

                "prompt":
                    "The kitchen is clean. Dad ___ it.",

                "options": [
                    "has cleaned",
                    "has been cleaning only",
                    "has clean",
                    "has been cleaned it",
                ],

                "answer":
                    "has cleaned",

                "explanation":
                    "Кухня уже чистая — результат завершён.",
            },

            {
                "order": 24,

                "prompt":
                    "Dad is tired because he ___ the kitchen.",

                "options": [
                    "has been cleaning",
                    "has cleaned three kitchens",
                    "has been cleaned",
                    "has cleaning",
                ],

                "answer":
                    "has been cleaning",

                "explanation":
                    "Усталость — результат длительного процесса.",
            },

            {
                "order": 25,

                "prompt":
                    "How many calls ___ she ___ today?",

                "options": [
                    "has / made",
                    "has / been making",
                    "did / made",
                    "is / made",
                ],

                "answer":
                    "has / made",

                "explanation":
                    "HOW MANY → количество результата.",
            },

            {
                "order": 26,

                "prompt":
                    "How long ___ she ___ on the phone?",

                "options": [
                    "has / been talking",
                    "has / talked three calls",
                    "did / been talking",
                    "is / talked",
                ],

                "answer":
                    "has / been talking",

                "explanation":
                    "HOW LONG → длительность процесса.",
            },

            {
                "order": 27,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I have known him since school.",
                    "I have been knowing him since school.",
                    "I am knowing him since school.",
                    "I have know him since school.",
                ],

                "answer":
                    "I have known him since school.",

                "explanation":
                    "KNOW — глагол состояния.",
            },

            {
                "order": 28,

                "prompt":
                    "The road is wet. It ___.",

                "options": [
                    "has been raining",
                    "has rained three roads",
                    "has rain",
                    "has been rained",
                ],

                "answer":
                    "has been raining",

                "explanation":
                    "Мокрая дорога — видимый результат недавнего процесса.",
            },

            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "I have written four emails. / I have been writing for an hour.",
                    "I have been writing four emails. / I have written for an hour.",
                    "I have wrote four emails. / I have been wrote for an hour.",
                    "I am written four emails. / I have writing for an hour.",
                ],

                "answer":
                    "I have written four emails. / I have been writing for an hour.",

                "explanation":
                    "Количество → Present Perfect; длительность → Continuous.",
            },

            {
                "order": 30,

                "prompt":
                    "Choose the sentence emphasizing a finished result.",

                "options": [
                    "She has repaired the computer.",
                    "She has been repairing the computer.",
                    "She has been repair the computer.",
                    "She has repaired since morning.",
                ],

                "answer":
                    "She has repaired the computer.",

                "explanation":
                    "Present Perfect показывает готовый результат.",
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
                "✅ Interactive A1 Lesson 33 seeded"
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
