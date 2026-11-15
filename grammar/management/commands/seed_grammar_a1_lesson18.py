from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 18: Prepositions of time."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=18,

                defaults={
                    "title":
                        "Предлоги времени: "
                        "AT, ON, IN, FOR, SINCE, BY, DURING",

                    "slug":
                        "prepositions-of-time",

                    "theory_text":
                        "Prepositions of time.",

                    "estimated_minutes":
                        19,

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
        # 10 MICRO-RULES
        # ================================================

        sections = [

            {
                "order": 1,

                "title":
                    "AT — точное время",

                "body":
                    """AT используется с конкретной точкой во времени.

at five o'clock

at 7:30

at noon

at midnight

Примеры:

The lesson starts at nine.

I get up at seven.

We arrived at midnight.

Также запомни:

at night

at lunchtime

AT = точка во времени.""",
            },


            {
                "order": 2,

                "title":
                    "ON — дни и даты",

                "body":
                    """ON используется с днями недели и конкретными датами.

on Monday

on Friday

on 10 July

on 15 May

Также:

on Monday morning

on Friday evening

on my birthday

on New Year's Day

Запомни:

ON = конкретный день.""",
            },


            {
                "order": 3,

                "title":
                    "IN — месяцы, годы и длинные периоды",

                "body":
                    """IN используется с более длинными периодами.

Месяцы:

in January

in July

Годы:

in 2025

in 2026

Сезоны:

in summer

in winter

Части дня:

in the morning

in the afternoon

in the evening

Но:

at night.""",
            },


            {
                "order": 4,

                "title":
                    "AT, ON или IN?",

                "body":
                    """Самая важная схема:

AT → точное время

ON → день / дата

IN → месяц / год / сезон / период

Сравни:

at 8:00

on Monday

on 10 July

in July

in 2026

in winter

Можно представить:

AT = маленькая точка

ON = день

IN = большой период.""",
            },


            {
                "order": 5,

                "title":
                    "Когда предлог вообще не нужен",

                "body":
                    """Перед некоторыми словами предлог времени обычно не ставится.

today

tomorrow

yesterday

last week

next month

this year

every Monday

Правильно:

I am busy today.

We will meet tomorrow.

She called me yesterday.

I work every Monday.

Не:

on today

in last week

in this year

on every Monday.""",
            },


            {
                "order": 6,

                "title":
                    "IN или FOR?",

                "body":
                    """IN может означать «через какое-то время».

I will call you in ten minutes.

She will return in two weeks.

FOR показывает продолжительность.

I waited for ten minutes.

She stayed for two weeks.

Сравни:

in two weeks
→ через две недели

for two weeks
→ в течение двух недель.""",
            },


            {
                "order": 7,

                "title":
                    "FOR или SINCE?",

                "body":
                    """FOR показывает продолжительность:

for two hours

for five days

for three years

SINCE показывает начальную точку:

since Monday

since 2020

since morning

since five o'clock

Сравни:

for five years
→ в течение пяти лет

since 2021
→ с 2021 года

FOR = сколько времени

SINCE = с какого момента.""",
            },


            {
                "order": 8,

                "title":
                    "BY или UNTIL?",

                "body":
                    """BY означает:

не позднее определённого момента.

Finish the report by Friday.

Send it by five o'clock.

UNTIL означает:

действие продолжается до определённого момента.

I will stay here until Friday.

The shop is open until nine.

Сравни:

by Friday
→ крайний срок

until Friday
→ продолжать до пятницы.""",
            },


            {
                "order": 9,

                "title":
                    "DURING или FOR?",

                "body":
                    """DURING означает «во время события или периода».

during the lesson

during the meeting

during the film

during the night

После DURING обычно стоит существительное.

I slept during the film.

FOR показывает продолжительность:

I slept for two hours.

Не:

during two hours

А:

for two hours.

Также:

DURING + noun

WHILE + subject + verb

during the lesson

while I was studying.""",
            },


            {
                "order": 10,

                "title":
                    "FROM...TO, BEFORE и AFTER",

                "body":
                    """FROM ... TO означает «с ... до ...».

from Monday to Friday

from nine to five

from January to March

Пример:

I work from Monday to Friday.

BEFORE = до / перед:

before work

before dinner

before six

AFTER = после:

after work

after lunch

after the lesson

Главная памятка:

AT = точка

ON = день

IN = период / через

FOR = длительность

SINCE = начало

BY = дедлайн

UNTIL = до какого момента продолжается

DURING = во время события.""",
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
                    "The lesson starts ___ nine o'clock.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "for",
                ],

                "answer":
                    "at",

                "explanation":
                    "Точное время → AT.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "fill",

                "prompt":
                    "I usually go to bed ___ midnight.",

                "options": [],

                "answer":
                    "at",

                "explanation":
                    "MIDNIGHT — конкретная точка времени → AT.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "We have English ___ Monday.",

                "options": [
                    "at",
                    "on",
                    "in",
                    "since",
                ],

                "answer":
                    "on",

                "explanation":
                    "День недели → ON.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "The meeting is ___ 15 July.",

                "options": [
                    "in",
                    "at",
                    "on",
                    "for",
                ],

                "answer":
                    "on",

                "explanation":
                    "Конкретная дата → ON.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "My birthday is ___ July.",

                "options": [
                    "on",
                    "at",
                    "in",
                    "by",
                ],

                "answer":
                    "in",

                "explanation":
                    "Месяц → IN.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "I am usually tired ___ the evening.",

                "options": [
                    "at",
                    "on",
                    "in",
                    "for",
                ],

                "answer":
                    "in",

                "explanation":
                    "Часть дня → IN THE EVENING.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct set.",

                "options": [
                    "at 8:00 / on Monday / in August",
                    "in 8:00 / at Monday / on August",
                    "on 8:00 / in Monday / at August",
                    "at 8:00 / in Monday / on August",
                ],

                "answer":
                    "at 8:00 / on Monday / in August",

                "explanation":
                    "AT — время, ON — день, IN — месяц.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "They travel a lot ___ winter.",

                "options": [
                    "at",
                    "on",
                    "in",
                    "by",
                ],

                "answer":
                    "in",

                "explanation":
                    "Сезон → IN.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I am busy on today.",
                    "I am busy at today.",
                    "I am busy today.",
                    "I am busy in today.",
                ],

                "answer":
                    "I am busy today.",

                "explanation":
                    "Перед TODAY предлог не нужен.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "We have a lesson on every Monday.",
                    "We have a lesson in every Monday.",
                    "We have a lesson every Monday.",
                    "We have a lesson at every Monday.",
                ],

                "answer":
                    "We have a lesson every Monday.",

                "explanation":
                    "Перед EVERY MONDAY предлог не ставится.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "I will call you ___ ten minutes.",

                "options": [
                    "for",
                    "in",
                    "since",
                    "during",
                ],

                "answer":
                    "in",

                "explanation":
                    "Значение «через десять минут» → IN.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "I spoke to him ___ ten minutes.",

                "options": [
                    "in",
                    "since",
                    "for",
                    "by",
                ],

                "answer":
                    "for",

                "explanation":
                    "Длительность разговора → FOR.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "She has lived here ___ 2020.",

                "options": [
                    "for",
                    "during",
                    "since",
                    "at",
                ],

                "answer":
                    "since",

                "explanation":
                    "2020 — начальная точка → SINCE.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "She has lived here ___ five years.",

                "options": [
                    "since",
                    "during",
                    "for",
                    "by",
                ],

                "answer":
                    "for",

                "explanation":
                    "Five years — продолжительность → FOR.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Please send the document ___ Friday.",

                "options": [
                    "until",
                    "by",
                    "during",
                    "since",
                ],

                "answer":
                    "by",

                "explanation":
                    "Не позднее пятницы → BY.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "The shop is open ___ nine.",

                "options": [
                    "by",
                    "until",
                    "since",
                    "during",
                ],

                "answer":
                    "until",

                "explanation":
                    "Магазин продолжает работать до девяти → UNTIL.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Do not use your phone ___ the lesson.",

                "options": [
                    "for",
                    "during",
                    "since",
                    "by",
                ],

                "answer":
                    "during",

                "explanation":
                    "Во время события → DURING.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I slept during two hours.",
                    "I slept for two hours.",
                    "I slept since two hours.",
                    "I slept by two hours.",
                ],

                "answer":
                    "I slept for two hours.",

                "explanation":
                    "Two hours — продолжительность → FOR.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "build",

                "prompt":
                    "Собери правильное выражение.",

                "options": [
                    "from",
                    "Monday",
                    "to",
                    "Friday",
                ],

                "answer":
                    "from Monday to Friday",

                "explanation":
                    "FROM ... TO = с ... до ...",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Call me ___ the lesson.",

                "options": [
                    "after",
                    "during of",
                    "for",
                    "since",
                ],

                "answer":
                    "after",

                "explanation":
                    "AFTER THE LESSON = после урока.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "The train leaves ___ 6:45.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "for",
                ],

                "answer":
                    "at",

                "explanation":
                    "Точное время → AT.",
            },


            {
                "order": 22,

                "prompt":
                    "We are meeting ___ Friday evening.",

                "options": [
                    "in",
                    "on",
                    "at",
                    "for",
                ],

                "answer":
                    "on",

                "explanation":
                    "Конкретный день + часть дня → ON.",
            },


            {
                "order": 23,

                "prompt":
                    "She was born ___ 2001.",

                "options": [
                    "at",
                    "on",
                    "in",
                    "since",
                ],

                "answer":
                    "in",

                "explanation":
                    "Год → IN.",
            },


            {
                "order": 24,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I will see you in next week.",
                    "I will see you on next week.",
                    "I will see you next week.",
                    "I will see you at next week.",
                ],

                "answer":
                    "I will see you next week.",

                "explanation":
                    "Перед NEXT WEEK предлог не нужен.",
            },


            {
                "order": 25,

                "prompt":
                    "The doctor will see you ___ twenty minutes.",

                "options": [
                    "for",
                    "in",
                    "since",
                    "during",
                ],

                "answer":
                    "in",

                "explanation":
                    "Через двадцать минут → IN.",
            },


            {
                "order": 26,

                "prompt":
                    "We waited ___ an hour.",

                "options": [
                    "in",
                    "for",
                    "since",
                    "by",
                ],

                "answer":
                    "for",

                "explanation":
                    "An hour — продолжительность → FOR.",
            },


            {
                "order": 27,

                "prompt":
                    "He has worked here ___ Monday.",

                "options": [
                    "for",
                    "since",
                    "during",
                    "by",
                ],

                "answer":
                    "since",

                "explanation":
                    "Monday — начальная точка → SINCE.",
            },


            {
                "order": 28,

                "prompt":
                    "Finish this task ___ 5 p.m.",

                "options": [
                    "until",
                    "by",
                    "for",
                    "during",
                ],

                "answer":
                    "by",

                "explanation":
                    "5 p.m. — крайний срок → BY.",
            },


            {
                "order": 29,

                "prompt":
                    "It started raining ___ the match.",

                "options": [
                    "during",
                    "for",
                    "since",
                    "by",
                ],

                "answer":
                    "during",

                "explanation":
                    "MATCH — событие → DURING.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct set.",

                "options": [
                    "at night / on Monday / in July / for two hours",
                    "in night / at Monday / on July / during two hours",
                    "on night / in Monday / at July / since two hours",
                    "at night / in Monday / on July / by two hours",
                ],

                "answer":
                    "at night / on Monday / in July / for two hours",

                "explanation":
                    "AT NIGHT, ON Monday, IN July и FOR duration — правильные сочетания.",
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
                "✅ Interactive A1 Lesson 18 seeded"
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
