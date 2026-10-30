from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 41: "
        "Passive Voice."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=41,
            defaults={
                "title": "Пассивный залог — Passive Voice",
                "slug": "passive-voice",
                "theory_text": "Passive Voice: be + Past Participle.",
                "estimated_minutes": 50,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Active Voice и Passive Voice",
                "body": """В Active Voice подлежащее выполняет действие.

The manager signed the document.

Менеджер выполняет действие.

В Passive Voice подлежащее испытывает действие на себе.

The document was signed.

Главное здесь — документ и действие над ним.

Сравните:

The teacher explains the rule.

The rule is explained by the teacher.""",
            },

            {
                "order": 2,
                "title": "Главная формула Passive Voice",
                "body": """Основная формула:

be + V3

Форма глагола BE зависит от времени.

Третья форма смыслового глагола сохраняется.

Примеры:

is written

was written

will be written

has been written

must be written

У неправильных глаголов обязательно нужна третья форма:

write → written

make → made

build → built

send → sent""",
            },

            {
                "order": 3,
                "title": "Когда используется Passive Voice",
                "body": """Пассив используется, когда:

исполнитель неизвестен;

исполнитель неважен;

исполнитель очевиден;

важнее результат;

используется официальный или научный стиль.

Примеры:

My phone was stolen.

The road was repaired last year.

The thief was arrested.

The work has been completed.

The data were collected in 2025.""",
            },

            {
                "order": 4,
                "title": "Present Simple Passive",
                "body": """Формула:

am/is/are + V3

Примеры:

English is spoken in many countries.

The office is cleaned every day.

These cars are made in Germany.

The documents are checked carefully.

Единственное число:

is + V3

Множественное число:

are + V3

Вопрос:

Is the office cleaned every day?

Are the documents checked?""",
            },

            {
                "order": 5,
                "title": "Past Simple Passive",
                "body": """Формула:

was/were + V3

Примеры:

The house was built in 1990.

The letter was sent yesterday.

The roads were repaired last year.

The students were invited.

Единственное число:

was + V3

Множественное число:

were + V3

Вопрос:

Was the letter sent?

Were the students invited?""",
            },

            {
                "order": 6,
                "title": "Future Simple Passive",
                "body": """Формула:

will be + V3

Примеры:

The work will be finished tomorrow.

The results will be published next week.

The documents will be sent today.

Отрицание:

won't be + V3

The meeting won't be cancelled.

Вопрос:

Will the work be finished tomorrow?""",
            },

            {
                "order": 7,
                "title": "Continuous Passive",
                "body": """Present Continuous Passive:

am/is/are being + V3

The room is being cleaned now.

The road is being repaired.

Past Continuous Passive:

was/were being + V3

The road was being repaired when we arrived.

The documents were being checked at five.

Слово being показывает процесс.""",
            },

            {
                "order": 8,
                "title": "Perfect Passive",
                "body": """Present Perfect Passive:

have/has been + V3

The report has been completed.

The documents have been sent.

Past Perfect Passive:

had been + V3

The work had been completed before the meeting.

Future Perfect Passive:

will have been + V3

The work will have been completed by Friday.

Во всех случаях смысловой глагол остаётся в V3.""",
            },

            {
                "order": 9,
                "title": "Passive с модальными глаголами",
                "body": """Формула:

modal + be + V3

Примеры:

The form must be completed.

The report should be checked.

This machine can be used safely.

The meeting may be cancelled.

The plan might be changed.

После модального глагола используется BE, а затем третья форма.""",
            },

            {
                "order": 10,
                "title": "BY и WITH",
                "body": """BY показывает исполнителя действия.

The book was written by George Orwell.

The document was signed by the director.

WITH показывает инструмент или материал.

The bread was cut with a knife.

The door was opened with a key.

Сравните:

The letter was written by Anna.
— Anna выполняет действие.

The letter was written with a pen.
— pen — инструмент.""",
            },

            {
                "order": 11,
                "title": "Когда BY не нужен",
                "body": """Если исполнитель:

неизвестен;

неважен;

очевиден,

его обычно не указывают.

Пример:

My car was stolen.

Необязательно:

My car was stolen by someone.

Ещё пример:

English is spoken in many countries.

Нет необходимости добавлять:

by people.""",
            },

            {
                "order": 12,
                "title": "Как преобразовать Active в Passive",
                "body": """Шаг 1.

Найдите объект.

The teacher explains the rule.

Объект:

the rule

Шаг 2.

Поставьте объект на первое место.

The rule...

Шаг 3.

Определите время.

explains → Present Simple

Шаг 4.

Выберите правильную форму BE:

is/are

Шаг 5.

Поставьте V3:

explain → explained

Итог:

The rule is explained by the teacher.""",
            },

            {
                "order": 13,
                "title": "Преобразование по временам",
                "body": """Present Simple:

They clean the room.

→ The room is cleaned.

Past Simple:

They cleaned the room.

→ The room was cleaned.

Future Simple:

They will clean the room.

→ The room will be cleaned.

Present Continuous:

They are cleaning the room.

→ The room is being cleaned.

Present Perfect:

They have cleaned the room.

→ The room has been cleaned.

Modal:

They must clean the room.

→ The room must be cleaned.""",
            },

            {
                "order": 14,
                "title": "Типичные ошибки",
                "body": """Неправильно:

The letter written yesterday.

Правильно:

The letter was written yesterday.

Неправильно:

The letter was wrote.

Правильно:

The letter was written.

Неправильно:

The documents is checked.

Правильно:

The documents are checked.

Неправильно:

The work has completed.

Правильно:

The work has been completed.

Если действие происходит сейчас:

The room is being cleaned now.""",
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
                "prompt": "These cars ___ in Japan.",
                "options": [
                    "make",
                    "are made",
                    "are making",
                    "made every day",
                ],
                "answer": "are made",
                "explanation": (
                    "Present Simple Passive: are + V3."
                ),
            },

            {
                "order": 2,
                "prompt": "The bridge ___ last year.",
                "options": [
                    "built",
                    "was built",
                    "has build",
                    "was building by itself",
                ],
                "answer": "was built",
                "explanation": (
                    "Past Simple Passive: was + V3."
                ),
            },

            {
                "order": 3,
                "prompt": "The documents ___ tomorrow.",
                "options": [
                    "will send",
                    "will be sent",
                    "will sent",
                    "are send",
                ],
                "answer": "will be sent",
                "explanation": (
                    "Future Simple Passive: will be + V3."
                ),
            },

            {
                "order": 4,
                "prompt": "The road ___ now.",
                "options": [
                    "is repairing",
                    "is being repaired",
                    "was repaired tomorrow",
                    "has repair",
                ],
                "answer": "is being repaired",
                "explanation": (
                    "Процесс происходит сейчас → "
                    "Present Continuous Passive."
                ),
            },

            {
                "order": 5,
                "prompt": "The letters ___ already ___.",
                "options": [
                    "have / been sent",
                    "are / sent yesterday",
                    "have / sent",
                    "were / sending",
                ],
                "answer": "have / been sent",
                "explanation": (
                    "Present Perfect Passive: have been + V3."
                ),
            },

            {
                "order": 6,
                "prompt": "The problem must ___.",
                "options": [
                    "solve",
                    "be solved",
                    "solved",
                    "be solving",
                ],
                "answer": "be solved",
                "explanation": (
                    "Modal Passive: must + be + V3."
                ),
            },

            {
                "order": 7,
                "prompt": "___ the room cleaned every day?",
                "options": [
                    "Does",
                    "Is",
                    "Was yesterday",
                    "Has be",
                ],
                "answer": "Is",
                "explanation": (
                    "Present Simple Passive question: "
                    "Is + subject + V3?"
                ),
            },

            {
                "order": 8,
                "prompt": "___ the documents sent yesterday?",
                "options": [
                    "Did",
                    "Were",
                    "Are",
                    "Have",
                ],
                "answer": "Were",
                "explanation": (
                    "Past Simple Passive question: Were + subject + V3?"
                ),
            },

            {
                "order": 9,
                "prompt": "The meeting may ___.",
                "options": [
                    "cancel",
                    "be cancelled",
                    "cancelled",
                    "be cancelling",
                ],
                "answer": "be cancelled",
                "explanation": (
                    "May + be + V3."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "The picture was painted ___ a famous artist."
                ),
                "options": [
                    "with",
                    "by",
                    "from",
                    "for",
                ],
                "answer": "by",
                "explanation": (
                    "BY показывает исполнителя."
                ),
            },

            {
                "order": 11,
                "prompt": "The bread was cut ___ a knife.",
                "options": [
                    "by",
                    "with",
                    "from",
                    "at",
                ],
                "answer": "with",
                "explanation": (
                    "WITH показывает инструмент."
                ),
            },

            {
                "order": 12,
                "prompt": "She ___ a certificate.",
                "options": [
                    "was given",
                    "gave by them",
                    "was gave",
                    "is giving yesterday",
                ],
                "answer": "was given",
                "explanation": (
                    "Give → given; passive: was given."
                ),
            },

            {
                "order": 13,
                "prompt": "I ___ in 1998.",
                "options": [
                    "born",
                    "was born",
                    "am born",
                    "did born",
                ],
                "answer": "was born",
                "explanation": (
                    "Конструкция be born используется в пассивной форме."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "The work ___ before the meeting started."
                ),
                "options": [
                    "had completed",
                    "had been completed",
                    "was completing itself",
                    "has complete",
                ],
                "answer": "had been completed",
                "explanation": (
                    "Past Perfect Passive: had been + V3."
                ),
            },

            {
                "order": 15,
                "prompt": "By Friday, the work ___.",
                "options": [
                    "will have completed",
                    "will have been completed",
                    "will be complete yesterday",
                    "has been completing",
                ],
                "answer": "will have been completed",
                "explanation": (
                    "Future Perfect Passive: will have been + V3."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "The letter written yesterday.",
                    "The letter was written yesterday.",
                    "The letter did written yesterday.",
                    "The letter was wrote yesterday.",
                ],
                "answer": "The letter was written yesterday.",
                "explanation": (
                    "Past Simple Passive requires was + V3."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "The documents is checked.",
                    "The documents are checked.",
                    "The documents are check.",
                    "The documents checked are.",
                ],
                "answer": "The documents are checked.",
                "explanation": (
                    "Documents — plural, поэтому are + V3."
                ),
            },

            {
                "order": 18,
                "prompt": (
                    "Choose the correct Present Perfect Passive."
                ),
                "options": [
                    "The work has completed.",
                    "The work has been completed.",
                    "The work is been completed.",
                    "The work has being completed.",
                ],
                "answer": "The work has been completed.",
                "explanation": (
                    "Present Perfect Passive: has been + V3."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "They are cleaning the room now. "
                    "Choose the passive form."
                ),
                "options": [
                    "The room is cleaned now.",
                    "The room is being cleaned now.",
                    "The room was being cleaned now.",
                    "The room has cleaning now.",
                ],
                "answer": "The room is being cleaned now.",
                "explanation": (
                    "Present Continuous Passive: is being + V3."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "They cleaned the room yesterday. "
                    "Choose the passive form."
                ),
                "options": [
                    "The room was cleaned yesterday.",
                    "The room is cleaned yesterday.",
                    "The room was cleaning yesterday.",
                    "The room did cleaned yesterday.",
                ],
                "answer": "The room was cleaned yesterday.",
                "explanation": (
                    "Past Simple Passive: was + V3."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "They will clean the room tomorrow. "
                    "Choose the passive form."
                ),
                "options": [
                    "The room will clean tomorrow.",
                    "The room will be cleaned tomorrow.",
                    "The room will cleaned tomorrow.",
                    "The room is will cleaned tomorrow.",
                ],
                "answer": "The room will be cleaned tomorrow.",
                "explanation": (
                    "Future Simple Passive: will be + V3."
                ),
            },

            {
                "order": 22,
                "prompt": (
                    "They must clean the room. "
                    "Choose the passive form."
                ),
                "options": [
                    "The room must clean.",
                    "The room must be cleaned.",
                    "The room must cleaned.",
                    "The room must be cleaning.",
                ],
                "answer": "The room must be cleaned.",
                "explanation": (
                    "Modal Passive: must + be + V3."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct BY/WITH pair."
                ),
                "options": [
                    (
                        "The letter was written by Anna. / "
                        "The bread was cut with a knife."
                    ),
                    (
                        "The letter was written with Anna. / "
                        "The bread was cut by a knife."
                    ),
                    (
                        "The letter was written from Anna. / "
                        "The bread was cut by with knife."
                    ),
                    (
                        "The letter was written by a pen. / "
                        "The bread was cut with Anna."
                    ),
                ],
                "answer": (
                    "The letter was written by Anna. / "
                    "The bread was cut with a knife."
                ),
                "explanation": (
                    "BY = исполнитель; WITH = инструмент."
                ),
            },

            {
                "order": 24,
                "prompt": (
                    "Choose the fully correct sequence."
                ),
                "options": [
                    (
                        "The room is cleaned every day. / "
                        "The room was cleaned yesterday. / "
                        "The room will be cleaned tomorrow."
                    ),
                    (
                        "The room is clean every day by passive. / "
                        "The room did cleaned yesterday. / "
                        "The room will cleaned tomorrow."
                    ),
                    (
                        "The room are cleaned every day. / "
                        "The room was clean yesterday. / "
                        "The room will be cleaning tomorrow result."
                    ),
                    (
                        "The room does cleaned every day. / "
                        "The room were cleaned yesterday. / "
                        "The room will be clean by workers."
                    ),
                ],
                "answer": (
                    "The room is cleaned every day. / "
                    "The room was cleaned yesterday. / "
                    "The room will be cleaned tomorrow."
                ),
                "explanation": (
                    "Present: is + V3; Past: was + V3; "
                    "Future: will be + V3."
                ),
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
                "✅ A1 Lesson 41 seeded: Passive Voice"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
