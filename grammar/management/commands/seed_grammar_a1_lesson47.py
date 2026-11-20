from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 47: First Conditional."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=47,
            defaults={
                "title":
                    "First Conditional",

                "slug":
                    "first-conditional",

                "theory_text":
                    "First Conditional: "
                    "If + Present Simple, will + V1.",

                "estimated_minutes":
                    20,

                "pass_score":
                    70,

                "xp_reward":
                    100,

                "is_published":
                    True,
            },
        )


        # =================================================
        # 10 MICRO RULES
        # =================================================

        sections = [

            {
                "order": 1,
                "title":
                    "Когда нужен First Conditional",

                "body":
                    """First Conditional используем,
когда говорим о реальной
возможности в будущем.

If it rains tomorrow,
we will stay home.

Дождь возможен,
но не гарантирован.

Результат зависит
от условия.""",
            },


            {
                "order": 2,
                "title":
                    "Главная формула",

                "body":
                    """Основная схема:

IF + Present Simple,
WILL + V1

If I have time,
I will help you.

Условие:

I have time

Результат:

I will help you.""",
            },


            {
                "order": 3,
                "title":
                    "После IF нет WILL",

                "body":
                    """После IF обычно
не используем WILL.

Правильно:

If she comes,
we will start.

Неправильно:

If she will come,
we will start.

Хотя речь о будущем,
после IF нужен
Present Simple.""",
            },


            {
                "order": 4,
                "title":
                    "Отрицание",

                "body":
                    """Отрицание в условии:

If you don't hurry,
you will be late.

If she doesn't study,
she will fail.

Отрицание в результате:

If it rains,
we won't go out.

WILL NOT = WON'T.""",
            },


            {
                "order": 5,
                "title":
                    "Порядок частей",

                "body":
                    """Если IF-часть первая:

If it rains,
we will stay home.

Ставим запятую.

Если результат первый:

We will stay home
if it rains.

Запятая обычно
не нужна.""",
            },


            {
                "order": 6,
                "title":
                    "CAN, MAY, MIGHT",

                "body":
                    """В результате можно использовать
не только WILL.

If you finish early,
you can go home.

If it rains,
we may stay home.

If we leave late,
we might miss the train.

Не говорим:

will can

will might.""",
            },


            {
                "order": 7,
                "title":
                    "SHOULD, MUST и команда",

                "body":
                    """Можно давать совет:

If you feel tired,
you should rest.

Необходимость:

If you feel worse,
you must see a doctor.

Команда:

If you see Anna,
tell her to call me.""",
            },


            {
                "order": 8,
                "title":
                    "UNLESS = IF NOT",

                "body":
                    """UNLESS означает:

если не.

Unless you hurry,
you will miss the bus.

То же самое:

If you don't hurry,
you will miss the bus.

После UNLESS
не нужно второе отрицание.""",
            },


            {
                "order": 9,
                "title":
                    "WHEN, AFTER, AS SOON AS",

                "body":
                    """После WHEN, AFTER,
BEFORE, AS SOON AS, UNTIL
для будущего тоже обычно
используем Present Simple.

I will call you
when I arrive.

We will eat
after she comes.

I will tell you
as soon as I know.""",
            },


            {
                "order": 10,
                "title":
                    "Zero vs First Conditional",

                "body":
                    """Zero Conditional:

общая закономерность.

If I drink coffee at night,
I can't sleep.

First Conditional:

конкретная будущая ситуация.

If I drink coffee tonight,
I won't sleep.

ZERO = всегда / обычно

FIRST = возможное будущее.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = GrammarLessonSection.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "title":
                        data["title"],

                    "body":
                        data["body"],
                },
            )

            section_objects[
                data["order"]
            ] = section


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            # SECTION 1
            {
                "order": 1,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Which sentence describes a real future possibility?",
                "options": [
                    "If it rains tomorrow, we will stay home.",
                    "If it rains, the ground gets wet.",
                    "If it rained yesterday, we stayed home.",
                    "If it had rained, we would have stayed home.",
                ],
                "answer":
                    "If it rains tomorrow, we will stay home.",
                "explanation":
                    "Конкретная возможная ситуация в будущем → First Conditional.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "First Conditional usually talks about...",
                "options": [
                    "a possible future result",
                    "a general scientific fact only",
                    "an impossible past event",
                    "a completed action yesterday",
                ],
                "answer":
                    "a possible future result",
                "explanation":
                    "First Conditional описывает реальную возможность в будущем.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "If I ___ time, I will call you.",
                "options": [
                    "have",
                    "will have",
                    "had",
                    "having",
                ],
                "answer":
                    "have",
                "explanation":
                    "После IF → Present Simple.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "If she studies hard, she ___ the exam.",
                "options": [
                    "will pass",
                    "passes every time",
                    "will passed",
                    "passing",
                ],
                "answer":
                    "will pass",
                "explanation":
                    "Результат → WILL + V1.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "If he ___ tomorrow, we will talk.",
                "options": [
                    "comes",
                    "will come",
                    "came",
                    "coming",
                ],
                "answer":
                    "comes",
                "explanation":
                    "После IF не используем WILL.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "If she calls, I will answer.",
                    "If she will call, I will answer.",
                    "If she calling, I will answer.",
                    "If she calls, I will answering.",
                ],
                "answer":
                    "If she calls, I will answer.",
                "explanation":
                    "IF + Present Simple, WILL + V1.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "If you ___ now, you will miss the bus.",
                "options": [
                    "don't leave",
                    "won't leave",
                    "doesn't leave",
                    "not leave",
                ],
                "answer":
                    "don't leave",
                "explanation":
                    "YOU → DON'T + base verb.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "If it rains, we ___ go to the park.",
                "options": [
                    "won't",
                    "don't will",
                    "not will",
                    "willn't",
                ],
                "answer":
                    "won't",
                "explanation":
                    "WILL NOT → WON'T.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "build",
                "prompt":
                    "Собери First Conditional.",
                "options": [
                    "If",
                    "I",
                    "finish",
                    "early",
                    "I",
                    "will",
                    "call",
                    "you",
                ],
                "answer":
                    "If I finish early I will call you",
                "explanation":
                    "IF + Present Simple → WILL + V1.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "Choose the correct reversed order.",
                "options": [
                    "I will call you if I finish early.",
                    "I will call you, if I will finish early.",
                    "I call you if I will finish early.",
                    "I will calling you if I finish early.",
                ],
                "answer":
                    "I will call you if I finish early.",
                "explanation":
                    "Если IF-часть стоит второй, запятая обычно не нужна.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "If you finish early, you ___ go home.",
                "options": [
                    "can",
                    "will can",
                    "can to",
                    "will able",
                ],
                "answer":
                    "can",
                "explanation":
                    "В результате можно использовать CAN.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "If we leave late, we ___ miss the train.",
                "options": [
                    "might",
                    "will might",
                    "might to",
                    "mights",
                ],
                "answer":
                    "might",
                "explanation":
                    "MIGHT выражает возможный результат.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "If you feel tired, you ___ rest.",
                "options": [
                    "should",
                    "should to",
                    "will should",
                    "shoulds",
                ],
                "answer":
                    "should",
                "explanation":
                    "В результате можно использовать SHOULD.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "If you see Anna, ___ her to call me.",
                "options": [
                    "tell",
                    "to tell",
                    "telling",
                    "will telling",
                ],
                "answer":
                    "tell",
                "explanation":
                    "В результате возможен imperative.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "___ you hurry, you will miss the train.",
                "options": [
                    "Unless",
                    "Unless not",
                    "If not will",
                    "Will unless",
                ],
                "answer":
                    "Unless",
                "explanation":
                    "UNLESS = IF NOT.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "Choose the same meaning: If you don't study, you will fail.",
                "options": [
                    "Unless you study, you will fail.",
                    "Unless you don't study, you will fail.",
                    "Unless you will study, you will fail.",
                    "Unless studying, you fail yesterday.",
                ],
                "answer":
                    "Unless you study, you will fail.",
                "explanation":
                    "После UNLESS не добавляем ещё одно отрицание.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "I will call you when I ___.",
                "options": [
                    "arrive",
                    "will arrive",
                    "arrived",
                    "will arriving",
                ],
                "answer":
                    "arrive",
                "explanation":
                    "После WHEN для будущего → Present Simple.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "We will start as soon as she ___.",
                "options": [
                    "comes",
                    "will come",
                    "came",
                    "coming",
                ],
                "answer":
                    "comes",
                "explanation":
                    "После AS SOON AS → Present Simple.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which is Zero Conditional?",
                "options": [
                    "If people don't sleep enough, they feel tired.",
                    "If I don't sleep tonight, I will be tired tomorrow.",
                    "If I had slept more, I wouldn't be tired.",
                    "If I sleep tomorrow, I slept better.",
                ],
                "answer":
                    "If people don't sleep enough, they feel tired.",
                "explanation":
                    "Общая закономерность → Zero Conditional.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which is First Conditional?",
                "options": [
                    "If I don't sleep tonight, I will be tired tomorrow.",
                    "If people don't sleep, they feel tired.",
                    "When I don't sleep enough, I feel bad.",
                    "If I didn't sleep yesterday, I was tired.",
                ],
                "answer":
                    "If I don't sleep tonight, I will be tired tomorrow.",
                "explanation":
                    "Конкретное возможное будущее → First Conditional.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "If the weather ___ good tomorrow, we will go hiking.",
                "options": [
                    "is",
                    "will be",
                    "was",
                    "being",
                ],
                "answer":
                    "is",
                "explanation":
                    "После IF → Present Simple.",
            },

            {
                "order": 22,
                "prompt":
                    "If my train is late, I ___ you.",
                "options": [
                    "will text",
                    "texted",
                    "will texting",
                    "will texts",
                ],
                "answer":
                    "will text",
                "explanation":
                    "Будущий результат → WILL + V1.",
            },

            {
                "order": 23,
                "prompt":
                    "If she ___ the job, she will move to London.",
                "options": [
                    "gets",
                    "will get",
                    "got",
                    "getting",
                ],
                "answer":
                    "gets",
                "explanation":
                    "SHE → GETS после IF.",
            },

            {
                "order": 24,
                "prompt":
                    "If we don't book now, we ___ a room.",
                "options": [
                    "might not get",
                    "will might not get",
                    "might not to get",
                    "not might gets",
                ],
                "answer":
                    "might not get",
                "explanation":
                    "MIGHT + base verb может выражать возможный результат.",
            },

            {
                "order": 25,
                "prompt":
                    "If your temperature gets higher, you ___ call a doctor.",
                "options": [
                    "should",
                    "will should",
                    "should to",
                    "shoulds",
                ],
                "answer":
                    "should",
                "explanation":
                    "SHOULD выражает совет.",
            },

            {
                "order": 26,
                "prompt":
                    "___ you leave now, you will be late.",
                "options": [
                    "Unless",
                    "Unless not",
                    "If won't",
                    "Will unless",
                ],
                "answer":
                    "Unless",
                "explanation":
                    "UNLESS = IF NOT.",
            },

            {
                "order": 27,
                "prompt":
                    "I will send you the file as soon as I ___ it.",
                "options": [
                    "finish",
                    "will finish",
                    "finished",
                    "will finished",
                ],
                "answer":
                    "finish",
                "explanation":
                    "После AS SOON AS → Present Simple.",
            },

            {
                "order": 28,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "If he arrives early, we will have time for coffee.",
                    "If he will arrive early, we will have time for coffee.",
                    "If he arrive early, we will have time for coffee.",
                    "If he arrives early, we will having time for coffee.",
                ],
                "answer":
                    "If he arrives early, we will have time for coffee.",
                "explanation":
                    "HE → ARRIVES; результат → WILL HAVE.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct future time-clause pair.",
                "options": [
                    "I'll call when I arrive. / We'll eat after she comes.",
                    "I'll call when I will arrive. / We'll eat after she will come.",
                    "I'll call when I arriving. / We'll eat after she come yesterday.",
                    "I'll calling when I arrive. / We'll ate after she comes.",
                ],
                "answer":
                    "I'll call when I arrive. / We'll eat after she comes.",
                "explanation":
                    "После WHEN и AFTER для будущего используется Present Simple.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "If I have time, I will help. / If you finish, you can leave. / Unless you hurry, you will be late.",
                    "If I will have time, I will help. / If you finish, you will can leave. / Unless you don't hurry, you will be late.",
                    "If I had time tomorrow, I will help. / If you finishing, can leave. / Unless you will hurry, you will be late.",
                    "If I have time, I will to help. / If you finish, can to leave. / Unless hurry, you will late.",
                ],
                "answer":
                    "If I have time, I will help. / If you finish, you can leave. / Unless you hurry, you will be late.",
                "explanation":
                    "First Conditional: Present Simple after IF/UNLESS; result can use WILL or CAN.",
            },

        ]


        all_exercises = (
            training
            +
            final_test
        )

        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

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
                "✅ Interactive A1 Lesson 47 seeded"
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
