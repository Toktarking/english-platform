from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 45: "
        "Adjectives ending in -ED and -ING."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=45,
            defaults={
                "title": "Прилагательные на -ED и -ING",
                "slug": "adjectives-ed-ing",
                "theory_text": "Adjectives ending in -ED and -ING.",
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Главное различие",
                "body": """В английском есть пары прилагательных:

bored / boring

interested / interesting

tired / tiring

excited / exciting

surprised / surprising

confused / confusing

Главное правило:

-ED описывает того, кто испытывает чувство.

-ING описывает человека, предмет или ситуацию, которые вызывают это чувство.""",
            },

            {
                "order": 2,
                "title": "Форма на -ED",
                "body": """Прилагательное на -ED показывает состояние или чувство.

Примеры:

I am bored.
— Мне скучно.

She is interested.
— Она заинтересована.

They are tired.
— Они устали.

He was surprised.
— Он был удивлён.

Главный вопрос:

Что человек чувствует?

Если описывается чувство, часто нужна форма на -ED.""",
            },

            {
                "order": 3,
                "title": "Форма на -ING",
                "body": """Прилагательное на -ING показывает причину чувства.

Примеры:

The lesson is boring.
— Урок скучный.

The book is interesting.
— Книга интересная.

The journey was tiring.
— Поездка была утомительной.

The news was surprising.
— Новость была удивительной.

Главный вопрос:

Что вызывает это чувство?

Если что-то вызывает эмоцию, часто нужна форма на -ING.""",
            },

            {
                "order": 4,
                "title": "BORED и BORING",
                "body": """BORED:

испытывающий скуку.

I am bored.

The children were bored.

BORING:

вызывающий скуку.

The lesson is boring.

It was a boring film.

Сравните:

I am bored.
— Мне скучно.

The film is boring.
— Фильм скучный.""",
            },

            {
                "order": 5,
                "title": "INTERESTED и INTERESTING",
                "body": """INTERESTED:

заинтересованный.

I am interested in history.

She is interested in learning English.

INTERESTING:

интересный, вызывающий интерес.

This book is interesting.

It was an interesting discussion.

Сравните:

I am interested in the book.

The book is interesting.""",
            },

            {
                "order": 6,
                "title": "TIRED и TIRING",
                "body": """TIRED:

уставший.

I am tired.

She looks tired.

They were tired after work.

TIRING:

утомительный.

The work is tiring.

It was a tiring journey.

Сравните:

I am tired after the journey.

The journey was tiring.""",
            },

            {
                "order": 7,
                "title": "EXCITED и SURPRISED",
                "body": """EXCITED:

человек испытывает волнение.

I am excited about the trip.

The children are excited.

EXCITING:

что-то вызывает волнение.

The trip is exciting.

It was an exciting match.

SURPRISED:

I was surprised by the news.

SURPRISING:

The news was surprising.""",
            },

            {
                "order": 8,
                "title": "CONFUSED и WORRIED",
                "body": """CONFUSED:

человек запутался.

The students are confused.

CONFUSING:

что-то сбивает с толку.

The instructions are confusing.

WORRIED:

человек обеспокоен.

I am worried about the exam.

WORRYING:

ситуация вызывает беспокойство.

The results are worrying.""",
            },

            {
                "order": 9,
                "title": "FRIGHTENED, ANNOYED, DISAPPOINTED",
                "body": """FRIGHTENED:

The child was frightened.

FRIGHTENING:

The noise was frightening.

ANNOYED:

She is annoyed with him.

ANNOYING:

His behaviour is annoying.

DISAPPOINTED:

I was disappointed with the result.

DISAPPOINTING:

The result was disappointing.""",
            },

            {
                "order": 10,
                "title": "EMBARRASSED, AMAZED, RELAXED",
                "body": """EMBARRASSED:

I felt embarrassed.

EMBARRASSING:

It was an embarrassing mistake.

AMAZED:

I was amazed by the view.

AMAZING:

The view was amazing.

RELAXED:

I feel relaxed.

RELAXING:

The music is relaxing.""",
            },

            {
                "order": 11,
                "title": "Не только люди могут быть на -ED",
                "body": """Форма на -ED описывает того, кто способен испытывать чувство.

Это может быть:

человек;

группа людей;

животное.

Примеры:

The audience was excited.

The team was disappointed.

The dog was frightened.

The children were bored.

Главное — не слово «человек», а способность испытывать эмоцию.""",
            },

            {
                "order": 12,
                "title": "Люди тоже могут быть на -ING",
                "body": """Человек может не только испытывать эмоцию, но и вызывать её у других.

Сравните:

He is bored.
— Ему скучно.

He is boring.
— Он скучный.

The teacher is interested.
— Учитель сам заинтересован.

The teacher is interesting.
— Учитель интересный.

She is annoyed.
— Она раздражена.

She is annoying.
— Она раздражает других.""",
            },

            {
                "order": 13,
                "title": "Предлоги после -ED форм",
                "body": """Частые конструкции:

interested in

I am interested in history.

excited about

She is excited about the trip.

worried about

He is worried about the exam.

frightened of

I am frightened of dogs.

disappointed with / by / in

I am disappointed with the service.

surprised at / by

She was surprised by his answer.""",
            },

            {
                "order": 14,
                "title": "Как выбрать -ED или -ING",
                "body": """Задайте два вопроса.

1. Кто испытывает чувство?

Используйте -ED.

I am tired.

She is interested.

They are confused.

2. Кто или что вызывает чувство?

Используйте -ING.

The work is tiring.

The book is interesting.

The instructions are confusing.

Главное правило:

-ED = чувство

-ING = причина чувства""",
            },

        ]

        for data in sections:
            GrammarLessonSection.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "title": data["title"],
                    "body": data["body"],
                },
            )

        exercises = [

            {
                "order": 1,
                "prompt": "The film was so ___ that I fell asleep.",
                "options": [
                    "bored",
                    "boring",
                    "bore",
                    "boredom",
                ],
                "answer": "boring",
                "explanation": (
                    "Фильм вызывает скуку → boring."
                ),
            },

            {
                "order": 2,
                "prompt": "The children were ___ during the lesson.",
                "options": [
                    "boring",
                    "bored",
                    "bore",
                    "boringly",
                ],
                "answer": "bored",
                "explanation": (
                    "Дети испытывали скуку → bored."
                ),
            },

            {
                "order": 3,
                "prompt": "I am very ___ in learning English.",
                "options": [
                    "interesting",
                    "interested",
                    "interest",
                    "interestingly",
                ],
                "answer": "interested",
                "explanation": (
                    "Человек испытывает интерес → interested in."
                ),
            },

            {
                "order": 4,
                "prompt": "This is an ___ topic.",
                "options": [
                    "interested",
                    "interesting",
                    "interest",
                    "interestedly",
                ],
                "answer": "interesting",
                "explanation": (
                    "Тема вызывает интерес → interesting."
                ),
            },

            {
                "order": 5,
                "prompt": "We felt ___ after the long meeting.",
                "options": [
                    "tiring",
                    "tired",
                    "tire",
                    "tiredly",
                ],
                "answer": "tired",
                "explanation": (
                    "Мы испытывали усталость → tired."
                ),
            },

            {
                "order": 6,
                "prompt": "It was a very ___ meeting.",
                "options": [
                    "tired",
                    "tiring",
                    "tire",
                    "tiredness",
                ],
                "answer": "tiring",
                "explanation": (
                    "Встреча вызвала усталость → tiring."
                ),
            },

            {
                "order": 7,
                "prompt": "She was ___ by the news.",
                "options": [
                    "surprising",
                    "surprised",
                    "surprise",
                    "surprisingly only",
                ],
                "answer": "surprised",
                "explanation": (
                    "Она испытала удивление → surprised."
                ),
            },

            {
                "order": 8,
                "prompt": "The news was ___.",
                "options": [
                    "surprised",
                    "surprising",
                    "surprise",
                    "surprisedly",
                ],
                "answer": "surprising",
                "explanation": (
                    "Новость вызвала удивление → surprising."
                ),
            },

            {
                "order": 9,
                "prompt": "The instructions were very ___.",
                "options": [
                    "confused",
                    "confusing",
                    "confusion",
                    "confusingly as an adjective",
                ],
                "answer": "confusing",
                "explanation": (
                    "Инструкции сбивают с толку → confusing."
                ),
            },

            {
                "order": 10,
                "prompt": "The students looked ___.",
                "options": [
                    "confusing",
                    "confused",
                    "confusion",
                    "confuse",
                ],
                "answer": "confused",
                "explanation": (
                    "Студенты испытывали растерянность → confused."
                ),
            },

            {
                "order": 11,
                "prompt": "I am ___ about the exam.",
                "options": [
                    "worrying",
                    "worried",
                    "worry",
                    "worriedly",
                ],
                "answer": "worried",
                "explanation": (
                    "Человек обеспокоен → worried about."
                ),
            },

            {
                "order": 12,
                "prompt": "The results are ___.",
                "options": [
                    "worried",
                    "worrying",
                    "worry",
                    "worriedly",
                ],
                "answer": "worrying",
                "explanation": (
                    "Результаты вызывают беспокойство → worrying."
                ),
            },

            {
                "order": 13,
                "prompt": "The child was ___ by the noise.",
                "options": [
                    "frightening",
                    "frightened",
                    "frighten",
                    "frighteningly",
                ],
                "answer": "frightened",
                "explanation": (
                    "Ребёнок испытал страх → frightened."
                ),
            },

            {
                "order": 14,
                "prompt": "The noise was ___.",
                "options": [
                    "frightened",
                    "frightening",
                    "frighten",
                    "frightenedly",
                ],
                "answer": "frightening",
                "explanation": (
                    "Шум вызывает страх → frightening."
                ),
            },

            {
                "order": 15,
                "prompt": "It was an ___ situation.",
                "options": [
                    "embarrassed",
                    "embarrassing",
                    "embarrassment",
                    "embarrass",
                ],
                "answer": "embarrassing",
                "explanation": (
                    "Ситуация вызывает смущение → embarrassing."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I am boring because there is nothing to do.",
                    "I am bored because there is nothing to do.",
                    "I am bore because there is nothing to do.",
                    "I am boredom because there is nothing to do.",
                ],
                "answer": (
                    "I am bored because there is nothing to do."
                ),
                "explanation": (
                    "Если человеку скучно, используется bored."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "The film is bored.",
                    "The film is boring.",
                    "The film is bore.",
                    "The film is boredom.",
                ],
                "answer": "The film is boring.",
                "explanation": (
                    "Фильм вызывает скуку → boring."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I am interesting in history.",
                    "I am interested in history.",
                    "I am interested at history.",
                    "I am interesting about history.",
                ],
                "answer": "I am interested in history.",
                "explanation": (
                    "Правильная конструкция: interested in."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct pair.",
                "options": [
                    (
                        "We are excited about the trip. / "
                        "The trip is exciting."
                    ),
                    (
                        "We are exciting about the trip. / "
                        "The trip is excited."
                    ),
                    (
                        "We are excitement about the trip. / "
                        "The trip is excite."
                    ),
                    (
                        "We are excited in the trip. / "
                        "The trip is excitingly."
                    ),
                ],
                "answer": (
                    "We are excited about the trip. / "
                    "The trip is exciting."
                ),
                "explanation": (
                    "Люди чувствуют → excited; "
                    "поездка вызывает чувство → exciting."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the correct pair.",
                "options": [
                    (
                        "The students are confused. / "
                        "The instructions are confusing."
                    ),
                    (
                        "The students are confusing. / "
                        "The instructions are confused."
                    ),
                    (
                        "The students are confusion. / "
                        "The instructions confuse adjective."
                    ),
                    (
                        "The students confuseding. / "
                        "The instructions are confusedly."
                    ),
                ],
                "answer": (
                    "The students are confused. / "
                    "The instructions are confusing."
                ),
                "explanation": (
                    "Студенты испытывают состояние; "
                    "инструкции вызывают его."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "The teacher is ___. "
                    "His lessons always keep us interested."
                ),
                "options": [
                    "interested",
                    "interesting",
                    "interest",
                    "interestingly person",
                ],
                "answer": "interesting",
                "explanation": (
                    "Учитель вызывает интерес у других → interesting."
                ),
            },

            {
                "order": 22,
                "prompt": (
                    "The teacher is ___ in new teaching methods."
                ),
                "options": [
                    "interesting",
                    "interested",
                    "interestingly",
                    "interest",
                ],
                "answer": "interested",
                "explanation": (
                    "Учитель сам испытывает интерес → interested in."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct preposition pair.",
                "options": [
                    (
                        "interested in English / "
                        "worried about the exam"
                    ),
                    (
                        "interested about English / "
                        "worried in the exam"
                    ),
                    (
                        "interested at English / "
                        "worried of the exam"
                    ),
                    (
                        "interested on English / "
                        "worried with exam"
                    ),
                ],
                "answer": (
                    "interested in English / "
                    "worried about the exam"
                ),
                "explanation": (
                    "Правильные сочетания: interested in, worried about."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "bored → feeling / "
                        "boring → cause / "
                        "interested → feeling / "
                        "interesting → cause"
                    ),
                    (
                        "bored → cause / "
                        "boring → feeling / "
                        "interested → cause / "
                        "interesting → feeling"
                    ),
                    (
                        "bored → action / "
                        "boring → person only / "
                        "interested → verb only / "
                        "interesting → tense"
                    ),
                    (
                        "bored → future / "
                        "boring → past / "
                        "interested → present / "
                        "interesting → continuous only"
                    ),
                ],
                "answer": (
                    "bored → feeling / "
                    "boring → cause / "
                    "interested → feeling / "
                    "interesting → cause"
                ),
                "explanation": (
                    "-ED = чувство; -ING = причина чувства."
                ),
            },

        ]

        for data in exercises:
            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "exercise_type": GrammarExercise.Type.CHOICE,
                    "prompt": data["prompt"],
                    "options": data["options"],
                    "correct_answer": data["answer"],
                    "explanation": data["explanation"],
                    "is_published": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ A1 Lesson 45 seeded: -ED and -ING adjectives"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
