from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 46: Zero Conditional."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=46,
            defaults={
                "title":
                    "Zero Conditional",

                "slug":
                    "zero-conditional",

                "theory_text":
                    "Zero Conditional: "
                    "If + Present Simple, Present Simple.",

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
                    "Когда нужен Zero Conditional",

                "body":
                    """Zero Conditional используем,
когда результат происходит
всегда или обычно.

Это может быть:

факт

правило

закономерность

привычная реакция

Пример:

If you heat water,
it boils.""",
            },


            {
                "order": 2,
                "title":
                    "Главная формула",

                "body":
                    """Основная схема:

IF + Present Simple,
Present Simple

If you heat water,
it boils.

Условие:

you heat water

Результат:

it boils

Обе части обычно
стоят в Present Simple.""",
            },


            {
                "order": 3,
                "title":
                    "Факты и законы природы",

                "body":
                    """Zero Conditional часто
описывает факты.

If water reaches 100°C,
it boils.

If water freezes,
it becomes ice.

If plants don't get water,
they die.

Это не прогноз.

Это закономерность.""",
            },


            {
                "order": 4,
                "title":
                    "Привычные ситуации",

                "body":
                    """Можно описывать
повторяющуюся личную реакцию.

If I drink coffee late,
I can't sleep.

If she skips breakfast,
she gets hungry.

If he feels stressed,
he goes for a walk.

Речь идёт о том,
что происходит обычно.""",
            },


            {
                "order": 5,
                "title":
                    "Правила и инструкции",

                "body":
                    """Zero Conditional подходит
для правил и устройств.

If you press this button,
the machine starts.

If the battery is empty,
the phone turns off.

If students arrive late,
the teacher marks them absent.""",
            },


            {
                "order": 6,
                "title":
                    "IF и WHEN",

                "body":
                    """В Zero Conditional
IF часто можно заменить на WHEN.

If I drink coffee late,
I can't sleep.

When I drink coffee late,
I can't sleep.

IF = если это происходит

WHEN = когда это происходит.""",
            },


            {
                "order": 7,
                "title":
                    "He / She / It → -S",

                "body":
                    """В Present Simple
не забывай -S.

If she drinks coffee,
she sleeps badly.

If it rains,
the road gets wet.

Не:

If she drink...

Не:

If it rain...""",
            },


            {
                "order": 8,
                "title":
                    "Отрицание",

                "body":
                    """Используем:

DON'T + verb

DOESN'T + verb

If I don't sleep enough,
I feel tired.

If she doesn't eat,
she gets hungry.

После DOESN'T
глагол без -S.""",
            },


            {
                "order": 9,
                "title":
                    "CAN, MUST и команда",

                "body":
                    """В результате можно использовать
не только Present Simple.

CAN:

If the sky is clear,
you can see the mountains.

MUST:

If the alarm rings,
you must leave.

Imperative:

If you don't understand,
ask the teacher.""",
            },


            {
                "order": 10,
                "title":
                    "Zero vs First Conditional",

                "body":
                    """Zero Conditional:

общий факт или привычка.

If I drink coffee at night,
I can't sleep.

First Conditional:

конкретная будущая ситуация.

If I drink coffee tonight,
I won't sleep.

ZERO = всегда / обычно

FIRST = конкретное будущее.""",
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
                    "Which sentence describes a general fact?",
                "options": [
                    "If you heat ice, it melts.",
                    "If you heat this ice tomorrow, it will melt.",
                    "If you heated the ice yesterday, it melted.",
                    "If you will heat ice, it melts.",
                ],
                "answer":
                    "If you heat ice, it melts.",
                "explanation":
                    "Общий факт → Zero Conditional.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Zero Conditional usually describes...",
                "options": [
                    "facts and regular results",
                    "imaginary past situations",
                    "one future plan only",
                    "finished actions yesterday",
                ],
                "answer":
                    "facts and regular results",
                "explanation":
                    "Zero Conditional = facts, rules, habits.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "If you ___ water, it boils.",
                "options": [
                    "heat",
                    "will heat",
                    "heated",
                    "are heat",
                ],
                "answer":
                    "heat",
                "explanation":
                    "После IF → Present Simple.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "If water reaches 100°C, it ___.",
                "options": [
                    "boils",
                    "will boil tomorrow",
                    "boiled",
                    "boiling",
                ],
                "answer":
                    "boils",
                "explanation":
                    "Результат общего факта → Present Simple.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "If plants don't get water, they ___.",
                "options": [
                    "die",
                    "will die only tomorrow",
                    "died yesterday",
                    "dying",
                ],
                "answer":
                    "die",
                "explanation":
                    "Это закономерность → Present Simple.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "If water freezes, it ___ ice.",
                "options": [
                    "becomes",
                    "will become someday",
                    "became yesterday",
                    "becoming",
                ],
                "answer":
                    "becomes",
                "explanation":
                    "Научный факт → Present Simple.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "If I drink coffee late, I ___ sleep.",
                "options": [
                    "can't",
                    "won't only tonight",
                    "didn't",
                    "not can",
                ],
                "answer":
                    "can't",
                "explanation":
                    "Регулярная личная реакция.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "If she skips breakfast, she ___ hungry.",
                "options": [
                    "gets",
                    "will get tomorrow only",
                    "got",
                    "getting",
                ],
                "answer":
                    "gets",
                "explanation":
                    "Повторяющийся результат → GETS.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "If you press this button, the machine ___.",
                "options": [
                    "starts",
                    "will starting",
                    "started",
                    "start",
                ],
                "answer":
                    "starts",
                "explanation":
                    "MACHINE = it → STARTS.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "build",
                "prompt":
                    "Собери правило работы устройства.",
                "options": [
                    "If",
                    "the",
                    "battery",
                    "is",
                    "empty",
                    "the",
                    "phone",
                    "turns",
                    "off",
                ],
                "answer":
                    "If the battery is empty the phone turns off",
                "explanation":
                    "Стандартный результат → Zero Conditional.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "___ I drink coffee late, I can't sleep.",
                "options": [
                    "When",
                    "Will",
                    "Would",
                    "Did",
                ],
                "answer":
                    "When",
                "explanation":
                    "В регулярной ситуации WHEN возможно вместо IF.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "Choose the correct pair.",
                "options": [
                    "If I feel tired, I rest. / When I feel tired, I rest.",
                    "If I will feel tired, I rest. / When I will feel tired, I rest.",
                    "If I felt tired every time, I rest. / When I feeling tired, I rest.",
                    "If tired, I will always rested. / When tired, I resting.",
                ],
                "answer":
                    "If I feel tired, I rest. / When I feel tired, I rest.",
                "explanation":
                    "IF и WHEN могут описывать регулярный результат.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "If she ___ coffee late, she sleeps badly.",
                "options": [
                    "drinks",
                    "drink",
                    "will drink",
                    "drinking",
                ],
                "answer":
                    "drinks",
                "explanation":
                    "SHE → DRINKS.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "If it ___, the road gets wet.",
                "options": [
                    "rains",
                    "rain",
                    "will rain",
                    "raining",
                ],
                "answer":
                    "rains",
                "explanation":
                    "IT → RAINS.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "If I ___ enough, I feel tired.",
                "options": [
                    "don't sleep",
                    "won't sleep",
                    "doesn't sleep",
                    "not sleep",
                ],
                "answer":
                    "don't sleep",
                "explanation":
                    "I → DON'T + base verb.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "If he ___ breakfast, he gets hungry.",
                "options": [
                    "doesn't eat",
                    "don't eats",
                    "doesn't eats",
                    "won't eat always",
                ],
                "answer":
                    "doesn't eat",
                "explanation":
                    "HE → DOESN'T + base verb.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "If the alarm rings, you ___ leave.",
                "options": [
                    "must",
                    "must to",
                    "will must",
                    "musts",
                ],
                "answer":
                    "must",
                "explanation":
                    "В результате можно использовать MUST.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "If you don't understand, ___ the teacher.",
                "options": [
                    "ask",
                    "to ask",
                    "asking",
                    "asked",
                ],
                "answer":
                    "ask",
                "explanation":
                    "В результате возможен imperative.",
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
                    "If I don't sleep tonight, I'll be tired tomorrow.",
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
                    "Which sentence describes one future situation?",
                "options": [
                    "If I drink coffee tonight, I won't sleep.",
                    "If I drink coffee at night, I can't sleep.",
                    "When I drink coffee late, I can't sleep.",
                    "If people drink coffee late, they may sleep badly.",
                ],
                "answer":
                    "If I drink coffee tonight, I won't sleep.",
                "explanation":
                    "TONIGHT + WILL → конкретное будущее.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "If you mix blue and yellow, you ___ green.",
                "options": [
                    "get",
                    "will get tomorrow",
                    "got yesterday",
                    "getting",
                ],
                "answer":
                    "get",
                "explanation":
                    "Общий факт → Present Simple.",
            },

            {
                "order": 22,
                "prompt":
                    "If metal gets very hot, it ___.",
                "options": [
                    "expands",
                    "will expands",
                    "expanded",
                    "expanding",
                ],
                "answer":
                    "expands",
                "explanation":
                    "Общая закономерность → EXPANDS.",
            },

            {
                "order": 23,
                "prompt":
                    "If my phone battery is low, I ___ it.",
                "options": [
                    "charge",
                    "will charge only tomorrow",
                    "charged yesterday",
                    "charging",
                ],
                "answer":
                    "charge",
                "explanation":
                    "Привычная реакция → Present Simple.",
            },

            {
                "order": 24,
                "prompt":
                    "If she ___ enough water, she gets a headache.",
                "options": [
                    "doesn't drink",
                    "don't drink",
                    "doesn't drinks",
                    "won't drink always",
                ],
                "answer":
                    "doesn't drink",
                "explanation":
                    "SHE → DOESN'T + DRINK.",
            },

            {
                "order": 25,
                "prompt":
                    "If the weather is clear, you ___ see the mountains.",
                "options": [
                    "can",
                    "can to",
                    "will can",
                    "cans",
                ],
                "answer":
                    "can",
                "explanation":
                    "CAN можно использовать в результате.",
            },

            {
                "order": 26,
                "prompt":
                    "If the light is red, ___ the car.",
                "options": [
                    "stop",
                    "to stop",
                    "stopping",
                    "stopped",
                ],
                "answer":
                    "stop",
                "explanation":
                    "В результате возможна команда.",
            },

            {
                "order": 27,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "If he feels sick, he stays home.",
                    "If he feel sick, he stays home.",
                    "If he will feel sick, he stays home.",
                    "If he feels sick, he stay home.",
                ],
                "answer":
                    "If he feels sick, he stays home.",
                "explanation":
                    "HE → FEELS, STAYS.",
            },

            {
                "order": 28,
                "prompt":
                    "Choose the correct negative sentence.",
                "options": [
                    "If people don't exercise, they often feel worse.",
                    "If people doesn't exercise, they often feel worse.",
                    "If people don't exercises, they often feel worse.",
                    "If people won't exercise always, they feel worse.",
                ],
                "answer":
                    "If people don't exercise, they often feel worse.",
                "explanation":
                    "PEOPLE → DON'T + base verb.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct IF / WHEN pair.",
                "options": [
                    "If I am tired, I go to bed early. / When I am tired, I go to bed early.",
                    "If I will be tired, I go to bed early. / When I will be tired, I go to bed early.",
                    "If I tired, I go bed early. / When I tired, I go bed early.",
                    "If I am tiring, I will always went early. / When I tiring, I went early.",
                ],
                "answer":
                    "If I am tired, I go to bed early. / When I am tired, I go to bed early.",
                "explanation":
                    "Обе конструкции возможны для регулярной реакции.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "If water freezes, it becomes ice. / If you feel tired, rest. / If the alarm rings, you must leave.",
                    "If water will freeze, it becomes ice. / If you feel tired, to rest. / If the alarm rings, you must to leave.",
                    "If water freeze, it become ice. / If you feels tired, resting. / If the alarm ring, you musts leave.",
                    "If water froze, it will always becomes ice. / If tired, you rested. / If alarm rings, you leaving.",
                ],
                "answer":
                    "If water freezes, it becomes ice. / If you feel tired, rest. / If the alarm rings, you must leave.",
                "explanation":
                    "Zero Conditional: Present Simple condition + regular result/modal/imperative.",
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
                "✅ Interactive A1 Lesson 46 seeded"
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
