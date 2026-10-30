from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 44: "
        "Adjectives and Adverbs."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=44,
            defaults={
                "title": "Прилагательные и наречия",
                "slug": "adjectives-and-adverbs",
                "theory_text": "Adjectives and Adverbs.",
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Прилагательное и наречие",
                "body": """Прилагательное описывает человека, предмет, место или ситуацию.

Примеры:

a beautiful city

a difficult task

a careful driver

Наречие обычно описывает действие.

Примеры:

speak slowly

work carefully

arrive early

Главное различие:

adjective → описывает существительное

adverb → описывает действие""",
            },

            {
                "order": 2,
                "title": "Сравните adjective и adverb",
                "body": """Сравните:

She is a careful driver.

Careful описывает существительное driver.

She drives carefully.

Carefully описывает действие drives.

Ещё пример:

He is a slow worker.

He works slowly.

Quiet person → speaks quietly.

Главный вопрос:

что описывает слово — предмет или действие?""",
            },

            {
                "order": 3,
                "title": "Как образуются наречия",
                "body": """Большинство наречий образуется:

adjective + -ly

slow → slowly

careful → carefully

quick → quickly

quiet → quietly

polite → politely

Если прилагательное заканчивается на Y:

easy → easily

happy → happily

angry → angrily

heavy → heavily

На -LE:

simple → simply

gentle → gently

terrible → terribly""",
            },

            {
                "order": 4,
                "title": "GOOD и WELL",
                "body": """GOOD — прилагательное.

She is a good teacher.

This is a good idea.

The food is good.

WELL — наречие.

She teaches well.

He speaks English well.

They work well together.

Сравните:

He is a good singer.

He sings well.

WELL также может быть прилагательным со значением «здоров»:

I am well.""",
            },

            {
                "order": 5,
                "title": "После TO BE — прилагательное",
                "body": """После am/is/are для описания подлежащего обычно используется adjective.

Правильно:

She is happy.

He is tired.

The room is quiet.

They are careful.

Неправильно:

She is happily.

He is carefully.

После TO BE мы обычно описываем состояние или качество подлежащего.""",
            },

            {
                "order": 6,
                "title": "LOOK, FEEL, SOUND, SMELL, TASTE",
                "body": """После некоторых глаголов часто используется прилагательное:

look

feel

sound

smell

taste

seem

become

get

Примеры:

You look tired.

She feels nervous.

That sounds interesting.

The soup smells delicious.

The cake tastes good.

Важно:

You look tired.

Не:

You look tiredly.""",
            },

            {
                "order": 7,
                "title": "LOOK и LOOK AT",
                "body": """LOOK + adjective описывает внешний вид.

She looked angry.

Она выглядела сердитой.

LOOK AT + object + adverb описывает, как человек посмотрел.

She looked at me angrily.

Она сердито посмотрела на меня.

Сравните:

She looks beautiful.

She looked at him angrily.""",
            },

            {
                "order": 8,
                "title": "FAST, HARD, LATE",
                "body": """Некоторые наречия имеют ту же форму, что и прилагательное.

FAST:

a fast car

drive fast

Не:

fastly

HARD:

a hard task

work hard

HARDLY имеет другое значение:

hardly = едва, почти не

He works hard.
— работает усердно.

He hardly works.
— почти не работает.

LATE:

a late train

arrive late""",
            },

            {
                "order": 9,
                "title": "LATE/LATELY, HIGH/HIGHLY",
                "body": """LATE означает поздно.

He arrived late.

LATELY означает в последнее время.

I haven't seen him lately.

HIGH — физически высоко.

The bird flew high.

HIGHLY — очень, высоко в переносном смысле.

I highly recommend this book.

a highly successful company

Важно помнить, что добавление -ly иногда меняет значение слова.""",
            },

            {
                "order": 10,
                "title": "Наречия степени",
                "body": """Наречия степени показывают, насколько сильно выражено качество.

Частые слова:

very

really

quite

extremely

too

enough

almost

completely

Примеры:

very interesting

really good

extremely difficult

too expensive

too quickly

ENOUGH ставится после adjective/adverb:

old enough

quickly enough

Но перед существительным:

enough time

enough money""",
            },

            {
                "order": 11,
                "title": "SO и SUCH",
                "body": """SO используется перед adjective или adverb.

so beautiful

so difficult

so slowly

Пример:

The film was so interesting.

SUCH используется с существительным.

such a beautiful place

such an interesting book

such a difficult question

Сравните:

The book is so interesting.

It is such an interesting book.""",
            },

            {
                "order": 12,
                "title": "Наречия частоты",
                "body": """Частые наречия частоты:

always

usually

often

sometimes

rarely

hardly ever

never

Перед смысловым глаголом:

I often read.

She usually arrives early.

После TO BE:

She is always busy.

He is usually late.

После вспомогательного глагола:

I have never seen it.

She can always help.""",
            },

            {
                "order": 13,
                "title": "Порядок наречий",
                "body": """Наречие образа действия обычно ставится после глагола или дополнения.

Правильно:

She speaks English fluently.

Менее естественно:

She speaks fluently English.

Часто используется порядок:

manner + place + time

Пример:

She spoke quietly in the office yesterday.

quietly — как

in the office — где

yesterday — когда""",
            },

            {
                "order": 14,
                "title": "Как выбрать форму",
                "body": """Слово описывает существительное?

→ adjective

She is a careful driver.

Слово описывает действие?

→ adverb

She drives carefully.

После be, look, feel, sound, smell, taste?

→ часто adjective

The soup smells good.

Это fast, hard, late или early?

Форма наречия может совпадать с прилагательным:

drive fast

work hard

arrive late

get up early""",
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
                "prompt": "He is a very ___ student.",
                "options": [
                    "carefully",
                    "careful",
                    "well",
                    "slowly",
                ],
                "answer": "careful",
                "explanation": (
                    "Student — существительное, поэтому нужен adjective."
                ),
            },

            {
                "order": 2,
                "prompt": "He studies very ___.",
                "options": [
                    "careful",
                    "carefully",
                    "good",
                    "carefulness",
                ],
                "answer": "carefully",
                "explanation": (
                    "Слово описывает действие studies → adverb."
                ),
            },

            {
                "order": 3,
                "prompt": "She answered the question ___.",
                "options": [
                    "correct",
                    "correctly",
                    "correctness",
                    "more correct",
                ],
                "answer": "correctly",
                "explanation": (
                    "Answered — действие, поэтому correctly."
                ),
            },

            {
                "order": 4,
                "prompt": "The answer was ___.",
                "options": [
                    "correctly",
                    "correct",
                    "correction",
                    "correcting",
                ],
                "answer": "correct",
                "explanation": (
                    "После was для описания answer нужен adjective."
                ),
            },

            {
                "order": 5,
                "prompt": "The baby is sleeping ___.",
                "options": [
                    "quiet",
                    "quietly",
                    "quietness",
                    "quieter adjective only",
                ],
                "answer": "quietly",
                "explanation": (
                    "Quietly описывает действие sleeping."
                ),
            },

            {
                "order": 6,
                "prompt": "The room is very ___.",
                "options": [
                    "quietly",
                    "quiet",
                    "quietness",
                    "silence",
                ],
                "answer": "quiet",
                "explanation": (
                    "После is используется adjective quiet."
                ),
            },

            {
                "order": 7,
                "prompt": "She speaks French very ___.",
                "options": [
                    "good",
                    "well",
                    "goodly",
                    "bestly",
                ],
                "answer": "well",
                "explanation": (
                    "Good — adjective, well — adverb."
                ),
            },

            {
                "order": 8,
                "prompt": "She is a ___ French teacher.",
                "options": [
                    "well",
                    "good",
                    "goodly",
                    "carefully",
                ],
                "answer": "good",
                "explanation": (
                    "Teacher — существительное → good."
                ),
            },

            {
                "order": 9,
                "prompt": "You look ___ today.",
                "options": [
                    "happily",
                    "happy",
                    "happiness",
                    "wellly",
                ],
                "answer": "happy",
                "explanation": (
                    "После look для описания внешнего вида используется adjective."
                ),
            },

            {
                "order": 10,
                "prompt": "The children played ___.",
                "options": [
                    "happy",
                    "happily",
                    "happiness",
                    "happier adjective only",
                ],
                "answer": "happily",
                "explanation": (
                    "Played — действие → happily."
                ),
            },

            {
                "order": 11,
                "prompt": "He runs very ___.",
                "options": [
                    "fast",
                    "fastly",
                    "fasterly",
                    "speed",
                ],
                "answer": "fast",
                "explanation": (
                    "Fast может быть наречием; fastly не используется."
                ),
            },

            {
                "order": 12,
                "prompt": "She works ___.",
                "options": [
                    "hardly, meaning diligently",
                    "hard",
                    "hardily",
                    "hardness",
                ],
                "answer": "hard",
                "explanation": (
                    "Work hard = работать усердно."
                ),
            },

            {
                "order": 13,
                "prompt": "I can ___ understand him.",
                "options": [
                    "hard",
                    "hardly",
                    "harder",
                    "hardworking",
                ],
                "answer": "hardly",
                "explanation": (
                    "Hardly = едва, почти не."
                ),
            },

            {
                "order": 14,
                "prompt": "The food tastes ___.",
                "options": [
                    "wonderfully",
                    "wonderful",
                    "wonder",
                    "wellly",
                ],
                "answer": "wonderful",
                "explanation": (
                    "После taste для описания качества используется adjective."
                ),
            },

            {
                "order": 15,
                "prompt": "They completed the project ___.",
                "options": [
                    "successful",
                    "successfully",
                    "success",
                    "more success",
                ],
                "answer": "successfully",
                "explanation": (
                    "Completed — действие → successfully."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She speaks English good.",
                    "She speaks English well.",
                    "She speaks English goodly.",
                    "She well speaks English good.",
                ],
                "answer": "She speaks English well.",
                "explanation": (
                    "Действие speaks описывается наречием well."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "He is carefully.",
                    "He is careful.",
                    "He carefully is.",
                    "He is carefulness.",
                ],
                "answer": "He is careful.",
                "explanation": (
                    "После be для описания подлежащего нужен adjective."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "He drives careful.",
                    "He drives carefully.",
                    "He carefully driver.",
                    "He drives carefulness.",
                ],
                "answer": "He drives carefully.",
                "explanation": (
                    "Действие drives описывается adverb carefully."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct HARD/HARDLY pair.",
                "options": [
                    (
                        "She works hard. / "
                        "She hardly works."
                    ),
                    (
                        "She works hardly diligently. / "
                        "She hard works."
                    ),
                    (
                        "She works hardily. / "
                        "She hardly means strongly."
                    ),
                    (
                        "She works hardness. / "
                        "She work hardly hard."
                    ),
                ],
                "answer": (
                    "She works hard. / "
                    "She hardly works."
                ),
                "explanation": (
                    "Hard = усердно; hardly = почти не."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the correct LATE/LATELY pair.",
                "options": [
                    (
                        "He arrived late. / "
                        "I haven't seen him lately."
                    ),
                    (
                        "He arrived lately yesterday. / "
                        "I haven't seen him late recently."
                    ),
                    (
                        "He late arrived. / "
                        "I lately him see."
                    ),
                    (
                        "He arrived latefully. / "
                        "I haven't seen him latest."
                    ),
                ],
                "answer": (
                    "He arrived late. / "
                    "I haven't seen him lately."
                ),
                "explanation": (
                    "Late = поздно; lately = в последнее время."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct sentence after LOOK.",
                "options": [
                    "You look beautifully.",
                    "You look beautiful.",
                    "You beautifully look.",
                    "You look beauty.",
                ],
                "answer": "You look beautiful.",
                "explanation": (
                    "Look + adjective для описания внешнего вида."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct word order.",
                "options": [
                    "She speaks fluently English.",
                    "She speaks English fluently.",
                    "She English fluently speaks always.",
                    "She speaks English fluent.",
                ],
                "answer": "She speaks English fluently.",
                "explanation": (
                    "Если есть дополнение, adverb обычно ставится после него."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct SO/SUCH pair.",
                "options": [
                    (
                        "The book is so interesting. / "
                        "It is such an interesting book."
                    ),
                    (
                        "The book is such interesting. / "
                        "It is so an interesting book."
                    ),
                    (
                        "The book so is interesting. / "
                        "It is such interesting."
                    ),
                    (
                        "The book is so an interesting. / "
                        "It is such interesting book."
                    ),
                ],
                "answer": (
                    "The book is so interesting. / "
                    "It is such an interesting book."
                ),
                "explanation": (
                    "SO + adjective; SUCH + a/an + adjective + noun."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "careful → carefully / "
                        "easy → easily / "
                        "good → well / "
                        "fast → fast / "
                        "hard → hard"
                    ),
                    (
                        "careful → carefuly / "
                        "easy → easyly / "
                        "good → goodly / "
                        "fast → fastly / "
                        "hard → hardly"
                    ),
                    (
                        "careful → care / "
                        "easy → easiness / "
                        "good → bestly / "
                        "fast → quickly fast / "
                        "hard → hardily"
                    ),
                    (
                        "careful → more careful adverb / "
                        "easy → easilyly / "
                        "good → wellly / "
                        "fast → fastestly / "
                        "hard → hardestly"
                    ),
                ],
                "answer": (
                    "careful → carefully / "
                    "easy → easily / "
                    "good → well / "
                    "fast → fast / "
                    "hard → hard"
                ),
                "explanation": (
                    "Это основные формы adjective → adverb из урока."
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
                "✅ A1 Lesson 44 seeded: Adjectives and Adverbs"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
