from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 29: "
        "Past Simple vs Past Continuous."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=29,
            defaults={
                "title": "Past Simple и Past Continuous",
                "slug": "past-simple-vs-past-continuous",
                "theory_text": (
                    "Past Simple vs Past Continuous."
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
                "title": "Главное различие",
                "body": """Оба времени относятся к прошлому, но показывают действие по-разному.

Past Simple:

I worked yesterday.

Действие рассматривается как завершённый факт.

Past Continuous:

I was working at six yesterday.

Подчёркивается процесс в конкретный момент прошлого.

Главный вопрос:

это завершённое событие или процесс?""",
            },

            {
                "order": 2,
                "title": "Когда нужен Past Simple",
                "body": """Past Simple используется для:

завершённого действия;

короткого события;

последовательности действий;

привычки в прошлом;

состояния в прошлом.

Примеры:

I finished the report.

She called me.

They went home.

We played outside every day.

He was tired.""",
            },

            {
                "order": 3,
                "title": "Когда нужен Past Continuous",
                "body": """Past Continuous используется для:

действия в процессе;

действия в определённый момент прошлого;

фонового действия;

длительного действия, которое было прервано;

двух одновременных действий.

Примеры:

I was working at six.

She was sleeping when I called.

They were playing while we were studying.

It was raining.""",
            },

            {
                "order": 4,
                "title": "Сравнение форм",
                "body": """Past Simple с правильным глаголом:

subject + verb-ed

I worked.

She studied.

Past Simple с неправильным глаголом:

subject + Past Simple form

I went.

She saw.

Past Continuous:

subject + was/were + verb-ing

I was working.

They were playing.""",
            },

            {
                "order": 5,
                "title": "Факт или процесс",
                "body": """Past Simple показывает действие как целое.

I read the report yesterday.

She cooked dinner.

Past Continuous показывает процесс.

I was reading the report at five.

She was cooking dinner when I arrived.

Сравните:

I had dinner at seven.
— Я поужинал в семь.

I was having dinner at seven.
— В семь я находился в процессе ужина.""",
            },

            {
                "order": 6,
                "title": "Длительное и короткое действие",
                "body": """Когда одно действие было в процессе, а другое его прервало:

длительное действие → Past Continuous

короткое событие → Past Simple

Формула:

Past Continuous + when + Past Simple

Пример:

I was sleeping when the phone rang.

Was sleeping — процесс.

Rang — короткое событие.""",
            },

            {
                "order": 7,
                "title": "WHEN",
                "body": """WHEN означает «когда».

Часто оно вводит короткое завершённое действие.

Примеры:

I was reading when she called.

He was walking home when he saw the accident.

We were eating when the door opened.

Порядок можно менять:

I was sleeping when you called.

When you called, I was sleeping.""",
            },

            {
                "order": 8,
                "title": "WHILE",
                "body": """WHILE означает:

пока;

в то время как.

Обычно после while стоит длительный процесс.

Примеры:

While I was reading, she was cooking.

He called while I was working.

Если два процесса происходили одновременно:

I was cooking while my wife was cleaning.

She was reading while the child was sleeping.""",
            },

            {
                "order": 9,
                "title": "Последовательность действий",
                "body": """Если несколько завершённых действий произошли одно за другим, обычно используется Past Simple.

Пример:

I woke up, got dressed, had breakfast and left home.

Все действия завершились последовательно.

Не нужно превращать такую обычную последовательность в Past Continuous.

Past Simple хорошо показывает:

сначала это;

потом это;

затем следующее действие.""",
            },

            {
                "order": 10,
                "title": "Фон и главное событие",
                "body": """Past Continuous часто описывает фон.

It was raining.

People were running home.

Cars were moving slowly.

Past Simple показывает главное событие:

Suddenly, the lights went out.

Таким образом:

Past Continuous = обстановка, фон;

Past Simple = событие, которое произошло на этом фоне.""",
            },

            {
                "order": 11,
                "title": "Конкретный момент прошлого",
                "body": """Если важно, что действие происходило в определённый момент:

Past Continuous.

At six, I was working.

At midnight, she was sleeping.

This time yesterday, we were flying to Astana.

Если речь о времени завершённого действия:

Past Simple.

I started work at six.

She went to bed at midnight.

We arrived yesterday.""",
            },

            {
                "order": 12,
                "title": "Вопросы и отрицания",
                "body": """Past Simple:

Did you work yesterday?

Where did they go?

I didn't work.

They didn't go.

Past Continuous:

Were you working at six?

What were they doing?

I wasn't working.

They weren't waiting.

Сравните:

What did you do yesterday?
— Что вы делали вчера в целом?

What were you doing at six?
— Что вы делали именно в шесть?""",
            },

            {
                "order": 13,
                "title": "Глаголы состояния и HAVE",
                "body": """Некоторые глаголы состояния обычно не используются в Continuous:

know;

understand;

like;

want;

need;

believe;

remember.

Правильно:

I knew the answer.

Не:

I was knowing the answer.

HAVE как владение:

I had a car.

HAVE как действие:

I was having breakfast.

She was having a shower.""",
            },

            {
                "order": 14,
                "title": "Как выбрать время",
                "body": """Шаг 1.

Это завершённый факт?

→ Past Simple

I finished the report.

Шаг 2.

Это процесс в определённый момент?

→ Past Continuous

I was writing the report at six.

Шаг 3.

Одно действие прервало другое?

→ длительное: Past Continuous

→ короткое: Past Simple

I was writing when the computer stopped.

Шаг 4.

Два процесса одновременно?

→ часто Past Continuous в обеих частях

I was writing while she was reading.""",
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
                "prompt": "I ___ television when she called.",
                "options": [
                    "watched",
                    "was watching",
                    "watch",
                    "were watching",
                ],
                "answer": "was watching",
                "explanation": "Просмотр был длительным процессом, который прервал звонок.",
            },

            {
                "order": 2,
                "prompt": "She ___ me while I was working.",
                "options": [
                    "called",
                    "was calling once",
                    "calls",
                    "call",
                ],
                "answer": "called",
                "explanation": "Звонок — короткое завершённое событие.",
            },

            {
                "order": 3,
                "prompt": "They ___ football when it started to rain.",
                "options": [
                    "played",
                    "were playing",
                    "play",
                    "was playing",
                ],
                "answer": "were playing",
                "explanation": "Игра была в процессе, когда начался дождь.",
            },

            {
                "order": 4,
                "prompt": "We ___ home when we saw the accident.",
                "options": [
                    "drove",
                    "were driving",
                    "drive",
                    "was driving",
                ],
                "answer": "were driving",
                "explanation": "Движение домой было процессом; saw — короткое событие.",
            },

            {
                "order": 5,
                "prompt": "He ___ the door and entered the room.",
                "options": [
                    "was opening",
                    "opened",
                    "opens",
                    "opening",
                ],
                "answer": "opened",
                "explanation": "Последовательность завершённых действий → Past Simple.",
            },

            {
                "order": 6,
                "prompt": "While I was reading, my sister ___ music.",
                "options": [
                    "listened to",
                    "was listening to",
                    "listens to",
                    "did listening to",
                ],
                "answer": "was listening to",
                "explanation": "Два процесса происходили одновременно.",
            },

            {
                "order": 7,
                "prompt": "At midnight, the children ___.",
                "options": [
                    "slept as a fact",
                    "were sleeping",
                    "sleep",
                    "was sleeping",
                ],
                "answer": "were sleeping",
                "explanation": "Процесс в конкретный момент прошлого → Past Continuous.",
            },

            {
                "order": 8,
                "prompt": "What ___ you doing at six?",
                "options": ["did", "were", "was", "are"],
                "answer": "were",
                "explanation": "Past Continuous question: What were you doing?",
            },

            {
                "order": 9,
                "prompt": "What ___ you do yesterday?",
                "options": ["were", "did", "was", "are"],
                "answer": "did",
                "explanation": "Вопрос о завершённых действиях в целом → Past Simple.",
            },

            {
                "order": 10,
                "prompt": "The lights ___ while we were having dinner.",
                "options": [
                    "went out",
                    "were going out",
                    "go out",
                    "did went out",
                ],
                "answer": "went out",
                "explanation": "Lights went out — короткое событие на фоне длительного действия.",
            },

            {
                "order": 11,
                "prompt": "I ___ breakfast, got dressed and left.",
                "options": [
                    "was having",
                    "had",
                    "have",
                    "were having",
                ],
                "answer": "had",
                "explanation": "Последовательность завершённых действий → Past Simple.",
            },

            {
                "order": 12,
                "prompt": "She ___ while she was driving.",
                "options": [
                    "didn't talk",
                    "wasn't talking",
                    "doesn't talk",
                    "not talking",
                ],
                "answer": "wasn't talking",
                "explanation": "Отрицательный процесс в Past Continuous: wasn't + verb-ing.",
            },

            {
                "order": 13,
                "prompt": "They ___ the answer.",
                "options": [
                    "were understanding",
                    "understood",
                    "did understood",
                    "understanding",
                ],
                "answer": "understood",
                "explanation": "Understand — глагол состояния; используется Past Simple.",
            },

            {
                "order": 14,
                "prompt": "Was he working?",
                "options": [
                    "Yes, he did.",
                    "Yes, he was.",
                    "Yes, he worked.",
                    "Yes, he were.",
                ],
                "answer": "Yes, he was.",
                "explanation": "Вопрос с was требует краткого ответа с was.",
            },

            {
                "order": 15,
                "prompt": "Did he work yesterday?",
                "options": [
                    "Yes, he was.",
                    "Yes, he did.",
                    "Yes, he were.",
                    "Yes, he is.",
                ],
                "answer": "Yes, he did.",
                "explanation": "Вопрос с did требует ответа с did.",
            },

            {
                "order": 16,
                "prompt": "I ___ dinner at seven yesterday.",
                "options": [
                    "had",
                    "was having",
                    "have",
                    "am having",
                ],
                "answer": "had",
                "explanation": "Если ужин рассматривается как завершённый факт, используется Past Simple.",
            },

            {
                "order": 17,
                "prompt": "At seven yesterday, I ___ dinner.",
                "options": [
                    "had as a completed fact",
                    "was having",
                    "have",
                    "were having",
                ],
                "answer": "was having",
                "explanation": "В семь действие находилось в процессе.",
            },

            {
                "order": 18,
                "prompt": "When the teacher entered, the students ___.",
                "options": [
                    "were talking",
                    "talked once",
                    "talk",
                    "did talking",
                ],
                "answer": "were talking",
                "explanation": "Разговор уже происходил, когда вошёл преподаватель.",
            },

            {
                "order": 19,
                "prompt": "While they ___, I was cooking.",
                "options": [
                    "were studying",
                    "studied once",
                    "study",
                    "did studying",
                ],
                "answer": "were studying",
                "explanation": "Два параллельных длительных процесса.",
            },

            {
                "order": 20,
                "prompt": "Choose the correct sequence of completed actions.",
                "options": [
                    "I was waking up, was dressing and was leaving.",
                    "I woke up, got dressed and left.",
                    "I was woke up, dressed and leave.",
                    "I did wake up, got dressed and was left.",
                ],
                "answer": "I woke up, got dressed and left.",
                "explanation": "Последовательность завершённых действий требует Past Simple.",
            },

            {
                "order": 21,
                "prompt": "Choose the best background description.",
                "options": [
                    "It rained, people ran, cars moved, all at that exact moment.",
                    "It was raining, people were running, and cars were moving slowly.",
                    "It was rain and people were run.",
                    "It raining and people running.",
                ],
                "answer": "It was raining, people were running, and cars were moving slowly.",
                "explanation": "Для описания фона используется Past Continuous.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I was knowing the answer.",
                    "I knew the answer.",
                    "I did knew the answer.",
                    "I was know the answer.",
                ],
                "answer": "I knew the answer.",
                "explanation": "Know — глагол состояния.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct pair.",
                "options": [
                    "What did you do yesterday? / What were you doing at six?",
                    "What were you do yesterday? / What did you doing at six?",
                    "What did you doing yesterday? / What was you doing at six?",
                    "What were you doing yesterday? / What did you were doing at six?",
                ],
                "answer": "What did you do yesterday? / What were you doing at six?",
                "explanation": "Past Simple спрашивает о действиях в целом; Past Continuous — о процессе в момент.",
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sentence.",
                "options": [
                    "I slept when the phone was ringing once.",
                    "I was sleeping when the phone rang.",
                    "I was slept when the phone rang.",
                    "I sleeping when the phone did ring.",
                ],
                "answer": "I was sleeping when the phone rang.",
                "explanation": "Длительный процесс → Past Continuous; короткое событие → Past Simple.",
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
                "✅ A1 Lesson 29 seeded: "
                "Past Simple vs Past Continuous"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
