from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 2: definite article THE."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=2,
                defaults={
                    "title":
                        "Определённый артикль THE",

                    "slug":
                        "definite-article-the",

                    "theory_text":
                        "Определённый артикль THE.",

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
                    "Когда нужен THE?",

                "body":
                    """THE показывает, что речь идёт о конкретном, понятном предмете.

Сравни:

I see a dog.
Я вижу какую-то собаку.

The dog is black.
Эта собака чёрная.

A / AN → предмет пока неизвестен.
THE → мы уже понимаем, о каком предмете идёт речь.

THE можно мысленно понимать как:
«этот», «эта», «эти», «тот», «конкретный».

Но отдельно THE обычно не переводится.""",
            },


            {
                "order": 2,

                "title":
                    "Предмет уже известен или понятен из ситуации",

                "body":
                    """Если предмет уже называли, при повторном упоминании обычно используется THE.

I bought a book.
The book is interesting.

She saw a man.
The man was wearing a black coat.

THE также нужен, когда предмет не называли, но из ситуации понятно, о чём речь:

Close the door, please.
Open the window.
Turn off the light.

Говорящий и слушающий понимают, какую именно дверь, окно или свет имеют в виду.""",
            },


            {
                "order": 3,

                "title":
                    "Уникальные объекты",

                "body":
                    """С объектами, которые воспринимаются как уникальные, обычно используется THE.

the sun
the moon
the sky
the Earth
the world

The sun is shining.

The moon looks beautiful tonight.

We must protect the Earth.""",
            },


            {
                "order": 4,

                "title":
                    "THE перед best, biggest, first, second...",

                "body":
                    """Перед превосходной степенью прилагательного обычно используется THE:

the best
the biggest
the highest
the most interesting
the most beautiful

She is the best student.

Перед порядковыми числительными также обычно нужен THE:

the first
the second
the third
the tenth

He lives on the second floor.""",
            },


            {
                "order": 5,

                "title":
                    "THE в географических названиях",

                "body":
                    """THE обычно используется с:

реками:
the Thames
the Nile
the Irtysh

морями и океанами:
the Caspian Sea
the Atlantic Ocean
the Pacific Ocean

горными цепями:
the Alps
the Himalayas

пустынями:
the Sahara
the Gobi Desert

группами островов:
the Maldives
the Philippines

Но обычные названия стран чаще используются без THE:

Kazakhstan
France
China
Germany

THE появляется в некоторых официальных названиях:

the United Kingdom
the United States
the Czech Republic
the United Arab Emirates.""",
            },


            {
                "order": 6,

                "title":
                    "Музеи, театры и другие названия",

                "body":
                    """THE входит в названия многих известных музеев, галерей и других объектов:

the British Museum
the National Gallery
the Tower of London
the Bolshoi Theatre

We visited the British Museum.

Но THE используется не со всеми собственными названиями.

Например:

Buckingham Palace
Oxford University
Heathrow Airport

Поэтому названия организаций и зданий иногда нужно запоминать как готовые выражения.""",
            },


            {
                "order": 7,

                "title":
                    "Музыкальные инструменты, спорт и группы людей",

                "body":
                    """Когда говорим об умении играть на музыкальном инструменте, обычно используется THE:

play the piano
play the guitar
play the violin

Но со спортивными играми артикль обычно не используется:

play football
play tennis
play basketball

THE + прилагательное может обозначать целую группу людей:

the rich — богатые
the poor — бедные
the young — молодые
the elderly — пожилые
the unemployed — безработные

The government should help the poor.

Такие слова обычно требуют глагол во множественном числе:

The rich are not always happy.""",
            },


            {
                "order": 8,

                "title":
                    "THE может стоять перед любым типом существительного",

                "body":
                    """THE может использоваться:

с единственным числом:
the book

с множественным числом:
the books

с неисчисляемым существительным:
the water
the information

Главное условие — речь должна идти о чём-то конкретном.

Сравни:

Water is important.
Вода вообще важна.

The water in this bottle is cold.
Конкретная вода в этой бутылке холодная.

Books are useful.
Книги вообще полезны.

The books on the table are mine.
Конкретные книги на столе мои.""",
            },


            {
                "order": 9,

                "title":
                    "A / AN, THE или без артикля?",

                "body":
                    """Используй простой алгоритм.

A / AN:
предмет упоминается впервые и он один.

I saw a cat.

THE:
предмет уже известен или конкретен.

The cat was under the table.

Без артикля:
говорим о множественном числе или неисчисляемом понятии вообще.

Children need love.
Books are useful.
Water is important.

Но если эти предметы становятся конкретными:

The children in this room...
The books on the table...
The water in this bottle...""",
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
                    "I saw a dog. ___ dog was very friendly.",
                "options":
                    ["A", "An", "The", "—"],
                "answer":
                    "The",
                "explanation":
                    "Собака уже упоминалась, поэтому теперь она конкретная.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "She bought ___ dress. The dress was expensive.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "a",
                "explanation":
                    "При первом упоминании одного неизвестного предмета используем A.",
            },

            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "Please close ___ door.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "the",
                "explanation":
                    "Из ситуации понятно, какую именно дверь нужно закрыть.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "fill",
                "prompt":
                    "Turn off ___ light.",
                "options":
                    [],
                "answer":
                    "the",
                "explanation":
                    "Говорящий и слушающий понимают, о каком свете идёт речь.",
            },

            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "___ sun is shining.",
                "options":
                    ["A", "An", "The", "—"],
                "answer":
                    "The",
                "explanation":
                    "Солнце рассматривается как уникальный объект.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "fill",
                "prompt":
                    "We must protect ___ Earth.",
                "options":
                    [],
                "answer":
                    "the",
                "explanation":
                    "Earth здесь рассматривается как уникальный объект.",
            },

            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "She is ___ best student in the class.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "the",
                "explanation":
                    "Перед превосходной степенью best используется THE.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "build",
                "prompt":
                    "Собери правильную фразу.",
                "options":
                    [
                        "the",
                        "first",
                        "lesson",
                    ],
                "answer":
                    "the first lesson",
                "explanation":
                    "Перед порядковым числительным first используется THE.",
            },

            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "London stands on ___ Thames.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "the",
                "explanation":
                    "С названиями рек используется THE.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "They crossed ___ Pacific Ocean.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "the",
                "explanation":
                    "С названиями океанов используется THE.",
            },

            {
                "order": 11,
                "section": 5,
                "type": "choice",
                "prompt":
                    "___ Kazakhstan is a large country.",
                "options":
                    ["A", "An", "The", "—"],
                "answer":
                    "—",
                "explanation":
                    "Обычное название Kazakhstan употребляется без THE.",
            },

            {
                "order": 12,
                "section": 5,
                "type": "choice",
                "prompt":
                    "They travelled to ___ United Kingdom.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "the",
                "explanation":
                    "Название the United Kingdom употребляется с THE.",
            },

            {
                "order": 13,
                "section": 6,
                "type": "choice",
                "prompt":
                    "We visited ___ British Museum.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "the",
                "explanation":
                    "Правильное название — the British Museum.",
            },

            {
                "order": 14,
                "section": 6,
                "type": "choice",
                "prompt":
                    "They visited ___ Buckingham Palace.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "—",
                "explanation":
                    "Buckingham Palace обычно используется без артикля.",
            },

            {
                "order": 15,
                "section": 7,
                "type": "fill",
                "prompt":
                    "He can play ___ guitar.",
                "options":
                    [],
                "answer":
                    "the",
                "explanation":
                    "При игре на музыкальном инструменте обычно используется THE.",
            },

            {
                "order": 16,
                "section": 7,
                "type": "choice",
                "prompt":
                    "She plays ___ tennis every weekend.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "—",
                "explanation":
                    "С названиями спортивных игр артикль обычно не используется.",
            },

            {
                "order": 17,
                "section": 7,
                "type": "choice",
                "prompt":
                    "The government should help ___ poor.",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "the",
                "explanation":
                    "THE + adjective может обозначать группу людей: the poor.",
            },

            {
                "order": 18,
                "section": 8,
                "type": "choice",
                "prompt":
                    "___ water in this bottle is cold.",
                "options":
                    ["A", "An", "The", "—"],
                "answer":
                    "The",
                "explanation":
                    "Речь идёт о конкретной воде в конкретной бутылке.",
            },

            {
                "order": 19,
                "section": 8,
                "type": "choice",
                "prompt":
                    "Books are useful. Какой артикль нужен перед Books?",
                "options":
                    ["a", "an", "the", "—"],
                "answer":
                    "—",
                "explanation":
                    "Речь идёт о книгах вообще, поэтому артикль не нужен.",
            },

            {
                "order": 20,
                "section": 9,
                "type": "choice",
                "prompt":
                    "I bought ___ phone yesterday. ___ phone is expensive.",
                "options":
                    [
                        "a / the",
                        "the / a",
                        "the / the",
                        "a / a",
                    ],
                "answer":
                    "a / the",
                "explanation":
                    "Первое упоминание — A. Повторное упоминание конкретного телефона — THE.",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # section=None means FINAL TEST
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "I saw a movie last night. ___ movie was excellent.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "The",

                "explanation":
                    "Movie уже упоминался, поэтому при повторном упоминании используется THE.",
            },

            {
                "order": 22,

                "prompt":
                    "Could you open ___ window, please?",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "the",

                "explanation":
                    "Из ситуации понятно, какое конкретно окно имеется в виду.",
            },

            {
                "order": 23,

                "prompt":
                    "___ moon is very bright tonight.",

                "options":
                    ["A", "An", "The", "—"],

                "answer":
                    "The",

                "explanation":
                    "Moon рассматривается как уникальный объект.",
            },

            {
                "order": 24,

                "prompt":
                    "This is ___ most expensive hotel in the city.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "the",

                "explanation":
                    "Перед превосходной степенью most expensive используется THE.",
            },

            {
                "order": 25,

                "prompt":
                    "Our office is on ___ second floor.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "the",

                "explanation":
                    "Перед порядковым числительным second используется THE.",
            },

            {
                "order": 26,

                "prompt":
                    "Выбери правильную пару.",

                "options": [
                    "the Nile / Kazakhstan",
                    "Nile / the Kazakhstan",
                    "the Nile / the Kazakhstan",
                    "Nile / Kazakhstan",
                ],

                "answer":
                    "the Nile / Kazakhstan",

                "explanation":
                    "С названием реки нужен THE, а Kazakhstan обычно используется без артикля.",
            },

            {
                "order": 27,

                "prompt":
                    "Выбери правильную пару.",

                "options": [
                    "the United States / the National Gallery",
                    "United States / National Gallery",
                    "the United States / National Gallery",
                    "United States / the National Gallery",
                ],

                "answer":
                    "the United States / the National Gallery",

                "explanation":
                    "Оба названия в этих формах употребляются с THE.",
            },

            {
                "order": 28,

                "prompt":
                    "She plays ___ violin, but she plays ___ basketball.",

                "options": [
                    "the / —",
                    "— / the",
                    "the / the",
                    "— / —",
                ],

                "answer":
                    "the / —",

                "explanation":
                    "С музыкальным инструментом используется THE, а со спортивной игрой — без артикля.",
            },

            {
                "order": 29,

                "prompt":
                    "This programme helps ___ elderly.",

                "options":
                    ["a", "an", "the", "—"],

                "answer":
                    "the",

                "explanation":
                    "THE + adjective может обозначать группу людей: the elderly.",
            },

            {
                "order": 30,

                "prompt":
                    "Выбери правильный вариант.",

                "options": [
                    "Water is important. The water in this glass is cold.",
                    "The water is important. Water in this glass is cold.",
                    "A water is important. The water in this glass is cold.",
                    "Water is important. A water in this glass is cold.",
                ],

                "answer":
                    "Water is important. The water in this glass is cold.",

                "explanation":
                    "В первом предложении water означает воду вообще, а во втором речь идёт о конкретной воде.",
            },

        ]


        all_exercises = (
            training
            +
            final_test
        )


        valid_orders = []


        for data in all_exercises:

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


        # Remove old sections 10-14 after exercises
        # have been reassigned to the new structure.

        GrammarLessonSection.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=[
                item["order"]
                for item in sections
            ],
        ).delete()


        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        self.stdout.write(
            self.style.SUCCESS(
                "✅ Interactive A1 Lesson 2 seeded"
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
