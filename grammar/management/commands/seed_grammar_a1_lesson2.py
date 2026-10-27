from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = "Create/update A1 Grammar Lesson 2: definite article THE."

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=2,
            defaults={
                "title": "Определённый артикль THE",
                "slug": "definite-article-the",
                "theory_text": "Определённый артикль THE.",
                "estimated_minutes": 20,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что означает THE",
                "body": """Артикль the употребляется, когда говорящий имеет в виду конкретный, определённый предмет.

Сравните:

I see a dog. — Я вижу какую-то собаку.

The dog is black. — Эта собака чёрная.

В первом предложении собака упоминается впервые, поэтому используется a.

Во втором предложении уже понятно, о какой собаке идёт речь, поэтому используется the.

Артикль the часто можно мысленно понять как:

этот;
эта;
это;
эти;
тот;
та;
конкретный.

Но отдельно обычно он не переводится.""",
            },

            {
                "order": 2,
                "title": "THE с уже известным предметом",
                "body": """Если предмет уже был назван, при повторном упоминании используется the.

Пример:

I bought a book yesterday.
— Вчера я купил книгу.

The book is very interesting.
— Эта книга очень интересная.

Ещё пример:

She saw a man near the house.
The man was wearing a black coat.

Сначала мы говорим о каком-то мужчине.

Затем уже ясно, о каком именно мужчине идёт речь.""",
            },

            {
                "order": 3,
                "title": "THE, когда предмет понятен из ситуации",
                "body": """Иногда предмет не назывался раньше, но всем понятно, о чём идёт речь.

Примеры:

Close the door, please.
— Закрой дверь, пожалуйста.

Open the window.
— Открой окно.

Turn off the light.
— Выключи свет.

Говорящий и слушающий находятся в одной ситуации и понимают, какую дверь, какое окно или какой свет имеют в виду.""",
            },

            {
                "order": 4,
                "title": "THE с уникальными объектами",
                "body": """Некоторые объекты считаются уникальными.

Поэтому с ними обычно используется the.

Примеры:

the sun — солнце;
the moon — луна;
the sky — небо;
the Earth — Земля;
the world — мир.

Предложения:

The sun is shining.

The moon looks beautiful tonight.

We must protect the Earth.""",
            },

            {
                "order": 5,
                "title": "THE с превосходной степенью",
                "body": """Перед превосходной степенью прилагательного обычно ставится the.

Примеры:

the best — лучший;
the biggest — самый большой;
the most interesting — самый интересный;
the most beautiful — самый красивый.

Предложения:

She is the best student in the class.

This is the most interesting book I have read.

Everest is the highest mountain in the world.

Неправильно:

She is best student.

Правильно:

She is the best student.""",
            },

            {
                "order": 6,
                "title": "THE с порядковыми числительными",
                "body": """Перед порядковыми числительными обычно используется the.

Примеры:

the first — первый;
the second — второй;
the third — третий;
the tenth — десятый.

Предложения:

This is the first lesson.

He lives on the second floor.

She was the third person to arrive.""",
            },

            {
                "order": 7,
                "title": "THE с географическими объектами",
                "body": """Артикль the используется с названиями некоторых географических объектов.

Реки:

the Thames;
the Nile;
the Irtysh.

Моря и океаны:

the Caspian Sea;
the Atlantic Ocean;
the Pacific Ocean.

Горные цепи:

the Alps;
the Himalayas.

Пустыни:

the Sahara;
the Gobi Desert.

Группы островов:

the Maldives;
the Philippines.

Примеры:

London stands on the Thames.

Kazakhstan is near the Caspian Sea.

The Pacific Ocean is very large.""",
            },

            {
                "order": 8,
                "title": "THE с названиями некоторых стран",
                "body": """Обычно названия стран употребляются без артикля:

Kazakhstan;
France;
China;
Germany.

Но the используется, если в названии есть слова:

republic;
kingdom;
states;
federation;
emirates.

Примеры:

the United Kingdom;
the United States;
the Czech Republic;
the United Arab Emirates.

Сравните:

Kazakhstan is a large country.

The United Kingdom consists of four parts.""",
            },

            {
                "order": 9,
                "title": "THE с известными зданиями, музеями и театрами",
                "body": """Артикль the часто используется с названиями известных объектов.

Примеры:

the British Museum;
the National Gallery;
the Tower of London;
the Bolshoi Theatre.

Предложения:

We visited the British Museum.

They went to the National Gallery.

Но некоторые названия употребляются без артикля:

Buckingham Palace;
Oxford University;
Heathrow Airport.""",
            },

            {
                "order": 10,
                "title": "THE с музыкальными инструментами",
                "body": """Когда говорим об умении играть на музыкальном инструменте, обычно используем the.

Примеры:

play the piano;
play the guitar;
play the violin.

Предложения:

She plays the piano.

He can play the guitar.

Но со спортивными играми артикль обычно не используется:

play football;
play tennis;
play basketball.""",
            },

            {
                "order": 11,
                "title": "THE + прилагательное = группа людей",
                "body": """Иногда прилагательное с артиклем the обозначает целую группу людей.

Примеры:

the rich — богатые;
the poor — бедные;
the young — молодые;
the elderly — пожилые;
the unemployed — безработные.

Предложения:

The government should help the poor.

This programme supports the elderly.

После таких слов глагол обычно стоит во множественном числе:

The rich are not always happy.""",
            },

            {
                "order": 12,
                "title": "THE с единственным, множественным и неисчисляемым",
                "body": """Артикль the может употребляться:

с единственным числом;
с множественным числом;
с неисчисляемыми существительными.

Примеры:

the book;
the books;
the water;
the information.

Главное — предмет или понятие должны быть конкретными.

Сравните:

Water is important.
— Вода важна вообще.

The water in this bottle is cold.
— Вода в этой бутылке холодная.""",
            },

            {
                "order": 13,
                "title": "Сравнение A и THE",
                "body": """A используется, когда предмет упоминается впервые или ещё неизвестен.

I saw a cat.

THE используется, когда предмет уже известен или конкретен.

The cat was under the table.

Ещё пример:

She bought a dress.

The dress was expensive.""",
            },

            {
                "order": 14,
                "title": "Когда THE не нужен",
                "body": """Не нужно использовать the, когда говорим о предметах или понятиях в общем смысле.

Сравните:

Children need love.
— Детям вообще нужна любовь.

The children in this room are quiet.
— Конкретные дети в этой комнате ведут себя тихо.

Ещё пример:

Books are useful.
— Книги вообще полезны.

The books on the table are mine.
— Конкретные книги на столе мои.""",
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
                "prompt": "I saw a dog. ___ dog was very friendly.",
                "options": ["A", "An", "The", "—"],
                "answer": "The",
                "explanation": "Собака уже упоминалась, поэтому используется the.",
            },

            {
                "order": 2,
                "prompt": "Please close ___ window.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "Из ситуации понятно, какое именно окно нужно закрыть.",
            },

            {
                "order": 3,
                "prompt": "___ sun is shining.",
                "options": ["A", "An", "The", "—"],
                "answer": "The",
                "explanation": "Солнце рассматривается как уникальный объект.",
            },

            {
                "order": 4,
                "prompt": "She is ___ best student in the group.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "Перед превосходной степенью используется the.",
            },

            {
                "order": 5,
                "prompt": "He lives on ___ third floor.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "Перед порядковым числительным используется the.",
            },

            {
                "order": 6,
                "prompt": "I bought ___ phone yesterday. ___ phone is expensive.",
                "options": [
                    "a / the",
                    "the / a",
                    "the / the",
                    "a / a",
                ],
                "answer": "a / the",
                "explanation": "Первое упоминание — a. Повторное упоминание конкретного телефона — the.",
            },

            {
                "order": 7,
                "prompt": "Kazakhstan is ___ large country.",
                "options": ["a", "an", "the", "—"],
                "answer": "a",
                "explanation": "Обычное название Kazakhstan употребляется без the, но перед исчисляемым country нужен a.",
            },

            {
                "order": 8,
                "prompt": "They visited ___ United Kingdom.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "С названием the United Kingdom используется the.",
            },

            {
                "order": 9,
                "prompt": "Children like ___ games.",
                "options": ["a", "an", "the", "—"],
                "answer": "—",
                "explanation": "Речь идёт об играх вообще, поэтому артикль не нужен.",
            },

            {
                "order": 10,
                "prompt": "___ games on this shelf are new.",
                "options": ["A", "An", "The", "—"],
                "answer": "The",
                "explanation": "Речь идёт о конкретных играх на этой полке.",
            },

            {
                "order": 11,
                "prompt": "He can play ___ guitar.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "С музыкальными инструментами в конструкции play обычно используется the.",
            },

            {
                "order": 12,
                "prompt": "She plays ___ tennis every weekend.",
                "options": ["a", "an", "the", "—"],
                "answer": "—",
                "explanation": "С названиями спортивных игр артикль обычно не используется.",
            },

            {
                "order": 13,
                "prompt": "This is ___ first time I have visited London.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "Перед порядковым числительным first используется the.",
            },

            {
                "order": 14,
                "prompt": "We went to ___ British Museum.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "Название музея употребляется как the British Museum.",
            },

            {
                "order": 15,
                "prompt": "___ water in this glass is warm.",
                "options": ["A", "An", "The", "—"],
                "answer": "The",
                "explanation": "Это конкретная вода — вода именно в этом стакане.",
            },

            {
                "order": 16,
                "prompt": "We live near ___ Irtysh River.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "С названиями рек используется the.",
            },

            {
                "order": 17,
                "prompt": "London stands on ___ Thames.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "С названиями рек используется the: the Thames.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She is best teacher in our school.",
                    "She is a best teacher in our school.",
                    "She is the best teacher in our school.",
                    "She is an best teacher in our school.",
                ],
                "answer": "She is the best teacher in our school.",
                "explanation": "Перед превосходной степенью best используется the.",
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
                "✅ A1 Lesson 2 seeded: Определённый артикль THE"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
