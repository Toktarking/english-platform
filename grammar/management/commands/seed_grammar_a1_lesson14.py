from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 14: Present Simple WH-questions."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=14,

                defaults={
                    "title":
                        "Специальные вопросы "
                        "в Present Simple",

                    "slug":
                        "present-simple-special-questions",

                    "theory_text":
                        "Wh-questions in Present Simple.",

                    "estimated_minutes":
                        18,

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
        # 10 MICRO-RULES
        # ================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Что такое специальный вопрос?",

                "body":
                    """Специальный вопрос просит конкретную информацию.

Where do you live?
Где ты живёшь?

What does she want?
Что она хочет?

Why do they study English?
Почему они изучают английский?

На такие вопросы обычно нельзя ответить только YES или NO.

Нужно дать конкретную информацию:

Where do you work?

I work at a university.""",
            },


            {
                "order": 2,

                "title":
                    "Главные вопросительные слова",

                "body":
                    """Основные WH-слова:

WHERE — где / куда

WHAT — что / какой

WHEN — когда

WHY — почему

HOW — как

WHO — кто

WHICH — какой из нескольких

Примеры:

Where do you work?

What does she want?

When do they arrive?

Why does he study English?

How do you go to work?

Which book do you want?""",
            },


            {
                "order": 3,

                "title":
                    "Главная формула",

                "body":
                    """С обычным смысловым глаголом:

WH-word
+ DO / DOES
+ subject
+ base verb?

Примеры:

Where do you live?

What does she want?

Why do they work here?

When does the shop open?

С I / you / we / they:

DO

С he / she / it:

DOES.""",
            },


            {
                "order": 4,

                "title":
                    "После DOES глагол без -S",

                "body":
                    """После DOES основной глагол возвращается в базовую форму.

She works at a school.

Where does she work?

Не:

Where does she works?

Ещё:

He lives in Astana.
→ Where does he live?

She studies English.
→ What does she study?

The shop opens at nine.
→ When does the shop open?

She has a car.
→ What does she have?""",
            },


            {
                "order": 5,

                "title":
                    "HOW OFTEN, HOW MANY, HOW MUCH",

                "body":
                    """HOW OFTEN = как часто

How often do you exercise?

How often does she call you?

HOW MANY = сколько с countable nouns:

How many books do you have?

How many students does she teach?

HOW MUCH = сколько с uncountable nouns:

How much money do you need?

How much water does he drink?

Запомни:

many → countable

much → uncountable.""",
            },


            {
                "order": 6,

                "title":
                    "WHAT DO YOU DO?",

                "body":
                    """Вопрос:

What do you do?

обычно означает:

Чем вы занимаетесь?
Кем вы работаете?

Ответ:

I am a teacher.

или:

I work at a university.

Не путай:

What do you do?
обычная деятельность

What are you doing?
что происходит прямо сейчас

Во втором случае уже используется Present Continuous.""",
            },


            {
                "order": 7,

                "title":
                    "WHO: объект или подлежащее?",

                "body":
                    """Если WHO — объект действия, DO / DOES нужны.

Who do you call?

Подлежащее здесь YOU.

Who does she visit?

Подлежащее SHE.

Но если WHO само выполняет действие, DO / DOES обычно не нужны:

Who calls you?

Who works here?

Сравни:

Who calls you?
Кто звонит тебе?

Who do you call?
Кому звонишь ты?""",
            },


            {
                "order": 8,

                "title":
                    "WHAT тоже может быть подлежащим",

                "body":
                    """Если WHAT само выполняет действие, DO / DOES не нужны.

What makes this noise?

What causes this problem?

Но если подлежащее уже есть:

What do you buy?

What does she need?

Сравни:

What makes this sound?

WHAT выполняет действие.

What do you hear?

YOU выполняет действие.""",
            },


            {
                "order": 9,

                "title":
                    "Предлоги и WHAT / WHICH + noun",

                "body":
                    """В разговорном английском предлог часто остаётся в конце:

Who do you work with?

Who does she speak to?

Where does he come from?

Также WH-слово может стоять с существительным:

What language do you speak?

What time does the lesson start?

Which book do you want?

Which bus does she take?

WHICH обычно используется, когда выбор ограничен.""",
            },


            {
                "order": 10,

                "title":
                    "TO BE или DO / DOES?",

                "body":
                    """Если используется AM / IS / ARE, DO и DOES не нужны.

Where are you?

Why is she tired?

What is his job?

Who are they?

Но с обычным действием:

Where does she work?

Why do they study English?

Сравни:

Where is she?
Где она?

Where does she work?
Где она работает?

Алгоритм:

1. Выбери WH-word.
2. Найди подлежащее.
3. Если обычный глагол → DO / DOES.
4. После DOES → base verb.
5. Если TO BE → DO / DOES не нужны.""",
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
                    "___ do you work?",

                "options": [
                    "Where",
                    "Who",
                    "How many",
                    "Which one",
                ],

                "answer":
                    "Where",

                "explanation":
                    "Чтобы спросить о месте, используется WHERE.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "Why do you study English?",

                "options": [
                    "Yes, I do.",
                    "Because I need it for work.",
                    "At university.",
                    "Every Monday.",
                ],

                "answer":
                    "Because I need it for work.",

                "explanation":
                    "WHY спрашивает о причине.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "___ do they arrive?",

                "options": [
                    "When",
                    "Who",
                    "How many",
                    "Which",
                ],

                "answer":
                    "When",

                "explanation":
                    "WHEN спрашивает о времени.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "___ book do you want: the red one or the blue one?",

                "options": [
                    "Which",
                    "Where",
                    "Why",
                    "Who",
                ],

                "answer":
                    "Which",

                "explanation":
                    "Есть ограниченный выбор, поэтому WHICH.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "Where ___ your brother live?",

                "options": [],

                "answer":
                    "does",

                "explanation":
                    "Your brother = HE → DOES.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "What ___ your parents do?",

                "options": [
                    "does",
                    "do",
                    "are",
                    "is",
                ],

                "answer":
                    "do",

                "explanation":
                    "Your parents = THEY → DO.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "What does your sister ___?",

                "options": [
                    "teaches",
                    "teach",
                    "teaching",
                    "is teach",
                ],

                "answer":
                    "teach",

                "explanation":
                    "После DOES используется базовая форма TEACH.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "When does the shop ___?",

                "options": [
                    "opens",
                    "open",
                    "opening",
                    "is open",
                ],

                "answer":
                    "open",

                "explanation":
                    "OPENS → DOES ... OPEN?",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "___ do you exercise?",

                "options": [
                    "How often",
                    "How much",
                    "How many",
                    "Which",
                ],

                "answer":
                    "How often",

                "explanation":
                    "Спрашиваем о частоте действия.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "___ books do you have?",

                "options": [
                    "How much",
                    "How many",
                    "How often",
                    "How",
                ],

                "answer":
                    "How many",

                "explanation":
                    "BOOKS — countable plural → HOW MANY.",
            },


            {
                "order": 11,
                "section": 5,
                "type": "choice",

                "prompt":
                    "___ money does he need?",

                "options": [
                    "How many",
                    "How much",
                    "How often",
                    "Which",
                ],

                "answer":
                    "How much",

                "explanation":
                    "MONEY — uncountable → HOW MUCH.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "What do you do?",

                "options": [
                    "I am a teacher.",
                    "I am doing my homework now.",
                    "At eight o'clock.",
                    "Yes, I do.",
                ],

                "answer":
                    "I am a teacher.",

                "explanation":
                    "WHAT DO YOU DO? спрашивает об обычной деятельности или профессии.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "___ calls you every morning?",

                "options": [
                    "Who",
                    "Who does",
                    "Who do",
                    "What do",
                ],

                "answer":
                    "Who",

                "explanation":
                    "WHO само является подлежащим.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Who ___ you call every morning?",

                "options": [
                    "do",
                    "does",
                    "are",
                    "is",
                ],

                "answer":
                    "do",

                "explanation":
                    "Подлежащее YOU, WHO здесь объект → DO.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "What does make this noise?",
                    "What makes this noise?",
                    "What do makes this noise?",
                    "What is make this noise?",
                ],

                "answer":
                    "What makes this noise?",

                "explanation":
                    "WHAT само выполняет действие, поэтому DOES не нужен.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "___ do you hear?",

                "options": [
                    "What",
                    "What does",
                    "Who does",
                    "Where is",
                ],

                "answer":
                    "What",

                "explanation":
                    "Подлежащее YOU → WHAT DO YOU HEAR?",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the natural question.",

                "options": [
                    "Who do you work with?",
                    "Who you work with?",
                    "Who does you work with?",
                    "With who you do work?",
                ],

                "answer":
                    "Who do you work with?",

                "explanation":
                    "В разговорном английском предлог WITH естественно остаётся в конце.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "___ language does she speak?",

                "options": [
                    "What",
                    "Where",
                    "Who",
                    "How much",
                ],

                "answer":
                    "What",

                "explanation":
                    "WHAT + noun: WHAT LANGUAGE.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Where does she be?",
                    "Where is she?",
                    "Where does she is?",
                    "Where she is?",
                ],

                "answer":
                    "Where is she?",

                "explanation":
                    "С TO BE DO / DOES не используются.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "She works at a school. Which question asks about the place?",

                "options": [
                    "What does she work?",
                    "Where does she work?",
                    "Where does she works?",
                    "Where is she work?",
                ],

                "answer":
                    "Where does she work?",

                "explanation":
                    "WORK — обычный глагол → WHERE DOES SHE WORK?",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "___ do you usually have lunch?",

                "options": [
                    "When",
                    "Who",
                    "How many",
                    "Which one",
                ],

                "answer":
                    "When",

                "explanation":
                    "WHEN спрашивает о времени.",
            },


            {
                "order": 22,

                "prompt":
                    "Where ___ your parents work?",

                "options": [
                    "does",
                    "do",
                    "are",
                    "is",
                ],

                "answer":
                    "do",

                "explanation":
                    "Your parents = THEY → DO.",
            },


            {
                "order": 23,

                "prompt":
                    "Why does Anna ___ English?",

                "options": [
                    "studies",
                    "study",
                    "studying",
                    "is study",
                ],

                "answer":
                    "study",

                "explanation":
                    "После DOES используется STUDY.",
            },


            {
                "order": 24,

                "prompt":
                    "___ water do you drink every day?",

                "options": [
                    "How many",
                    "How much",
                    "How often",
                    "Which",
                ],

                "answer":
                    "How much",

                "explanation":
                    "WATER — uncountable → HOW MUCH.",
            },


            {
                "order": 25,

                "prompt":
                    "___ students does she teach?",

                "options": [
                    "How much",
                    "How many",
                    "How often",
                    "How",
                ],

                "answer":
                    "How many",

                "explanation":
                    "STUDENTS — countable plural → HOW MANY.",
            },


            {
                "order": 26,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Who does work here?",
                    "Who works here?",
                    "Who do works here?",
                    "Who is work here?",
                ],

                "answer":
                    "Who works here?",

                "explanation":
                    "WHO является подлежащим, поэтому DO / DOES не нужны.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Who do they visit?",
                    "Who they visit?",
                    "Who does they visit?",
                    "Who are they visit?",
                ],

                "answer":
                    "Who do they visit?",

                "explanation":
                    "THEY — подлежащее; WHO — объект → DO.",
            },


            {
                "order": 28,

                "prompt":
                    "What time does the train ___?",

                "options": [
                    "leaves",
                    "leave",
                    "leaving",
                    "is leave",
                ],

                "answer":
                    "leave",

                "explanation":
                    "После DOES используется базовая форма LEAVE.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Why does she tired?",
                    "Why is she tired?",
                    "Why do she tired?",
                    "Why does she be tired?",
                ],

                "answer":
                    "Why is she tired?",

                "explanation":
                    "TIRED используется с TO BE → WHY IS SHE TIRED?",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct pair.",

                "options": [
                    "Where is she? / Where does she work?",
                    "Where does she be? / Where is she work?",
                    "Where she is? / Where she works?",
                    "Where does she is? / Where does she works?",
                ],

                "answer":
                    "Where is she? / Where does she work?",

                "explanation":
                    "Местонахождение → TO BE; действие WORK → DOES + base verb.",
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
                "✅ Interactive A1 Lesson 14 seeded"
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
