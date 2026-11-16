from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 39: Future Continuous and Future Perfect."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=39,
            defaults={
                "title":
                    "Future Continuous и Future Perfect",

                "slug":
                    "future-continuous-future-perfect",

                "theory_text":
                    "Future Continuous and Future Perfect.",

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
                    "Future Continuous: процесс в будущем",

                "body":
                    """Future Continuous показывает процесс,
который будет происходить
в определённый момент будущего.

At six tomorrow,
I will be working.

В шесть часов действие
будет в процессе.

Главная идея:

что будет происходить
в конкретный будущий момент?""",
            },


            {
                "order": 2,
                "title":
                    "Формула WILL BE + -ING",

                "body":
                    """Формула:

WILL + BE + verb-ing

I will be working.

She will be studying.

They will be travelling.

После WILL всегда:

BE

а затем:

verb-ing.

Не:

will working

will be work.""",
            },


            {
                "order": 3,
                "title":
                    "Маркеры Future Continuous",

                "body":
                    """Часто используются:

at six tomorrow

this time tomorrow

this time next week

all evening tomorrow

Примеры:

This time tomorrow,
we will be flying to Astana.

At ten,
she will be taking her exam.""",
            },


            {
                "order": 4,
                "title":
                    "Вежливый вопрос о планах",

                "body":
                    """Future Continuous можно использовать,
чтобы нейтрально спросить
о чьих-то планах.

Will you be using
the car tonight?

Will you be coming
to the meeting?

Will she be staying
for dinner?

Это звучит мягче,
чем прямой вопрос о решении.""",
            },


            {
                "order": 5,
                "title":
                    "Отрицание и вопросы",

                "body":
                    """Отрицание:

WON'T BE + verb-ing

I won't be working tomorrow.

Вопрос:

WILL + subject + BE + verb-ing?

Will you be working?

Краткий ответ:

Yes, I will.

No, I won't.""",
            },


            {
                "order": 6,
                "title":
                    "Future Perfect: результат к моменту",

                "body":
                    """Future Perfect показывает,
что действие уже завершится
к определённому моменту будущего.

By six,
I will have finished the report.

К шести отчёт уже будет готов.

Главная идея:

что уже будет сделано
к определённому сроку?""",
            },


            {
                "order": 7,
                "title":
                    "Формула WILL HAVE + V3",

                "body":
                    """Формула:

WILL + HAVE + V3

I will have finished.

She will have arrived.

They will have left.

После WILL HAVE
нужна третья форма.

go → gone

see → seen

write → written

Не:

will have went

will have wrote.""",
            },


            {
                "order": 8,
                "title":
                    "BY и BY THE TIME",

                "body":
                    """BY показывает крайний срок.

by six

by Friday

by next week

I will have finished
by six.

BY THE TIME:

By the time you arrive,
I will have finished.

После BY THE TIME
для будущего используем
Present Simple:

you arrive

не:

you will arrive.""",
            },


            {
                "order": 9,
                "title":
                    "Количество к будущему сроку",

                "body":
                    """Future Perfect может показывать,
сколько будет сделано
к определённому моменту.

By Friday,
I will have written ten pages.

By the end of the month,
she will have read four books.

То есть:

готовый результат
или количество
→ Future Perfect.""",
            },


            {
                "order": 10,
                "title":
                    "AT или BY?",

                "body":
                    """Очень важное различие:

AT → процесс в момент.

At six,
I will be writing the report.

BY → результат к моменту.

By six,
I will have written the report.

Запомни:

AT → Future Continuous

BY → Future Perfect.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects.update_or_create(
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
                    "At eight tomorrow, I ___ dinner.",
                "options": [
                    "will be cooking",
                    "will have cooked by eight",
                    "will cooking",
                    "cook yesterday",
                ],
                "answer":
                    "will be cooking",
                "explanation":
                    "AT EIGHT → процесс в конкретный будущий момент.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "This time tomorrow, we ___ to Almaty.",
                "options": [
                    "will be travelling",
                    "will have travelled by then",
                    "will travelling",
                    "travelled",
                ],
                "answer":
                    "will be travelling",
                "explanation":
                    "THIS TIME TOMORROW → Future Continuous.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "build",
                "prompt":
                    "Собери Future Continuous.",
                "options": [
                    "She",
                    "will",
                    "be",
                    "studying",
                ],
                "answer":
                    "She will be studying",
                "explanation":
                    "WILL + BE + verb-ing.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "They will be working.",
                    "They will working.",
                    "They will be work.",
                    "They will been working.",
                ],
                "answer":
                    "They will be working.",
                "explanation":
                    "Future Continuous = WILL BE + verb-ing.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "This time next week, she ___ in Dubai.",
                "options": [
                    "will be staying",
                    "will have stayed by then",
                    "will staying",
                    "stayed",
                ],
                "answer":
                    "will be staying",
                "explanation":
                    "THIS TIME NEXT WEEK показывает процесс.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "At ten tomorrow, they ___ the exam.",
                "options": [
                    "will be taking",
                    "will have taken by ten",
                    "will taking",
                    "take yesterday",
                ],
                "answer":
                    "will be taking",
                "explanation":
                    "AT TEN → действие будет происходить в этот момент.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "___ you be using the car tonight?",
                "options": [
                    "Will",
                    "Do",
                    "Are",
                    "Have",
                ],
                "answer":
                    "Will",
                "explanation":
                    "Вопрос Future Continuous начинается с WILL.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "Choose the polite question about someone's plans.",
                "options": [
                    "Will you be coming to the meeting?",
                    "Do you coming to the meeting?",
                    "Will you coming to the meeting?",
                    "Are you be coming to the meeting?",
                ],
                "answer":
                    "Will you be coming to the meeting?",
                "explanation":
                    "WILL + subject + BE + verb-ing.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "She ___ be working tomorrow.",
                "options": [
                    "won't",
                    "doesn't",
                    "isn't will",
                    "not will",
                ],
                "answer":
                    "won't",
                "explanation":
                    "Отрицание → WON'T BE + verb-ing.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "Will he be studying at six?",
                "options": [
                    "Yes, he will.",
                    "Yes, he is.",
                    "Yes, he does.",
                    "Yes, he has.",
                ],
                "answer":
                    "Yes, he will.",
                "explanation":
                    "Краткий ответ повторяет WILL.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "By six, I ___ the report.",
                "options": [
                    "will have finished",
                    "will be finishing at six",
                    "will has finished",
                    "will have finish",
                ],
                "answer":
                    "will have finished",
                "explanation":
                    "BY SIX → готовый результат к сроку.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "By Monday, she ___ home.",
                "options": [
                    "will have returned",
                    "will be returning at Monday",
                    "will has returned",
                    "will have return",
                ],
                "answer":
                    "will have returned",
                "explanation":
                    "Действие завершится к понедельнику.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "He will have ___ the email by then.",
                "options": [
                    "written",
                    "wrote",
                    "write",
                    "writing",
                ],
                "answer":
                    "written",
                "explanation":
                    "WRITE → WROTE → WRITTEN.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "fill",
                "prompt":
                    "go → went → ___",
                "options": [],
                "answer":
                    "gone",
                "explanation":
                    "После WILL HAVE нужна V3: GONE.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "I will have finished the work ___ Friday.",
                "options": [
                    "by",
                    "at",
                    "since",
                    "for",
                ],
                "answer":
                    "by",
                "explanation":
                    "BY показывает крайний срок.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "By the time you ___, I will have finished.",
                "options": [
                    "arrive",
                    "will arrive",
                    "arrived",
                    "arriving",
                ],
                "answer":
                    "arrive",
                "explanation":
                    "После BY THE TIME → Present Simple.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "By Friday, she ___ ten pages.",
                "options": [
                    "will have written",
                    "will be writing at Friday",
                    "will have wrote",
                    "will writing",
                ],
                "answer":
                    "will have written",
                "explanation":
                    "TEN PAGES → количество готового результата.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "By next month, they ___ three projects.",
                "options": [
                    "will have completed",
                    "will be completing at that moment",
                    "will has completed",
                    "will complete yesterday",
                ],
                "answer":
                    "will have completed",
                "explanation":
                    "Количество завершённых результатов → Future Perfect.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "At six, I ___ the report.",
                "options": [
                    "will be writing",
                    "will have written by six",
                    "will writing",
                    "will have write",
                ],
                "answer":
                    "will be writing",
                "explanation":
                    "AT SIX → процесс.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "By six, I ___ the report.",
                "options": [
                    "will have written",
                    "will be writing at six",
                    "will has written",
                    "will have wrote",
                ],
                "answer":
                    "will have written",
                "explanation":
                    "BY SIX → результат.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "At this time tomorrow, Tom ___ to work.",
                "options": [
                    "will be driving",
                    "will have driven by then",
                    "will driving",
                    "drives yesterday",
                ],
                "answer":
                    "will be driving",
                "explanation":
                    "Процесс в конкретный будущий момент → Future Continuous.",
            },

            {
                "order": 22,
                "prompt":
                    "At nine tonight, we ___ dinner.",
                "options": [
                    "will be having",
                    "will have had by nine",
                    "will having",
                    "have yesterday",
                ],
                "answer":
                    "will be having",
                "explanation":
                    "AT NINE → процесс в этот момент.",
            },

            {
                "order": 23,
                "prompt":
                    "Choose the correct Future Continuous question.",
                "options": [
                    "Will she be working tomorrow?",
                    "Will she working tomorrow?",
                    "Does she be working tomorrow?",
                    "Will she be work tomorrow?",
                ],
                "answer":
                    "Will she be working tomorrow?",
                "explanation":
                    "WILL + subject + BE + verb-ing.",
            },

            {
                "order": 24,
                "prompt":
                    "By tomorrow morning, I ___ the presentation.",
                "options": [
                    "will have prepared",
                    "will be preparing at morning",
                    "will have prepare",
                    "will has prepared",
                ],
                "answer":
                    "will have prepared",
                "explanation":
                    "BY TOMORROW MORNING → результат к сроку.",
            },

            {
                "order": 25,
                "prompt":
                    "By next year, she ___ university.",
                "options": [
                    "will have finished",
                    "will be finishing at every moment",
                    "will have finish",
                    "will finished",
                ],
                "answer":
                    "will have finished",
                "explanation":
                    "Завершённый результат к будущему сроку → Future Perfect.",
            },

            {
                "order": 26,
                "prompt":
                    "Choose the correct form of SEE after WILL HAVE.",
                "options": [
                    "seen",
                    "saw",
                    "see",
                    "seeing",
                ],
                "answer":
                    "seen",
                "explanation":
                    "SEE → SAW → SEEN.",
            },

            {
                "order": 27,
                "prompt":
                    "By the time the lesson ___, we will have finished the test.",
                "options": [
                    "ends",
                    "will end",
                    "ended yesterday",
                    "ending",
                ],
                "answer":
                    "ends",
                "explanation":
                    "После BY THE TIME для будущего → Present Simple.",
            },

            {
                "order": 28,
                "prompt":
                    "How many books ___ she ___ by the end of the year?",
                "options": [
                    "will / have read",
                    "will / be reading",
                    "does / read",
                    "has / read tomorrow",
                ],
                "answer":
                    "will / have read",
                "explanation":
                    "Количество результата к сроку → Future Perfect.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct comparison.",
                "options": [
                    "At seven, she will be cooking. / By seven, she will have cooked dinner.",
                    "At seven, she will have cooking. / By seven, she will be cooked.",
                    "At seven, she will cooking. / By seven, she will has cooked.",
                    "At seven, she cooks yesterday. / By seven, she has cooking.",
                ],
                "answer":
                    "At seven, she will be cooking. / By seven, she will have cooked dinner.",
                "explanation":
                    "AT → процесс; BY → готовый результат.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct pair.",
                "options": [
                    "This time tomorrow, I will be flying. / By tomorrow evening, I will have arrived.",
                    "This time tomorrow, I will flying. / By tomorrow evening, I will have arrive.",
                    "This time tomorrow, I will have flying. / By tomorrow evening, I will arrived.",
                    "This time tomorrow, I flying. / By tomorrow evening, I have arrived tomorrow.",
                ],
                "answer":
                    "This time tomorrow, I will be flying. / By tomorrow evening, I will have arrived.",
                "explanation":
                    "Процесс → Future Continuous; результат к сроку → Future Perfect.",
            },

        ]


        all_exercises = training + final_test

        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

            if data["order"] <= 20:
                section = section_objects[data["section"]]
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
                "✅ Interactive A1 Lesson 39 seeded"
            )
        )

        self.stdout.write(
            f"Micro rules: {lesson.sections.count()}"
        )

        self.stdout.write(
            "Training exercises: "
            f"{lesson.exercises.filter(section__isnull=False).count()}"
        )

        self.stdout.write(
            "Final test: "
            f"{lesson.exercises.filter(section__isnull=True).count()}"
        )
