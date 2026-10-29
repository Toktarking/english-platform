from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 33: "
        "Present Perfect vs Present Perfect Continuous."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=33,
            defaults={
                "title": (
                    "Present Perfect и "
                    "Present Perfect Continuous"
                ),
                "slug": "present-perfect-vs-perfect-continuous",
                "theory_text": (
                    "Present Perfect vs "
                    "Present Perfect Continuous."
                ),
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Главное различие",
                "body": """Оба времени связывают прошлое с настоящим, но показывают действие по-разному.

Present Perfect:

I have written five emails.

Важны результат и количество.

Present Perfect Continuous:

I have been writing emails for two hours.

Важны процесс и продолжительность.

Главный вопрос:

что важнее — результат или процесс?""",
            },

            {
                "order": 2,
                "title": "Present Perfect",
                "body": """Формула:

have/has + третья форма глагола

Используется, когда важны:

результат;

завершённость;

количество выполненных действий;

жизненный опыт;

состояние до настоящего момента.

Примеры:

I have finished the report.

She has written three pages.

They have visited London.

We have known each other for years.""",
            },

            {
                "order": 3,
                "title": "Present Perfect Continuous",
                "body": """Формула:

have/has been + verb-ing

Используется, когда важны:

процесс;

продолжительность;

временное действие;

действие, которое продолжается сейчас;

видимый результат недавнего процесса.

Примеры:

I have been writing for two hours.

She has been studying since morning.

They have been waiting.

It has been raining.""",
            },

            {
                "order": 4,
                "title": "Готовый результат или процесс",
                "body": """Сравните:

I have cleaned the room.

Комната уже убрана.

Важен результат.

I have been cleaning the room.

Важно, что я занимался уборкой.

Возможно:

уборка ещё продолжается;

уборка только что закончилась;

комната ещё не полностью убрана.""",
            },

            {
                "order": 5,
                "title": "Количество или продолжительность",
                "body": """Если указано количество готовых результатов:

Present Perfect.

I have written five emails.

She has read three books.

They have completed ten tasks.

Если указана длительность процесса:

Present Perfect Continuous.

I have been writing for two hours.

She has been reading since morning.

They have been working all day.

Простое правило:

Сколько сделано? → Present Perfect

Как долго? → Present Perfect Continuous""",
            },

            {
                "order": 6,
                "title": "Завершено или ещё продолжается",
                "body": """Present Perfect часто показывает завершённость:

I have finished the report.

She has cooked dinner.

He has read the book.

Present Perfect Continuous часто показывает процесс:

I have been writing the report.

She has been cooking dinner.

He has been reading the book.

Но Continuous может описывать и только что завершившийся процесс:

I am tired because I have been working all day.""",
            },

            {
                "order": 7,
                "title": "Видимый результат сейчас",
                "body": """Present Perfect Continuous часто используется, если сейчас видны следы действия.

Примеры:

Your clothes are dirty.
Have you been working in the garden?

Her eyes are red.
She has been crying.

The ground is wet.
It has been raining.

You are out of breath.
Have you been running?

Здесь важен процесс, который привёл к результату сейчас.""",
            },

            {
                "order": 8,
                "title": "FOR, SINCE и длительные глаголы",
                "body": """Оба времени могут использоваться с FOR и SINCE.

Например с:

live;

work;

study;

teach.

Present Perfect:

I have worked here for five years.

Подчёркивается факт.

Present Perfect Continuous:

I have been working here for five years.

Подчёркивается длительность процесса.

Оба варианта могут быть правильными.""",
            },

            {
                "order": 9,
                "title": "Глаголы состояния",
                "body": """Глаголы состояния обычно не используются в Continuous.

Например:

know;

understand;

like;

love;

want;

need;

believe;

remember;

own;

belong;

prefer.

Правильно:

I have known him for ten years.

He has owned the house since 2021.

Неправильно:

I have been knowing him.

He has been owning the house.""",
            },

            {
                "order": 10,
                "title": "HAVE и THINK",
                "body": """HAVE как владение:

Present Perfect.

I have had this phone for two years.

Не:

I have been having this phone.

Но HAVE как действие может быть Continuous:

I have been having problems with my computer.

THINK как мнение:

I have always thought he was right.

THINK как процесс размышления:

I have been thinking about your idea.""",
            },

            {
                "order": 11,
                "title": "READ, WRITE, CLEAN, REPAIR",
                "body": """Сравните результат и процесс.

READ:

I have read the book.
— книга прочитана.

I have been reading the book.
— я читал её некоторое время.

WRITE:

She has written the report.
— отчёт готов.

She has been writing the report.
— процесс написания.

CLEAN:

They have cleaned the house.
— дом убран.

They have been cleaning the house.
— занимались уборкой.""",
            },

            {
                "order": 12,
                "title": "Маркеры двух времён",
                "body": """С Present Perfect часто встречаются:

already;

just;

yet;

ever;

never;

so far;

three times;

five books;

many tasks.

С Present Perfect Continuous:

for;

since;

all day;

all morning;

lately;

recently;

how long.

Но маркер — это подсказка.

Главное — смысл предложения.""",
            },

            {
                "order": 13,
                "title": "HOW MANY и HOW LONG",
                "body": """HOW MANY обычно спрашивает о результате.

How many emails have you written?

How many books has she read?

HOW LONG спрашивает о длительности.

How long have you been writing?

How long has she been reading?

Сравните:

How many pages have you written?
— сколько готово?

How long have you been writing?
— как долго длится процесс?""",
            },

            {
                "order": 14,
                "title": "Как выбрать время",
                "body": """Шаг 1.

Важен готовый результат?

→ Present Perfect

I have finished the work.

Шаг 2.

Важен процесс?

→ Present Perfect Continuous

I have been working for three hours.

Шаг 3.

Указано количество?

→ Present Perfect

She has written six pages.

Шаг 4.

Указана длительность?

→ чаще Present Perfect Continuous

She has been writing for two hours.

Шаг 5.

Это глагол состояния?

→ Present Perfect

I have known him for years.""",
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
                "prompt": "I ___ the report. It is ready.",
                "options": [
                    "have finished",
                    "have been finishing",
                    "have finish",
                    "am finished",
                ],
                "answer": "have finished",
                "explanation": "Отчёт готов — важен завершённый результат.",
            },

            {
                "order": 2,
                "prompt": "I ___ on the report all morning.",
                "options": [
                    "have finished",
                    "have been working",
                    "have worked three reports",
                    "worked since",
                ],
                "answer": "have been working",
                "explanation": "All morning подчёркивает длительный процесс.",
            },

            {
                "order": 3,
                "prompt": "She ___ four pages.",
                "options": [
                    "has written",
                    "has been writing for four",
                    "has wrote",
                    "is writing since",
                ],
                "answer": "has written",
                "explanation": "Four pages — количество готового результата.",
            },

            {
                "order": 4,
                "prompt": "She ___ for two hours.",
                "options": [
                    "has written four pages",
                    "has been writing",
                    "has writing",
                    "wrote since",
                ],
                "answer": "has been writing",
                "explanation": "For two hours → длительность процесса.",
            },

            {
                "order": 5,
                "prompt": "They ___ the house. It looks much better now.",
                "options": [
                    "have painted",
                    "have been painting only",
                    "have paint",
                    "painted since",
                ],
                "answer": "have painted",
                "explanation": "Важен готовый результат.",
            },

            {
                "order": 6,
                "prompt": "Their clothes are dirty because they ___ the house.",
                "options": [
                    "have painted the whole house",
                    "have been painting",
                    "have been painted",
                    "have painting",
                ],
                "answer": "have been painting",
                "explanation": "Грязная одежда — видимый результат недавнего процесса.",
            },

            {
                "order": 7,
                "prompt": "He ___ me six times today.",
                "options": [
                    "has called",
                    "has been calling six",
                    "has call",
                    "is calling since",
                ],
                "answer": "has called",
                "explanation": "Six times — количество завершённых действий.",
            },

            {
                "order": 8,
                "prompt": "He ___ me all morning.",
                "options": [
                    "has called once",
                    "has been calling",
                    "has been called",
                    "called since",
                ],
                "answer": "has been calling",
                "explanation": "All morning подчёркивает процесс.",
            },

            {
                "order": 9,
                "prompt": "We ___ each other since childhood.",
                "options": [
                    "have been knowing",
                    "have known",
                    "are knowing",
                    "have know",
                ],
                "answer": "have known",
                "explanation": "Know — глагол состояния.",
            },

            {
                "order": 10,
                "prompt": "She ___ here for five years.",
                "options": [
                    "has worked",
                    "has been working",
                    "both A and B are possible",
                    "worked and still works only",
                ],
                "answer": "both A and B are possible",
                "explanation": "С work возможны обе формы; Continuous сильнее подчёркивает длительность.",
            },

            {
                "order": 11,
                "prompt": "How many books ___ you ___ this year?",
                "options": [
                    "have / read",
                    "have / been reading",
                    "did / read since",
                    "are / reading",
                ],
                "answer": "have / read",
                "explanation": "How many спрашивает количество результатов.",
            },

            {
                "order": 12,
                "prompt": "How long ___ you ___ this book?",
                "options": [
                    "have / read completely",
                    "have / been reading",
                    "did / been reading",
                    "are / read",
                ],
                "answer": "have / been reading",
                "explanation": "How long спрашивает длительность процесса.",
            },

            {
                "order": 13,
                "prompt": "The ground is wet because it ___.",
                "options": [
                    "has rained once",
                    "has been raining",
                    "has rain",
                    "rained since",
                ],
                "answer": "has been raining",
                "explanation": "Видимый результат связан с продолжающимся или недавним процессом.",
            },

            {
                "order": 14,
                "prompt": "The rain ___, so we can go outside now.",
                "options": [
                    "has stopped",
                    "has been stopping",
                    "has stop",
                    "is stopped",
                ],
                "answer": "has stopped",
                "explanation": "Важен завершённый результат: дождь прекратился.",
            },

            {
                "order": 15,
                "prompt": "I ___ this phone for two years.",
                "options": [
                    "have been having",
                    "have had",
                    "am having",
                    "have have",
                ],
                "answer": "have had",
                "explanation": "Have в значении владения не используется в Continuous.",
            },

            {
                "order": 16,
                "prompt": "Choose the sentence emphasizing a finished result.",
                "options": [
                    "I have been reading the book.",
                    "I have read the book.",
                    "I have been read the book.",
                    "I am reading the book since Monday.",
                ],
                "answer": "I have read the book.",
                "explanation": "Present Perfect показывает, что книга прочитана.",
            },

            {
                "order": 17,
                "prompt": "Choose the sentence emphasizing the process.",
                "options": [
                    "She has written the report.",
                    "She has been writing the report.",
                    "She has been written the report.",
                    "She has wrote the report.",
                ],
                "answer": "She has been writing the report.",
                "explanation": "Present Perfect Continuous подчёркивает процесс.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I have been knowing her for years.",
                    "I have known her for years.",
                    "I am knowing her for years.",
                    "I have know her for years.",
                ],
                "answer": "I have known her for years.",
                "explanation": "Know — глагол состояния.",
            },

            {
                "order": 19,
                "prompt": "Choose the correct question about quantity.",
                "options": [
                    "How long have you written?",
                    "How many emails have you written?",
                    "How many emails have you been writing for?",
                    "How much have you been written?",
                ],
                "answer": "How many emails have you written?",
                "explanation": "Количество завершённых результатов → Present Perfect.",
            },

            {
                "order": 20,
                "prompt": "Choose the correct question about duration.",
                "options": [
                    "How many hours have you written?",
                    "How long have you been writing?",
                    "How long have you written five pages?",
                    "How long did you been writing?",
                ],
                "answer": "How long have you been writing?",
                "explanation": "Продолжительность процесса → Present Perfect Continuous.",
            },

            {
                "order": 21,
                "prompt": "I ___ about your idea all day.",
                "options": [
                    "have thought one idea",
                    "have been thinking",
                    "have been thought",
                    "am thought",
                ],
                "answer": "have been thinking",
                "explanation": "Think в значении процесса размышления может использоваться в Continuous.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She has working all day.",
                    "She has been working all day.",
                    "She has been worked all day.",
                    "She have been work all day.",
                ],
                "answer": "She has been working all day.",
                "explanation": "Формула: has been + verb-ing.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct pair.",
                "options": [
                    "I have written five emails. / I have been writing for two hours.",
                    "I have been writing five emails. / I have written for two hours.",
                    "I have wrote five emails. / I have been wrote for two hours.",
                    "I have been written five emails. / I have writing for two hours.",
                ],
                "answer": "I have written five emails. / I have been writing for two hours.",
                "explanation": "Количество → Present Perfect; длительность → Present Perfect Continuous.",
            },

            {
                "order": 24,
                "prompt": "Choose the best pair.",
                "options": [
                    "She has cleaned the room. / She has been cleaning the room.",
                    "She has been cleaned the room. / She has cleaning the room.",
                    "She has clean the room. / She has been clean the room.",
                    "She cleaned since morning. / She has cleaning since morning.",
                ],
                "answer": "She has cleaned the room. / She has been cleaning the room.",
                "explanation": "Первая форма подчёркивает результат, вторая — процесс.",
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
                "✅ A1 Lesson 33 seeded: "
                "Present Perfect vs Present Perfect Continuous"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
