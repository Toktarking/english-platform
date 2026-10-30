from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 22: "
        "Present Continuous negatives and questions."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=22,
            defaults={
                "title": (
                    "Present Continuous: "
                    "отрицания и вопросы"
                ),
                "slug": "present-continuous-negatives-questions",
                "theory_text": (
                    "Present Continuous negatives "
                    "and questions."
                ),
                "estimated_minutes": 35,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Отрицание в Present Continuous",
                "body": """Чтобы сделать отрицание, после am, is или are ставится not.

Формула:

Подлежащее + am/is/are + not + глагол-ing

Примеры:

I am not working.

She is not reading.

They are not playing.

Важно:

глагол с -ing остаётся без изменений.""",
            },

            {
                "order": 2,
                "title": "I'M NOT, ISN'T, AREN'T",
                "body": """С I:

I am not working.

Сокращённо:

I'm not working.

Форма I amn't в стандартном английском обычно не используется.

С he/she/it:

He isn't working.

She's not reading.

С you/we/they:

They aren't waiting.

We're not studying.

Оба варианта возможны:

she isn't;

she's not.

they aren't;

they're not.""",
            },

            {
                "order": 3,
                "title": "Что означает отрицание",
                "body": """Отрицание может показывать, что действие не происходит сейчас.

Примеры:

I'm not reading now.

She isn't sleeping.

They aren't playing football.

Также оно может описывать отсутствие временной ситуации:

I'm not working this week.

She isn't staying with us this month.

We aren't using this office today.""",
            },

            {
                "order": 4,
                "title": "Общий вопрос",
                "body": """Чтобы задать вопрос, am/is/are переносится перед подлежащим.

Сравните:

She is working.

Is she working?

They are waiting.

Are they waiting?

Формула:

Am/Is/Are + подлежащее + глагол-ing?

Примеры:

Am I speaking too quickly?

Is he sleeping?

Are they waiting?""",
            },

            {
                "order": 5,
                "title": "AM I, IS HE/SHE/IT, ARE YOU/WE/THEY",
                "body": """С I:

Am I doing this correctly?

Am I disturbing you?

С he/she/it:

Is he working?

Is she reading?

Is it raining?

С you/we/they:

Are you listening?

Are we leaving now?

Are they studying?

Важно:

в вопросе am/is/are стоит перед подлежащим.""",
            },

            {
                "order": 6,
                "title": "Краткие ответы",
                "body": """На вопрос с IS:

Is she working?

Yes, she is.

No, she isn't.

На вопрос с ARE:

Are they waiting?

Yes, they are.

No, they aren't.

На вопрос:

Are you working?

Ответ:

Yes, I am.

No, I'm not.

Не используйте do/does:

Is she working?

Не:

Yes, she does.

А:

Yes, she is.""",
            },

            {
                "order": 7,
                "title": "Специальные вопросы",
                "body": """Формула:

Вопросительное слово
+
am/is/are
+
подлежащее
+
глагол-ing?

Примеры:

What are you doing?

Where is she going?

Why are they laughing?

Who is he talking to?

When are we leaving?

Сначала вопросительное слово, затем am/is/are.""",
            },

            {
                "order": 8,
                "title": "WHAT ARE YOU DOING?",
                "body": """What are you doing?

означает:

Что ты делаешь сейчас?

Примеры ответов:

I am reading.

I am working.

I am cooking dinner.

Не путайте:

What do you do?
— Кем вы работаете / чем занимаетесь?

What are you doing?
— Что вы делаете сейчас?""",
            },

            {
                "order": 9,
                "title": "WHERE и WHY",
                "body": """WHERE:

Where are you going?

Where is she working today?

Where are they staying?

Ответ:

I am going home.

She is working at home.

WHY:

Why are you crying?

Why is he laughing?

Why are they leaving?

Ответ часто начинается с because:

Because I am tired.

Because he is happy.""",
            },

            {
                "order": 10,
                "title": "WHO и WHAT как подлежащее",
                "body": """WHO может быть объектом:

Who are you talking to?

Здесь подлежащее — you.

Но WHO может само выполнять действие:

Who is calling?

Who is knocking at the door?

Who is sitting there?

То же с WHAT:

What is happening?

What is making that noise?

What is changing?

В таких случаях who/what сами являются подлежащим.""",
            },

            {
                "order": 11,
                "title": "Вопросы с предлогами",
                "body": """В разговорном английском предлог часто остаётся в конце.

Примеры:

Who are you talking to?

What are you looking at?

Who is she waiting for?

What are they thinking about?

Такой порядок является естественным для обычной речи.""",
            },

            {
                "order": 12,
                "title": "Present Continuous и Present Simple",
                "body": """Present Simple:

Do you work here?

Это вопрос о постоянной работе.

Present Continuous:

Are you working now?

Это вопрос о действии сейчас.

Сравните:

Does she read every day?

Is she reading now?

Do they play football on Sundays?

Are they playing football now?""",
            },

            {
                "order": 13,
                "title": "Глаголы состояния и HAVE",
                "body": """Глаголы состояния обычно используются в Present Simple.

Правильно:

Do you understand?

Does she know the answer?

Do they like this film?

Не:

Are you understanding?

Is she knowing?

Если HAVE означает действие, Continuous возможен:

Are you having breakfast?

Is she having a shower?

Если HAVE означает владение:

Do you have a car?

Не:

Are you having a car?""",
            },

            {
                "order": 14,
                "title": "Главный алгоритм",
                "body": """Отрицание:

subject + am/is/are + not + verb-ing

She isn't working.

Общий вопрос:

Am/Is/Are + subject + verb-ing?

Is she working?

Специальный вопрос:

Question word + am/is/are + subject + verb-ing?

Where is she working?

Важно:

Present Continuous не использует do/does.

Неправильно:

Does she working?

Правильно:

Is she working?""",
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
                "prompt": "I ___ not listening.",
                "options": ["is", "am", "are", "do"],
                "answer": "am",
                "explanation": "С I используется am: I am not listening.",
            },

            {
                "order": 2,
                "prompt": "My brother ___ not sleeping.",
                "options": ["am", "are", "is", "does"],
                "answer": "is",
                "explanation": "My brother = he, поэтому is.",
            },

            {
                "order": 3,
                "prompt": "The children ___ not playing outside.",
                "options": ["is", "am", "are", "do"],
                "answer": "are",
                "explanation": "Children = they, поэтому are.",
            },

            {
                "order": 4,
                "prompt": "___ your sister cooking?",
                "options": ["Do", "Does", "Is", "Are"],
                "answer": "Is",
                "explanation": "Your sister = she: Is your sister cooking?",
            },

            {
                "order": 5,
                "prompt": "___ your parents travelling?",
                "options": ["Is", "Are", "Do", "Does"],
                "answer": "Are",
                "explanation": "Parents = they, поэтому Are.",
            },

            {
                "order": 6,
                "prompt": "Is the baby crying?",
                "options": [
                    "Yes, it is.",
                    "Yes, it does.",
                    "Yes, it cries.",
                    "Yes, it can.",
                ],
                "answer": "Yes, it is.",
                "explanation": "Вопрос начинается с is, поэтому краткий ответ тоже с is.",
            },

            {
                "order": 7,
                "prompt": "Are the students writing?",
                "options": [
                    "No, they don't.",
                    "No, they aren't.",
                    "No, they doesn't.",
                    "No, they not.",
                ],
                "answer": "No, they aren't.",
                "explanation": "Are they...? → No, they aren't.",
            },

            {
                "order": 8,
                "prompt": "What ___ he doing?",
                "options": ["do", "does", "is", "are"],
                "answer": "is",
                "explanation": "He → is: What is he doing?",
            },

            {
                "order": 9,
                "prompt": "Where ___ the children playing?",
                "options": ["is", "are", "do", "does"],
                "answer": "are",
                "explanation": "Children = they, поэтому are.",
            },

            {
                "order": 10,
                "prompt": "Why ___ she crying?",
                "options": ["is", "are", "does", "do"],
                "answer": "is",
                "explanation": "She → is.",
            },

            {
                "order": 11,
                "prompt": "Who ___ knocking at the door?",
                "options": ["are", "is", "do", "does"],
                "answer": "is",
                "explanation": "Who здесь само выполняет действие: Who is knocking?",
            },

            {
                "order": 12,
                "prompt": "Who are you talking ___?",
                "options": ["at", "to", "on", "in"],
                "answer": "to",
                "explanation": "Устойчивая конструкция: talk to someone.",
            },

            {
                "order": 13,
                "prompt": "___ you having lunch?",
                "options": ["Do", "Does", "Are", "Is"],
                "answer": "Are",
                "explanation": "Have означает действие; Present Continuous: Are you having...?",
            },

            {
                "order": 14,
                "prompt": "Do you have a car?",
                "options": [
                    "Yes, I am.",
                    "Yes, I do.",
                    "Yes, I have got doing.",
                    "Yes, I am having.",
                ],
                "answer": "Yes, I do.",
                "explanation": "Have здесь означает владение, поэтому используется Present Simple.",
            },

            {
                "order": 15,
                "prompt": "Are you understanding the rule?",
                "options": [
                    "Correct",
                    'Incorrect; use "Do you understand the rule?"',
                    'Incorrect; use "Are you understand?"',
                    "Correct only in questions.",
                ],
                "answer": 'Incorrect; use "Do you understand the rule?"',
                "explanation": "Understand — глагол состояния и обычно используется в Present Simple.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "She doesn't working.",
                    "She isn't working.",
                    "She not working.",
                    "She isn't work.",
                ],
                "answer": "She isn't working.",
                "explanation": "Present Continuous negative: is not + verb-ing.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct question.",
                "options": [
                    "She is working?",
                    "Does she working?",
                    "Is she working?",
                    "Do she is working?",
                ],
                "answer": "Is she working?",
                "explanation": "В вопросе is переносится перед подлежащим.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct question.",
                "options": [
                    "Do they waiting?",
                    "Are they waiting?",
                    "They are waiting?",
                    "Does they wait now?",
                ],
                "answer": "Are they waiting?",
                "explanation": "They → are: Are they waiting?",
            },

            {
                "order": 19,
                "prompt": "What are you ___?",
                "options": ["do", "does", "doing", "done"],
                "answer": "doing",
                "explanation": "Форма: What are you doing?",
            },

            {
                "order": 20,
                "prompt": "Where is she ___?",
                "options": ["go", "goes", "going", "went"],
                "answer": "going",
                "explanation": "Present Continuous требует verb-ing.",
            },

            {
                "order": 21,
                "prompt": "Who is she waiting ___?",
                "options": ["for", "at", "on", "in"],
                "answer": "for",
                "explanation": "Устойчивая конструкция: wait for someone.",
            },

            {
                "order": 22,
                "prompt": "Which question asks about an action happening now?",
                "options": [
                    "Do you work here?",
                    "Are you working now?",
                    "Do you work every day?",
                    "Does she work here?",
                ],
                "answer": "Are you working now?",
                "explanation": "Now указывает на действие в текущий момент.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I'm not understanding.",
                    "I don't understand.",
                    "I am not understand.",
                    "I doesn't understand.",
                ],
                "answer": "I don't understand.",
                "explanation": "Understand — глагол состояния.",
            },

            {
                "order": 24,
                "prompt": "They are waiting. Choose the correct special question.",
                "options": [
                    "Why do they waiting?",
                    "Why are they waiting?",
                    "Why they are waiting?",
                    "Why does they wait?",
                ],
                "answer": "Why are they waiting?",
                "explanation": "Question word + are + subject + verb-ing.",
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
                "✅ A1 Lesson 22 seeded: "
                "Present Continuous — отрицания и вопросы"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
