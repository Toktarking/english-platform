from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 18: "
        "Prepositions of time."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=18,
            defaults={
                "title": (
                    "Предлоги времени: "
                    "AT, ON, IN, FOR, SINCE, BY, DURING"
                ),
                "slug": "prepositions-of-time",
                "theory_text": "Prepositions of time.",
                "estimated_minutes": 35,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое предлоги времени",
                "body": """Предлоги времени показывают, когда происходит действие.

Основные предлоги урока:

at;
on;
in;
for;
since;
by;
during.

Например:

at five o'clock;

on Monday;

in July;

for two hours;

since Monday;

by Friday;

during the lesson.

Нельзя использовать один предлог in во всех случаях.""",
            },

            {
                "order": 2,
                "title": "AT — точное время",
                "body": """AT используется с точным временем.

Примеры:

at five o'clock;

at 7:30;

at noon;

at midnight.

Предложения:

The lesson starts at nine.

I get up at seven.

We arrived at midnight.

Также:

at night;

at lunchtime;

at sunrise;

at sunset.

Запомните:

AT = точка во времени.""",
            },

            {
                "order": 3,
                "title": "ON — дни и даты",
                "body": """ON используется с днями недели и датами.

Примеры:

on Monday;

on Friday;

on 10 July;

on 15 May 2026.

Также ON используется с конкретным днём и частью дня:

on Monday morning;

on Friday evening;

on Sunday afternoon.

И с особыми днями:

on my birthday;

on New Year's Day;

on Christmas Day.""",
            },

            {
                "order": 4,
                "title": "IN — месяцы, годы и периоды",
                "body": """IN используется с более длинными периодами.

Месяцы:

in January;

in July.

Годы:

in 2020;

in 2026.

Века:

in the twentieth century.

Времена года:

in summer;

in winter.

Части дня:

in the morning;

in the afternoon;

in the evening.

Но:

at night.""",
            },

            {
                "order": 5,
                "title": "AT, ON или IN",
                "body": """Простая схема:

AT → точное время

ON → день или дата

IN → месяц, год, сезон, длинный период

Сравните:

at 7:00;

on Monday;

on 10 July;

in July;

in 2026;

in winter.

Можно запомнить движение от малого к большому:

AT = точка;

ON = день;

IN = большой период.""",
            },

            {
                "order": 6,
                "title": "Когда предлог не нужен",
                "body": """Перед некоторыми словами предлог времени обычно не ставится.

TODAY:

I am busy today.

TOMORROW:

We will meet tomorrow.

YESTERDAY:

She called me yesterday.

Также без предлога:

last week;

next month;

this year;

every Monday.

Неправильно:

on today;

in last week;

in this year;

on every Monday.""",
            },

            {
                "order": 7,
                "title": "IN в значении «через»",
                "body": """IN может означать, что действие произойдёт через определённое время.

Примеры:

in two days;

in three weeks;

in an hour;

in five minutes.

Предложения:

I will call you in an hour.

She will return in two weeks.

The lesson will start in ten minutes.

Сравните:

I will return in two weeks.
— Я вернусь через две недели.

I will stay for two weeks.
— Я останусь на две недели.""",
            },

            {
                "order": 8,
                "title": "FOR — продолжительность",
                "body": """FOR показывает продолжительность.

Он отвечает на вопрос:

Как долго?

Примеры:

for two hours;

for three days;

for a week;

for many years.

Предложения:

I studied for two hours.

She stayed in London for a week.

He waited for thirty minutes.

Главная идея:

FOR = сколько времени длилось действие.""",
            },

            {
                "order": 9,
                "title": "SINCE — начальная точка",
                "body": """SINCE показывает начальную точку действия.

Он отвечает на вопрос:

С какого момента?

Примеры:

since Monday;

since 2020;

since childhood;

since morning;

since five o'clock.

Сравните:

for five years
— пять лет;

since 2021
— с 2021 года.

FOR = продолжительность.

SINCE = начальная точка.""",
            },

            {
                "order": 10,
                "title": "BY и UNTIL",
                "body": """BY означает:

к определённому времени;

не позднее определённого момента.

Примеры:

by Friday;

by five o'clock;

by tomorrow.

Please finish the report by Friday.

UNTIL означает, что действие продолжается до момента.

I will stay here until Friday.

The shop is open until nine.

Сравните:

Send the document by Friday.
— отправить не позднее пятницы.

I will work until Friday.
— работать до пятницы.""",
            },

            {
                "order": 11,
                "title": "DURING",
                "body": """DURING означает:

во время;

в течение какого-то события или периода.

После during обычно стоит существительное.

Примеры:

during the lesson;

during the meeting;

during the holiday;

during the night;

during the summer.

Предложения:

Do not talk during the lesson.

She called me during the meeting.

It rained during the night.""",
            },

            {
                "order": 12,
                "title": "DURING, FOR и WHILE",
                "body": """DURING показывает, во время какого события произошло действие.

I slept during the film.

FOR показывает продолжительность.

I slept for two hours.

Неправильно:

I slept during two hours.

Правильно:

I slept for two hours.

Также:

DURING + существительное

during the lesson

WHILE + подлежащее + глагол

while I was studying

Сравните:

She called me during the lesson.

She called me while I was studying.""",
            },

            {
                "order": 13,
                "title": "FROM ... TO, BEFORE, AFTER",
                "body": """FROM ... TO означает:

с ... до ...

Примеры:

from Monday to Friday;

from nine to five;

from January to March.

I work from Monday to Friday.

BEFORE означает «до / перед»:

before work;

before dinner;

before six.

AFTER означает «после»:

after work;

after lunch;

after the lesson.

Call me after six.""",
            },

            {
                "order": 14,
                "title": "Как быстро выбрать предлог",
                "body": """Сначала определите значение.

Точное время?

→ AT

at seven

День или дата?

→ ON

on Monday

Месяц, год или сезон?

→ IN

in July

Продолжительность?

→ FOR

for two hours

Начальная точка?

→ SINCE

since 2020

Крайний срок?

→ BY

by Friday

Во время события?

→ DURING

during the lesson

Главная схема:

AT = точка

ON = день

IN = период

FOR = длительность

SINCE = начало

BY = дедлайн

DURING = внутри события""",
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
                "prompt": "The lesson starts ___ nine o'clock.",
                "options": ["in", "on", "at", "for"],
                "answer": "at",
                "explanation": "Точное время → at.",
            },

            {
                "order": 2,
                "prompt": "We have English ___ Monday.",
                "options": ["at", "on", "in", "since"],
                "answer": "on",
                "explanation": "День недели → on.",
            },

            {
                "order": 3,
                "prompt": "My birthday is ___ July.",
                "options": ["on", "at", "in", "by"],
                "answer": "in",
                "explanation": "Месяц → in.",
            },

            {
                "order": 4,
                "prompt": "She graduated ___ 2022.",
                "options": ["at", "on", "in", "for"],
                "answer": "in",
                "explanation": "Год → in.",
            },

            {
                "order": 5,
                "prompt": "I do not work ___ night.",
                "options": ["in", "at", "on", "during of"],
                "answer": "at",
                "explanation": "Устойчивое выражение: at night.",
            },

            {
                "order": 6,
                "prompt": "We have a meeting ___ Monday morning.",
                "options": ["in", "on", "at", "for"],
                "answer": "on",
                "explanation": "Конкретный день + часть дня → on.",
            },

            {
                "order": 7,
                "prompt": "She will return ___ two weeks.",
                "options": ["for", "since", "in", "during"],
                "answer": "in",
                "explanation": "Здесь значение «через две недели» → in.",
            },

            {
                "order": 8,
                "prompt": "She will stay here ___ two weeks.",
                "options": ["in", "for", "since", "by"],
                "answer": "for",
                "explanation": "Продолжительность → for.",
            },

            {
                "order": 9,
                "prompt": "I have lived here ___ 2020.",
                "options": ["for", "during", "since", "at"],
                "answer": "since",
                "explanation": "2020 — начальная точка, поэтому since.",
            },

            {
                "order": 10,
                "prompt": "Please finish the report ___ Friday.",
                "options": ["during", "for", "by", "since"],
                "answer": "by",
                "explanation": "Не позднее пятницы → by.",
            },

            {
                "order": 11,
                "prompt": "Do not use your phone ___ the lesson.",
                "options": ["for", "during", "since", "by"],
                "answer": "during",
                "explanation": "Во время события → during.",
            },

            {
                "order": 12,
                "prompt": "I studied ___ three hours.",
                "options": ["during", "since", "for", "by"],
                "answer": "for",
                "explanation": "Three hours — продолжительность.",
            },

            {
                "order": 13,
                "prompt": "The shop opens ___ eight.",
                "options": ["in", "on", "at", "for"],
                "answer": "at",
                "explanation": "Точное время → at.",
            },

            {
                "order": 14,
                "prompt": "We study English ___ Tuesdays.",
                "options": ["in", "on", "at", "since"],
                "answer": "on",
                "explanation": "День недели → on.",
            },

            {
                "order": 15,
                "prompt": "They travel a lot ___ summer.",
                "options": ["in", "on", "at", "by"],
                "answer": "in",
                "explanation": "Время года → in.",
            },

            {
                "order": 16,
                "prompt": "I am usually tired ___ the evening.",
                "options": ["at", "on", "in", "for"],
                "answer": "in",
                "explanation": "Часть дня: in the evening.",
            },

            {
                "order": 17,
                "prompt": "The meeting is ___ 15 July.",
                "options": ["in", "at", "on", "since"],
                "answer": "on",
                "explanation": "Дата → on.",
            },

            {
                "order": 18,
                "prompt": "I will call you ___ ten minutes.",
                "options": ["for", "in", "since", "during"],
                "answer": "in",
                "explanation": "Через десять минут → in.",
            },

            {
                "order": 19,
                "prompt": "I spoke to him ___ ten minutes.",
                "options": ["in", "since", "for", "by"],
                "answer": "for",
                "explanation": "Длительность разговора → for.",
            },

            {
                "order": 20,
                "prompt": "She has worked here ___ five years.",
                "options": ["since", "during", "for", "by"],
                "answer": "for",
                "explanation": "Five years — продолжительность.",
            },

            {
                "order": 21,
                "prompt": "The shop is open ___ nine.",
                "options": ["by", "until", "since", "during"],
                "answer": "until",
                "explanation": "Работа магазина продолжается до девяти.",
            },

            {
                "order": 22,
                "prompt": "He fell asleep ___ the film.",
                "options": ["for", "since", "during", "by"],
                "answer": "during",
                "explanation": "Film — событие, поэтому during.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I slept during two hours.",
                    "I slept for two hours.",
                    "I slept since two hours.",
                    "I slept by two hours.",
                ],
                "answer": "I slept for two hours.",
                "explanation": "Продолжительность выражается через for.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I have lived here since five years.",
                    "I have lived here for 2020.",
                    "I have lived here for five years.",
                    "I have lived here during five years.",
                ],
                "answer": "I have lived here for five years.",
                "explanation": "Five years — продолжительность, поэтому for.",
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
                "✅ A1 Lesson 18 seeded: "
                "Предлоги времени"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
