from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = "Create/update A1 Grammar Lesson 3: Zero Article."

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=3,
            defaults={
                "title": "Нулевой артикль",
                "slug": "zero-article",
                "theory_text": "Нулевой артикль.",
                "estimated_minutes": 25,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        # ==================================================
        # THEORY
        # ==================================================

        sections = [

            {
                "order": 1,
                "title": "Что такое нулевой артикль",
                "body": """Нулевой артикль означает, что перед существительным не ставится ни a/an, ни the.

Примеры:

I like coffee. — Я люблю кофе.
Children need care. — Детям нужна забота.
Books are useful. — Книги полезны.
Kazakhstan is a large country. — Казахстан — большая страна.

То есть существительное употребляется без артикля.

В заданиях нулевой артикль часто обозначают:

—
zero article
no article

Нулевой артикль часто используется:

• с неисчисляемыми существительными в общем значении;
• с существительными во множественном числе в общем значении;
• с именами людей;
• с большинством стран и городов;
• с языками и учебными предметами;
• с названиями еды;
• с видами спорта;
• в некоторых устойчивых выражениях.""",
            },

            {
                "order": 2,
                "title": "Неисчисляемые существительные",
                "body": """Неисчисляемые существительные обозначают то, что обычно нельзя посчитать как отдельные предметы.

Например:

water — вода;
milk — молоко;
coffee — кофе;
money — деньги;
information — информация;
advice — совет;
happiness — счастье;
love — любовь;
music — музыка;
work — работа.

Нельзя сказать:

one water;
two informations;
three advices.

Поэтому с такими словами нельзя использовать a/an.

Неправильно:

a money;
an information;
an advice.

Правильно:

money;
information;
advice.""",
            },

            {
                "order": 3,
                "title": "Общее и конкретное значение",
                "body": """Если неисчисляемое существительное используется в общем значении, артикль обычно не нужен.

Water is important.
— Вода важна вообще.

Но если речь идёт о конкретной воде:

The water in this bottle is cold.
— Вода в этой бутылке холодная.

Сравните:

Music helps people relax.
— Музыка вообще помогает людям расслабиться.

The music in this café is too loud.
— Конкретная музыка в этом кафе слишком громкая.

Ещё пример:

Money cannot buy you happiness.

Happiness — неисчисляемое существительное и обозначает счастье вообще.

Но возможно:

The happiness she felt was difficult to describe.

Здесь речь идёт о конкретном чувстве счастья.""",
            },

            {
                "order": 4,
                "title": "Множественное число в общем значении",
                "body": """Когда мы говорим о людях, животных или предметах вообще, артикль не используется.

Children like games.
Dogs are friendly animals.
Teachers help students.
Books are useful.

Речь идёт обо всей группе вообще.

Сравните:

Students need practice.
— Студентам вообще нужна практика.

The students in my group need practice.
— Конкретным студентам моей группы нужна практика.

Cars are expensive.
— Машины вообще дорогие.

The cars outside are expensive.
— Конкретные машины снаружи дорогие.""",
            },

            {
                "order": 5,
                "title": "Имена людей и титулы",
                "body": """Перед именами людей артикль обычно не ставится.

Marat is my friend.
Aigul works at a school.
Charles Dickens was a writer.
Abai Kunanbayev was a poet.

Неправильно:

the Marat;
a Aigul;
the Charles Dickens.

Когда титул используется вместе с именем, артикль тоже обычно не нужен:

Professor Brown;
Doctor Smith;
President Lincoln;
Queen Elizabeth II.

Но если должность используется без имени и речь идёт о конкретном человеке, нужен the:

the president;
the doctor;
the teacher.

Сравните:

Doctor Smith is here.
The doctor is here.""",
            },

            {
                "order": 6,
                "title": "Страны, города и континенты",
                "body": """Большинство названий стран употребляется без артикля:

Kazakhstan;
France;
Germany;
China;
Japan;
Canada.

Kazakhstan is in Central Asia.
France is famous for its cuisine.
Japan is an island country.

Но the используется с названиями типа:

the United Kingdom;
the United States;
the Czech Republic;
the Russian Federation;
the United Arab Emirates.

Перед названиями городов и континентов артикль обычно не ставится:

London;
Astana;
Almaty;
Paris;
Asia;
Europe;
Africa.

London is the capital of the United Kingdom.
Astana is the capital of Kazakhstan.
Asia is the largest continent.""",
            },

            {
                "order": 7,
                "title": "Языки и учебные предметы",
                "body": """Перед названиями языков артикль обычно не ставится.

English;
Kazakh;
Russian;
French;
German.

I speak English.
She is learning Kazakh.
They study Russian.

Неправильно:

I study the English.

Но выражение the English может обозначать английский народ:

The English are known for drinking tea.

Перед названиями учебных предметов артикль тоже обычно не ставится:

mathematics;
history;
geography;
biology;
English;
physics.

I like history.
She teaches English.
Mathematics is difficult for him.""",
            },

            {
                "order": 8,
                "title": "Приёмы пищи",
                "body": """Перед названиями обычных приёмов пищи артикль обычно не ставится.

have breakfast;
eat lunch;
cook dinner.

I have breakfast at seven.
We had lunch together.
She is cooking dinner.

Но артикль возможен, когда речь идёт о конкретном событии или приём пищи описывается:

The breakfast at the hotel was excellent.
We had a wonderful dinner.
They organised a formal lunch.

Сравните:

We had dinner at eight.

The dinner at the hotel was delicious.""",
            },

            {
                "order": 9,
                "title": "Спорт и музыкальные инструменты",
                "body": """Перед названиями видов спорта артикль обычно не ставится.

play football;
play tennis;
play basketball;
play chess;
go swimming.

He plays football.
She likes tennis.
We play chess after work.

Важно не путать спорт и музыкальные инструменты.

Со спортом:

play football;
play tennis;
play chess.

С музыкальными инструментами:

play the piano;
play the guitar;
play the violin.

Сравните:

She plays tennis.
She plays the piano.""",
            },

            {
                "order": 10,
                "title": "School, work, bed и home",
                "body": """В некоторых устойчивых выражениях артикль не используется, когда человек находится в месте ради его обычной функции.

go to school;
be at school;
go to university;
be at university;
go to work;
be at work;
go to bed;
be in bed;
go home;
be at home.

Сравните:

The child goes to school every day.
— Ребёнок ходит в школу учиться.

The mother went to the school to speak to the teacher.
— Мама пошла в конкретное здание школы.

He went to bed at ten.
— Он лёг спать.

The cat is under the bed.
— Речь идёт о конкретной кровати.

После глаголов движения обычно говорим:

go home;
come home;
return home;
get home.

Неправильно:

go to home;
go to the home.""",
            },

            {
                "order": 11,
                "title": "Дни недели, месяцы и времена года",
                "body": """Перед днями недели и названиями месяцев артикль обычно не ставится.

on Monday;
in July;
in December;
on Friday morning.

We have English on Monday.
My birthday is in July.

С временами года часто возможны оба варианта:

in summer;
in the summer.

Но когда речь идёт о конкретном периоде, чаще используется the:

We travelled to London in the summer of 2025.""",
            },

            {
                "order": 12,
                "title": "Транспорт",
                "body": """После by перед видом транспорта артикль не используется.

by bus;
by car;
by train;
by plane;
by taxi.

I go to work by bus.
We travelled by train.
She came by taxi.

Но если речь идёт о конкретном транспортном средстве, нужен артикль:

I took the bus.
We missed the train.
She got into the car.

Сравните:

I go to work by bus.

I took the bus at eight.""",
            },

            {
                "order": 13,
                "title": "Типичные ошибки",
                "body": """Неправильно:

She gave me an advice.

Правильно:

She gave me advice.
She gave me a piece of advice.

Неправильно:

The dogs are friendly animals.

Если речь идёт о собаках вообще:

Dogs are friendly animals.

Неправильно:

I study the English.

Правильно:

I study English.

Неправильно:

He plays the football.

Правильно:

He plays football.

Неправильно:

We have the breakfast at seven.

Правильно:

We have breakfast at seven.

Неправильно:

I went to home.

Правильно:

I went home.""",
            },

            {
                "order": 14,
                "title": "Как выбрать артикль",
                "body": """Когда видите существительное, задайте себе несколько вопросов.

1. Существительное исчисляемое и стоит в единственном числе?

Если да, обычно нужен:

a/an;
the;
my/your/this и другое определяющее слово.

Нельзя просто сказать:

book.

Но можно:

a book;
the book;
my book.

2. Речь идёт о конкретном предмете?

Если да, часто используется the:

the book on the table;
the water in this glass;
the students in my group.

3. Речь идёт о чём-то вообще?

Если это неисчисляемое существительное или существительное во множественном числе, артикль обычно не нужен:

Water is important.
Books are useful.

4. Это имя, язык, обычное название страны или города, спорт или обычный приём пищи?

Чаще всего артикль не нужен:

Marat;
English;
Kazakhstan;
London;
football;
breakfast.""",
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


        # ==================================================
        # PRACTICE
        # ==================================================

        exercises = [

            {
                "order": 1,
                "prompt": "___ money cannot solve every problem.",
                "options": ["A", "An", "The", "—"],
                "answer": "—",
                "explanation": "Money — неисчисляемое существительное в общем значении.",
            },

            {
                "order": 2,
                "prompt": "I need ___ information about the course.",
                "options": ["a", "an", "the", "—"],
                "answer": "—",
                "explanation": "Information — неисчисляемое существительное. Здесь речь идёт об информации вообще.",
            },

            {
                "order": 3,
                "prompt": "___ information in this email is important.",
                "options": ["A", "An", "The", "—"],
                "answer": "The",
                "explanation": "Речь идёт о конкретной информации — информации в этом письме.",
            },

            {
                "order": 4,
                "prompt": "___ dogs are loyal animals.",
                "options": ["A", "An", "The", "—"],
                "answer": "—",
                "explanation": "Речь идёт о собаках вообще, поэтому артикль не нужен.",
            },

            {
                "order": 5,
                "prompt": "___ dogs in our garden are noisy.",
                "options": ["A", "An", "The", "—"],
                "answer": "The",
                "explanation": "Речь идёт о конкретных собаках — собаках в нашем саду.",
            },

            {
                "order": 6,
                "prompt": "She speaks ___ English and ___ Kazakh.",
                "options": [
                    "— / —",
                    "the / the",
                    "a / a",
                    "the / —",
                ],
                "answer": "— / —",
                "explanation": "Перед названиями языков артикль обычно не ставится.",
            },

            {
                "order": 7,
                "prompt": "He lives in ___ Kazakhstan.",
                "options": ["a", "an", "the", "—"],
                "answer": "—",
                "explanation": "Kazakhstan — обычное название страны, поэтому артикль не нужен.",
            },

            {
                "order": 8,
                "prompt": "They moved to ___ United States.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "Правильно: the United States.",
            },

            {
                "order": 9,
                "prompt": "We have ___ lunch at one o'clock.",
                "options": ["a", "an", "the", "—"],
                "answer": "—",
                "explanation": "Перед обычным названием приёма пищи артикль не нужен.",
            },

            {
                "order": 10,
                "prompt": "___ lunch at the hotel was excellent.",
                "options": ["A", "An", "The", "—"],
                "answer": "The",
                "explanation": "Речь идёт о конкретном обеде — обеде в отеле.",
            },

            {
                "order": 11,
                "prompt": "My brother plays ___ football.",
                "options": ["a", "an", "the", "—"],
                "answer": "—",
                "explanation": "Перед названием вида спорта артикль не используется.",
            },

            {
                "order": 12,
                "prompt": "My sister plays ___ violin.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "С музыкальными инструментами обычно используется the: play the violin.",
            },

            {
                "order": 13,
                "prompt": "I go to work by ___ car.",
                "options": ["a", "an", "the", "—"],
                "answer": "—",
                "explanation": "После by перед видом транспорта артикль не используется.",
            },

            {
                "order": 14,
                "prompt": "I left my bag in ___ car.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "Речь идёт о конкретной машине.",
            },

            {
                "order": 15,
                "prompt": "The children go to ___ school at eight.",
                "options": ["a", "an", "the", "—"],
                "answer": "—",
                "explanation": "Go to school означает посещать школу ради её основной функции — учёбы.",
            },

            {
                "order": 16,
                "prompt": "Their mother went to ___ school to meet the director.",
                "options": ["a", "an", "the", "—"],
                "answer": "the",
                "explanation": "Речь идёт о конкретном здании школы.",
            },

            {
                "order": 17,
                "prompt": "He went ___ home after work.",
                "options": ["a", "to the", "the", "—"],
                "answer": "—",
                "explanation": "Правильно: go home. Перед home здесь не нужны ни предлог to, ни артикль.",
            },

            {
                "order": 18,
                "prompt": "We study ___ history and ___ mathematics.",
                "options": [
                    "— / —",
                    "the / the",
                    "a / a",
                    "the / —",
                ],
                "answer": "— / —",
                "explanation": "Перед названиями учебных предметов артикль обычно не ставится.",
            },

            {
                "order": 19,
                "prompt": "___ love is important for children.",
                "options": ["A", "An", "The", "—"],
                "answer": "—",
                "explanation": "Love используется в общем значении и является неисчисляемым существительным.",
            },

            {
                "order": 20,
                "prompt": "___ love she felt for her child was very strong.",
                "options": ["A", "An", "The", "—"],
                "answer": "The",
                "explanation": "Речь идёт о конкретной любви — любви, которую она испытывала к своему ребёнку.",
            },

        ]


        for data in exercises:

            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "exercise_type":
                        GrammarExercise.Type.CHOICE,

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


        self.stdout.write(
            self.style.SUCCESS(
                "✅ A1 Lesson 3 seeded: Нулевой артикль"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
