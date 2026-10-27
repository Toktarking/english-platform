from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 14: "
        "Present Simple special questions."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=14,
            defaults={
                "title": (
                    "Специальные вопросы "
                    "в Present Simple"
                ),
                "slug": "present-simple-special-questions",
                "theory_text": (
                    "Wh-questions in Present Simple."
                ),
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое специальный вопрос",
                "body": """Специальный вопрос начинается с вопросительного слова и просит конкретную информацию.

Например:

Where do you live?
— Где ты живёшь?

What does she do?
— Чем она занимается?

Why do they study English?
— Почему они изучают английский?

На такой вопрос нельзя нормально ответить только:

Yes.

или:

No.

Нужно дать конкретную информацию.""",
            },

            {
                "order": 2,
                "title": "Основные вопросительные слова",
                "body": """Основные вопросительные слова:

where — где / куда;

what — что / какой;

when — когда;

why — почему;

how — как;

who — кто;

which — который / какой из нескольких.

Примеры:

Where do you work?

What does she want?

When do they arrive?

Why does he study English?

How do you go to work?

Who do you know?

Which book do you want?""",
            },

            {
                "order": 3,
                "title": "HOW OFTEN, HOW MANY, HOW MUCH",
                "body": """Полезные конструкции:

HOW OFTEN = как часто

How often do you exercise?

How often does she call you?

HOW MANY = сколько с исчисляемыми существительными

How many books do you have?

How many students does she teach?

HOW MUCH = сколько с неисчисляемыми существительными

How much money do you need?

How much water does he drink?

Запомните:

many → исчисляемые;

much → неисчисляемые.""",
            },

            {
                "order": 4,
                "title": "Главная формула",
                "body": """С обычным смысловым глаголом используется формула:

Вопросительное слово
+
do / does
+
подлежащее
+
глагол?

Примеры:

Where do you live?

What does she want?

Why do they work here?

When does the shop open?

С DO:

I;
you;
we;
they;
множественное число.

С DOES:

he;
she;
it;
один человек;
один предмет.""",
            },

            {
                "order": 5,
                "title": "После DOES глагол без -S",
                "body": """После does основной глагол возвращается в начальную форму.

Сравните:

She works at a school.

Where does she work?

Неправильно:

Where does she works?

Правильно:

Where does she work?

Другие примеры:

He lives in Astana.

Where does he live?

She studies English.

What does she study?

The shop opens at nine.

When does the shop open?

He has a car.

What does he have?""",
            },

            {
                "order": 6,
                "title": "Порядок слов",
                "body": """Нельзя сохранять порядок обычного утверждения.

Утверждение:

You live in Astana.

Неправильно:

Where you live?

Правильно:

Where do you live?

С he/she/it:

She works at a school.

Неправильно:

Where she works?

Правильно:

Where does she work?

После вопросительного слова нужен do или does, если это обычный глагол.""",
            },

            {
                "order": 7,
                "title": "WHAT DO YOU DO?",
                "body": """Вопрос:

What do you do?

обычно означает:

Чем вы занимаетесь?

Кем вы работаете?

Ответы:

I am a teacher.

I work at a university.

I am an engineer.

Не путайте:

What do you do?
— Чем вы занимаетесь обычно?

What are you doing?
— Что вы делаете прямо сейчас?

Второй вопрос относится к Present Continuous.""",
            },

            {
                "order": 8,
                "title": "WHO как объект",
                "body": """Если who является объектом действия, do/does нужны.

Пример:

You know someone.

Вопрос:

Who do you know?

Здесь:

you — подлежащее;

who — объект.

Ещё примеры:

Who does she call?

Who do they visit?

Who does he help?

Формула остаётся обычной:

Who + do/does + subject + verb?""",
            },

            {
                "order": 9,
                "title": "WHO как подлежащее",
                "body": """Если who само выполняет действие, do/does обычно не нужны.

Someone works here.

Вопрос:

Who works here?

Не:

Who does work here?

Сравните:

Who calls you?
— Кто тебе звонит?

Who do you call?
— Кому ты звонишь?

В первом случае who выполняет действие.

Во втором действие выполняет you.""",
            },

            {
                "order": 10,
                "title": "WHAT как подлежащее",
                "body": """Такое же правило работает с what.

Если what само выполняет действие, do/does не нужны.

Something makes this noise.

Вопрос:

What makes this noise?

Не:

What does make this noise?

Сравните:

What causes this problem?
— Что вызывает проблему?

What do you buy?
— Что ты покупаешь?

В первом случае what — подлежащее.

Во втором подлежащее — you.""",
            },

            {
                "order": 11,
                "title": "Вопросы с предлогами",
                "body": """В обычном разговорном английском предлог часто остаётся в конце вопроса.

Примеры:

Who do you work with?

What do you think about?

Where does she come from?

Who does he speak to?

Более формально можно сказать:

With whom do you work?

To whom does he speak?

Но для уровня A1 проще и естественнее использовать:

Who do you work with?

Who does he speak to?""",
            },

            {
                "order": 12,
                "title": "Другие вопросы с HOW",
                "body": """HOW OLD:

How old are you?

How old is she?

Здесь используется to be, поэтому do/does не нужны.

HOW LONG:

How long do you work every day?

How long does the lesson last?

HOW FAR:

How far do you live from work?

HOW WELL:

How well do you speak English?

How well does she know him?""",
            },

            {
                "order": 13,
                "title": "WHAT / WHICH + существительное",
                "body": """Вопросительное слово может стоять вместе с существительным.

WHAT:

What language do you speak?

What time does the lesson start?

What books do they read?

What music does she like?

WHICH используется, когда выбор ограничен:

Which book do you prefer?

Which bus does she take?

Which answer is correct?

Также:

How many children do they have?

How many lessons does she teach?""",
            },

            {
                "order": 14,
                "title": "TO BE и специальные вопросы",
                "body": """Если в предложении есть am/is/are, do и does не используются.

Примеры:

Where are you?

Why is she tired?

What is his job?

Who are they?

Сравните:

Where is she?
— Где она?

Where does she work?
— Где она работает?

Неправильно:

Where does she be?

Where is she work?

Главный алгоритм:

1. Выберите вопросительное слово.
2. Определите подлежащее.
3. Если обычный глагол — выберите do/does.
4. После does верните глагол в начальную форму.

She works at a school.

→ Where does she work?""",
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
                "prompt": "___ do you work?",
                "options": [
                    "Where",
                    "Who",
                    "How many",
                    "Which one",
                ],
                "answer": "Where",
                "explanation": "Чтобы спросить о месте работы, используется Where.",
            },

            {
                "order": 2,
                "prompt": "Where ___ your brother live?",
                "options": ["do", "does", "is", "are"],
                "answer": "does",
                "explanation": "Your brother = he, поэтому используется does.",
            },

            {
                "order": 3,
                "prompt": "What ___ your parents do?",
                "options": ["does", "do", "are", "is"],
                "answer": "do",
                "explanation": "Your parents = they, поэтому используется do.",
            },

            {
                "order": 4,
                "prompt": "What does your sister ___?",
                "options": [
                    "teaches",
                    "teach",
                    "teaching",
                    "taught",
                ],
                "answer": "teach",
                "explanation": "После does основной глагол используется в начальной форме.",
            },

            {
                "order": 5,
                "prompt": "Why ___ he study English?",
                "options": ["do", "does", "is", "are"],
                "answer": "does",
                "explanation": "He → does.",
            },

            {
                "order": 6,
                "prompt": "When ___ the students arrive?",
                "options": ["does", "do", "are", "is"],
                "answer": "do",
                "explanation": "Students = they, поэтому do.",
            },

            {
                "order": 7,
                "prompt": "How often ___ she call you?",
                "options": ["do", "does", "is", "has"],
                "answer": "does",
                "explanation": "She → does, а основной глагол остаётся call.",
            },

            {
                "order": 8,
                "prompt": "How many books ___ you have?",
                "options": ["does", "do", "are", "is"],
                "answer": "do",
                "explanation": "You → do.",
            },

            {
                "order": 9,
                "prompt": "How much water ___ he drink?",
                "options": ["do", "does", "is", "has"],
                "answer": "does",
                "explanation": "He → does. Water неисчисляемое, поэтому how much.",
            },

            {
                "order": 10,
                "prompt": "Who ___ English at your school?",
                "options": [
                    "teach",
                    "teaches",
                    "does teach",
                    "teaching",
                ],
                "answer": "teaches",
                "explanation": "Who здесь само выполняет действие, поэтому do/does не нужны.",
            },

            {
                "order": 11,
                "prompt": "Who do you ___ with?",
                "options": [
                    "works",
                    "work",
                    "working",
                    "worked",
                ],
                "answer": "work",
                "explanation": "После do используется начальная форма work.",
            },

            {
                "order": 12,
                "prompt": "What time does the lesson ___?",
                "options": [
                    "begins",
                    "begin",
                    "beginning",
                    "began",
                ],
                "answer": "begin",
                "explanation": "После does основной глагол используется без -s.",
            },

            {
                "order": 13,
                "prompt": "Which bus ___ she take?",
                "options": ["do", "does", "is", "has"],
                "answer": "does",
                "explanation": "She → does.",
            },

            {
                "order": 14,
                "prompt": "Why are you tired?",
                "options": [
                    "Because I work a lot.",
                    "Yes, I am.",
                    "No, I don't.",
                    "At home.",
                ],
                "answer": "Because I work a lot.",
                "explanation": "Why спрашивает о причине, поэтому нужен конкретный ответ.",
            },

            {
                "order": 15,
                "prompt": "Where does he work?",
                "options": [
                    "Yes, he does.",
                    "He works at a hospital.",
                    "No, he doesn't.",
                    "Because he needs money.",
                ],
                "answer": "He works at a hospital.",
                "explanation": "Where спрашивает о месте, а не требует yes/no.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct question.",
                "options": [
                    "Where you live?",
                    "Where do you live?",
                    "Where are you live?",
                    "Where does you live?",
                ],
                "answer": "Where do you live?",
                "explanation": "С обычным глаголом и you используется Where do you live?",
            },

            {
                "order": 17,
                "prompt": "Choose the correct question.",
                "options": [
                    "Where does she works?",
                    "Where she works?",
                    "Where does she work?",
                    "Where is she work?",
                ],
                "answer": "Where does she work?",
                "explanation": "После does глагол используется в начальной форме work.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct question.",
                "options": [
                    "What do he do?",
                    "What does he does?",
                    "What does he do?",
                    "What is he do?",
                ],
                "answer": "What does he do?",
                "explanation": "He → does, а основной глагол остаётся do.",
            },

            {
                "order": 19,
                "prompt": "Choose the correct question.",
                "options": [
                    "Why does they study English?",
                    "Why do they study English?",
                    "Why are they study English?",
                    "Why do they studies English?",
                ],
                "answer": "Why do they study English?",
                "explanation": "They → do + базовая форма study.",
            },

            {
                "order": 20,
                "prompt": "Who ___ you every morning?",
                "options": [
                    "calls",
                    "does call",
                    "do call",
                    "call",
                ],
                "answer": "calls",
                "explanation": "Who является подлежащим и выполняет действие: Who calls you?",
            },

            {
                "order": 21,
                "prompt": "Who do you ___ every morning?",
                "options": [
                    "calls",
                    "call",
                    "calling",
                    "does call",
                ],
                "answer": "call",
                "explanation": "Здесь подлежащее — you, а who является объектом.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct question about money.",
                "options": [
                    "How many money do you need?",
                    "How much money do you need?",
                    "How much money does you need?",
                    "How many money does you need?",
                ],
                "answer": "How much money do you need?",
                "explanation": "Money — неисчисляемое существительное, поэтому how much.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct question.",
                "options": [
                    "Where does she be?",
                    "Where is she?",
                    "Where does she is?",
                    "Where she is?",
                ],
                "answer": "Where is she?",
                "explanation": "С глаголом to be do/does не используются.",
            },

            {
                "order": 24,
                "prompt": (
                    "She works at a school. "
                    "Choose the question asking about the place."
                ),
                "options": [
                    "What does she work?",
                    "Where does she work?",
                    "Where does she works?",
                    "Where is she work?",
                ],
                "answer": "Where does she work?",
                "explanation": "Спрашиваем о месте: Where + does + she + work?",
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
                "✅ A1 Lesson 14 seeded: "
                "Специальные вопросы в Present Simple"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
