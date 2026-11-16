from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 44: Adjectives and Adverbs."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=44,
            defaults={
                "title":
                    "Прилагательные и наречия",

                "slug":
                    "adjectives-and-adverbs",

                "theory_text":
                    "Adjectives and Adverbs.",

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
                    "Adjective или Adverb?",

                "body":
                    """Adjective описывает
человека или предмет.

a careful driver

a beautiful city

a difficult task

Adverb обычно описывает действие.

drive carefully

speak quietly

work quickly

Коротко:

noun → adjective

verb → adverb.""",
            },


            {
                "order": 2,
                "title":
                    "CAREFUL → CAREFULLY",

                "body":
                    """Большинство наречий образуется:

adjective + LY

slow → slowly

careful → carefully

quick → quickly

quiet → quietly

Пример:

She is a careful driver.

She drives carefully.""",
            },


            {
                "order": 3,
                "title":
                    "Y меняется: EASY → EASILY",

                "body":
                    """Если adjective заканчивается на Y:

Y часто меняется на I.

easy → easily

happy → happily

angry → angrily

heavy → heavily

Пример:

The task is easy.

She completed it easily.""",
            },


            {
                "order": 4,
                "title":
                    "GOOD и WELL",

                "body":
                    """GOOD — adjective.

She is a good teacher.

The food is good.

WELL — обычно adverb.

She teaches well.

He speaks English well.

Сравни:

He is a good singer.

He sings well.""",
            },


            {
                "order": 5,
                "title":
                    "После BE нужен adjective",

                "body":
                    """После AM / IS / ARE
обычно используем adjective,
когда описываем подлежащее.

She is happy.

He is tired.

The room is quiet.

Не:

She is happily.

He is carefully.""",
            },


            {
                "order": 6,
                "title":
                    "LOOK, FEEL, SOUND, TASTE",

                "body":
                    """После некоторых глаголов
часто используется adjective.

look

feel

sound

smell

taste

Примеры:

You look tired.

She feels nervous.

That sounds interesting.

The soup tastes good.""",
            },


            {
                "order": 7,
                "title":
                    "FAST, HARD, LATE, EARLY",

                "body":
                    """Некоторые adverbs
не получают -LY.

fast:

a fast car

drive fast

hard:

a hard job

work hard

late:

a late train

arrive late

early:

an early meeting

arrive early.""",
            },


            {
                "order": 8,
                "title":
                    "HARD и HARDLY",

                "body":
                    """HARD и HARDLY —
не одно и то же.

He works hard.

→ он усердно работает.

He hardly works.

→ он почти не работает.

То есть:

hard = усердно

hardly = едва / почти не.""",
            },


            {
                "order": 9,
                "title":
                    "TOO и ENOUGH",

                "body":
                    """TOO означает:

слишком.

too expensive

too slowly

ENOUGH после adjective/adverb:

old enough

fast enough

quickly enough

Но перед noun:

enough time

enough money.""",
            },


            {
                "order": 10,
                "title":
                    "SO и SUCH",

                "body":
                    """SO используется
перед adjective или adverb.

so beautiful

so quickly

SUCH используется
с существительным.

such a beautiful city

such an interesting book

Сравни:

The book is so interesting.

It is such an interesting book.""",
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

            section_objects[data["order"]] = section


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
                    "He is a very ___ driver.",
                "options": [
                    "careful",
                    "carefully",
                    "care",
                    "caringly",
                ],
                "answer":
                    "careful",
                "explanation":
                    "DRIVER — noun, поэтому нужен adjective.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "He drives very ___.",
                "options": [
                    "carefully",
                    "careful",
                    "care",
                    "carefulness",
                ],
                "answer":
                    "carefully",
                "explanation":
                    "DRIVES — действие, поэтому нужен adverb.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "The baby is sleeping ___.",
                "options": [
                    "quietly",
                    "quiet",
                    "quietness",
                    "quieter",
                ],
                "answer":
                    "quietly",
                "explanation":
                    "SLEEPING описывается наречием QUIETLY.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "She answered the question ___.",
                "options": [
                    "correctly",
                    "correct",
                    "correction",
                    "correcting",
                ],
                "answer":
                    "correctly",
                "explanation":
                    "ANSWERED → действие → CORRECTLY.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "She completed the task ___.",
                "options": [
                    "easily",
                    "easy",
                    "easyly",
                    "easier",
                ],
                "answer":
                    "easily",
                "explanation":
                    "EASY → EASILY.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "The children played ___.",
                "options": [
                    "happily",
                    "happy",
                    "happyly",
                    "happier",
                ],
                "answer":
                    "happily",
                "explanation":
                    "HAPPY → HAPPILY.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "She is a ___ teacher.",
                "options": [
                    "good",
                    "well",
                    "goodly",
                    "betterly",
                ],
                "answer":
                    "good",
                "explanation":
                    "TEACHER — noun → GOOD.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "She teaches English very ___.",
                "options": [
                    "well",
                    "good",
                    "goodly",
                    "bestly",
                ],
                "answer":
                    "well",
                "explanation":
                    "TEACHES — действие → WELL.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "The room is very ___.",
                "options": [
                    "quiet",
                    "quietly",
                    "quietness",
                    "quieterly",
                ],
                "answer":
                    "quiet",
                "explanation":
                    "После IS для описания комнаты → adjective.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "She is ___.",
                "options": [
                    "happy",
                    "happily",
                    "happiness",
                    "happyly",
                ],
                "answer":
                    "happy",
                "explanation":
                    "После BE используется adjective.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "You look ___ today.",
                "options": [
                    "tired",
                    "tiredly",
                    "tiringly",
                    "tire",
                ],
                "answer":
                    "tired",
                "explanation":
                    "LOOK + adjective.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "The soup tastes ___.",
                "options": [
                    "delicious",
                    "deliciously",
                    "delightfully taste",
                    "deliciousness",
                ],
                "answer":
                    "delicious",
                "explanation":
                    "После TASTE для описания качества → adjective.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "He can run very ___.",
                "options": [
                    "fast",
                    "fastly",
                    "fastness",
                    "fasterly",
                ],
                "answer":
                    "fast",
                "explanation":
                    "FAST может быть и adjective, и adverb.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "She arrived ___.",
                "options": [
                    "late",
                    "lately",
                    "lately yesterday",
                    "latefully",
                ],
                "answer":
                    "late",
                "explanation":
                    "ARRIVE LATE = прибыть поздно.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "She works very ___.",
                "options": [
                    "hard",
                    "hardly",
                    "hardly meaning diligently",
                    "hardlyly",
                ],
                "answer":
                    "hard",
                "explanation":
                    "WORK HARD = работать усердно.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "I can ___ hear you.",
                "options": [
                    "hardly",
                    "hard",
                    "harder",
                    "hardest",
                ],
                "answer":
                    "hardly",
                "explanation":
                    "HARDLY = едва / почти не.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "This bag is ___ heavy for me.",
                "options": [
                    "too",
                    "enough",
                    "very enough",
                    "such",
                ],
                "answer":
                    "too",
                "explanation":
                    "TOO HEAVY = слишком тяжёлый.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "He is old ___ to drive.",
                "options": [
                    "enough",
                    "too",
                    "very",
                    "such",
                ],
                "answer":
                    "enough",
                "explanation":
                    "Adjective + ENOUGH.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "The film was ___ interesting.",
                "options": [
                    "so",
                    "such",
                    "such an",
                    "enough",
                ],
                "answer":
                    "so",
                "explanation":
                    "SO + adjective.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "It was ___ interesting film.",
                "options": [
                    "such an",
                    "so",
                    "so an",
                    "such",
                ],
                "answer":
                    "such an",
                "explanation":
                    "SUCH + article + adjective + noun.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "The manager spoke very ___.",
                "options": [
                    "clearly",
                    "clear",
                    "clearness",
                    "clearer",
                ],
                "answer":
                    "clearly",
                "explanation":
                    "SPOKE — действие → adverb.",
            },

            {
                "order": 22,
                "prompt":
                    "This is a very ___ explanation.",
                "options": [
                    "clear",
                    "clearly",
                    "clearness",
                    "clearly explained",
                ],
                "answer":
                    "clear",
                "explanation":
                    "EXPLANATION — noun → adjective.",
            },

            {
                "order": 23,
                "prompt":
                    "The students completed the test ___.",
                "options": [
                    "quickly",
                    "quick",
                    "quickness",
                    "quicker adjective",
                ],
                "answer":
                    "quickly",
                "explanation":
                    "COMPLETED → действие → QUICKLY.",
            },

            {
                "order": 24,
                "prompt":
                    "The music sounds ___.",
                "options": [
                    "beautiful",
                    "beautifully",
                    "beauty",
                    "beautifuller",
                ],
                "answer":
                    "beautiful",
                "explanation":
                    "SOUND + adjective.",
            },

            {
                "order": 25,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "He speaks English well.",
                    "He speaks English good.",
                    "He speaks English goodly.",
                    "He well English speaks.",
                ],
                "answer":
                    "He speaks English well.",
                "explanation":
                    "GOOD — adjective; WELL — adverb.",
            },

            {
                "order": 26,
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "They worked hard all day.",
                    "They worked hardly all day.",
                    "They hard worked all day.",
                    "They worked hardily all day.",
                ],
                "answer":
                    "They worked hard all day.",
                "explanation":
                    "WORK HARD = работать усердно.",
            },

            {
                "order": 27,
                "prompt":
                    "The car isn't fast ___.",
                "options": [
                    "enough",
                    "too",
                    "such",
                    "very enough",
                ],
                "answer":
                    "enough",
                "explanation":
                    "Adjective + ENOUGH.",
            },

            {
                "order": 28,
                "prompt":
                    "The task was ___ difficult for me.",
                "options": [
                    "too",
                    "enough",
                    "such a",
                    "hardly",
                ],
                "answer":
                    "too",
                "explanation":
                    "TOO DIFFICULT = слишком сложно.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct SO / SUCH pair.",
                "options": [
                    "She is so friendly. / She is such a friendly person.",
                    "She is such friendly. / She is so a friendly person.",
                    "She is so a friendly. / She is such friendly person.",
                    "She is such so friendly. / She is a so friendly person.",
                ],
                "answer":
                    "She is so friendly. / She is such a friendly person.",
                "explanation":
                    "SO + adjective; SUCH + a/an + adjective + noun.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "careful → carefully / easy → easily / good → well / fast → fast / hard → hard",
                    "careful → carefuly / easy → easyly / good → goodly / fast → fastly / hard → hardly",
                    "careful → carely / easy → easilly / good → betterly / fast → quickly fast / hard → hardily",
                    "careful → carefullyly / easy → easilyly / good → wellly / fast → fastestly / hard → hardestly",
                ],
                "answer":
                    "careful → carefully / easy → easily / good → well / fast → fast / hard → hard",
                "explanation":
                    "Это правильные формы adjective → adverb.",
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
                "✅ Interactive A1 Lesson 44 seeded"
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
