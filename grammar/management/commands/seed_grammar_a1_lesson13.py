from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 13: Present Simple questions."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=13,

                defaults={
                    "title":
                        "Вопросы в Present Simple: "
                        "DO и DOES",

                    "slug":
                        "present-simple-questions",

                    "theory_text":
                        "Present Simple questions "
                        "with do and does.",

                    "estimated_minutes":
                        16,

                    "pass_score":
                        70,

                    "xp_reward":
                        100,

                    "is_published":
                        True,
                },
            )
        )


        # ================================================
        # 9 MICRO-RULES
        # ================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Как задать вопрос в Present Simple?",

                "body":
                    """С обычными глаголами вопрос строится через DO или DOES.

Утверждение:

You work here.

Вопрос:

Do you work here?

Утверждение:

She works here.

Вопрос:

Does she work here?

Главная формула:

DO / DOES
+ subject
+ base verb?

После DO и DOES основной глагол используется в базовой форме.""",
            },


            {
                "order": 2,

                "title":
                    "I, YOU, WE, THEY → DO",

                "body":
                    """С I, YOU, WE, THEY используется DO.

Do I need this?

Do you work here?

Do we have enough time?

Do they speak English?

То же правило работает с множественным числом:

Do the students understand?

Do your parents live here?

Главная схема:

I / you / we / they
→ DO.""",
            },


            {
                "order": 3,

                "title":
                    "HE, SHE, IT → DOES",

                "body":
                    """С HE, SHE, IT используется DOES.

Does he work here?

Does she speak English?

Does it work?

То же правило с одним человеком или предметом:

Does Marat live in Astana?

Does your sister drive?

Does the phone work?

Главная схема:

he / she / it
→ DOES.""",
            },


            {
                "order": 4,

                "title":
                    "После DOES глагол без -S",

                "body":
                    """Это главное правило урока.

Утверждение:

She works here.

Вопрос:

Does she work here?

Не:

Does she works here?

Окончание третьего лица уже находится в DOES.

То же самое:

He lives
→ Does he live?

She watches
→ Does she watch?

He studies
→ Does he study?

После DOES всегда базовая форма.""",
            },


            {
                "order": 5,

                "title":
                    "HAS → DOES ... HAVE?",

                "body":
                    """HAVE ведёт себя как обычный глагол.

Утверждение:

She has a car.

Вопрос:

Does she have a car?

Не:

Does she has a car?

Ещё примеры:

Do you have children?

Does he have a job?

Do they have enough money?

Запомни:

HAS
→ DOES ... HAVE?""",
            },


            {
                "order": 6,

                "title":
                    "Краткие ответы",

                "body":
                    """На общий вопрос можно ответить YES или NO.

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

No, he doesn't.

В кратком ответе основной глагол обычно не повторяется.""",
            },


            {
                "order": 7,

                "title":
                    "DO / DOES или IS / ARE?",

                "body":
                    """Если есть TO BE, DO и DOES не нужны.

Профессия:

She is a teacher.

Вопрос:

Is she a teacher?

Не:

Does she is a teacher?

Но с обычным действием:

She works here.

Вопрос:

Does she work here?

Сравни:

Is he a doctor?

Does he work at a hospital?

Doctor — описание через TO BE.

Work — действие через DOES.""",
            },


            {
                "order": 8,

                "title":
                    "Often, usually и ever в вопросах",

                "body":
                    """Наречие частотности обычно ставится после подлежащего и перед основным глаголом.

Do you often read?

Does she usually work at home?

Do they always come on time?

Does he sometimes drive?

Для значения «когда-нибудь» часто используется EVER:

Do you ever travel abroad?

Does she ever cook at home?

Схема:

DO / DOES
+ subject
+ frequency word
+ base verb?""",
            },


            {
                "order": 9,

                "title":
                    "Как быстро построить вопрос",

                "body":
                    """Шаг 1.

Найди подлежащее:

My sister works here.

My sister = SHE.

Шаг 2.

Выбери DOES:

Does my sister...

Шаг 3.

Верни глагол в базовую форму:

works → work

Итог:

Does my sister work here?

Другой пример:

My parents live in Astana.

My parents = THEY.

Используем DO:

Do my parents live in Astana?

Главная схема:

I / you / we / they
→ DO

he / she / it
→ DOES

после DO / DOES
→ base verb.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects
                .update_or_create(
                    lesson=lesson,
                    order=data["order"],

                    defaults={
                        "title":
                            data["title"],

                        "body":
                            data["body"],
                    },
                )
            )

            section_objects[
                data["order"]
            ] = section


        # ================================================
        # 20 TRAINING EXERCISES
        # ================================================

        training = [

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "___ you speak English?",

                "options": [
                    "Does",
                    "Do",
                    "Are",
                    "Is",
                ],

                "answer":
                    "Do",

                "explanation":
                    "YOU → DO.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "___ she work here?",

                "options": [
                    "Do",
                    "Does",
                    "Is",
                    "Are",
                ],

                "answer":
                    "Does",

                "explanation":
                    "SHE → DOES.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "___ they live in Karaganda?",

                "options": [],

                "answer":
                    "Do",

                "explanation":
                    "THEY → DO.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "___ your parents work here?",

                "options": [
                    "Does",
                    "Do",
                    "Is",
                    "Are",
                ],

                "answer":
                    "Do",

                "explanation":
                    "Your parents = THEY → DO.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "___ your father drive?",

                "options": [],

                "answer":
                    "Does",

                "explanation":
                    "Your father = HE → DOES.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "___ the phone work?",

                "options": [
                    "Do",
                    "Does",
                    "Is",
                    "Are",
                ],

                "answer":
                    "Does",

                "explanation":
                    "The phone = IT → DOES.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Does he ___ in Astana?",

                "options": [
                    "lives",
                    "live",
                    "living",
                    "is live",
                ],

                "answer":
                    "live",

                "explanation":
                    "После DOES используется базовая форма LIVE.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Does she ___ TV every evening?",

                "options": [
                    "watches",
                    "watch",
                    "watching",
                    "is watch",
                ],

                "answer":
                    "watch",

                "explanation":
                    "WATCHES → DOES SHE WATCH?",
            },


            {
                "order": 9,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Does your brother ___ English?",

                "options": [
                    "studies",
                    "study",
                    "studys",
                    "studying",
                ],

                "answer":
                    "study",

                "explanation":
                    "STUDIES возвращается к STUDY.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Does she ___ a car?",

                "options": [
                    "has",
                    "have",
                    "haves",
                    "having",
                ],

                "answer":
                    "have",

                "explanation":
                    "HAS → DOES ... HAVE?",
            },


            {
                "order": 11,
                "section": 5,
                "type": "build",

                "prompt":
                    "Собери правильный вопрос.",

                "options": [
                    "Does",
                    "he",
                    "have",
                    "a",
                    "job",
                ],

                "answer":
                    "Does he have a job",

                "explanation":
                    "После DOES используется HAVE.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Do you work here?",

                "options": [
                    "Yes, I do.",
                    "Yes, I am.",
                    "Yes, I does.",
                    "Yes, I work do.",
                ],

                "answer":
                    "Yes, I do.",

                "explanation":
                    "Вопрос с DO → краткий ответ YES, I DO.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Does Marat live here?",

                "options": [
                    "No, he don't.",
                    "No, he isn't.",
                    "No, he doesn't.",
                    "No, he not.",
                ],

                "answer":
                    "No, he doesn't.",

                "explanation":
                    "Marat = HE → NO, HE DOESN'T.",
            },


            {
                "order": 14,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Do the students understand?",

                "options": [
                    "Yes, they do.",
                    "Yes, they are.",
                    "Yes, they does.",
                    "Yes, them do.",
                ],

                "answer":
                    "Yes, they do.",

                "explanation":
                    "THE STUDENTS = THEY → YES, THEY DO.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Does she is a teacher?",
                    "Do she is a teacher?",
                    "Is she a teacher?",
                    "Does she be a teacher?",
                ],

                "answer":
                    "Is she a teacher?",

                "explanation":
                    "С TO BE вспомогательный DO / DOES не используется.",
            },


            {
                "order": 16,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct question about an action.",

                "options": [
                    "Is he work at a hospital?",
                    "Does he work at a hospital?",
                    "Does he works at a hospital?",
                    "Do he work at a hospital?",
                ],

                "answer":
                    "Does he work at a hospital?",

                "explanation":
                    "WORK — обычный глагол → DOES + WORK.",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Do you often read?",
                    "Do often you read?",
                    "Are you often read?",
                    "Does you often read?",
                ],

                "answer":
                    "Do you often read?",

                "explanation":
                    "Правильный порядок: DO + YOU + OFTEN + READ.",
            },


            {
                "order": 18,
                "section": 8,
                "type": "choice",

                "prompt":
                    "___ you ever travel abroad?",

                "options": [
                    "Does",
                    "Do",
                    "Are",
                    "Is",
                ],

                "answer":
                    "Do",

                "explanation":
                    "YOU → DO. EVER означает «когда-нибудь».",
            },


            {
                "order": 19,
                "section": 9,
                "type": "choice",

                "prompt":
                    "My sister works at a school. Choose the correct question.",

                "options": [
                    "Does my sister works at a school?",
                    "Do my sister work at a school?",
                    "Does my sister work at a school?",
                    "Is my sister work at a school?",
                ],

                "answer":
                    "Does my sister work at a school?",

                "explanation":
                    "My sister = SHE → DOES + WORK.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "My parents live in Astana. Choose the correct question.",

                "options": [
                    "Does my parents live in Astana?",
                    "Do my parents live in Astana?",
                    "Are my parents live in Astana?",
                    "Do my parents lives in Astana?",
                ],

                "answer":
                    "Do my parents live in Astana?",

                "explanation":
                    "My parents = THEY → DO + LIVE.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "___ you like coffee?",

                "options": [
                    "Do",
                    "Does",
                    "Are",
                    "Is",
                ],

                "answer":
                    "Do",

                "explanation":
                    "YOU → DO.",
            },


            {
                "order": 22,

                "prompt":
                    "___ your brother play football?",

                "options": [
                    "Do",
                    "Does",
                    "Is",
                    "Are",
                ],

                "answer":
                    "Does",

                "explanation":
                    "Your brother = HE → DOES.",
            },


            {
                "order": 23,

                "prompt":
                    "Does Anna ___ English?",

                "options": [
                    "speaks",
                    "speak",
                    "speaking",
                    "is speak",
                ],

                "answer":
                    "speak",

                "explanation":
                    "После DOES используется базовая форма SPEAK.",
            },


            {
                "order": 24,

                "prompt":
                    "Does the lesson ___ at ten?",

                "options": [
                    "starts",
                    "start",
                    "starting",
                    "is start",
                ],

                "answer":
                    "start",

                "explanation":
                    "STARTS → DOES ... START?",
            },


            {
                "order": 25,

                "prompt":
                    "Does your mother ___ a car?",

                "options": [
                    "has",
                    "have",
                    "haves",
                    "having",
                ],

                "answer":
                    "have",

                "explanation":
                    "HAS → DOES ... HAVE?",
            },


            {
                "order": 26,

                "prompt":
                    "Do they work here?",

                "options": [
                    "No, they don't.",
                    "No, they aren't.",
                    "No, they doesn't.",
                    "No, they not.",
                ],

                "answer":
                    "No, they don't.",

                "explanation":
                    "Вопрос с DO → NO, THEY DON'T.",
            },


            {
                "order": 27,

                "prompt":
                    "Does she study English?",

                "options": [
                    "Yes, she do.",
                    "Yes, she is.",
                    "Yes, she does.",
                    "Yes, she studies does.",
                ],

                "answer":
                    "Yes, she does.",

                "explanation":
                    "Вопрос с DOES → YES, SHE DOES.",
            },


            {
                "order": 28,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Does he is tired?",
                    "Is he tired?",
                    "Do he tired?",
                    "Does he be tired?",
                ],

                "answer":
                    "Is he tired?",

                "explanation":
                    "TIRED используется с TO BE → IS HE TIRED?",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Does she usually works at home?",
                    "Does she usually work at home?",
                    "Do she usually work at home?",
                    "Is she usually work at home?",
                ],

                "answer":
                    "Does she usually work at home?",

                "explanation":
                    "Правильный порядок: DOES + SHE + USUALLY + WORK.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct pair.",

                "options": [
                    "Is she a teacher? / Does she work at a school?",
                    "Does she a teacher? / Is she work at a school?",
                    "Is she teacher? / Does she works at a school?",
                    "Does she is a teacher? / Do she work at a school?",
                ],

                "answer":
                    "Is she a teacher? / Does she work at a school?",

                "explanation":
                    "Профессия → TO BE; действие WORK → DOES + базовая форма.",
            },

        ]


        valid_orders = []


        for data in (
            training
            +
            final_test
        ):

            valid_orders.append(
                data["order"]
            )


            if data["order"] <= 20:

                section = (
                    section_objects[
                        data["section"]
                    ]
                )

            else:

                section = None


            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],

                defaults={
                    "section":
                        section,

                    "exercise_type":
                        data.get(
                            "type",
                            "choice",
                        ),

                    "prompt":
                        data["prompt"],

                    "options":
                        data["options"],

                    "correct_answer":
                        data["answer"],

                    "explanation":
                        data["explanation"],

                    "is_published":
                        True,
                },
            )


        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        GrammarLessonSection.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=[
                item["order"]
                for item in sections
            ],
        ).delete()


        self.stdout.write(
            self.style.SUCCESS(
                "✅ Interactive A1 Lesson 13 seeded"
            )
        )

        self.stdout.write(
            f"Micro rules: "
            f"{lesson.sections.count()}"
        )

        self.stdout.write(
            "Training exercises: "
            f"{lesson.exercises.filter(section__isnull=False).count()}"
        )

        self.stdout.write(
            "Final test: "
            f"{lesson.exercises.filter(section__isnull=True).count()}"
        )
