from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 53: Question Tags."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=53,
            defaults={
                "title":
                    "Разделительные вопросы — Question Tags",

                "slug":
                    "question-tags",

                "theory_text":
                    "Question Tags: auxiliary verbs, "
                    "opposite polarity and special cases.",

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
                    "Что такое Question Tag",

                "body":
                    """Question Tag — короткий вопрос
в конце предложения.

You are tired,
aren't you?

He works here,
doesn't he?

Мы используем Question Tag,
когда хотим:

проверить информацию;

получить подтверждение;

поддержать разговор.""",
            },


            {
                "order": 2,
                "title":
                    "Главное правило",

                "body":
                    """Positive sentence
→ negative tag.

She is ready,
isn't she?

Negative sentence
→ positive tag.

She isn't ready,
is she?

Главное:

две части должны иметь
противоположный знак.""",
            },


            {
                "order": 3,
                "title":
                    "BE: IS, ARE, WAS, WERE",

                "body":
                    """С BE повторяем
тот же глагол.

She is tired,
isn't she?

They are ready,
aren't they?

He wasn't at home,
was he?

They weren't late,
were they?

DO здесь не нужен.""",
            },


            {
                "order": 4,
                "title":
                    "Present Simple",

                "body":
                    """Если обычный глагол
в Present Simple:

I / you / we / they
→ DO

he / she / it
→ DOES

You work here,
don't you?

She works here,
doesn't she?

He doesn't drive,
does he?""",
            },


            {
                "order": 5,
                "title":
                    "Past Simple",

                "body":
                    """В Past Simple используем:

DID

She arrived yesterday,
didn't she?

They called you,
didn't they?

He didn't come,
did he?

Важно:

в tag повторяем время,
а не основной глагол.""",
            },


            {
                "order": 6,
                "title":
                    "Perfect, Future и Modals",

                "body":
                    """Повторяем auxiliary
или modal.

You have finished,
haven't you?

She has left,
hasn't she?

He will come,
won't he?

She can swim,
can't she?

We should leave,
shouldn't we?""",
            },


            {
                "order": 7,
                "title":
                    "Правильное pronoun",

                "body":
                    """Имя или существительное
заменяем местоимением.

Anna is here,
isn't she?

Marat works here,
doesn't he?

The students are ready,
aren't they?

This is your book,
isn't it?

These are your keys,
aren't they?""",
            },


            {
                "order": 8,
                "title":
                    "Negative meaning",

                "body":
                    """Некоторые слова уже
имеют отрицательное значение.

never

nobody

nothing

hardly

rarely

Поэтому tag будет
положительным.

He never calls,
does he?

Nobody came,
did they?

Nothing happened,
did it?""",
            },


            {
                "order": 9,
                "title":
                    "I AM и LET'S",

                "body":
                    """Есть два важных
особых случая.

I am...

→ aren't I?

I am late,
aren't I?

LET'S...

→ shall we?

Let's start,
shall we?

Их лучше просто
запомнить.""",
            },


            {
                "order": 10,
                "title":
                    "Commands",

                "body":
                    """После команды часто
используем:

will you?

Open the door,
will you?

Wait here,
will you?

Don't be late,
will you?

Алгоритм:

1. Найди tense / auxiliary.
2. Сделай opposite form.
3. Выбери pronoun.""",
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
                    "She is your teacher, ___?",
                "options": [
                    "isn't she",
                    "is she",
                    "doesn't she",
                    "aren't she",
                ],
                "answer":
                    "isn't she",
                "explanation":
                    "Positive IS → negative ISN'T.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Which sentence contains a Question Tag?",
                "options": [
                    "You live here, don't you?",
                    "Do you live here?",
                    "Where do you live?",
                    "Who lives here?",
                ],
                "answer":
                    "You live here, don't you?",
                "explanation":
                    "Question Tag — короткий вопрос после основного предложения.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "They are ready, ___?",
                "options": [
                    "aren't they",
                    "are they",
                    "don't they",
                    "weren't they",
                ],
                "answer":
                    "aren't they",
                "explanation":
                    "Positive sentence → negative tag.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "They aren't ready, ___?",
                "options": [
                    "are they",
                    "aren't they",
                    "do they",
                    "were they",
                ],
                "answer":
                    "are they",
                "explanation":
                    "Negative sentence → positive tag.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "She was tired, ___?",
                "options": [
                    "wasn't she",
                    "didn't she",
                    "was she",
                    "isn't she",
                ],
                "answer":
                    "wasn't she",
                "explanation":
                    "С WAS повторяем WAS.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "They weren't at home, ___?",
                "options": [
                    "were they",
                    "weren't they",
                    "did they",
                    "are they",
                ],
                "answer":
                    "were they",
                "explanation":
                    "Negative WERE → positive WERE.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "You like coffee, ___?",
                "options": [
                    "don't you",
                    "do you",
                    "aren't you",
                    "didn't you",
                ],
                "answer":
                    "don't you",
                "explanation":
                    "Present Simple with YOU → DO.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "She doesn't work here, ___?",
                "options": [
                    "does she",
                    "doesn't she",
                    "is she",
                    "did she",
                ],
                "answer":
                    "does she",
                "explanation":
                    "Negative DOESN'T → positive DOES.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "He called yesterday, ___?",
                "options": [
                    "didn't he",
                    "doesn't he",
                    "wasn't he",
                    "did he",
                ],
                "answer":
                    "didn't he",
                "explanation":
                    "Past Simple → DID.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "They didn't come, ___?",
                "options": [
                    "did they",
                    "didn't they",
                    "do they",
                    "were they",
                ],
                "answer":
                    "did they",
                "explanation":
                    "Negative DIDN'T → positive DID.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "You have finished, ___?",
                "options": [
                    "haven't you",
                    "don't you",
                    "have you",
                    "didn't you",
                ],
                "answer":
                    "haven't you",
                "explanation":
                    "Present Perfect → HAVE.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "She can swim, ___?",
                "options": [
                    "can't she",
                    "doesn't she",
                    "can she",
                    "isn't she",
                ],
                "answer":
                    "can't she",
                "explanation":
                    "Modal CAN повторяется в tag.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "Anna is busy, ___?",
                "options": [
                    "isn't she",
                    "isn't Anna",
                    "doesn't she",
                    "aren't she",
                ],
                "answer":
                    "isn't she",
                "explanation":
                    "Anna → SHE.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "These are your books, ___?",
                "options": [
                    "aren't they",
                    "aren't these",
                    "isn't it",
                    "are they",
                ],
                "answer":
                    "aren't they",
                "explanation":
                    "THESE → THEY.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "He never calls, ___?",
                "options": [
                    "does he",
                    "doesn't he",
                    "is he",
                    "did he",
                ],
                "answer":
                    "does he",
                "explanation":
                    "NEVER имеет negative meaning → positive tag.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "Nobody came, ___?",
                "options": [
                    "did they",
                    "didn't they",
                    "did he",
                    "does they",
                ],
                "answer":
                    "did they",
                "explanation":
                    "NOBODY отрицательно по смыслу; pronoun → THEY.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "I am right, ___?",
                "options": [
                    "aren't I",
                    "amn't I",
                    "don't I",
                    "isn't I",
                ],
                "answer":
                    "aren't I",
                "explanation":
                    "Особый случай: I AM → AREN'T I.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "Let's go, ___?",
                "options": [
                    "shall we",
                    "will we",
                    "do we",
                    "aren't we",
                ],
                "answer":
                    "shall we",
                "explanation":
                    "LET'S → SHALL WE.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Open the window, ___?",
                "options": [
                    "will you",
                    "shall we",
                    "do you",
                    "aren't you",
                ],
                "answer":
                    "will you",
                "explanation":
                    "После imperative часто используется WILL YOU.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Don't be late, ___?",
                "options": [
                    "will you",
                    "won't you",
                    "do you",
                    "shall we",
                ],
                "answer":
                    "will you",
                "explanation":
                    "После команды, включая отрицательную, часто используем WILL YOU.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "Tom is at home, ___?",
                "options": [
                    "isn't he",
                    "doesn't he",
                    "is he",
                    "aren't he",
                ],
                "answer":
                    "isn't he",
                "explanation":
                    "Tom → HE; positive IS → ISN'T.",
            },

            {
                "order": 22,
                "prompt":
                    "You don't know him, ___?",
                "options": [
                    "do you",
                    "don't you",
                    "are you",
                    "did you",
                ],
                "answer":
                    "do you",
                "explanation":
                    "Negative DON'T → positive DO.",
            },

            {
                "order": 23,
                "prompt":
                    "She went to work, ___?",
                "options": [
                    "didn't she",
                    "doesn't she",
                    "wasn't she",
                    "did she",
                ],
                "answer":
                    "didn't she",
                "explanation":
                    "WENT = Past Simple → DID.",
            },

            {
                "order": 24,
                "prompt":
                    "They haven't arrived, ___?",
                "options": [
                    "have they",
                    "haven't they",
                    "do they",
                    "did they",
                ],
                "answer":
                    "have they",
                "explanation":
                    "Negative HAVEN'T → positive HAVE.",
            },

            {
                "order": 25,
                "prompt":
                    "He will help us, ___?",
                "options": [
                    "won't he",
                    "will he",
                    "doesn't he",
                    "isn't he",
                ],
                "answer":
                    "won't he",
                "explanation":
                    "Positive WILL → negative WON'T.",
            },

            {
                "order": 26,
                "prompt":
                    "Marat can drive, ___?",
                "options": [
                    "can't he",
                    "doesn't he",
                    "can he",
                    "isn't he",
                ],
                "answer":
                    "can't he",
                "explanation":
                    "Marat → HE; CAN → CAN'T.",
            },

            {
                "order": 27,
                "prompt":
                    "Nothing happened, ___?",
                "options": [
                    "did it",
                    "didn't it",
                    "did they",
                    "does it",
                ],
                "answer":
                    "did it",
                "explanation":
                    "NOTHING negative meaning; pronoun → IT.",
            },

            {
                "order": 28,
                "prompt":
                    "This is your phone, ___?",
                "options": [
                    "isn't it",
                    "isn't this",
                    "doesn't it",
                    "is it",
                ],
                "answer":
                    "isn't it",
                "explanation":
                    "THIS → IT.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct special-case pair.",
                "options": [
                    "I am late, aren't I? / Let's start, shall we?",
                    "I am late, amn't I? / Let's start, will we?",
                    "I am late, don't I? / Let's start, do we?",
                    "I am late, isn't I? / Let's start, won't we?",
                ],
                "answer":
                    "I am late, aren't I? / Let's start, shall we?",
                "explanation":
                    "I AM → AREN'T I; LET'S → SHALL WE.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "She is ready, isn't she? / He works here, doesn't he? / They came early, didn't they? / Nobody called, did they?",
                    "She is ready, is she? / He works here, isn't he? / They came early, weren't they? / Nobody called, didn't they?",
                    "She is ready, doesn't she? / He works here, don't he? / They came early, doesn't they? / Nobody called, was they?",
                    "She is ready, aren't she? / He works here, does he? / They came early, do they? / Nobody called, don't they?",
                ],
                "answer":
                    "She is ready, isn't she? / He works here, doesn't he? / They came early, didn't they? / Nobody called, did they?",
                "explanation":
                    "Нужно правильно выбрать auxiliary, opposite form и pronoun.",
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


        # Удаляем старые лишние упражнения
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
                "✅ Interactive A1 Lesson 53 seeded"
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
