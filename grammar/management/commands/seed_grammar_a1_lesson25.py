from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 25: "
        "Past Simple with regular verbs."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=25,
            defaults={
                "title": "Past Simple с правильными глаголами",
                "slug": "past-simple-regular-verbs",
                "theory_text": "Past Simple with regular verbs.",
                "estimated_minutes": 35,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Past Simple",
                "body": """Past Simple используется, когда действие:

произошло в прошлом;

завершилось в прошлом;

произошло в конкретный момент;

больше не продолжается.

Примеры:

I worked yesterday.

She studied English last year.

They played football on Sunday.""",
            },

            {
                "order": 2,
                "title": "Правильные глаголы и -ED",
                "body": """У правильных глаголов Past Simple обычно образуется добавлением -ed.

Примеры:

work → worked

play → played

open → opened

clean → cleaned

watch → watched

visit → visited

Форма одинакова для всех лиц:

I worked.

She worked.

They worked.

Окончание -s, как в Present Simple, не используется.""",
            },

            {
                "order": 3,
                "title": "Когда используется Past Simple",
                "body": """Past Simple используется для завершённых действий.

I finished the report yesterday.

She called me last night.

They visited Almaty last year.

Также для последовательности действий:

I opened the door, entered the room and turned on the light.

И для привычек в прошлом:

We played outside every day.

She visited her grandmother every Sunday.""",
            },

            {
                "order": 4,
                "title": "Слова-маркеры",
                "body": """Частые маркеры Past Simple:

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

I worked yesterday.

She called me last night.

They moved here three years ago.""",
            },

            {
                "order": 5,
                "title": "Обычное добавление -ED",
                "body": """К большинству глаголов просто добавляется -ed.

work → worked

clean → cleaned

open → opened

help → helped

start → started

Примеры:

I worked yesterday.

She cleaned the room.

We opened the window.""",
            },

            {
                "order": 6,
                "title": "Глаголы на E",
                "body": """Если глагол уже заканчивается на e, добавляется только -d.

live → lived

love → loved

move → moved

dance → danced

arrive → arrived

Неправильно:

liveed

Правильно:

lived""",
            },

            {
                "order": 7,
                "title": "Глаголы на Y",
                "body": """Если перед y стоит согласная:

y → i + ed

study → studied

carry → carried

try → tried

cry → cried

Если перед y стоит гласная, y сохраняется:

play → played

stay → stayed

enjoy → enjoyed

Сравните:

study → studied

play → played""",
            },

            {
                "order": 8,
                "title": "Удвоение согласной",
                "body": """У коротких глаголов типа:

согласная + гласная + согласная

последняя согласная часто удваивается.

Примеры:

stop → stopped

plan → planned

shop → shopped

drop → dropped

Но обычно не удваиваются:

w;

x;

y.

Примеры:

snow → snowed

fix → fixed

play → played""",
            },

            {
                "order": 9,
                "title": "Произношение -ED",
                "body": """Окончание -ed имеет три основных варианта произношения:

/t/

/d/

/ɪd/

Примеры /t/:

worked;

watched;

helped;

stopped.

Примеры /d/:

played;

cleaned;

opened;

called.

Примеры /ɪd/:

wanted;

needed;

started;

visited.

Написание одинаковое, но произношение разное.""",
            },

            {
                "order": 10,
                "title": "Утвердительное предложение",
                "body": """Формула:

Подлежащее + глагол-ed

Примеры:

I worked yesterday.

She played tennis.

They studied English.

We visited our friends.

Для всех подлежащих используется одна форма Past Simple.

He worked.

They worked.""",
            },

            {
                "order": 11,
                "title": "Отрицание с DIDN'T",
                "body": """Отрицание образуется с did not / didn't.

Формула:

Подлежащее + didn't + глагол

Примеры:

I didn't work.

She didn't play.

They didn't study.

Важно:

после didn't глагол возвращается в начальную форму.

She worked.

She didn't work.

Неправильно:

She didn't worked.""",
            },

            {
                "order": 12,
                "title": "Вопросы с DID",
                "body": """Формула:

Did + подлежащее + глагол?

Примеры:

Did you work yesterday?

Did she call you?

Did they study English?

Did he open the door?

После did используется начальная форма.

Неправильно:

Did she worked?

Правильно:

Did she work?

Краткие ответы:

Yes, I did.

No, I didn't.""",
            },

            {
                "order": 13,
                "title": "Специальные вопросы и WHO",
                "body": """Формула специального вопроса:

Question word + did + subject + verb?

Примеры:

Where did you work?

When did she arrive?

Why did they leave?

What did he study?

Who did you call?

Но если WHO само выполняет действие, did обычно не используется.

Who called you?

Who opened the door?

Сравните:

Who called you?
— Кто позвонил тебе?

Who did you call?
— Кому позвонил ты?""",
            },

            {
                "order": 14,
                "title": "Past Simple и WAS/WERE",
                "body": """WAS/WERE используются для:

состояния;

места;

профессии;

возраста.

I was tired.

She was at home.

They were students.

Обычный Past Simple используется для действий:

I worked.

She studied.

They played.

Сравните:

He was at work yesterday.
— Он был на работе.

He worked yesterday.
— Он работал вчера.

Важно:

с was/were DID не используется.

Was she tired?

Но с обычным глаголом:

Did she work yesterday?""",
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
                "prompt": "We ___ the room yesterday.",
                "options": ["clean", "cleaned", "cleaning", "did cleaned"],
                "answer": "cleaned",
                "explanation": "Утвердительный Past Simple: clean → cleaned.",
            },

            {
                "order": 2,
                "prompt": "She ___ me last night.",
                "options": ["call", "called", "calling", "did called"],
                "answer": "called",
                "explanation": "Call — правильный глагол: called.",
            },

            {
                "order": 3,
                "prompt": "They ___ in Astana for two years.",
                "options": ["lived", "liveed", "living", "did lived"],
                "answer": "lived",
                "explanation": "Live заканчивается на e, поэтому добавляется только d.",
            },

            {
                "order": 4,
                "prompt": "He ___ the window.",
                "options": ["opened", "openened", "opening", "did opened"],
                "answer": "opened",
                "explanation": "Open → opened.",
            },

            {
                "order": 5,
                "prompt": "I ___ the film.",
                "options": ["watched", "watchd", "watching", "did watched"],
                "answer": "watched",
                "explanation": "Watch → watched.",
            },

            {
                "order": 6,
                "prompt": "She didn't ___ the question.",
                "options": ["answered", "answer", "answers", "answering"],
                "answer": "answer",
                "explanation": "После didn't используется базовая форма.",
            },

            {
                "order": 7,
                "prompt": "We didn't ___ late.",
                "options": ["arrived", "arrive", "arrives", "arriving"],
                "answer": "arrive",
                "explanation": "После didn't → arrive, не arrived.",
            },

            {
                "order": 8,
                "prompt": "Did they ___ you?",
                "options": ["helped", "help", "helps", "helping"],
                "answer": "help",
                "explanation": "После did используется базовая форма.",
            },

            {
                "order": 9,
                "prompt": "Did she ___ in London?",
                "options": ["lived", "live", "lives", "living"],
                "answer": "live",
                "explanation": "Did + subject + base verb.",
            },

            {
                "order": 10,
                "prompt": "Where did you ___?",
                "options": ["worked", "work", "works", "working"],
                "answer": "work",
                "explanation": "После did → work.",
            },

            {
                "order": 11,
                "prompt": "When did the lesson ___?",
                "options": ["started", "start", "starts", "starting"],
                "answer": "start",
                "explanation": "После did используется начальная форма start.",
            },

            {
                "order": 12,
                "prompt": "Why did he ___?",
                "options": ["stopped", "stop", "stops", "stopping"],
                "answer": "stop",
                "explanation": "После did → stop.",
            },

            {
                "order": 13,
                "prompt": "Who ___ the door?",
                "options": ["did opened", "opened", "open", "opening"],
                "answer": "opened",
                "explanation": "Who здесь подлежащее, поэтому did не нужен.",
            },

            {
                "order": 14,
                "prompt": "Did you visit Almaty?",
                "options": [
                    "Yes, I did.",
                    "Yes, I was.",
                    "Yes, I visited did.",
                    "Yes, I do.",
                ],
                "answer": "Yes, I did.",
                "explanation": "Вопрос с did требует краткий ответ с did.",
            },

            {
                "order": 15,
                "prompt": "She ___ tired yesterday.",
                "options": ["worked", "was", "did", "were"],
                "answer": "was",
                "explanation": "Tired — состояние, поэтому используется was.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct Past Simple form of STUDY.",
                "options": ["studyed", "studied", "studyd", "studing"],
                "answer": "studied",
                "explanation": "Согласная + y: y → i + ed.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct Past Simple form of PLAY.",
                "options": ["plaied", "played", "playd", "playyed"],
                "answer": "played",
                "explanation": "Перед y стоит гласная, поэтому y сохраняется.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct Past Simple form of STOP.",
                "options": ["stoped", "stopped", "stopt", "stopping"],
                "answer": "stopped",
                "explanation": "Последняя согласная удваивается: stop → stopped.",
            },

            {
                "order": 19,
                "prompt": "Choose the correct Past Simple form of MOVE.",
                "options": ["moveed", "moved", "movied", "moving"],
                "answer": "moved",
                "explanation": "Глагол заканчивается на e, поэтому добавляем d.",
            },

            {
                "order": 20,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "She didn't worked yesterday.",
                    "She didn't work yesterday.",
                    "She wasn't work yesterday.",
                    "She doesn't worked yesterday.",
                ],
                "answer": "She didn't work yesterday.",
                "explanation": "Didn't уже показывает прошлое, поэтому work без -ed.",
            },

            {
                "order": 21,
                "prompt": "Choose the correct question.",
                "options": [
                    "Did she worked yesterday?",
                    "Did she work yesterday?",
                    "Was she work yesterday?",
                    "Does she worked yesterday?",
                ],
                "answer": "Did she work yesterday?",
                "explanation": "Did + subject + base verb.",
            },

            {
                "order": 22,
                "prompt": "Choose the sentence about an action.",
                "options": [
                    "He was at work yesterday.",
                    "He worked yesterday.",
                    "He was tired yesterday.",
                    "He was a student.",
                ],
                "answer": "He worked yesterday.",
                "explanation": "Worked описывает действие; was описывает состояние/место/роль.",
            },

            {
                "order": 23,
                "prompt": "Which word has -ed pronounced as /ɪd/?",
                "options": ["worked", "played", "wanted", "helped"],
                "answer": "wanted",
                "explanation": "После звука /t/ окончание -ed произносится как /ɪd/.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct pair.",
                "options": [
                    "She worked. / She didn't worked.",
                    "She worked. / She didn't work.",
                    "She work. / Did she worked?",
                    "She was worked. / She didn't work.",
                ],
                "answer": "She worked. / She didn't work.",
                "explanation": "В утверждении — worked; после didn't — базовая форма work.",
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
                "✅ A1 Lesson 25 seeded: "
                "Past Simple — regular verbs"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
