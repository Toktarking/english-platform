from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 52: "
        "Types of Questions."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=52,
            defaults={
                "title": "Типы вопросов в английском языке",
                "slug": "types-of-questions",
                "theory_text": (
                    "General, special, alternative, subject, "
                    "tag and indirect questions."
                ),
                "estimated_minutes": 50,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Основные типы вопросов",
                "body": """В английском языке есть несколько основных типов вопросов:

1. Общий вопрос.

2. Специальный вопрос.

3. Альтернативный вопрос.

4. Вопрос к подлежащему.

5. Разделительный вопрос.

6. Косвенный вопрос.

Главное — сначала понять, какую информацию мы хотим получить, а затем выбрать правильную структуру.""",
            },

            {
                "order": 2,
                "title": "Общий вопрос",
                "body": """Общий вопрос требует ответа Yes или No.

Примеры:

Are you tired?

Do you work here?

Did she call?

Have they arrived?

Will he come?

Can you swim?

Структура зависит от глагола и времени.

С TO BE:

Are you ready?

Was she at home?

Со смысловым глаголом:

Do you work?

Did she call?""",
            },

            {
                "order": 3,
                "title": "DO, DOES и DID",
                "body": """Present Simple:

Do/Does + subject + V1?

Do you work here?

Does she speak English?

После DOES используется первая форма:

Does she work?

Не:

Does she works?

Past Simple:

Did + subject + V1?

Did she go?

Did he write?

Не:

Did she went?

Did he wrote?""",
            },

            {
                "order": 4,
                "title": "Вопросы в других временах",
                "body": """Present Continuous:

Am/Is/Are + subject + verb-ing?

Are you working?

Past Continuous:

Was/Were + subject + verb-ing?

Were they waiting?

Present Perfect:

Have/Has + subject + V3?

Have you finished?

Future Simple:

Will + subject + V1?

Will she come?

Modal:

Can/Should/Must + subject + V1?

Can you swim?

Should we leave?""",
            },

            {
                "order": 5,
                "title": "Специальный вопрос",
                "body": """Специальный вопрос начинается с вопросительного слова и требует развёрнутого ответа.

Частые слова:

what

where

when

why

who

whose

which

how

Общая формула:

Question word + auxiliary + subject + main verb?

Примеры:

Where do you live?

What does she want?

When did they arrive?

Why are you laughing?""",
            },

            {
                "order": 6,
                "title": "WHAT, WHERE, WHEN, WHY",
                "body": """WHAT:

What do you want?

What time is it?

WHERE:

Where do you live?

Where did they go?

WHEN:

When does the lesson start?

When will they come?

WHY:

Why are you tired?

Why did she leave?

На WHY часто отвечают с BECAUSE:

Why are you tired?

Because I worked late.""",
            },

            {
                "order": 7,
                "title": "WHO, WHOSE и WHICH",
                "body": """WHO:

кто? кого? кому?

Who is she?

Who did you call?

WHOSE:

чей?

Whose book is this?

Whose phone is ringing?

WHICH:

какой из ограниченного выбора?

Which dress do you prefer, the red one or the blue one?

WHAT используется при широком выборе:

What music do you like?

WHICH — когда варианты ограничены.""",
            },

            {
                "order": 8,
                "title": "HOW и его сочетания",
                "body": """HOW означает:

как?

How are you?

How does it work?

Частые сочетания:

how old — сколько лет;

how much — сколько с неисчисляемыми;

how many — сколько с исчисляемыми;

how often — как часто;

how long — как долго;

how far — как далеко;

how fast — как быстро.

Примеры:

How much money do you need?

How many students are there?

How often do you exercise?""",
            },

            {
                "order": 9,
                "title": "Альтернативный вопрос",
                "body": """Альтернативный вопрос предлагает выбор.

Используется OR.

Примеры:

Do you want tea or coffee?

Is she at home or at work?

Will you go by bus or by train?

Did he call or send a message?

На такой вопрос обычно нельзя ответить только Yes или No.

Ответ:

Tea, please.

By train.

She is at work.""",
            },

            {
                "order": 10,
                "title": "Вопрос к подлежащему",
                "body": """Вопрос к подлежащему спрашивает:

кто выполняет действие?

Примеры:

Who called you?

Who lives here?

Who broke the window?

What happened?

Главное правило:

обычно НЕ используются do, does, did.

Правильно:

Who called you?

Who works here?

Неправильно:

Who did call you?

Who does work here?""",
            },

            {
                "order": 11,
                "title": "Вопрос к дополнению",
                "body": """Если спрашиваем не исполнителя, а объект действия, используется обычная вопросительная структура.

Сравните:

Who called you?

Кто позвонил тебе?

WHO = подлежащее.

Who did you call?

Кому позвонил ты?

YOU = подлежащее, WHO = объект.

Ещё пример:

Who saw Anna?

Who did Anna see?""",
            },

            {
                "order": 12,
                "title": "Разделительный вопрос",
                "body": """Разделительный вопрос состоит из:

утверждения;

короткого вопроса в конце.

Пример:

You are tired, aren't you?

You work here, don't you?

She can swim, can't she?

Эта конструкция используется, когда говорящий просит подтверждение.

Основное правило:

положительное предложение → отрицательный хвост.

Отрицательное предложение → положительный хвост.""",
            },

            {
                "order": 13,
                "title": "Косвенный вопрос",
                "body": """Косвенный вопрос является частью более длинной и часто более вежливой фразы.

Примеры:

Can you tell me where the bank is?

Do you know when the lesson starts?

Could you explain how this works?

Главное правило:

используется ПРЯМОЙ порядок слов.

Прямой вопрос:

Where is the bank?

Косвенный:

Can you tell me where the bank is?

Не:

Can you tell me where is the bank?""",
            },

            {
                "order": 14,
                "title": "Как построить вопрос",
                "body": """Шаг 1.

Определите глагол:

TO BE;

смысловой;

модальный;

вспомогательный.

Шаг 2.

Определите время.

Шаг 3.

Выберите вспомогательный глагол:

do / does / did;

have / has;

will;

can;

is / are / was / were.

Шаг 4.

Если нужен question word — поставьте его в начало.

Шаг 5.

Проверьте, спрашиваете ли вы подлежащее.

Если да, do/does/did обычно не нужны.

Шаг 6.

Если вопрос косвенный — используйте прямой порядок слов.""",
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
                "prompt": "___ she at home?",
                "options": [
                    "Does",
                    "Is",
                    "Do",
                    "Did",
                ],
                "answer": "Is",
                "explanation": (
                    "С TO BE вспомогательный do не нужен."
                ),
            },

            {
                "order": 2,
                "prompt": "Where ___ they live?",
                "options": [
                    "do",
                    "are",
                    "does",
                    "did live now",
                ],
                "answer": "do",
                "explanation": (
                    "Present Simple, they → do."
                ),
            },

            {
                "order": 3,
                "prompt": "What ___ he want?",
                "options": [
                    "do",
                    "does",
                    "is",
                    "did yesterday only",
                ],
                "answer": "does",
                "explanation": (
                    "Present Simple, he → does + V1."
                ),
            },

            {
                "order": 4,
                "prompt": "Why ___ she leave yesterday?",
                "options": [
                    "does",
                    "did",
                    "is",
                    "has every day",
                ],
                "answer": "did",
                "explanation": (
                    "Yesterday → Past Simple → did."
                ),
            },

            {
                "order": 5,
                "prompt": "___ you finished the work?",
                "options": [
                    "Do",
                    "Have",
                    "Are",
                    "Did finish already",
                ],
                "answer": "Have",
                "explanation": (
                    "Present Perfect: Have + subject + V3."
                ),
            },

            {
                "order": 6,
                "prompt": "When ___ they arrive?",
                "options": [
                    "will",
                    "do tomorrow",
                    "are every day",
                    "did future",
                ],
                "answer": "will",
                "explanation": (
                    "Future Simple question: will + subject + V1."
                ),
            },

            {
                "order": 7,
                "prompt": "___ you swim?",
                "options": [
                    "Can",
                    "Do can",
                    "Are can",
                    "Can to",
                ],
                "answer": "Can",
                "explanation": (
                    "Modal question: Can + subject + V1?"
                ),
            },

            {
                "order": 8,
                "prompt": "Who ___ the window?",
                "options": [
                    "did break",
                    "broke",
                    "break did",
                    "was break",
                ],
                "answer": "broke",
                "explanation": (
                    "Вопрос к подлежащему: did не нужен."
                ),
            },

            {
                "order": 9,
                "prompt": "Who did she ___?",
                "options": [
                    "called",
                    "call",
                    "calls",
                    "calling",
                ],
                "answer": "call",
                "explanation": (
                    "После did используется V1."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "Do you want the red one ___ the blue one?"
                ),
                "options": [
                    "and",
                    "or",
                    "because",
                    "so",
                ],
                "answer": "or",
                "explanation": (
                    "Альтернативный вопрос использует or."
                ),
            },

            {
                "order": 11,
                "prompt": "___ book is this?",
                "options": [
                    "Who",
                    "Whose",
                    "Which person",
                    "How",
                ],
                "answer": "Whose",
                "explanation": (
                    "Whose = чей?"
                ),
            },

            {
                "order": 12,
                "prompt": "___ do you exercise?",
                "options": [
                    "How often",
                    "How much students",
                    "How many time",
                    "What often",
                ],
                "answer": "How often",
                "explanation": (
                    "How often = как часто."
                ),
            },

            {
                "order": 13,
                "prompt": "How ___ does the journey take?",
                "options": [
                    "much",
                    "many",
                    "long",
                    "far time",
                ],
                "answer": "long",
                "explanation": (
                    "How long = как долго."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "Can you tell me when the lesson ___?"
                ),
                "options": [
                    "does start",
                    "starts",
                    "start does",
                    "is start",
                ],
                "answer": "starts",
                "explanation": (
                    "В косвенном вопросе прямой порядок слов."
                ),
            },

            {
                "order": 15,
                "prompt": "Do you know if she ___?",
                "options": [
                    "has arrived",
                    "has she arrived",
                    "did arrive she",
                    "arrived has",
                ],
                "answer": "has arrived",
                "explanation": (
                    "Indirect Yes/No question: if + direct word order."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct Present Simple question.",
                "options": [
                    "Where she works?",
                    "Where does she work?",
                    "Where does she works?",
                    "Where she does work?",
                ],
                "answer": "Where does she work?",
                "explanation": (
                    "Does + subject + V1."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct Past Simple question.",
                "options": [
                    "When did he arrived?",
                    "When did he arrive?",
                    "When he did arrive?",
                    "When does he arrived?",
                ],
                "answer": "When did he arrive?",
                "explanation": (
                    "После did используется V1."
                ),
            },

            {
                "order": 18,
                "prompt": (
                    "Which sentence is a subject question?"
                ),
                "options": [
                    "Who called Anna?",
                    "Who did Anna call?",
                    "Who does Anna call?",
                    "Who is Anna calling?",
                ],
                "answer": "Who called Anna?",
                "explanation": (
                    "WHO выполняет действие → subject question."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "Which sentence is an object question?"
                ),
                "options": [
                    "Who called Anna?",
                    "Who did Anna call?",
                    "Who arrived?",
                    "What happened?",
                ],
                "answer": "Who did Anna call?",
                "explanation": (
                    "Anna — подлежащее, WHO — объект."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the correct indirect question.",
                "options": [
                    "Can you tell me where is the bank?",
                    "Can you tell me where the bank is?",
                    "Can you tell me where does the bank is?",
                    "Can you tell me where the bank does be?",
                ],
                "answer": (
                    "Can you tell me where the bank is?"
                ),
                "explanation": (
                    "После introductory phrase используется прямой порядок."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct HOW MUCH / HOW MANY pair.",
                "options": [
                    (
                        "How much money? / "
                        "How many students?"
                    ),
                    (
                        "How many money? / "
                        "How much students?"
                    ),
                    (
                        "How much students? / "
                        "How many water?"
                    ),
                    (
                        "How many time? / "
                        "How much books?"
                    ),
                ],
                "answer": (
                    "How much money? / "
                    "How many students?"
                ),
                "explanation": (
                    "Much → uncountable; many → countable plural."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct WHAT / WHICH pair.",
                "options": [
                    (
                        "What music do you like? / "
                        "Which dress do you prefer, "
                        "the red one or the blue one?"
                    ),
                    (
                        "Which music in the world do you like? / "
                        "What dress, red or blue?"
                    ),
                    (
                        "What of two dresses do you prefer? / "
                        "Which music generally do you like?"
                    ),
                    (
                        "What one red or blue? / "
                        "Which all music do you like?"
                    ),
                ],
                "answer": (
                    "What music do you like? / "
                    "Which dress do you prefer, "
                    "the red one or the blue one?"
                ),
                "explanation": (
                    "What = широкий выбор; Which = ограниченный выбор."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct tag question.",
                "options": [
                    "You are tired, aren't you?",
                    "You are tired, don't you?",
                    "You are tired, are you not tired?",
                    "You are tired, isn't she?",
                ],
                "answer": "You are tired, aren't you?",
                "explanation": (
                    "Положительное предложение → отрицательный tag."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "Do you work here? / "
                        "Where do you work? / "
                        "Who works here? / "
                        "Can you tell me where you work?"
                    ),
                    (
                        "Do you work here? / "
                        "Where you work? / "
                        "Who does work here? / "
                        "Can you tell me where do you work?"
                    ),
                    (
                        "Are you work here? / "
                        "Where does you work? / "
                        "Who do works here? / "
                        "Can you tell me where are you work?"
                    ),
                    (
                        "Does you work here? / "
                        "Where did you works? / "
                        "Who did works here? / "
                        "Can you tell me where does you work?"
                    ),
                ],
                "answer": (
                    "Do you work here? / "
                    "Where do you work? / "
                    "Who works here? / "
                    "Can you tell me where you work?"
                ),
                "explanation": (
                    "General → Do...?; special → Where do...?; "
                    "subject question → no do; indirect → direct order."
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
                "✅ A1 Lesson 52 seeded: Types of Questions"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
