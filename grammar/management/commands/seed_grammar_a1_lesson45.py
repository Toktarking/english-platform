from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 45: -ED and -ING adjectives."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=45,
            defaults={
                "title":
                    "Прилагательные на -ED и -ING",

                "slug":
                    "adjectives-ed-ing",

                "theory_text":
                    "Adjectives ending in -ED and -ING.",

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
                    "-ED или -ING?",

                "body":
                    """Главное правило:

-ED описывает чувство.

I am bored.

She is interested.

They are excited.

-ING описывает то,
что вызывает чувство.

The film is boring.

The book is interesting.

The trip is exciting.""",
            },


            {
                "order": 2,
                "title":
                    "BORED и BORING",

                "body":
                    """BORED:

человеку скучно.

I am bored.

The children are bored.

BORING:

что-то вызывает скуку.

The film is boring.

The lesson was boring.

Коротко:

bored → чувство

boring → причина.""",
            },


            {
                "order": 3,
                "title":
                    "INTERESTED и INTERESTING",

                "body":
                    """INTERESTED:

человек испытывает интерес.

I am interested in history.

She is interested in English.

INTERESTING:

что-то вызывает интерес.

The book is interesting.

It was an interesting lesson.

Запомни:

interested IN.""",
            },


            {
                "order": 4,
                "title":
                    "TIRED и TIRING",

                "body":
                    """TIRED:

человек устал.

I am tired.

She looks tired.

TIRING:

что-то утомляет.

The journey was tiring.

This job is tiring.

Сравни:

I am tired.

The work is tiring.""",
            },


            {
                "order": 5,
                "title":
                    "EXCITED и EXCITING",

                "body":
                    """EXCITED:

человек чувствует волнение.

We are excited about the trip.

The children are excited.

EXCITING:

что-то вызывает волнение.

The trip is exciting.

It was an exciting game.

Запомни:

excited ABOUT.""",
            },


            {
                "order": 6,
                "title":
                    "SURPRISED и SURPRISING",

                "body":
                    """SURPRISED:

человек удивлён.

I was surprised.

She was surprised by the news.

SURPRISING:

что-то удивляет.

The result was surprising.

The news was surprising.

-ED → чувство

-ING → причина.""",
            },


            {
                "order": 7,
                "title":
                    "CONFUSED и CONFUSING",

                "body":
                    """CONFUSED:

человек не понимает.

The students are confused.

I am confused.

CONFUSING:

что-то трудно понять.

The instructions are confusing.

This question is confusing.

Сравни:

I am confused.

The question is confusing.""",
            },


            {
                "order": 8,
                "title":
                    "WORRIED и WORRYING",

                "body":
                    """WORRIED:

человек беспокоится.

I am worried about the exam.

She is worried about her son.

WORRYING:

что-то вызывает беспокойство.

The results are worrying.

The situation is worrying.

Запомни:

worried ABOUT.""",
            },


            {
                "order": 9,
                "title":
                    "Люди тоже могут быть -ING",

                "body":
                    """Человек может сам испытывать чувство:

He is bored.

→ ему скучно.

Но человек может
вызывать чувство у других:

He is boring.

→ он скучный.

Сравни:

The teacher is interested.

→ учителю интересно.

The teacher is interesting.

→ учитель интересный.""",
            },


            {
                "order": 10,
                "title":
                    "Как быстро выбрать",

                "body":
                    """Задай вопрос:

КТО ЧУВСТВУЕТ?

→ -ED

I am tired.

She is surprised.

They are excited.

ЧТО ВЫЗЫВАЕТ ЧУВСТВО?

→ -ING

The work is tiring.

The result is surprising.

The trip is exciting.

Главное:

-ED = feeling

-ING = cause.""",
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
                    "I am ___. There is nothing to do.",
                "options": [
                    "bored",
                    "boring",
                    "bore",
                    "boredom",
                ],
                "answer":
                    "bored",
                "explanation":
                    "Человек испытывает чувство → BORED.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "This film is very ___.",
                "options": [
                    "boring",
                    "bored",
                    "bore",
                    "boredly",
                ],
                "answer":
                    "boring",
                "explanation":
                    "Фильм вызывает чувство → BORING.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "The children were ___ during the lecture.",
                "options": [
                    "bored",
                    "boring",
                    "bore",
                    "boringly",
                ],
                "answer":
                    "bored",
                "explanation":
                    "Дети чувствовали скуку → BORED.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "It was a ___ meeting.",
                "options": [
                    "boring",
                    "bored",
                    "boredom",
                    "bore",
                ],
                "answer":
                    "boring",
                "explanation":
                    "Встреча вызывает скуку → BORING.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "She is ___ in science.",
                "options": [
                    "interested",
                    "interesting",
                    "interest",
                    "interestingly",
                ],
                "answer":
                    "interested",
                "explanation":
                    "INTERESTED IN = заинтересован в.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "This article is very ___.",
                "options": [
                    "interesting",
                    "interested",
                    "interest",
                    "interestedly",
                ],
                "answer":
                    "interesting",
                "explanation":
                    "Статья вызывает интерес → INTERESTING.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "I feel ___ after work.",
                "options": [
                    "tired",
                    "tiring",
                    "tire",
                    "tiredly",
                ],
                "answer":
                    "tired",
                "explanation":
                    "Человек чувствует усталость → TIRED.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "The journey was very ___.",
                "options": [
                    "tiring",
                    "tired",
                    "tire",
                    "tiredness",
                ],
                "answer":
                    "tiring",
                "explanation":
                    "Поездка вызывает усталость → TIRING.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "We are ___ about our holiday.",
                "options": [
                    "excited",
                    "exciting",
                    "excite",
                    "excitedly",
                ],
                "answer":
                    "excited",
                "explanation":
                    "Люди испытывают волнение → EXCITED.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "The match was really ___.",
                "options": [
                    "exciting",
                    "excited",
                    "excitement",
                    "excitedly",
                ],
                "answer":
                    "exciting",
                "explanation":
                    "Матч вызывает волнение → EXCITING.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "She was ___ by the result.",
                "options": [
                    "surprised",
                    "surprising",
                    "surprise",
                    "surprisingly",
                ],
                "answer":
                    "surprised",
                "explanation":
                    "Она испытала удивление → SURPRISED.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "The result was ___.",
                "options": [
                    "surprising",
                    "surprised",
                    "surprise",
                    "surprisedly",
                ],
                "answer":
                    "surprising",
                "explanation":
                    "Результат вызывает удивление → SURPRISING.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "The students look ___.",
                "options": [
                    "confused",
                    "confusing",
                    "confusion",
                    "confuse",
                ],
                "answer":
                    "confused",
                "explanation":
                    "Студенты испытывают состояние → CONFUSED.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "These instructions are ___.",
                "options": [
                    "confusing",
                    "confused",
                    "confusion",
                    "confusedly",
                ],
                "answer":
                    "confusing",
                "explanation":
                    "Инструкции вызывают растерянность → CONFUSING.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "I am ___ about tomorrow's exam.",
                "options": [
                    "worried",
                    "worrying",
                    "worry",
                    "worriedly",
                ],
                "answer":
                    "worried",
                "explanation":
                    "WORRIED ABOUT = беспокоиться о.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "The latest results are ___.",
                "options": [
                    "worrying",
                    "worried",
                    "worry",
                    "worries",
                ],
                "answer":
                    "worrying",
                "explanation":
                    "Результаты вызывают беспокойство → WORRYING.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "He is ___. Nobody enjoys his stories.",
                "options": [
                    "boring",
                    "bored",
                    "bore",
                    "boredom",
                ],
                "answer":
                    "boring",
                "explanation":
                    "Человек может быть BORING, если вызывает скуку.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "The teacher is ___. Her lessons are excellent.",
                "options": [
                    "interesting",
                    "interested",
                    "interest",
                    "interestedly",
                ],
                "answer":
                    "interesting",
                "explanation":
                    "Учитель вызывает интерес → INTERESTING.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Choose the correct pair.",
                "options": [
                    "I am tired. / The work is tiring.",
                    "I am tiring. / The work is tired.",
                    "I am tiredly. / The work is tire.",
                    "I am tire. / The work is tiredly.",
                ],
                "answer":
                    "I am tired. / The work is tiring.",
                "explanation":
                    "-ED = feeling; -ING = cause.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Choose the correct pair.",
                "options": [
                    "She is excited. / The trip is exciting.",
                    "She is exciting. / The trip is excited.",
                    "She is excitement. / The trip is excite.",
                    "She is excitedly. / The trip is excitement.",
                ],
                "answer":
                    "She is excited. / The trip is exciting.",
                "explanation":
                    "Человек чувствует → EXCITED; причина → EXCITING.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "I was ___ because the presentation lasted three hours.",
                "options": [
                    "bored",
                    "boring",
                    "bore",
                    "boredom",
                ],
                "answer":
                    "bored",
                "explanation":
                    "Человек испытывает скуку → BORED.",
            },

            {
                "order": 22,
                "prompt":
                    "The presentation was extremely ___.",
                "options": [
                    "boring",
                    "bored",
                    "bore",
                    "boredly",
                ],
                "answer":
                    "boring",
                "explanation":
                    "Презентация вызывает скуку → BORING.",
            },

            {
                "order": 23,
                "prompt":
                    "My brother is ___ in photography.",
                "options": [
                    "interested",
                    "interesting",
                    "interest",
                    "interestingly",
                ],
                "answer":
                    "interested",
                "explanation":
                    "INTERESTED IN.",
            },

            {
                "order": 24,
                "prompt":
                    "It was an ___ documentary.",
                "options": [
                    "interesting",
                    "interested",
                    "interest",
                    "interestedly",
                ],
                "answer":
                    "interesting",
                "explanation":
                    "Документальный фильм вызывает интерес → INTERESTING.",
            },

            {
                "order": 25,
                "prompt":
                    "After ten hours of driving, we were ___.",
                "options": [
                    "tired",
                    "tiring",
                    "tire",
                    "tiredly",
                ],
                "answer":
                    "tired",
                "explanation":
                    "Люди испытывают усталость → TIRED.",
            },

            {
                "order": 26,
                "prompt":
                    "Driving for ten hours was ___.",
                "options": [
                    "tiring",
                    "tired",
                    "tire",
                    "tiredness",
                ],
                "answer":
                    "tiring",
                "explanation":
                    "Действие вызывает усталость → TIRING.",
            },

            {
                "order": 27,
                "prompt":
                    "The children are ___ about the school trip.",
                "options": [
                    "excited",
                    "exciting",
                    "excitement",
                    "excitedly",
                ],
                "answer":
                    "excited",
                "explanation":
                    "Дети испытывают волнение → EXCITED.",
            },

            {
                "order": 28,
                "prompt":
                    "The exam instructions were very ___.",
                "options": [
                    "confusing",
                    "confused",
                    "confusion",
                    "confusedly",
                ],
                "answer":
                    "confusing",
                "explanation":
                    "Инструкции вызывают растерянность → CONFUSING.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct pair.",
                "options": [
                    "She was surprised by the news. / The news was surprising.",
                    "She was surprising by the news. / The news was surprised.",
                    "She was surprise by the news. / The news was surprisedly.",
                    "She was surprisingly by the news. / The news was surprise.",
                ],
                "answer":
                    "She was surprised by the news. / The news was surprising.",
                "explanation":
                    "SURPRISED = чувство; SURPRISING = причина.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "bored = feeling / boring = cause / interested = feeling / interesting = cause",
                    "bored = cause / boring = feeling / interested = cause / interesting = feeling",
                    "bored = past tense only / boring = present tense only / interested = verb / interesting = noun",
                    "bored = action / boring = person only / interested = future / interesting = past",
                ],
                "answer":
                    "bored = feeling / boring = cause / interested = feeling / interesting = cause",
                "explanation":
                    "Главное правило урока: -ED = feeling; -ING = cause.",
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


        # Remove old exercises
        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        # Remove old sections
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
                "✅ Interactive A1 Lesson 45 seeded"
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
