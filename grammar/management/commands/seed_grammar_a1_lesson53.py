from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 53: "
        "Question Tags."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=53,
            defaults={
                "title": "Разделительные вопросы — Question Tags",
                "slug": "question-tags",
                "theory_text": (
                    "Question Tags: auxiliary verbs, "
                    "opposite polarity and special cases."
                ),
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Question Tag",
                "body": """Разделительный вопрос состоит из двух частей:

1. основного предложения;

2. короткого вопроса в конце.

Пример:

You are tired, aren't you?

Такие вопросы используются, когда говорящий:

ожидает подтверждения;

проверяет информацию;

не уверен;

поддерживает разговор.""",
            },

            {
                "order": 2,
                "title": "Главное правило",
                "body": """Если основное предложение положительное:

→ хвостик отрицательный.

She is ready, isn't she?

You work here, don't you?

Если основное предложение отрицательное:

→ хвостик положительный.

She isn't ready, is she?

You don't work here, do you?

Главная схема:

positive → negative tag

negative → positive tag""",
            },

            {
                "order": 3,
                "title": "Как выбрать вспомогательный глагол",
                "body": """В question tag нужно повторить вспомогательный или модальный глагол.

She is busy, isn't she?

They have finished, haven't they?

He will come, won't he?

She can swim, can't she?

Если в Present Simple или Past Simple вспомогательного глагола не видно:

work → do/does

worked → did

Примеры:

He works here, doesn't he?

They arrived, didn't they?""",
            },

            {
                "order": 4,
                "title": "TO BE: AM, IS, ARE, WAS, WERE",
                "body": """С TO BE используется тот же глагол.

Present:

She is at home, isn't she?

They are ready, aren't they?

Отрицание:

She isn't at home, is she?

Past:

She was tired, wasn't she?

They were ready, weren't they?

Отрицание:

She wasn't tired, was she?

They weren't ready, were they?""",
            },

            {
                "order": 5,
                "title": "Особый случай I AM",
                "body": """После:

I am...

используется:

aren't I?

Примеры:

I am late, aren't I?

I am right, aren't I?

Не:

amn't I?

После отрицания:

I'm not late, am I?

I'm not disturbing you, am I?""",
            },

            {
                "order": 6,
                "title": "Present Simple и Past Simple",
                "body": """Present Simple:

You work here, don't you?

She speaks English, doesn't she?

Отрицание:

You don't work here, do you?

She doesn't speak English, does she?

Past Simple:

You called him, didn't you?

She arrived early, didn't she?

Отрицание:

You didn't call him, did you?

She didn't arrive early, did she?""",
            },

            {
                "order": 7,
                "title": "Continuous, Perfect и Future",
                "body": """Present Continuous:

She is working, isn't she?

Past Continuous:

They were waiting, weren't they?

Present Perfect:

You have finished, haven't you?

She has called, hasn't she?

Past Perfect:

She had left, hadn't she?

Future Simple:

He will come, won't he?

Отрицательные формы используют положительный tag.""",
            },

            {
                "order": 8,
                "title": "Модальные глаголы",
                "body": """С модальными глаголами повторяем сам modal.

CAN:

She can swim, can't she?

He can't drive, can he?

COULD:

You could help, couldn't you?

SHOULD:

We should leave, shouldn't we?

MUST:

You must go, mustn't you?

Modal в основной части определяет modal в хвостике.""",
            },

            {
                "order": 9,
                "title": "THERE, THIS, THAT, THESE, THOSE",
                "body": """С THERE IS / THERE ARE слово THERE сохраняется.

There is a problem, isn't there?

There are many students, aren't there?

THIS и THAT заменяются на IT.

This is your book, isn't it?

That was interesting, wasn't it?

THESE и THOSE заменяются на THEY.

These are your keys, aren't they?

Those were expensive, weren't they?""",
            },

            {
                "order": 10,
                "title": "Someone, Nobody, Nothing",
                "body": """После:

someone

somebody

everyone

everybody

no one

nobody

обычно используется THEY.

Someone called, didn't they?

Nobody came, did they?

После:

something

everything

nothing

используется IT.

Nothing happened, did it?

Everything is ready, isn't it?""",
            },

            {
                "order": 11,
                "title": "Слова с отрицательным значением",
                "body": """Некоторые слова уже имеют отрицательное значение:

never

rarely

seldom

hardly

scarcely

barely

Поэтому хвостик будет положительным.

He never calls, does he?

She rarely complains, does she?

They hardly know us, do they?

Также:

Nobody called, did they?

Nothing happened, did it?""",
            },

            {
                "order": 12,
                "title": "LITTLE, FEW, A LITTLE, A FEW",
                "body": """LITTLE и FEW без артикля имеют отрицательное значение:

мало;

почти нет.

Поэтому tag положительный:

He has little time, does he?

Few people understand this, do they?

A LITTLE и A FEW имеют положительное значение:

немного;

несколько.

Поэтому tag отрицательный:

He has a little time, doesn't he?

A few students passed, didn't they?""",
            },

            {
                "order": 13,
                "title": "Команды и LET'S",
                "body": """После повелительного предложения часто используется:

will you?

Open the door, will you?

Wait here, will you?

Don't be late, will you?

Более мягко:

would you?

Close the window, would you?

После LET'S используется:

shall we?

Let's go, shall we?

Let's start, shall we?

Не:

Let's go, will we?""",
            },

            {
                "order": 14,
                "title": "Алгоритм Question Tag",
                "body": """Шаг 1.

Определите: предложение положительное или отрицательное.

Шаг 2.

Найдите вспомогательный или модальный глагол.

Шаг 3.

Сделайте противоположную форму:

is → isn't

doesn't → does

will → won't

can't → can

Шаг 4.

Замените подлежащее местоимением.

Anna → she

Marat → he

students → they

this → it

Шаг 5.

Проверьте особые случаи:

I am → aren't I?

Let's → shall we?

приказ → will you?

Nobody → they

Nothing → it

Never/rarely/hardly → положительный tag.""",
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
                "prompt": "She is your sister, ___?",
                "options": [
                    "is she",
                    "isn't she",
                    "doesn't she",
                    "wasn't she",
                ],
                "answer": "isn't she",
                "explanation": (
                    "Положительное is → отрицательное isn't."
                ),
            },

            {
                "order": 2,
                "prompt": "They aren't at home, ___?",
                "options": [
                    "aren't they",
                    "are they",
                    "do they",
                    "were they",
                ],
                "answer": "are they",
                "explanation": (
                    "Отрицательное aren't → положительное are."
                ),
            },

            {
                "order": 3,
                "prompt": "You like coffee, ___?",
                "options": [
                    "do you",
                    "don't you",
                    "aren't you",
                    "didn't you",
                ],
                "answer": "don't you",
                "explanation": (
                    "Present Simple, you → don't you?"
                ),
            },

            {
                "order": 4,
                "prompt": "He doesn't drive, ___?",
                "options": [
                    "doesn't he",
                    "does he",
                    "is he",
                    "did he",
                ],
                "answer": "does he",
                "explanation": (
                    "Отрицательное doesn't → does."
                ),
            },

            {
                "order": 5,
                "prompt": "She arrived yesterday, ___?",
                "options": [
                    "didn't she",
                    "doesn't she",
                    "wasn't she",
                    "did she",
                ],
                "answer": "didn't she",
                "explanation": (
                    "Past Simple → did; предложение положительное."
                ),
            },

            {
                "order": 6,
                "prompt": "They haven't finished, ___?",
                "options": [
                    "haven't they",
                    "have they",
                    "do they",
                    "did they",
                ],
                "answer": "have they",
                "explanation": (
                    "Отрицательный Present Perfect → have they?"
                ),
            },

            {
                "order": 7,
                "prompt": "He can swim, ___?",
                "options": [
                    "can he",
                    "can't he",
                    "doesn't he",
                    "isn't he",
                ],
                "answer": "can't he",
                "explanation": (
                    "Can повторяется в tag."
                ),
            },

            {
                "order": 8,
                "prompt": "You won't be late, ___?",
                "options": [
                    "won't you",
                    "will you",
                    "do you",
                    "are you",
                ],
                "answer": "will you",
                "explanation": (
                    "Won't → положительный will."
                ),
            },

            {
                "order": 9,
                "prompt": "There is a problem, ___?",
                "options": [
                    "is it",
                    "isn't it",
                    "isn't there",
                    "is there not it",
                ],
                "answer": "isn't there",
                "explanation": (
                    "После there is слово there сохраняется."
                ),
            },

            {
                "order": 10,
                "prompt": "These are your keys, ___?",
                "options": [
                    "aren't these",
                    "aren't they",
                    "isn't it",
                    "are they",
                ],
                "answer": "aren't they",
                "explanation": (
                    "These → they."
                ),
            },

            {
                "order": 11,
                "prompt": "Someone called, ___?",
                "options": [
                    "didn't he",
                    "didn't they",
                    "did they",
                    "wasn't it",
                ],
                "answer": "didn't they",
                "explanation": (
                    "Someone → they; положительное Past Simple → didn't."
                ),
            },

            {
                "order": 12,
                "prompt": "Nobody knows, ___?",
                "options": [
                    "doesn't he",
                    "do they",
                    "don't they",
                    "does nobody",
                ],
                "answer": "do they",
                "explanation": (
                    "Nobody отрицательно по смыслу → положительный tag."
                ),
            },

            {
                "order": 13,
                "prompt": "Nothing is wrong, ___?",
                "options": [
                    "isn't it",
                    "is it",
                    "are they",
                    "does it",
                ],
                "answer": "is it",
                "explanation": (
                    "Nothing → it и считается отрицательным."
                ),
            },

            {
                "order": 14,
                "prompt": "He rarely goes out, ___?",
                "options": [
                    "doesn't he",
                    "does he",
                    "isn't he",
                    "did he",
                ],
                "answer": "does he",
                "explanation": (
                    "Rarely имеет отрицательное значение → positive tag."
                ),
            },

            {
                "order": 15,
                "prompt": "Open the window, ___?",
                "options": [
                    "shall we",
                    "do you",
                    "will you",
                    "aren't you",
                ],
                "answer": "will you",
                "explanation": (
                    "После imperative часто используется will you?"
                ),
            },

            {
                "order": 16,
                "prompt": "I am late, ___?",
                "options": [
                    "am I",
                    "amn't I",
                    "aren't I",
                    "don't I",
                ],
                "answer": "aren't I",
                "explanation": (
                    "Особый случай: I am → aren't I?"
                ),
            },

            {
                "order": 17,
                "prompt": "Let's start, ___?",
                "options": [
                    "will we",
                    "do we",
                    "shall we",
                    "aren't we",
                ],
                "answer": "shall we",
                "explanation": (
                    "После Let's используется shall we?"
                ),
            },

            {
                "order": 18,
                "prompt": "This is your book, ___?",
                "options": [
                    "isn't this",
                    "isn't it",
                    "doesn't it",
                    "is it",
                ],
                "answer": "isn't it",
                "explanation": (
                    "This → it."
                ),
            },

            {
                "order": 19,
                "prompt": "Everything is ready, ___?",
                "options": [
                    "aren't they",
                    "isn't it",
                    "is it",
                    "doesn't it",
                ],
                "answer": "isn't it",
                "explanation": (
                    "Everything → it."
                ),
            },

            {
                "order": 20,
                "prompt": "Few people understand this, ___?",
                "options": [
                    "don't they",
                    "do they",
                    "doesn't he",
                    "did they",
                ],
                "answer": "do they",
                "explanation": (
                    "Few имеет отрицательное значение → positive tag."
                ),
            },

            {
                "order": 21,
                "prompt": "A few students passed, ___?",
                "options": [
                    "did they",
                    "didn't they",
                    "do they",
                    "weren't they",
                ],
                "answer": "didn't they",
                "explanation": (
                    "A few имеет положительное значение."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "He never calls, doesn't he?",
                    "He never calls, does he?",
                    "He never calls, isn't he?",
                    "He never calls, did he?",
                ],
                "answer": "He never calls, does he?",
                "explanation": (
                    "Never отрицательно по смыслу → positive tag."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct special-case pair.",
                "options": [
                    (
                        "I am right, aren't I? / "
                        "Let's go, shall we?"
                    ),
                    (
                        "I am right, amn't I? / "
                        "Let's go, will we?"
                    ),
                    (
                        "I am right, don't I? / "
                        "Let's go, do we?"
                    ),
                    (
                        "I am right, isn't I? / "
                        "Let's go, won't we?"
                    ),
                ],
                "answer": (
                    "I am right, aren't I? / "
                    "Let's go, shall we?"
                ),
                "explanation": (
                    "Это два основных особых случая."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "She is ready, isn't she? / "
                        "He works here, doesn't he? / "
                        "They came early, didn't they? / "
                        "Nobody called, did they? / "
                        "Nothing happened, did it?"
                    ),
                    (
                        "She is ready, is she? / "
                        "He works here, isn't he? / "
                        "They came early, weren't they? / "
                        "Nobody called, didn't they? / "
                        "Nothing happened, didn't it?"
                    ),
                    (
                        "She is ready, doesn't she? / "
                        "He works here, don't he? / "
                        "They came early, doesn't they? / "
                        "Nobody called, was they? / "
                        "Nothing happened, does it?"
                    ),
                    (
                        "She is ready, aren't she? / "
                        "He works here, does he? / "
                        "They came early, do they? / "
                        "Nobody called, don't they? / "
                        "Nothing happened, wasn't it?"
                    ),
                ],
                "answer": (
                    "She is ready, isn't she? / "
                    "He works here, doesn't he? / "
                    "They came early, didn't they? / "
                    "Nobody called, did they? / "
                    "Nothing happened, did it?"
                ),
                "explanation": (
                    "Нужно выбрать правильный auxiliary, "
                    "противоположную форму и подходящее pronoun."
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
                "✅ A1 Lesson 53 seeded: Question Tags"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
