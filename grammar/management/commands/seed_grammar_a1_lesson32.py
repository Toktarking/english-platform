from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 32: "
        "Present Perfect Continuous."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=32,
            defaults={
                "title": "Present Perfect Continuous",
                "slug": "present-perfect-continuous",
                "theory_text": "Present Perfect Continuous.",
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Present Perfect Continuous",
                "body": """Present Perfect Continuous используется, когда действие:

началось в прошлом;

продолжалось некоторое время;

продолжается сейчас;

или только что закончилось, но результат заметен сейчас.

Примеры:

I have been working for three hours.

She has been studying since morning.

It has been raining.

Главная идея:

действие началось раньше и связано с настоящим.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Формула:

subject + have/has + been + verb-ing

Примеры:

I have been working.

She has been reading.

They have been waiting.

He has been sleeping.

Форма состоит из трёх частей:

have/has;

been;

глагол с -ing.""",
            },

            {
                "order": 3,
                "title": "HAVE BEEN и HAS BEEN",
                "body": """HAVE BEEN используется с:

I;

you;

we;

they.

Примеры:

I have been working.

We have been studying.

They have been talking.

HAS BEEN используется с:

he;

she;

it;

одним человеком или предметом.

He has been working.

She has been cooking.

It has been raining.""",
            },

            {
                "order": 4,
                "title": "Как образуется -ING",
                "body": """Обычный случай:

work → working

read → reading

play → playing

Глаголы на немую e:

write → writing

make → making

come → coming

Короткие глаголы:

sit → sitting

run → running

swim → swimming

Глаголы на -ie:

lie → lying

die → dying""",
            },

            {
                "order": 5,
                "title": "Действие продолжается сейчас",
                "body": """Present Perfect Continuous часто показывает действие, которое началось раньше и всё ещё продолжается.

Пример:

I have been working for three hours.

Это значит:

я начал работать три часа назад;

я всё ещё работаю.

Другие примеры:

She has been studying since morning.

We have been waiting for an hour.

He has been learning English for six months.""",
            },

            {
                "order": 6,
                "title": "FOR и SINCE",
                "body": """FOR показывает продолжительность.

for two hours

for five days

for ten years

Пример:

I have been working for two hours.

SINCE показывает начальную точку.

since Monday

since 2020

since morning

since five o'clock

Пример:

She has been studying since morning.

Запомните:

FOR = как долго

SINCE = с какого момента""",
            },

            {
                "order": 7,
                "title": "HOW LONG",
                "body": """Чтобы спросить о продолжительности:

How long have/has + subject + been + verb-ing?

Примеры:

How long have you been working?

How long has she been studying?

How long have they been waiting?

Ответы:

I have been working for three hours.

She has been living here since 2022.""",
            },

            {
                "order": 8,
                "title": "Действие только что закончилось",
                "body": """Present Perfect Continuous может описывать действие, которое недавно закончилось, но результат заметен сейчас.

Примеры:

You are wet. Have you been walking in the rain?

She is tired because she has been working.

His eyes are red because he has been crying.

The ground is wet because it has been raining.

You are out of breath. Have you been running?""",
            },

            {
                "order": 9,
                "title": "Акцент на процессе",
                "body": """Present Perfect Continuous подчёркивает:

процесс;

продолжительность;

временную деятельность.

Пример:

I have been reading for two hours.

Главное — процесс чтения и его длительность.

She has been writing a report.

Возможно, отчёт ещё не закончен.

Действие может продолжаться и сейчас.""",
            },

            {
                "order": 10,
                "title": "Отрицание и вопросы",
                "body": """Отрицание:

subject + haven't/hasn't been + verb-ing

I haven't been sleeping well.

She hasn't been working recently.

Вопрос:

Have/Has + subject + been + verb-ing?

Have you been working?

Has she been studying?

Краткие ответы:

Yes, I have.

No, I haven't.

Yes, she has.

No, she hasn't.""",
            },

            {
                "order": 11,
                "title": "Специальные вопросы",
                "body": """Формула:

Question word + have/has + subject + been + verb-ing?

Примеры:

What have you been doing?

Where has she been working?

Why have they been laughing?

How long has he been waiting?

Who have you been talking to?

Если WHO само выполняет действие:

Who has been using my computer?

Who has been calling me?""",
            },

            {
                "order": 12,
                "title": "Present Continuous и Present Perfect Continuous",
                "body": """Present Continuous показывает действие сейчас:

I am working now.

Present Perfect Continuous показывает, как долго действие продолжается:

I have been working for three hours.

Сравните:

She is studying now.
— она занимается сейчас.

She has been studying since morning.
— она занимается с утра до настоящего момента.""",
            },

            {
                "order": 13,
                "title": "Present Perfect или Present Perfect Continuous",
                "body": """Present Perfect чаще подчёркивает:

результат;

количество;

завершённость.

I have written three emails.

Present Perfect Continuous чаще подчёркивает:

процесс;

продолжительность.

I have been writing emails for two hours.

Сравните:

She has cleaned the room.
— комната убрана.

She has been cleaning the room.
— она занималась уборкой; возможно, ещё не закончила.""",
            },

            {
                "order": 14,
                "title": "Глаголы состояния и выбор времени",
                "body": """Глаголы состояния обычно не используются в Continuous.

Например:

know;

understand;

like;

want;

need;

believe;

own.

Правильно:

I have known him for ten years.

Не:

I have been knowing him.

HAVE как владение:

I have had this phone for two years.

Не:

I have been having this phone.

Главное правило:

важна длительность процесса → Present Perfect Continuous

важен готовый результат или состояние → Present Perfect""",
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
                "prompt": "We ___ been waiting for an hour.",
                "options": ["has", "have", "are", "did"],
                "answer": "have",
                "explanation": "We используется с have.",
            },

            {
                "order": 2,
                "prompt": "My brother ___ been working since morning.",
                "options": ["have", "has", "is", "does"],
                "answer": "has",
                "explanation": "My brother = he, поэтому has.",
            },

            {
                "order": 3,
                "prompt": "The children have been ___ outside.",
                "options": ["play", "played", "playing", "plays"],
                "answer": "playing",
                "explanation": "После been используется глагол с -ing.",
            },

            {
                "order": 4,
                "prompt": "She has been ___ English for six months.",
                "options": ["learn", "learned", "learning", "learns"],
                "answer": "learning",
                "explanation": "Present Perfect Continuous: has been + verb-ing.",
            },

            {
                "order": 5,
                "prompt": "I have been living here ___ five years.",
                "options": ["since", "for", "ago", "from"],
                "answer": "for",
                "explanation": "For показывает продолжительность.",
            },

            {
                "order": 6,
                "prompt": "He has been sleeping ___ noon.",
                "options": ["for", "since", "during", "ago"],
                "answer": "since",
                "explanation": "Noon — начальная точка, поэтому since.",
            },

            {
                "order": 7,
                "prompt": "___ they been working all day?",
                "options": ["Did", "Have", "Are", "Do"],
                "answer": "Have",
                "explanation": "They → Have they been working?",
            },

            {
                "order": 8,
                "prompt": "___ she been crying?",
                "options": ["Has", "Is", "Did", "Does"],
                "answer": "Has",
                "explanation": "She → Has she been crying?",
            },

            {
                "order": 9,
                "prompt": "How long ___ you been studying English?",
                "options": ["has", "have", "are", "did"],
                "answer": "have",
                "explanation": "You используется с have.",
            },

            {
                "order": 10,
                "prompt": "Why ___ he been running?",
                "options": ["have", "has", "is", "did"],
                "answer": "has",
                "explanation": "He используется с has.",
            },

            {
                "order": 11,
                "prompt": "I am tired because I ___ all day.",
                "options": [
                    "worked yesterday",
                    "have been working",
                    "have worked five tasks",
                    "was work",
                ],
                "answer": "have been working",
                "explanation": "Текущий результат вызван длительным процессом.",
            },

            {
                "order": 12,
                "prompt": "She ___ three emails.",
                "options": [
                    "has been writing for three",
                    "has written",
                    "has been written",
                    "has write",
                ],
                "answer": "has written",
                "explanation": "Указано количество готовых писем → Present Perfect.",
            },

            {
                "order": 13,
                "prompt": "She ___ emails for two hours.",
                "options": [
                    "has written five",
                    "has been writing",
                    "has been written",
                    "wrote now",
                ],
                "answer": "has been writing",
                "explanation": "For two hours подчёркивает длительность процесса.",
            },

            {
                "order": 14,
                "prompt": "I ___ him for ten years.",
                "options": [
                    "have been knowing",
                    "have known",
                    "knew and still know",
                    "am knowing",
                ],
                "answer": "have known",
                "explanation": "Know — глагол состояния, поэтому используется Present Perfect.",
            },

            {
                "order": 15,
                "prompt": "Has it been raining?",
                "options": [
                    "Yes, it has.",
                    "Yes, it is.",
                    "Yes, it did.",
                    "Yes, it was.",
                ],
                "answer": "Yes, it has.",
                "explanation": "Краткий ответ повторяет has.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I have been worked.",
                    "I have been working.",
                    "I have working.",
                    "I am been working.",
                ],
                "answer": "I have been working.",
                "explanation": "Формула: have been + verb-ing.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She has been work.",
                    "She has been working.",
                    "She has working.",
                    "She been working.",
                ],
                "answer": "She has been working.",
                "explanation": "Has been + working.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct question.",
                "options": [
                    "Did you been working?",
                    "Have you been working?",
                    "Have you been worked?",
                    "Are you been working?",
                ],
                "answer": "Have you been working?",
                "explanation": "Вопрос: Have + subject + been + verb-ing?",
            },

            {
                "order": 19,
                "prompt": "The ground is wet because it ___.",
                "options": [
                    "has been raining",
                    "has rained three times",
                    "was rain",
                    "has been rained",
                ],
                "answer": "has been raining",
                "explanation": "Видимый результат сейчас связан с недавним процессом.",
            },

            {
                "order": 20,
                "prompt": "Which sentence emphasizes a finished result?",
                "options": [
                    "I have been writing for two hours.",
                    "I have written five pages.",
                    "I am writing now.",
                    "I was writing yesterday.",
                ],
                "answer": "I have written five pages.",
                "explanation": "Количество готового результата → Present Perfect.",
            },

            {
                "order": 21,
                "prompt": "Which sentence emphasizes duration?",
                "options": [
                    "She has cleaned the room.",
                    "She has been cleaning the room for two hours.",
                    "She cleaned the room yesterday.",
                    "She is clean.",
                ],
                "answer": "She has been cleaning the room for two hours.",
                "explanation": "For two hours подчёркивает длительность процесса.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence with SINCE.",
                "options": [
                    "I have been working since three hours.",
                    "I have been working since Monday.",
                    "I have been working since two hours.",
                    "I have been working for Monday.",
                ],
                "answer": "I have been working since Monday.",
                "explanation": "Since используется с начальной точкой.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence about possession.",
                "options": [
                    "I have been having this phone for two years.",
                    "I have had this phone for two years.",
                    "I have been had this phone for two years.",
                    "I am having this phone since two years.",
                ],
                "answer": "I have had this phone for two years.",
                "explanation": "Have в значении владения обычно не используется в Continuous.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct pair.",
                "options": [
                    "I have written five emails. / I have been writing for two hours.",
                    "I have been written five emails. / I have writing for two hours.",
                    "I have wrote five emails. / I have been wrote for two hours.",
                    "I wrote five emails now. / I have been written for two hours.",
                ],
                "answer": "I have written five emails. / I have been writing for two hours.",
                "explanation": "Количество результата → Present Perfect; длительность процесса → Present Perfect Continuous.",
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
                "✅ A1 Lesson 32 seeded: "
                "Present Perfect Continuous"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
