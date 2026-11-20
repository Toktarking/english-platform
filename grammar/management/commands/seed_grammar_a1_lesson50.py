from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 50: Wish / If only."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=50,
            defaults={
                "title":
                    "Wish / If only",

                "slug":
                    "wish-if-only",

                "theory_text":
                    "Wish and If only: wishes, regrets "
                    "and unreal situations.",

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
                    "Что означают WISH и IF ONLY",

                "body":
                    """WISH и IF ONLY используем,
когда хотим,
чтобы ситуация была другой.

I wish I had more time.

If only I had more time!

IF ONLY обычно звучит
сильнее и эмоциональнее.

Обе конструкции говорят
о неудовлетворённости ситуацией.""",
            },


            {
                "order": 2,
                "title":
                    "WISH о настоящем",

                "body":
                    """Если хотим изменить
ситуацию сейчас:

WISH + Past Simple

I wish I had more money.

Реальность:

I don't have much money.

She wishes she lived closer.

He wishes he knew the answer.""",
            },


            {
                "order": 3,
                "title":
                    "WISH + WERE",

                "body":
                    """С глаголом BE
в гипотетических ситуациях
часто используем WERE.

I wish I were taller.

She wishes she were here.

We wish it were warmer.

В учебных заданиях
лучше использовать WERE.""",
            },


            {
                "order": 4,
                "title":
                    "IF ONLY о настоящем",

                "body":
                    """IF ONLY использует
ту же грамматику.

IF ONLY + Past Simple

If only I had more time!

If only she lived closer!

If only we knew the answer!

IF ONLY выражает
сильное желание или сожаление.""",
            },


            {
                "order": 5,
                "title":
                    "WISH + COULD",

                "body":
                    """Если хотим иметь
способность или возможность:

WISH + COULD + V1

I wish I could drive.

She wishes she could speak French.

We wish we could travel more.

Реальность:

I can't drive.""",
            },


            {
                "order": 6,
                "title":
                    "WISH о прошлом",

                "body":
                    """Если сожалеем о прошлом:

WISH + HAD + V3

I wish I had studied harder.

Реальность:

I didn't study enough.

She wishes she had accepted the job.

We wish we had left earlier.""",
            },


            {
                "order": 7,
                "title":
                    "HADN'T + V3",

                "body":
                    """Если сожалеем
о совершённом действии:

WISH + HADN'T + V3

I wish I hadn't said that.

She wishes she hadn't left.

If only I hadn't forgotten my passport!

Прошлое уже нельзя изменить.""",
            },


            {
                "order": 8,
                "title":
                    "WISH + WOULD",

                "body":
                    """Если хотим,
чтобы кто-то или что-то изменилось:

WISH + WOULD + V1

I wish you would listen.

We wish the rain would stop.

He wishes the bus would come.

Часто это выражает
раздражение или недовольство.""",
            },


            {
                "order": 9,
                "title":
                    "WISH и HOPE",

                "body":
                    """HOPE = реальная надежда.

I hope she comes tomorrow.

I hope I pass the exam.

WISH = ситуация не такая,
как нам хочется.

I wish she were here.

I wish I had passed the exam.

HOPE → возможно

WISH → нереальность / сожаление.""",
            },


            {
                "order": 10,
                "title":
                    "Как быстро выбрать форму",

                "body":
                    """Хочу изменить настоящее:

WISH + Past Simple

Сожалею о прошлом:

WISH + HAD + V3

Хочу изменить поведение:

WISH + WOULD

Нет способности:

WISH + COULD

Реальная надежда:

HOPE.""",
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
                    "Which sentence expresses dissatisfaction with the present?",
                "options": [
                    "I wish I had more free time.",
                    "I hope I have free time tomorrow.",
                    "I had free time yesterday.",
                    "I will have free time next week.",
                ],
                "answer":
                    "I wish I had more free time.",
                "explanation":
                    "WISH говорит о ситуации, которую хотим изменить.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Which is stronger and more emotional?",
                "options": [
                    "If only I had more time!",
                    "I have more time.",
                    "I will have more time.",
                    "I had more time yesterday.",
                ],
                "answer":
                    "If only I had more time!",
                "explanation":
                    "IF ONLY обычно эмоциональнее WISH.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "I wish I ___ more money.",
                "options": [
                    "had",
                    "have",
                    "will have",
                    "would have tomorrow",
                ],
                "answer":
                    "had",
                "explanation":
                    "Нереальное настоящее → Past Simple.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "She wishes she ___ closer to work.",
                "options": [
                    "lived",
                    "lives",
                    "will live",
                    "had lived yesterday",
                ],
                "answer":
                    "lived",
                "explanation":
                    "WISH о настоящем → Past Simple.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "I wish I ___ taller.",
                "options": [
                    "were",
                    "am",
                    "will be",
                    "would be tomorrow",
                ],
                "answer":
                    "were",
                "explanation":
                    "Гипотетическое BE → WERE.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "She wishes she ___ here now.",
                "options": [
                    "were",
                    "is",
                    "will be",
                    "had been yesterday",
                ],
                "answer":
                    "were",
                "explanation":
                    "WISH о настоящем → WERE.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "If only we ___ the answer!",
                "options": [
                    "knew",
                    "know",
                    "will know",
                    "had known yesterday only",
                ],
                "answer":
                    "knew",
                "explanation":
                    "IF ONLY о настоящем → Past Simple.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "build",
                "prompt":
                    "Собери сильное желание.",
                "options": [
                    "If",
                    "only",
                    "I",
                    "had",
                    "more",
                    "time",
                ],
                "answer":
                    "If only I had more time",
                "explanation":
                    "IF ONLY + Past Simple.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "I wish I ___ drive.",
                "options": [
                    "could",
                    "can",
                    "will can",
                    "could to",
                ],
                "answer":
                    "could",
                "explanation":
                    "Нет способности сейчас → WISH + COULD.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "She wishes she ___ speak Spanish.",
                "options": [
                    "could",
                    "can",
                    "will could",
                    "could to",
                ],
                "answer":
                    "could",
                "explanation":
                    "WISH + COULD + base verb.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "I wish I ___ harder last year.",
                "options": [
                    "had studied",
                    "studied",
                    "would study",
                    "study",
                ],
                "answer":
                    "had studied",
                "explanation":
                    "Сожаление о прошлом → HAD + V3.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "We wish we ___ earlier.",
                "options": [
                    "had left",
                    "left",
                    "would leave",
                    "have left",
                ],
                "answer":
                    "had left",
                "explanation":
                    "Прошлое уже нельзя изменить → Past Perfect.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "I wish I ___ that message.",
                "options": [
                    "hadn't sent",
                    "didn't send",
                    "wouldn't send",
                    "don't send",
                ],
                "answer":
                    "hadn't sent",
                "explanation":
                    "Сожаление о совершённом прошлом действии.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "If only she ___ her passport!",
                "options": [
                    "hadn't forgotten",
                    "didn't forget",
                    "wouldn't forget yesterday",
                    "doesn't forget",
                ],
                "answer":
                    "hadn't forgotten",
                "explanation":
                    "IF ONLY + HADN'T + V3.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "I wish you ___ to me.",
                "options": [
                    "would listen",
                    "will listen",
                    "listened yesterday only",
                    "would listened",
                ],
                "answer":
                    "would listen",
                "explanation":
                    "Хотим изменить чужое поведение → WOULD.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "We wish the rain ___.",
                "options": [
                    "would stop",
                    "will stop",
                    "stopped yesterday",
                    "would stopped",
                ],
                "answer":
                    "would stop",
                "explanation":
                    "Хотим изменить внешнюю ситуацию → WISH + WOULD.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "Which sentence expresses a real future hope?",
                "options": [
                    "I hope I pass the exam.",
                    "I wish I had passed the exam.",
                    "I wish I knew the answer.",
                    "If only I had studied more.",
                ],
                "answer":
                    "I hope I pass the exam.",
                "explanation":
                    "HOPE = реальная будущая возможность.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "Which sentence expresses regret about the past?",
                "options": [
                    "I wish I had passed the exam.",
                    "I hope I pass the exam.",
                    "I will pass the exam.",
                    "I pass exams every year.",
                ],
                "answer":
                    "I wish I had passed the exam.",
                "explanation":
                    "WISH + Past Perfect = сожаление.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which form is used for present dissatisfaction?",
                "options": [
                    "wish + Past Simple",
                    "wish + will",
                    "wish + Present Simple",
                    "wish + Future Perfect",
                ],
                "answer":
                    "wish + Past Simple",
                "explanation":
                    "Настоящее → WISH + Past Simple.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which form is used for past regret?",
                "options": [
                    "wish + had + V3",
                    "wish + Present Simple",
                    "wish + will + V1",
                    "wish + am/is/are",
                ],
                "answer":
                    "wish + had + V3",
                "explanation":
                    "Прошлое сожаление → Past Perfect.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "I wish my apartment ___ bigger.",
                "options": [
                    "were",
                    "is",
                    "will be",
                    "would have been yesterday",
                ],
                "answer":
                    "were",
                "explanation":
                    "Нереальное настоящее → WERE.",
            },

            {
                "order": 22,
                "prompt":
                    "He wishes he ___ more free time.",
                "options": [
                    "had",
                    "has",
                    "will have",
                    "would have tomorrow",
                ],
                "answer":
                    "had",
                "explanation":
                    "WISH о настоящем → Past Simple.",
            },

            {
                "order": 23,
                "prompt":
                    "I wish I ___ play the piano.",
                "options": [
                    "could",
                    "can",
                    "will can",
                    "could to",
                ],
                "answer":
                    "could",
                "explanation":
                    "Нет способности → WISH + COULD.",
            },

            {
                "order": 24,
                "prompt":
                    "She wishes she ___ the offer last month.",
                "options": [
                    "had accepted",
                    "accepted",
                    "would accept",
                    "accepts",
                ],
                "answer":
                    "had accepted",
                "explanation":
                    "Сожаление о прошлом → HAD + V3.",
            },

            {
                "order": 25,
                "prompt":
                    "If only we ___ so much money!",
                "options": [
                    "hadn't spent",
                    "didn't spend",
                    "wouldn't spend yesterday",
                    "don't spend",
                ],
                "answer":
                    "hadn't spent",
                "explanation":
                    "Past regret → HADN'T + V3.",
            },

            {
                "order": 26,
                "prompt":
                    "I wish my neighbours ___ so much noise.",
                "options": [
                    "wouldn't make",
                    "won't make",
                    "didn't made",
                    "wouldn't made",
                ],
                "answer":
                    "wouldn't make",
                "explanation":
                    "Хотим изменить чужое поведение → WISH + WOULD.",
            },

            {
                "order": 27,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "I wish I knew the answer.",
                    "I wish I know the answer.",
                    "I wish I will know the answer.",
                    "I wish I knowing the answer.",
                ],
                "answer":
                    "I wish I knew the answer.",
                "explanation":
                    "Настоящее нереальное состояние → Past Simple.",
            },

            {
                "order": 28,
                "prompt":
                    "Choose the correct past regret.",
                "options": [
                    "I wish I had gone earlier.",
                    "I wish I had went earlier.",
                    "I wish I went earlier yesterday regret.",
                    "I wish I would go earlier yesterday.",
                ],
                "answer":
                    "I wish I had gone earlier.",
                "explanation":
                    "GO → GONE; после HAD нужен V3.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct WISH / HOPE pair.",
                "options": [
                    "I wish she were here now. / I hope she comes tomorrow.",
                    "I wish she is here now. / I hope she were here tomorrow.",
                    "I wish she will be here now. / I hope she had come tomorrow.",
                    "I wish she comes now. / I hope she would came tomorrow.",
                ],
                "answer":
                    "I wish she were here now. / I hope she comes tomorrow.",
                "explanation":
                    "WISH = нереальная ситуация; HOPE = реальная надежда.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "I wish I had more time. / I wish I had studied harder. / I wish he would listen. / I wish I could drive.",
                    "I wish I have more time. / I wish I studied harder yesterday. / I wish he will listen. / I wish I can drive.",
                    "I wish I would have more time. / I wish I had study harder. / I wish he would listens. / I wish I could to drive.",
                    "I wish I had had more time now. / I wish I will study harder yesterday. / I wish he listened tomorrow would. / I wish I can to drive.",
                ],
                "answer":
                    "I wish I had more time. / I wish I had studied harder. / I wish he would listen. / I wish I could drive.",
                "explanation":
                    "Present → Past Simple; past regret → Past Perfect; behaviour → WOULD; ability → COULD.",
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
                "✅ Interactive A1 Lesson 50 seeded"
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
