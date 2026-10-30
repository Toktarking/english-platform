from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 36: "
        "Future Simple with WILL."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=36,
            defaults={
                "title": "Future Simple с WILL",
                "slug": "future-simple-will",
                "theory_text": "Future Simple with WILL.",
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Future Simple",
                "body": """Future Simple — простое будущее время.

WILL часто используется, когда мы говорим:

о будущем действии;

о спонтанном решении;

об обещании;

о предложении помощи;

о предположении или прогнозе.

Примеры:

I will call you tomorrow.

She will help us.

I think it will rain.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Формула:

subject + will + base verb

Примеры:

I will work.

She will come.

They will study.

He will call.

WILL одинаково используется со всеми подлежащими:

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
                "title": "После WILL — первая форма",
                "body": """После WILL используется основная форма глагола.

Правильно:

will go

will work

will study

will come

will be

Неправильно:

will goes

will worked

will studying

will to come

Сокращение:

I will → I'll

she will → she'll

they will → they'll""",
            },

            {
                "order": 4,
                "title": "Будущее действие и маркеры",
                "body": """Future Simple может описывать будущее действие.

Примеры:

I will start work tomorrow.

She will visit us next week.

They will move next year.

We will meet on Monday.

Частые маркеры:

tomorrow;

next week;

next month;

next year;

soon;

later;

in an hour;

in two days;

in the future.""",
            },

            {
                "order": 5,
                "title": "Спонтанное решение",
                "body": """WILL часто используется, когда решение принимается прямо в момент речи.

Пример:

The phone is ringing.

I'll answer it.

Другие примеры:

I'm thirsty. I'll get some water.

It is cold. I'll close the window.

We don't have any bread. I'll buy some.

Someone is at the door. I'll open it.

Это не заранее подготовленный план.""",
            },

            {
                "order": 6,
                "title": "Обещания и предложение помощи",
                "body": """WILL часто используется в обещаниях:

I will help you.

I won't tell anyone.

I promise I will be careful.

I promise I won't be late.

Также WILL используется, когда человек предлагает помощь:

I'll carry your bag.

I'll open the door.

I'll explain the rule.

I'll help you with the task.""",
            },

            {
                "order": 7,
                "title": "Предположения и прогнозы",
                "body": """WILL используется для мнения или предположения о будущем.

Примеры:

I think it will rain tomorrow.

She will probably come.

They will win the match.

People will live longer in the future.

Частые выражения:

I think;

I don't think;

I believe;

probably;

perhaps;

maybe;

I'm sure;

I hope.""",
            },

            {
                "order": 8,
                "title": "PROBABLY и I DON'T THINK",
                "body": """В утвердительном предложении probably часто стоит после WILL:

She will probably come.

It will probably rain.

В отрицательном:

She probably won't come.

They probably won't agree.

Часто говорят:

I don't think he will come.

I don't think she will agree.

Так обычно звучит естественнее, чем:

I think he won't come.""",
            },

            {
                "order": 9,
                "title": "WILL BE и WILL HAVE",
                "body": """После WILL глагол TO BE используется в форме:

be

Правильно:

I will be at home.

She will be busy.

They will be ready.

Неправильно:

I will am

She will is

They will are

С HAVE:

I will have more time.

She will have a meeting.

Не:

She will has a meeting.""",
            },

            {
                "order": 10,
                "title": "Отрицание с WON'T",
                "body": """Отрицание:

will not

Сокращение:

won't

Формула:

subject + won't + base verb

Примеры:

I won't come.

She won't work tomorrow.

They won't agree.

It won't rain.

После won't также используется первая форма.

Не:

won't goes

won't worked

won't to come""",
            },

            {
                "order": 11,
                "title": "Вопросы и краткие ответы",
                "body": """В вопросе WILL ставится перед подлежащим.

Формула:

Will + subject + base verb?

Примеры:

Will you come?

Will she help us?

Will they arrive soon?

Краткие ответы:

Yes, I will.

No, I won't.

Yes, she will.

No, she won't.

В положительном кратком ответе обычно не говорят:

Yes, I'll.""",
            },

            {
                "order": 12,
                "title": "Специальные вопросы и SHALL",
                "body": """Специальный вопрос:

Question word + will + subject + verb?

Примеры:

What will you do?

Where will she go?

When will they arrive?

How will we get there?

WHO как подлежащее:

Who will help me?

SHALL чаще используется с I и WE в предложениях:

Shall I help you?

Shall I open the window?

Shall we start?

Shall we go?""",
            },

            {
                "order": 13,
                "title": "WHEN и IF: без WILL",
                "body": """После WHEN, BEFORE, AFTER, UNTIL, AS SOON AS и IF в придаточной части для будущего обычно используется Present Simple.

Правильно:

I will call you when I arrive.

If it rains, we will stay at home.

We will eat when she comes.

She will call me as soon as she arrives.

Неправильно:

I will call you when I will arrive.

If it will rain, we will stay at home.""",
            },

            {
                "order": 14,
                "title": "WILL или заранее подготовленный план",
                "body": """Используйте WILL, если:

решение принято сейчас;

это обещание;

это предложение помощи;

это мнение или прогноз.

Примеры:

I'll answer the phone.

I will never tell anyone.

I'll help you.

I think she will pass the exam.

Если план был подготовлен заранее, обычно лучше BE GOING TO или Present Continuous.

Пример:

I am going to visit my parents this weekend.

Подробно BE GOING TO — в следующем уроке.""",
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
                "prompt": "We ___ finish the project next week.",
                "options": ["will", "are will", "do", "have"],
                "answer": "will",
                "explanation": "Future Simple: subject + will + base verb.",
            },

            {
                "order": 2,
                "prompt": "My sister will ___ us tomorrow.",
                "options": [
                    "visits",
                    "visited",
                    "visit",
                    "visiting",
                ],
                "answer": "visit",
                "explanation": "После will используется первая форма.",
            },

            {
                "order": 3,
                "prompt": "I think they ___ win.",
                "options": ["are", "will", "do", "have"],
                "answer": "will",
                "explanation": "Прогноз на основе мнения → will.",
            },

            {
                "order": 4,
                "prompt": "He ___ be at home tonight.",
                "options": [
                    "won't",
                    "doesn't will",
                    "isn't will",
                    "not will",
                ],
                "answer": "won't",
                "explanation": "Отрицательная форма Future Simple — won't.",
            },

            {
                "order": 5,
                "prompt": "___ she call us?",
                "options": ["Does", "Is", "Will", "Has"],
                "answer": "Will",
                "explanation": "Вопрос Future Simple начинается с Will.",
            },

            {
                "order": 6,
                "prompt": "Will they come?",
                "options": [
                    "Yes, they do.",
                    "Yes, they will.",
                    "Yes, they are.",
                    "Yes, they'll.",
                ],
                "answer": "Yes, they will.",
                "explanation": "Краткий положительный ответ: Yes, they will.",
            },

            {
                "order": 7,
                "prompt": "The room is cold. I ___ close the window.",
                "options": [
                    "will",
                    "closed",
                    "am close",
                    "have closed tomorrow",
                ],
                "answer": "will",
                "explanation": "Решение принято прямо сейчас → will.",
            },

            {
                "order": 8,
                "prompt": "I promise I ___ tell anyone.",
                "options": [
                    "don't",
                    "won't",
                    "am not",
                    "didn't",
                ],
                "answer": "won't",
                "explanation": "Обещание в отрицательной форме → won't.",
            },

            {
                "order": 9,
                "prompt": "What ___ you do tomorrow?",
                "options": ["do", "will", "are", "did"],
                "answer": "will",
                "explanation": "What will you do?",
            },

            {
                "order": 10,
                "prompt": "Where ___ they stay?",
                "options": [
                    "will",
                    "do will",
                    "are will",
                    "did",
                ],
                "answer": "will",
                "explanation": "Where will they stay?",
            },

            {
                "order": 11,
                "prompt": "Who ___ help us?",
                "options": [
                    "does will",
                    "will",
                    "is",
                    "did",
                ],
                "answer": "will",
                "explanation": "Who как подлежащее: Who will help us?",
            },

            {
                "order": 12,
                "prompt": "I will call you when I ___ home.",
                "options": [
                    "will get",
                    "get",
                    "got",
                    "am get",
                ],
                "answer": "get",
                "explanation": "После when для будущего используется Present Simple.",
            },

            {
                "order": 13,
                "prompt": "If it ___, we will stay home.",
                "options": [
                    "will rain",
                    "rains",
                    "rained",
                    "raining",
                ],
                "answer": "rains",
                "explanation": "После if в условной части используется Present Simple.",
            },

            {
                "order": 14,
                "prompt": "She will probably ___ late.",
                "options": [
                    "arrives",
                    "arrive",
                    "arrived",
                    "arriving",
                ],
                "answer": "arrive",
                "explanation": "После will используется base form arrive.",
            },

            {
                "order": 15,
                "prompt": "Shall we ___?",
                "options": [
                    "start",
                    "started",
                    "starting",
                    "starts",
                ],
                "answer": "start",
                "explanation": "После shall также используется первая форма.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She will goes home.",
                    "She will go home.",
                    "She will to go home.",
                    "She will went home.",
                ],
                "answer": "She will go home.",
                "explanation": "После will используется первая форма go.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence with TO BE.",
                "options": [
                    "She will is busy.",
                    "She will be busy.",
                    "She will being busy.",
                    "She will was busy.",
                ],
                "answer": "She will be busy.",
                "explanation": "После will используется be.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence with HAVE.",
                "options": [
                    "She will has a meeting.",
                    "She will have a meeting.",
                    "She will having a meeting.",
                    "She will had a meeting.",
                ],
                "answer": "She will have a meeting.",
                "explanation": "После will используется первая форма have.",
            },

            {
                "order": 19,
                "prompt": "The phone is ringing. I ___ it.",
                "options": [
                    "will answer",
                    "answered tomorrow",
                    "am answer",
                    "will answered",
                ],
                "answer": "will answer",
                "explanation": "Спонтанное решение → will.",
            },

            {
                "order": 20,
                "prompt": "Choose the best prediction.",
                "options": [
                    "I think she will pass the exam.",
                    "I think she passes the exam tomorrow yesterday.",
                    "I think she will passed the exam.",
                    "I think she will to pass the exam.",
                ],
                "answer": "I think she will pass the exam.",
                "explanation": "Мнение о будущем → will + base verb.",
            },

            {
                "order": 21,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I will call you when I will arrive.",
                    "I will call you when I arrive.",
                    "I will call you when I arrived tomorrow.",
                    "I will call you when I arriving.",
                ],
                "answer": "I will call you when I arrive.",
                "explanation": "После when используется Present Simple.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct conditional sentence.",
                "options": [
                    "If it will rain, we will stay home.",
                    "If it rains, we will stay home.",
                    "If it raining, we stay will home.",
                    "If it rained tomorrow, we will stays home.",
                ],
                "answer": "If it rains, we will stay home.",
                "explanation": "После if → Present Simple; главная часть → will.",
            },

            {
                "order": 23,
                "prompt": "Which sentence is a spontaneous decision?",
                "options": [
                    "I am going to visit my parents this weekend.",
                    "The doorbell is ringing. I'll open the door.",
                    "I am meeting Anna tomorrow at six.",
                    "I bought the ticket yesterday.",
                ],
                "answer": "The doorbell is ringing. I'll open the door.",
                "explanation": "Решение принято в момент речи.",
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct pair.",
                "options": [
                    "Will she come? / No, she won't.",
                    "Does she will come? / No, she doesn't will.",
                    "Will she comes? / No, she willn't.",
                    "Is she will come? / No, she isn't.",
                ],
                "answer": "Will she come? / No, she won't.",
                "explanation": "Вопрос: Will + subject + verb; отрицательный ответ: won't.",
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
                "✅ A1 Lesson 36 seeded: Future Simple with WILL"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
