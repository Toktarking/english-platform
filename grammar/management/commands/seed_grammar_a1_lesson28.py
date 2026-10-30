from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 28: "
        "Past Continuous."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=28,
            defaults={
                "title": "Past Continuous",
                "slug": "past-continuous",
                "theory_text": "Past Continuous.",
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Past Continuous",
                "body": """Past Continuous — прошедшее продолженное время.

Оно используется, когда действие:

происходило в определённый момент в прошлом;

длилось некоторое время;

было в процессе, когда произошло другое действие;

служило фоном для другого события;

происходило одновременно с другим действием.

Примеры:

I was working at six yesterday.

She was sleeping when I called.

They were playing while we were studying.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Past Continuous состоит из:

was / were

+

глагол-ing

Формула:

subject + was/were + verb-ing

Примеры:

I was working.

She was reading.

They were playing.

Главное правило:

без was/were Past Continuous не строится.""",
            },

            {
                "order": 3,
                "title": "WAS или WERE",
                "body": """Используйте:

I → was

you → were

he → was

she → was

it → was

we → were

they → were

Примеры:

I was sleeping.

He was driving.

She was cooking.

We were waiting.

They were playing.""",
            },

            {
                "order": 4,
                "title": "Как добавить -ING",
                "body": """Обычный случай:

work → working

read → reading

play → playing

Глагол на немую e:

write → writing

make → making

come → coming

Короткий глагол:

sit → sitting

run → running

swim → swimming

Глагол на -ie:

lie → lying

die → dying""",
            },

            {
                "order": 5,
                "title": "Действие в конкретный момент прошлого",
                "body": """Past Continuous показывает процесс в определённый момент прошлого.

Примеры:

I was working at five yesterday.

She was sleeping at midnight.

They were having dinner at seven.

We were studying at that time.

Частые выражения:

at five yesterday;

at midnight;

at that moment;

this time yesterday;

all evening;

from six to eight.""",
            },

            {
                "order": 6,
                "title": "Past Simple или Past Continuous",
                "body": """Сравните:

I had dinner at seven.

Это завершённый факт.

I was having dinner at seven.

Это процесс в семь часов.

Past Simple:

завершённое действие;

короткое событие;

факт.

Past Continuous:

процесс;

фон;

действие в конкретный момент прошлого.""",
            },

            {
                "order": 7,
                "title": "Длительное и короткое действие",
                "body": """Часто одно действие было в процессе, когда произошло другое.

Формула:

Past Continuous + when + Past Simple

Пример:

I was sleeping when you called.

Длительное действие:

was sleeping

Короткое действие:

called

Ещё примеры:

She was cooking when the phone rang.

We were driving home when the car stopped.""",
            },

            {
                "order": 8,
                "title": "WHEN",
                "body": """WHEN означает «когда».

Часто после when стоит короткое завершённое действие в Past Simple.

Примеры:

I was reading when she came.

He was sleeping when I called.

They were walking when it began to snow.

Порядок можно менять:

I was sleeping when you called.

When you called, I was sleeping.""",
            },

            {
                "order": 9,
                "title": "WHILE",
                "body": """WHILE означает:

пока;

в то время как.

Обычно после while идёт длительное действие.

Примеры:

While I was reading, she was cooking.

They were playing while we were studying.

He was listening to music while he was working.

Если два действия происходили одновременно, часто используются два Past Continuous.""",
            },

            {
                "order": 10,
                "title": "WHEN или WHILE",
                "body": """Простая схема:

длительное действие → Past Continuous

короткое действие → Past Simple

WHEN часто вводит короткое событие:

when she called;

when he arrived.

WHILE часто вводит длительный процесс:

while I was working;

while they were studying.

Сравните:

I was working when she called.

She called while I was working.""",
            },

            {
                "order": 11,
                "title": "Фон для события",
                "body": """Past Continuous часто описывает фон рассказа.

Пример:

The sun was shining.

The birds were singing.

People were walking in the park.

Children were playing.

Затем происходит главное событие:

Suddenly, a car stopped near us.

Past Continuous = фон.

Past Simple = главное завершённое событие.""",
            },

            {
                "order": 12,
                "title": "Отрицание и вопросы",
                "body": """Отрицание:

subject + wasn't / weren't + verb-ing

I wasn't sleeping.

She wasn't working.

They weren't playing.

Вопрос:

Was/Were + subject + verb-ing?

Was she sleeping?

Were they waiting?

Краткие ответы:

Yes, she was.

No, she wasn't.

Yes, they were.

No, they weren't.""",
            },

            {
                "order": 13,
                "title": "Специальные вопросы",
                "body": """Формула:

Question word + was/were + subject + verb-ing?

Примеры:

What were you doing?

Where was she going?

Why were they laughing?

Who was he talking to?

What was happening?

Если who само выполняет действие:

Who was calling?

Who was knocking?""",
            },

            {
                "order": 14,
                "title": "Глаголы состояния и HAVE",
                "body": """Некоторые глаголы состояния обычно не используются в Continuous:

know;

understand;

like;

want;

need;

believe;

remember;

own.

Правильно:

I knew the answer.

She understood the question.

Не:

I was knowing the answer.

HAVE как действие:

I was having breakfast.

She was having a shower.

HAVE как владение:

I had a car.

Не:

I was having a car.""",
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
                "prompt": "I ___ reading at nine last night.",
                "options": ["was", "were", "did", "am"],
                "answer": "was",
                "explanation": "I → was.",
            },

            {
                "order": 2,
                "prompt": "My parents ___ watching television.",
                "options": ["was", "were", "did", "are"],
                "answer": "were",
                "explanation": "Parents = they, поэтому were.",
            },

            {
                "order": 3,
                "prompt": "The child was ___.",
                "options": ["cry", "cried", "crying", "cries"],
                "answer": "crying",
                "explanation": "Past Continuous: was + verb-ing.",
            },

            {
                "order": 4,
                "prompt": "We were ___ for the bus.",
                "options": ["wait", "waited", "waiting", "waits"],
                "answer": "waiting",
                "explanation": "Were + waiting.",
            },

            {
                "order": 5,
                "prompt": "She ___ cooking when I arrived.",
                "options": ["was", "were", "did", "is"],
                "answer": "was",
                "explanation": "She → was cooking.",
            },

            {
                "order": 6,
                "prompt": "They ___ playing when it started to rain.",
                "options": ["was", "were", "did", "are"],
                "answer": "were",
                "explanation": "They → were playing.",
            },

            {
                "order": 7,
                "prompt": "While I was studying, my brother ___ television.",
                "options": [
                    "watched",
                    "was watching",
                    "watches",
                    "is watching",
                ],
                "answer": "was watching",
                "explanation": "Два действия происходили одновременно.",
            },

            {
                "order": 8,
                "prompt": "I ___ home when I saw the accident.",
                "options": [
                    "walked",
                    "was walking",
                    "walk",
                    "am walking",
                ],
                "answer": "was walking",
                "explanation": "Длительный процесс → Past Continuous; saw — короткое событие.",
            },

            {
                "order": 9,
                "prompt": "The phone rang while she ___ a shower.",
                "options": [
                    "had",
                    "was having",
                    "has",
                    "is having",
                ],
                "answer": "was having",
                "explanation": "Have a shower — действие в процессе.",
            },

            {
                "order": 10,
                "prompt": "___ you sleeping at midnight?",
                "options": ["Did", "Was", "Were", "Are"],
                "answer": "Were",
                "explanation": "You → were: Were you sleeping?",
            },

            {
                "order": 11,
                "prompt": "What ___ she doing?",
                "options": ["was", "were", "did", "is"],
                "answer": "was",
                "explanation": "She → was.",
            },

            {
                "order": 12,
                "prompt": "Where ___ they going?",
                "options": ["was", "were", "did", "are"],
                "answer": "were",
                "explanation": "They → were.",
            },

            {
                "order": 13,
                "prompt": "Who was he talking ___?",
                "options": ["at", "to", "on", "in"],
                "answer": "to",
                "explanation": "Устойчивая конструкция: talk to someone.",
            },

            {
                "order": 14,
                "prompt": "I ___ the answer.",
                "options": [
                    "was knowing",
                    "knew",
                    "knowing",
                    "did knew",
                ],
                "answer": "knew",
                "explanation": "Know — глагол состояния, поэтому Past Simple: knew.",
            },

            {
                "order": 15,
                "prompt": "Was she working?",
                "options": [
                    "Yes, she did.",
                    "Yes, she was.",
                    "Yes, she were.",
                    "Yes, she is.",
                ],
                "answer": "Yes, she was.",
                "explanation": "Вопрос с was требует ответ с was.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I were working.",
                    "I was working.",
                    "I did working.",
                    "I was work.",
                ],
                "answer": "I was working.",
                "explanation": "I → was + verb-ing.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "They was playing.",
                    "They were playing.",
                    "They did playing.",
                    "They were play.",
                ],
                "answer": "They were playing.",
                "explanation": "They → were + playing.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct question.",
                "options": [
                    "Did you working?",
                    "Were you working?",
                    "Was you working?",
                    "Did you were working?",
                ],
                "answer": "Were you working?",
                "explanation": "Past Continuous question: Were + subject + verb-ing?",
            },

            {
                "order": 19,
                "prompt": "I was sleeping when she ___.",
                "options": [
                    "was calling",
                    "called",
                    "calls",
                    "is calling",
                ],
                "answer": "called",
                "explanation": "Короткое завершённое действие → Past Simple.",
            },

            {
                "order": 20,
                "prompt": "While she was cooking, I ___ the table.",
                "options": [
                    "was setting",
                    "set every day",
                    "am setting",
                    "did setting",
                ],
                "answer": "was setting",
                "explanation": "Два параллельных процесса → Past Continuous.",
            },

            {
                "order": 21,
                "prompt": "Which sentence describes a process at a specific past time?",
                "options": [
                    "I watched a film yesterday.",
                    "I was watching a film at eight.",
                    "I watch films every day.",
                    "I am watching a film now.",
                ],
                "answer": "I was watching a film at eight.",
                "explanation": "Действие было в процессе в конкретный момент прошлого.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence about possession.",
                "options": [
                    "I was having a car.",
                    "I had a car.",
                    "I was have a car.",
                    "I did having a car.",
                ],
                "answer": "I had a car.",
                "explanation": "Have в значении владения обычно используется в Past Simple.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct pair.",
                "options": [
                    "I had dinner at seven. / I was having dinner at seven.",
                    "I was had dinner at seven. / I having dinner at seven.",
                    "I did dinner at seven. / I were having dinner.",
                    "I had dinner at seven. / I was have dinner at seven.",
                ],
                "answer": "I had dinner at seven. / I was having dinner at seven.",
                "explanation": "Past Simple показывает факт; Past Continuous — процесс.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct sequence.",
                "options": [
                    "I was walking home when I saw an accident.",
                    "I walked home when I was saw an accident.",
                    "I was walk home when I saw an accident.",
                    "I did walking home when I saw an accident.",
                ],
                "answer": "I was walking home when I saw an accident.",
                "explanation": "Длительное действие — Past Continuous; короткое событие — Past Simple.",
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
                "✅ A1 Lesson 28 seeded: Past Continuous"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
