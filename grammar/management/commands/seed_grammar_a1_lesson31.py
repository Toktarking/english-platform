from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 31: Present Perfect vs Past Simple."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=31,

                defaults={
                    "title":
                        "Present Perfect и Past Simple",

                    "slug":
                        "present-perfect-vs-past-simple",

                    "theory_text":
                        "Present Perfect vs Past Simple.",

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
                    "Главное различие",

                "body":
                    """Оба времени говорят о прошлом.

Но Present Perfect связывает прошлое
с настоящим:

I have lost my keys.

→ сейчас ключей нет.

Past Simple говорит о завершённом
событии в прошлом:

I lost my keys yesterday.

Главный вопрос:

важен результат сейчас
или завершённое прошлое?""",
            },


            {
                "order": 2,
                "title":
                    "Есть точное время? Past Simple",

                "body":
                    """Если указано завершённое время прошлого,
обычно нужен Past Simple.

yesterday
last week
two days ago
in 2020
at six yesterday

I saw him yesterday.

She arrived last week.

They moved here in 2020.

Не говорим:

I have seen him yesterday.""",
            },


            {
                "order": 3,
                "title":
                    "Нет точного времени? Present Perfect",

                "body":
                    """Если точное время не называется,
а важен сам факт или результат:

Present Perfect.

I have finished the report.

She has seen this film.

We have visited London.

Нас интересует:

что произошло,

а не когда именно.""",
            },


            {
                "order": 4,
                "title":
                    "Результат сейчас",

                "body":
                    """Present Perfect показывает,
что прошлое действие влияет на настоящее.

She has broken her phone.

→ телефон сейчас сломан.

I have lost my wallet.

→ кошелька сейчас нет.

Past Simple:

She broke her phone last year.

Это просто событие прошлого.""",
            },


            {
                "order": 5,
                "title":
                    "Жизненный опыт",

                "body":
                    """Когда спрашиваем об опыте жизни:

Present Perfect.

Have you ever been to Turkey?

I have never tried sushi.

She has visited Italy twice.

Точное время не называется.

Если появляется конкретная дата:

I went to Turkey in 2024.

→ Past Simple.""",
            },


            {
                "order": 6,
                "title":
                    "Сначала опыт, потом детали",

                "body":
                    """Очень частая схема:

Have you ever been to London?

→ Present Perfect: опыт.

Yes, I have.

When did you go there?

→ Past Simple: конкретная деталь.

I went there in 2023.

Запомни:

опыт → Present Perfect

детали → Past Simple.""",
            },


            {
                "order": 7,
                "title":
                    "TODAY, THIS WEEK, THIS YEAR",

                "body":
                    """Если период ещё продолжается,
часто используется Present Perfect.

I have had three meetings today.

She has called twice this week.

Но завершённый период:

I had three meetings yesterday.

She called twice last week.

Главное:

период ещё идёт
или уже закончился?""",
            },


            {
                "order": 8,
                "title":
                    "FOR и SINCE: продолжается или закончилось?",

                "body":
                    """Если ситуация продолжается сейчас:

Present Perfect.

I have lived here for five years.

She has worked here since 2021.

Если ситуация закончилась:

Past Simple.

I lived there for five years,
but now I live elsewhere.

She worked there from 2018 to 2022.""",
            },


            {
                "order": 9,
                "title":
                    "HOW LONG",

                "body":
                    """Если ситуация продолжается:

How long have you lived here?

→ ты всё ещё здесь живёшь.

Если ситуация завершена:

How long did you live in London?

→ ты уже там не живёшь.

То же правило:

продолжается → Present Perfect

закончилось → Past Simple.""",
            },


            {
                "order": 10,
                "title":
                    "Новость и подробности",

                "body":
                    """Новость часто сообщается
в Present Perfect:

I have lost my phone.

После этого детали идут в Past Simple:

Where did you lose it?

I lost it on the bus.

Ещё пример:

She has got a new job.

When did she start?

She started on Monday.""",
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

            # 1

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ my keys. I can't open the door.",

                "options": [
                    "have lost",
                    "lost yesterday",
                    "have lose",
                    "did lost",
                ],

                "answer":
                    "have lost",

                "explanation":
                    "Важен результат сейчас: ключей нет.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ my keys yesterday.",

                "options": [
                    "lost",
                    "have lost",
                    "have lose",
                    "lose",
                ],

                "answer":
                    "lost",

                "explanation":
                    "YESTERDAY → завершённое прошлое.",
            },


            # 2

            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "She ___ to Almaty last week.",

                "options": [
                    "went",
                    "has gone",
                    "has been",
                    "go",
                ],

                "answer":
                    "went",

                "explanation":
                    "LAST WEEK требует Past Simple.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "fill",

                "prompt":
                    "I ___ him two days ago. (see)",

                "options": [],

                "answer":
                    "saw",

                "explanation":
                    "TWO DAYS AGO → Past Simple → SAW.",
            },


            # 3

            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "We ___ this film before.",

                "options": [
                    "have seen",
                    "saw yesterday",
                    "have saw",
                    "see",
                ],

                "answer":
                    "have seen",

                "explanation":
                    "BEFORE без точного времени → Present Perfect.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "She ___ the report. It's ready now.",

                "options": [
                    "has finished",
                    "finished yesterday at five",
                    "has finish",
                    "did finished",
                ],

                "answer":
                    "has finished",

                "explanation":
                    "Важен готовый результат сейчас.",
            },


            # 4

            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "My phone doesn't work. I ___ it.",

                "options": [
                    "have broken",
                    "broke it last year",
                    "have broke",
                    "break",
                ],

                "answer":
                    "have broken",

                "explanation":
                    "Телефон сейчас сломан → Present Perfect.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She ___ her phone in 2023.",

                "options": [
                    "broke",
                    "has broken",
                    "has broke",
                    "breaks",
                ],

                "answer":
                    "broke",

                "explanation":
                    "IN 2023 → конкретное завершённое прошлое.",
            },


            # 5

            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "___ you ever been to Dubai?",

                "options": [
                    "Have",
                    "Did",
                    "Has",
                    "Were",
                ],

                "answer":
                    "Have",

                "explanation":
                    "Вопрос о жизненном опыте → HAVE YOU EVER...?",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "I ___ to Dubai in 2024.",

                "options": [
                    "went",
                    "have been",
                    "have gone",
                    "go",
                ],

                "answer":
                    "went",

                "explanation":
                    "IN 2024 → Past Simple.",
            },


            # 6

            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Have you ever tried Korean food? — Yes. When ___ you try it?",

                "options": [
                    "did",
                    "have",
                    "has",
                    "were",
                ],

                "answer":
                    "did",

                "explanation":
                    "После вопроса об опыте детали спрашиваем в Past Simple.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "build",

                "prompt":
                    "Собери вопрос о конкретной поездке.",

                "options": [
                    "When",
                    "did",
                    "you",
                    "go",
                    "there",
                ],

                "answer":
                    "When did you go there",

                "explanation":
                    "Конкретная деталь прошлого → DID + base verb.",
            },


            # 7

            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I ___ three coffees today.",

                "options": [
                    "have had",
                    "had yesterday",
                    "have have",
                    "did had",
                ],

                "answer":
                    "have had",

                "explanation":
                    "TODAY ещё продолжается → Present Perfect.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I ___ three coffees yesterday.",

                "options": [
                    "had",
                    "have had",
                    "have",
                    "has had",
                ],

                "answer":
                    "had",

                "explanation":
                    "YESTERDAY завершён → Past Simple.",
            },


            # 8

            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "We ___ here for ten years and still live here.",

                "options": [
                    "have lived",
                    "lived",
                    "did live",
                    "have living",
                ],

                "answer":
                    "have lived",

                "explanation":
                    "Ситуация продолжается сейчас.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "We ___ there for ten years, but now we live elsewhere.",

                "options": [
                    "lived",
                    "have lived",
                    "have live",
                    "living",
                ],

                "answer":
                    "lived",

                "explanation":
                    "Ситуация завершилась → Past Simple.",
            },


            # 9

            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "How long ___ you lived here?",

                "options": [
                    "have",
                    "did",
                    "has",
                    "were",
                ],

                "answer":
                    "have",

                "explanation":
                    "Человек всё ещё здесь живёт → Present Perfect.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "How long ___ you live in London before moving away?",

                "options": [
                    "did",
                    "have",
                    "has",
                    "were",
                ],

                "answer":
                    "did",

                "explanation":
                    "Период жизни в Лондоне закончился.",
            },


            # 10

            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "I have lost my wallet. — Where ___ you lose it?",

                "options": [
                    "did",
                    "have",
                    "has",
                    "do",
                ],

                "answer":
                    "did",

                "explanation":
                    "Новость → Present Perfect; детали → Past Simple.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "build",

                "prompt":
                    "Собери правильную последовательность.",

                "options": [
                    "I",
                    "have",
                    "lost",
                    "my",
                    "phone",
                ],

                "answer":
                    "I have lost my phone",

                "explanation":
                    "Новость о текущей проблеме → Present Perfect.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "I ___ this book last month.",

                "options": [
                    "read",
                    "have read",
                    "have reading",
                    "has read",
                ],

                "answer":
                    "read",

                "explanation":
                    "LAST MONTH → Past Simple.",
            },

            {
                "order": 22,

                "prompt":
                    "I ___ this book three times.",

                "options": [
                    "have read",
                    "read last week",
                    "have reading",
                    "did read yesterday",
                ],

                "answer":
                    "have read",

                "explanation":
                    "Опыт без конкретного времени → Present Perfect.",
            },

            {
                "order": 23,

                "prompt":
                    "Sara ___ her homework, so she can relax now.",

                "options": [
                    "has finished",
                    "finished yesterday",
                    "has finish",
                    "did finished",
                ],

                "answer":
                    "has finished",

                "explanation":
                    "Важен результат сейчас.",
            },

            {
                "order": 24,

                "prompt":
                    "Sara ___ her homework at 8 p.m.",

                "options": [
                    "finished",
                    "has finished",
                    "has finish",
                    "finish",
                ],

                "answer":
                    "finished",

                "explanation":
                    "AT 8 P.M. → конкретное прошлое.",
            },

            {
                "order": 25,

                "prompt":
                    "Have you ever ___ a horse?",

                "options": [
                    "ridden",
                    "rode",
                    "ride",
                    "riding",
                ],

                "answer":
                    "ridden",

                "explanation":
                    "Present Perfect требует V3: RIDE → RODE → RIDDEN.",
            },

            {
                "order": 26,

                "prompt":
                    "When ___ you ride a horse for the first time?",

                "options": [
                    "did",
                    "have",
                    "has",
                    "are",
                ],

                "answer":
                    "did",

                "explanation":
                    "Конкретная деталь прошлого → Past Simple.",
            },

            {
                "order": 27,

                "prompt":
                    "He ___ at this company since 2021.",

                "options": [
                    "has worked",
                    "worked",
                    "did work",
                    "has working",
                ],

                "answer":
                    "has worked",

                "explanation":
                    "SINCE + продолжающаяся ситуация → Present Perfect.",
            },

            {
                "order": 28,

                "prompt":
                    "He ___ there from 2018 to 2020.",

                "options": [
                    "worked",
                    "has worked",
                    "has working",
                    "works",
                ],

                "answer":
                    "worked",

                "explanation":
                    "2018–2020 — завершённый период.",
            },

            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "I have seen her today. / I saw her yesterday.",
                    "I saw her today. / I have seen her yesterday.",
                    "I have saw her today. / I seen her yesterday.",
                    "I seen her today. / I have saw her yesterday.",
                ],

                "answer":
                    "I have seen her today. / I saw her yesterday.",

                "explanation":
                    "TODAY может быть незавершённым; YESTERDAY завершён.",
            },

            {
                "order": 30,

                "prompt":
                    "Choose the correct news-and-detail sequence.",

                "options": [
                    "She has got a new job. When did she start?",
                    "She got a new job. When has she started yesterday?",
                    "She has got a new job yesterday. When did she start?",
                    "She have got a new job. When did she started?",
                ],

                "answer":
                    "She has got a new job. When did she start?",

                "explanation":
                    "Новость → Present Perfect; конкретная деталь → Past Simple.",
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
                "✅ Interactive A1 Lesson 31 seeded"
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
