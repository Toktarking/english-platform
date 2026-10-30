from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 19: "
        "Imperatives, requests and suggestions."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=19,
            defaults={
                "title": (
                    "Повелительное наклонение: "
                    "команды, просьбы и предложения"
                ),
                "slug": "imperatives-requests-suggestions",
                "theory_text": (
                    "Imperatives, requests and suggestions."
                ),
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое повелительное наклонение",
                "body": """Повелительное наклонение используется, когда мы:

даём команду;

просим что-то сделать;

даём инструкцию;

советуем;

запрещаем;

предлагаем сделать что-то вместе.

Примеры:

Open the door.

Sit down, please.

Don't touch that.

Let's begin.""",
            },

            {
                "order": 2,
                "title": "Положительная команда",
                "body": """Чтобы дать команду, используется обычная форма глагола без to.

Формула:

Глагол + остальная часть предложения

Примеры:

Come here.

Sit down.

Open the book.

Read the text.

Listen carefully.

Wait a minute.

Важно:

не нужно ставить to;

не нужно добавлять -s.""",
            },

            {
                "order": 3,
                "title": "Подлежащее YOU обычно не ставится",
                "body": """В обычной команде слово you не используется.

Неправильно:

You open the door.

Если это команда:

Open the door.

Подлежащее you подразумевается.

Другие примеры:

Stand up.

Close the window.

Write your name.

Turn left.

Call me tomorrow.""",
            },

            {
                "order": 4,
                "title": "PLEASE — вежливая просьба",
                "body": """Чтобы сделать команду мягче, добавляется please.

Примеры:

Please sit down.

Sit down, please.

Please open the window.

Wait here, please.

Please может стоять:

в начале;

в конце.

Сравните:

Close the door.

Please close the door.

Второй вариант звучит вежливее.""",
            },

            {
                "order": 5,
                "title": "Отрицательная команда",
                "body": """Чтобы запретить действие, используется:

Don't + глагол

Примеры:

Don't speak.

Don't run.

Don't open the door.

Don't touch this.

Don't be late.

Полная форма:

Do not + глагол

Она часто используется на знаках и в официальных инструкциях:

Do not enter.

Do not smoke.

Do not use your phone.""",
            },

            {
                "order": 6,
                "title": "После DON'T — базовая форма",
                "body": """После don't используется обычная форма глагола.

Правильно:

Don't go.

Don't speak.

Don't touch.

Неправильно:

Don't goes.

Don't speaking.

Don't to touch.

То же правило работает с be:

Don't be late.

Не:

Don't are late.

Не:

Don't being late.""",
            },

            {
                "order": 7,
                "title": "Команды с BE",
                "body": """Если команда относится к состоянию, используется be.

Примеры:

Be careful.

Be quiet.

Be patient.

Be ready.

Отрицание:

Don't be + прилагательное

Don't be late.

Don't be afraid.

Don't be rude.

Don't be nervous.""",
            },

            {
                "order": 8,
                "title": "Инструкции и указания",
                "body": """Повелительное наклонение часто используется в инструкциях.

Пример:

Open the box.

Take out the device.

Press the button.

Wait for ten seconds.

Turn the device off.

В рецептах:

Cut the vegetables.

Add some salt.

Mix the ingredients.

В указаниях дороги:

Go straight.

Turn left.

Turn right.

Cross the road.""",
            },

            {
                "order": 9,
                "title": "LET'S — давай / давайте",
                "body": """Let's используется, когда говорящий предлагает совместное действие.

Формула:

Let's + глагол

Примеры:

Let's go.

Let's start.

Let's study together.

Let's have lunch.

Let's ask the teacher.

После let's глагол используется без to.

Неправильно:

Let's to go.

Правильно:

Let's go.""",
            },

            {
                "order": 10,
                "title": "LET'S NOT",
                "body": """Чтобы предложить чего-то не делать:

Let's not + глагол

Примеры:

Let's not argue.

Let's not be late.

Let's not tell anyone.

Let's not go there.

Важно:

Неправильно:

Let's don't argue.

Правильно:

Let's not argue.""",
            },

            {
                "order": 11,
                "title": "LET ME, LET HIM, LET HER, LET THEM",
                "body": """Let me означает:

позвольте мне;

дай мне;

давайте я.

Примеры:

Let me help you.

Let me explain.

Let me check.

После let используется объектная форма:

let me;

let him;

let her;

let us;

let them.

Примеры:

Let him speak.

Let her decide.

Let them go.

Неправильно:

let he;

let she.""",
            },

            {
                "order": 12,
                "title": "ALWAYS и NEVER",
                "body": """Always можно использовать в советах и инструкциях:

Always wash your hands.

Always check your work.

Always wear a seat belt.

Never означает «никогда».

Never touch electrical wires.

Never open the door to strangers.

Never drive when you are tired.

После never используется обычный глагол.

Неправильно:

Never don't touch.

Правильно:

Never touch.""",
            },

            {
                "order": 13,
                "title": "Команда + AND / OR",
                "body": """После команды можно использовать and или or.

AND показывает результат:

Work hard and you will succeed.

Press this button and the machine will start.

OR часто выражает предупреждение:

Hurry up or you will be late.

Be careful or you will fall.

На знаках также часто встречаются:

Stop.

Keep out.

Do not enter.

No smoking.

Push.

Pull.""",
            },

            {
                "order": 14,
                "title": "Главное правило",
                "body": """Положительная команда:

глагол без to

Open the door.

Sit down.

Be careful.

Отрицательная команда:

Don't + глагол

Don't open the door.

Don't speak.

Don't be late.

Совместное предложение:

Let's + глагол

Let's begin.

Let's go.

Отрицательное предложение:

Let's not + глагол

Let's not argue.

Let's not be late.""",
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
                "prompt": "___ the door, please.",
                "options": ["Opens", "Open", "To open", "Opening"],
                "answer": "Open",
                "explanation": "В команде используется базовая форма глагола без to.",
            },

            {
                "order": 2,
                "prompt": "___ late.",
                "options": ["Don't be", "Don't is", "Not be", "Doesn't be"],
                "answer": "Don't be",
                "explanation": "Отрицательная команда с состоянием: Don't be.",
            },

            {
                "order": 3,
                "prompt": "___ your phone during the lesson.",
                "options": [
                    "Don't use",
                    "Doesn't use",
                    "Not use",
                    "Don't using",
                ],
                "answer": "Don't use",
                "explanation": "Don't + базовая форма use.",
            },

            {
                "order": 4,
                "prompt": "___ begin the lesson.",
                "options": ["Lets", "Let's", "Let's to", "Let us to"],
                "answer": "Let's",
                "explanation": "Для совместного предложения используется Let's + глагол.",
            },

            {
                "order": 5,
                "prompt": "Let's ___ home.",
                "options": ["to go", "goes", "go", "going"],
                "answer": "go",
                "explanation": "После let's используется базовая форма без to.",
            },

            {
                "order": 6,
                "prompt": "Let's not ___ about this now.",
                "options": ["talks", "talking", "to talk", "talk"],
                "answer": "talk",
                "explanation": "Let's not + базовая форма.",
            },

            {
                "order": 7,
                "prompt": "___ me help you.",
                "options": ["Let", "Lets", "Let's", "Allow to"],
                "answer": "Let",
                "explanation": "Правильно: Let me help you.",
            },

            {
                "order": 8,
                "prompt": "Never ___ this button.",
                "options": ["touching", "to touch", "touch", "touches"],
                "answer": "touch",
                "explanation": "После never в такой инструкции используется базовая форма.",
            },

            {
                "order": 9,
                "prompt": "___ your name here.",
                "options": ["Writes", "Write", "To write", "Writing"],
                "answer": "Write",
                "explanation": "Положительная команда начинается с базовой формы Write.",
            },

            {
                "order": 10,
                "prompt": "Please ___ quietly.",
                "options": ["speak", "speaks", "speaking", "to speak"],
                "answer": "speak",
                "explanation": "После please в просьбе используется базовая форма.",
            },

            {
                "order": 11,
                "prompt": "___ the window.",
                "options": [
                    "Don't opening",
                    "Don't open",
                    "Doesn't open",
                    "Not open",
                ],
                "answer": "Don't open",
                "explanation": "Отрицательная команда: Don't + open.",
            },

            {
                "order": 12,
                "prompt": "___ careful.",
                "options": ["Be", "Are", "Is", "Being"],
                "answer": "Be",
                "explanation": "Команда с состоянием: Be careful.",
            },

            {
                "order": 13,
                "prompt": "___ afraid.",
                "options": [
                    "Don't is",
                    "Don't be",
                    "Not being",
                    "Doesn't be",
                ],
                "answer": "Don't be",
                "explanation": "Правильно: Don't be afraid.",
            },

            {
                "order": 14,
                "prompt": "Let's ___ a break.",
                "options": ["having", "have", "has", "to have"],
                "answer": "have",
                "explanation": "После let's используется базовая форма have.",
            },

            {
                "order": 15,
                "prompt": "Let's not ___ time.",
                "options": ["wasting", "waste", "to waste", "wastes"],
                "answer": "waste",
                "explanation": "Let's not + waste.",
            },

            {
                "order": 16,
                "prompt": "___ me check the document.",
                "options": ["Lets", "Let", "Let's", "Allow"],
                "answer": "Let",
                "explanation": "Конструкция: Let me check.",
            },

            {
                "order": 17,
                "prompt": "Let ___ speak.",
                "options": ["he", "him", "his", "himself"],
                "answer": "him",
                "explanation": "После let используется объектная форма: him.",
            },

            {
                "order": 18,
                "prompt": "Please don't ___ loudly.",
                "options": ["talks", "speaking", "speak", "to speak"],
                "answer": "speak",
                "explanation": "После don't используется базовая форма speak.",
            },

            {
                "order": 19,
                "prompt": "Always ___ your seat belt.",
                "options": ["wear", "wears", "wearing", "to wear"],
                "answer": "wear",
                "explanation": "В инструкции после always используется базовая форма.",
            },

            {
                "order": 20,
                "prompt": "Never ___ personal information to strangers.",
                "options": ["gives", "giving", "give", "to give"],
                "answer": "give",
                "explanation": "Never + базовая форма give.",
            },

            {
                "order": 21,
                "prompt": "___ straight and turn left.",
                "options": ["Going", "Go", "Goes", "To go"],
                "answer": "Go",
                "explanation": "Указание дороги начинается с команды Go.",
            },

            {
                "order": 22,
                "prompt": "Hurry up, ___ you will be late.",
                "options": ["and", "but", "or", "because"],
                "answer": "or",
                "explanation": "Or передаёт предупреждение: иначе опоздаешь.",
            },

            {
                "order": 23,
                "prompt": "Press this button, ___ the machine will start.",
                "options": ["or", "and", "but", "because"],
                "answer": "and",
                "explanation": "And показывает результат выполнения команды.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "Let's don't argue.",
                    "Let's not argue.",
                    "Let's not to argue.",
                    "Let's doesn't argue.",
                ],
                "answer": "Let's not argue.",
                "explanation": "Отрицательная форма предложения с let's: Let's not + verb.",
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
                "✅ A1 Lesson 19 seeded: "
                "Повелительное наклонение"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
