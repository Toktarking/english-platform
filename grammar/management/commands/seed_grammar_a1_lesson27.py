from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 27: "
        "Past Simple complete review."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=27,
            defaults={
                "title": "Past Simple: полное обобщение",
                "slug": "past-simple-complete-review",
                "theory_text": "Complete review of Past Simple.",
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Три системы Past Simple",
                "body": """Past Simple используется для действий и состояний, которые:

произошли в прошлом;

завершились в прошлом;

не продолжаются сейчас;

относятся к конкретному периоду прошлого.

В Past Simple есть три основные системы:

1. WAS / WERE — глагол to be;

2. правильные глаголы с -ed;

3. неправильные глаголы со второй формой.

Примеры:

I was tired.

I worked yesterday.

I went home.""",
            },

            {
                "order": 2,
                "title": "Когда используется Past Simple",
                "body": """Past Simple используется для завершённых действий:

I finished the report yesterday.

She called me last night.

Для конкретного момента:

He arrived at six.

We met in 2023.

Для последовательности:

I woke up, had breakfast and went to work.

Для привычек в прошлом:

I played outside every day when I was a child.

Для состояния:

I was tired.

They were students.""",
            },

            {
                "order": 3,
                "title": "Слова-маркеры",
                "body": """Частые слова и выражения:

yesterday;

last night;

last week;

last month;

last year;

two days ago;

five years ago;

in 2020;

when I was a child;

then;

after that.

Примеры:

I worked yesterday.

She went home last night.

They moved here three years ago.""",
            },

            {
                "order": 4,
                "title": "WAS / WERE",
                "body": """Используйте WAS / WERE для:

состояния;

места;

профессии;

возраста.

I / he / she / it → WAS

you / we / they → WERE

Примеры:

I was busy.

She was at work.

You were late.

They were happy.

Отрицание:

wasn't / weren't

Вопрос:

Was she tired?

Were they ready?""",
            },

            {
                "order": 5,
                "title": "Правильные глаголы",
                "body": """Правильные глаголы обычно получают окончание -ed.

work → worked

play → played

clean → cleaned

watch → watched

Если глагол заканчивается на e:

live → lived

Согласная + y:

study → studied

Гласная + y:

play → played

Короткий CVC-глагол:

stop → stopped""",
            },

            {
                "order": 6,
                "title": "Неправильные глаголы",
                "body": """Неправильные глаголы нужно запоминать.

Примеры:

go → went

come → came

see → saw

have → had

do → did

take → took

get → got

make → made

buy → bought

find → found

write → wrote

eat → ate

drink → drank

speak → spoke

sleep → slept""",
            },

            {
                "order": 7,
                "title": "Утвердительные предложения",
                "body": """С правильным глаголом:

subject + verb-ed

I worked yesterday.

She studied English.

С неправильным глаголом:

subject + Past Simple form

I went home.

She saw him.

С to be:

subject + was/were

She was tired.

They were at home.

Форма обычного глагола одинакова для всех лиц.""",
            },

            {
                "order": 8,
                "title": "Отрицание",
                "body": """С обычными глаголами:

subject + didn't + base verb

I didn't work.

She didn't study.

They didn't go.

He didn't see her.

После didn't всегда первая форма:

worked → didn't work

went → didn't go

saw → didn't see

Но с TO BE:

I wasn't tired.

They weren't ready.

Нельзя:

didn't was

didn't were""",
            },

            {
                "order": 9,
                "title": "Общие вопросы",
                "body": """С обычным глаголом:

Did + subject + base verb?

Did you work yesterday?

Did she study English?

Did they go home?

После DID — первая форма.

Не:

Did she worked?

Не:

Did they went?

С TO BE:

Was she tired?

Were they at home?

DID с was/were не используется.""",
            },

            {
                "order": 10,
                "title": "Краткие ответы",
                "body": """С обычным глаголом:

Did you work?

Yes, I did.

No, I didn't.

Did she go?

Yes, she did.

No, she didn't.

С TO BE:

Was she busy?

Yes, she was.

No, she wasn't.

Were they ready?

Yes, they were.

No, they weren't.""",
            },

            {
                "order": 11,
                "title": "Специальные вопросы",
                "body": """С обычным глаголом:

Question word + did + subject + base verb?

Where did you work?

When did she arrive?

Why did they leave?

What did he buy?

Who did you call?

Но если WHO само является подлежащим:

Who called you?

Who came yesterday?

Who wrote this message?

DID тогда не нужен.""",
            },

            {
                "order": 12,
                "title": "Состояние или действие",
                "body": """Сначала определите: это состояние или действие?

Состояние / место / роль:

She was tired.

They were at home.

He was a doctor.

Действие:

She worked.

They went home.

He studied medicine.

Сравните:

She was at work.
— Она была на работе.

She worked.
— Она работала.

Нельзя:

She was worked.""",
            },

            {
                "order": 13,
                "title": "HAD и DID",
                "body": """Утверждение:

I had breakfast.

She had a car.

Отрицание:

I didn't have breakfast.

She didn't have a car.

Вопрос:

Did you have breakfast?

Did she have a car?

Не:

didn't had

Не:

Did she had...?

Также:

I did my homework.

I didn't do my homework.

Did you do your homework?

Здесь did может быть и основным, и вспомогательным глаголом.""",
            },

            {
                "order": 14,
                "title": "Главный алгоритм выбора",
                "body": """Шаг 1.

Это состояние, место, профессия или возраст?

→ WAS / WERE

She was tired.

Шаг 2.

Это действие?

→ используйте Past Simple глагола.

Правильный:

worked

Неправильный:

went

Шаг 3.

Это отрицание?

→ didn't + первая форма

She didn't work.

She didn't go.

Шаг 4.

Это вопрос?

→ Did + subject + первая форма?

Did she work?

Did she go?

Но с TO BE:

Was she tired?""",
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
                "prompt": "We ___ busy yesterday.",
                "options": ["was", "were", "did", "worked"],
                "answer": "were",
                "explanation": "Busy — состояние; we → were.",
            },

            {
                "order": 2,
                "prompt": "My sister ___ me last night.",
                "options": [
                    "called",
                    "call",
                    "did called",
                    "was call",
                ],
                "answer": "called",
                "explanation": "Call — правильный глагол: called.",
            },

            {
                "order": 3,
                "prompt": "They ___ to the cinema.",
                "options": [
                    "went",
                    "goed",
                    "did went",
                    "were go",
                ],
                "answer": "went",
                "explanation": "Go → went.",
            },

            {
                "order": 4,
                "prompt": "He ___ breakfast at seven.",
                "options": [
                    "had",
                    "haved",
                    "have",
                    "did had",
                ],
                "answer": "had",
                "explanation": "Have → had.",
            },

            {
                "order": 5,
                "prompt": "I ___ not tired.",
                "options": [
                    "did",
                    "wasn't",
                    "didn't be",
                    "weren't",
                ],
                "answer": "wasn't",
                "explanation": "Tired — состояние; I → wasn't.",
            },

            {
                "order": 6,
                "prompt": "She didn't ___ English.",
                "options": [
                    "studied",
                    "study",
                    "studies",
                    "studying",
                ],
                "answer": "study",
                "explanation": "После didn't используется первая форма.",
            },

            {
                "order": 7,
                "prompt": "They didn't ___ the answer.",
                "options": [
                    "knew",
                    "know",
                    "known",
                    "knowing",
                ],
                "answer": "know",
                "explanation": "После didn't → know.",
            },

            {
                "order": 8,
                "prompt": "___ you at work yesterday?",
                "options": ["Did", "Was", "Were", "Are"],
                "answer": "Were",
                "explanation": "At work — место; you → were.",
            },

            {
                "order": 9,
                "prompt": "___ she call you?",
                "options": ["Was", "Did", "Were", "Does"],
                "answer": "Did",
                "explanation": "Call — обычный глагол, поэтому используется Did.",
            },

            {
                "order": 10,
                "prompt": "Did they ___ home?",
                "options": ["went", "go", "gone", "going"],
                "answer": "go",
                "explanation": "После did используется первая форма go.",
            },

            {
                "order": 11,
                "prompt": "Where ___ you yesterday?",
                "options": ["did", "was", "were", "are"],
                "answer": "were",
                "explanation": "Вопрос о месте с TO BE: Where were you?",
            },

            {
                "order": 12,
                "prompt": "Where did she ___?",
                "options": ["worked", "work", "works", "working"],
                "answer": "work",
                "explanation": "После did используется base form.",
            },

            {
                "order": 13,
                "prompt": "What did he ___?",
                "options": ["bought", "buy", "buys", "buying"],
                "answer": "buy",
                "explanation": "После did → buy.",
            },

            {
                "order": 14,
                "prompt": "Who ___ this message?",
                "options": [
                    "did write",
                    "wrote",
                    "write",
                    "written",
                ],
                "answer": "wrote",
                "explanation": "Who является подлежащим, поэтому did не нужен.",
            },

            {
                "order": 15,
                "prompt": "Were they ready?",
                "options": [
                    "Yes, they did.",
                    "Yes, they were.",
                    "Yes, they was.",
                    "Yes, they are.",
                ],
                "answer": "Yes, they were.",
                "explanation": "Вопрос с were → Yes, they were.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "She didn't went home.",
                    "She didn't go home.",
                    "She wasn't go home.",
                    "She didn't gone home.",
                ],
                "answer": "She didn't go home.",
                "explanation": "После didn't неправильный глагол возвращается в первую форму.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct question.",
                "options": [
                    "Did he went home?",
                    "Did he go home?",
                    "Was he go home?",
                    "Did he gone home?",
                ],
                "answer": "Did he go home?",
                "explanation": "После did используется первая форма.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She was worked yesterday.",
                    "She worked yesterday.",
                    "She did worked yesterday.",
                    "She was work yesterday.",
                ],
                "answer": "She worked yesterday.",
                "explanation": "Work — действие, поэтому нужен обычный Past Simple.",
            },

            {
                "order": 19,
                "prompt": "Choose the correct sentence about a state.",
                "options": [
                    "She worked tired yesterday.",
                    "She was tired yesterday.",
                    "She did tired yesterday.",
                    "She tired yesterday.",
                ],
                "answer": "She was tired yesterday.",
                "explanation": "Tired — состояние; используется was.",
            },

            {
                "order": 20,
                "prompt": "I ___ breakfast and then I went to work.",
                "options": ["had", "haved", "have", "did had"],
                "answer": "had",
                "explanation": "Have → had.",
            },

            {
                "order": 21,
                "prompt": "I didn't ___ breakfast.",
                "options": ["had", "have", "having", "has"],
                "answer": "have",
                "explanation": "После didn't используется have.",
            },

            {
                "order": 22,
                "prompt": "Did you ___ your homework?",
                "options": ["did", "do", "done", "doing"],
                "answer": "do",
                "explanation": "Первое did — вспомогательное; основной глагол остаётся do.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct pair.",
                "options": [
                    "She went. / She didn't went.",
                    "She went. / She didn't go.",
                    "She go. / She didn't went.",
                    "She was went. / She didn't go.",
                ],
                "answer": "She went. / She didn't go.",
                "explanation": "Вторая форма только в утверждении; после didn't — первая.",
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    "She was tired. / Was she tired? / Yes, she was.",
                    "She was tired. / Did she was tired? / Yes, she did.",
                    "She tired. / Was she tired? / Yes, she did.",
                    "She was tired. / Was she tired? / Yes, she did.",
                ],
                "answer": "She was tired. / Was she tired? / Yes, she was.",
                "explanation": "TO BE образует вопрос и ответ без did.",
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
                "✅ A1 Lesson 27 seeded: "
                "Past Simple — complete review"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
