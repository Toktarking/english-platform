from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 35: "
        "Past Perfect Continuous."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=35,
            defaults={
                "title": "Past Perfect Continuous",
                "slug": "past-perfect-continuous",
                "theory_text": (
                    "Past Perfect Continuous: "
                    "had been + verb-ing."
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
                "title": "Что такое Past Perfect Continuous",
                "body": """Past Perfect Continuous показывает длительный процесс, который начался раньше другого момента в прошлом.

Пример:

I had been working for three hours before he arrived.

Сначала:

я начал работать;

работал три часа.

Потом:

он пришёл.

Главная идея:

процесс продолжался до другого события или момента в прошлом.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Формула:

subject + had been + verb-ing

Примеры:

I had been working.

She had been studying.

They had been waiting.

He had been sleeping.

HAD BEEN одинаково используется со всеми подлежащими:

I;

you;

he;

she;

it;

we;

they.""",
            },

            {
                "order": 3,
                "title": "Как образуется -ING",
                "body": """Обычный случай:

work → working

read → reading

play → playing

Глагол на немую e:

write → writing

make → making

come → coming

Короткий глагол:

sit → sitting

run → running

swim → swimming

Глагол на -ie:

lie → lying

die → dying""",
            },

            {
                "order": 4,
                "title": "Длительность до прошлого момента",
                "body": """Past Perfect Continuous показывает, как долго действие продолжалось до другого момента прошлого.

Примеры:

I had been studying for two hours before the lesson started.

She had been working all day before she went home.

They had been waiting for an hour before the bus arrived.

We had been travelling for ten hours before we reached the hotel.""",
            },

            {
                "order": 5,
                "title": "FOR и SINCE",
                "body": """FOR показывает продолжительность.

for two hours

for three days

for five years

Пример:

I had been working for three hours.

SINCE показывает начальную точку.

since morning

since Monday

since 2019

since five o'clock

Пример:

She had been working since morning.

Запомните:

FOR = сколько времени

SINCE = с какого момента""",
            },

            {
                "order": 6,
                "title": "HOW LONG",
                "body": """Чтобы спросить о продолжительности:

How long had + subject + been + verb-ing?

Примеры:

How long had you been working before he arrived?

How long had she been studying before the exam?

How long had they been waiting?

Ответ:

I had been working for three hours.

She had been living there since 2020.""",
            },

            {
                "order": 7,
                "title": "Причина результата в прошлом",
                "body": """Past Perfect Continuous может объяснять прошлое состояние.

Пример:

She was tired because she had been working all day.

Результат в прошлом:

she was tired

Причина:

she had been working all day

Другие примеры:

He was wet because he had been walking in the rain.

Her eyes were red because she had been crying.

The ground was wet because it had been raining.""",
            },

            {
                "order": 8,
                "title": "BEFORE, WHEN и BY THE TIME",
                "body": """BEFORE:

I had been waiting for an hour before the bus arrived.

WHEN:

I had been working for two hours when he arrived.

BY THE TIME:

By the time he arrived, I had been waiting for an hour.

Во всех случаях:

длительный процесс начался раньше;

позднее событие обычно стоит в Past Simple.""",
            },

            {
                "order": 9,
                "title": "ALL DAY, ALL NIGHT, ALL WEEK",
                "body": """Past Perfect Continuous часто используется с длительными периодами.

Примеры:

She had been working all day.

They had been travelling all night.

It had been raining all week.

We had been preparing for the exam all month.

Такие выражения подчёркивают длительность процесса.""",
            },

            {
                "order": 10,
                "title": "Отрицание и вопросы",
                "body": """Отрицание:

subject + hadn't been + verb-ing

I hadn't been sleeping well.

She hadn't been working.

They hadn't been waiting long.

Вопрос:

Had + subject + been + verb-ing?

Had you been working?

Had she been studying?

Краткие ответы:

Yes, I had.

No, I hadn't.

Yes, she had.

No, she hadn't.""",
            },

            {
                "order": 11,
                "title": "Специальные вопросы",
                "body": """Формула:

Question word + had + subject + been + verb-ing?

Примеры:

What had you been doing?

Where had she been working?

Why had they been waiting?

How long had he been sleeping?

Who had she been talking to?

Если WHO само выполняет действие:

Who had been using my computer?

Who had been calling you?""",
            },

            {
                "order": 12,
                "title": "Past Continuous или Past Perfect Continuous",
                "body": """Past Continuous показывает процесс в конкретный момент прошлого.

At six, I was working.

Past Perfect Continuous показывает, как долго процесс уже продолжался к этому моменту.

By six, I had been working for three hours.

Сравните:

At six, she was studying.
— в шесть она занималась.

By six, she had been studying for three hours.
— к шести она занималась уже три часа.""",
            },

            {
                "order": 13,
                "title": "Past Perfect или Past Perfect Continuous",
                "body": """Past Perfect:

had + V3

Подчёркивает:

результат;

завершённость;

количество.

She had written five pages.

Past Perfect Continuous:

had been + verb-ing

Подчёркивает:

процесс;

продолжительность;

причину прошлого результата.

She had been writing for two hours.

Простое правило:

Сколько сделано? → Past Perfect

Как долго? → Past Perfect Continuous""",
            },

            {
                "order": 14,
                "title": "Глаголы состояния и выбор времени",
                "body": """Глаголы состояния обычно не используются в Continuous.

Например:

know;

understand;

like;

want;

need;

believe;

own;

belong.

Правильно:

I had known him for ten years.

Не:

I had been knowing him.

HAVE как владение:

I had had that phone for two years.

Главный алгоритм:

важна длительность процесса → Past Perfect Continuous

важен готовый результат или количество → Past Perfect

глагол состояния → обычно Past Perfect""",
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
                    "We ___ been waiting for an hour "
                    "before the bus arrived."
                ),
                "options": ["have", "had", "were", "did"],
                "answer": "had",
                "explanation": (
                    "Past Perfect Continuous использует had been."
                ),
            },

            {
                "order": 2,
                "prompt": "My sister had been ___ all morning.",
                "options": [
                    "study",
                    "studied",
                    "studying",
                    "studies",
                ],
                "answer": "studying",
                "explanation": (
                    "После had been используется verb-ing."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "They had been living there ___ ten years."
                ),
                "options": [
                    "since",
                    "for",
                    "ago",
                    "during",
                ],
                "answer": "for",
                "explanation": (
                    "Ten years — продолжительность, поэтому for."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "He had been working there ___ 2019."
                ),
                "options": [
                    "for",
                    "since",
                    "from",
                    "ago",
                ],
                "answer": "since",
                "explanation": (
                    "2019 — начальная точка, поэтому since."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "___ she been crying before you arrived?"
                ),
                "options": [
                    "Did",
                    "Had",
                    "Was",
                    "Has",
                ],
                "answer": "Had",
                "explanation": (
                    "Вопрос: Had + subject + been + verb-ing?"
                ),
            },

            {
                "order": 6,
                "prompt": "How long ___ they been waiting?",
                "options": [
                    "did",
                    "had",
                    "were",
                    "have",
                ],
                "answer": "had",
                "explanation": (
                    "Past Perfect Continuous question: "
                    "How long had they been waiting?"
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "The ground was wet because it ___."
                ),
                "options": [
                    "rained yesterday",
                    "had been raining",
                    "has been raining",
                    "was rain",
                ],
                "answer": "had been raining",
                "explanation": (
                    "Длительный предыдущий процесс объясняет "
                    "результат в прошлом."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "She was tired because she ___ all night."
                ),
                "options": [
                    "had been studying",
                    "had studied five chapters only",
                    "was study",
                    "has studied",
                ],
                "answer": "had been studying",
                "explanation": (
                    "Усталость — результат длительного процесса."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "He ___ three reports before the meeting."
                ),
                "options": [
                    "had been writing",
                    "had written",
                    "had wrote",
                    "was written",
                ],
                "answer": "had written",
                "explanation": (
                    "Three reports — количество готовых результатов, "
                    "поэтому Past Perfect."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "He ___ reports for four hours "
                    "before the meeting."
                ),
                "options": [
                    "had written three",
                    "had been writing",
                    "was wrote",
                    "wrote since",
                ],
                "answer": "had been writing",
                "explanation": (
                    "For four hours подчёркивает длительность процесса."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "I ___ him for years before he moved."
                ),
                "options": [
                    "had been knowing",
                    "had known",
                    "was knowing",
                    "knew and still know now",
                ],
                "answer": "had known",
                "explanation": (
                    "Know — глагол состояния, поэтому Past Perfect."
                ),
            },

            {
                "order": 12,
                "prompt": "Had she been working?",
                "options": [
                    "Yes, she had.",
                    "Yes, she did.",
                    "Yes, she was.",
                    "Yes, she has.",
                ],
                "answer": "Yes, she had.",
                "explanation": (
                    "Краткий ответ повторяет had."
                ),
            },

            {
                "order": 13,
                "prompt": "They hadn't been ___ long.",
                "options": [
                    "wait",
                    "waited",
                    "waiting",
                    "waits",
                ],
                "answer": "waiting",
                "explanation": (
                    "Hadn't been + verb-ing."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "By the time I arrived, "
                    "he ___ for two hours."
                ),
                "options": [
                    "had slept",
                    "had been sleeping",
                    "was slept",
                    "has been sleeping",
                ],
                "answer": "had been sleeping",
                "explanation": (
                    "Длительный процесс продолжался два часа "
                    "до моего прихода."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "She had ___ the room before the guests came."
                ),
                "options": [
                    "been cleaning for two hours",
                    "cleaned",
                    "clean",
                    "cleaning",
                ],
                "answer": "cleaned",
                "explanation": (
                    "Если важен готовый результат, используется "
                    "Past Perfect: had cleaned."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I had been work for three hours.",
                    "I had been working for three hours.",
                    "I had working for three hours.",
                    "I was been working for three hours.",
                ],
                "answer": (
                    "I had been working for three hours."
                ),
                "explanation": (
                    "Правильная формула: had been + verb-ing."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct question.",
                "options": [
                    "Did they been waiting?",
                    "Had they been waiting?",
                    "Were they been waiting?",
                    "Had they been waited?",
                ],
                "answer": "Had they been waiting?",
                "explanation": (
                    "Вопрос строится через Had."
                ),
            },

            {
                "order": 18,
                "prompt": (
                    "By six, I ___ for four hours."
                ),
                "options": [
                    "was working",
                    "had been working",
                    "have been working",
                    "had worked four tasks",
                ],
                "answer": "had been working",
                "explanation": (
                    "By six + продолжительность до прошлого момента "
                    "→ Past Perfect Continuous."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "At six, I ___."
                ),
                "options": [
                    "had been working for four hours necessarily",
                    "was working",
                    "have worked",
                    "had working",
                ],
                "answer": "was working",
                "explanation": (
                    "At six показывает процесс именно в этот момент "
                    "→ Past Continuous."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "How many emails had she ___ before lunch?"
                ),
                "options": [
                    "been writing",
                    "written",
                    "wrote",
                    "writing",
                ],
                "answer": "written",
                "explanation": (
                    "How many спрашивает количество завершённых "
                    "результатов → Past Perfect."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "How long had she ___ before lunch?"
                ),
                "options": [
                    "written five emails",
                    "been writing",
                    "been written",
                    "wrote",
                ],
                "answer": "been writing",
                "explanation": (
                    "How long спрашивает длительность процесса."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I had been knowing her for years.",
                    "I had known her for years.",
                    "I had knowing her for years.",
                    "I was knowing her for years.",
                ],
                "answer": "I had known her for years.",
                "explanation": (
                    "Know — stative verb и обычно не используется "
                    "в Continuous."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct pair."
                ),
                "options": [
                    (
                        "She had written five pages. / "
                        "She had been writing for two hours."
                    ),
                    (
                        "She had been writing five pages. / "
                        "She had written for two hours."
                    ),
                    (
                        "She had wrote five pages. / "
                        "She had been wrote for two hours."
                    ),
                    (
                        "She was written five pages. / "
                        "She had writing for two hours."
                    ),
                ],
                "answer": (
                    "She had written five pages. / "
                    "She had been writing for two hours."
                ),
                "explanation": (
                    "Количество → Past Perfect; "
                    "длительность → Past Perfect Continuous."
                ),
            },

            {
                "order": 24,
                "prompt": (
                    "Choose the correct cause-and-result sentence."
                ),
                "options": [
                    (
                        "He was out of breath because "
                        "he had been running."
                    ),
                    (
                        "He was out of breath because "
                        "he had been ran."
                    ),
                    (
                        "He was out of breath because "
                        "he did been running."
                    ),
                    (
                        "He was out of breath because "
                        "he had running."
                    ),
                ],
                "answer": (
                    "He was out of breath because "
                    "he had been running."
                ),
                "explanation": (
                    "Past Perfect Continuous объясняет причину "
                    "прошлого результата."
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
                "✅ A1 Lesson 35 seeded: "
                "Past Perfect Continuous"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
