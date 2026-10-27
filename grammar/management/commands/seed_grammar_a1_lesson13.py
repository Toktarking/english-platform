from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 13: "
        "Present Simple questions with DO and DOES."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=13,
            defaults={
                "title": (
                    "Вопросы в Present Simple: "
                    "DO и DOES"
                ),
                "slug": "present-simple-questions",
                "theory_text": (
                    "Present Simple questions "
                    "with do and does."
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
                "title": "Как задать вопрос в Present Simple",
                "body": """С обычными глаголами вопросы в Present Simple образуются с помощью:

do;

does.

Сравните:

You work here.

Do you work here?

She lives in Astana.

Does she live in Astana?

Главная формула:

Do / Does + подлежащее + глагол?

Важно:

основной глагол после do/does используется в начальной форме.""",
            },

            {
                "order": 2,
                "title": "Когда используется DO",
                "body": """Do используется с:

I;

you;

we;

they;

подлежащими во множественном числе.

Примеры:

Do I need this?

Do you work here?

Do we have enough time?

Do they speak English?

Do the students understand the task?

Запомните:

I / you / we / they → DO.""",
            },

            {
                "order": 3,
                "title": "Вопросы с I, YOU, WE, THEY",
                "body": """Примеры с I:

Do I know you?

Do I need a ticket?

Do I have to wait?

С YOU:

Do you live in Kazakhstan?

Do you like coffee?

Do you have children?

С WE:

Do we start now?

Do we have a lesson today?

С THEY:

Do they work together?

Do they study English?

Do they have a car?""",
            },

            {
                "order": 4,
                "title": "Когда используется DOES",
                "body": """Does используется с:

he;

she;

it;

одним человеком;

одним предметом;

одним животным.

Примеры:

Does he work here?

Does she speak English?

Does it work?

Does Marat live in Astana?

Does the phone charge quickly?

Запомните:

he / she / it → DOES.""",
            },

            {
                "order": 5,
                "title": "Вопросы с HE, SHE и IT",
                "body": """С HE:

Does he work at a university?

Does he drive?

Does he know the answer?

Does he have a car?

С SHE:

Does she speak English?

Does she live in Karaganda?

Does she like coffee?

Does she have children?

С IT:

Does it work?

Does it open at nine?

Does it cost much?

Does it need electricity?""",
            },

            {
                "order": 6,
                "title": "После DOES глагол без -S",
                "body": """Это главное правило урока.

После does основной глагол используется в начальной форме.

Сравните:

She works here.

Does she work here?

Неправильно:

Does she works here?

Правильно:

Does she work here?

Окончание -s уже находится в слове does.

То же самое:

He lives → Does he live?

She watches → Does she watch?

He studies → Does he study?

She has → Does she have?""",
            },

            {
                "order": 7,
                "title": "DO / DOES с разными формами глагола",
                "body": """Посмотрите, как глагол возвращается в начальную форму.

Утверждение:

He lives in Astana.

Вопрос:

Does he live in Astana?

Утверждение:

She watches television.

Вопрос:

Does she watch television?

Утверждение:

He studies English.

Вопрос:

Does he study English?

Утверждение:

She has a car.

Вопрос:

Does she have a car?

После does всегда:

live;
watch;
study;
have.""",
            },

            {
                "order": 8,
                "title": "Общие вопросы и краткие ответы",
                "body": """Общий вопрос — это вопрос, на который можно ответить yes или no.

С DO:

Do you work here?

Yes, I do.

No, I don't.

Do they speak English?

Yes, they do.

No, they don't.

С DOES:

Does she work here?

Yes, she does.

No, she doesn't.

Does he drive?

Yes, he does.

No, he doesn't.""",
            },

            {
                "order": 9,
                "title": "Почему в ответе нет основного глагола",
                "body": """В кратком ответе основной глагол обычно не повторяется.

Вопрос:

Do you speak English?

Краткий ответ:

Yes, I do.

Вопрос:

Does she work here?

Краткий ответ:

Yes, she does.

Не нужно говорить:

Yes, I speak English.

Такой полный ответ возможен, но краткий ответ строится через do/does.

Важно:

Do you work?

Yes, I do.

Не:

Yes, I am.""",
            },

            {
                "order": 10,
                "title": "Вопросы с HAVE и LIKE",
                "body": """Have в Present Simple ведёт себя как обычный глагол.

Примеры:

Do you have a car?

Does she have children?

Do they have enough money?

Does he have a job?

Важно:

Does she have...?

Не:

Does she has...?

С LIKE:

Do you like coffee?

Does he like football?

Does she like this book?

Do they like their teacher?

Краткие ответы:

Yes, I do.

No, I don't.

Yes, she does.

No, she doesn't.""",
            },

            {
                "order": 11,
                "title": "Наречия частотности в вопросах",
                "body": """Наречие частотности обычно ставится после подлежащего и перед основным глаголом.

Примеры:

Do you often read?

Does she usually work at home?

Do they always come on time?

Does he sometimes drive to work?

Слово never редко используется в нейтральных вопросах.

Вместо него часто используется ever:

Do you ever travel abroad?

Ever означает:

когда-нибудь.""",
            },

            {
                "order": 12,
                "title": "Существительное как подлежащее",
                "body": """Если подлежащее — существительное, мысленно замените его местоимением.

Your brother = he:

Does your brother work here?

Your parents = they:

Do your parents live here?

The phone = it:

Does the phone work?

The phones = they:

Do the phones work?

Это помогает быстро выбрать do или does.""",
            },

            {
                "order": 13,
                "title": "TO BE или DO / DOES",
                "body": """Если в предложении используется am/is/are, do и does не нужны.

Неправильно:

Does she is a teacher?

Правильно:

Is she a teacher?

Но если есть обычный смысловой глагол:

Неправильно:

Is she work here?

Правильно:

Does she work here?

Сравните:

Is he a doctor?

Does he work at a hospital?

Doctor — профессия, поэтому to be.

Work — действие, поэтому does.""",
            },

            {
                "order": 14,
                "title": "Как быстро построить вопрос",
                "body": """Шаг 1. Найдите подлежащее.

My sister works at a school.

Подлежащее:

my sister.

My sister = she.

Шаг 2. Выберите DOES.

Does my sister...

Шаг 3. Верните глагол в начальную форму.

works → work

Итог:

Does my sister work at a school?

С множественным числом:

My parents live in Astana.

My parents = they.

Используем do:

Do my parents live in Astana?

Главное правило:

I / you / we / they → DO

he / she / it → DOES

После do/does → базовая форма глагола.""",
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
                "prompt": "___ you speak English?",
                "options": ["Does", "Do", "Are", "Is"],
                "answer": "Do",
                "explanation": "С you используется Do.",
            },

            {
                "order": 2,
                "prompt": "___ your wife speak English?",
                "options": ["Do", "Does", "Is", "Are"],
                "answer": "Does",
                "explanation": "Your wife = she, поэтому Does.",
            },

            {
                "order": 3,
                "prompt": "Do they ___ in Karaganda?",
                "options": ["lives", "live", "living", "lived"],
                "answer": "live",
                "explanation": "После do используется начальная форма live.",
            },

            {
                "order": 4,
                "prompt": "Does he ___ in Karaganda?",
                "options": ["lives", "live", "living", "lived"],
                "answer": "live",
                "explanation": "После does окончание -s у основного глагола исчезает.",
            },

            {
                "order": 5,
                "prompt": "___ your parents work?",
                "options": ["Does", "Do", "Are", "Is"],
                "answer": "Do",
                "explanation": "Your parents = they, поэтому Do.",
            },

            {
                "order": 6,
                "prompt": "___ your father work?",
                "options": ["Do", "Does", "Is", "Are"],
                "answer": "Does",
                "explanation": "Your father = he, поэтому Does.",
            },

            {
                "order": 7,
                "prompt": "Does the lesson ___ at nine?",
                "options": ["starts", "start", "starting", "started"],
                "answer": "start",
                "explanation": "После does используется базовая форма start.",
            },

            {
                "order": 8,
                "prompt": "Do the lessons ___ at nine?",
                "options": ["starts", "start", "starting", "started"],
                "answer": "start",
                "explanation": "После do используется start.",
            },

            {
                "order": 9,
                "prompt": "Does she ___ television every day?",
                "options": ["watches", "watch", "watching", "watched"],
                "answer": "watch",
                "explanation": "Watches → Does she watch...?",
            },

            {
                "order": 10,
                "prompt": "Do they ___ television every day?",
                "options": ["watches", "watch", "watching", "watched"],
                "answer": "watch",
                "explanation": "They → do + watch.",
            },

            {
                "order": 11,
                "prompt": "Does your brother ___ English?",
                "options": ["studies", "study", "studying", "studied"],
                "answer": "study",
                "explanation": "Studies возвращается к базовой форме study.",
            },

            {
                "order": 12,
                "prompt": "Do you ___ a car?",
                "options": ["has", "have", "having", "had"],
                "answer": "have",
                "explanation": "После do используется have.",
            },

            {
                "order": 13,
                "prompt": "Does she ___ a car?",
                "options": ["has", "have", "having", "had"],
                "answer": "have",
                "explanation": "Правильно: Does she have...?, не Does she has...?",
            },

            {
                "order": 14,
                "prompt": "Do the students understand the task?",
                "options": [
                    "Yes, they do.",
                    "Yes, they are.",
                    "Yes, they does.",
                    "Yes, they understand do.",
                ],
                "answer": "Yes, they do.",
                "explanation": "Вопрос с do требует краткий ответ Yes, they do.",
            },

            {
                "order": 15,
                "prompt": "Does Marat work here?",
                "options": [
                    "No, he don't.",
                    "No, he isn't.",
                    "No, he doesn't.",
                    "No, he not.",
                ],
                "answer": "No, he doesn't.",
                "explanation": "Marat = he, поэтому краткий ответ: No, he doesn't.",
            },

            {
                "order": 16,
                "prompt": "Does she ___ coffee?",
                "options": ["likes", "like", "liking", "liked"],
                "answer": "like",
                "explanation": "После does используется базовая форма like.",
            },

            {
                "order": 17,
                "prompt": "___ the phone work?",
                "options": ["Do", "Does", "Is", "Are"],
                "answer": "Does",
                "explanation": "The phone = it, поэтому Does.",
            },

            {
                "order": 18,
                "prompt": "___ the phones work?",
                "options": ["Does", "Do", "Is", "Are"],
                "answer": "Do",
                "explanation": "The phones = they, поэтому Do.",
            },

            {
                "order": 19,
                "prompt": "Does he usually ___ at home?",
                "options": ["works", "work", "working", "worked"],
                "answer": "work",
                "explanation": "Usually стоит перед основным глаголом; после does используется work.",
            },

            {
                "order": 20,
                "prompt": "Do you ___ travel abroad?",
                "options": ["never", "ever", "always not", "does"],
                "answer": "ever",
                "explanation": "В нейтральном вопросе «когда-нибудь» обычно передаётся словом ever.",
            },

            {
                "order": 21,
                "prompt": "Choose the correct question.",
                "options": [
                    "Does she works here?",
                    "Do she work here?",
                    "Does she work here?",
                    "Is she work here?",
                ],
                "answer": "Does she work here?",
                "explanation": "She → does, а основной глагол используется без -s.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct question.",
                "options": [
                    "Does they study English?",
                    "Do they study English?",
                    "Are they study English?",
                    "Do they studies English?",
                ],
                "answer": "Do they study English?",
                "explanation": "They → do + базовая форма study.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct question.",
                "options": [
                    "Does she is a teacher?",
                    "Do she is a teacher?",
                    "Is she a teacher?",
                    "Does she be a teacher?",
                ],
                "answer": "Is she a teacher?",
                "explanation": "С глаголом to be do/does не используются.",
            },

            {
                "order": 24,
                "prompt": "My sister works at a school. Choose the correct question.",
                "options": [
                    "Does my sister works at a school?",
                    "Do my sister work at a school?",
                    "Does my sister work at a school?",
                    "Is my sister work at a school?",
                ],
                "answer": "Does my sister work at a school?",
                "explanation": "My sister = she → does, а works возвращается к work.",
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
                "✅ A1 Lesson 13 seeded: "
                "Вопросы в Present Simple — DO / DOES"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
