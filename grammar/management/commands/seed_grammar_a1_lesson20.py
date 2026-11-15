from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 20: CAN, COULD and BE ABLE TO."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=20,

                defaults={
                    "title":
                        "CAN, COULD и BE ABLE TO",

                    "slug":
                        "can-could-be-able-to",

                    "theory_text":
                        "Can, could and be able to.",

                    "estimated_minutes":
                        19,

                    "pass_score":
                        70,

                    "xp_reward":
                        100,

                    "is_published":
                        True,
                },
            )
        )


        # ================================================
        # 10 MICRO-RULES
        # ================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Что означает CAN?",

                "body":
                    """CAN используется, когда мы говорим об:

умении;

способности;

возможности;

разрешении;

просьбе.

Умение:

I can swim.

She can speak English.

Возможность:

We can meet tomorrow.

Разрешение:

Can I come in?

Просьба:

Can you help me?""",
            },


            {
                "order": 2,

                "title":
                    "CAN одинаковый для всех",

                "body":
                    """CAN не изменяется по лицам.

I can

you can

he can

she can

it can

we can

they can

Не:

He cans drive.

А:

He can drive.

Даже с HE / SHE / IT окончание -S к CAN не добавляется.""",
            },


            {
                "order": 3,

                "title":
                    "После CAN — глагол без TO",

                "body":
                    """После CAN используется базовая форма глагола.

I can swim.

She can read.

He can work.

They can help.

Не:

I can to swim.

She can reads.

He can working.

Формула:

subject
+ CAN
+ base verb.""",
            },


            {
                "order": 4,

                "title":
                    "CAN'T = не могу",

                "body":
                    """Отрицание:

CANNOT

или чаще:

CAN'T

I can't drive.

He can't speak French.

We can't stay.

They can't help us.

После CAN'T тоже используется базовая форма.

She can't come.

Не:

She can't to come.

Не:

She doesn't can come.""",
            },


            {
                "order": 5,

                "title":
                    "Вопросы с CAN",

                "body":
                    """В вопросе CAN ставится перед подлежащим.

Can you swim?

Can she drive?

Can they help?

DO и DOES не нужны.

Не:

Do you can swim?

Does she can drive?

Краткие ответы:

Can you swim?

Yes, I can.

No, I can't.

Специальные вопросы:

Where can I park?

How can I help?

When can she come?""",
            },


            {
                "order": 6,

                "title":
                    "CAN для разрешения и просьбы",

                "body":
                    """Разрешение:

Can I come in?

Can I sit here?

Can I use your phone?

Ответ:

Yes, you can.

No, you can't.

Просьба другому человеку:

Can you help me?

Can you open the window?

Can you repeat that?

CAN здесь означает не только физическую способность, но и просьбу или разрешение.""",
            },


            {
                "order": 7,

                "title":
                    "COULD — способность в прошлом",

                "body":
                    """COULD часто показывает общую способность в прошлом.

I could swim when I was five.

She could read at the age of four.

He could run very fast when he was young.

COULD тоже не изменяется:

I could

he could

they could

После COULD используется базовая форма без TO.

Не:

She could to read.

А:

She could read.""",
            },


            {
                "order": 8,

                "title":
                    "COULDN'T и вопросы с COULD",

                "body":
                    """Отрицание:

COULD NOT
→ COULDN'T

I couldn't swim.

She couldn't understand the question.

He couldn't come yesterday.

Вопрос:

Could you swim when you were six?

Could she read at that age?

Краткие ответы:

Yes, I could.

No, I couldn't.""",
            },


            {
                "order": 9,

                "title":
                    "COULD YOU...? — вежливая просьба",

                "body":
                    """COULD YOU...? часто звучит вежливее, чем CAN YOU...?

Can you help me?

Could you help me?

Другие примеры:

Could you open the window?

Could you repeat that?

Could you speak more slowly?

Could you send me the document?

Важно:

COULD в такой просьбе не означает прошлое.

Could you help me now?

Это просьба в настоящем.""",
            },


            {
                "order": 10,

                "title":
                    "BE ABLE TO и будущее",

                "body":
                    """BE ABLE TO означает «быть способным / суметь».

В настоящем часто проще использовать CAN:

I can swim.

Но для будущей способности используется:

WILL BE ABLE TO

I will be able to help you tomorrow.

She will be able to come next week.

Не:

I will can help.

Отрицание:

won't be able to

I won't be able to come.

Вопрос:

Will you be able to come?

Для конкретного успешного результата в прошлом часто используется:

was / were able to

The door was locked, but we were able to open it.

Коротко:

сейчас → CAN

общее умение в прошлом → COULD

будущая способность → WILL BE ABLE TO

конкретный успех в прошлом → WAS / WERE ABLE TO.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects
                .update_or_create(
                    lesson=lesson,
                    order=data["order"],

                    defaults={
                        "title":
                            data["title"],

                        "body":
                            data["body"],
                    },
                )
            )

            section_objects[
                data["order"]
            ] = section


        # ================================================
        # 20 TRAINING EXERCISES
        # ================================================

        training = [

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ swim.",

                "options": [
                    "can",
                    "cans",
                    "am can",
                    "do can",
                ],

                "answer":
                    "can",

                "explanation":
                    "Для способности используется CAN.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "We ___ meet tomorrow.",

                "options": [
                    "can",
                    "are can",
                    "cans",
                    "do can",
                ],

                "answer":
                    "can",

                "explanation":
                    "CAN может выражать возможность.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "My brother ___ drive.",

                "options": [
                    "can",
                    "cans",
                    "does can",
                    "is can",
                ],

                "answer":
                    "can",

                "explanation":
                    "CAN не получает -S с HE.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She cans cook.",
                    "She can cook.",
                    "She can cooks.",
                    "She does can cook.",
                ],

                "answer":
                    "She can cook.",

                "explanation":
                    "CAN имеет одну форму для всех лиц.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "They can ___ very fast.",

                "options": [
                    "runs",
                    "run",
                    "running",
                    "to run",
                ],

                "answer":
                    "run",

                "explanation":
                    "После CAN используется базовая форма RUN.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "fill",

                "prompt":
                    "She can ___ English. (speak)",

                "options": [],

                "answer":
                    "speak",

                "explanation":
                    "После CAN не используется TO или -S.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "He ___ speak French.",

                "options": [
                    "can't",
                    "doesn't can",
                    "isn't can",
                    "not can",
                ],

                "answer":
                    "can't",

                "explanation":
                    "Отрицательная форма CAN → CAN'T.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She can't to come.",
                    "She can't comes.",
                    "She can't come.",
                    "She doesn't can come.",
                ],

                "answer":
                    "She can't come.",

                "explanation":
                    "CAN'T + базовая форма COME.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "___ your child read?",

                "options": [
                    "Does can",
                    "Can",
                    "Do",
                    "Is",
                ],

                "answer":
                    "Can",

                "explanation":
                    "CAN сам ставится перед подлежащим.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Can your child read?",

                "options": [
                    "Yes, he does.",
                    "Yes, he is.",
                    "Yes, he can.",
                    "Yes, he reads can.",
                ],

                "answer":
                    "Yes, he can.",

                "explanation":
                    "Вопрос с CAN → краткий ответ с CAN.",
            },


            {
                "order": 11,
                "section": 5,
                "type": "build",

                "prompt":
                    "Собери правильный вопрос.",

                "options": [
                    "Where",
                    "can",
                    "I",
                    "park",
                ],

                "answer":
                    "Where can I park",

                "explanation":
                    "WH-word + CAN + subject + base verb.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "___ I use your phone?",

                "options": [
                    "Can",
                    "Do",
                    "Am",
                    "Does",
                ],

                "answer":
                    "Can",

                "explanation":
                    "CAN I...? используется для просьбы о разрешении.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "choice",

                "prompt":
                    "___ you help me with this bag?",

                "options": [
                    "Can",
                    "Are",
                    "Do can",
                    "Does",
                ],

                "answer":
                    "Can",

                "explanation":
                    "CAN YOU...? — обычная просьба.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I ___ swim when I was six.",

                "options": [
                    "can",
                    "could",
                    "will can",
                    "am able",
                ],

                "answer":
                    "could",

                "explanation":
                    "Общая способность в прошлом → COULD.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She could to read.",
                    "She could reads.",
                    "She could read.",
                    "She could reading.",
                ],

                "answer":
                    "She could read.",

                "explanation":
                    "После COULD используется базовая форма.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "She ___ understand the question yesterday.",

                "options": [
                    "couldn't",
                    "doesn't can",
                    "can't",
                    "not could",
                ],

                "answer":
                    "couldn't",

                "explanation":
                    "Неспособность в прошлом → COULDN'T.",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Could you swim when you were five?",

                "options": [
                    "Yes, I could.",
                    "Yes, I can.",
                    "Yes, I did.",
                    "Yes, I was.",
                ],

                "answer":
                    "Yes, I could.",

                "explanation":
                    "Вопрос с COULD → ответ с COULD.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the more polite request.",

                "options": [
                    "Can you open the window?",
                    "Could you open the window?",
                    "Do you open the window?",
                    "Are you open the window?",
                ],

                "answer":
                    "Could you open the window?",

                "explanation":
                    "COULD YOU...? обычно звучит вежливее.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "I ___ help you tomorrow.",

                "options": [
                    "will can",
                    "will be able to",
                    "will able to",
                    "can will",
                ],

                "answer":
                    "will be able to",

                "explanation":
                    "Будущая способность → WILL BE ABLE TO.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "The door was locked, but we ___ open it.",

                "options": [
                    "were able to",
                    "will be able to",
                    "can to",
                    "are able to",
                ],

                "answer":
                    "were able to",

                "explanation":
                    "Конкретный успешный результат в прошлом → WERE ABLE TO.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "My sister ___ play the piano.",

                "options": [
                    "can",
                    "cans",
                    "does can",
                    "is can",
                ],

                "answer":
                    "can",

                "explanation":
                    "CAN не изменяется с SHE.",
            },


            {
                "order": 22,

                "prompt":
                    "He can ___ very well.",

                "options": [
                    "cooks",
                    "cook",
                    "cooking",
                    "to cook",
                ],

                "answer":
                    "cook",

                "explanation":
                    "После CAN используется базовая форма.",
            },


            {
                "order": 23,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "They don't can come.",
                    "They can't come.",
                    "They can't to come.",
                    "They aren't can come.",
                ],

                "answer":
                    "They can't come.",

                "explanation":
                    "Отрицание CAN → CAN'T + base verb.",
            },


            {
                "order": 24,

                "prompt":
                    "___ she speak English?",

                "options": [
                    "Does can",
                    "Can",
                    "Does",
                    "Is",
                ],

                "answer":
                    "Can",

                "explanation":
                    "CAN ставится перед подлежащим без DO / DOES.",
            },


            {
                "order": 25,

                "prompt":
                    "Can I sit here?",

                "options": [
                    "Yes, you can.",
                    "Yes, you do.",
                    "Yes, you are.",
                    "Yes, you sit.",
                ],

                "answer":
                    "Yes, you can.",

                "explanation":
                    "Вопрос о разрешении с CAN → ответ с CAN.",
            },


            {
                "order": 26,

                "prompt":
                    "When he was young, he ___ run very fast.",

                "options": [
                    "could",
                    "can",
                    "cans",
                    "will be able to",
                ],

                "answer":
                    "could",

                "explanation":
                    "Общая способность в прошлом → COULD.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She couldn't to understand me.",
                    "She couldn't understands me.",
                    "She couldn't understand me.",
                    "She doesn't could understand me.",
                ],

                "answer":
                    "She couldn't understand me.",

                "explanation":
                    "COULDN'T + базовая форма.",
            },


            {
                "order": 28,

                "prompt":
                    "Which sentence is a polite request now?",

                "options": [
                    "Could you speak more slowly?",
                    "Could you spoke more slowly?",
                    "Do you could speak more slowly?",
                    "Are you could speak more slowly?",
                ],

                "answer":
                    "Could you speak more slowly?",

                "explanation":
                    "COULD YOU...? может выражать вежливую просьбу в настоящем.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the sentence about future ability.",

                "options": [
                    "I can drive.",
                    "I could drive when I was eighteen.",
                    "I will be able to drive next month.",
                    "I will can drive next month.",
                ],

                "answer":
                    "I will be able to drive next month.",

                "explanation":
                    "Будущая способность → WILL BE ABLE TO.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct set.",

                "options": [
                    "I can swim. / I could swim at five. / I will be able to swim again soon.",
                    "I can to swim. / I could swam at five. / I will can swim soon.",
                    "I cans swim. / I could to swim at five. / I will able to swim soon.",
                    "I do can swim. / I was could swim at five. / I can will swim soon.",
                ],

                "answer":
                    "I can swim. / I could swim at five. / I will be able to swim again soon.",

                "explanation":
                    "CAN — настоящее, COULD — прошлая способность, WILL BE ABLE TO — будущая способность.",
            },

        ]


        valid_orders = []


        for data in (
            training
            +
            final_test
        ):

            valid_orders.append(
                data["order"]
            )


            if data["order"] <= 20:

                section = (
                    section_objects[
                        data["section"]
                    ]
                )

            else:

                section = None


            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],

                defaults={
                    "section":
                        section,

                    "exercise_type":
                        data.get(
                            "type",
                            "choice",
                        ),

                    "prompt":
                        data["prompt"],

                    "options":
                        data["options"],

                    "correct_answer":
                        data["answer"],

                    "explanation":
                        data["explanation"],

                    "is_published":
                        True,
                },
            )


        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        GrammarLessonSection.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=[
                item["order"]
                for item in sections
            ],
        ).delete()


        self.stdout.write(
            self.style.SUCCESS(
                "✅ Interactive A1 Lesson 20 seeded"
            )
        )

        self.stdout.write(
            f"Micro rules: "
            f"{lesson.sections.count()}"
        )

        self.stdout.write(
            "Training exercises: "
            f"{lesson.exercises.filter(section__isnull=False).count()}"
        )

        self.stdout.write(
            "Final test: "
            f"{lesson.exercises.filter(section__isnull=True).count()}"
        )
