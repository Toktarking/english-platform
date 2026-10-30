from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 46: "
        "Zero Conditional."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=46,
            defaults={
                "title": "Zero Conditional",
                "slug": "zero-conditional",
                "theory_text": (
                    "Zero Conditional: "
                    "If + Present Simple, Present Simple."
                ),
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Zero Conditional",
                "body": """Zero Conditional используется для:

общеизвестных фактов;

законов природы;

правил;

постоянных закономерностей;

привычных результатов.

Пример:

If you heat water, it boils.

Это не прогноз.

Это факт, который происходит всегда или обычно.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Основная схема:

If + Present Simple, Present Simple

Пример:

If you heat water, it boils.

Условие:

If you heat water

Результат:

it boils

Обе части обычно стоят в Present Simple.""",
            },

            {
                "order": 3,
                "title": "Общие факты и законы природы",
                "body": """Zero Conditional часто используется для научных и природных фактов.

Примеры:

If water reaches 100°C, it boils.

If temperatures fall below zero, water freezes.

If plants don't get sunlight, they die.

If you drop an object, it falls.

Если условие выполняется, результат закономерен.""",
            },

            {
                "order": 4,
                "title": "Привычки и повторяющиеся ситуации",
                "body": """Zero Conditional может описывать регулярную личную реакцию.

Примеры:

If I drink coffee late, I can't sleep.

If she misses breakfast, she gets hungry.

If we leave home late, we take a taxi.

If he feels stressed, he goes for a walk.

Речь идёт не об одном случае, а о повторяющейся ситуации.""",
            },

            {
                "order": 5,
                "title": "Правила и инструкции",
                "body": """Zero Conditional подходит для правил и работы устройств.

Примеры:

If you press this button, the computer turns on.

If you click here, the file opens.

If students arrive late, the teacher marks them absent.

If the battery is empty, the phone turns off.

Такие предложения описывают стандартный результат.""",
            },

            {
                "order": 6,
                "title": "IF и WHEN",
                "body": """В Zero Conditional IF часто можно заменить на WHEN.

If I drink coffee at night, I can't sleep.

When I drink coffee at night, I can't sleep.

IF:

если это происходит.

WHEN:

когда это происходит.

При регулярной закономерности разница часто небольшая.""",
            },

            {
                "order": 7,
                "title": "Порядок частей и запятая",
                "body": """Если IF-часть стоит первой, обычно используется запятая:

If you heat water, it boils.

Если результат стоит первым:

Water boils if you heat it.

Запятая обычно не нужна.

Сравните:

If I am tired, I go to bed early.

I go to bed early if I am tired.""",
            },

            {
                "order": 8,
                "title": "Present Simple после IF",
                "body": """В IF-части используется Present Simple.

I/you/we/they:

If you exercise, you feel better.

He/she/it:

If she drinks coffee, she sleeps badly.

Не забывайте -s / -es:

If it rains, the road gets wet.

Не:

If it rain...""",
            },

            {
                "order": 9,
                "title": "Отрицание",
                "body": """Для отрицания используются don't и doesn't.

Примеры:

If I don't sleep enough, I feel tired.

If you don't water plants, they die.

If she doesn't eat breakfast, she gets hungry.

Если подлежащее he/she/it:

doesn't + base verb

Не:

If he don't eat...""",
            },

            {
                "order": 10,
                "title": "Модальные глаголы и Imperative",
                "body": """Результат не всегда обязан быть только Present Simple.

Можно использовать CAN:

If the weather is clear, you can see the mountains.

MUST:

If the alarm rings, you must leave the building.

SHOULD:

If you feel tired, you should rest.

Imperative:

If you don't understand, ask the teacher.

Основное условие всё равно остаётся:

If + Present Simple""",
            },

            {
                "order": 11,
                "title": "UNLESS",
                "body": """UNLESS означает:

если не.

Пример:

Plants die unless they get water.

Это значит:

Plants die if they don't get water.

Важно:

после UNLESS не нужно второе отрицание.

Неправильно:

Unless plants don't get water...

Правильно:

Unless plants get water...""",
            },

            {
                "order": 12,
                "title": "Zero Conditional и First Conditional",
                "body": """Zero Conditional:

общий факт или регулярная закономерность.

If you don't water plants, they die.

First Conditional:

конкретная будущая ситуация.

If you don't water this plant, it will die.

Сравните:

If I drink coffee at night, I can't sleep.
— моя обычная реакция.

If I drink coffee tonight, I won't sleep.
— конкретная ситуация сегодня.""",
            },

            {
                "order": 13,
                "title": "Типичные ошибки",
                "body": """Неправильно:

If you will heat water, it will boil.

Правильно:

If you heat water, it boils.

Неправильно:

If she drink coffee, she sleeps badly.

Правильно:

If she drinks coffee, she sleeps badly.

Неправильно:

Unless you don't study, you fail.

Правильно:

Unless you study, you fail.""",
            },

            {
                "order": 14,
                "title": "Как выбрать Zero Conditional",
                "body": """Используйте Zero Conditional, если:

это общий факт;

это закон природы;

это регулярная личная реакция;

это правило;

это инструкция;

результат происходит всегда или обычно.

Главная формула:

If + Present Simple, Present Simple

Пример:

If water freezes, it becomes ice.""",
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
                "prompt": "If water reaches 100°C, it ___.",
                "options": [
                    "boils",
                    "will boil tomorrow",
                    "boiled",
                    "is boiling every time",
                ],
                "answer": "boils",
                "explanation": (
                    "Общий факт → Present Simple."
                ),
            },

            {
                "order": 2,
                "prompt": "If you ___ ice, it melts.",
                "options": [
                    "heat",
                    "will heat",
                    "heated",
                    "are heating tomorrow",
                ],
                "answer": "heat",
                "explanation": (
                    "После if в Zero Conditional используется Present Simple."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "If she doesn't eat breakfast, "
                    "she ___ hungry."
                ),
                "options": [
                    "gets",
                    "will get only tomorrow",
                    "got",
                    "getting",
                ],
                "answer": "gets",
                "explanation": (
                    "Регулярный результат → gets."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "If people ___ enough sleep, "
                    "they feel tired."
                ),
                "options": [
                    "don't get",
                    "won't get",
                    "didn't get",
                    "not getting",
                ],
                "answer": "don't get",
                "explanation": (
                    "Present Simple negative: don't get."
                ),
            },

            {
                "order": 5,
                "prompt": "If I ___ stressed, I go for a walk.",
                "options": [
                    "feel",
                    "will feel",
                    "felt",
                    "feeling",
                ],
                "answer": "feel",
                "explanation": (
                    "Повторяющаяся личная реакция → Present Simple."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "If the battery is empty, "
                    "the phone ___ off."
                ),
                "options": [
                    "turns",
                    "will turn tomorrow",
                    "turned",
                    "turning",
                ],
                "answer": "turns",
                "explanation": (
                    "Обычный результат работы устройства."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "If you press this button, "
                    "the machine ___."
                ),
                "options": [
                    "starts",
                    "will starting",
                    "started",
                    "start with he",
                ],
                "answer": "starts",
                "explanation": (
                    "Machine = it, поэтому starts."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "If students arrive late, "
                    "the teacher ___ them absent."
                ),
                "options": [
                    "marks",
                    "will mark only tomorrow",
                    "marked",
                    "marking",
                ],
                "answer": "marks",
                "explanation": (
                    "Правило организации → Zero Conditional."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "If you don't understand, ___ the teacher."
                ),
                "options": [
                    "ask",
                    "will ask yourself",
                    "asking",
                    "asked",
                ],
                "answer": "ask",
                "explanation": (
                    "После условия возможен imperative."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "If the alarm rings, "
                    "you ___ leave the building."
                ),
                "options": [
                    "must",
                    "must to",
                    "will must",
                    "musts",
                ],
                "answer": "must",
                "explanation": (
                    "В результате можно использовать modal must."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "If the weather is clear, "
                    "you ___ see the mountains."
                ),
                "options": [
                    "can",
                    "can to",
                    "will can",
                    "could yesterday",
                ],
                "answer": "can",
                "explanation": (
                    "Modal can возможен в результате."
                ),
            },

            {
                "order": 12,
                "prompt": (
                    "Plants die ___ they don't get water."
                ),
                "options": [
                    "if",
                    "will",
                    "would",
                    "because will",
                ],
                "answer": "if",
                "explanation": (
                    "If вводит условие."
                ),
            },

            {
                "order": 13,
                "prompt": "Plants die ___ they get water.",
                "options": [
                    "unless",
                    "unless not",
                    "if not they",
                    "will unless",
                ],
                "answer": "unless",
                "explanation": (
                    "Unless = if ... not."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "What ___ if you press this button?"
                ),
                "options": [
                    "happens",
                    "will happens always",
                    "happen does",
                    "happened every day",
                ],
                "answer": "happens",
                "explanation": (
                    "Частая модель: What happens if...?"
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "What do you do if you ___ tired?"
                ),
                "options": [
                    "feel",
                    "will feel",
                    "felt",
                    "feeling",
                ],
                "answer": "feel",
                "explanation": (
                    "Вопрос о привычной реакции → Present Simple."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct Zero Conditional sentence.",
                "options": [
                    "If you heat water, it boils.",
                    "If you will heat water, it will boil.",
                    "If you heated water, it boils tomorrow.",
                    "If you heating water, it boil.",
                ],
                "answer": "If you heat water, it boils.",
                "explanation": (
                    "Базовая формула: Present Simple + Present Simple."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "If she drink coffee, she sleeps badly.",
                    "If she drinks coffee, she sleeps badly.",
                    "If she will drink coffee, she sleeps badly.",
                    "If she drinks coffee, she will always slept badly.",
                ],
                "answer": (
                    "If she drinks coffee, she sleeps badly."
                ),
                "explanation": (
                    "She → drinks; регулярный результат → sleeps."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence with UNLESS.",
                "options": [
                    "Unless you don't study, you fail.",
                    "Unless you study, you fail.",
                    "Unless you will study, you fail.",
                    "Unless not you study, you fail.",
                ],
                "answer": "Unless you study, you fail.",
                "explanation": (
                    "После unless двойное отрицание не используется."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "Which sentence describes a general fact?"
                ),
                "options": [
                    "If you don't water plants, they die.",
                    "If you don't water this plant, it will die.",
                    "If you didn't water it, it died yesterday.",
                    "If you water it tomorrow, it will grow.",
                ],
                "answer": (
                    "If you don't water plants, they die."
                ),
                "explanation": (
                    "Общий факт → Zero Conditional."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "Which sentence describes a specific future situation?"
                ),
                "options": [
                    "If I drink coffee at night, I can't sleep.",
                    "If I drink coffee tonight, I won't sleep.",
                    "When I drink coffee, I can't sleep.",
                    "If people don't sleep, they get tired.",
                ],
                "answer": (
                    "If I drink coffee tonight, I won't sleep."
                ),
                "explanation": (
                    "Конкретная будущая ситуация → First Conditional."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct punctuation.",
                "options": [
                    "If it rains, the ground gets wet.",
                    "If it rains the ground, gets wet.",
                    "The ground gets wet, if it rains.",
                    "If, it rains the ground gets wet.",
                ],
                "answer": "If it rains, the ground gets wet.",
                "explanation": (
                    "Когда if-clause стоит первой, ставится запятая."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct reversed order.",
                "options": [
                    "Water boils if you heat it.",
                    "Water boils, if you heat it.",
                    "Water will boil always if you will heat it.",
                    "Water boil if you heats it.",
                ],
                "answer": "Water boils if you heat it.",
                "explanation": (
                    "Если if-clause стоит второй, запятая обычно не нужна."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct IF/WHEN pair.",
                "options": [
                    (
                        "If I drink coffee late, I can't sleep. / "
                        "When I drink coffee late, I can't sleep."
                    ),
                    (
                        "If I will drink coffee late, I can't sleep. / "
                        "When I will drink coffee late, I can't sleep."
                    ),
                    (
                        "If I drank coffee late every day, I can't sleep. / "
                        "When I drinking coffee, I can't sleep."
                    ),
                    (
                        "If coffee late, I can't sleep. / "
                        "When coffee late, I can't sleep."
                    ),
                ],
                "answer": (
                    "If I drink coffee late, I can't sleep. / "
                    "When I drink coffee late, I can't sleep."
                ),
                "explanation": (
                    "В Zero Conditional if и when часто оба возможны."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "If water freezes, it becomes ice. / "
                        "If you feel tired, rest. / "
                        "If the alarm rings, you must leave."
                    ),
                    (
                        "If water will freeze, it will becomes ice. / "
                        "If you feel tired, to rest. / "
                        "If alarm rings, you must to leave."
                    ),
                    (
                        "If water froze, it becomes ice always. / "
                        "If you feeling tired, rest. / "
                        "If the alarm will ring, leave."
                    ),
                    (
                        "If water freezing, it become ice. / "
                        "If you feels tired, resting. / "
                        "If the alarm rings, you musts leave."
                    ),
                ],
                "answer": (
                    "If water freezes, it becomes ice. / "
                    "If you feel tired, rest. / "
                    "If the alarm rings, you must leave."
                ),
                "explanation": (
                    "Zero Conditional может иметь Present Simple, "
                    "imperative или modal в результате."
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
                "✅ A1 Lesson 46 seeded: Zero Conditional"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
