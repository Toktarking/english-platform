from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive "
        "A1 Grammar Lesson 3: Zero Article."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=3,
                defaults={
                    "title":
                        "Нулевой артикль",

                    "slug":
                        "zero-article",

                    "theory_text":
                        "Нулевой артикль.",

                    "estimated_minutes":
                        15,

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
        # 9 MICRO-RULES
        # =================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Что такое нулевой артикль?",

                "body":
                    """Нулевой артикль означает, что перед существительным не ставится ни A/AN, ни THE.

В заданиях мы обозначаем его так:

—

Примеры:

I like coffee.
Books are useful.
Children need care.
Kazakhstan is a large country.

Нулевой артикль часто используется, когда мы говорим о чём-то вообще, а не о конкретном предмете.""",
            },


            {
                "order": 2,

                "title":
                    "Неисчисляемое: вообще или конкретно?",

                "body":
                    """Неисчисляемые существительные обычно нельзя считать как отдельные предметы:

water
milk
money
information
advice
music
love
happiness

Если говорим о них вообще, артикль обычно не нужен:

Water is important.
Music helps people relax.
Money cannot buy happiness.

Но если значение становится конкретным, обычно появляется THE:

The water in this bottle is cold.

The music in this café is too loud.

The information in this email is important.

Важно:

не говорим an information или an advice.

Можно сказать:

information
advice
a piece of advice.""",
            },


            {
                "order": 3,

                "title":
                    "Множественное число: вообще или конкретно?",

                "body":
                    """Когда говорим о группе людей, животных или предметов вообще, артикль не нужен:

Dogs are friendly animals.
Books are useful.
Students need practice.
Teachers help students.

Но если группа конкретная, используем THE:

The dogs in our garden are noisy.

The books on the table are mine.

The students in my group need practice.

Главный вопрос:

«Все такие предметы вообще» или «конкретные предметы»?""",
            },


            {
                "order": 4,

                "title":
                    "Имена, страны, города и континенты",

                "body":
                    """Перед именами людей обычно нет артикля:

Marat
Aigul
Charles Dickens
Abai Kunanbayev

С титулом + именем тоже обычно без артикля:

Professor Brown
Doctor Smith
President Lincoln

Но если должность используется без имени и человек конкретный:

the doctor
the president
the teacher

Большинство стран:

Kazakhstan
France
Germany
China
Japan

Города и континенты:

London
Astana
Almaty
Paris
Asia
Europe

Но некоторые страны требуют THE:

the United Kingdom
the United States
the Czech Republic
the United Arab Emirates.""",
            },


            {
                "order": 5,

                "title":
                    "Языки и учебные предметы",

                "body":
                    """Перед названиями языков обычно нет артикля:

I speak English.
She is learning Kazakh.
They study Russian.

Перед учебными предметами тоже:

I like history.
She teaches English.
Mathematics is difficult.

Не говорим:

I study the English.

Но выражение the English может означать английский народ:

The English are known for drinking tea.""",
            },


            {
                "order": 6,

                "title":
                    "Еда, спорт и музыкальные инструменты",

                "body":
                    """Перед обычными приёмами пищи артикль обычно не нужен:

have breakfast
have lunch
eat dinner

We had lunch at one.

Но конкретный приём пищи:

The breakfast at the hotel was excellent.

Или описанный как один отдельный приём пищи:

We had a wonderful dinner.

Со спортом артикль обычно не нужен:

play football
play tennis
play basketball
play chess

Но с музыкальными инструментами обычно используется THE:

play the piano
play the guitar
play the violin.""",
            },


            {
                "order": 7,

                "title":
                    "School, work, bed и home",

                "body":
                    """Некоторые места используются без артикля, когда речь идёт об их обычной функции:

go to school
be at school

go to work
be at work

go to bed
be in bed

go home
be at home

Например:

The child goes to school every day.
Он идёт туда учиться.

Но:

The mother went to the school to speak to the teacher.

Здесь school — конкретное здание.

Сравни:

He went to bed.
The cat is under the bed.

Особенно запомни:

go home
come home
return home
get home

Не:

go to home.""",
            },


            {
                "order": 8,

                "title":
                    "Monday, July и by bus",

                "body":
                    """Перед днями недели и месяцами обычно нет артикля:

on Monday
on Friday
in July
in December

We have English on Monday.

С временами года часто возможны варианты:

in summer
in the summer

Но для конкретного периода обычно используется THE:

in the summer of 2025

После BY + транспорт артикль не нужен:

by bus
by car
by train
by plane
by taxi

I go to work by bus.

Но конкретный транспорт:

I took the bus.
We missed the train.
She got into the car.""",
            },


            {
                "order": 9,

                "title":
                    "Как выбрать A, THE или —?",

                "body":
                    """Используй простой алгоритм.

1. Один исчисляемый предмет, который упоминается впервые?

→ A / AN

I bought a book.

2. Предмет конкретный или уже известный?

→ THE

The book is interesting.

3. Множественное число или неисчисляемое слово в общем значении?

→ —

Books are useful.
Water is important.

4. Имя, обычная страна или город, язык, предмет, спорт, обычный приём пищи?

Чаще всего:

→ —

Marat
Kazakhstan
London
English
history
football
breakfast

И помни:

одиночное исчисляемое существительное обычно нельзя оставлять совсем без определителя.

Не:
I bought book.

А:
I bought a book.
I bought the book.
I bought my book.""",
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

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "___ coffee helps me wake up.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "—",

                "explanation":
                    "Coffee используется в общем значении, поэтому артикль не нужен.",
            },


            {
                "order": 2,
                "section": 2,
                "type": "choice",

                "prompt":
                    "I need ___ information about the course.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "—",

                "explanation":
                    "Information — неисчисляемое существительное в общем значении.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "___ information in this email is important.",

                "options":
                    [],

                "answer":
                    "the",

                "explanation":
                    "Речь идёт о конкретной информации — информации в этом письме.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "She gave me ___ advice.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "—",

                "explanation":
                    "Advice — неисчисляемое существительное. Здесь артикль не нужен.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "___ dogs are loyal animals.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "—",

                "explanation":
                    "Речь идёт о собаках вообще.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "___ dogs in our garden are noisy.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "The",

                "explanation":
                    "Это конкретные собаки — собаки в нашем саду.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "___ Professor Brown teaches economics.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "—",

                "explanation":
                    "Перед титулом вместе с именем артикль обычно не используется.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "fill",

                "prompt":
                    "___ doctor is waiting for you.",

                "options":
                    [],

                "answer":
                    "the",

                "explanation":
                    "Doctor используется без имени и означает конкретного врача.",
            },


            {
                "order": 9,
                "section": 4,
                "type": "choice",

                "prompt":
                    "He lives in ___ Kazakhstan.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "—",

                "explanation":
                    "Kazakhstan — обычное название страны, поэтому артикль не нужен.",
            },


            {
                "order": 10,
                "section": 4,
                "type": "choice",

                "prompt":
                    "They moved to ___ United States.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "the",

                "explanation":
                    "Правильное название — the United States.",
            },


            {
                "order": 11,
                "section": 5,
                "type": "choice",

                "prompt":
                    "She speaks ___ English and ___ Kazakh.",

                "options": [
                    "— / —",
                    "the / the",
                    "a / a",
                    "the / —",
                ],

                "answer":
                    "— / —",

                "explanation":
                    "Перед названиями языков артикль обычно не используется.",
            },


            {
                "order": 12,
                "section": 5,
                "type": "choice",

                "prompt":
                    "We study ___ history and ___ mathematics.",

                "options": [
                    "— / —",
                    "the / the",
                    "a / a",
                    "the / —",
                ],

                "answer":
                    "— / —",

                "explanation":
                    "Перед названиями учебных предметов артикль обычно не ставится.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "choice",

                "prompt":
                    "We have ___ breakfast at seven.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "—",

                "explanation":
                    "Обычный приём пищи используется без артикля.",
            },


            {
                "order": 14,
                "section": 6,
                "type": "choice",

                "prompt":
                    "___ breakfast at the hotel was excellent.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "The",

                "explanation":
                    "Речь идёт о конкретном завтраке — завтраке в отеле.",
            },


            {
                "order": 15,
                "section": 6,
                "type": "choice",

                "prompt":
                    "He plays ___ football, but his sister plays ___ violin.",

                "options": [
                    "— / the",
                    "the / —",
                    "the / the",
                    "— / —",
                ],

                "answer":
                    "— / the",

                "explanation":
                    "Спорт используется без артикля, а музыкальный инструмент — с THE.",
            },


            {
                "order": 16,
                "section": 7,
                "type": "choice",

                "prompt":
                    "The children go to ___ school every morning.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "—",

                "explanation":
                    "Go to school означает идти туда ради основной функции — учёбы.",
            },


            {
                "order": 17,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Their mother went to ___ school to meet the director.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "the",

                "explanation":
                    "Здесь речь идёт о конкретном здании школы.",
            },


            {
                "order": 18,
                "section": 7,
                "type": "build",

                "prompt":
                    "Собери правильную фразу.",

                "options": [
                    "go",
                    "home",
                ],

                "answer":
                    "go home",

                "explanation":
                    "Говорим go home — без TO и без артикля.",
            },


            {
                "order": 19,
                "section": 8,
                "type": "choice",

                "prompt":
                    "We have English ___ Monday and usually go there by ___ bus.",

                "options": [
                    "— / —",
                    "the / the",
                    "the / —",
                    "— / the",
                ],

                "answer":
                    "— / —",

                "explanation":
                    "Перед Monday артикль не нужен. После by + transport артикль тоже не используется.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "I bought ___ book yesterday. ___ book is on my desk now.",

                "options": [
                    "a / the",
                    "the / a",
                    "— / the",
                    "a / —",
                ],

                "answer":
                    "a / the",

                "explanation":
                    "Первое упоминание одного предмета — A. Повторное конкретное упоминание — THE.",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "___ music helps many people relax.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "—",

                "explanation":
                    "Music — неисчисляемое существительное в общем значении.",
            },


            {
                "order": 22,

                "prompt":
                    "___ music in this restaurant is too loud.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "The",

                "explanation":
                    "Речь идёт о конкретной музыке в конкретном ресторане.",
            },


            {
                "order": 23,

                "prompt":
                    "___ students need regular practice.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "—",

                "explanation":
                    "Students означает студентов вообще.",
            },


            {
                "order": 24,

                "prompt":
                    "___ students in this classroom are taking a test.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "The",

                "explanation":
                    "Это конкретные студенты — студенты в этой аудитории.",
            },


            {
                "order": 25,

                "prompt":
                    "Выбери правильную пару.",

                "options": [
                    "Doctor Smith / Kazakhstan",
                    "the Doctor Smith / the Kazakhstan",
                    "Doctor Smith / the Kazakhstan",
                    "the Doctor Smith / Kazakhstan",
                ],

                "answer":
                    "Doctor Smith / Kazakhstan",

                "explanation":
                    "Титул + имя и обычное название страны используются без артикля.",
            },


            {
                "order": 26,

                "prompt":
                    "She studies ___ French and ___ biology.",

                "options": [
                    "— / —",
                    "the / the",
                    "a / a",
                    "the / —",
                ],

                "answer":
                    "— / —",

                "explanation":
                    "Перед языками и учебными предметами артикль обычно не нужен.",
            },


            {
                "order": 27,

                "prompt":
                    "He had ___ lunch at noon, then played ___ tennis.",

                "options": [
                    "— / —",
                    "the / the",
                    "a / the",
                    "the / —",
                ],

                "answer":
                    "— / —",

                "explanation":
                    "Обычный приём пищи и вид спорта используются без артикля.",
            },


            {
                "order": 28,

                "prompt":
                    "She went to ___ bed at eleven, but her phone was under ___ bed.",

                "options": [
                    "— / the",
                    "the / —",
                    "the / the",
                    "— / —",
                ],

                "answer":
                    "— / the",

                "explanation":
                    "Go to bed — устойчивое выражение. Во второй части bed означает конкретную кровать.",
            },


            {
                "order": 29,

                "prompt":
                    "We travelled by ___ train, but we almost missed ___ train home.",

                "options": [
                    "— / the",
                    "the / —",
                    "a / the",
                    "the / the",
                ],

                "answer":
                    "— / the",

                "explanation":
                    "После by + transport артикль не используется. Конкретный поезд требует THE.",
            },


            {
                "order": 30,

                "prompt":
                    "Выбери полностью правильный вариант.",

                "options": [
                    "Books are useful. The books on my desk are new.",
                    "The books are useful. Books on my desk are new.",
                    "A books are useful. The books on my desk are new.",
                    "Books are useful. A books on my desk are new.",
                ],

                "answer":
                    "Books are useful. The books on my desk are new.",

                "explanation":
                    "Books без артикля означает книги вообще. The books on my desk — конкретные книги.",
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
                "✅ Interactive A1 Lesson 3 seeded"
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
