from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 24: "
        "Past Simple with was and were."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=24,
            defaults={
                "title": (
                    "Past Simple с глаголом TO BE: "
                    "WAS и WERE"
                ),
                "slug": "past-simple-was-were",
                "theory_text": (
                    "Past Simple with was and were."
                ),
                "estimated_minutes": 35,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое WAS и WERE",
                "body": """WAS и WERE — прошедшие формы глагола to be.

Они используются, когда мы говорим о:

состоянии в прошлом;

месте в прошлом;

возрасте в прошлом;

профессии или роли в прошлом.

Примеры:

I was at home yesterday.

She was tired.

They were students.""",
            },

            {
                "order": 2,
                "title": "WAS или WERE",
                "body": """Главная таблица:

I → was

you → were

he → was

she → was

it → was

we → were

they → were

Запомните:

I / he / she / it → WAS

you / we / they → WERE

Важно:

you всегда используется с were.""",
            },

            {
                "order": 3,
                "title": "Состояние, место и возраст",
                "body": """WAS / WERE могут описывать состояние:

I was tired yesterday.

She was happy.

They were busy.

Место:

I was at home.

She was in Astana.

We were at the university.

Возраст:

I was ten years old.

She was five.

Неправильно:

I had ten years.

Правильно:

I was ten years old.""",
            },

            {
                "order": 4,
                "title": "Профессия, погода и время",
                "body": """Профессия или роль:

He was a teacher.

She was a student.

They were doctors.

Погода:

It was cold yesterday.

It was sunny last weekend.

Время:

It was late.

It was five o'clock.

Формула:

subject + was/were + остальная часть предложения""",
            },

            {
                "order": 5,
                "title": "Слова-маркеры прошлого",
                "body": """С Past Simple часто используются:

yesterday;

last night;

last week;

last month;

last year;

two days ago;

a week ago;

in 2020;

when I was a child.

Примеры:

I was tired yesterday.

She was in Almaty last week.

They were students ten years ago.""",
            },

            {
                "order": 6,
                "title": "AGO",
                "body": """AGO означает «назад».

Оно ставится после периода времени.

Правильно:

two days ago;

three weeks ago;

a year ago;

ten minutes ago.

Неправильно:

ago two days

Правильно:

two days ago

Пример:

She was here a week ago.""",
            },

            {
                "order": 7,
                "title": "Отрицание",
                "body": """Отрицание строится прямо с was/were.

WAS NOT:

wasn't

I wasn't tired.

She wasn't at home.

WERE NOT:

weren't

We weren't ready.

They weren't at school.

Формула:

subject + wasn't / weren't + остальная часть

Do/does/did не нужны.""",
            },

            {
                "order": 8,
                "title": "Общие вопросы",
                "body": """Чтобы задать вопрос, was или were ставится перед подлежащим.

Сравните:

She was at home.

Was she at home?

They were tired.

Were they tired?

Формула:

Was/Were + subject + ...?

Примеры:

Was he at work?

Were you busy?

Were they at school?

Важно:

не используйте did.""",
            },

            {
                "order": 9,
                "title": "Краткие ответы",
                "body": """Вопрос:

Was she at home?

Ответ:

Yes, she was.

No, she wasn't.

Вопрос:

Were they busy?

Ответ:

Yes, they were.

No, they weren't.

Вопрос:

Were you tired?

Ответ:

Yes, I was.

No, I wasn't.""",
            },

            {
                "order": 10,
                "title": "Специальные вопросы",
                "body": """Формула:

Question word + was/were + subject?

Примеры:

Where were you?

Why was she tired?

When were they at home?

How was the lesson?

Who was at the door?

Примеры ответов:

Where were you yesterday?

I was at home.

Why was he angry?

Because he was tired.""",
            },

            {
                "order": 11,
                "title": "HOW WAS / HOW WERE",
                "body": """How was...? означает:

Как прошёл...?

Каким был...?

Примеры:

How was your day?

How was the lesson?

How was the trip?

Ответ:

It was good.

It was interesting.

С множественным числом:

How were the exams?

How were your holidays?

They were difficult.

They were great.""",
            },

            {
                "order": 12,
                "title": "WAS BORN / WERE BORN",
                "body": """Чтобы сказать «родился / родились», используется:

was born;

were born.

Примеры:

I was born in Kazakhstan.

She was born in 2000.

He was born in Karaganda.

They were born in the same year.

Вопросы:

Where were you born?

When was she born?

Неправильно:

I born in 1998.

Правильно:

I was born in 1998.""",
            },

            {
                "order": 13,
                "title": "THERE WAS / THERE WERE",
                "body": """THERE WAS используется с:

одним предметом;

одним человеком;

неисчисляемым существительным.

There was a book on the table.

There was some water.

THERE WERE используется с множественным числом.

There were two books.

There were many students.

Вопросы:

Was there a problem?

Were there any students?

Ответы:

Yes, there was.

No, there weren't.""",
            },

            {
                "order": 14,
                "title": "WAS/WERE или обычный глагол",
                "body": """WAS/WERE используются с:

профессией;

прилагательным;

местом;

возрастом.

She was a teacher.

He was tired.

They were at home.

Но если это действие, нужен обычный глагол в Past Simple.

She worked yesterday.

He studied English.

Неправильно:

She was worked yesterday.

Сравните:

He was at work.
— Он был на работе.

He worked yesterday.
— Он работал вчера.""",
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
                "prompt": "We ___ at the cinema last night.",
                "options": ["was", "were", "are", "did"],
                "answer": "were",
                "explanation": "We → were.",
            },

            {
                "order": 2,
                "prompt": "My brother ___ ill yesterday.",
                "options": ["were", "was", "did", "is"],
                "answer": "was",
                "explanation": "My brother = he, поэтому was.",
            },

            {
                "order": 3,
                "prompt": "The children ___ hungry.",
                "options": ["was", "were", "is", "did"],
                "answer": "were",
                "explanation": "Children = they, поэтому were.",
            },

            {
                "order": 4,
                "prompt": "It ___ cold last week.",
                "options": ["were", "was", "did", "are"],
                "answer": "was",
                "explanation": "It → was.",
            },

            {
                "order": 5,
                "prompt": "I ___ not at work yesterday.",
                "options": ["were", "was", "did", "am"],
                "answer": "was",
                "explanation": "I → was: I was not at work.",
            },

            {
                "order": 6,
                "prompt": "They ___ not ready.",
                "options": ["was", "were", "did", "are"],
                "answer": "were",
                "explanation": "They → were.",
            },

            {
                "order": 7,
                "prompt": "___ your father at home?",
                "options": ["Did", "Was", "Were", "Does"],
                "answer": "Was",
                "explanation": "Your father = he, поэтому Was.",
            },

            {
                "order": 8,
                "prompt": "___ your parents at home?",
                "options": ["Was", "Were", "Did", "Are"],
                "answer": "Were",
                "explanation": "Parents = they, поэтому Were.",
            },

            {
                "order": 9,
                "prompt": "Was the lesson interesting?",
                "options": [
                    "Yes, it was.",
                    "Yes, it did.",
                    "Yes, it were.",
                    "Yes, it is.",
                ],
                "answer": "Yes, it was.",
                "explanation": "Вопрос с was требует краткий ответ с was.",
            },

            {
                "order": 10,
                "prompt": "Were the students tired?",
                "options": [
                    "No, they didn't.",
                    "No, they wasn't.",
                    "No, they weren't.",
                    "No, they aren't.",
                ],
                "answer": "No, they weren't.",
                "explanation": "Were they...? → No, they weren't.",
            },

            {
                "order": 11,
                "prompt": "Where ___ you yesterday?",
                "options": ["was", "were", "did", "are"],
                "answer": "were",
                "explanation": "You всегда используется с were.",
            },

            {
                "order": 12,
                "prompt": "Why ___ she late?",
                "options": ["were", "was", "did", "is"],
                "answer": "was",
                "explanation": "She → was.",
            },

            {
                "order": 13,
                "prompt": "How ___ your holiday?",
                "options": ["were", "was", "did", "is"],
                "answer": "was",
                "explanation": "Holiday — единственное число, поэтому was.",
            },

            {
                "order": 14,
                "prompt": "There ___ a problem.",
                "options": ["were", "was", "did", "have"],
                "answer": "was",
                "explanation": "Один problem → there was.",
            },

            {
                "order": 15,
                "prompt": "There ___ many people at the meeting.",
                "options": ["was", "were", "did", "is"],
                "answer": "were",
                "explanation": "Many people → there were.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "You was late.",
                    "You were late.",
                    "You did were late.",
                    "You were be late.",
                ],
                "answer": "You were late.",
                "explanation": "You всегда используется с were.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "She didn't was tired.",
                    "She wasn't tired.",
                    "She weren't tired.",
                    "She didn't be tired.",
                ],
                "answer": "She wasn't tired.",
                "explanation": "To be образует отрицание без did.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct question.",
                "options": [
                    "Did she was at home?",
                    "Was she at home?",
                    "Did she be at home?",
                    "She was at home?",
                ],
                "answer": "Was she at home?",
                "explanation": "Was ставится перед подлежащим; did не нужен.",
            },

            {
                "order": 19,
                "prompt": "I ___ born in Kazakhstan.",
                "options": ["were", "was", "did", "am"],
                "answer": "was",
                "explanation": "Правильная конструкция: I was born.",
            },

            {
                "order": 20,
                "prompt": "Where ___ you born?",
                "options": ["was", "were", "did", "are"],
                "answer": "were",
                "explanation": "You → were: Where were you born?",
            },

            {
                "order": 21,
                "prompt": "There wasn't ___ milk in the fridge.",
                "options": ["some", "any", "many", "a few"],
                "answer": "any",
                "explanation": "С отрицанием обычно используется any.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence about an action.",
                "options": [
                    "She was worked yesterday.",
                    "She worked yesterday.",
                    "She was work yesterday.",
                    "She did worked yesterday.",
                ],
                "answer": "She worked yesterday.",
                "explanation": "Work — действие; здесь нужен обычный Past Simple, не was.",
            },

            {
                "order": 23,
                "prompt": "Choose the sentence meaning 'Он был на работе вчера.'",
                "options": [
                    "He worked yesterday.",
                    "He was at work yesterday.",
                    "He was work yesterday.",
                    "He did at work yesterday.",
                ],
                "answer": "He was at work yesterday.",
                "explanation": "At work — место, поэтому используется was.",
            },

            {
                "order": 24,
                "prompt": "Two days ___, I was in Astana.",
                "options": ["last", "ago", "before ago", "yesterday"],
                "answer": "ago",
                "explanation": "Ago ставится после периода времени: two days ago.",
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
                "✅ A1 Lesson 24 seeded: "
                "Past Simple — WAS / WERE"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
