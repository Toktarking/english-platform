from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 20: "
        "Can, Could and Be able to."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=20,
            defaults={
                "title": "CAN, COULD и BE ABLE TO",
                "slug": "can-could-be-able-to",
                "theory_text": (
                    "Can, could and be able to."
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
                "title": "Что означает CAN",
                "body": """CAN используется, когда мы говорим:

об умении;

о способности;

о возможности;

о разрешении;

о просьбе.

Примеры:

I can swim.

She can speak English.

We can meet tomorrow.

Can I come in?

Can you help me?""",
            },

            {
                "order": 2,
                "title": "CAN не изменяется",
                "body": """CAN имеет одну форму для всех лиц:

I can

you can

he can

she can

it can

we can

they can

Нельзя добавлять -s.

Неправильно:

He cans drive.

Правильно:

He can drive.""",
            },

            {
                "order": 3,
                "title": "После CAN глагол без TO",
                "body": """Формула:

Подлежащее + can + глагол

Примеры:

I can swim.

She can read.

They can help.

He can work.

Неправильно:

I can to swim.

She can reads.

He can working.

После CAN используется базовая форма глагола.""",
            },

            {
                "order": 4,
                "title": "CAN: умение и возможность",
                "body": """CAN может показывать умение:

I can swim.

She can use Excel.

He can cook.

They can speak English.

Также CAN может показывать возможность:

We can meet after work.

You can call me tomorrow.

I can finish this today.

She can come with us.

Иногда CAN показывает общую возможность:

This road can be dangerous in winter.

People can change.""",
            },

            {
                "order": 5,
                "title": "CAN: разрешение и просьба",
                "body": """Чтобы попросить разрешение:

Can I + глагол?

Can I come in?

Can I sit here?

Can I use your phone?

Ответ:

Yes, you can.

No, you can't.

Чтобы попросить другого человека:

Can you + глагол?

Can you help me?

Can you open the door?

Can you repeat that?""",
            },

            {
                "order": 6,
                "title": "CAN'T",
                "body": """Отрицательные формы:

cannot;

can't.

Формула:

Подлежащее + can't + глагол

Примеры:

I can't drive.

He can't speak French.

We can't stay.

They can't help us.

После can't также используется глагол без to.

Правильно:

She can't come.

Неправильно:

She can't to come.""",
            },

            {
                "order": 7,
                "title": "Вопросы с CAN",
                "body": """В вопросе CAN ставится перед подлежащим.

Формула:

Can + подлежащее + глагол?

Примеры:

Can you swim?

Can she drive?

Can they help?

Краткие ответы:

Yes, I can.

No, I can't.

Важно:

DO и DOES не нужны.

Неправильно:

Do you can swim?

Does she can drive?

Правильно:

Can you swim?

Can she drive?""",
            },

            {
                "order": 8,
                "title": "Специальные вопросы с CAN",
                "body": """Формула:

Вопросительное слово + can + подлежащее + глагол?

Примеры:

What can you do?

Where can we meet?

When can she come?

How can I help?

Where can I park?

How can I contact you?

После can основной глагол остаётся в базовой форме.""",
            },

            {
                "order": 9,
                "title": "COULD — способность в прошлом",
                "body": """COULD часто используется для способности в прошлом.

Примеры:

I could swim when I was five.

She could read at the age of four.

He could run very fast when he was young.

They could speak English well.

COULD не изменяется по лицам:

I could;

he could;

they could.

После could используется глагол без to.""",
            },

            {
                "order": 10,
                "title": "COULDN'T и вопросы с COULD",
                "body": """Отрицание:

could not = couldn't

Примеры:

I couldn't swim.

She couldn't understand the question.

He couldn't come yesterday.

Вопрос:

Could + подлежащее + глагол?

Could you swim when you were six?

Could she read at that age?

Ответы:

Yes, I could.

No, I couldn't.""",
            },

            {
                "order": 11,
                "title": "COULD как вежливая просьба",
                "body": """Could you...? звучит вежливее, чем Can you...?

Сравните:

Can you help me?

Could you help me?

Другие примеры:

Could you open the window?

Could you repeat that?

Could you speak more slowly?

Could you send me the document?

Важно:

в просьбе COULD не обязательно относится к прошлому.

Could you help me now?

Это просьба в настоящем.""",
            },

            {
                "order": 12,
                "title": "BE ABLE TO",
                "body": """BE ABLE TO означает:

быть способным;

мочь;

суметь.

Примеры:

I am able to swim.

She is able to solve this problem.

They are able to help us.

В настоящем времени CAN обычно звучит естественнее:

I can swim.

Но BE ABLE TO полезно, когда CAN нельзя поставить в нужную форму.""",
            },

            {
                "order": 13,
                "title": "Будущее: WILL BE ABLE TO",
                "body": """У CAN нет обычной формы будущего времени.

Неправильно:

I will can come.

Правильно:

I will be able to come.

Формула:

will be able to + глагол

Примеры:

I will be able to help you tomorrow.

She will be able to come next week.

Отрицание:

won't be able to

I won't be able to come.

Вопрос:

Will + подлежащее + be able to + глагол?

Will you be able to come?""",
            },

            {
                "order": 14,
                "title": "CAN, COULD или BE ABLE TO",
                "body": """Короткий алгоритм:

Настоящее умение:

CAN

I can drive.

Прошлое общее умение:

COULD

I could read when I was five.

Будущая возможность:

WILL BE ABLE TO

I will be able to come tomorrow.

Вежливая просьба:

COULD YOU...?

Could you help me?

Конкретный успешный результат в прошлом часто выражается:

was/were able to

We were able to open the door.

Главное правило:

после can/could используется глагол без to.""",
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
                "prompt": "My brother ___ drive.",
                "options": ["can", "cans", "is can", "does can"],
                "answer": "can",
                "explanation": "CAN не изменяется с he/she/it.",
            },

            {
                "order": 2,
                "prompt": "They can ___ very fast.",
                "options": ["runs", "run", "running", "to run"],
                "answer": "run",
                "explanation": "После can используется базовая форма без to.",
            },

            {
                "order": 3,
                "prompt": "___ your child read?",
                "options": ["Does can", "Can", "Is", "Do"],
                "answer": "Can",
                "explanation": "Модальный глагол сам ставится перед подлежащим.",
            },

            {
                "order": 4,
                "prompt": "Can your child read? — No, he ___.",
                "options": [
                    "doesn't can",
                    "can't",
                    "isn't can",
                    "not can",
                ],
                "answer": "can't",
                "explanation": "Краткий отрицательный ответ: No, he can't.",
            },

            {
                "order": 5,
                "prompt": "I ___ speak English when I was ten.",
                "options": [
                    "can",
                    "could",
                    "will be able",
                    "am able",
                ],
                "answer": "could",
                "explanation": "Способность в прошлом выражается через could.",
            },

            {
                "order": 6,
                "prompt": "She ___ understand the teacher yesterday.",
                "options": [
                    "couldn't",
                    "doesn't can",
                    "can't",
                    "not could",
                ],
                "answer": "couldn't",
                "explanation": "Для невозможности в прошлом используется couldn't.",
            },

            {
                "order": 7,
                "prompt": "___ you open the window, please?",
                "options": ["Could", "Do", "Are", "Does"],
                "answer": "Could",
                "explanation": "Could you...? — вежливая просьба.",
            },

            {
                "order": 8,
                "prompt": "Could I ___ your phone?",
                "options": ["uses", "use", "using", "to use"],
                "answer": "use",
                "explanation": "После could используется базовая форма use.",
            },

            {
                "order": 9,
                "prompt": "We will ___ finish the work tomorrow.",
                "options": [
                    "can",
                    "able to",
                    "be able to",
                    "could",
                ],
                "answer": "be able to",
                "explanation": "Будущая возможность: will be able to.",
            },

            {
                "order": 10,
                "prompt": "Will she be able to ___?",
                "options": ["comes", "come", "coming", "came"],
                "answer": "come",
                "explanation": "После be able to используется базовая форма глагола.",
            },

            {
                "order": 11,
                "prompt": "I won't be able to ___ the meeting.",
                "options": [
                    "attends",
                    "attending",
                    "attend",
                    "attended",
                ],
                "answer": "attend",
                "explanation": "Правильно: be able to attend.",
            },

            {
                "order": 12,
                "prompt": "___ you be able to help us tomorrow?",
                "options": ["Can", "Will", "Do", "Are"],
                "answer": "Will",
                "explanation": "Вопрос в будущем: Will you be able to...?",
            },

            {
                "order": 13,
                "prompt": "He ___ swim when he was four.",
                "options": ["could", "can", "will can", "is able"],
                "answer": "could",
                "explanation": "Общая способность в прошлом → could.",
            },

            {
                "order": 14,
                "prompt": "Can you help me?",
                "options": [
                    "Yes, I do.",
                    "Yes, I am.",
                    "Yes, I can.",
                    "Yes, I help.",
                ],
                "answer": "Yes, I can.",
                "explanation": "Вопрос с can требует краткий ответ с can.",
            },

            {
                "order": 15,
                "prompt": "Could you speak more slowly?",
                "options": [
                    "Yes, of course.",
                    "Yes, I could yesterday.",
                    "No, I don't speak.",
                    "Yes, I am.",
                ],
                "answer": "Yes, of course.",
                "explanation": "Здесь could используется как вежливая просьба.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "He cans swim.",
                    "He can swims.",
                    "He can swim.",
                    "He can to swim.",
                ],
                "answer": "He can swim.",
                "explanation": "CAN не получает -s, а основной глагол остаётся в базовой форме.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct question.",
                "options": [
                    "Do you can speak English?",
                    "Can you speak English?",
                    "Are you can speak English?",
                    "Does you can speak English?",
                ],
                "answer": "Can you speak English?",
                "explanation": "Do/does с can не используются.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I will can help you.",
                    "I will be able to help you.",
                    "I will able to help you.",
                    "I can will help you.",
                ],
                "answer": "I will be able to help you.",
                "explanation": "Для будущего используется will be able to.",
            },

            {
                "order": 19,
                "prompt": "Where ___ I park?",
                "options": ["do can", "can", "am can", "does"],
                "answer": "can",
                "explanation": "Специальный вопрос: Where can I park?",
            },

            {
                "order": 20,
                "prompt": "She ___ read when she was five.",
                "options": ["could", "can", "cans", "was can"],
                "answer": "could",
                "explanation": "Прошлая общая способность → could.",
            },

            {
                "order": 21,
                "prompt": "The door was locked, but we ___ open it.",
                "options": [
                    "were able to",
                    "will be able to",
                    "can to",
                    "are able",
                ],
                "answer": "were able to",
                "explanation": "Для конкретного успешного результата в прошлом подходит were able to.",
            },

            {
                "order": 22,
                "prompt": "Choose the more polite request.",
                "options": [
                    "Can you help me?",
                    "Could you help me?",
                    "Do you help me?",
                    "Are you help me?",
                ],
                "answer": "Could you help me?",
                "explanation": "Could you...? обычно звучит вежливее.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She could to read.",
                    "She could reads.",
                    "She could read.",
                    "She could reading.",
                ],
                "answer": "She could read.",
                "explanation": "После could используется базовая форма без to.",
            },

            {
                "order": 24,
                "prompt": "Which sentence talks about future ability?",
                "options": [
                    "I can help you.",
                    "I could help when I was younger.",
                    "I will be able to help you tomorrow.",
                    "I can helping you tomorrow.",
                ],
                "answer": "I will be able to help you tomorrow.",
                "explanation": "Будущая способность выражается через will be able to.",
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
                "✅ A1 Lesson 20 seeded: "
                "CAN, COULD и BE ABLE TO"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
