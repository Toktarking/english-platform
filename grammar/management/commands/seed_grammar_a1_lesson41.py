from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 41: Passive Voice."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=41,
            defaults={
                "title":
                    "Пассивный залог — Passive Voice",

                "slug":
                    "passive-voice",

                "theory_text":
                    "Passive Voice: be + Past Participle.",

                "estimated_minutes":
                    20,

                "pass_score":
                    70,

                "xp_reward":
                    100,

                "is_published":
                    True,
            },
        )


        # =================================================
        # 10 MICRO RULES
        # =================================================

        sections = [

            {
                "order": 1,
                "title":
                    "Active и Passive",

                "body":
                    """Active Voice:

человек или предмет
сам выполняет действие.

The chef cooks the food.

Passive Voice:

важно то,
над чем выполняют действие.

The food is cooked.

Сравни:

They clean the room.

The room is cleaned.""",
            },


            {
                "order": 2,
                "title":
                    "Главная формула: BE + V3",

                "body":
                    """Основа Passive Voice:

BE + V3

Например:

is made

was built

will be sent

Смысловой глагол
ставится в третью форму.

write → written

make → made

build → built

send → sent.""",
            },


            {
                "order": 3,
                "title":
                    "Present Simple Passive",

                "body":
                    """Формула:

AM / IS / ARE + V3

The office is cleaned every day.

These cars are made in Japan.

Выбираем:

один предмет → IS

несколько → ARE

Пример:

The document is checked.

The documents are checked.""",
            },


            {
                "order": 4,
                "title":
                    "Past Simple Passive",

                "body":
                    """Формула:

WAS / WERE + V3

The bridge was built in 2010.

The letters were sent yesterday.

Один предмет:

WAS

Несколько:

WERE

Главное:

Past Simple Passive
= WAS/WERE + V3.""",
            },


            {
                "order": 5,
                "title":
                    "Future Simple Passive",

                "body":
                    """Формула:

WILL BE + V3

The work will be finished tomorrow.

The results will be published next week.

Отрицание:

WON'T BE + V3

The meeting won't be cancelled.""",
            },


            {
                "order": 6,
                "title":
                    "Passive с модальными глаголами",

                "body":
                    """После модального глагола:

modal + BE + V3

The form must be completed.

The report should be checked.

This machine can be used.

The meeting may be cancelled.

Важно:

must be done

не:

must done.""",
            },


            {
                "order": 7,
                "title":
                    "Действие происходит сейчас",

                "body":
                    """Если действие происходит
прямо сейчас:

AM / IS / ARE
+ BEING
+ V3

The room is being cleaned now.

The road is being repaired.

Слово BEING показывает,
что процесс идёт сейчас.""",
            },


            {
                "order": 8,
                "title":
                    "Результат уже готов",

                "body":
                    """Present Perfect Passive:

HAVE / HAS BEEN + V3

The report has been completed.

The documents have been sent.

Один предмет:

HAS BEEN

Несколько:

HAVE BEEN

Главное:

результат уже получен.""",
            },


            {
                "order": 9,
                "title":
                    "BY и WITH",

                "body":
                    """BY показывает,
кто выполнил действие.

The book was written
by George Orwell.

WITH показывает инструмент.

The bread was cut
with a knife.

Коротко:

BY → исполнитель

WITH → инструмент.""",
            },


            {
                "order": 10,
                "title":
                    "Как превратить Active в Passive",

                "body":
                    """Active:

They clean the room.

Шаг 1:

объект ставим первым.

The room...

Шаг 2:

определяем время.

clean → Present Simple

Шаг 3:

добавляем BE + V3.

The room is cleaned.

Ещё пример:

They built the house.

→ The house was built.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = GrammarLessonSection.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "title":
                        data["title"],
                    "body":
                        data["body"],
                },
            )

            section_objects[
                data["order"]
            ] = section


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            # SECTION 1
            {
                "order": 1,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Which sentence is Passive Voice?",
                "options": [
                    "The room is cleaned every day.",
                    "They clean the room every day.",
                    "She cleans the office.",
                    "We wash the car.",
                ],
                "answer":
                    "The room is cleaned every day.",
                "explanation":
                    "IS CLEANED = BE + V3 → Passive Voice.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "They make these cars in Japan. Choose the passive idea.",
                "options": [
                    "These cars are made in Japan.",
                    "These cars make in Japan.",
                    "Japan makes these cars passive.",
                    "These cars are making in Japan.",
                ],
                "answer":
                    "These cars are made in Japan.",
                "explanation":
                    "Объект THESE CARS становится подлежащим Passive.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "What is the basic Passive Voice formula?",
                "options": [
                    "be + V3",
                    "do + V1",
                    "have + V1",
                    "will + V-ing",
                ],
                "answer":
                    "be + V3",
                "explanation":
                    "Основа Passive Voice → BE + Past Participle.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "Choose the correct V3 of WRITE.",
                "options": [
                    "written",
                    "wrote",
                    "write",
                    "writing",
                ],
                "answer":
                    "written",
                "explanation":
                    "WRITE → WROTE → WRITTEN.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "The office ___ every day.",
                "options": [
                    "is cleaned",
                    "are cleaned",
                    "is cleaning",
                    "clean",
                ],
                "answer":
                    "is cleaned",
                "explanation":
                    "OFFICE — единственное число → IS + V3.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "The documents ___ carefully.",
                "options": [
                    "are checked",
                    "is checked",
                    "are checking",
                    "checks",
                ],
                "answer":
                    "are checked",
                "explanation":
                    "DOCUMENTS — множественное число → ARE + V3.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "The house ___ in 1995.",
                "options": [
                    "was built",
                    "is built",
                    "was building",
                    "built",
                ],
                "answer":
                    "was built",
                "explanation":
                    "Past Simple Passive → WAS + V3.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "The invitations ___ yesterday.",
                "options": [
                    "were sent",
                    "was sent",
                    "are sent",
                    "were sending",
                ],
                "answer":
                    "were sent",
                "explanation":
                    "INVITATIONS — plural → WERE + V3.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "The results ___ tomorrow.",
                "options": [
                    "will be published",
                    "will published",
                    "will be publish",
                    "are publish",
                ],
                "answer":
                    "will be published",
                "explanation":
                    "Future Passive → WILL BE + V3.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "build",
                "prompt":
                    "Собери Future Passive.",
                "options": [
                    "The",
                    "letter",
                    "will",
                    "be",
                    "sent",
                ],
                "answer":
                    "The letter will be sent",
                "explanation":
                    "WILL + BE + SENT.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "The form must ___.",
                "options": [
                    "be completed",
                    "completed",
                    "be complete",
                    "to be completed",
                ],
                "answer":
                    "be completed",
                "explanation":
                    "Modal Passive → MUST + BE + V3.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "This machine can ___ safely.",
                "options": [
                    "be used",
                    "used",
                    "be use",
                    "using",
                ],
                "answer":
                    "be used",
                "explanation":
                    "CAN + BE + V3.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "The road ___ now.",
                "options": [
                    "is being repaired",
                    "is repaired yesterday",
                    "is repairing",
                    "has repair",
                ],
                "answer":
                    "is being repaired",
                "explanation":
                    "Действие идёт сейчас → IS BEING + V3.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "The rooms ___ right now.",
                "options": [
                    "are being cleaned",
                    "is being cleaned",
                    "are cleaning themselves",
                    "have cleaned",
                ],
                "answer":
                    "are being cleaned",
                "explanation":
                    "ROOMS → ARE BEING + V3.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "The report ___ already ___.",
                "options": [
                    "has / been completed",
                    "has / completed",
                    "is / been completed",
                    "was / completing",
                ],
                "answer":
                    "has / been completed",
                "explanation":
                    "Present Perfect Passive → HAS BEEN + V3.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "The emails ___ already ___.",
                "options": [
                    "have / been sent",
                    "has / been sent",
                    "have / sent",
                    "are / been sent",
                ],
                "answer":
                    "have / been sent",
                "explanation":
                    "EMAILS → HAVE BEEN + V3.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "The novel was written ___ George Orwell.",
                "options": [
                    "by",
                    "with",
                    "from",
                    "at",
                ],
                "answer":
                    "by",
                "explanation":
                    "BY показывает исполнителя.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "The bread was cut ___ a knife.",
                "options": [
                    "with",
                    "by",
                    "from",
                    "of",
                ],
                "answer":
                    "with",
                "explanation":
                    "WITH показывает инструмент.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "They clean the room every day. Choose the passive form.",
                "options": [
                    "The room is cleaned every day.",
                    "The room cleans every day.",
                    "The room was cleaned every day.",
                    "The room is cleaning every day.",
                ],
                "answer":
                    "The room is cleaned every day.",
                "explanation":
                    "Present Simple → IS + V3.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "They built the school in 2010. Choose the passive form.",
                "options": [
                    "The school was built in 2010.",
                    "The school is built in 2010.",
                    "The school was building in 2010.",
                    "The school built in 2010.",
                ],
                "answer":
                    "The school was built in 2010.",
                "explanation":
                    "Past Simple → WAS + V3.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "Coffee ___ in many countries.",
                "options": [
                    "is grown",
                    "grows passive",
                    "is growing every year",
                    "was grow",
                ],
                "answer":
                    "is grown",
                "explanation":
                    "Present Simple Passive → IS + V3.",
            },

            {
                "order": 22,
                "prompt":
                    "These products ___ in Kazakhstan.",
                "options": [
                    "are made",
                    "is made",
                    "are making",
                    "made are",
                ],
                "answer":
                    "are made",
                "explanation":
                    "PRODUCTS — plural → ARE + V3.",
            },

            {
                "order": 23,
                "prompt":
                    "The window ___ last night.",
                "options": [
                    "was broken",
                    "is broken tomorrow",
                    "was broke",
                    "was breaking itself",
                ],
                "answer":
                    "was broken",
                "explanation":
                    "BREAK → BROKE → BROKEN; Past Passive → WAS BROKEN.",
            },

            {
                "order": 24,
                "prompt":
                    "The new building ___ next year.",
                "options": [
                    "will be opened",
                    "will opened",
                    "will be open by workers",
                    "will opening",
                ],
                "answer":
                    "will be opened",
                "explanation":
                    "Future Passive → WILL BE + V3.",
            },

            {
                "order": 25,
                "prompt":
                    "The problem should ___.",
                "options": [
                    "be solved",
                    "solved",
                    "be solve",
                    "to solve",
                ],
                "answer":
                    "be solved",
                "explanation":
                    "SHOULD + BE + V3.",
            },

            {
                "order": 26,
                "prompt":
                    "Look! The car ___ right now.",
                "options": [
                    "is being washed",
                    "is washed yesterday",
                    "is washing",
                    "has washed",
                ],
                "answer":
                    "is being washed",
                "explanation":
                    "Процесс идёт сейчас → IS BEING + V3.",
            },

            {
                "order": 27,
                "prompt":
                    "The work ___ already ___.",
                "options": [
                    "has / been finished",
                    "has / finished",
                    "is / been finished",
                    "was / finish",
                ],
                "answer":
                    "has / been finished",
                "explanation":
                    "Present Perfect Passive → HAS BEEN + V3.",
            },

            {
                "order": 28,
                "prompt":
                    "Choose the correct BY / WITH pair.",
                "options": [
                    "The song was written by Anna. / The door was opened with a key.",
                    "The song was written with Anna. / The door was opened by a key.",
                    "The song was written from Anna. / The door was opened of a key.",
                    "The song was written by a pen. / The door was opened with Anna.",
                ],
                "answer":
                    "The song was written by Anna. / The door was opened with a key.",
                "explanation":
                    "BY = исполнитель; WITH = инструмент.",
            },

            {
                "order": 29,
                "prompt":
                    "They will send the documents tomorrow. Choose the passive form.",
                "options": [
                    "The documents will be sent tomorrow.",
                    "The documents will sent tomorrow.",
                    "The documents are sent yesterday.",
                    "The documents will be sending tomorrow.",
                ],
                "answer":
                    "The documents will be sent tomorrow.",
                "explanation":
                    "Future Simple Passive → WILL BE + SENT.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "The room is cleaned every day. / It was cleaned yesterday. / It will be cleaned tomorrow.",
                    "The room is clean every day. / It did cleaned yesterday. / It will cleaned tomorrow.",
                    "The room are cleaned every day. / It was clean yesterday. / It will be cleaning tomorrow.",
                    "The room does cleaned every day. / It were cleaned yesterday. / It will be clean tomorrow.",
                ],
                "answer":
                    "The room is cleaned every day. / It was cleaned yesterday. / It will be cleaned tomorrow.",
                "explanation":
                    "Present → IS + V3; Past → WAS + V3; Future → WILL BE + V3.",
            },

        ]


        all_exercises = training + final_test

        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

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


        # Remove old exercises
        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        # Remove old sections
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
                "✅ Interactive A1 Lesson 41 seeded"
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
