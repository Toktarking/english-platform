from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = "Create/update A1 Grammar Lesson 34: Past Perfect."

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=34,
            defaults={
                "title": "Past Perfect",
                "slug": "past-perfect",
                "theory_text": "Past Perfect: had + Past Participle.",
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Past Perfect",
                "body": """Past Perfect показывает действие, которое произошло раньше другого действия или момента в прошлом.

Пример:

I had finished the work before he arrived.

Сначала:

I had finished the work.

Потом:

he arrived.

Главная схема:

более раннее действие → Past Perfect

более позднее действие → обычно Past Simple""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Формула Past Perfect:

subject + had + третья форма глагола

Примеры:

I had finished.

She had arrived.

They had gone.

He had written the report.

HAD одинаково используется со всеми подлежащими:

I, you, he, she, it, we, they.

В Past Perfect нет отдельных have и has.""",
            },

            {
                "order": 3,
                "title": "Третья форма глагола",
                "body": """После HAD используется третья форма глагола.

Правильные глаголы:

work → worked → worked

finish → finished → finished

study → studied → studied

Неправильные:

go → went → gone

see → saw → seen

write → wrote → written

eat → ate → eaten

take → took → taken

Неправильно:

had went

had saw

had wrote

Правильно:

had gone

had seen

had written""",
            },

            {
                "order": 4,
                "title": "Два действия в прошлом",
                "body": """Если в прошлом произошло два действия, Past Perfect помогает показать, какое случилось раньше.

Пример:

When I arrived, they had already eaten.

Порядок событий:

1. Они поели.
2. Я приехал.

Хотя в предложении сначала говорится о моём приезде, форма had eaten показывает более раннее действие.

Ещё пример:

She had left before I called.""",
            },

            {
                "order": 5,
                "title": "BEFORE и AFTER",
                "body": """BEFORE означает «до того как».

I had finished the work before he arrived.

Порядок частей можно изменить:

Before he arrived, I had finished the work.

AFTER означает «после того как».

After she had finished the report, she went home.

Сначала:

she had finished

Потом:

she went home

Если порядок и так очевиден, Past Simple иногда тоже возможен:

After she finished the report, she went home.""",
            },

            {
                "order": 6,
                "title": "WHEN и BY THE TIME",
                "body": """WHEN:

When I arrived, they had already left.

Сначала они ушли.

Потом я приехал.

BY THE TIME означает:

«к тому времени как».

Примеры:

By the time I arrived, the meeting had started.

By the time we reached the airport, the plane had left.

By the time he was twenty, he had finished university.""",
            },

            {
                "order": 7,
                "title": "ALREADY, JUST, NEVER и YET",
                "body": """ALREADY обычно ставится между had и третьей формой:

I had already finished.

She had already left.

JUST:

She had just left when I called.

NEVER:

I had never seen snow before I moved there.

После never дополнительное not не нужно.

YET обычно используется в конце:

She hadn't finished yet when I called.

Had they arrived yet?""",
            },

            {
                "order": 8,
                "title": "Отрицание",
                "body": """Отрицание:

had not → hadn't

Формула:

subject + hadn't + V3

Примеры:

I hadn't finished.

She hadn't arrived.

They hadn't gone home.

He hadn't seen the film.

Важно:

после hadn't также нужна третья форма.

Не:

hadn't went

Правильно:

hadn't gone""",
            },

            {
                "order": 9,
                "title": "Вопросы и краткие ответы",
                "body": """В вопросе HAD ставится перед подлежащим.

Формула:

Had + subject + V3?

Примеры:

Had you finished?

Had she arrived?

Had they left?

Краткие ответы:

Yes, I had.

No, I hadn't.

Yes, she had.

No, she hadn't.

DID не используется.

Неправильно:

Did she had finished?

Правильно:

Had she finished?""",
            },

            {
                "order": 10,
                "title": "Специальные вопросы",
                "body": """Формула:

Question word + had + subject + V3?

Примеры:

What had you done?

Where had she gone?

Why had they left?

How many pages had he written?

Who had she called?

Если WHO само выполняет действие:

Who had opened the door?

Who had taken the documents?""",
            },

            {
                "order": 11,
                "title": "Past Perfect или Past Simple",
                "body": """Сравните:

When I arrived, she left.

Это означает:

я приехал → после этого она ушла.

Но:

When I arrived, she had left.

Это означает:

она ушла раньше → потом я приехал.

Past Perfect показывает более раннее прошлое.

Past Simple показывает более позднее событие или обычный завершённый факт.""",
            },

            {
                "order": 12,
                "title": "Когда Past Perfect не нужен",
                "body": """Если события происходят одно за другим в естественном порядке, обычно достаточно Past Simple.

Пример:

I got up, washed my face, had breakfast and left home.

Не нужно использовать Past Perfect для каждого действия.

Но если рассказ возвращается к более раннему событию:

I arrived at work late.

I had missed the bus.

Сначала я пропустил автобус.

Потом опоздал на работу.""",
            },

            {
                "order": 13,
                "title": "Причина, косвенная речь и HAD BEEN",
                "body": """Past Perfect может объяснять прошлый результат:

She was tired because she had slept badly.

He was hungry because he hadn't eaten breakfast.

В косвенной речи:

She said, “I finished the work.”

→ She said that she had finished the work.

Для глагола BE используется:

had been

She had been ill before the exam.

He had been a teacher before he became a manager.""",
            },

            {
                "order": 14,
                "title": "Past Perfect и другие прошедшие времена",
                "body": """Past Perfect:

действие завершилось до другого момента прошлого.

She had written the report before six.

Past Continuous:

процесс происходил в определённый момент.

She was writing the report at six.

Сравните:

At six, she was writing the report.
— в шесть процесс продолжался.

By six, she had written the report.
— к шести отчёт уже был готов.

Главный алгоритм:

найдите два события в прошлом;

определите, какое произошло раньше;

более раннее → Past Perfect;

более позднее → Past Simple.""",
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
                "prompt": "By the time I arrived, the lesson ___.",
                "options": [
                    "started",
                    "had started",
                    "has started",
                    "was start",
                ],
                "answer": "had started",
                "explanation": "Урок начался раньше моего прихода, поэтому Past Perfect.",
            },

            {
                "order": 2,
                "prompt": "She was tired because she ___ badly.",
                "options": [
                    "slept",
                    "had slept",
                    "has slept",
                    "was slept",
                ],
                "answer": "had slept",
                "explanation": "Плохой сон произошёл раньше состояния tired.",
            },

            {
                "order": 3,
                "prompt": "They ___ before we came.",
                "options": [
                    "left",
                    "had left",
                    "have left",
                    "did left",
                ],
                "answer": "had left",
                "explanation": "Они ушли до нашего прихода.",
            },

            {
                "order": 4,
                "prompt": "He had ___ the door.",
                "options": [
                    "opened",
                    "open",
                    "opening",
                    "opens",
                ],
                "answer": "opened",
                "explanation": "После had нужна третья форма; у regular verb open это opened.",
            },

            {
                "order": 5,
                "prompt": "I had never ___ that film before.",
                "options": [
                    "saw",
                    "seen",
                    "see",
                    "seeing",
                ],
                "answer": "seen",
                "explanation": "See → saw → seen; после had нужна третья форма.",
            },

            {
                "order": 6,
                "prompt": "She hadn't ___ breakfast.",
                "options": [
                    "ate",
                    "eaten",
                    "eat",
                    "eating",
                ],
                "answer": "eaten",
                "explanation": "Eat → ate → eaten.",
            },

            {
                "order": 7,
                "prompt": "___ you finished before the manager arrived?",
                "options": [
                    "Did",
                    "Had",
                    "Have",
                    "Were",
                ],
                "answer": "Had",
                "explanation": "Past Perfect question: Had + subject + V3?",
            },

            {
                "order": 8,
                "prompt": "Where had they ___ before they moved here?",
                "options": [
                    "lived",
                    "live",
                    "living",
                    "lives",
                ],
                "answer": "lived",
                "explanation": "После had используется третья форма lived.",
            },

            {
                "order": 9,
                "prompt": "When we reached the station, the train ___.",
                "options": [
                    "left",
                    "had left",
                    "has left",
                    "was leave",
                ],
                "answer": "had left",
                "explanation": "Поезд ушёл до того, как мы приехали.",
            },

            {
                "order": 10,
                "prompt": "After she ___ the report, she went home.",
                "options": [
                    "had finished",
                    "has finished",
                    "finishing",
                    "did finished",
                ],
                "answer": "had finished",
                "explanation": "Завершение отчёта произошло раньше ухода домой.",
            },

            {
                "order": 11,
                "prompt": "He was hungry because he ___ lunch.",
                "options": [
                    "didn't eat earlier",
                    "hadn't eaten",
                    "hasn't eaten",
                    "wasn't eating once",
                ],
                "answer": "hadn't eaten",
                "explanation": "Причина голода произошла раньше в прошлом.",
            },

            {
                "order": 12,
                "prompt": "Had they seen the film?",
                "options": [
                    "Yes, they did.",
                    "Yes, they had.",
                    "Yes, they have.",
                    "Yes, they were.",
                ],
                "answer": "Yes, they had.",
                "explanation": "Краткий ответ на вопрос с had использует had.",
            },

            {
                "order": 13,
                "prompt": "By six o'clock, I ___ the work.",
                "options": [
                    "was finishing",
                    "had finished",
                    "finished at that moment only",
                    "have finished",
                ],
                "answer": "had finished",
                "explanation": "By six означает завершение к этому моменту.",
            },

            {
                "order": 14,
                "prompt": "At six o'clock, I ___ the work.",
                "options": [
                    "had finished always",
                    "was doing",
                    "have done",
                    "had do",
                ],
                "answer": "was doing",
                "explanation": "At six подчёркивает процесс в конкретный момент.",
            },

            {
                "order": 15,
                "prompt": "She said that she ___ the message.",
                "options": [
                    "saw",
                    "had seen",
                    "has seen",
                    "see",
                ],
                "answer": "had seen",
                "explanation": "В косвенной речи более раннее действие может быть в Past Perfect.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She had went home.",
                    "She had gone home.",
                    "She had go home.",
                    "She did had gone home.",
                ],
                "answer": "She had gone home.",
                "explanation": "Go → went → gone; после had нужна третья форма.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct question.",
                "options": [
                    "Did she had left?",
                    "Had she left?",
                    "Had she leave?",
                    "Did she left?",
                ],
                "answer": "Had she left?",
                "explanation": "Вопрос Past Perfect: Had + subject + V3?",
            },

            {
                "order": 18,
                "prompt": "When I arrived, she ___. She was already gone.",
                "options": [
                    "left",
                    "had left",
                    "has left",
                    "was leaving after me",
                ],
                "answer": "had left",
                "explanation": "Она ушла раньше моего приезда.",
            },

            {
                "order": 19,
                "prompt": "When I arrived, she ___. I saw her walk out.",
                "options": [
                    "had left before",
                    "left",
                    "has left",
                    "had gone already",
                ],
                "answer": "left",
                "explanation": "Здесь она ушла после моего приезда, поэтому Past Simple.",
            },

            {
                "order": 20,
                "prompt": "Choose the natural sequence.",
                "options": [
                    "I had got up, had washed my face and had gone to work.",
                    "I got up, washed my face and went to work.",
                    "I had get up, washed my face and went.",
                    "I got up, had washed my face and had went to work.",
                ],
                "answer": "I got up, washed my face and went to work.",
                "explanation": "Для обычной последовательности событий Past Simple достаточно.",
            },

            {
                "order": 21,
                "prompt": "I arrived at work late because I ___ the bus.",
                "options": [
                    "missed later",
                    "had missed",
                    "have missed",
                    "was missed",
                ],
                "answer": "had missed",
                "explanation": "Сначала автобус был пропущен, потом человек опоздал.",
            },

            {
                "order": 22,
                "prompt": "Before the storm started, the weather ___ warm.",
                "options": [
                    "had been",
                    "has been",
                    "was been",
                    "had be",
                ],
                "answer": "had been",
                "explanation": "Past Perfect глагола be: had been.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct pair.",
                "options": [
                    "At five, he was reading. / By five, he had read the book.",
                    "At five, he had read. / By five, he was reading always.",
                    "At five, he has read. / By five, he was read.",
                    "At five, he did read. / By five, he had reading.",
                ],
                "answer": "At five, he was reading. / By five, he had read the book.",
                "explanation": "AT показывает процесс в момент; BY — завершение к моменту.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct event order.",
                "options": [
                    "The train had left before we arrived.",
                    "The train has left before we arrived.",
                    "The train had leave before we arrived.",
                    "The train left before we had arrive.",
                ],
                "answer": "The train had left before we arrived.",
                "explanation": "Более раннее действие → Past Perfect; более позднее → Past Simple.",
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
                "✅ A1 Lesson 34 seeded: Past Perfect"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
