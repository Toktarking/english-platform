from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 50: "
        "Wish and If only."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=50,
            defaults={
                "title": "Wish / If only",
                "slug": "wish-if-only",
                "theory_text": (
                    "Wish and If only: wishes, regrets "
                    "and unreal situations."
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
                "title": "Что означают WISH и IF ONLY",
                "body": """WISH и IF ONLY используются, когда человек хочет, чтобы ситуация была другой.

Они могут выражать:

сожаление о настоящем;

сожаление о прошлом;

сильное желание;

мечту;

желание изменить поведение;

недовольство ситуацией.

Примеры:

I wish I had more time.

If only I had more time!

IF ONLY обычно звучит сильнее и эмоциональнее.""",
            },

            {
                "order": 2,
                "title": "WISH о настоящем",
                "body": """Если хочется изменить настоящую ситуацию, после WISH используется Past Simple.

Формула:

wish + subject + Past Simple

Пример:

I wish I had more money.

Реальность:

I don't have much money.

Ещё примеры:

I wish I lived near the sea.

She wishes she spoke English better.

He wishes he knew the answer.

Past Simple здесь не означает прошлое.

Он показывает нереальность настоящей ситуации.""",
            },

            {
                "order": 3,
                "title": "WERE после WISH",
                "body": """С глаголом TO BE в стандартном английском часто используется WERE.

Примеры:

I wish I were taller.

She wishes she were here.

He wishes he were younger.

We wish it were warmer.

В разговорной речи можно услышать:

I wish I was taller.

Но в учебных заданиях безопаснее использовать WERE.""",
            },

            {
                "order": 4,
                "title": "IF ONLY о настоящем",
                "body": """IF ONLY использует ту же грамматику, что и WISH.

Для настоящего:

If only + Past Simple

Примеры:

If only I had more time!

If only she lived closer!

If only we knew the answer!

If only it were warmer!

IF ONLY обычно выражает более сильное сожаление или желание.""",
            },

            {
                "order": 5,
                "title": "WISH + COULD",
                "body": """WISH + COULD используется, когда человек хочет иметь способность или возможность, которой сейчас нет.

Формула:

wish + subject + could + V1

Примеры:

I wish I could drive.

She wishes she could speak French.

We wish we could travel more often.

He wishes he could help us.

Реальность:

I wish I could swim.

= I can't swim.""",
            },

            {
                "order": 6,
                "title": "WISH о прошлом",
                "body": """Если человек сожалеет о прошлом, используется Past Perfect.

Формула:

wish + subject + had + V3

Пример:

I wish I had studied harder.

Это значит:

я учился недостаточно;

прошлое уже нельзя изменить;

я об этом сожалею.

Ещё примеры:

She wishes she had accepted the offer.

We wish we had left earlier.

I wish I had known about the meeting.""",
            },

            {
                "order": 7,
                "title": "HADN'T и IF ONLY о прошлом",
                "body": """Если человек сожалеет о совершённом действии:

wish + hadn't + V3

Примеры:

I wish I hadn't said that.

She wishes she hadn't left her job.

We wish we hadn't spent so much money.

IF ONLY использует ту же модель:

If only I had known!

If only we had left earlier!

If only I hadn't forgotten my passport!""",
            },

            {
                "order": 8,
                "title": "WISH + WOULD",
                "body": """WISH + WOULD используется, когда хочется изменить:

чужое поведение;

внешнюю ситуацию;

работу предмета;

ситуацию в будущем.

Формула:

wish + subject + would + V1

Примеры:

I wish you would listen to me.

We wish the rain would stop.

He wishes the bus would come.

I wish the computer would work properly.

Эта конструкция часто выражает раздражение.""",
            },

            {
                "order": 9,
                "title": "Когда WOULD не подходит",
                "body": """WISH + WOULD обычно не используется для собственного контролируемого решения.

Неестественно:

I wish I would study more.

Лучше:

I wish I studied more.

Или:

I wish I could study more.

WISH + WOULD обычно означает:

я хочу, чтобы кто-то или что-то изменилось,

но я не контролирую это напрямую.""",
            },

            {
                "order": 10,
                "title": "WISH и HOPE",
                "body": """HOPE используется для реальной возможности.

I hope she comes tomorrow.

I hope I pass the exam.

We hope the weather will improve.

WISH используется для нереальной или неудовлетворительной ситуации.

I wish she were here.

I wish I had passed the exam.

We wish the weather were better.

Сравните:

I hope I pass the exam.
— экзамен ещё впереди.

I wish I had passed the exam.
— экзамен уже был.""",
            },

            {
                "order": 11,
                "title": "Четыре основные модели WISH",
                "body": """1. Нереальное настоящее:

wish + Past Simple

I wish I knew.

2. Сожаление о прошлом:

wish + Past Perfect

I wish I had known.

3. Желание изменить поведение:

wish + would + V1

I wish he would listen.

4. Отсутствие способности:

wish + could + V1

I wish I could help.""",
            },

            {
                "order": 12,
                "title": "WISH и условные предложения",
                "body": """WISH связан с Second Conditional.

If I had more money, I would travel.

I wish I had more money.

В обоих случаях HAD описывает нереальное настоящее.

WISH также связан с Third Conditional.

If I had studied more, I would have passed.

I wish I had studied more.

Оба предложения относятся к нереальному прошлому.""",
            },

            {
                "order": 13,
                "title": "Типичные ошибки",
                "body": """Неправильно:

I wish I know the answer.

Правильно:

I wish I knew the answer.

Неправильно:

I wish I have more money.

Правильно:

I wish I had more money.

Неправильно:

I wish I studied harder last year.

Правильно:

I wish I had studied harder last year.

Неправильно:

I wish I had went earlier.

Правильно:

I wish I had gone earlier.""",
            },

            {
                "order": 14,
                "title": "Как выбрать форму",
                "body": """Хотите изменить настоящее?

→ wish + Past Simple

I wish I had more time.

Сожалеете о прошлом?

→ wish + Past Perfect

I wish I had studied harder.

Хотите изменить чьё-то поведение?

→ wish + would

I wish he would listen.

Хотите иметь способность или возможность?

→ wish + could

I wish I could drive.

Это реальная надежда на будущее?

→ HOPE

I hope she comes tomorrow.""",
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
                "prompt": "I wish I ___ taller.",
                "options": [
                    "am",
                    "were",
                    "will be",
                    "had been yesterday only",
                ],
                "answer": "were",
                "explanation": (
                    "Нереальное настоящее с be → wish + were."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "She wishes she ___ closer to work."
                ),
                "options": [
                    "lives",
                    "lived",
                    "will live",
                    "would have lived",
                ],
                "answer": "lived",
                "explanation": (
                    "Желание изменить настоящее → Past Simple."
                ),
            },

            {
                "order": 3,
                "prompt": "We wish we ___ more money.",
                "options": [
                    "have",
                    "had",
                    "will have",
                    "had had last year only",
                ],
                "answer": "had",
                "explanation": (
                    "Нереальная ситуация сейчас → wish + Past Simple."
                ),
            },

            {
                "order": 4,
                "prompt": "He wishes he ___ the answer.",
                "options": [
                    "knows",
                    "knew",
                    "will know",
                    "had know",
                ],
                "answer": "knew",
                "explanation": (
                    "Сейчас он не знает ответа → knew."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "I wish I ___ the job last year."
                ),
                "options": [
                    "accepted",
                    "had accepted",
                    "would accept",
                    "accept",
                ],
                "answer": "had accepted",
                "explanation": (
                    "Сожаление о прошлом → Past Perfect."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "She wishes she ___ so much money."
                ),
                "options": [
                    "didn't spend",
                    "hadn't spent",
                    "wouldn't spend yesterday",
                    "doesn't spend",
                ],
                "answer": "hadn't spent",
                "explanation": (
                    "Сожаление о совершённом прошлом действии."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "We wish we ___ the tickets earlier."
                ),
                "options": [
                    "booked",
                    "had booked",
                    "would book",
                    "book",
                ],
                "answer": "had booked",
                "explanation": (
                    "Прошлое уже нельзя изменить → had booked."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "I wish he ___ me more carefully."
                ),
                "options": [
                    "listens to",
                    "would listen to",
                    "had listened every day",
                    "will listen to",
                ],
                "answer": "would listen to",
                "explanation": (
                    "Желание изменить чужое поведение → would."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "She wishes her neighbours ___ quieter."
                ),
                "options": [
                    "are",
                    "would be",
                    "had been yesterday only",
                    "will being",
                ],
                "answer": "would be",
                "explanation": (
                    "Хотим изменить поведение/ситуацию."
                ),
            },

            {
                "order": 10,
                "prompt": "I wish the rain ___.",
                "options": [
                    "stops",
                    "would stop",
                    "had stopped every day",
                    "will stop",
                ],
                "answer": "would stop",
                "explanation": (
                    "Внешняя неприятная ситуация → wish + would."
                ),
            },

            {
                "order": 11,
                "prompt": "He wishes he ___ speak Spanish.",
                "options": [
                    "can",
                    "could",
                    "will can",
                    "could to",
                ],
                "answer": "could",
                "explanation": (
                    "Отсутствие способности → wish + could."
                ),
            },

            {
                "order": 12,
                "prompt": "If only we ___ longer!",
                "options": [
                    "can stay",
                    "could stay",
                    "will stay",
                    "had staying",
                ],
                "answer": "could stay",
                "explanation": (
                    "Сильное желание иметь возможность → could."
                ),
            },

            {
                "order": 13,
                "prompt": (
                    "I hope the weather ___ tomorrow."
                ),
                "options": [
                    "improved",
                    "improves",
                    "had improved",
                    "would improve because of regret",
                ],
                "answer": "improves",
                "explanation": (
                    "Реальная надежда на будущее → hope."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "I wish the weather ___ better now."
                ),
                "options": [
                    "is",
                    "were",
                    "will be",
                    "had been yesterday",
                ],
                "answer": "were",
                "explanation": (
                    "Нереальная ситуация сейчас → wish + were."
                ),
            },

            {
                "order": 15,
                "prompt": "If only I ___ that mistake!",
                "options": [
                    "didn't make",
                    "hadn't made",
                    "wouldn't make yesterday",
                    "don't make",
                ],
                "answer": "hadn't made",
                "explanation": (
                    "Сильное сожаление о прошлом → had not + V3."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I wish I know the answer.",
                    "I wish I knew the answer.",
                    "I wish I will know the answer.",
                    "I wish I knowing the answer.",
                ],
                "answer": "I wish I knew the answer.",
                "explanation": (
                    "Нереальное настоящее → Past Simple."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I wish I have more time.",
                    "I wish I had more time.",
                    "I wish I will have more time.",
                    "I wish I would have more time.",
                ],
                "answer": "I wish I had more time.",
                "explanation": (
                    "Для неудовлетворительной ситуации сейчас → had."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct regret about the past.",
                "options": [
                    "I wish I studied harder last year.",
                    "I wish I had studied harder last year.",
                    "I wish I would study harder last year.",
                    "I wish I study harder last year.",
                ],
                "answer": (
                    "I wish I had studied harder last year."
                ),
                "explanation": (
                    "Сожаление о прошлом → Past Perfect."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct V3 form.",
                "options": [
                    "I wish I had went earlier.",
                    "I wish I had gone earlier.",
                    "I wish I had go earlier.",
                    "I wish I went earlier yesterday regret.",
                ],
                "answer": "I wish I had gone earlier.",
                "explanation": (
                    "Go → went → gone; после had нужен V3."
                ),
            },

            {
                "order": 20,
                "prompt": "Which sentence expresses a real hope?",
                "options": [
                    "I hope she comes tomorrow.",
                    "I wish she were here now.",
                    "I wish she had come yesterday.",
                    "If only she were here!",
                ],
                "answer": "I hope she comes tomorrow.",
                "explanation": (
                    "Hope используется для реальной будущей возможности."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "Which sentence expresses irritation "
                    "about someone's behaviour?"
                ),
                "options": [
                    "I wish you would stop shouting.",
                    "I wish you stopped yesterday.",
                    "I hope you shouted.",
                    "I wish I had shouted.",
                ],
                "answer": "I wish you would stop shouting.",
                "explanation": (
                    "Wish + would часто выражает раздражение."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct present/past pair.",
                "options": [
                    (
                        "I wish I knew the answer. / "
                        "I wish I had known the answer."
                    ),
                    (
                        "I wish I know the answer. / "
                        "I wish I knew the answer yesterday."
                    ),
                    (
                        "I wish I will know the answer. / "
                        "I wish I had knew the answer."
                    ),
                    (
                        "I wish I knowing the answer. / "
                        "I wish I would known the answer."
                    ),
                ],
                "answer": (
                    "I wish I knew the answer. / "
                    "I wish I had known the answer."
                ),
                "explanation": (
                    "Knew = нереальное настоящее; "
                    "had known = сожаление о прошлом."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct WISH/HOPE pair.",
                "options": [
                    (
                        "I wish she were here now. / "
                        "I hope she comes tomorrow."
                    ),
                    (
                        "I wish she will be here now. / "
                        "I hope she were here tomorrow."
                    ),
                    (
                        "I wish she is here now. / "
                        "I hope she had come tomorrow."
                    ),
                    (
                        "I wish she comes now. / "
                        "I hope she would came tomorrow."
                    ),
                ],
                "answer": (
                    "I wish she were here now. / "
                    "I hope she comes tomorrow."
                ),
                "explanation": (
                    "Wish = нереальная ситуация; "
                    "hope = реальная будущая надежда."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "I wish I had more time. / "
                        "I wish I had studied harder. / "
                        "I wish he would listen. / "
                        "I wish I could drive."
                    ),
                    (
                        "I wish I have more time. / "
                        "I wish I studied harder yesterday. / "
                        "I wish he will listen. / "
                        "I wish I can drive."
                    ),
                    (
                        "I wish I would have more time. / "
                        "I wish I had study harder. / "
                        "I wish he would listens. / "
                        "I wish I could to drive."
                    ),
                    (
                        "I wish I had had more time now. / "
                        "I wish I will study harder yesterday. / "
                        "I wish he listened tomorrow would. / "
                        "I wish I can to drive."
                    ),
                ],
                "answer": (
                    "I wish I had more time. / "
                    "I wish I had studied harder. / "
                    "I wish he would listen. / "
                    "I wish I could drive."
                ),
                "explanation": (
                    "Present → Past Simple; past regret → Past Perfect; "
                    "behaviour → would; ability → could."
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
                "✅ A1 Lesson 50 seeded: Wish / If only"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
