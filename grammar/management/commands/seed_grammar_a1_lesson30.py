from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 30: "
        "Present Perfect."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=30,
            defaults={
                "title": (
                    "Present Perfect: "
                    "HAVE / HAS + третья форма глагола"
                ),
                "slug": "present-perfect",
                "theory_text": "Present Perfect.",
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Present Perfect",
                "body": """Present Perfect используется, когда действие произошло в прошлом, но связано с настоящим.

Нас может интересовать:

результат сейчас;

жизненный опыт;

действие в ещё не закончившийся период;

действие, которое началось в прошлом и продолжается сейчас;

недавнее действие без точного времени.

Примеры:

I have finished the report.

She has lost her keys.

They have visited London.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Present Perfect состоит из:

have / has

+

третья форма глагола

Формула:

subject + have/has + Past Participle

HAVE:

I

you

we

they

HAS:

he

she

it

Примеры:

I have worked.

She has finished.

They have gone.

He has seen.""",
            },

            {
                "order": 3,
                "title": "Третья форма глагола",
                "body": """Для Present Perfect нужна третья форма глагола.

Примеры:

work — worked — worked

go — went — gone

see — saw — seen

write — wrote — written

У правильных глаголов:

worked → worked

played → played

studied → studied

У неправильных третью форму нужно запоминать:

do → done

eat → eaten

take → taken

speak → spoken

know → known

break → broken""",
            },

            {
                "order": 4,
                "title": "Не используйте вторую форму",
                "body": """После have / has нельзя использовать Past Simple форму неправильного глагола.

Неправильно:

I have went.

She has saw.

They have wrote.

Правильно:

I have gone.

She has seen.

They have written.

Сравните:

I went home.
— Past Simple

I have gone home.
— Present Perfect""",
            },

            {
                "order": 5,
                "title": "Результат сейчас",
                "body": """Present Perfect часто показывает результат, который важен сейчас.

Пример:

I have lost my keys.

Ключи были потеряны раньше, но результат важен сейчас: ключей нет.

Другие примеры:

She has broken her phone.

We have finished the work.

He has opened the window.

They have left the office.

Точное время действия здесь не важно.""",
            },

            {
                "order": 6,
                "title": "Present Perfect или Past Simple",
                "body": """Present Perfect обычно не используется с завершённым временем прошлого.

Правильно:

I have seen this film.

Но:

I saw this film yesterday.

Неправильно:

I have seen this film yesterday.

Past Simple используется с:

yesterday;

last week;

last year;

two days ago;

in 2020.

Present Perfect используется, когда важен результат или опыт и точное время не называется.""",
            },

            {
                "order": 7,
                "title": "EVER и NEVER",
                "body": """EVER означает «когда-нибудь».

Часто используется в вопросах:

Have you ever been to London?

Has she ever tried sushi?

NEVER означает «никогда».

I have never been to London.

She has never tried sushi.

После never дополнительное not не нужно.

Неправильно:

I haven't never been there.

Правильно:

I have never been there.""",
            },

            {
                "order": 8,
                "title": "BEEN и GONE",
                "body": """HAVE/HAS BEEN TO означает:

человек был где-то и уже вернулся.

I have been to London.

HAVE/HAS GONE TO означает:

человек ушёл или уехал и ещё не вернулся.

She has gone to the shop.

Сравните:

Marat has been to Astana.
— был и вернулся.

Marat has gone to Astana.
— уехал и сейчас ещё там или в пути.""",
            },

            {
                "order": 9,
                "title": "JUST, ALREADY и YET",
                "body": """JUST = только что

have/has + just + third form

I have just finished.

She has just arrived.

ALREADY = уже

have/has + already + third form

I have already finished.

She has already eaten.

YET используется обычно в конце.

В вопросах:

Have you finished yet?

В отрицаниях:

I haven't finished yet.""",
            },

            {
                "order": 10,
                "title": "TODAY, THIS WEEK и SO FAR",
                "body": """Present Perfect может использоваться, если период времени ещё продолжается.

I have had two meetings today.

She has called me three times this week.

We have completed five tasks this month.

They have travelled a lot this year.

SO FAR означает:

пока;

до настоящего момента.

We have completed five tasks so far.

I have read three chapters so far.""",
            },

            {
                "order": 11,
                "title": "FOR и SINCE",
                "body": """FOR показывает продолжительность:

for two hours;

for five years;

for a long time.

Пример:

I have lived here for five years.

SINCE показывает начальную точку:

since Monday;

since 2020;

since childhood.

Пример:

I have lived here since 2020.

Запомните:

FOR = сколько времени

SINCE = с какого момента""",
            },

            {
                "order": 12,
                "title": "HOW LONG",
                "body": """Чтобы спросить о продолжительности:

How long have/has...?

Примеры:

How long have you lived here?

How long has she worked at the university?

How long have they known each other?

Ответы:

I have lived here for five years.

She has worked here since 2022.""",
            },

            {
                "order": 13,
                "title": "Отрицания и вопросы",
                "body": """Отрицание:

haven't / hasn't + third form

I haven't finished.

She hasn't arrived.

He hasn't seen the film.

Вопрос:

Have/Has + subject + third form?

Have you finished?

Has she arrived?

Has he seen the film?

Краткие ответы:

Yes, I have.

No, I haven't.

Yes, she has.

No, she hasn't.

Do и did здесь не используются.""",
            },

            {
                "order": 14,
                "title": "Как выбрать Present Perfect",
                "body": """Шаг 1.

Указано точное завершённое время?

yesterday

last week

in 2020

→ Past Simple

I saw him yesterday.

Шаг 2.

Важен результат сейчас?

→ Present Perfect

I have lost my phone.

Шаг 3.

Это жизненный опыт?

→ Present Perfect

I have been to Turkey.

Шаг 4.

Действие началось раньше и продолжается сейчас?

→ Present Perfect + for/since

I have lived here for five years.""",
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
                "prompt": "We ___ completed the task.",
                "options": ["has", "have", "did", "are"],
                "answer": "have",
                "explanation": "We используется с have.",
            },

            {
                "order": 2,
                "prompt": "My sister ___ called me.",
                "options": ["have", "has", "did", "is"],
                "answer": "has",
                "explanation": "My sister = she, поэтому has.",
            },

            {
                "order": 3,
                "prompt": "They have ___ to London.",
                "options": ["went", "been", "was", "be"],
                "answer": "been",
                "explanation": "Been — третья форма be.",
            },

            {
                "order": 4,
                "prompt": "He has ___ breakfast.",
                "options": ["ate", "eaten", "eat", "eating"],
                "answer": "eaten",
                "explanation": "Eat — ate — eaten.",
            },

            {
                "order": 5,
                "prompt": "I have ___ the book.",
                "options": ["read", "wrote", "reading", "reads"],
                "answer": "read",
                "explanation": "Третья форма read пишется так же: read.",
            },

            {
                "order": 6,
                "prompt": "She hasn't ___ yet.",
                "options": ["came", "come", "coming", "comes"],
                "answer": "come",
                "explanation": "Come — came — come; нужна третья форма.",
            },

            {
                "order": 7,
                "prompt": "Have you ever ___ sushi?",
                "options": ["ate", "eaten", "eat", "eating"],
                "answer": "eaten",
                "explanation": "После have нужна третья форма eaten.",
            },

            {
                "order": 8,
                "prompt": "Has he ___ the report?",
                "options": ["wrote", "written", "write", "writing"],
                "answer": "written",
                "explanation": "Write — wrote — written.",
            },

            {
                "order": 9,
                "prompt": "I have just ___ home.",
                "options": ["came", "come", "coming", "comes"],
                "answer": "come",
                "explanation": "Have just + third form: come.",
            },

            {
                "order": 10,
                "prompt": "They have already ___.",
                "options": ["left", "leave", "leaving", "leaves"],
                "answer": "left",
                "explanation": "Leave — left — left.",
            },

            {
                "order": 11,
                "prompt": "She hasn't finished ___.",
                "options": ["already", "yet", "just", "yesterday"],
                "answer": "yet",
                "explanation": "Yet обычно ставится в конце отрицательного предложения.",
            },

            {
                "order": 12,
                "prompt": "I have lived here ___ five years.",
                "options": ["since", "for", "from", "during"],
                "answer": "for",
                "explanation": "For показывает продолжительность.",
            },

            {
                "order": 13,
                "prompt": "She has worked here ___ 2022.",
                "options": ["for", "since", "during", "ago"],
                "answer": "since",
                "explanation": "Since показывает начальную точку.",
            },

            {
                "order": 14,
                "prompt": "Have they arrived?",
                "options": [
                    "Yes, they did.",
                    "Yes, they have.",
                    "Yes, they are.",
                    "Yes, they arrived have.",
                ],
                "answer": "Yes, they have.",
                "explanation": "Вопрос с have требует краткого ответа с have.",
            },

            {
                "order": 15,
                "prompt": "I ___ him yesterday.",
                "options": [
                    "have seen",
                    "saw",
                    "have saw",
                    "seen",
                ],
                "answer": "saw",
                "explanation": "Yesterday требует Past Simple.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I have went home.",
                    "I have gone home.",
                    "I have go home.",
                    "I has gone home.",
                ],
                "answer": "I have gone home.",
                "explanation": "Go — went — gone; после have нужна третья форма.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She has saw the film.",
                    "She has seen the film.",
                    "She have seen the film.",
                    "She has see the film.",
                ],
                "answer": "She has seen the film.",
                "explanation": "See — saw — seen.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence with NEVER.",
                "options": [
                    "I haven't never been there.",
                    "I have never been there.",
                    "I never have been not there.",
                    "I did never been there.",
                ],
                "answer": "I have never been there.",
                "explanation": "Never уже содержит отрицательное значение.",
            },

            {
                "order": 19,
                "prompt": "Marat has ___ to Astana and is back now.",
                "options": ["gone", "been", "went", "go"],
                "answer": "been",
                "explanation": "Been to означает, что человек был там и вернулся.",
            },

            {
                "order": 20,
                "prompt": "Marat has ___ to Astana and is still there.",
                "options": ["been", "gone", "went", "going"],
                "answer": "gone",
                "explanation": "Gone to означает, что человек ещё не вернулся.",
            },

            {
                "order": 21,
                "prompt": "Choose the correct word order.",
                "options": [
                    "She just has arrived.",
                    "She has just arrived.",
                    "She has arrived just has.",
                    "She did just arrived.",
                ],
                "answer": "She has just arrived.",
                "explanation": "Just обычно стоит между have/has и третьей формой.",
            },

            {
                "order": 22,
                "prompt": "Which sentence describes life experience?",
                "options": [
                    "I visited Turkey in 2024.",
                    "I have visited Turkey.",
                    "I am visiting Turkey yesterday.",
                    "I have visited Turkey last year.",
                ],
                "answer": "I have visited Turkey.",
                "explanation": "Без точного времени Present Perfect может описывать жизненный опыт.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct question.",
                "options": [
                    "Did you finished yet?",
                    "Have you finished yet?",
                    "Do you have finished yet?",
                    "Have you finish yet?",
                ],
                "answer": "Have you finished yet?",
                "explanation": "Present Perfect question: Have + subject + third form?",
            },

            {
                "order": 24,
                "prompt": "Choose the correct pair.",
                "options": [
                    "I have seen him yesterday. / I saw him before.",
                    "I saw him yesterday. / I have seen him before.",
                    "I have saw him yesterday. / I seen him before.",
                    "I saw him yesterday. / I have saw him before.",
                ],
                "answer": "I saw him yesterday. / I have seen him before.",
                "explanation": "Yesterday → Past Simple; опыт без точного времени → Present Perfect.",
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
                "✅ A1 Lesson 30 seeded: Present Perfect"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
