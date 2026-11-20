from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 49: Third Conditional."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=49,
            defaults={
                "title":
                    "Third Conditional",

                "slug":
                    "third-conditional",

                "theory_text":
                    "Third Conditional: "
                    "If + Past Perfect, would have + V3.",

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
                    "Когда нужен Third Conditional",

                "body":
                    """Third Conditional говорит
о нереальном прошлом.

Что-то уже произошло,
и изменить это нельзя.

If I had studied more,
I would have passed.

Реальность:

I didn't study enough.

I didn't pass.""",
            },


            {
                "order": 2,
                "title":
                    "Главная формула",

                "body":
                    """Основная схема:

IF + HAD + V3,
WOULD HAVE + V3

If she had left earlier,
she would have caught the bus.

Условие:

had left

Результат:

would have caught.""",
            },


            {
                "order": 3,
                "title":
                    "Past Perfect после IF",

                "body":
                    """В IF-части используем:

HAD + V3

had studied

had worked

had gone

had seen

had written

Неправильные глаголы:

go → gone

see → seen

write → written.""",
            },


            {
                "order": 4,
                "title":
                    "WOULD HAVE + V3",

                "body":
                    """В результате используем:

WOULD HAVE + V3

would have passed

would have arrived

would have helped

Пример:

If I had known,
I would have helped you.

Не:

would helped

Не:

would have help.""",
            },


            {
                "order": 5,
                "title":
                    "Сожаление о прошлом",

                "body":
                    """Third Conditional часто
показывает сожаление.

If I had studied more,
I would have passed.

If we had left earlier,
we wouldn't have missed the train.

То есть:

прошлое могло быть другим,
но уже поздно.""",
            },


            {
                "order": 6,
                "title":
                    "Отрицание",

                "body":
                    """В IF-части:

HADN'T + V3

If I hadn't missed the bus,
I would have arrived earlier.

В результате:

WOULDN'T HAVE + V3

If she had taken an umbrella,
she wouldn't have got wet.""",
            },


            {
                "order": 7,
                "title":
                    "COULD HAVE",

                "body":
                    """COULD HAVE + V3
показывает возможность в прошлом.

If I had had more time,
I could have helped you.

Смысл:

у меня была бы возможность помочь.

COULD HAVE = мог бы.""",
            },


            {
                "order": 8,
                "title":
                    "MIGHT HAVE",

                "body":
                    """MIGHT HAVE + V3
показывает менее уверенный результат.

If she had left earlier,
she might have caught the bus.

MIGHT HAVE = возможно,
результат произошёл бы.""",
            },


            {
                "order": 9,
                "title":
                    "HAD HAD",

                "body":
                    """Иногда встречается:

HAD HAD

If I had had more time,
I would have finished.

Первое HAD:

вспомогательный глагол.

Второе HAD:

третья форма HAVE.

Это правильно.""",
            },


            {
                "order": 10,
                "title":
                    "Second vs Third Conditional",

                "body":
                    """Second Conditional:

нереальное настоящее.

If I had more money,
I would travel.

Third Conditional:

нереальное прошлое.

If I had had more money,
I would have travelled.

SECOND → сейчас

THIRD → прошлое.""",
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
                    "Which sentence describes an unreal past?",
                "options": [
                    "If I had studied more, I would have passed.",
                    "If I study, I will pass.",
                    "If I studied more, I would pass.",
                    "If I study, I pass.",
                ],
                "answer":
                    "If I had studied more, I would have passed.",
                "explanation":
                    "Third Conditional = unreal past.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Third Conditional usually talks about...",
                "options": [
                    "a past situation that cannot be changed",
                    "a general fact",
                    "a real future plan",
                    "a present routine",
                ],
                "answer":
                    "a past situation that cannot be changed",
                "explanation":
                    "Third Conditional относится к нереальному прошлому.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "If she ___ earlier, she would have caught the bus.",
                "options": [
                    "had left",
                    "left",
                    "would leave",
                    "has left",
                ],
                "answer":
                    "had left",
                "explanation":
                    "После IF → HAD + V3.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "If I had known, I ___ you.",
                "options": [
                    "would have called",
                    "would call",
                    "will call",
                    "would called",
                ],
                "answer":
                    "would have called",
                "explanation":
                    "Результат → WOULD HAVE + V3.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "Choose the correct V3: GO",
                "options": [
                    "gone",
                    "went",
                    "go",
                    "going",
                ],
                "answer":
                    "gone",
                "explanation":
                    "GO → WENT → GONE.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "If he ___ the message, he would have replied.",
                "options": [
                    "had seen",
                    "had saw",
                    "saw",
                    "would see",
                ],
                "answer":
                    "had seen",
                "explanation":
                    "SEE → SEEN; Past Perfect → HAD SEEN.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "If we had booked earlier, we ___ less.",
                "options": [
                    "would have paid",
                    "would pay",
                    "paid",
                    "would have pay",
                ],
                "answer":
                    "would have paid",
                "explanation":
                    "WOULD HAVE + V3.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "Choose the correct form.",
                "options": [
                    "would have gone",
                    "would have went",
                    "would gone",
                    "would have go",
                ],
                "answer":
                    "would have gone",
                "explanation":
                    "После WOULD HAVE нужна третья форма.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "If we had left earlier, we ___ the train.",
                "options": [
                    "wouldn't have missed",
                    "wouldn't miss",
                    "didn't miss",
                    "hadn't missed",
                ],
                "answer":
                    "wouldn't have missed",
                "explanation":
                    "Нереальный прошлый результат.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "build",
                "prompt":
                    "Собери Third Conditional.",
                "options": [
                    "If",
                    "I",
                    "had",
                    "studied",
                    "I",
                    "would",
                    "have",
                    "passed",
                ],
                "answer":
                    "If I had studied I would have passed",
                "explanation":
                    "HAD + V3 → WOULD HAVE + V3.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "If I ___ the bus, I would have arrived on time.",
                "options": [
                    "hadn't missed",
                    "didn't miss",
                    "wouldn't miss",
                    "haven't missed",
                ],
                "answer":
                    "hadn't missed",
                "explanation":
                    "Отрицание Past Perfect → HADN'T + V3.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "If she had taken an umbrella, she ___ wet.",
                "options": [
                    "wouldn't have got",
                    "wouldn't get",
                    "won't get",
                    "hadn't got",
                ],
                "answer":
                    "wouldn't have got",
                "explanation":
                    "WOULDN'T HAVE + V3.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "If I had had more time, I ___ you.",
                "options": [
                    "could have helped",
                    "could help",
                    "could to have helped",
                    "will can help",
                ],
                "answer":
                    "could have helped",
                "explanation":
                    "COULD HAVE + V3 = возможность в прошлом.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "If they had listened, they ___ the problem.",
                "options": [
                    "could have avoided",
                    "could avoid yesterday",
                    "could to avoid",
                    "will have avoided",
                ],
                "answer":
                    "could have avoided",
                "explanation":
                    "COULD HAVE + V3.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "If she had left earlier, she ___ the bus.",
                "options": [
                    "might have caught",
                    "might catch",
                    "might to have caught",
                    "will might catch",
                ],
                "answer":
                    "might have caught",
                "explanation":
                    "MIGHT HAVE + V3.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "If we had taken another road, we ___ arrived earlier.",
                "options": [
                    "might have",
                    "might",
                    "will might have",
                    "might to have",
                ],
                "answer":
                    "might have",
                "explanation":
                    "MIGHT HAVE + V3 выражает возможный прошлый результат.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "If I ___ more money, I would have bought the laptop.",
                "options": [
                    "had had",
                    "had",
                    "would have",
                    "have had",
                ],
                "answer":
                    "had had",
                "explanation":
                    "Past Perfect глагола HAVE → HAD HAD.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "If she ___ more careful, she wouldn't have made the mistake.",
                "options": [
                    "had been",
                    "was",
                    "would be",
                    "has been",
                ],
                "answer":
                    "had been",
                "explanation":
                    "Past Perfect глагола BE → HAD BEEN.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which is Second Conditional?",
                "options": [
                    "If I had more money, I would travel.",
                    "If I had had more money, I would have travelled.",
                    "If I have money, I will travel.",
                    "If I have money, I travel.",
                ],
                "answer":
                    "If I had more money, I would travel.",
                "explanation":
                    "Second Conditional = unreal present/future.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which is Third Conditional?",
                "options": [
                    "If I had had more money, I would have travelled.",
                    "If I had more money, I would travel.",
                    "If I have money, I will travel.",
                    "If I have money, I travel.",
                ],
                "answer":
                    "If I had had more money, I would have travelled.",
                "explanation":
                    "Third Conditional = unreal past.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "If I ___ about the traffic, I would have left earlier.",
                "options": [
                    "had known",
                    "knew",
                    "would know",
                    "have known",
                ],
                "answer":
                    "had known",
                "explanation":
                    "Third Conditional → HAD + V3.",
            },

            {
                "order": 22,
                "prompt":
                    "If she had prepared better, she ___ the interview.",
                "options": [
                    "would have passed",
                    "would pass",
                    "will pass",
                    "would have pass",
                ],
                "answer":
                    "would have passed",
                "explanation":
                    "Результат → WOULD HAVE + V3.",
            },

            {
                "order": 23,
                "prompt":
                    "If we ___ the map, we wouldn't have got lost.",
                "options": [
                    "had checked",
                    "checked",
                    "would check",
                    "have checked",
                ],
                "answer":
                    "had checked",
                "explanation":
                    "IF + Past Perfect.",
            },

            {
                "order": 24,
                "prompt":
                    "If he hadn't driven so fast, he ___ the accident.",
                "options": [
                    "might have avoided",
                    "might avoid",
                    "will might avoid",
                    "might to have avoided",
                ],
                "answer":
                    "might have avoided",
                "explanation":
                    "MIGHT HAVE + V3.",
            },

            {
                "order": 25,
                "prompt":
                    "If I had had your number, I ___ you.",
                "options": [
                    "could have called",
                    "could call tomorrow",
                    "could to have called",
                    "will can call",
                ],
                "answer":
                    "could have called",
                "explanation":
                    "COULD HAVE + V3 = возможность в прошлом.",
            },

            {
                "order": 26,
                "prompt":
                    "If they had taken a taxi, they ___ late.",
                "options": [
                    "wouldn't have been",
                    "wouldn't be",
                    "weren't",
                    "hadn't been",
                ],
                "answer":
                    "wouldn't have been",
                "explanation":
                    "WOULDN'T HAVE BEEN = нереальный прошлый результат.",
            },

            {
                "order": 27,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "If she had gone earlier, she would have arrived on time.",
                    "If she had went earlier, she would have arrived on time.",
                    "If she went earlier, she would have arrive on time.",
                    "If she would have gone earlier, she would arrived on time.",
                ],
                "answer":
                    "If she had gone earlier, she would have arrived on time.",
                "explanation":
                    "GO → GONE; WOULD HAVE + ARRIVED.",
            },

            {
                "order": 28,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "If I had known, I would have told you.",
                    "If I knew, I would have told you yesterday.",
                    "If I would have known, I would have told you.",
                    "If I had knew, I would told you.",
                ],
                "answer":
                    "If I had known, I would have told you.",
                "explanation":
                    "Правильная формула Third Conditional.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct Second / Third Conditional pair.",
                "options": [
                    "If she knew, she would tell us. / If she had known, she would have told us.",
                    "If she had known, she would tell us. / If she knew, she would have told us.",
                    "If she would know, she would tell us. / If she would have known, she would have told us.",
                    "If she knows, she would tell us. / If she had knew, she would told us.",
                ],
                "answer":
                    "If she knew, she would tell us. / If she had known, she would have told us.",
                "explanation":
                    "Second = unreal present; Third = unreal past.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "If I had studied, I would have passed. / If I had had time, I could have helped. / If she had left earlier, she might have caught the bus.",
                    "If I studied, I would have passed. / If I would have time, I could help. / If she had left earlier, she might caught the bus.",
                    "If I had studied, I would passed. / If I had had time, I could to have helped. / If she left earlier, she might have caught the bus.",
                    "If I would have studied, I would have passed. / If I had time, I could have help. / If she had left earlier, she will might have caught the bus.",
                ],
                "answer":
                    "If I had studied, I would have passed. / If I had had time, I could have helped. / If she had left earlier, she might have caught the bus.",
                "explanation":
                    "Third Conditional: HAD + V3 → WOULD/COULD/MIGHT HAVE + V3.",
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
                "✅ Interactive A1 Lesson 49 seeded"
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
