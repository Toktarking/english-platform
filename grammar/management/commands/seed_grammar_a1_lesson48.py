from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 48: "
        "Second Conditional."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=48,
            defaults={
                "title": "Second Conditional",
                "slug": "second-conditional",
                "theory_text": (
                    "Second Conditional: "
                    "If + Past Simple, would + V1."
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
                "title": "Что такое Second Conditional",
                "body": """Second Conditional используется для:

маловероятных ситуаций;

воображаемых ситуаций;

нереального настоящего;

гипотетического будущего;

мечтаний;

советов.

Пример:

If I had more money, I would buy a new car.

Сейчас денег недостаточно.

Ситуация воображаемая или маловероятная.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Главная формула:

If + Past Simple, would + V1

Пример:

If I had more time, I would travel more.

Условие:

If I had more time

Результат:

I would travel more

Важно:

Past Simple здесь часто не означает прошлое.

Он показывает дистанцию от реальности.""",
            },

            {
                "order": 3,
                "title": "Нереальное настоящее",
                "body": """Second Conditional часто описывает ситуацию, которая сейчас не соответствует реальности.

Пример:

If I knew the answer, I would tell you.

Реальность:

I don't know the answer.

Ещё примеры:

If I had a car, I would drive to work.

If she spoke English, she would apply for the job.

If we lived closer, we would visit you more often.""",
            },

            {
                "order": 4,
                "title": "Маловероятное будущее",
                "body": """Second Conditional можно использовать для будущего, если ситуация возможна, но маловероятна.

Пример:

If I won the lottery, I would buy a house.

Выиграть теоретически возможно, но вероятность небольшая.

Ещё примеры:

If we moved abroad, we would learn another language.

If they invited me, I would go.

If he found a better job, he would leave.""",
            },

            {
                "order": 5,
                "title": "Отрицание",
                "body": """В IF-части:

didn't + V1

If I didn't work so much, I would have more free time.

If she didn't live so far away, we would visit more often.

Важно:

после DIDN'T используется первая форма.

Правильно:

If she didn't work...

Не:

If she didn't worked...

В результате:

wouldn't + V1

If I were you, I wouldn't do that.""",
            },

            {
                "order": 6,
                "title": "IF I WERE",
                "body": """В Second Conditional часто используется WERE.

Особенно в стандартном английском:

If I were rich, I would travel the world.

If I were you, I would apologise.

If she were here, she would know what to do.

В гипотетических конструкциях возможны:

if I were

if he were

if she were

if it were

В учебных заданиях лучше использовать WERE.""",
            },

            {
                "order": 7,
                "title": "IF I WERE YOU — совет",
                "body": """Очень частая модель для совета:

If I were you, I would...

Перевод:

На твоём месте я бы...

Примеры:

If I were you, I would talk to the manager.

If I were you, I would see a doctor.

If I were you, I wouldn't buy that car.

If I were you, I would study more.""",
            },

            {
                "order": 8,
                "title": "Вопросы",
                "body": """Общий вопрос:

Would you travel more if you had enough money?

Would she accept the job if they offered it?

Краткие ответы:

Yes, I would.

No, I wouldn't.

Специальный вопрос:

What would you do if you lost your job?

Where would you live if you could choose any country?

Очень частая модель:

What would you do if...?""",
            },

            {
                "order": 9,
                "title": "COULD вместо WOULD",
                "body": """COULD показывает возможность или способность.

Пример:

If I had more time, I could learn another language.

If she lived closer, she could visit us more often.

Сравните:

If I had more money, I would buy a car.

WOULD = предполагаемый результат.

If I had more money, I could buy a car.

COULD = возможность.""",
            },

            {
                "order": 10,
                "title": "MIGHT вместо WOULD",
                "body": """MIGHT показывает менее уверенный результат.

Примеры:

If I had more free time, I might start a new hobby.

If she invited him, he might come.

If we moved, we might be happier.

If the weather were better, we might go for a walk.

После MIGHT используется первая форма без TO.""",
            },

            {
                "order": 11,
                "title": "WOULD не используется после IF",
                "body": """В основной модели WOULD не ставится в IF-части.

Неправильно:

If I would have more money, I would travel.

Правильно:

If I had more money, I would travel.

Основная модель:

If + Past Simple, would + V1

Не:

If + would...

Также:

would buy

не:

would to buy""",
            },

            {
                "order": 12,
                "title": "First или Second Conditional",
                "body": """First Conditional:

реальная или вероятная ситуация в будущем.

If I have enough money, I will buy a car.

Second Conditional:

маловероятная или воображаемая ситуация.

If I had enough money, I would buy a car.

Сравните:

If she studies, she will pass.

If she studied more, she would pass.

Во втором случае подразумевается, что сейчас она учится недостаточно.""",
            },

            {
                "order": 13,
                "title": "Zero, First и Second Conditional",
                "body": """Zero Conditional:

общий факт.

If people don't sleep, they feel tired.

First Conditional:

реальная будущая ситуация.

If I don't sleep tonight, I will feel tired tomorrow.

Second Conditional:

воображаемая ситуация.

If I didn't need sleep, I would work all night.

Главное различие — степень реальности ситуации.""",
            },

            {
                "order": 14,
                "title": "Как выбрать Second Conditional",
                "body": """Используйте Second Conditional, если:

ситуация нереальна сейчас;

ситуация маловероятна в будущем;

вы даёте совет;

вы воображаете другую жизнь.

Формула:

If + Past Simple, would + V1

Примеры:

If I knew the answer, I would tell you.

If I won the lottery, I would buy a house.

If I were you, I would rest.

Возможны также:

could + V1

might + V1""",
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
                "prompt": (
                    "If I ___ near the sea, "
                    "I would swim every day."
                ),
                "options": [
                    "live",
                    "lived",
                    "will live",
                    "would live",
                ],
                "answer": "lived",
                "explanation": (
                    "Second Conditional: if + Past Simple."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "If she ___ more confident, "
                    "she would apply for the job."
                ),
                "options": [
                    "is",
                    "were",
                    "will be",
                    "would be",
                ],
                "answer": "were",
                "explanation": (
                    "В гипотетической конструкции используется were."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "If we had a bigger house, "
                    "we ___ more guests."
                ),
                "options": [
                    "invite",
                    "will invite",
                    "would invite",
                    "invited yesterday",
                ],
                "answer": "would invite",
                "explanation": (
                    "Результат Second Conditional: would + V1."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "If he knew her number, he ___ her."
                ),
                "options": [
                    "calls",
                    "would call",
                    "will call",
                    "called already",
                ],
                "answer": "would call",
                "explanation": (
                    "Воображаемый результат → would call."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "If they ___ more carefully, "
                    "they wouldn't make so many mistakes."
                ),
                "options": [
                    "work",
                    "worked",
                    "will work",
                    "would work",
                ],
                "answer": "worked",
                "explanation": (
                    "После if используется Past Simple."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "If I didn't have to work, "
                    "I ___ more time with my family."
                ),
                "options": [
                    "spend",
                    "will spend",
                    "would spend",
                    "spent yesterday",
                ],
                "answer": "would spend",
                "explanation": (
                    "Результат → would + V1."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "If she lived closer, "
                    "she ___ visit us more often."
                ),
                "options": [
                    "can",
                    "could",
                    "will can",
                    "could to",
                ],
                "answer": "could",
                "explanation": (
                    "Could выражает гипотетическую возможность."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "If the weather were better, "
                    "we ___ go outside."
                ),
                "options": [
                    "might",
                    "might to",
                    "will might",
                    "mights",
                ],
                "answer": "might",
                "explanation": (
                    "Might + V1 = менее уверенный результат."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "What would you do if you ___ your job?"
                ),
                "options": [
                    "lose",
                    "lost",
                    "will lose",
                    "would lose",
                ],
                "answer": "lost",
                "explanation": (
                    "После if → Past Simple."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "If I ___ rich, "
                    "I would travel around the world."
                ),
                "options": [
                    "am",
                    "were",
                    "will be",
                    "would be",
                ],
                "answer": "were",
                "explanation": (
                    "Стандартная гипотетическая форма: If I were."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "If I were you, I ___ to the doctor."
                ),
                "options": [
                    "go",
                    "will go",
                    "would go",
                    "went yesterday",
                ],
                "answer": "would go",
                "explanation": (
                    "If I were you, I would + V1."
                ),
            },

            {
                "order": 12,
                "prompt": (
                    "If she didn't spend so much money, "
                    "she ___ more."
                ),
                "options": [
                    "saves",
                    "will save",
                    "would save",
                    "saved already",
                ],
                "answer": "would save",
                "explanation": (
                    "Гипотетический результат → would save."
                ),
            },

            {
                "order": 13,
                "prompt": (
                    "Would you move abroad if you ___ "
                    "a good job there?"
                ),
                "options": [
                    "find",
                    "found",
                    "will find",
                    "would find",
                ],
                "answer": "found",
                "explanation": (
                    "В if-clause нужен Past Simple."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "If he ___ taller, "
                    "he could play basketball."
                ),
                "options": [
                    "is",
                    "were",
                    "will be",
                    "would be",
                ],
                "answer": "were",
                "explanation": (
                    "Гипотетическое состояние → were."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "I wouldn't accept the offer "
                    "if the salary ___ low."
                ),
                "options": [
                    "is",
                    "were",
                    "will be",
                    "would be",
                ],
                "answer": "were",
                "explanation": (
                    "Second Conditional → Past Simple / were."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "If I would know the answer, I would tell you.",
                    "If I knew the answer, I would tell you.",
                    "If I know the answer, I would tell you.",
                    "If I knew the answer, I will tell you.",
                ],
                "answer": (
                    "If I knew the answer, I would tell you."
                ),
                "explanation": (
                    "If + Past Simple, would + V1."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "If I were rich, I will travel.",
                    "If I were rich, I would travel.",
                    "If I would be rich, I would travel.",
                    "If I were rich, I would to travel.",
                ],
                "answer": (
                    "If I were rich, I would travel."
                ),
                "explanation": (
                    "Стандартная модель Second Conditional."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "If she didn't studied, she would fail.",
                    "If she didn't study, she would fail.",
                    "If she wouldn't study, she would fail.",
                    "If she not studied, she would fail.",
                ],
                "answer": (
                    "If she didn't study, she would fail."
                ),
                "explanation": (
                    "После didn't используется первая форма."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "Which sentence gives advice?"
                ),
                "options": [
                    "If I were you, I would talk to the manager.",
                    "If I am you, I will talk to the manager.",
                    "If I was manager, I talk.",
                    "If I would be you, I would talk.",
                ],
                "answer": (
                    "If I were you, I would talk to the manager."
                ),
                "explanation": (
                    "If I were you... — стандартная модель совета."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "Which sentence describes a real future possibility?"
                ),
                "options": [
                    "If I have enough money, I will buy a car.",
                    "If I had enough money, I would buy a car.",
                    "If I had had money, I would have bought a car.",
                    "If I were a millionaire, I would buy ten cars.",
                ],
                "answer": (
                    "If I have enough money, I will buy a car."
                ),
                "explanation": (
                    "Реальная будущая возможность → First Conditional."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "Which sentence describes an unreal present?"
                ),
                "options": [
                    "If I know the answer, I will tell you.",
                    "If I knew the answer, I would tell you.",
                    "If I knew the answer yesterday, I told you.",
                    "If I will know, I will tell you.",
                ],
                "answer": (
                    "If I knew the answer, I would tell you."
                ),
                "explanation": (
                    "Сейчас ответ неизвестен → unreal present."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct WOULD/COULD pair.",
                "options": [
                    (
                        "If I had more money, I would buy a car. / "
                        "If I had more money, I could buy a car."
                    ),
                    (
                        "If I would have money, I would buy a car. / "
                        "If I had money, I could to buy a car."
                    ),
                    (
                        "If I had money, I will buy a car. / "
                        "If I had money, I can buy a car yesterday."
                    ),
                    (
                        "If I had money, I would to buy a car. / "
                        "If I could money, I buy car."
                    ),
                ],
                "answer": (
                    "If I had more money, I would buy a car. / "
                    "If I had more money, I could buy a car."
                ),
                "explanation": (
                    "Would = предполагаемый результат; "
                    "could = возможность."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct First/Second Conditional pair."
                ),
                "options": [
                    (
                        "If she studies, she will pass. / "
                        "If she studied more, she would pass."
                    ),
                    (
                        "If she will study, she will pass. / "
                        "If she would study, she would pass."
                    ),
                    (
                        "If she studied, she will pass. / "
                        "If she studies, she would pass."
                    ),
                    (
                        "If she study, she will pass. / "
                        "If she studied, she would to pass."
                    ),
                ],
                "answer": (
                    "If she studies, she will pass. / "
                    "If she studied more, she would pass."
                ),
                "explanation": (
                    "First = реальная возможность; "
                    "Second = гипотетическая ситуация."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "If I had time, I would help. / "
                        "If I had time, I could help. / "
                        "If she called, I might answer. / "
                        "If I were you, I would rest."
                    ),
                    (
                        "If I would have time, I would help. / "
                        "If I had time, I could to help. / "
                        "If she called, I will might answer. / "
                        "If I was you, I will rest."
                    ),
                    (
                        "If I have time, I would help. / "
                        "If I had time, I can help. / "
                        "If she would call, I might answer. / "
                        "If I am you, I would rest."
                    ),
                    (
                        "If I had time, I would to help. / "
                        "If I had time, I could helped. / "
                        "If she called, she mights answer. / "
                        "If I were you, I would resting."
                    ),
                ],
                "answer": (
                    "If I had time, I would help. / "
                    "If I had time, I could help. / "
                    "If she called, I might answer. / "
                    "If I were you, I would rest."
                ),
                "explanation": (
                    "Second Conditional может использовать "
                    "would, could и might в результате."
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
                "✅ A1 Lesson 48 seeded: Second Conditional"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
