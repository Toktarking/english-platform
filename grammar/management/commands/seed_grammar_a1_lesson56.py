from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 56: "
        "Comparative Structures."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=56,
            defaults={
                "title": (
                    "Сравнительные конструкции: "
                    "as…as, too, enough, so, such"
                ),
                "slug": "comparative-structures-as-too-enough-so-such",
                "theory_text": (
                    "Comparative structures: as...as, too, "
                    "enough, so and such."
                ),
                "estimated_minutes": 50,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "AS…AS — равенство",
                "body": """Конструкция AS…AS показывает равенство.

Формула:

as + adjective + as

Примеры:

She is as tall as her sister.

This book is as interesting as that one.

My car is as fast as yours.

С наречием:

as + adverb + as

She speaks as clearly as her teacher.

He works as carefully as his colleague.""",
            },

            {
                "order": 2,
                "title": "NOT AS…AS — неравенство",
                "body": """NOT AS…AS означает:

не такой… как;

не настолько… как.

Формула:

not as + adjective/adverb + as

Примеры:

This room is not as large as that one.

My phone is not as expensive as yours.

He doesn't work as quickly as she does.

Сравните:

Tom is taller than Jack.

Jack is not as tall as Tom.""",
            },

            {
                "order": 3,
                "title": "AS MUCH, AS MANY, AS LITTLE, AS FEW",
                "body": """С неисчисляемыми существительными:

as much + noun + as

I don't have as much time as you.

С исчисляемыми:

as many + plural noun + as

She has as many books as I do.

Малое количество:

as little + uncountable noun + as

as few + plural noun + as

Try to use as little sugar as possible.

Try to make as few mistakes as possible.""",
            },

            {
                "order": 4,
                "title": "AS…AS POSSIBLE и TWICE AS…AS",
                "body": """AS…AS POSSIBLE означает:

как можно…

Примеры:

Come as soon as possible.

Speak as clearly as possible.

Finish as quickly as possible.

Для сравнения во сколько раз:

twice as + adjective + as

This house is twice as big as ours.

three times as + adjective + as

This building is three times as tall as that one.""",
            },

            {
                "order": 5,
                "title": "THE SAME AS и DIFFERENT FROM",
                "body": """THE SAME AS означает:

такой же, как;

то же самое, что.

My phone is the same as yours.

She has the same bag as me.

DIFFERENT FROM означает:

отличающийся от.

My opinion is different from yours.

This book is different from the first one.

Для учебных заданий лучше использовать:

different from""",
            },

            {
                "order": 6,
                "title": "TOO — слишком",
                "body": """TOO означает:

слишком.

Обычно оно показывает чрезмерность и проблему.

Формула:

too + adjective/adverb

Примеры:

too expensive

too difficult

too quickly

too late

Сравните:

The coffee is very hot.
— очень горячий.

The coffee is too hot to drink.
— слишком горячий, чтобы пить.""",
            },

            {
                "order": 7,
                "title": "TOO + TO / FOR",
                "body": """Формула:

too + adjective + to + V1

Примеры:

The box is too heavy to carry.

He is too tired to work.

She is too young to drive.

С человеком:

too + adjective + for + person

This task is too difficult for me.

The shoes are too small for him.

Too часто означает, что действие невозможно или проблематично.""",
            },

            {
                "order": 8,
                "title": "TOO MUCH, TOO MANY, TOO LITTLE, TOO FEW",
                "body": """TOO MUCH используется с неисчисляемыми:

too much money

too much work

too much information

TOO MANY — с исчисляемыми во множественном числе:

too many people

too many mistakes

TOO LITTLE — слишком мало неисчисляемого:

too little time

TOO FEW — слишком мало исчисляемого:

too few students""",
            },

            {
                "order": 9,
                "title": "ENOUGH — достаточно",
                "body": """ENOUGH означает:

достаточно.

Позиция зависит от части речи.

После adjective:

old enough

strong enough

warm enough

После adverb:

quickly enough

clearly enough

Перед noun:

enough time

enough money

enough chairs

Важно:

old enough

не:

enough old""",
            },

            {
                "order": 10,
                "title": "ENOUGH + TO / FOR",
                "body": """Формула:

adjective/adverb + enough + to + V1

Примеры:

He is old enough to drive.

She spoke clearly enough to be understood.

The room is large enough to hold fifty people.

С FOR:

There is enough food for everyone.

This task is easy enough for beginners.

We have enough money for the trip.""",
            },

            {
                "order": 11,
                "title": "TOO и ENOUGH",
                "body": """TOO показывает чрезмерность.

ENOUGH показывает достаточность.

Сравните:

The box is too heavy to carry.

The box is not light enough to carry.

He is too young to drive.

He is not old enough to drive.

Часто можно преобразовать:

too expensive

→ not cheap enough

too difficult

→ not easy enough

too weak

→ not strong enough""",
            },

            {
                "order": 12,
                "title": "SO и SO…THAT",
                "body": """SO используется перед adjective или adverb.

Формула:

so + adjective/adverb

Примеры:

so beautiful

so tired

so quickly

SO…THAT показывает результат.

Формула:

so + adjective/adverb + that + result

The film was so boring that I fell asleep.

She was so tired that she couldn't work.

Также:

so much + uncountable noun

so many + plural noun""",
            },

            {
                "order": 13,
                "title": "SUCH и SUCH…THAT",
                "body": """SUCH используется перед существительным или noun phrase.

Singular countable:

such + a/an + adjective + noun

such a beautiful city

such an interesting book

Plural:

such + adjective + plural noun

such friendly people

Uncountable:

such + adjective + uncountable noun

such useful information

SUCH…THAT:

It was such a boring film that I fell asleep.""",
            },

            {
                "order": 14,
                "title": "Как выбрать конструкцию",
                "body": """Нужно показать равенство?

→ as…as

Неравенство?

→ not as…as

Качество чрезмерное и создаёт проблему?

→ too

Качества или количества достаточно?

→ enough

Нужно усилить adjective/adverb?

→ so

Нужно усилить noun phrase?

→ such

Нужно показать результат?

→ so…that / such…that

Главное:

so + adjective/adverb

such + noun phrase""",
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
                "prompt": (
                    "My brother is ___ tall as my father."
                ),
                "options": [
                    "as",
                    "so that",
                    "too",
                    "enough",
                ],
                "answer": "as",
                "explanation": (
                    "Равенство → as + adjective + as."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "This book is not ___ interesting "
                    "as the first one."
                ),
                "options": [
                    "too",
                    "as",
                    "enough",
                    "such",
                ],
                "answer": "as",
                "explanation": (
                    "Неравенство → not as...as."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "She doesn't have ___ much experience "
                    "as her colleague."
                ),
                "options": [
                    "too",
                    "so",
                    "as",
                    "enough",
                ],
                "answer": "as",
                "explanation": (
                    "Experience неисчисляемое → as much...as."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "He has twice ___ many clients as last year."
                ),
                "options": [
                    "so",
                    "too",
                    "as",
                    "enough",
                ],
                "answer": "as",
                "explanation": (
                    "Формула: twice as many...as."
                ),
            },

            {
                "order": 5,
                "prompt": "The coffee is ___ hot to drink.",
                "options": [
                    "very",
                    "too",
                    "such",
                    "enough",
                ],
                "answer": "too",
                "explanation": (
                    "Слишком горячий, чтобы пить → too."
                ),
            },

            {
                "order": 6,
                "prompt": "The room is warm ___.",
                "options": [
                    "too",
                    "enough",
                    "so a",
                    "such",
                ],
                "answer": "enough",
                "explanation": (
                    "После adjective: warm enough."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "We don't have ___ chairs for everyone."
                ),
                "options": [
                    "too",
                    "enough",
                    "so",
                    "such",
                ],
                "answer": "enough",
                "explanation": (
                    "Перед существительным: enough chairs."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "The film was ___ boring that I fell asleep."
                ),
                "options": [
                    "such",
                    "so",
                    "too much",
                    "enough",
                ],
                "answer": "so",
                "explanation": (
                    "SO + adjective + THAT."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "It was ___ boring film that I fell asleep."
                ),
                "options": [
                    "so a",
                    "such a",
                    "too a",
                    "enough a",
                ],
                "answer": "such a",
                "explanation": (
                    "SUCH + a + adjective + singular noun."
                ),
            },

            {
                "order": 10,
                "prompt": "She gave me ___ useful advice.",
                "options": [
                    "such",
                    "such a",
                    "so",
                    "too many",
                ],
                "answer": "such",
                "explanation": (
                    "Advice неисчисляемое → such useful advice."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "There were ___ many questions "
                    "that we couldn't answer them all."
                ),
                "options": [
                    "such",
                    "so",
                    "enough",
                    "as",
                ],
                "answer": "so",
                "explanation": (
                    "Формула: so many + plural noun + that."
                ),
            },

            {
                "order": 12,
                "prompt": "I have ___ much work to do today.",
                "options": [
                    "too",
                    "too many",
                    "enough many",
                    "such a",
                ],
                "answer": "too",
                "explanation": (
                    "Work неисчисляемое → too much work."
                ),
            },

            {
                "order": 13,
                "prompt": (
                    "There are ___ few students in the class."
                ),
                "options": [
                    "too",
                    "too much",
                    "such a",
                    "enough of",
                ],
                "answer": "too",
                "explanation": (
                    "Too few + plural noun."
                ),
            },

            {
                "order": 14,
                "prompt": "He didn't speak clearly ___.",
                "options": [
                    "too",
                    "enough",
                    "so that",
                    "such",
                ],
                "answer": "enough",
                "explanation": (
                    "После adverb: clearly enough."
                ),
            },

            {
                "order": 15,
                "prompt": "This phone is the same ___ mine.",
                "options": [
                    "than",
                    "as",
                    "from",
                    "like as",
                ],
                "answer": "as",
                "explanation": (
                    "Правильная конструкция: the same as."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She is as taller as her sister.",
                    "She is as tall as her sister.",
                    "She is as tall than her sister.",
                    "She is so tall as her sister equality.",
                ],
                "answer": "She is as tall as her sister.",
                "explanation": (
                    "После as используется обычная форма adjective."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct ENOUGH sentence.",
                "options": [
                    "He is enough old to drive.",
                    "He is old enough to drive.",
                    "He is old enough driving.",
                    "He enough is old to drive.",
                ],
                "answer": "He is old enough to drive.",
                "explanation": (
                    "Adjective + enough + to + V1."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence with TOO.",
                "options": [
                    "The box is too heavy to carry.",
                    "The box is heavy too carry.",
                    "The box is too heavy carrying.",
                    "The box is enough heavy to carry.",
                ],
                "answer": "The box is too heavy to carry.",
                "explanation": (
                    "Too + adjective + to + V1."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct SO/SUCH pair.",
                "options": [
                    (
                        "The city is so beautiful. / "
                        "It is such a beautiful city."
                    ),
                    (
                        "The city is such beautiful. / "
                        "It is so a beautiful city."
                    ),
                    (
                        "The city is so a beautiful. / "
                        "It is such beautiful city."
                    ),
                    (
                        "The city is suchly beautiful. / "
                        "It is so beautiful a city only basic."
                    ),
                ],
                "answer": (
                    "The city is so beautiful. / "
                    "It is such a beautiful city."
                ),
                "explanation": (
                    "SO + adjective; SUCH + noun phrase."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the correct MUCH/MANY pair.",
                "options": [
                    (
                        "too much money / "
                        "too many books"
                    ),
                    (
                        "too many money / "
                        "too much books"
                    ),
                    (
                        "too much students / "
                        "too many information"
                    ),
                    (
                        "too many work / "
                        "too much people"
                    ),
                ],
                "answer": (
                    "too much money / "
                    "too many books"
                ),
                "explanation": (
                    "Much → uncountable; many → countable plural."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "Choose the correct transformation."
                ),
                "options": [
                    (
                        "He is too young to drive. → "
                        "He is not old enough to drive."
                    ),
                    (
                        "He is too young to drive. → "
                        "He is enough old not to drive."
                    ),
                    (
                        "He is too young to drive. → "
                        "He is not too old enough."
                    ),
                    (
                        "He is too young to drive. → "
                        "He has not enough old."
                    ),
                ],
                "answer": (
                    "He is too young to drive. → "
                    "He is not old enough to drive."
                ),
                "explanation": (
                    "Too + adjective можно передать через "
                    "not + opposite adjective + enough."
                ),
            },

            {
                "order": 22,
                "prompt": (
                    "Choose the correct AS MUCH / AS MANY pair."
                ),
                "options": [
                    (
                        "as much time as / "
                        "as many books as"
                    ),
                    (
                        "as many time as / "
                        "as much books as"
                    ),
                    (
                        "as much students as / "
                        "as many money as"
                    ),
                    (
                        "as many information as / "
                        "as much people as"
                    ),
                ],
                "answer": (
                    "as much time as / "
                    "as many books as"
                ),
                "explanation": (
                    "Much → uncountable; many → countable."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct result pair."
                ),
                "options": [
                    (
                        "The film was so boring that I fell asleep. / "
                        "It was such a boring film that I fell asleep."
                    ),
                    (
                        "The film was such boring that I fell asleep. / "
                        "It was so a boring film that I fell asleep."
                    ),
                    (
                        "The film was so boring film that I fell asleep. / "
                        "It was such boring a film that I fell asleep."
                    ),
                    (
                        "The film was too boring that I fell asleep. / "
                        "It was enough boring film that I fell asleep."
                    ),
                ],
                "answer": (
                    "The film was so boring that I fell asleep. / "
                    "It was such a boring film that I fell asleep."
                ),
                "explanation": (
                    "SO относится к adjective; SUCH — к noun phrase."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "equality → as...as / "
                        "excess → too / "
                        "sufficiency → enough / "
                        "adjective/adverb emphasis → so / "
                        "noun phrase emphasis → such"
                    ),
                    (
                        "equality → too / "
                        "excess → enough / "
                        "sufficiency → such / "
                        "adjective → as many / "
                        "noun → so"
                    ),
                    (
                        "equality → such / "
                        "excess → as...as / "
                        "sufficiency → too / "
                        "adjective → such / "
                        "noun → enough adjective"
                    ),
                    (
                        "equality → enough / "
                        "excess → so / "
                        "sufficiency → too / "
                        "adjective → such a / "
                        "noun → as...as"
                    ),
                ],
                "answer": (
                    "equality → as...as / "
                    "excess → too / "
                    "sufficiency → enough / "
                    "adjective/adverb emphasis → so / "
                    "noun phrase emphasis → such"
                ),
                "explanation": (
                    "Это основная система выбора конструкций урока."
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
                "✅ A1 Lesson 56 seeded: Comparative Structures"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
