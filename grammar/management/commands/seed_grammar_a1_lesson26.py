from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 26: "
        "Past Simple with irregular verbs."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=26,
            defaults={
                "title": "Past Simple с неправильными глаголами",
                "slug": "past-simple-irregular-verbs",
                "theory_text": "Past Simple with irregular verbs.",
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое неправильные глаголы",
                "body": """У правильных глаголов Past Simple обычно образуется при помощи -ed:

work → worked

play → played

study → studied

Но неправильные глаголы меняют форму по-другому.

Примеры:

go → went

see → saw

have → had

do → did

come → came

take → took

Нельзя просто добавить -ed.

Неправильно:

goed

seed

taked

comed""",
            },

            {
                "order": 2,
                "title": "Вторая форма глагола",
                "body": """У неправильных глаголов для Past Simple нужно запомнить вторую форму.

Примеры:

go → went

see → saw

have → had

do → did

come → came

take → took

get → got

make → made

give → gave

find → found

Форма Past Simple одинакова для всех лиц:

I went.

She went.

They went.

Не:

He wents.""",
            },

            {
                "order": 3,
                "title": "GO, COME и SEE",
                "body": """GO → WENT

I went to work yesterday.

She went home early.

COME → CAME

She came home late.

They came by bus.

SEE → SAW

I saw him yesterday.

We saw the accident.

Сравните:

I went to the office.
— Я пошёл в офис.

I came to the office.
— Я пришёл в офис.

Также:

see = увидеть;

watch = смотреть некоторое время.""",
            },

            {
                "order": 4,
                "title": "HAVE и DO",
                "body": """HAVE → HAD

I had a car.

She had two children.

Had также используется в выражениях:

had breakfast;

had lunch;

had a meeting;

had a good time.

DO → DID

I did my homework.

She did the work.

Важно:

DID может быть и основным, и вспомогательным глаголом.

I did my homework.

Did you do your homework?

В вопросе второе do остаётся в начальной форме.""",
            },

            {
                "order": 5,
                "title": "TAKE, GET и MAKE",
                "body": """TAKE → TOOK

I took the book.

She took a taxi.

He took a photo.

GET → GOT

I got a message.

She got tired.

We got home late.

MAKE → MADE

She made dinner.

I made a mistake.

They made a decision.

Не путайте:

do homework;

do the cleaning;

но:

make dinner;

make a mistake;

make a decision.""",
            },

            {
                "order": 6,
                "title": "GIVE, FIND и KNOW",
                "body": """GIVE → GAVE

She gave me a book.

I gave him my phone number.

FIND → FOUND

I found my keys.

They found the answer.

KNOW → KNEW

I knew the answer.

She knew him well.

They knew the truth.""",
            },

            {
                "order": 7,
                "title": "THINK, SAY и TELL",
                "body": """THINK → THOUGHT

I thought about the problem.

She thought he was right.

SAY → SAID

She said hello.

He said that he was tired.

TELL → TOLD

She told me the truth.

He told us a story.

Сравните:

She said that she was tired.

She told me that she was tired.

После tell часто указывается человек:

told me;

told him;

told us.""",
            },

            {
                "order": 8,
                "title": "Другие частые неправильные глаголы",
                "body": """LEAVE → LEFT

She left early.

FEEL → FELT

I felt tired.

BUY → BOUGHT

I bought a new phone.

BRING → BROUGHT

She brought some documents.

WRITE → WROTE

I wrote an email.

SPEAK → SPOKE

I spoke to the teacher.

EAT → ATE

I ate breakfast.

DRINK → DRANK

I drank coffee.""",
            },

            {
                "order": 9,
                "title": "READ, SLEEP и WAKE",
                "body": """READ → READ

Написание одинаковое, но произношение разное.

Настоящее:

read /riːd/

Прошлое:

read /red/

Пример:

I read every day.

I read this book yesterday.

SLEEP → SLEPT

I slept well.

WAKE → WOKE

wake up → woke up

I woke up at seven.""",
            },

            {
                "order": 10,
                "title": "Утверждение",
                "body": """В утвердительном предложении используется вторая форма неправильного глагола.

Формула:

Подлежащее + Past Simple form

Примеры:

I went home.

She saw him.

They had lunch.

We came early.

He took a taxi.

Важно:

вторая форма используется именно в утверждении.""",
            },

            {
                "order": 11,
                "title": "Отрицание с DIDN'T",
                "body": """В отрицании используется:

didn't + первая форма глагола

Примеры:

I didn't go.

She didn't see him.

They didn't come.

He didn't take a taxi.

We didn't have lunch.

Неправильно:

didn't went

didn't saw

didn't came

didn't had

Правильно:

didn't go

didn't see

didn't come

didn't have""",
            },

            {
                "order": 12,
                "title": "Вопросы с DID",
                "body": """Формула:

Did + подлежащее + первая форма глагола?

Примеры:

Did you go home?

Did she see him?

Did they come?

Did he take a taxi?

Did you have breakfast?

Неправильно:

Did she went home?

Правильно:

Did she go home?

Краткие ответы:

Yes, I did.

No, I didn't.""",
            },

            {
                "order": 13,
                "title": "Специальные вопросы и WHO",
                "body": """Специальный вопрос:

Question word + did + subject + verb?

Примеры:

Where did you go?

What did she see?

When did they come?

Why did he leave?

What did you buy?

Но если WHO само выполняет действие, did не используется:

Who came yesterday?

Who saw the accident?

Who took my phone?

Who wrote this message?

Сравните:

Who called you?

Who did you call?""",
            },

            {
                "order": 14,
                "title": "Как запоминать неправильные глаголы",
                "body": """Неправильные глаголы лучше учить небольшими группами.

Движение:

go → went

come → came

leave → left

run → ran

Общение:

say → said

tell → told

speak → spoke

write → wrote

Еда:

eat → ate

drink → drank

have → had

Лучше учить не только форму:

go → went

а сразу предложение:

I went home yesterday.

Главное правило урока:

утверждение → вторая форма

She went.

отрицание → didn't + первая форма

She didn't go.

вопрос → Did + первая форма

Did she go?""",
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
                "prompt": "We ___ to Astana last week.",
                "options": ["went", "goed", "go", "did went"],
                "answer": "went",
                "explanation": "Past Simple глагола go — went.",
            },

            {
                "order": 2,
                "prompt": "She ___ home at six.",
                "options": ["came", "comed", "come", "did came"],
                "answer": "came",
                "explanation": "Past Simple глагола come — came.",
            },

            {
                "order": 3,
                "prompt": "I ___ an interesting film yesterday.",
                "options": ["saw", "see", "seed", "seen"],
                "answer": "saw",
                "explanation": "Past Simple глагола see — saw.",
            },

            {
                "order": 4,
                "prompt": "He ___ breakfast at seven.",
                "options": ["had", "have", "haved", "has"],
                "answer": "had",
                "explanation": "Past Simple глагола have — had.",
            },

            {
                "order": 5,
                "prompt": "They ___ their homework.",
                "options": ["did", "doed", "do", "done"],
                "answer": "did",
                "explanation": "Past Simple глагола do — did.",
            },

            {
                "order": 6,
                "prompt": "She ___ a photo.",
                "options": ["taked", "took", "take", "taken"],
                "answer": "took",
                "explanation": "Past Simple глагола take — took.",
            },

            {
                "order": 7,
                "prompt": "I didn't ___ the answer.",
                "options": ["knew", "know", "known", "knowing"],
                "answer": "know",
                "explanation": "После didn't используется первая форма know.",
            },

            {
                "order": 8,
                "prompt": "He didn't ___ the door.",
                "options": ["opened", "open", "opens", "opening"],
                "answer": "open",
                "explanation": "После didn't используется начальная форма.",
            },

            {
                "order": 9,
                "prompt": "Did she ___ the document?",
                "options": ["found", "find", "finds", "finding"],
                "answer": "find",
                "explanation": "После did используется первая форма find.",
            },

            {
                "order": 10,
                "prompt": "Did you ___ him the truth?",
                "options": ["told", "tell", "tells", "telling"],
                "answer": "tell",
                "explanation": "После did используется tell, не told.",
            },

            {
                "order": 11,
                "prompt": "Where did they ___?",
                "options": ["went", "go", "gone", "going"],
                "answer": "go",
                "explanation": "После did → go.",
            },

            {
                "order": 12,
                "prompt": "What did she ___?",
                "options": ["bought", "buy", "buys", "buying"],
                "answer": "buy",
                "explanation": "После did используется первая форма buy.",
            },

            {
                "order": 13,
                "prompt": "Who ___ this email?",
                "options": ["did write", "wrote", "write", "written"],
                "answer": "wrote",
                "explanation": "Who является подлежащим, поэтому did не нужен.",
            },

            {
                "order": 14,
                "prompt": "Did he come to the meeting?",
                "options": [
                    "Yes, he did.",
                    "Yes, he came.",
                    "Yes, he was.",
                    "Yes, he does.",
                ],
                "answer": "Yes, he did.",
                "explanation": "Краткий ответ на вопрос с did: Yes, he did.",
            },

            {
                "order": 15,
                "prompt": "She ___ tired after work.",
                "options": ["felt", "feeled", "feel", "did felt"],
                "answer": "felt",
                "explanation": "Past Simple глагола feel — felt.",
            },

            {
                "order": 16,
                "prompt": "I ___ a new phone yesterday.",
                "options": ["buyed", "bought", "buy", "did bought"],
                "answer": "bought",
                "explanation": "Buy → bought.",
            },

            {
                "order": 17,
                "prompt": "He ___ me a book.",
                "options": ["gived", "gave", "give", "given"],
                "answer": "gave",
                "explanation": "Give → gave.",
            },

            {
                "order": 18,
                "prompt": "We ___ the answer.",
                "options": ["finded", "found", "find", "founded"],
                "answer": "found",
                "explanation": "Find → found.",
            },

            {
                "order": 19,
                "prompt": "She ___ that the lesson was difficult.",
                "options": ["thinked", "thought", "think", "thinks"],
                "answer": "thought",
                "explanation": "Think → thought.",
            },

            {
                "order": 20,
                "prompt": "He ___ me the truth.",
                "options": ["said", "told", "telled", "tell"],
                "answer": "told",
                "explanation": "Tell + человек: He told me the truth.",
            },

            {
                "order": 21,
                "prompt": "I ___ an email yesterday.",
                "options": ["writed", "wrote", "written", "write"],
                "answer": "wrote",
                "explanation": "Write → wrote.",
            },

            {
                "order": 22,
                "prompt": "They ___ dinner at a restaurant.",
                "options": ["eated", "ate", "eat", "eaten"],
                "answer": "ate",
                "explanation": "Eat → ate.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She didn't went home.",
                    "She didn't go home.",
                    "She didn't gone home.",
                    "She wasn't went home.",
                ],
                "answer": "She didn't go home.",
                "explanation": "После didn't неправильный глагол возвращается в первую форму.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct sequence.",
                "options": [
                    "She went. / She didn't went. / Did she went?",
                    "She went. / She didn't go. / Did she go?",
                    "She go. / She didn't went. / Did she go?",
                    "She was went. / She didn't go. / Was she go?",
                ],
                "answer": "She went. / She didn't go. / Did she go?",
                "explanation": "Вторая форма только в утверждении; после did/didn't используется первая форма.",
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
                "✅ A1 Lesson 26 seeded: "
                "Past Simple — irregular verbs"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
