from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 10: "
        "Present tense of TO BE."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=10,
            defaults={
                "title": (
                    "Глагол TO BE в настоящем времени: "
                    "AM, IS, ARE"
                ),
                "slug": "to-be-am-is-are",
                "theory_text": (
                    "Present tense of TO BE: "
                    "am, is, are."
                ),
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое TO BE",
                "body": """Глагол to be может означать:

быть;
находиться;
являться.

В русском языке в настоящем времени мы часто его не произносим:

Я студент.
Она дома.
Они заняты.

Но в английском языке to be обязателен:

I am a student.

She is at home.

They are busy.

Неправильно:

I a student.

She at home.

They busy.""",
            },

            {
                "order": 2,
                "title": "Главная таблица AM, IS, ARE",
                "body": """Запомните три основные группы:

I → am

he / she / it → is

you / we / they → are

Полная таблица:

I am

you are

he is

she is

it is

we are

they are

Это основа всего урока.""",
            },

            {
                "order": 3,
                "title": "Когда используется AM",
                "body": """Am используется только с I.

Примеры:

I am a teacher.

I am tired.

I am at home.

Нельзя:

I is.

I are.

Правильно только:

I am.""",
            },

            {
                "order": 4,
                "title": "Когда используется IS",
                "body": """Is используется с:

he;
she;
it;
одним человеком;
одним предметом.

Примеры:

He is a doctor.

She is busy.

It is cold.

Marat is at work.

The book is interesting.

Если подлежащее можно заменить на he, she или it, обычно используется is.""",
            },

            {
                "order": 5,
                "title": "Когда используется ARE",
                "body": """Are используется с:

you;
we;
they;
несколькими людьми;
несколькими предметами.

Примеры:

You are my friend.

We are ready.

They are students.

Marat and Aigul are at home.

The books are new.

Если подлежащее можно заменить на they, обычно используется are.""",
            },

            {
                "order": 6,
                "title": "Когда нужен TO BE",
                "body": """To be часто используется, когда после него стоит:

профессия;

прилагательное или состояние;

местонахождение;

возраст;

национальность или происхождение.

Профессия:

I am a teacher.

He is a doctor.

Состояние:

She is happy.

We are ready.

Место:

She is at work.

The children are in the garden.

Возраст:

My son is one year old.

Национальность:

I am Kazakh.

She is British.""",
            },

            {
                "order": 7,
                "title": "Погода, время и возраст",
                "body": """С погодой обычно используется it is:

It is cold.

It is hot.

It is sunny.

It is windy.

Со временем:

It is five o'clock.

It is late.

Возраст в английском выражается через to be:

I am twenty years old.

She is ten.

My son is one year old.

Неправильно:

I have twenty years.

Правильно:

I am twenty years old.""",
            },

            {
                "order": 8,
                "title": "Утвердительные предложения",
                "body": """Формула:

Подлежащее + am / is / are + остальная часть предложения.

Примеры:

I am a student.

She is happy.

They are at home.

С именами:

Marat is a teacher.

Aigul is at home.

С множественным числом:

Marat and Aigul are teachers.

The children are outside.

Также:

This is my book.

That is our house.

These are my keys.

Those are their children.""",
            },

            {
                "order": 9,
                "title": "Сокращённые формы",
                "body": """В разговорной речи часто используются сокращения:

I am → I'm

you are → you're

he is → he's

she is → she's

it is → it's

we are → we're

they are → they're

Примеры:

I'm tired.

You're late.

He's a doctor.

She's at home.

It's cold.

We're ready.

They're busy.

Полные и сокращённые формы имеют одинаковое значение.""",
            },

            {
                "order": 10,
                "title": "Отрицание",
                "body": """Чтобы сделать предложение отрицательным, после am/is/are ставится not.

Формула:

Подлежащее + am/is/are + not

Примеры:

I am not tired.

He is not at home.

They are not ready.

Сокращения:

I'm not;

isn't;

aren't.

Примеры:

He isn't tired.

They aren't ready.

Важно:

формы I amn't в стандартном английском нет.

Правильно:

I'm not.""",
            },

            {
                "order": 11,
                "title": "Общие вопросы",
                "body": """В вопросе am/is/are ставится перед подлежащим.

Утверждение:

She is at home.

Вопрос:

Is she at home?

Формула:

Am / Is / Are + подлежащее + ... ?

Примеры:

Am I late?

Is he a doctor?

Is she at work?

Is it cold?

Are you ready?

Are they students?

Are the children outside?""",
            },

            {
                "order": 12,
                "title": "Краткие ответы",
                "body": """Краткие ответы:

Are you tired?

Yes, I am.

No, I'm not.

Is he at home?

Yes, he is.

No, he isn't.

Are they ready?

Yes, they are.

No, they aren't.

Важно:

в положительном кратком ответе обычно не используется сокращение.

Неправильно:

Yes, I'm.

Yes, he's.

Правильно:

Yes, I am.

Yes, he is.""",
            },

            {
                "order": 13,
                "title": "Специальные вопросы",
                "body": """Специальный вопрос начинается с вопросительного слова.

Основные слова:

who — кто;

what — что / какой;

where — где;

how old — сколько лет;

why — почему;

how — как.

Формула:

Вопросительное слово + am/is/are + подлежащее?

Примеры:

Where are you?

Where is the book?

How old is she?

How old are they?

Why are they late?

What is this?

Who is he?

Who are they?""",
            },

            {
                "order": 14,
                "title": "TO BE или обычный глагол",
                "body": """Очень важно не ставить am/is/are перед обычным смысловым глаголом.

TO BE:

He is a teacher.

She is tired.

She is at home.

She is thirty.

She is British.

Обычное действие:

I work at a university.

She speaks English.

They live in Astana.

Неправильно:

I am work at a university.

She is speaks English.

They are live in Astana.

Сравните:

He is a teacher.
— Teacher — профессия.

He works at a school.
— Works — действие.

She is tired.
— Tired — состояние.

She works hard.
— Works — действие.""",
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
                "prompt": "I ___ a teacher.",
                "options": ["is", "are", "am", "be"],
                "answer": "am",
                "explanation": "С местоимением I используется только am.",
            },

            {
                "order": 2,
                "prompt": "She ___ at home.",
                "options": ["am", "is", "are", "be"],
                "answer": "is",
                "explanation": "She → is.",
            },

            {
                "order": 3,
                "prompt": "They ___ ready.",
                "options": ["is", "am", "are", "be"],
                "answer": "are",
                "explanation": "They → are.",
            },

            {
                "order": 4,
                "prompt": "The book ___ interesting.",
                "options": ["am", "are", "is", "be"],
                "answer": "is",
                "explanation": "Book — один предмет, поэтому is.",
            },

            {
                "order": 5,
                "prompt": "The students ___ in the classroom.",
                "options": ["is", "am", "are", "be"],
                "answer": "are",
                "explanation": "Students — множественное число.",
            },

            {
                "order": 6,
                "prompt": "I ___ not tired.",
                "options": ["am", "is", "are", "do"],
                "answer": "am",
                "explanation": "Правильно: I am not tired.",
            },

            {
                "order": 7,
                "prompt": "___ she a doctor?",
                "options": ["Am", "Are", "Is", "Does"],
                "answer": "Is",
                "explanation": "В вопросе с she форма is ставится перед подлежащим.",
            },

            {
                "order": 8,
                "prompt": "___ they at home?",
                "options": ["Is", "Are", "Am", "Do"],
                "answer": "Are",
                "explanation": "They → are, поэтому Are they...?",
            },

            {
                "order": 9,
                "prompt": "Are you ready?",
                "options": [
                    "Yes, I'm.",
                    "Yes, I am.",
                    "Yes, you are.",
                    "Yes, I is.",
                ],
                "answer": "Yes, I am.",
                "explanation": "В положительном кратком ответе используется полная форма: Yes, I am.",
            },

            {
                "order": 10,
                "prompt": "Where ___ your children?",
                "options": ["is", "am", "are", "be"],
                "answer": "are",
                "explanation": "Children — множественное число.",
            },

            {
                "order": 11,
                "prompt": "I ___ from Kazakhstan.",
                "options": ["is", "are", "am", "be"],
                "answer": "am",
                "explanation": "I → am.",
            },

            {
                "order": 12,
                "prompt": "My wife ___ a teacher.",
                "options": ["are", "is", "am", "be"],
                "answer": "is",
                "explanation": "My wife — один человек, she → is.",
            },

            {
                "order": 13,
                "prompt": "My parents ___ at home.",
                "options": ["is", "am", "are", "be"],
                "answer": "are",
                "explanation": "Parents — множественное число.",
            },

            {
                "order": 14,
                "prompt": "The weather ___ cold today.",
                "options": ["are", "is", "am", "be"],
                "answer": "is",
                "explanation": "Weather — единственное число: the weather is cold.",
            },

            {
                "order": 15,
                "prompt": "These books ___ mine.",
                "options": ["is", "are", "am", "be"],
                "answer": "are",
                "explanation": "These books — множественное число.",
            },

            {
                "order": 16,
                "prompt": "He ___ not at work today.",
                "options": ["are", "am", "is", "do"],
                "answer": "is",
                "explanation": "He → is: He is not...",
            },

            {
                "order": 17,
                "prompt": "___ your sister a doctor?",
                "options": ["Are", "Is", "Am", "Do"],
                "answer": "Is",
                "explanation": "Your sister — один человек, поэтому Is.",
            },

            {
                "order": 18,
                "prompt": "How old ___ your son?",
                "options": ["are", "is", "am", "do"],
                "answer": "is",
                "explanation": "Your son — один человек: How old is your son?",
            },

            {
                "order": 19,
                "prompt": "Where ___ my keys?",
                "options": ["is", "am", "are", "does"],
                "answer": "are",
                "explanation": "Keys — множественное число.",
            },

            {
                "order": 20,
                "prompt": "Is Marat at home?",
                "options": [
                    "Yes, he is.",
                    "Yes, he's.",
                    "Yes, he are.",
                    "Yes, it is.",
                ],
                "answer": "Yes, he is.",
                "explanation": "В кратком положительном ответе: Yes, he is.",
            },

            {
                "order": 21,
                "prompt": "Are the students ready?",
                "options": [
                    "No, they is not.",
                    "No, they aren't.",
                    "No, they not.",
                    "No, they isn't.",
                ],
                "answer": "No, they aren't.",
                "explanation": "Students → they → are. Отрицательный ответ: No, they aren't.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She is speaks English.",
                    "She are speak English.",
                    "She speaks English.",
                    "She is speak English.",
                ],
                "answer": "She speaks English.",
                "explanation": "Speaks — обычный смысловой глагол, поэтому is перед ним не нужен.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence about age.",
                "options": [
                    "I have twenty years.",
                    "I am twenty years old.",
                    "I is twenty years old.",
                    "I do twenty years old.",
                ],
                "answer": "I am twenty years old.",
                "explanation": "Возраст в английском выражается через to be.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct question.",
                "options": [
                    "She is at home?",
                    "Does she is at home?",
                    "Is she at home?",
                    "Are she at home?",
                ],
                "answer": "Is she at home?",
                "explanation": "В вопросе is ставится перед подлежащим.",
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
                "✅ A1 Lesson 10 seeded: "
                "TO BE — AM, IS, ARE"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
