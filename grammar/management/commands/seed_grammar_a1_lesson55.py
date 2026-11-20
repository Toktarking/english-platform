from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 55: Word Formation."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=55,
            defaults={
                "title":
                    "Словообразование в английском языке",

                "slug":
                    "word-formation",

                "theory_text":
                    "Word Formation: nouns, adjectives, "
                    "adverbs, prefixes and word families.",

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
                    "Word Families",

                "body":
                    """Одно слово может иметь
несколько форм.

success — noun

successful — adjective

successfully — adverb

succeed — verb

Пример:

The project was a success.

It was successful.

They completed it successfully.

Главное — выбрать форму,
которая нужна в предложении.""",
            },


            {
                "order": 2,
                "title":
                    "Как узнать NOUN",

                "body":
                    """Noun часто стоит после:

a / an / the

my / your / his

adjective

preposition

Примеры:

an important decision

economic development

a good education

После adjective часто
нужно существительное.

DECIDE
→ decision""",
            },


            {
                "order": 3,
                "title":
                    "Noun suffixes",

                "body":
                    """Частые окончания nouns:

-tion

-ment

-ness

-er

-or

-ity

Примеры:

educate → education

develop → development

happy → happiness

teach → teacher

act → actor

possible → possibility""",
            },


            {
                "order": 4,
                "title":
                    "Как узнать ADJECTIVE",

                "body":
                    """Adjective описывает noun.

a successful company

an important decision

Adjective также часто
стоит после BE.

The task is difficult.

The service was excellent.

Подсказка:

перед noun
или после BE
часто нужен adjective.""",
            },


            {
                "order": 5,
                "title":
                    "Adjective suffixes",

                "body":
                    """Частые окончания adjectives:

-ful

-less

-able

-ous

-al

-ive

-y

Примеры:

help → helpful

care → careful

use → useful

danger → dangerous

culture → cultural

effect → effective

rain → rainy""",
            },


            {
                "order": 6,
                "title":
                    "Как узнать ADVERB",

                "body":
                    """Adverb описывает действие.

She answered correctly.

He worked carefully.

They finished quickly.

Часто:

adjective + LY

careful → carefully

quick → quickly

correct → correctly

easy → easily

Если слово описывает
КАК выполнено действие,
часто нужен adverb.""",
            },


            {
                "order": 7,
                "title":
                    "Negative prefixes",

                "body":
                    """Чтобы сделать значение
отрицательным, часто используем:

un-

in-

im-

il-

ir-

dis-

Примеры:

happy → unhappy

correct → incorrect

possible → impossible

legal → illegal

regular → irregular

honest → dishonest

Форма зависит от слова.""",
            },


            {
                "order": 8,
                "title":
                    "RE-, MIS-, OVER-, UNDER-",

                "body":
                    """Другие полезные prefixes:

RE- = снова

write → rewrite

MIS- = неправильно

understand → misunderstand

OVER- = слишком

work → overwork

UNDER- = недостаточно

estimate → underestimate

Prefix обычно меняет
значение слова.""",
            },


            {
                "order": 9,
                "title":
                    "EMPLOY и SUCCESS",

                "body":
                    """Полезные word families.

EMPLOY:

employ — verb

employee — worker

employer — company/person

employment — noun

unemployed — adjective

SUCCESS:

succeed — verb

success — noun

successful — adjective

successfully — adverb""",
            },


            {
                "order": 10,
                "title":
                    "Алгоритм выбора",

                "body":
                    """Шаг 1.

Прочитай всё предложение.

Шаг 2.

Определи, что нужно:

noun?

adjective?

adverb?

verb?

Шаг 3.

Проверь смысл:

positive или negative?

Шаг 4.

Выбери правильную форму.

She is a ___ manager.
SUCCESS

Нужен adjective:

successful.""",
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
                "prompt":
                    "Choose the adjective from the SUCCESS family.",
                "options": [
                    "successful",
                    "success",
                    "successfully",
                    "succeed",
                ],
                "answer":
                    "successful",
                "explanation":
                    "SUCCESSFUL — adjective.",
            },

            {
                "order": 2,
                "section": 1,
                "prompt":
                    "Choose the adverb from the SUCCESS family.",
                "options": [
                    "successfully",
                    "successful",
                    "success",
                    "succeed",
                ],
                "answer":
                    "successfully",
                "explanation":
                    "SUCCESSFULLY описывает действие.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "prompt":
                    "They made an important ___. DECIDE",
                "options": [
                    "decision",
                    "decide",
                    "decisive",
                    "decisively",
                ],
                "answer":
                    "decision",
                "explanation":
                    "После AN IMPORTANT нужен noun.",
            },

            {
                "order": 4,
                "section": 2,
                "prompt":
                    "The country needs economic ___. DEVELOP",
                "options": [
                    "development",
                    "develop",
                    "developed",
                    "developing",
                ],
                "answer":
                    "development",
                "explanation":
                    "ECONOMIC описывает noun DEVELOPMENT.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "prompt":
                    "Choose the noun from TEACH.",
                "options": [
                    "teacher",
                    "teachingly",
                    "teachful",
                    "teachness",
                ],
                "answer":
                    "teacher",
                "explanation":
                    "-ER может обозначать человека.",
            },

            {
                "order": 6,
                "section": 3,
                "prompt":
                    "Choose the noun from HAPPY.",
                "options": [
                    "happiness",
                    "happily",
                    "happy",
                    "unhappy",
                ],
                "answer":
                    "happiness",
                "explanation":
                    "HAPPY → HAPPINESS.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "prompt":
                    "She is a very ___ employee. RESPONSIBILITY",
                "options": [
                    "responsible",
                    "responsibly",
                    "responsibility",
                    "response",
                ],
                "answer":
                    "responsible",
                "explanation":
                    "Перед EMPLOYEE нужен adjective.",
            },

            {
                "order": 8,
                "section": 4,
                "prompt":
                    "The new system is very ___. EFFECT",
                "options": [
                    "effective",
                    "effectively",
                    "effect",
                    "effectiveness",
                ],
                "answer":
                    "effective",
                "explanation":
                    "После IS VERY нужен adjective.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "prompt":
                    "Choose the adjective from HELP.",
                "options": [
                    "helpful",
                    "helpfully",
                    "helper",
                    "helpness",
                ],
                "answer":
                    "helpful",
                "explanation":
                    "HELP + FUL → HELPFUL.",
            },

            {
                "order": 10,
                "section": 5,
                "prompt":
                    "Choose the adjective from DANGER.",
                "options": [
                    "dangerous",
                    "dangerously",
                    "danger",
                    "endanger",
                ],
                "answer":
                    "dangerous",
                "explanation":
                    "DANGER + OUS → DANGEROUS.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "prompt":
                    "She answered the question ___. CORRECT",
                "options": [
                    "correctly",
                    "correct",
                    "correction",
                    "incorrect",
                ],
                "answer":
                    "correctly",
                "explanation":
                    "Слово описывает действие ANSWERED.",
            },

            {
                "order": 12,
                "section": 6,
                "prompt":
                    "He completed the work ___. CAREFUL",
                "options": [
                    "carefully",
                    "careful",
                    "care",
                    "careless",
                ],
                "answer":
                    "carefully",
                "explanation":
                    "Описываем, КАК он выполнил работу.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "prompt":
                    "Choose the negative form of POSSIBLE.",
                "options": [
                    "impossible",
                    "unpossible",
                    "inpossible",
                    "dispossible",
                ],
                "answer":
                    "impossible",
                "explanation":
                    "POSSIBLE → IMPOSSIBLE.",
            },

            {
                "order": 14,
                "section": 7,
                "prompt":
                    "Choose the negative form of LEGAL.",
                "options": [
                    "illegal",
                    "unlegal",
                    "inlegal",
                    "irlegal",
                ],
                "answer":
                    "illegal",
                "explanation":
                    "LEGAL → ILLEGAL.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "prompt":
                    "Which word means 'understand incorrectly'?",
                "options": [
                    "misunderstand",
                    "reunderstand",
                    "overunderstand",
                    "ununderstand",
                ],
                "answer":
                    "misunderstand",
                "explanation":
                    "MIS- = неправильно.",
            },

            {
                "order": 16,
                "section": 8,
                "prompt":
                    "Which word means 'write again'?",
                "options": [
                    "rewrite",
                    "miswrite",
                    "underwrite",
                    "unwrite",
                ],
                "answer":
                    "rewrite",
                "explanation":
                    "RE- = снова.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "prompt":
                    "A person who works for a company is an ___.",
                "options": [
                    "employee",
                    "employer",
                    "employment",
                    "unemployment",
                ],
                "answer":
                    "employee",
                "explanation":
                    "EMPLOYEE = работник.",
            },

            {
                "order": 18,
                "section": 9,
                "prompt":
                    "She completed the project ___. SUCCESS",
                "options": [
                    "successfully",
                    "successful",
                    "success",
                    "succeed",
                ],
                "answer":
                    "successfully",
                "explanation":
                    "После COMPLETED нужна adverb form.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "prompt":
                    "She is a ___ manager. SUCCESS",
                "options": [
                    "successful",
                    "successfully",
                    "success",
                    "succeed",
                ],
                "answer":
                    "successful",
                "explanation":
                    "Перед MANAGER нужен adjective.",
            },

            {
                "order": 20,
                "section": 10,
                "prompt":
                    "There was a big ___ in sales. IMPROVE",
                "options": [
                    "improvement",
                    "improve",
                    "improved",
                    "improvingly",
                ],
                "answer":
                    "improvement",
                "explanation":
                    "После A BIG нужен noun.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "The company made a large ___. INVEST",
                "options": [
                    "investment",
                    "invest",
                    "investive",
                    "investly",
                ],
                "answer":
                    "investment",
                "explanation":
                    "После A LARGE нужен noun.",
            },

            {
                "order": 22,
                "prompt":
                    "The instructions were very ___. HELP",
                "options": [
                    "helpful",
                    "helpfully",
                    "help",
                    "helper",
                ],
                "answer":
                    "helpful",
                "explanation":
                    "После WERE VERY нужен adjective.",
            },

            {
                "order": 23,
                "prompt":
                    "He spoke very ___. QUIET",
                "options": [
                    "quietly",
                    "quiet",
                    "quietness",
                    "unquiet",
                ],
                "answer":
                    "quietly",
                "explanation":
                    "SPOKE описывается adverb.",
            },

            {
                "order": 24,
                "prompt":
                    "Her ___ is very important to the team. CREATE",
                "options": [
                    "creativity",
                    "creative",
                    "creatively",
                    "create",
                ],
                "answer":
                    "creativity",
                "explanation":
                    "После HER нужен noun.",
            },

            {
                "order": 25,
                "prompt":
                    "The answer was ___. CORRECT",
                "options": [
                    "incorrect",
                    "incorrectly",
                    "correction",
                    "correctnessly",
                ],
                "answer":
                    "incorrect",
                "explanation":
                    "После WAS нужен adjective; по смыслу — отрицательная форма.",
            },

            {
                "order": 26,
                "prompt":
                    "The company wants to ___ its website. MODERN",
                "options": [
                    "modernize",
                    "modernly",
                    "modernity",
                    "modernful",
                ],
                "answer":
                    "modernize",
                "explanation":
                    "После TO нужен verb.",
            },

            {
                "order": 27,
                "prompt":
                    "There is high ___ in this region. EMPLOY",
                "options": [
                    "unemployment",
                    "unemployed",
                    "employee",
                    "employer",
                ],
                "answer":
                    "unemployment",
                "explanation":
                    "Нужен noun; по смыслу — unemployment.",
            },

            {
                "order": 28,
                "prompt":
                    "Choose the correct word family.",
                "options": [
                    "educate → education → educational",
                    "educate → educately → educationful",
                    "education → educateness → educationally noun",
                    "educate → uneducatement → educatorly",
                ],
                "answer":
                    "educate → education → educational",
                "explanation":
                    "Verb → noun → adjective.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct negative pair.",
                "options": [
                    "possible → impossible / regular → irregular",
                    "possible → unpossible / regular → inregular",
                    "possible → dispossible / regular → unregular",
                    "possible → inpossible / regular → disregular",
                ],
                "answer":
                    "possible → impossible / regular → irregular",
                "explanation":
                    "Правильные формы: IMPOSSIBLE и IRREGULAR.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "develop → development / success → successful / careful → carefully / possible → impossible",
                    "develop → developly / success → successfully adjective / careful → carement / possible → unpossible",
                    "develop → developmentful / success → successly / careful → carefully noun / possible → inpossible",
                    "develop → developness / success → succeedful / careful → carely / possible → dispossible",
                ],
                "answer":
                    "develop → development / success → successful / careful → carefully / possible → impossible",
                "explanation":
                    "Нужно правильно определить noun, adjective, adverb и negative form.",
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
                        "choice",

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


        # Удаляем старые упражнения
        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        # Удаляем старые Sections 11–14
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
                "✅ Interactive A1 Lesson 55 seeded"
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
