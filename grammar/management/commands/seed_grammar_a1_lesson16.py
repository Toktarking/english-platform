from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 16: HAVE/HAS and HAVE GOT/HAS GOT."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=16,

                defaults={
                    "title":
                        "HAVE / HAS и "
                        "HAVE GOT / HAS GOT",

                    "slug":
                        "have-has-have-got",

                    "theory_text":
                        "Have / has and "
                        "have got / has got.",

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
                    "Что означает HAVE?",

                "body":
                    """HAVE часто означает:

иметь;
у кого-то есть;
обладать.

В русском:

У меня есть машина.

В английском:

I have a car.

То есть владелец становится подлежащим.

Примеры:

I have a laptop.

They have two children.

She has a new job.""",
            },


            {
                "order": 2,

                "title":
                    "HAVE или HAS?",

                "body":
                    """Главная схема:

I → HAVE

you → HAVE

we → HAVE

they → HAVE

he → HAS

she → HAS

it → HAS

Примеры:

We have a question.

They have a house.

He has a car.

She has a brother.

The house has three bedrooms.""",
            },


            {
                "order": 3,

                "title":
                    "HAVE используется не только для вещей",

                "body":
                    """HAVE / HAS может описывать:

владение:

I have a phone.

семью:

She has two brothers.

внешность:

He has dark hair.

She has blue eyes.

характеристику:

The house has large windows.

состояние:

I have a headache.

She has a cold.

проблему:

We have a problem.""",
            },


            {
                "order": 4,

                "title":
                    "Что ставить после HAVE / HAS?",

                "body":
                    """С одним countable noun обычно нужен A / AN:

I have a car.

He has an idea.

Не:

I have car.

С plural:

I have two books.

She has three sisters.

С uncountable nouns:

We have some information.

They have enough money.

I have little time.

Не:

an information

a money.""",
            },


            {
                "order": 5,

                "title":
                    "Отрицание: DON'T HAVE / DOESN'T HAVE",

                "body":
                    """С I / YOU / WE / THEY:

DON'T HAVE

I don't have a car.

They don't have much time.

С HE / SHE / IT:

DOESN'T HAVE

He doesn't have a car.

She doesn't have children.

Важно:

HAS превращается в DOESN'T HAVE.

She has a car.

She doesn't have a car.

Не:

She doesn't has a car.""",
            },


            {
                "order": 6,

                "title":
                    "Вопросы и краткие ответы с HAVE",

                "body":
                    """Обычная система HAVE использует DO / DOES.

Do you have a car?

Does she have a car?

Do they have children?

Does he have a job?

После DOES используется HAVE:

не:

Does she has...?

а:

Does she have...?

Краткие ответы:

Do you have a car?

Yes, I do.
No, I don't.

Does she have a car?

Yes, she does.
No, she doesn't.""",
            },


            {
                "order": 7,

                "title":
                    "HAVE GOT / HAS GOT",

                "body":
                    """Для владения можно также использовать HAVE GOT.

I have a car.

I have got a car.

Оба варианта означают:

У меня есть машина.

Формы:

I / you / we / they
→ HAVE GOT

he / she / it
→ HAS GOT

Примеры:

I've got a question.

She's got a new job.

They've got three children.

The house has got a garden.""",
            },


            {
                "order": 8,

                "title":
                    "Отрицания и вопросы с HAVE GOT",

                "body":
                    """В системе HAVE GOT DO / DOES не используются.

Отрицание:

I haven't got a car.

She hasn't got a car.

They haven't got much time.

Вопрос:

Have you got a car?

Has she got a car?

Have they got children?

Краткие ответы:

Have you got a car?

Yes, I have.
No, I haven't.

Has she got a car?

Yes, she has.
No, she hasn't.""",
            },


            {
                "order": 9,

                "title":
                    "Не смешивай две системы",

                "body":
                    """Есть две правильные системы.

Система 1:

She has a car.

She doesn't have a car.

Does she have a car?

Yes, she does.

Система 2:

She has got a car.

She hasn't got a car.

Has she got a car?

Yes, she has.

Не смешивай:

Does she have got a car? ❌

She doesn't have got a car. ❌

Выбери одну систему и строй её полностью.""",
            },


            {
                "order": 10,

                "title":
                    "Когда HAVE означает действие",

                "body":
                    """HAVE может быть обычным действием:

have breakfast

have lunch

have dinner

have a shower

have a rest

have a lesson

have a good time

Примеры:

I have breakfast at seven.

She has a shower every morning.

We have English on Monday.

В таком значении обычно используется обычная система DO / DOES:

Does she have lunch at work?

Do you have breakfast at home?

Не:

I have got breakfast at seven.

HAVE TO — «нужно / приходится» — это уже отдельная конструкция.""",
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
                    "We ___ two children.",

                "options": [
                    "has",
                    "have",
                    "having",
                    "are have",
                ],

                "answer":
                    "have",

                "explanation":
                    "WE → HAVE.",
            },


            {
                "order": 2,
                "section": 2,
                "type": "choice",

                "prompt":
                    "My sister ___ a new job.",

                "options": [
                    "have",
                    "has",
                    "having",
                    "is have",
                ],

                "answer":
                    "has",

                "explanation":
                    "My sister = SHE → HAS.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "The students ___ many questions.",

                "options": [],

                "answer":
                    "have",

                "explanation":
                    "The students = THEY → HAVE.",
            },


            {
                "order": 4,
                "section": 3,
                "type": "choice",

                "prompt":
                    "The house ___ four bedrooms.",

                "options": [
                    "have",
                    "has",
                    "is",
                    "are",
                ],

                "answer":
                    "has",

                "explanation":
                    "The house = IT → HAS.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "She ___ blue eyes.",

                "options": [
                    "have",
                    "has",
                    "is",
                    "are",
                ],

                "answer":
                    "has",

                "explanation":
                    "SHE → HAS. Здесь описывается внешность.",
            },


            {
                "order": 6,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I have car.",
                    "I have a car.",
                    "I have an car.",
                    "I have one a car.",
                ],

                "answer":
                    "I have a car.",

                "explanation":
                    "Один countable noun требует A / AN.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "We have ___ information about the project.",

                "options": [
                    "an",
                    "a",
                    "some",
                    "two",
                ],

                "answer":
                    "some",

                "explanation":
                    "INFORMATION — uncountable noun.",
            },


            {
                "order": 8,
                "section": 5,
                "type": "choice",

                "prompt":
                    "He doesn't ___ a driving licence.",

                "options": [
                    "has",
                    "have",
                    "having",
                    "had",
                ],

                "answer":
                    "have",

                "explanation":
                    "После DOESN'T используется HAVE.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "She doesn't has a car.",
                    "She doesn't have a car.",
                    "She don't have a car.",
                    "She isn't have a car.",
                ],

                "answer":
                    "She doesn't have a car.",

                "explanation":
                    "SHE → DOESN'T HAVE.",
            },


            {
                "order": 10,
                "section": 6,
                "type": "choice",

                "prompt":
                    "___ you have any brothers?",

                "options": [
                    "Does",
                    "Do",
                    "Are",
                    "Has",
                ],

                "answer":
                    "Do",

                "explanation":
                    "YOU → DO YOU HAVE...?",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Does she ___ a car?",

                "options": [
                    "has",
                    "have",
                    "having",
                    "got",
                ],

                "answer":
                    "have",

                "explanation":
                    "После DOES используется базовая форма HAVE.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Does Marat have a car?",

                "options": [
                    "Yes, he has.",
                    "Yes, he does.",
                    "Yes, he is.",
                    "Yes, he have.",
                ],

                "answer":
                    "Yes, he does.",

                "explanation":
                    "В обычной HAVE-системе вопрос с DOES требует ответа DOES.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "fill",

                "prompt":
                    "She ___ got a new phone.",

                "options": [],

                "answer":
                    "has",

                "explanation":
                    "SHE → HAS GOT.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "They have ___ a large house.",

                "options": [
                    "get",
                    "got",
                    "gets",
                    "getting",
                ],

                "answer":
                    "got",

                "explanation":
                    "Правильная конструкция — HAVE GOT.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct HAVE GOT negative.",

                "options": [
                    "She doesn't have got a car.",
                    "She hasn't got a car.",
                    "She doesn't has got a car.",
                    "She isn't got a car.",
                ],

                "answer":
                    "She hasn't got a car.",

                "explanation":
                    "HAS GOT → HASN'T GOT.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "___ they got enough time?",

                "options": [
                    "Has",
                    "Have",
                    "Do",
                    "Are",
                ],

                "answer":
                    "Have",

                "explanation":
                    "HAVE GOT question → HAVE THEY GOT...?",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Has your sister got a car?",

                "options": [
                    "No, she doesn't.",
                    "No, she hasn't.",
                    "No, she isn't.",
                    "No, she don't.",
                ],

                "answer":
                    "No, she hasn't.",

                "explanation":
                    "HAS ... GOT? → NO, SHE HASN'T.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Which pair uses one system consistently?",

                "options": [
                    "She has a car. / Does she have a car?",
                    "She has a car. / Has she got a car?",
                    "She has got a car. / Does she have got a car?",
                    "She has got a car. / Does she has a car?",
                ],

                "answer":
                    "She has a car. / Does she have a car?",

                "explanation":
                    "Это единая обычная HAVE-система.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence about breakfast.",

                "options": [
                    "I have got breakfast at seven.",
                    "I have breakfast at seven.",
                    "I am have breakfast at seven.",
                    "I has breakfast at seven.",
                ],

                "answer":
                    "I have breakfast at seven.",

                "explanation":
                    "HAVE BREAKFAST — действие; HAVE GOT здесь не используется.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "build",

                "prompt":
                    "Собери правильный вопрос.",

                "options": [
                    "Does",
                    "she",
                    "have",
                    "lunch",
                    "at",
                    "work",
                ],

                "answer":
                    "Does she have lunch at work",

                "explanation":
                    "HAVE LUNCH — действие, поэтому используется DOES + HAVE.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "My parents ___ a small house.",

                "options": [
                    "has",
                    "have",
                    "having",
                    "is have",
                ],

                "answer":
                    "have",

                "explanation":
                    "My parents = THEY → HAVE.",
            },


            {
                "order": 22,

                "prompt":
                    "The dog ___ a long tail.",

                "options": [
                    "have",
                    "has",
                    "is",
                    "are",
                ],

                "answer":
                    "has",

                "explanation":
                    "The dog = IT → HAS.",
            },


            {
                "order": 23,

                "prompt":
                    "He doesn't ___ any brothers.",

                "options": [
                    "has",
                    "have",
                    "having",
                    "got",
                ],

                "answer":
                    "have",

                "explanation":
                    "После DOESN'T используется HAVE.",
            },


            {
                "order": 24,

                "prompt":
                    "___ your parents have a car?",

                "options": [
                    "Does",
                    "Do",
                    "Has",
                    "Are",
                ],

                "answer":
                    "Do",

                "explanation":
                    "Your parents = THEY → DO THEY HAVE...?",
            },


            {
                "order": 25,

                "prompt":
                    "Does your brother have children?",

                "options": [
                    "Yes, he does.",
                    "Yes, he has.",
                    "Yes, he is.",
                    "Yes, he have.",
                ],

                "answer":
                    "Yes, he does.",

                "explanation":
                    "Обычная система с DOES → YES, HE DOES.",
            },


            {
                "order": 26,

                "prompt":
                    "We ___ got enough time.",

                "options": [
                    "has",
                    "have",
                    "do",
                    "are",
                ],

                "answer":
                    "have",

                "explanation":
                    "WE → HAVE GOT.",
            },


            {
                "order": 27,

                "prompt":
                    "___ she got a new job?",

                "options": [
                    "Does",
                    "Has",
                    "Is",
                    "Do",
                ],

                "answer":
                    "Has",

                "explanation":
                    "HAS GOT question → HAS SHE GOT...?",
            },


            {
                "order": 28,

                "prompt":
                    "Choose the correct HAVE GOT negative.",

                "options": [
                    "They don't have got enough money.",
                    "They haven't got enough money.",
                    "They doesn't got enough money.",
                    "They aren't got enough money.",
                ],

                "answer":
                    "They haven't got enough money.",

                "explanation":
                    "THEY HAVE GOT → THEY HAVEN'T GOT.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the sentence where HAVE describes an action.",

                "options": [
                    "She has two sisters.",
                    "He has blue eyes.",
                    "I have breakfast at eight.",
                    "The house has a garden.",
                ],

                "answer":
                    "I have breakfast at eight.",

                "explanation":
                    "HAVE BREAKFAST — действие, а не владение.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct pair.",

                "options": [
                    "She has a car. / Does she have a car?",
                    "She has a car. / Does she has a car?",
                    "She has got a car. / Does she have got a car?",
                    "She has got a car. / Does she got a car?",
                ],

                "answer":
                    "She has a car. / Does she have a car?",

                "explanation":
                    "Обе фразы принадлежат одной системе: HAS → DOES ... HAVE?",
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
                "✅ Interactive A1 Lesson 16 seeded"
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
