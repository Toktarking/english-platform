from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 12: Present Simple negatives."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=12,

                defaults={
                    "title":
                        "Отрицания в Present Simple",

                    "slug":
                        "present-simple-negatives",

                    "theory_text":
                        "Present Simple negatives: "
                        "don't and doesn't.",

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


        # ================================================
        # 9 MICRO-RULES
        # ================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Как сказать «не» в Present Simple?",

                "body":
                    """С обычными глаголами нельзя просто добавить NOT.

Утверждение:

I work.

Отрицание:

I don't work.

Утверждение:

She works.

Отрицание:

She doesn't work.

Используем:

DO NOT → DON'T

DOES NOT → DOESN'T

Не:

I not work.

А:

I don't work.""",
            },


            {
                "order": 2,

                "title":
                    "I, YOU, WE, THEY → DON'T",

                "body":
                    """С I, YOU, WE, THEY используется DON'T.

I don't work on Sundays.

You don't understand me.

We don't live in Astana.

They don't study English.

То же правило работает с множественным числом:

The children don't play outside.

My parents don't live here.

Главная схема:

I / you / we / they
→ don't + verb.""",
            },


            {
                "order": 3,

                "title":
                    "HE, SHE, IT → DOESN'T",

                "body":
                    """С HE, SHE, IT используется DOESN'T.

He doesn't work here.

She doesn't speak French.

It doesn't work.

То же правило с одним человеком или предметом:

Marat doesn't live in Almaty.

My sister doesn't drive.

The phone doesn't work.

Главная схема:

he / she / it
→ doesn't + verb.""",
            },


            {
                "order": 4,

                "title":
                    "После DOESN'T глагол теряет -S",

                "body":
                    """Это главное правило урока.

Утверждение:

She works.

Отрицание:

She doesn't work.

Не:

She doesn't works.

Почему?

Потому что показатель третьего лица уже находится в DOES.

То же самое:

He lives.
→ He doesn't live.

She watches TV.
→ She doesn't watch TV.

He studies English.
→ He doesn't study English.

После DON'T и DOESN'T используется базовая форма глагола.""",
            },


            {
                "order": 5,

                "title":
                    "HAS → DOESN'T HAVE",

                "body":
                    """HAVE тоже возвращается в базовую форму.

Утверждение:

She has a car.

Отрицание:

She doesn't have a car.

Не:

She doesn't has a car.

Ещё:

He has a job.

He doesn't have a job.

My brother has two children.

My brother doesn't have two children.

Запомни:

HAS → DOESN'T HAVE.""",
            },


            {
                "order": 6,

                "title":
                    "DON'T / DOESN'T или ISN'T / AREN'T?",

                "body":
                    """С обычным действием используем DON'T / DOESN'T:

I don't work here.

She doesn't live here.

They don't study English.

Но с TO BE используется NOT:

I am not tired.

She isn't at home.

They aren't ready.

Не:

She doesn't tired.

А:

She isn't tired.

Сравни:

She isn't busy.
BUSY — состояние.

She doesn't work today.
WORK — действие.""",
            },


            {
                "order": 7,

                "title":
                    "NEVER уже означает «никогда»",

                "body":
                    """NEVER уже содержит отрицательное значение.

Поэтому DON'T / DOESN'T вместе с NEVER обычно не нужны.

Правильно:

I never smoke.

She never drinks coffee.

They never arrive late.

Не:

I don't never smoke.

She doesn't never drink coffee.

Сравни:

I don't smoke.
Я не курю.

I never smoke.
Я никогда не курю.""",
            },


            {
                "order": 8,

                "title":
                    "Наречия частотности в отрицании",

                "body":
                    """С DON'T / DOESN'T наречие частотности обычно ставится перед основным глаголом.

I don't usually work on Sundays.

She doesn't often watch TV.

They don't always agree.

С NEVER другая схема:

I never eat fast food.

He never comes late.

She never drives at night.

То есть:

don't usually work

doesn't often watch

never comes.""",
            },


            {
                "order": 9,

                "title":
                    "Как быстро построить отрицание",

                "body":
                    """Шаг 1.

Найди подлежащее.

My brother works here.

My brother = HE.

Шаг 2.

Выбери DOESN'T:

My brother doesn't...

Шаг 3.

Верни глагол в базовую форму:

works → work

Итог:

My brother doesn't work here.

Другой пример:

My parents live in Astana.

My parents = THEY.

Используем DON'T:

My parents don't live in Astana.

Главная схема:

I / you / we / they
→ DON'T + verb

he / she / it
→ DOESN'T + verb.""",
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
                    "I ___ work on Sundays.",

                "options": [
                    "doesn't",
                    "don't",
                    "am not",
                    "not",
                ],

                "answer":
                    "don't",

                "explanation":
                    "С I используется DON'T.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "She ___ work on Sundays.",

                "options": [
                    "don't",
                    "isn't",
                    "doesn't",
                    "not",
                ],

                "answer":
                    "doesn't",

                "explanation":
                    "С SHE используется DOESN'T.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "We ___ understand this rule.",

                "options": [],

                "answer":
                    "don't",

                "explanation":
                    "WE → DON'T.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "My parents ___ live in Almaty.",

                "options": [
                    "doesn't",
                    "don't",
                    "isn't",
                    "aren't live",
                ],

                "answer":
                    "don't",

                "explanation":
                    "My parents = THEY → DON'T.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "My sister ___ drive.",

                "options": [],

                "answer":
                    "doesn't",

                "explanation":
                    "My sister = SHE → DOESN'T.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "The phone ___ work properly.",

                "options": [
                    "don't",
                    "doesn't",
                    "isn't",
                    "aren't",
                ],

                "answer":
                    "doesn't",

                "explanation":
                    "The phone = IT → DOESN'T.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "He doesn't ___ English.",

                "options": [
                    "speaks",
                    "speak",
                    "speaking",
                    "is speak",
                ],

                "answer":
                    "speak",

                "explanation":
                    "После DOESN'T используется базовая форма SPEAK.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She doesn't ___ television.",

                "options": [
                    "watches",
                    "watch",
                    "watching",
                    "is watch",
                ],

                "answer":
                    "watch",

                "explanation":
                    "WATCHES → DOESN'T WATCH.",
            },


            {
                "order": 9,
                "section": 4,
                "type": "choice",

                "prompt":
                    "My brother doesn't ___ English.",

                "options": [
                    "studies",
                    "study",
                    "studys",
                    "studying",
                ],

                "answer":
                    "study",

                "explanation":
                    "STUDIES → DOESN'T STUDY.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "She doesn't ___ a car.",

                "options": [
                    "has",
                    "have",
                    "haves",
                    "having",
                ],

                "answer":
                    "have",

                "explanation":
                    "После DOESN'T используется HAVE, а не HAS.",
            },


            {
                "order": 11,
                "section": 5,
                "type": "build",

                "prompt":
                    "Собери правильное отрицание.",

                "options": [
                    "He",
                    "doesn't",
                    "have",
                    "a",
                    "car",
                ],

                "answer":
                    "He doesn't have a car",

                "explanation":
                    "HAS в отрицании превращается в DOESN'T HAVE.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She doesn't tired.",
                    "She isn't tired.",
                    "She don't tired.",
                    "She doesn't be tired.",
                ],

                "answer":
                    "She isn't tired.",

                "explanation":
                    "TIRED — состояние с TO BE.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "They aren't study English.",
                    "They don't study English.",
                    "They doesn't study English.",
                    "They not study English.",
                ],

                "answer":
                    "They don't study English.",

                "explanation":
                    "STUDY — обычный смысловой глагол → DON'T.",
            },


            {
                "order": 14,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "She isn't busy. / She doesn't work today.",
                    "She doesn't busy. / She isn't work today.",
                    "She isn't busy. / She isn't work today.",
                    "She doesn't busy. / She doesn't works today.",
                ],

                "answer":
                    "She isn't busy. / She doesn't work today.",

                "explanation":
                    "BUSY требует TO BE, WORK — обычный глагол.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "choice",

                "prompt":
                    "He ___ drinks coffee.",

                "options": [
                    "doesn't never",
                    "never",
                    "don't never",
                    "not never",
                ],

                "answer":
                    "never",

                "explanation":
                    "NEVER уже имеет отрицательное значение.",
            },


            {
                "order": 16,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I don't never smoke.",
                    "I never smoke.",
                    "I never don't smoke.",
                    "I doesn't never smoke.",
                ],

                "answer":
                    "I never smoke.",

                "explanation":
                    "Дополнительное DON'T с NEVER не требуется.",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I usually don't work on Sundays.",
                    "I don't usually work on Sundays.",
                    "I don't work usually on Sundays.",
                    "I doesn't usually work on Sundays.",
                ],

                "answer":
                    "I don't usually work on Sundays.",

                "explanation":
                    "Обычная схема: DON'T + USUALLY + VERB.",
            },


            {
                "order": 18,
                "section": 8,
                "type": "choice",

                "prompt":
                    "She ___ watches TV in the morning.",

                "options": [
                    "doesn't often",
                    "doesn't never",
                    "don't often",
                    "isn't often",
                ],

                "answer":
                    "doesn't often",

                "explanation":
                    "SHE → DOESN'T; OFTEN стоит перед основным глаголом.",
            },


            {
                "order": 19,
                "section": 9,
                "type": "choice",

                "prompt":
                    "My brother works here. Choose the negative form.",

                "options": [
                    "My brother doesn't works here.",
                    "My brother don't work here.",
                    "My brother doesn't work here.",
                    "My brother isn't work here.",
                ],

                "answer":
                    "My brother doesn't work here.",

                "explanation":
                    "My brother = HE → DOESN'T + WORK.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "My parents live in Astana. Choose the negative form.",

                "options": [
                    "My parents doesn't live in Astana.",
                    "My parents don't live in Astana.",
                    "My parents aren't live in Astana.",
                    "My parents don't lives in Astana.",
                ],

                "answer":
                    "My parents don't live in Astana.",

                "explanation":
                    "My parents = THEY → DON'T + LIVE.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "We ___ watch TV in the morning.",

                "options": [
                    "doesn't",
                    "don't",
                    "aren't",
                    "not",
                ],

                "answer":
                    "don't",

                "explanation":
                    "WE → DON'T.",
            },


            {
                "order": 22,

                "prompt":
                    "My father ___ drink coffee.",

                "options": [
                    "don't",
                    "doesn't",
                    "isn't",
                    "aren't",
                ],

                "answer":
                    "doesn't",

                "explanation":
                    "My father = HE → DOESN'T.",
            },


            {
                "order": 23,

                "prompt":
                    "Anna doesn't ___ in this city.",

                "options": [
                    "lives",
                    "live",
                    "living",
                    "is live",
                ],

                "answer":
                    "live",

                "explanation":
                    "После DOESN'T используется базовая форма LIVE.",
            },


            {
                "order": 24,

                "prompt":
                    "The shop doesn't ___ on Sundays.",

                "options": [
                    "opens",
                    "open",
                    "opening",
                    "is open",
                ],

                "answer":
                    "open",

                "explanation":
                    "После DOESN'T окончание -s исчезает.",
            },


            {
                "order": 25,

                "prompt":
                    "He doesn't ___ a new phone.",

                "options": [
                    "has",
                    "have",
                    "haves",
                    "having",
                ],

                "answer":
                    "have",

                "explanation":
                    "HAS → DOESN'T HAVE.",
            },


            {
                "order": 26,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "She doesn't hungry.",
                    "She isn't hungry.",
                    "She don't hungry.",
                    "She doesn't be hungry.",
                ],

                "answer":
                    "She isn't hungry.",

                "explanation":
                    "HUNGRY — состояние, поэтому используется TO BE.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "They don't likes this restaurant.",
                    "They doesn't like this restaurant.",
                    "They don't like this restaurant.",
                    "They aren't like this restaurant.",
                ],

                "answer":
                    "They don't like this restaurant.",

                "explanation":
                    "THEY → DON'T + базовая форма LIKE.",
            },


            {
                "order": 28,

                "prompt":
                    "Choose the correct sentence with NEVER.",

                "options": [
                    "She doesn't never arrive late.",
                    "She never arrives late.",
                    "She never arrive late.",
                    "She don't never arrives late.",
                ],

                "answer":
                    "She never arrives late.",

                "explanation":
                    "NEVER используется без DOESN'T, "
                    "а SHE требует ARRIVES.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "He doesn't usually drive to work.",
                    "He usually doesn't drives to work.",
                    "He doesn't usually drives to work.",
                    "He isn't usually drive to work.",
                ],

                "answer":
                    "He doesn't usually drive to work.",

                "explanation":
                    "Правильная схема: DOESN'T + USUALLY + DRIVE.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct option.",

                "options": [
                    "She isn't tired, but she doesn't work today.",
                    "She doesn't tired, but she isn't work today.",
                    "She isn't tired, but she doesn't works today.",
                    "She don't tired, but she doesn't work today.",
                ],

                "answer":
                    "She isn't tired, but she doesn't work today.",

                "explanation":
                    "TIRED требует ISN'T; "
                    "WORK — DOESN'T + базовая форма.",
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
                "✅ Interactive A1 Lesson 12 seeded"
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
