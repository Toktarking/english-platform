from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 49: "
        "Third Conditional."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=49,
            defaults={
                "title": "Third Conditional",
                "slug": "third-conditional",
                "theory_text": (
                    "Third Conditional: "
                    "If + Past Perfect, would have + V3."
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
                "title": "Что такое Third Conditional",
                "body": """Third Conditional используется для нереальных ситуаций в прошлом.

Он помогает говорить:

о результате, который не произошёл;

о сожалении;

о критике прошлого решения;

об упущенной возможности;

о воображаемом изменении прошлого.

Пример:

If I had studied harder, I would have passed the exam.

Реальность:

я учился недостаточно;

я не сдал экзамен.

Прошлое уже нельзя изменить.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Главная формула:

If + Past Perfect, would have + V3

Кратко:

If + had + V3, would have + V3

Пример:

If she had left earlier, she would have caught the bus.

Условие:

she had left earlier

Результат:

she would have caught the bus

Обе ситуации относятся к прошлому.""",
            },

            {
                "order": 3,
                "title": "Past Perfect в IF-части",
                "body": """В условии используется:

had + V3

Примеры:

had worked

had studied

had gone

had seen

had written

С неправильными глаголами нужна третья форма:

go → gone

see → seen

write → written

take → taken

know → known

Не:

had went

had saw""",
            },

            {
                "order": 4,
                "title": "WOULD HAVE + V3",
                "body": """Во второй части используется:

would have + V3

Примеры:

would have passed

would have arrived

would have helped

would have known

Пример:

If I had known about the meeting, I would have attended it.

Реальность:

я не знал;

я не пришёл.""",
            },

            {
                "order": 5,
                "title": "Сожаление и упущенные возможности",
                "body": """Third Conditional часто показывает сожаление о прошлом.

Примеры:

If I had studied more, I would have passed.

If we had left earlier, we wouldn't have missed the train.

If she had accepted the offer, she would have got the job.

If I had applied for the job, I might have got it.

Смысл:

прошлое уже произошло иначе.""",
            },

            {
                "order": 6,
                "title": "Отрицание",
                "body": """Отрицание в IF-части:

had not + V3

Сокращение:

hadn't + V3

Пример:

If I hadn't missed the bus, I would have arrived earlier.

Отрицание результата:

wouldn't have + V3

If she had taken an umbrella, she wouldn't have got wet.

Возможны отрицания в обеих частях:

If I hadn't stayed up late, I wouldn't have felt tired.""",
            },

            {
                "order": 7,
                "title": "Порядок частей",
                "body": """Если IF-часть стоит первой, нужна запятая:

If we had left earlier, we would have caught the train.

Можно поменять части местами:

We would have caught the train if we had left earlier.

Во втором случае запятая обычно не нужна.

Смысл не меняется.""",
            },

            {
                "order": 8,
                "title": "Вопросы",
                "body": """Общий вопрос:

Would you have gone if they had invited you?

Краткие ответы:

Yes, I would have.

No, I wouldn't have.

Специальный вопрос:

What would you have done if you had lost your passport?

Where would they have stayed if the hotel had been full?

Частая модель:

What would you have done if...?""",
            },

            {
                "order": 9,
                "title": "COULD HAVE и MIGHT HAVE",
                "body": """В результате можно использовать COULD HAVE.

If I had had more time, I could have helped you.

COULD HAVE показывает возможность:

мог бы.

MIGHT HAVE показывает менее уверенный результат:

If she had left earlier, she might have caught the bus.

Сравните:

would have → предполагаемый результат;

could have → возможность;

might have → менее уверенная возможность.""",
            },

            {
                "order": 10,
                "title": "HAD HAD и HAD BEEN",
                "body": """Иногда встречается конструкция:

had had

Пример:

If I had had more time, I would have finished the work.

Первое had:

вспомогательный глагол Past Perfect.

Второе had:

V3 глагола have.

С глаголом TO BE:

had been

If I had been more careful, I wouldn't have made the mistake.""",
            },

            {
                "order": 11,
                "title": "Second и Third Conditional",
                "body": """Second Conditional описывает нереальное настоящее или будущее.

If I had more money, I would travel.

Сейчас денег недостаточно.

Third Conditional описывает нереальное прошлое.

If I had had more money, I would have travelled.

В прошлом денег не было, поэтому поездка не состоялась.

Сравните:

If she knew, she would tell us.

If she had known, she would have told us.""",
            },

            {
                "order": 12,
                "title": "First, Second и Third Conditional",
                "body": """First Conditional:

реальная будущая возможность.

If I study, I will pass.

Second Conditional:

воображаемая ситуация.

If I studied more, I would pass.

Third Conditional:

нереальное прошлое.

If I had studied more, I would have passed.

Главное различие:

First → реальное будущее

Second → нереальное настоящее/будущее

Third → нереальное прошлое""",
            },

            {
                "order": 13,
                "title": "Типичные ошибки",
                "body": """Неправильно:

If I knew about the meeting, I would have come.

Если речь о прошлом:

If I had known about the meeting, I would have come.

Неправильно:

If I would have known...

Правильно:

If I had known...

Неправильно:

I would have went.

Правильно:

I would have gone.

Неправильно:

I would helped you.

Правильно:

I would have helped you.""",
            },

            {
                "order": 14,
                "title": "Как выбрать Third Conditional",
                "body": """Задайте три вопроса.

1. Ситуация относится к прошлому?

2. Она уже не может измениться?

3. Реальный результат был другим?

Если да:

используйте Third Conditional.

Формула:

If + had + V3, would have + V3

Пример:

If I had left earlier, I would have caught the train.

Также возможны:

could have + V3

might have + V3""",
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
                    "If I ___ about the meeting, "
                    "I would have attended it."
                ),
                "options": [
                    "knew",
                    "had known",
                    "would know",
                    "have known",
                ],
                "answer": "had known",
                "explanation": (
                    "Third Conditional: if + Past Perfect."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "If she had studied more, "
                    "she ___ the exam."
                ),
                "options": [
                    "would pass",
                    "would have passed",
                    "passed",
                    "had passed",
                ],
                "answer": "would have passed",
                "explanation": (
                    "Результат в прошлом: would have + V3."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "If we had left earlier, "
                    "we ___ the train."
                ),
                "options": [
                    "wouldn't miss",
                    "wouldn't have missed",
                    "didn't miss",
                    "hadn't missed",
                ],
                "answer": "wouldn't have missed",
                "explanation": (
                    "Отрицательный результат: wouldn't have + V3."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "If he ___ the instructions, "
                    "he wouldn't have made the mistake."
                ),
                "options": [
                    "read",
                    "had read",
                    "would read",
                    "has read",
                ],
                "answer": "had read",
                "explanation": (
                    "Условие относится к нереальному прошлому."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "If they had booked earlier, "
                    "they ___ less."
                ),
                "options": [
                    "would pay",
                    "would have paid",
                    "paid",
                    "had paid",
                ],
                "answer": "would have paid",
                "explanation": (
                    "Воображаемый прошлый результат."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "If I had had more time, I ___ you."
                ),
                "options": [
                    "could help",
                    "could have helped",
                    "can help",
                    "had helped",
                ],
                "answer": "could have helped",
                "explanation": (
                    "Could have + V3 показывает возможность в прошлом."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "If she had taken a taxi, "
                    "she ___ on time."
                ),
                "options": [
                    "might arrive",
                    "might have arrived",
                    "arrived",
                    "had arrived",
                ],
                "answer": "might have arrived",
                "explanation": (
                    "Might have + V3 = менее уверенный результат."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "What would you have done "
                    "if you ___ the money?"
                ),
                "options": [
                    "found",
                    "had found",
                    "would find",
                    "have found",
                ],
                "answer": "had found",
                "explanation": (
                    "После if нужен Past Perfect."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "If he hadn't driven so fast, "
                    "he ___ an accident."
                ),
                "options": [
                    "wouldn't have had",
                    "wouldn't have",
                    "didn't have",
                    "hadn't had",
                ],
                "answer": "wouldn't have had",
                "explanation": (
                    "Wouldn't have + V3; V3 глагола have = had."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "If we ___ the weather forecast, "
                    "we would have taken umbrellas."
                ),
                "options": [
                    "checked",
                    "had checked",
                    "would check",
                    "have checked",
                ],
                "answer": "had checked",
                "explanation": (
                    "Нереальное условие в прошлом → had checked."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "If she had been at home, "
                    "she ___ the phone."
                ),
                "options": [
                    "would answer",
                    "would have answered",
                    "answered",
                    "had answered",
                ],
                "answer": "would have answered",
                "explanation": (
                    "Результат относится к прошлому."
                ),
            },

            {
                "order": 12,
                "prompt": (
                    "If they had listened to us, "
                    "they ___ the problem."
                ),
                "options": [
                    "could avoid",
                    "could have avoided",
                    "avoided",
                    "had avoided",
                ],
                "answer": "could have avoided",
                "explanation": (
                    "Возможность в прошлом → could have + V3."
                ),
            },

            {
                "order": 13,
                "prompt": (
                    "If I hadn't stayed up late, "
                    "I ___ so tired."
                ),
                "options": [
                    "wouldn't be",
                    "wouldn't have been",
                    "wasn't",
                    "hadn't been",
                ],
                "answer": "wouldn't have been",
                "explanation": (
                    "Нереальный прошлый результат → wouldn't have been."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "Would you have accepted the job "
                    "if the salary ___ higher?"
                ),
                "options": [
                    "was",
                    "had been",
                    "would be",
                    "has been",
                ],
                "answer": "had been",
                "explanation": (
                    "If-clause Third Conditional: had been."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "If I had known the truth, I ___."
                ),
                "options": [
                    "wouldn't agree",
                    "wouldn't have agreed",
                    "didn't agree",
                    "hadn't agreed",
                ],
                "answer": "wouldn't have agreed",
                "explanation": (
                    "Результат относится к прошлому."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct Third Conditional sentence.",
                "options": [
                    (
                        "If I had known, "
                        "I would have helped."
                    ),
                    (
                        "If I knew, "
                        "I would have helped."
                    ),
                    (
                        "If I would have known, "
                        "I would have helped."
                    ),
                    (
                        "If I had knew, "
                        "I would helped."
                    ),
                ],
                "answer": (
                    "If I had known, "
                    "I would have helped."
                ),
                "explanation": (
                    "Had + V3, would have + V3."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "If she had went earlier, she would have arrived.",
                    "If she had gone earlier, she would have arrived.",
                    "If she had gone earlier, she would arrived.",
                    "If she went earlier, she would have arrive.",
                ],
                "answer": (
                    "If she had gone earlier, she would have arrived."
                ),
                "explanation": (
                    "Go → gone; would have + arrived."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I would have went with you.",
                    "I would have gone with you.",
                    "I would gone with you.",
                    "I would have go with you.",
                ],
                "answer": "I would have gone with you.",
                "explanation": (
                    "После would have нужна третья форма: gone."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "Which sentence describes an unreal present?"
                ),
                "options": [
                    (
                        "If I had more money, "
                        "I would travel."
                    ),
                    (
                        "If I had had more money, "
                        "I would have travelled."
                    ),
                    (
                        "If I have more money, "
                        "I will travel."
                    ),
                    (
                        "If I have money, "
                        "I travel every year."
                    ),
                ],
                "answer": (
                    "If I had more money, "
                    "I would travel."
                ),
                "explanation": (
                    "Это Second Conditional: нереальное настоящее."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "Which sentence describes an unreal past?"
                ),
                "options": [
                    (
                        "If I had had more money, "
                        "I would have travelled."
                    ),
                    (
                        "If I had more money, "
                        "I would travel."
                    ),
                    (
                        "If I have enough money, "
                        "I will travel."
                    ),
                    (
                        "If I have money, "
                        "I travel."
                    ),
                ],
                "answer": (
                    "If I had had more money, "
                    "I would have travelled."
                ),
                "explanation": (
                    "Это Third Conditional."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct HAD HAD sentence.",
                "options": [
                    (
                        "If I had had more time, "
                        "I would have finished."
                    ),
                    (
                        "If I had more time yesterday, "
                        "I would have finished."
                    ),
                    (
                        "If I had have more time, "
                        "I would finished."
                    ),
                    (
                        "If I would have had more time, "
                        "I would have finished."
                    ),
                ],
                "answer": (
                    "If I had had more time, "
                    "I would have finished."
                ),
                "explanation": (
                    "Первое had = auxiliary; второе had = V3 of have."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct WOULD/COULD/MIGHT sequence.",
                "options": [
                    (
                        "would have helped / "
                        "could have helped / "
                        "might have helped"
                    ),
                    (
                        "would helped / "
                        "could to have helped / "
                        "might helped"
                    ),
                    (
                        "would have help / "
                        "could have help / "
                        "might have help"
                    ),
                    (
                        "will have helped / "
                        "can have helped / "
                        "might to have helped"
                    ),
                ],
                "answer": (
                    "would have helped / "
                    "could have helped / "
                    "might have helped"
                ),
                "explanation": (
                    "После would/could/might используется have + V3."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct Second/Third Conditional pair."
                ),
                "options": [
                    (
                        "If she knew the answer, she would tell us. / "
                        "If she had known the answer, "
                        "she would have told us."
                    ),
                    (
                        "If she had known now, she would tell us. / "
                        "If she knew yesterday, she would have told us."
                    ),
                    (
                        "If she would know, she would tell us. / "
                        "If she would have known, "
                        "she would have told us."
                    ),
                    (
                        "If she knows, she would tell us. / "
                        "If she had knew, she would told us."
                    ),
                ],
                "answer": (
                    "If she knew the answer, she would tell us. / "
                    "If she had known the answer, "
                    "she would have told us."
                ),
                "explanation": (
                    "Second = unreal present; Third = unreal past."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "If I had studied, I would have passed. / "
                        "If I had had time, I could have helped. / "
                        "If she had left earlier, "
                        "she might have caught the bus."
                    ),
                    (
                        "If I studied, I would have passed. / "
                        "If I would have time, I could help. / "
                        "If she had left earlier, "
                        "she might caught the bus."
                    ),
                    (
                        "If I had studied, I would passed. / "
                        "If I had had time, I could to have helped. / "
                        "If she left earlier, "
                        "she might have caught the bus."
                    ),
                    (
                        "If I would have studied, I would have passed. / "
                        "If I had time, I could have help. / "
                        "If she had left earlier, "
                        "she will might have caught the bus."
                    ),
                ],
                "answer": (
                    "If I had studied, I would have passed. / "
                    "If I had had time, I could have helped. / "
                    "If she had left earlier, "
                    "she might have caught the bus."
                ),
                "explanation": (
                    "Third Conditional использует had + V3 "
                    "и would/could/might have + V3."
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
                "✅ A1 Lesson 49 seeded: Third Conditional"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
