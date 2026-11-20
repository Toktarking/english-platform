from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 48: Second Conditional."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=48,
            defaults={
                "title":
                    "Second Conditional",

                "slug":
                    "second-conditional",

                "theory_text":
                    "Second Conditional: "
                    "If + Past Simple, would + V1.",

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
                    "Когда нужен Second Conditional",

                "body":
                    """Second Conditional используем,
когда ситуация:

нереальна сейчас;

маловероятна в будущем;

воображаемая;

гипотетическая.

Пример:

If I had more money,
I would travel more.

Сейчас денег недостаточно.""",
            },


            {
                "order": 2,
                "title":
                    "Главная формула",

                "body":
                    """Основная схема:

IF + Past Simple,
WOULD + V1

If I had more time,
I would read more.

Условие:

I had more time

Результат:

I would read more.""",
            },


            {
                "order": 3,
                "title":
                    "Past Simple здесь не про прошлое",

                "body":
                    """В Second Conditional
Past Simple часто
не означает прошлое.

If I knew the answer,
I would tell you.

Реальность сейчас:

I don't know the answer.

Past Simple здесь показывает,
что ситуация нереальна.""",
            },


            {
                "order": 4,
                "title":
                    "Маловероятное будущее",

                "body":
                    """Second Conditional может говорить
о маловероятном будущем.

If I won the lottery,
I would buy a house.

Выиграть возможно,
но вероятность небольшая.

If they invited me,
I would go.""",
            },


            {
                "order": 5,
                "title":
                    "Отрицание",

                "body":
                    """В IF-части:

DIDN'T + V1

If I didn't work so much,
I would have more free time.

В результате:

WOULDN'T + V1

If I were you,
I wouldn't buy it.

После DIDN'T
глагол без -ED.""",
            },


            {
                "order": 6,
                "title":
                    "IF I WERE",

                "body":
                    """В гипотетических ситуациях
часто используем WERE.

If I were rich,
I would travel.

If she were here,
she would help us.

Особенно важно:

If I were you...

В учебных заданиях
используем WERE.""",
            },


            {
                "order": 7,
                "title":
                    "IF I WERE YOU",

                "body":
                    """Очень частая конструкция
для совета:

If I were you,
I would...

Примеры:

If I were you,
I would see a doctor.

If I were you,
I would study more.

If I were you,
I wouldn't do that.""",
            },


            {
                "order": 8,
                "title":
                    "COULD вместо WOULD",

                "body":
                    """COULD показывает возможность.

If I had more time,
I could learn Spanish.

WOULD:

что я бы сделал.

If I had more money,
I would buy a car.

COULD:

что было бы возможно.

If I had more money,
I could buy a car.""",
            },


            {
                "order": 9,
                "title":
                    "MIGHT вместо WOULD",

                "body":
                    """MIGHT показывает
менее уверенный результат.

If I had more free time,
I might start a new hobby.

If she invited him,
he might come.

После MIGHT:

обычная форма глагола.

might come

не:

might to come.""",
            },


            {
                "order": 10,
                "title":
                    "First vs Second Conditional",

                "body":
                    """First Conditional:

реальная возможность.

If I have enough money,
I will buy a car.

Second Conditional:

гипотетическая ситуация.

If I had enough money,
I would buy a car.

FIRST = реально возможно

SECOND = воображаемо / маловероятно.""",
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
                    "Which sentence is hypothetical?",
                "options": [
                    "If I had a private plane, I would travel every week.",
                    "If I have time tomorrow, I will call you.",
                    "If water freezes, it becomes ice.",
                    "I travelled last week.",
                ],
                "answer":
                    "If I had a private plane, I would travel every week.",
                "explanation":
                    "Воображаемая ситуация → Second Conditional.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Second Conditional usually describes...",
                "options": [
                    "unreal or unlikely situations",
                    "general facts only",
                    "finished past actions",
                    "certain future plans",
                ],
                "answer":
                    "unreal or unlikely situations",
                "explanation":
                    "Second Conditional = unreal / unlikely.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "If I ___ more money, I would travel.",
                "options": [
                    "had",
                    "have",
                    "will have",
                    "would have",
                ],
                "answer":
                    "had",
                "explanation":
                    "После IF → Past Simple.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "If she lived closer, we ___ her more often.",
                "options": [
                    "would visit",
                    "will visit",
                    "visited yesterday",
                    "would visited",
                ],
                "answer":
                    "would visit",
                "explanation":
                    "Результат → WOULD + V1.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "If I knew the answer, I ___ you.",
                "options": [
                    "would tell",
                    "will tell",
                    "told",
                    "would told",
                ],
                "answer":
                    "would tell",
                "explanation":
                    "Сейчас я не знаю ответ → unreal present.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "If he spoke English better, he ___ for that job.",
                "options": [
                    "would apply",
                    "will apply",
                    "applies every day",
                    "would applied",
                ],
                "answer":
                    "would apply",
                "explanation":
                    "Гипотетическое настоящее → WOULD + V1.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "If I ___ the lottery, I would buy a house.",
                "options": [
                    "won",
                    "win",
                    "will win",
                    "would win",
                ],
                "answer":
                    "won",
                "explanation":
                    "Маловероятное будущее → Past Simple.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "If they invited me, I ___ to the party.",
                "options": [
                    "would go",
                    "will go",
                    "went",
                    "would went",
                ],
                "answer":
                    "would go",
                "explanation":
                    "Результат гипотетической ситуации → WOULD GO.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "If she ___ so much, she would have more time.",
                "options": [
                    "didn't work",
                    "didn't worked",
                    "wouldn't work",
                    "doesn't worked",
                ],
                "answer":
                    "didn't work",
                "explanation":
                    "DIDN'T + base verb.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "If I were you, I ___ buy that car.",
                "options": [
                    "wouldn't",
                    "won't",
                    "didn't",
                    "wouldn't to",
                ],
                "answer":
                    "wouldn't",
                "explanation":
                    "Отрицательный результат → WOULDN'T + V1.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "If I ___ rich, I would travel the world.",
                "options": [
                    "were",
                    "am",
                    "will be",
                    "would be",
                ],
                "answer":
                    "were",
                "explanation":
                    "Стандартная гипотетическая форма → IF I WERE.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "If she ___ here, she would know what to do.",
                "options": [
                    "were",
                    "is",
                    "will be",
                    "would be",
                ],
                "answer":
                    "were",
                "explanation":
                    "Гипотетическое состояние → WERE.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "If I were you, I ___ to the manager.",
                "options": [
                    "would talk",
                    "will talk",
                    "talked",
                    "would talked",
                ],
                "answer":
                    "would talk",
                "explanation":
                    "If I were you → совет.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "build",
                "prompt":
                    "Собери совет.",
                "options": [
                    "If",
                    "I",
                    "were",
                    "you",
                    "I",
                    "would",
                    "rest",
                ],
                "answer":
                    "If I were you I would rest",
                "explanation":
                    "Стандартная модель совета.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "If I had more free time, I ___ learn another language.",
                "options": [
                    "could",
                    "will can",
                    "could to",
                    "can yesterday",
                ],
                "answer":
                    "could",
                "explanation":
                    "COULD = гипотетическая возможность.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "If we lived closer, we ___ visit you more often.",
                "options": [
                    "could",
                    "will can",
                    "could to",
                    "cans",
                ],
                "answer":
                    "could",
                "explanation":
                    "COULD + base verb.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "If the weather were better, we ___ go for a walk.",
                "options": [
                    "might",
                    "will might",
                    "might to",
                    "mights",
                ],
                "answer":
                    "might",
                "explanation":
                    "MIGHT показывает менее уверенный результат.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "If he had more time, he ___ start a new hobby.",
                "options": [
                    "might",
                    "might to",
                    "will might",
                    "mighted",
                ],
                "answer":
                    "might",
                "explanation":
                    "После MIGHT → base verb.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which is First Conditional?",
                "options": [
                    "If I have enough money, I will buy the laptop.",
                    "If I had enough money, I would buy the laptop.",
                    "If I were rich, I would buy ten laptops.",
                    "If I had known, I would have bought it.",
                ],
                "answer":
                    "If I have enough money, I will buy the laptop.",
                "explanation":
                    "Реальная будущая возможность → First Conditional.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which is Second Conditional?",
                "options": [
                    "If I had more free time, I would travel more.",
                    "If I have time tomorrow, I will travel.",
                    "If people exercise, they feel better.",
                    "If I travelled yesterday, I was tired.",
                ],
                "answer":
                    "If I had more free time, I would travel more.",
                "explanation":
                    "Гипотетическая ситуация → Second Conditional.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "If I ___ a bigger apartment, I would invite more friends.",
                "options": [
                    "had",
                    "have",
                    "will have",
                    "would have",
                ],
                "answer":
                    "had",
                "explanation":
                    "Second Conditional → IF + Past Simple.",
            },

            {
                "order": 22,
                "prompt":
                    "If she knew his number, she ___ him.",
                "options": [
                    "would call",
                    "will call",
                    "called yesterday",
                    "would called",
                ],
                "answer":
                    "would call",
                "explanation":
                    "Результат → WOULD + V1.",
            },

            {
                "order": 23,
                "prompt":
                    "If we ___ in another country, we would learn the language faster.",
                "options": [
                    "lived",
                    "live",
                    "will live",
                    "would live",
                ],
                "answer":
                    "lived",
                "explanation":
                    "Гипотетическая ситуация → Past Simple.",
            },

            {
                "order": 24,
                "prompt":
                    "If he didn't spend so much money, he ___ more.",
                "options": [
                    "would save",
                    "will save",
                    "saved",
                    "would saved",
                ],
                "answer":
                    "would save",
                "explanation":
                    "WOULD + base verb.",
            },

            {
                "order": 25,
                "prompt":
                    "If I ___ you, I wouldn't accept that offer.",
                "options": [
                    "were",
                    "am",
                    "will be",
                    "would be",
                ],
                "answer":
                    "were",
                "explanation":
                    "Совет → IF I WERE YOU.",
            },

            {
                "order": 26,
                "prompt":
                    "If she had more experience, she ___ get a better job.",
                "options": [
                    "could",
                    "will can",
                    "could to",
                    "can yesterday",
                ],
                "answer":
                    "could",
                "explanation":
                    "COULD показывает возможность.",
            },

            {
                "order": 27,
                "prompt":
                    "If they invited him, he ___ come.",
                "options": [
                    "might",
                    "will might",
                    "might to",
                    "mights",
                ],
                "answer":
                    "might",
                "explanation":
                    "MIGHT = менее уверенный результат.",
            },

            {
                "order": 28,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "If I knew the answer, I would tell you.",
                    "If I would know the answer, I would tell you.",
                    "If I know the answer, I would tell you.",
                    "If I knew the answer, I will tell you.",
                ],
                "answer":
                    "If I knew the answer, I would tell you.",
                "explanation":
                    "IF + Past Simple, WOULD + V1.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct First / Second Conditional pair.",
                "options": [
                    "If she studies, she will pass. / If she studied more, she would pass.",
                    "If she will study, she will pass. / If she would study, she would pass.",
                    "If she studied, she will pass. / If she studies, she would pass.",
                    "If she study, she will pass. / If she studied, she would to pass.",
                ],
                "answer":
                    "If she studies, she will pass. / If she studied more, she would pass.",
                "explanation":
                    "First = real possibility; Second = hypothetical situation.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "If I had time, I would help. / If I had more money, I could travel. / If I were you, I would rest.",
                    "If I would have time, I would help. / If I had money, I could to travel. / If I was you, I will rest.",
                    "If I have time, I would help. / If I had money, I will can travel. / If I would be you, I would rest.",
                    "If I had time, I would to help. / If I had money, I could travelled. / If I were you, I would resting.",
                ],
                "answer":
                    "If I had time, I would help. / If I had more money, I could travel. / If I were you, I would rest.",
                "explanation":
                    "Second Conditional использует Past Simple + would/could + V1.",
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
                "✅ Interactive A1 Lesson 48 seeded"
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
