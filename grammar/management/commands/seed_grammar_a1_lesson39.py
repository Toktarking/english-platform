from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 39: "
        "Future Continuous and Future Perfect."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=39,
            defaults={
                "title": "Future Continuous и Future Perfect",
                "slug": "future-continuous-future-perfect",
                "theory_text": (
                    "Future Continuous and Future Perfect."
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
                "title": "Future Continuous: процесс в будущем",
                "body": """Future Continuous показывает действие, которое будет находиться в процессе в определённый момент будущего.

Формула:

subject + will be + verb-ing

Примеры:

I will be working at six tomorrow.

She will be studying.

They will be travelling.

We will be waiting.

Главное — не начало и не конец действия, а сам процесс в будущем.""",
            },

            {
                "order": 2,
                "title": "Когда используется Future Continuous",
                "body": """Future Continuous часто используется с конкретным будущим моментом.

Примеры:

At eight tomorrow, I will be driving to work.

This time next week, we will be staying in Astana.

She will be taking her exam at ten.

They will be having dinner at seven.

Частые маркеры:

at six tomorrow;

this time tomorrow;

this time next week;

all day tomorrow;

from five to seven.""",
            },

            {
                "order": 3,
                "title": "Длительный процесс и естественное будущее",
                "body": """Future Continuous может подчёркивать длительность:

I will be working all day.

She will be studying all evening.

They will be travelling for several hours.

Он также может описывать естественно ожидаемое действие:

I will be seeing Marat tomorrow.

She will be working in the office next week.

We will be staying at the same hotel.""",
            },

            {
                "order": 4,
                "title": "Вежливые вопросы о планах",
                "body": """Future Continuous часто используется для вежливых вопросов о планах.

Примеры:

Will you be using the car tonight?

Will you be coming to the meeting?

Will you be staying for dinner?

Will you be working tomorrow?

Сравните:

Will you use the car tonight?
— более прямой вопрос.

Will you be using the car tonight?
— более нейтральный и вежливый вопрос о планах.""",
            },

            {
                "order": 5,
                "title": "Отрицание и вопросы Future Continuous",
                "body": """Отрицание:

subject + won't be + verb-ing

I won't be working tomorrow.

She won't be coming tonight.

Вопрос:

Will + subject + be + verb-ing?

Will you be working?

Will she be studying?

Краткие ответы:

Yes, I will.

No, I won't.

Специальный вопрос:

What will you be doing at six?""",
            },

            {
                "order": 6,
                "title": "Future Simple или Future Continuous",
                "body": """Future Simple часто показывает:

решение;

обещание;

будущий факт;

прогноз.

I will call you at six.

Future Continuous показывает процесс в конкретный момент:

I will be working at six.

Сравните:

I will meet him tomorrow.
— будущий факт.

I will be meeting him tomorrow.
— ожидаемая часть будущих событий.""",
            },

            {
                "order": 7,
                "title": "Что такое Future Perfect",
                "body": """Future Perfect показывает действие, которое завершится к определённому моменту в будущем.

Пример:

I will have finished the report by six.

Это означает:

к шести отчёт уже будет готов.

Главная идея:

результат будет достигнут не позднее определённого будущего момента.""",
            },

            {
                "order": 8,
                "title": "Формула Future Perfect",
                "body": """Формула:

subject + will have + V3

Примеры:

I will have finished.

She will have arrived.

They will have left.

We will have completed the project.

После WILL HAVE нужна третья форма глагола.

Правильно:

will have gone

will have seen

will have written

Неправильно:

will have went

will have saw

will have wrote""",
            },

            {
                "order": 9,
                "title": "BY и BY THE TIME",
                "body": """BY показывает крайний срок:

by six;

by Monday;

by next week;

by the end of the year.

Примеры:

I will have finished by six.

She will have returned by Monday.

BY THE TIME означает:

к тому времени как.

Пример:

By the time you arrive, I will have finished.

Важно:

после by the time для будущего используется Present Simple.

Не:

By the time you will arrive...""",
            },

            {
                "order": 10,
                "title": "Результат и количество к будущему моменту",
                "body": """Future Perfect подчёркивает:

завершённость;

готовый результат;

количество к определённому моменту.

Примеры:

By Friday, I will have written ten pages.

By the end of the month, she will have read four books.

By next year, they will have visited five countries.

By the end of the course, we will have completed many lessons.""",
            },

            {
                "order": 11,
                "title": "Отрицание и вопросы Future Perfect",
                "body": """Отрицание:

subject + won't have + V3

I won't have finished by six.

She won't have arrived by then.

Вопрос:

Will + subject + have + V3?

Will you have finished by six?

Will she have arrived by Monday?

Краткие ответы:

Yes, I will.

No, I won't.

Специальный вопрос:

How many pages will she have written by Friday?""",
            },

            {
                "order": 12,
                "title": "Future Continuous или Future Perfect",
                "body": """Сравните:

At six, I will be writing the report.

Это процесс в шесть часов.

By six, I will have written the report.

Это готовый результат к шести.

Главная подсказка:

AT → что будет происходить в этот момент?

BY → что уже будет завершено к этому моменту?

Ещё пример:

At eight, she will be cooking dinner.

By eight, she will have cooked dinner.""",
            },

            {
                "order": 13,
                "title": "AT, UNTIL и BY",
                "body": """AT показывает конкретный момент:

At six, I will be studying.

UNTIL показывает, до какого момента действие продолжается:

I will be working until six.

BY показывает крайний срок завершения:

I will have finished by six.

Сравните:

I will work until six.
— работа продолжается до шести.

I will have finished by six.
— не позднее шести работа уже закончится.""",
            },

            {
                "order": 14,
                "title": "Сравнение будущих времён",
                "body": """Future Simple:

will + V1

I will write the report tomorrow.

Future Continuous:

will be + V-ing

I will be writing the report at six.

Future Perfect:

will have + V3

I will have written the report by six.

Future Perfect Continuous:

will have been + V-ing

I will have been writing for three hours by six.

Простое правило:

будущий факт → Future Simple

процесс в момент → Future Continuous

готовый результат к моменту → Future Perfect

длительность процесса к моменту → Future Perfect Continuous""",
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
                "prompt": "This time tomorrow, I ___ on the train.",
                "options": [
                    "will be travelling",
                    "will have travelled by then",
                    "travel every day",
                    "am travel",
                ],
                "answer": "will be travelling",
                "explanation": (
                    "This time tomorrow показывает процесс "
                    "в конкретный будущий момент."
                ),
            },

            {
                "order": 2,
                "prompt": "At eight, she ___ dinner.",
                "options": [
                    "will be cooking",
                    "will have cooked by eight",
                    "will cooking",
                    "cooks yesterday",
                ],
                "answer": "will be cooking",
                "explanation": (
                    "At eight → процесс в этот момент → "
                    "Future Continuous."
                ),
            },

            {
                "order": 3,
                "prompt": "By eight, she ___ dinner.",
                "options": [
                    "will be cooking at that moment",
                    "will have cooked",
                    "will has cooked",
                    "is cooked",
                ],
                "answer": "will have cooked",
                "explanation": (
                    "By eight → готовый результат к этому моменту."
                ),
            },

            {
                "order": 4,
                "prompt": "We ___ the project by Friday.",
                "options": [
                    "will have completed",
                    "will be completing at six only",
                    "will has completed",
                    "have complete",
                ],
                "answer": "will have completed",
                "explanation": (
                    "Проект будет завершён к пятнице → Future Perfect."
                ),
            },

            {
                "order": 5,
                "prompt": "At ten tomorrow, they ___ the exam.",
                "options": [
                    "will be taking",
                    "will have taken before ten",
                    "will taking",
                    "take yesterday",
                ],
                "answer": "will be taking",
                "explanation": (
                    "At ten tomorrow → процесс в конкретный момент."
                ),
            },

            {
                "order": 6,
                "prompt": "By ten tomorrow, they ___ the exam.",
                "options": [
                    "will be taking at ten",
                    "will have completed",
                    "will has complete",
                    "are completed",
                ],
                "answer": "will have completed",
                "explanation": (
                    "By ten → экзамен уже будет завершён."
                ),
            },

            {
                "order": 7,
                "prompt": "___ you be using the car tonight?",
                "options": [
                    "Do",
                    "Will",
                    "Are will",
                    "Have",
                ],
                "answer": "Will",
                "explanation": (
                    "Future Continuous question: "
                    "Will + subject + be + verb-ing?"
                ),
            },

            {
                "order": 8,
                "prompt": "Will she have arrived by Monday?",
                "options": [
                    "Yes, she will.",
                    "Yes, she has.",
                    "Yes, she is.",
                    "Yes, she does.",
                ],
                "answer": "Yes, she will.",
                "explanation": (
                    "Краткий ответ на вопрос с will: Yes, she will."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "At this time next week, we ___ at a hotel."
                ),
                "options": [
                    "will be staying",
                    "will have stayed by then only",
                    "will staying",
                    "are stay",
                ],
                "answer": "will be staying",
                "explanation": (
                    "This time next week → Future Continuous."
                ),
            },

            {
                "order": 10,
                "prompt": "By next year, I ___ here for ten years.",
                "options": [
                    "will have lived",
                    "will be living at that moment only",
                    "will has lived",
                    "have lived yesterday",
                ],
                "answer": "will have lived",
                "explanation": (
                    "К следующему году период проживания достигнет "
                    "десяти лет."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "How many pages ___ she ___ by Friday?"
                ),
                "options": [
                    "will / have written",
                    "will / be writing",
                    "does / write",
                    "has / wrote",
                ],
                "answer": "will / have written",
                "explanation": (
                    "How many + результат к сроку → Future Perfect."
                ),
            },

            {
                "order": 12,
                "prompt": "What ___ you be doing at six?",
                "options": ["do", "will", "are", "have"],
                "answer": "will",
                "explanation": (
                    "What will you be doing at six?"
                ),
            },

            {
                "order": 13,
                "prompt": "I will be working ___ six.",
                "options": ["by", "at", "since", "ago"],
                "answer": "at",
                "explanation": (
                    "AT показывает процесс в конкретный момент."
                ),
            },

            {
                "order": 14,
                "prompt": "I will have finished ___ six.",
                "options": ["at only", "by", "since", "for"],
                "answer": "by",
                "explanation": (
                    "BY показывает крайний срок завершения."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "By the time you ___, "
                    "I will have prepared dinner."
                ),
                "options": [
                    "will arrive",
                    "arrive",
                    "arrived",
                    "arriving",
                ],
                "answer": "arrive",
                "explanation": (
                    "После by the time для будущего "
                    "используется Present Simple."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct Future Continuous sentence.",
                "options": [
                    "I will be work at six.",
                    "I will be working at six.",
                    "I will working at six.",
                    "I will have working at six.",
                ],
                "answer": "I will be working at six.",
                "explanation": (
                    "Future Continuous: will be + verb-ing."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct Future Perfect sentence.",
                "options": [
                    "I will have finish by six.",
                    "I will have finished by six.",
                    "I will has finished by six.",
                    "I will be finished by six always.",
                ],
                "answer": "I will have finished by six.",
                "explanation": (
                    "Future Perfect: will have + V3."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "He will have wrote the report.",
                    "He will have written the report.",
                    "He will have write the report.",
                    "He will written the report.",
                ],
                "answer": "He will have written the report.",
                "explanation": (
                    "Write → wrote → written; Future Perfect требует V3."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "Which sentence emphasizes a process "
                    "at six tomorrow?"
                ),
                "options": [
                    "I will have finished by six.",
                    "I will be working at six.",
                    "I will work yesterday.",
                    "I have worked at six tomorrow.",
                ],
                "answer": "I will be working at six.",
                "explanation": (
                    "Процесс в конкретный момент → Future Continuous."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "Which sentence emphasizes a completed "
                    "result by six?"
                ),
                "options": [
                    "I will be working at six.",
                    "I will have finished by six.",
                    "I will working until six.",
                    "I am finished tomorrow.",
                ],
                "answer": "I will have finished by six.",
                "explanation": (
                    "Готовый результат к моменту → Future Perfect."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct pair.",
                "options": [
                    (
                        "At six, I will be writing. / "
                        "By six, I will have written the report."
                    ),
                    (
                        "At six, I will have wrote. / "
                        "By six, I will be writing always."
                    ),
                    (
                        "At six, I will writing. / "
                        "By six, I will has written."
                    ),
                    (
                        "At six, I write yesterday. / "
                        "By six, I have writing."
                    ),
                ],
                "answer": (
                    "At six, I will be writing. / "
                    "By six, I will have written the report."
                ),
                "explanation": (
                    "AT → процесс; BY → завершённый результат."
                ),
            },

            {
                "order": 22,
                "prompt": (
                    "Choose the correct sentence with UNTIL."
                ),
                "options": [
                    "I will be working until six.",
                    "I will have finished until six.",
                    "I will working until six.",
                    "I will have work until six.",
                ],
                "answer": "I will be working until six.",
                "explanation": (
                    "Until показывает, до какого момента "
                    "продолжается действие."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "By six, I ___ for five hours."
                ),
                "options": [
                    "will have been working",
                    "will be worked",
                    "will have working",
                    "will has been working",
                ],
                "answer": "will have been working",
                "explanation": (
                    "Длительность процесса к будущему моменту → "
                    "Future Perfect Continuous."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct comparison.",
                "options": [
                    (
                        "I will write tomorrow. / "
                        "I will be writing at six. / "
                        "I will have written it by six."
                    ),
                    (
                        "I will wrote tomorrow. / "
                        "I will working at six. / "
                        "I will have wrote by six."
                    ),
                    (
                        "I will be write tomorrow. / "
                        "I have writing at six. / "
                        "I will has written by six."
                    ),
                    (
                        "I writing tomorrow. / "
                        "I will been writing at six. / "
                        "I have written tomorrow."
                    ),
                ],
                "answer": (
                    "I will write tomorrow. / "
                    "I will be writing at six. / "
                    "I will have written it by six."
                ),
                "explanation": (
                    "Future Simple = факт; "
                    "Future Continuous = процесс; "
                    "Future Perfect = результат к моменту."
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
                "✅ A1 Lesson 39 seeded: "
                "Future Continuous and Future Perfect"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
