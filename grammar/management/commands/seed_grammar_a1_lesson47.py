from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 47: "
        "First Conditional."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=47,
            defaults={
                "title": "First Conditional",
                "slug": "first-conditional",
                "theory_text": (
                    "First Conditional: "
                    "If + Present Simple, will + V1."
                ),
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое First Conditional",
                "body": """First Conditional используется, когда мы говорим о реальной возможности в будущем.

Он может выражать:

вероятный результат;

предупреждение;

обещание;

предложение;

план, зависящий от условия.

Пример:

If it rains tomorrow, we will stay at home.

Дождь возможен, но не гарантирован.

Результат зависит от условия.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Главная формула:

If + Present Simple, will + V1

Пример:

If I finish early, I will call you.

Условие:

If I finish early

Результат:

I will call you

Важно:

после IF используется Present Simple, хотя смысл относится к будущему.""",
            },

            {
                "order": 3,
                "title": "После IF нет WILL",
                "body": """Главное правило First Conditional:

после IF обычно не используется WILL.

Неправильно:

If I will finish early, I will call you.

Правильно:

If I finish early, I will call you.

Ещё пример:

If she comes tomorrow, we will talk.

Не:

If she will come tomorrow...""",
            },

            {
                "order": 4,
                "title": "Утверждение и отрицание",
                "body": """Утверждение:

If + Present Simple, will + V1

If she studies, she will pass.

Отрицание в условии:

If you don't hurry, you will miss the bus.

If she doesn't study, she will fail.

Отрицание в результате:

If it rains, we won't go out.

If she is tired, she won't come.

WILL NOT сокращается:

won't""",
            },

            {
                "order": 5,
                "title": "Порядок частей",
                "body": """Если IF-часть стоит первой, ставится запятая:

If it rains, we will stay at home.

Если результат стоит первым:

We will stay at home if it rains.

Запятая обычно не нужна.

Сравните:

If I finish early, I will call you.

I will call you if I finish early.

Смысл одинаковый.""",
            },

            {
                "order": 6,
                "title": "Вопросы в First Conditional",
                "body": """Можно задавать вопросы о результате.

Примеры:

What will you do if it rains?

Will you stay home if you feel ill?

Will she come if we invite her?

What will happen if they lose?

Формула специального вопроса:

Question word + will + subject + V1 + if + Present Simple?""",
            },

            {
                "order": 7,
                "title": "CAN, MAY, MIGHT вместо WILL",
                "body": """В результате можно использовать не только WILL.

CAN:

If you finish early, you can go home.

MAY:

If it rains, we may stay at home.

MIGHT:

If we leave late, we might miss the train.

Might обычно показывает менее уверенную возможность.

Важно:

не говорим will can или will might.""",
            },

            {
                "order": 8,
                "title": "MUST, SHOULD и Imperative",
                "body": """В результате можно использовать MUST:

If you feel worse, you must see a doctor.

SHOULD:

If you feel tired, you should rest.

Также возможен Imperative:

If you see Anna, tell her to call me.

If you feel tired, take a break.

If the door is locked, use the side entrance.

Такие конструкции выражают правило, совет или инструкцию.""",
            },

            {
                "order": 9,
                "title": "UNLESS",
                "body": """UNLESS означает:

если не.

Пример:

Unless you hurry, you will miss the bus.

Это равно:

If you don't hurry, you will miss the bus.

Важно:

не используйте двойное отрицание.

Неправильно:

Unless you don't hurry...

Правильно:

Unless you hurry...""",
            },

            {
                "order": 10,
                "title": "WHEN и IF",
                "body": """WHEN используется, если говорящий ожидает, что событие произойдёт.

When she arrives, we will start.

IF используется, если событие возможно, но не гарантировано.

If she arrives early, we will start sooner.

Сравните:

When I finish work, I will call you.

If I finish work early, I will call you.""",
            },

            {
                "order": 11,
                "title": "AFTER, BEFORE, AS SOON AS, UNTIL",
                "body": """После when, after, before, as soon as и until для будущего тоже обычно не используется WILL.

Правильно:

I will call you when I arrive.

We will eat after she comes.

I will finish this before I leave.

I will tell you as soon as I know.

We will wait until he arrives.

Не:

when I will arrive

after she will come""",
            },

            {
                "order": 12,
                "title": "Предупреждения, обещания и планы",
                "body": """First Conditional часто используется для предупреждений:

If you drive too fast, you will have an accident.

Для обещаний:

If you help me, I will help you.

Для предложений:

If you are tired, I will drive.

Для планов:

If the weather is good, we will go to the park.

Во всех случаях результат зависит от условия.""",
            },

            {
                "order": 13,
                "title": "First Conditional и Zero Conditional",
                "body": """Zero Conditional описывает общий факт:

If you heat ice, it melts.

First Conditional описывает конкретную будущую ситуацию:

If you leave this ice in the sun, it will melt.

Сравните:

If I drink coffee at night, I can't sleep.
— обычная реакция.

If I drink coffee tonight, I won't sleep.
— конкретная ситуация сегодня.""",
            },

            {
                "order": 14,
                "title": "Как выбрать First Conditional",
                "body": """Задайте три вопроса.

1. Ситуация относится к будущему?

2. Она реальна или возможна?

3. Результат зависит от условия?

Если да:

используйте First Conditional.

Основная формула:

If + Present Simple, will + V1

Пример:

If I have time, I will help you.

Также в результате возможны:

can;

may;

might;

must;

should;

imperative.""",
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
                "prompt": "If I ___ time, I will help you.",
                "options": [
                    "have",
                    "will have",
                    "had",
                    "having",
                ],
                "answer": "have",
                "explanation": (
                    "После if используется Present Simple."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "If she ___ early, we will start at once."
                ),
                "options": [
                    "arrive",
                    "arrives",
                    "will arrive",
                    "arrived",
                ],
                "answer": "arrives",
                "explanation": (
                    "She → arrives; после if нет will."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "If they don't leave now, they ___ late."
                ),
                "options": [
                    "are always",
                    "will be",
                    "were",
                    "will being",
                ],
                "answer": "will be",
                "explanation": (
                    "Результат будущего → will be."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "If he studies hard, he ___ the exam."
                ),
                "options": [
                    "passes every year",
                    "will pass",
                    "passed",
                    "will passing",
                ],
                "answer": "will pass",
                "explanation": (
                    "Вероятный будущий результат → will + V1."
                ),
            },

            {
                "order": 5,
                "prompt": "If it is sunny, we ___ to the park.",
                "options": [
                    "will go",
                    "went",
                    "goes",
                    "will going",
                ],
                "answer": "will go",
                "explanation": (
                    "Will + base verb: will go."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "If you don't wear a coat, you ___ cold."
                ),
                "options": [
                    "will get",
                    "got",
                    "get yesterday",
                    "will getting",
                ],
                "answer": "will get",
                "explanation": (
                    "Предупреждение о будущем → will get."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "If she calls, I ___ her the news."
                ),
                "options": [
                    "tell yesterday",
                    "will tell",
                    "told",
                    "will told",
                ],
                "answer": "will tell",
                "explanation": (
                    "Will + V1: will tell."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "If you finish the task, you ___ leave."
                ),
                "options": [
                    "can",
                    "will can",
                    "can to",
                    "will able",
                ],
                "answer": "can",
                "explanation": (
                    "После if-clause в результате можно использовать can."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "If he feels worse, he ___ see a doctor."
                ),
                "options": [
                    "must",
                    "will must",
                    "must to",
                    "musts",
                ],
                "answer": "must",
                "explanation": (
                    "Необходимость → must + V1."
                ),
            },

            {
                "order": 10,
                "prompt": "If you are tired, ___.",
                "options": [
                    "rest",
                    "will resting",
                    "rested",
                    "to rest",
                ],
                "answer": "rest",
                "explanation": (
                    "В результате возможен imperative."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "I will call you as soon as I ___ the answer."
                ),
                "options": [
                    "will know",
                    "know",
                    "knew",
                    "knowing",
                ],
                "answer": "know",
                "explanation": (
                    "После as soon as для будущего используется Present Simple."
                ),
            },

            {
                "order": 12,
                "prompt": "We will wait until she ___.",
                "options": [
                    "will arrive",
                    "arrives",
                    "arrived",
                    "arriving",
                ],
                "answer": "arrives",
                "explanation": (
                    "После until используется Present Simple."
                ),
            },

            {
                "order": 13,
                "prompt": (
                    "Unless you ___, you will not improve."
                ),
                "options": [
                    "practise",
                    "will practise",
                    "practised",
                    "practising",
                ],
                "answer": "practise",
                "explanation": (
                    "Unless + Present Simple."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "What will you do if you ___ the bus?"
                ),
                "options": [
                    "miss",
                    "will miss",
                    "missed",
                    "missing",
                ],
                "answer": "miss",
                "explanation": (
                    "После if используется Present Simple."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "If the weather improves, we ___ go out."
                ),
                "options": [
                    "might",
                    "might to",
                    "will might",
                    "mights",
                ],
                "answer": "might",
                "explanation": (
                    "Might + V1 выражает менее уверенную возможность."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "If she will come, we will start.",
                    "If she comes, we will start.",
                    "If she coming, we will start.",
                    "If she came tomorrow, we will start.",
                ],
                "answer": "If she comes, we will start.",
                "explanation": (
                    "После if в First Conditional нет will."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "If he call, I will answer.",
                    "If he calls, I will answer.",
                    "If he will calls, I answer.",
                    "If he calling, I will answer.",
                ],
                "answer": "If he calls, I will answer.",
                "explanation": (
                    "He → calls в Present Simple."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "If she doesn't studies, she will fail.",
                    "If she doesn't study, she will fail.",
                    "If she won't study, she will fail.",
                    "If she not study, she will fail.",
                ],
                "answer": (
                    "If she doesn't study, she will fail."
                ),
                "explanation": (
                    "После doesn't используется base verb."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct sentence with UNLESS.",
                "options": [
                    "Unless you don't hurry, you will be late.",
                    "Unless you hurry, you will be late.",
                    "Unless you will hurry, you will be late.",
                    "Unless not hurry, you will be late.",
                ],
                "answer": (
                    "Unless you hurry, you will be late."
                ),
                "explanation": (
                    "Unless уже содержит отрицательное значение."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the correct sentence with WHEN.",
                "options": [
                    "I will call you when I will arrive.",
                    "I will call you when I arrive.",
                    "I call you when I will arrive tomorrow.",
                    "I will calling you when I arrive.",
                ],
                "answer": (
                    "I will call you when I arrive."
                ),
                "explanation": (
                    "После when для будущего используется Present Simple."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "Which sentence is Zero Conditional?"
                ),
                "options": [
                    "If you heat ice, it melts.",
                    "If you leave this ice in the sun, it will melt.",
                    "If you heated the ice, it melted yesterday.",
                    "If you will heat ice, it melts.",
                ],
                "answer": "If you heat ice, it melts.",
                "explanation": (
                    "Общий факт → Zero Conditional."
                ),
            },

            {
                "order": 22,
                "prompt": (
                    "Which sentence is First Conditional?"
                ),
                "options": [
                    "If I drink coffee at night, I can't sleep.",
                    "If I drink coffee tonight, I won't sleep.",
                    "If I drank coffee yesterday, I couldn't sleep.",
                    "When I drink coffee, I feel awake.",
                ],
                "answer": (
                    "If I drink coffee tonight, I won't sleep."
                ),
                "explanation": (
                    "Конкретная возможная ситуация в будущем."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct future time-clause pair."
                ),
                "options": [
                    (
                        "I will call you when I arrive. / "
                        "We will start as soon as she comes."
                    ),
                    (
                        "I will call you when I will arrive. / "
                        "We will start as soon as she will come."
                    ),
                    (
                        "I call you when I will arrive. / "
                        "We starting when she comes."
                    ),
                    (
                        "I will calling when I arrive. / "
                        "We will start as soon as she coming."
                    ),
                ],
                "answer": (
                    "I will call you when I arrive. / "
                    "We will start as soon as she comes."
                ),
                "explanation": (
                    "После when/as soon as используется Present Simple."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "If I have time, I will help you. / "
                        "If you finish, you can leave. / "
                        "If you feel tired, you should rest. / "
                        "If you see Anna, tell her."
                    ),
                    (
                        "If I will have time, I will help you. / "
                        "If you finish, you will can leave. / "
                        "If you feel tired, you will should rest. / "
                        "If you see Anna, to tell her."
                    ),
                    (
                        "If I had time tomorrow, I will help. / "
                        "If you finishing, can leave. / "
                        "If you feel tired, should to rest. / "
                        "If Anna, telling her."
                    ),
                    (
                        "If I have time, I will to help. / "
                        "If you finish, can to leave. / "
                        "If you feels tired, you should rests. / "
                        "If you see Anna, will tell imperative."
                    ),
                ],
                "answer": (
                    "If I have time, I will help you. / "
                    "If you finish, you can leave. / "
                    "If you feel tired, you should rest. / "
                    "If you see Anna, tell her."
                ),
                "explanation": (
                    "В результате First Conditional возможны "
                    "will, can, should и imperative."
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
                "✅ A1 Lesson 47 seeded: First Conditional"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
