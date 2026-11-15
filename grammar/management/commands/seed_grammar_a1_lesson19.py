from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 19: Imperatives, requests and suggestions."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=19,

                defaults={
                    "title":
                        "Повелительное наклонение: "
                        "команды, просьбы и предложения",

                    "slug":
                        "imperatives-requests-suggestions",

                    "theory_text":
                        "Imperatives, requests and suggestions.",

                    "estimated_minutes":
                        17,

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
                    "Команда = глагол без TO",

                "body":
                    """Чтобы дать команду или инструкцию, начинаем с базовой формы глагола.

Open the door.

Sit down.

Read the text.

Listen carefully.

Wait a minute.

Не нужно:

TO

окончание -S

ING

Не:

To open the door.

Opens the door.

А:

Open the door.""",
            },


            {
                "order": 2,

                "title":
                    "YOU обычно не ставится",

                "body":
                    """В обычной команде подлежащее YOU подразумевается.

Не:

You open the window.

Если это команда:

Open the window.

Другие примеры:

Stand up.

Write your name.

Turn left.

Call me tomorrow.

Человек уже понимает, что команда обращена к нему.""",
            },


            {
                "order": 3,

                "title":
                    "PLEASE делает просьбу вежливее",

                "body":
                    """PLEASE смягчает команду.

Close the door.

Более вежливо:

Please close the door.

или:

Close the door, please.

PLEASE может стоять:

в начале

или

в конце просьбы.

Примеры:

Please sit down.

Wait here, please.

Please speak slowly.""",
            },


            {
                "order": 4,

                "title":
                    "DON'T + глагол",

                "body":
                    """Для запрета используется:

DON'T + base verb

Don't speak.

Don't run.

Don't open the door.

Don't touch this.

После DON'T глагол остаётся в базовой форме.

Не:

Don't goes.

Don't speaking.

Don't to touch.

Полная форма:

DO NOT

Do not enter.

Do not smoke.""",
            },


            {
                "order": 5,

                "title":
                    "BE и DON'T BE",

                "body":
                    """Если команда описывает состояние, используется BE.

Be careful.

Be quiet.

Be patient.

Be ready.

Отрицание:

DON'T BE

Don't be late.

Don't be afraid.

Don't be nervous.

Не:

Don't are late.

Don't being late.""",
            },


            {
                "order": 6,

                "title":
                    "Инструкции и направления",

                "body":
                    """Imperative очень часто используется в инструкциях.

Техника:

Press the button.

Wait ten seconds.

Turn the device off.

Рецепт:

Cut the vegetables.

Add some salt.

Mix the ingredients.

Дорога:

Go straight.

Turn left.

Turn right.

Cross the road.

Все эти команды начинаются с базовой формы глагола.""",
            },


            {
                "order": 7,

                "title":
                    "LET'S = давай / давайте",

                "body":
                    """LET'S используется для совместного предложения.

Let's go.

Let's start.

Let's study together.

Let's have lunch.

После LET'S используется базовая форма без TO.

Не:

Let's to go.

А:

Let's go.

Формула:

LET'S + base verb.""",
            },


            {
                "order": 8,

                "title":
                    "LET'S NOT = давай не будем",

                "body":
                    """Чтобы предложить чего-то не делать:

LET'S NOT + base verb

Let's not argue.

Let's not be late.

Let's not tell anyone.

Let's not go there.

Не:

Let's don't argue.

Не:

Let's not to argue.

Правильно:

Let's not argue.""",
            },


            {
                "order": 9,

                "title":
                    "LET ME / HIM / HER / THEM",

                "body":
                    """LET может означать «позволь».

Let me help you.

Let me explain.

Let him speak.

Let her decide.

Let them go.

После LET используется объектная форма:

me

him

her

us

them

Не:

let he

let she

А:

let him

let her.""",
            },


            {
                "order": 10,

                "title":
                    "ALWAYS, NEVER, AND и OR",

                "body":
                    """Советы:

Always check your work.

Always wear a seat belt.

Запрет через NEVER:

Never touch electrical wires.

Never give personal information to strangers.

Не:

Never don't touch.

После команды можно показать результат через AND:

Press this button and the machine will start.

OR часто означает предупреждение:

Hurry up or you will be late.

Be careful or you will fall.""",
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
                    "___ the door.",

                "options": [
                    "Opens",
                    "Open",
                    "To open",
                    "Opening",
                ],

                "answer":
                    "Open",

                "explanation":
                    "Команда начинается с базовой формы OPEN.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "fill",

                "prompt":
                    "___ your name here. (write)",

                "options": [],

                "answer":
                    "Write",

                "explanation":
                    "В imperative используется базовая форма WRITE.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the natural command.",

                "options": [
                    "You sit down.",
                    "Sit down.",
                    "You are sit down.",
                    "To sit down.",
                ],

                "answer":
                    "Sit down.",

                "explanation":
                    "В обычной команде YOU не требуется.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери команду.",

                "options": [
                    "Turn",
                    "left",
                    "at",
                    "the",
                    "corner",
                ],

                "answer":
                    "Turn left at the corner",

                "explanation":
                    "Команда начинается с TURN.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "Choose the more polite request.",

                "options": [
                    "Close the window.",
                    "Please close the window.",
                    "You close the window.",
                    "To close the window.",
                ],

                "answer":
                    "Please close the window.",

                "explanation":
                    "PLEASE делает просьбу более вежливой.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "___ speak more slowly.",

                "options": [
                    "Please",
                    "Does",
                    "Are",
                    "To",
                ],

                "answer":
                    "Please",

                "explanation":
                    "PLEASE + base verb используется для вежливой просьбы.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "___ your phone during the lesson.",

                "options": [
                    "Don't use",
                    "Doesn't use",
                    "Don't using",
                    "Not use",
                ],

                "answer":
                    "Don't use",

                "explanation":
                    "Запрет: DON'T + USE.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct negative command.",

                "options": [
                    "Don't touches it.",
                    "Don't touch it.",
                    "Don't touching it.",
                    "Doesn't touch it.",
                ],

                "answer":
                    "Don't touch it.",

                "explanation":
                    "После DON'T используется базовая форма TOUCH.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "___ careful.",

                "options": [
                    "Be",
                    "Are",
                    "Is",
                    "Being",
                ],

                "answer":
                    "Be",

                "explanation":
                    "С состоянием используем команду BE CAREFUL.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "___ late.",

                "options": [
                    "Don't be",
                    "Don't is",
                    "Doesn't be",
                    "Not being",
                ],

                "answer":
                    "Don't be",

                "explanation":
                    "Отрицательная команда с состоянием → DON'T BE.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "___ straight for 200 metres.",

                "options": [
                    "Going",
                    "Go",
                    "Goes",
                    "To go",
                ],

                "answer":
                    "Go",

                "explanation":
                    "Указание дороги начинается с GO.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "First, ___ the vegetables.",

                "options": [
                    "cut",
                    "cuts",
                    "cutting",
                    "to cut",
                ],

                "answer":
                    "cut",

                "explanation":
                    "Инструкция использует базовую форму CUT.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Let's ___ lunch.",

                "options": [
                    "having",
                    "have",
                    "has",
                    "to have",
                ],

                "answer":
                    "have",

                "explanation":
                    "После LET'S используется базовая форма HAVE.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct suggestion.",

                "options": [
                    "Let's to start.",
                    "Let's start.",
                    "Let's starts.",
                    "Let's starting.",
                ],

                "answer":
                    "Let's start.",

                "explanation":
                    "LET'S + base verb.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Let's not ___ about it now.",

                "options": [
                    "talk",
                    "talks",
                    "talking",
                    "to talk",
                ],

                "answer":
                    "talk",

                "explanation":
                    "LET'S NOT + base verb.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "Let's don't argue.",
                    "Let's not argue.",
                    "Let's not to argue.",
                    "Let's doesn't argue.",
                ],

                "answer":
                    "Let's not argue.",

                "explanation":
                    "Правильная отрицательная форма — LET'S NOT.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "___ me help you.",

                "options": [
                    "Let",
                    "Lets",
                    "Let's",
                    "To let",
                ],

                "answer":
                    "Let",

                "explanation":
                    "Конструкция: LET ME HELP YOU.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Let ___ speak.",

                "options": [
                    "he",
                    "him",
                    "his",
                    "himself",
                ],

                "answer":
                    "him",

                "explanation":
                    "После LET используется объектная форма HIM.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Never ___ personal information to strangers.",

                "options": [
                    "gives",
                    "give",
                    "giving",
                    "to give",
                ],

                "answer":
                    "give",

                "explanation":
                    "После NEVER в инструкции используется базовая форма GIVE.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Hurry up, ___ you will be late.",

                "options": [
                    "and",
                    "or",
                    "because",
                    "so",
                ],

                "answer":
                    "or",

                "explanation":
                    "OR показывает предупреждение: иначе опоздаешь.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "___ the light, please.",

                "options": [
                    "Turn on",
                    "Turns on",
                    "To turn on",
                    "Turning on",
                ],

                "answer":
                    "Turn on",

                "explanation":
                    "Imperative начинается с базовой формы TURN.",
            },


            {
                "order": 22,

                "prompt":
                    "Choose the correct command.",

                "options": [
                    "You wait here.",
                    "Wait here.",
                    "You are wait here.",
                    "To wait here.",
                ],

                "answer":
                    "Wait here.",

                "explanation":
                    "YOU в обычной команде не ставится.",
            },


            {
                "order": 23,

                "prompt":
                    "___ this door.",

                "options": [
                    "Don't opens",
                    "Don't open",
                    "Doesn't open",
                    "Don't opening",
                ],

                "answer":
                    "Don't open",

                "explanation":
                    "Отрицательная команда → DON'T + OPEN.",
            },


            {
                "order": 24,

                "prompt":
                    "___ nervous.",

                "options": [
                    "Don't be",
                    "Don't are",
                    "Doesn't be",
                    "Not being",
                ],

                "answer":
                    "Don't be",

                "explanation":
                    "Состояние в отрицательной команде → DON'T BE.",
            },


            {
                "order": 25,

                "prompt":
                    "Choose the correct instruction.",

                "options": [
                    "Press the button.",
                    "Presses the button.",
                    "To press the button.",
                    "Pressing the button.",
                ],

                "answer":
                    "Press the button.",

                "explanation":
                    "Инструкция использует базовую форму PRESS.",
            },


            {
                "order": 26,

                "prompt":
                    "Let's ___ the teacher.",

                "options": [
                    "ask",
                    "asks",
                    "asking",
                    "to ask",
                ],

                "answer":
                    "ask",

                "explanation":
                    "LET'S + base verb.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct negative suggestion.",

                "options": [
                    "Let's don't go there.",
                    "Let's not go there.",
                    "Let's not to go there.",
                    "Let's doesn't go there.",
                ],

                "answer":
                    "Let's not go there.",

                "explanation":
                    "Отрицательное предложение → LET'S NOT + GO.",
            },


            {
                "order": 28,

                "prompt":
                    "Let ___ decide.",

                "options": [
                    "she",
                    "her",
                    "hers",
                    "herself",
                ],

                "answer":
                    "her",

                "explanation":
                    "После LET используется объектная форма HER.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct safety instruction.",

                "options": [
                    "Never don't touch the wires.",
                    "Never touch the wires.",
                    "Never touching the wires.",
                    "Never to touch the wires.",
                ],

                "answer":
                    "Never touch the wires.",

                "explanation":
                    "NEVER уже выражает запрет; затем идёт базовая форма.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct pair.",

                "options": [
                    "Press this button and the machine will start. / Hurry up or you will be late.",
                    "Press this button or the machine will start. / Hurry up and you will be late.",
                    "Presses this button and the machine starts. / Hurry up or you are late.",
                    "To press this button and the machine will start. / Hurrying up or you will be late.",
                ],

                "answer":
                    "Press this button and the machine will start. / Hurry up or you will be late.",

                "explanation":
                    "AND показывает результат, OR — предупреждение.",
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
                "✅ Interactive A1 Lesson 19 seeded"
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
