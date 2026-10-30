from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 31: "
        "Present Perfect vs Past Simple."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=31,
            defaults={
                "title": "Present Perfect и Past Simple",
                "slug": "present-perfect-vs-past-simple",
                "theory_text": (
                    "Present Perfect vs Past Simple."
                ),
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Главное различие",
                "body": """Present Perfect и Past Simple могут говорить о прошлом, но смысл разный.

Present Perfect:

I have seen this film.

Важно, что у меня есть такой опыт сейчас.

Past Simple:

I saw this film yesterday.

Важно, когда именно это произошло.

Главный вопрос:

важна связь с настоящим или конкретное завершённое прошлое?""",
            },

            {
                "order": 2,
                "title": "Когда нужен Present Perfect",
                "body": """Present Perfect используется, когда:

точное время не указано;

важен результат сейчас;

речь идёт о жизненном опыте;

период времени ещё не закончился;

действие началось в прошлом и продолжается сейчас.

Примеры:

I have finished the report.

She has lost her keys.

They have visited London.

We have lived here for five years.""",
            },

            {
                "order": 3,
                "title": "Когда нужен Past Simple",
                "body": """Past Simple используется, когда:

действие завершилось в прошлом;

указано конкретное время;

период уже закончился;

события произошли одно за другим;

речь идёт о завершённой ситуации.

Примеры:

I finished the report yesterday.

She lost her keys last week.

They visited London in 2024.

We lived there for five years, but now we live elsewhere.""",
            },

            {
                "order": 4,
                "title": "Сравнение форм",
                "body": """Present Perfect:

have/has + третья форма

I have worked.

She has gone.

They have seen.

Past Simple:

правильный глагол:

worked

played

studied

неправильный глагол:

went

saw

wrote

Не смешивайте вторую и третью формы.""",
            },

            {
                "order": 5,
                "title": "Конкретное время прошлого",
                "body": """Если указано завершённое время прошлого, используйте Past Simple.

Частые выражения:

yesterday;

last week;

two days ago;

in 2020;

at six yesterday;

when I was a child.

Примеры:

I saw him yesterday.

She arrived last week.

They moved here in 2020.

Неправильно:

I have seen him yesterday.""",
            },

            {
                "order": 6,
                "title": "Результат сейчас",
                "body": """Present Perfect показывает результат, связанный с настоящим.

I have lost my keys.

Сейчас ключей нет.

Past Simple сообщает о прошлом событии:

I lost my keys yesterday, but I found them later.

Сейчас проблема уже решена.

Сравните:

She has broken her phone.
— телефон сейчас сломан.

She broke her phone last year.
— событие прошлого.""",
            },

            {
                "order": 7,
                "title": "Жизненный опыт и детали",
                "body": """Для жизненного опыта используйте Present Perfect.

Have you ever been to London?

Yes, I have.

Когда начинаем спрашивать детали, переходим на Past Simple.

When did you go there?

I went there in 2023.

Схема:

опыт → Present Perfect

детали → Past Simple""",
            },

            {
                "order": 8,
                "title": "EVER, NEVER, JUST, ALREADY, YET",
                "body": """С Present Perfect часто используются:

ever;

never;

just;

already;

yet.

Примеры:

Have you ever seen snow?

I have never been to Paris.

I have just finished.

He has already eaten.

She hasn't arrived yet.

Для стандартных учебных заданий эти слова лучше связывать с Present Perfect.""",
            },

            {
                "order": 9,
                "title": "TODAY, THIS WEEK, THIS YEAR",
                "body": """Если период ещё продолжается, часто используется Present Perfect.

I have had three meetings today.

She has called me twice this week.

They have travelled a lot this year.

Если период завершён:

I had three meetings yesterday.

She called me twice last week.

They travelled a lot last year.

Главное — закончился период или нет.""",
            },

            {
                "order": 10,
                "title": "FOR и SINCE",
                "body": """Если ситуация продолжается сейчас:

Present Perfect.

I have lived here for five years.

She has worked here since 2021.

Если ситуация уже закончилась:

Past Simple.

I lived there for five years, but now I live in Astana.

She worked there from 2018 to 2022.

Сравните:

I have lived here for five years.
— всё ещё живу здесь.

I lived there for five years.
— уже не живу там.""",
            },

            {
                "order": 11,
                "title": "HOW LONG",
                "body": """Если ситуация продолжается:

How long have you lived here?

How long has she worked here?

Если ситуация завершена:

How long did you live in London?

How long did she work there?

Сравните:

How long have you lived here?
— вы всё ещё здесь живёте.

How long did you live there?
— вы там уже не живёте.""",
            },

            {
                "order": 12,
                "title": "BEEN, GONE и конкретная поездка",
                "body": """Have been to:

человек был где-то и вернулся.

I have been to Astana.

Have gone to:

человек уехал и ещё не вернулся.

She has gone to the shop.

Если говорим о конкретной поездке:

Past Simple.

She went to Astana yesterday.

They went to Turkey last summer.""",
            },

            {
                "order": 13,
                "title": "Новости и детали",
                "body": """Новость или результат часто сообщается в Present Perfect.

I have lost my phone.

She has got a new job.

They have bought a house.

После этого детали обычно идут в Past Simple:

I have lost my phone.

Where did you lose it?

I lost it on the bus.

Это очень типичная связка двух времён.""",
            },

            {
                "order": 14,
                "title": "Как выбрать время",
                "body": """Шаг 1.

Есть точное завершённое время?

→ Past Simple

I saw him yesterday.

Шаг 2.

Важен результат сейчас?

→ Present Perfect

I have lost my phone.

Шаг 3.

Это жизненный опыт?

→ Present Perfect

Have you ever travelled abroad?

Шаг 4.

Действие продолжается сейчас?

→ Present Perfect

I have worked here since 2022.

Шаг 5.

Период завершён?

→ Past Simple

I worked there from 2020 to 2022.""",
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
                "prompt": "I ___ my keys. I can't open the door.",
                "options": [
                    "lost yesterday",
                    "have lost",
                    "have lose",
                    "did lost",
                ],
                "answer": "have lost",
                "explanation": "Важен результат сейчас: ключей нет.",
            },

            {
                "order": 2,
                "prompt": "I ___ my keys yesterday, but I found them later.",
                "options": [
                    "have lost",
                    "lost",
                    "have lose",
                    "lose",
                ],
                "answer": "lost",
                "explanation": "Yesterday — завершённое время прошлого.",
            },

            {
                "order": 3,
                "prompt": "She ___ to Turkey twice.",
                "options": [
                    "went last year",
                    "has been",
                    "has went",
                    "was",
                ],
                "answer": "has been",
                "explanation": "Жизненный опыт без конкретного времени → Present Perfect.",
            },

            {
                "order": 4,
                "prompt": "She ___ to Turkey last summer.",
                "options": [
                    "has been",
                    "went",
                    "has gone",
                    "goes",
                ],
                "answer": "went",
                "explanation": "Last summer — завершённый период → Past Simple.",
            },

            {
                "order": 5,
                "prompt": "___ you ever ___ sushi?",
                "options": [
                    "Did / ate",
                    "Have / eaten",
                    "Have / ate",
                    "Did / eaten",
                ],
                "answer": "Have / eaten",
                "explanation": "Жизненный опыт: Have + third form.",
            },

            {
                "order": 6,
                "prompt": "When ___ you ___ sushi for the first time?",
                "options": [
                    "have / eaten",
                    "did / eat",
                    "did / ate",
                    "have / eat",
                ],
                "answer": "did / eat",
                "explanation": "Когда спрашиваем конкретные детали, используем Past Simple.",
            },

            {
                "order": 7,
                "prompt": "We ___ here for ten years and we still live here.",
                "options": [
                    "lived",
                    "have lived",
                    "did live",
                    "have living",
                ],
                "answer": "have lived",
                "explanation": "Ситуация продолжается сейчас → Present Perfect.",
            },

            {
                "order": 8,
                "prompt": "We ___ there for ten years, but now we live here.",
                "options": [
                    "have lived",
                    "lived",
                    "have live",
                    "living",
                ],
                "answer": "lived",
                "explanation": "Ситуация завершилась → Past Simple.",
            },

            {
                "order": 9,
                "prompt": "He ___ three emails today.",
                "options": [
                    "wrote yesterday",
                    "has written",
                    "has wrote",
                    "did written",
                ],
                "answer": "has written",
                "explanation": "Today рассматривается как незавершённый период.",
            },

            {
                "order": 10,
                "prompt": "He ___ three emails yesterday.",
                "options": [
                    "has written",
                    "wrote",
                    "has wrote",
                    "writes",
                ],
                "answer": "wrote",
                "explanation": "Yesterday → Past Simple.",
            },

            {
                "order": 11,
                "prompt": "She ___ yet.",
                "options": [
                    "didn't arrive yesterday",
                    "hasn't arrived",
                    "hasn't arrive",
                    "not arrived",
                ],
                "answer": "hasn't arrived",
                "explanation": "Yet в отрицании обычно используется с Present Perfect.",
            },

            {
                "order": 12,
                "prompt": "She ___ at six.",
                "options": [
                    "has arrived",
                    "arrived",
                    "has arrive",
                    "arriving",
                ],
                "answer": "arrived",
                "explanation": "At six — конкретное завершённое время.",
            },

            {
                "order": 13,
                "prompt": "How long ___ you ___ here if you still live here?",
                "options": [
                    "did / live",
                    "have / lived",
                    "have / live",
                    "did / lived",
                ],
                "answer": "have / lived",
                "explanation": "Ситуация продолжается сейчас.",
            },

            {
                "order": 14,
                "prompt": "How long ___ you ___ in London if you no longer live there?",
                "options": [
                    "have / lived",
                    "did / live",
                    "did / lived",
                    "have / live",
                ],
                "answer": "did / live",
                "explanation": "Завершённая ситуация → Past Simple.",
            },

            {
                "order": 15,
                "prompt": "I ___ him last week.",
                "options": [
                    "have seen",
                    "saw",
                    "have saw",
                    "seen",
                ],
                "answer": "saw",
                "explanation": "Last week требует Past Simple.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I have seen him yesterday.",
                    "I saw him yesterday.",
                    "I have saw him yesterday.",
                    "I seen him yesterday.",
                ],
                "answer": "I saw him yesterday.",
                "explanation": "Present Perfect обычно не используется с yesterday.",
            },

            {
                "order": 17,
                "prompt": "Choose the sentence where the result is important now.",
                "options": [
                    "She broke her phone last year.",
                    "She has broken her phone.",
                    "She did break her phone yesterday.",
                    "She was breaking her phone last year.",
                ],
                "answer": "She has broken her phone.",
                "explanation": "Present Perfect подчёркивает текущий результат.",
            },

            {
                "order": 18,
                "prompt": "Have you ever been to London? — Yes, I have. When ___ you ___ there?",
                "options": [
                    "have / gone",
                    "did / go",
                    "did / went",
                    "have / been",
                ],
                "answer": "did / go",
                "explanation": "Сначала опыт — Present Perfect, затем детали — Past Simple.",
            },

            {
                "order": 19,
                "prompt": "I ___ here since 2020.",
                "options": [
                    "lived",
                    "have lived",
                    "did live",
                    "was lived",
                ],
                "answer": "have lived",
                "explanation": "Since + продолжающаяся ситуация → Present Perfect.",
            },

            {
                "order": 20,
                "prompt": "I ___ there from 2018 to 2022.",
                "options": [
                    "have lived",
                    "lived",
                    "have living",
                    "live",
                ],
                "answer": "lived",
                "explanation": "Период полностью завершён → Past Simple.",
            },

            {
                "order": 21,
                "prompt": "She has gone to the shop. What does it mean?",
                "options": [
                    "She went there last year.",
                    "She is still there or on the way.",
                    "She has been there and returned.",
                    "She never went there.",
                ],
                "answer": "She is still there or on the way.",
                "explanation": "Has gone to означает, что человек ещё не вернулся.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct pair.",
                "options": [
                    "I have finished the report. / I finished it at six.",
                    "I finished the report. / I have finished it at six yesterday.",
                    "I have finished yesterday. / I finished it already now.",
                    "I have finish the report. / I finished it at six.",
                ],
                "answer": "I have finished the report. / I finished it at six.",
                "explanation": "Результат сейчас → Present Perfect; точное время → Past Simple.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct news-and-detail sequence.",
                "options": [
                    "I lost my phone. Where have you lost it? I have lost it on the bus.",
                    "I have lost my phone. Where did you lose it? I lost it on the bus.",
                    "I have lost my phone yesterday. Where did you lose it?",
                    "I lost my phone. Where did you lost it?",
                ],
                "answer": "I have lost my phone. Where did you lose it? I lost it on the bus.",
                "explanation": "Новость → Present Perfect; детали завершённого события → Past Simple.",
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct pair.",
                "options": [
                    "Have you seen this film? / When did you see it?",
                    "Did you seen this film? / When have you saw it?",
                    "Have you saw this film? / When did you saw it?",
                    "Did you see this film? / When have you seen it yesterday?",
                ],
                "answer": "Have you seen this film? / When did you see it?",
                "explanation": "Опыт → Present Perfect; конкретные детали → Past Simple.",
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
                "✅ A1 Lesson 31 seeded: "
                "Present Perfect vs Past Simple"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
