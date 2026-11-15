from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 22: Present Continuous negatives and questions."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=22,

                defaults={
                    "title":
                        "Present Continuous: "
                        "отрицания и вопросы",

                    "slug":
                        "present-continuous-negatives-questions",

                    "theory_text":
                        "Present Continuous negatives and questions.",

                    "estimated_minutes":
                        18,

                    "pass_score":
                        70,

                    "xp_reward":
                        100,

                    "is_published":
                        True,
                },
            )
        )


        sections = [

            {
                "order": 1,

                "title":
                    "Как сделать отрицание?",

                "body":
                    """Чтобы сделать отрицание, после AM / IS / ARE ставим NOT.

Формула:

subject
+ am/is/are
+ not
+ verb-ing

Примеры:

I am not working.

She is not reading.

They are not playing.

Глагол с -ING не меняется.""",
            },


            {
                "order": 2,

                "title":
                    "I'M NOT, ISN'T, AREN'T",

                "body":
                    """С I:

I am not working.

Сокращённо:

I'm not working.

С HE / SHE / IT:

He isn't sleeping.

She's not reading.

С YOU / WE / THEY:

They aren't waiting.

We're not studying.

Оба варианта нормальны:

she isn't

she's not

they aren't

they're not.""",
            },


            {
                "order": 3,

                "title":
                    "Как построить общий вопрос?",

                "body":
                    """В вопросе AM / IS / ARE ставится перед подлежащим.

She is working.

→ Is she working?

They are waiting.

→ Are they waiting?

Формула:

Am / Is / Are
+ subject
+ verb-ing?

Примеры:

Am I speaking too quickly?

Is he sleeping?

Are they studying?""",
            },


            {
                "order": 4,

                "title":
                    "Краткие ответы",

                "body":
                    """Is she working?

Yes, she is.

No, she isn't.

Are they waiting?

Yes, they are.

No, they aren't.

Are you working?

Yes, I am.

No, I'm not.

Важно:

Present Continuous не использует DO / DOES.

Не:

Yes, she does.

А:

Yes, she is.""",
            },


            {
                "order": 5,

                "title":
                    "Специальные вопросы",

                "body":
                    """Формула:

question word
+ am/is/are
+ subject
+ verb-ing?

Примеры:

What are you doing?

Where is she going?

Why are they laughing?

When are we leaving?

Who is he talking to?

После вопросительного слова идёт AM / IS / ARE.""",
            },


            {
                "order": 6,

                "title":
                    "WHAT DO YOU DO? или WHAT ARE YOU DOING?",

                "body":
                    """Эти вопросы означают разное.

What do you do?

Обычно:

Чем вы занимаетесь?
Кем работаете?

Пример ответа:

I am a teacher.

What are you doing?

Что вы делаете прямо сейчас?

Пример ответа:

I am reading.

Сравни:

Present Simple → обычная деятельность

Present Continuous → действие сейчас.""",
            },


            {
                "order": 7,

                "title":
                    "WHERE, WHY и вопросы с предлогами",

                "body":
                    """WHERE:

Where are you going?

Where is she working today?

WHY:

Why are you crying?

Why are they leaving?

В разговорном английском предлог часто остаётся в конце:

Who are you talking to?

Who is she waiting for?

What are you looking at?

What are they thinking about?""",
            },


            {
                "order": 8,

                "title":
                    "WHO и WHAT как подлежащее",

                "body":
                    """WHO может само выполнять действие.

Who is calling?

Who is knocking?

Who is sitting there?

WHAT тоже может быть подлежащим:

What is happening?

What is making that noise?

Здесь дополнительное подлежащее не нужно.

Сравни:

Who is calling you?

WHO выполняет действие.

Who are you calling?

YOU выполняет действие.""",
            },


            {
                "order": 9,

                "title":
                    "Present Simple или Continuous?",

                "body":
                    """Present Simple:

Do you work here?

Does she read every day?

Это привычка или постоянная ситуация.

Present Continuous:

Are you working now?

Is she reading now?

Это действие прямо сейчас или временная ситуация.

Сравни:

Do they play football on Sundays?

Are they playing football now?""",
            },


            {
                "order": 10,

                "title":
                    "HAVE и stative verbs",

                "body":
                    """Некоторые глаголы состояния обычно не используются в Continuous:

know

understand

like

want

need

believe

Поэтому:

Do you understand?

She knows the answer.

Не:

Are you understanding?

Is she knowing?

Но HAVE может быть действием:

Are you having breakfast?

Is she having a shower?

Если HAVE означает владение:

Do you have a car?

Не:

Are you having a car?""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects
                .update_or_create(
                    lesson=lesson,
                    order=data["order"],

                    defaults={
                        "title":
                            data["title"],

                        "body":
                            data["body"],
                    },
                )
            )

            section_objects[
                data["order"]
            ] = section


        training = [

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ not listening.",

                "options": [
                    "is",
                    "am",
                    "are",
                    "do",
                ],

                "answer":
                    "am",

                "explanation":
                    "С I используется AM.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "The children ___ not playing outside.",

                "options": [
                    "is",
                    "am",
                    "are",
                    "do",
                ],

                "answer":
                    "are",

                "explanation":
                    "Children = THEY → ARE NOT.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "She doesn't working.",
                    "She isn't working.",
                    "She not working.",
                    "She isn't work.",
                ],

                "answer":
                    "She isn't working.",

                "explanation":
                    "Present Continuous negative = ISN'T + verb-ing.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "fill",

                "prompt":
                    "They ___ waiting for us. (are not)",

                "options": [],

                "answer":
                    "aren't",

                "explanation":
                    "ARE NOT сокращается до AREN'T.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "___ your sister cooking?",

                "options": [
                    "Do",
                    "Does",
                    "Is",
                    "Are",
                ],

                "answer":
                    "Is",

                "explanation":
                    "Your sister = SHE → IS.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "___ your parents travelling?",

                "options": [
                    "Is",
                    "Are",
                    "Do",
                    "Does",
                ],

                "answer":
                    "Are",

                "explanation":
                    "Parents = THEY → ARE.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Is the baby crying?",

                "options": [
                    "Yes, it is.",
                    "Yes, it does.",
                    "Yes, it cries.",
                    "Yes, it can.",
                ],

                "answer":
                    "Yes, it is.",

                "explanation":
                    "Вопрос с IS требует ответа с IS.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Are the students writing?",

                "options": [
                    "No, they don't.",
                    "No, they aren't.",
                    "No, they doesn't.",
                    "No, they not.",
                ],

                "answer":
                    "No, they aren't.",

                "explanation":
                    "ARE THEY...? → NO, THEY AREN'T.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "What ___ he doing?",

                "options": [
                    "do",
                    "does",
                    "is",
                    "are",
                ],

                "answer":
                    "is",

                "explanation":
                    "HE → IS: WHAT IS HE DOING?",
            },


            {
                "order": 10,
                "section": 5,
                "type": "build",

                "prompt":
                    "Собери правильный вопрос.",

                "options": [
                    "Why",
                    "are",
                    "they",
                    "laughing",
                ],

                "answer":
                    "Why are they laughing",

                "explanation":
                    "Question word + ARE + THEY + verb-ing.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "What are you doing?",

                "options": [
                    "I am a teacher.",
                    "I am reading.",
                    "I work at a university.",
                    "I usually read at night.",
                ],

                "answer":
                    "I am reading.",

                "explanation":
                    "Вопрос спрашивает о действии прямо сейчас.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "What do you do?",

                "options": [
                    "I am cooking now.",
                    "I am a teacher.",
                    "I am talking on the phone.",
                    "I am waiting now.",
                ],

                "answer":
                    "I am a teacher.",

                "explanation":
                    "WHAT DO YOU DO? обычно спрашивает о профессии или обычной деятельности.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Where ___ the children playing?",

                "options": [
                    "is",
                    "are",
                    "do",
                    "does",
                ],

                "answer":
                    "are",

                "explanation":
                    "Children = THEY → WHERE ARE...?",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Who are you talking ___?",

                "options": [
                    "to",
                    "at",
                    "on",
                    "in",
                ],

                "answer":
                    "to",

                "explanation":
                    "Правильная конструкция: TALK TO SOMEONE.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Who ___ knocking at the door?",

                "options": [
                    "is",
                    "are",
                    "do",
                    "does",
                ],

                "answer":
                    "is",

                "explanation":
                    "WHO само выполняет действие → WHO IS KNOCKING?",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "What is happening?",
                    "What does happening?",
                    "What are happen?",
                    "What happening is?",
                ],

                "answer":
                    "What is happening?",

                "explanation":
                    "WHAT здесь является подлежащим.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Which question asks about an action happening now?",

                "options": [
                    "Do you work here?",
                    "Are you working now?",
                    "Do you work every day?",
                    "Does she work here?",
                ],

                "answer":
                    "Are you working now?",

                "explanation":
                    "NOW указывает на Present Continuous.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "Does she read every day? / Is she reading now?",
                    "Is she read every day? / Does she reading now?",
                    "Does she reading every day? / Is she reads now?",
                    "Is she reading every day always? / Does she read now at the moment?",
                ],

                "answer":
                    "Does she read every day? / Is she reading now?",

                "explanation":
                    "EVERY DAY → Present Simple; NOW → Present Continuous.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I'm not understanding.",
                    "I don't understand.",
                    "I am not understand.",
                    "I doesn't understand.",
                ],

                "answer":
                    "I don't understand.",

                "explanation":
                    "UNDERSTAND — stative verb.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "___ you having breakfast now?",

                "options": [
                    "Do",
                    "Does",
                    "Are",
                    "Is",
                ],

                "answer":
                    "Are",

                "explanation":
                    "HAVE здесь означает действие → ARE YOU HAVING...?",
            },

        ]


        final_test = [

            {
                "order": 21,

                "prompt":
                    "My brother ___ not working today.",

                "options": [
                    "am",
                    "is",
                    "are",
                    "does",
                ],

                "answer":
                    "is",

                "explanation":
                    "My brother = HE → IS NOT.",
            },


            {
                "order": 22,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "They don't waiting.",
                    "They aren't waiting.",
                    "They aren't wait.",
                    "They not are waiting.",
                ],

                "answer":
                    "They aren't waiting.",

                "explanation":
                    "ARE NOT + WAITING.",
            },


            {
                "order": 23,

                "prompt":
                    "___ she studying at the moment?",

                "options": [
                    "Does",
                    "Do",
                    "Is",
                    "Are",
                ],

                "answer":
                    "Is",

                "explanation":
                    "SHE → IS; вопрос начинается с IS.",
            },


            {
                "order": 24,

                "prompt":
                    "Are they coming with us?",

                "options": [
                    "Yes, they are.",
                    "Yes, they do.",
                    "Yes, they come.",
                    "Yes, they is.",
                ],

                "answer":
                    "Yes, they are.",

                "explanation":
                    "Вопрос с ARE → ответ с ARE.",
            },


            {
                "order": 25,

                "prompt":
                    "Where ___ your sister going?",

                "options": [
                    "does",
                    "do",
                    "is",
                    "are",
                ],

                "answer":
                    "is",

                "explanation":
                    "Your sister = SHE → WHERE IS...?",
            },


            {
                "order": 26,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "What are you doing?",
                    "What do you doing?",
                    "What are you do?",
                    "What does you doing?",
                ],

                "answer":
                    "What are you doing?",

                "explanation":
                    "Present Continuous question = ARE + YOU + DOING.",
            },


            {
                "order": 27,

                "prompt":
                    "Who is she waiting ___?",

                "options": [
                    "for",
                    "to",
                    "at",
                    "on",
                ],

                "answer":
                    "for",

                "explanation":
                    "Правильная конструкция: WAIT FOR SOMEONE.",
            },


            {
                "order": 28,

                "prompt":
                    "Which question asks about a regular job?",

                "options": [
                    "What are you doing?",
                    "What do you do?",
                    "Why are you working now?",
                    "Where are you going?",
                ],

                "answer":
                    "What do you do?",

                "explanation":
                    "WHAT DO YOU DO? обычно спрашивает о профессии или обычной деятельности.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "Are you understanding me?",
                    "Do you understand me?",
                    "Are you understand me?",
                    "Do you understanding me?",
                ],

                "answer":
                    "Do you understand me?",

                "explanation":
                    "UNDERSTAND обычно используется в Present Simple.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct set.",

                "options": [
                    "She isn't working. / Is she working? / Why is she working?",
                    "She doesn't working. / Does she working? / Why does she working?",
                    "She isn't work. / Is she work? / Why she is working?",
                    "She not working. / She is working? / Why does she work now at the moment?",
                ],

                "answer":
                    "She isn't working. / Is she working? / Why is she working?",

                "explanation":
                    "Отрицание, общий вопрос и специальный вопрос правильно строятся через IS + verb-ing.",
            },

        ]


        valid_orders = []


        for data in (
            training
            +
            final_test
        ):

            valid_orders.append(
                data["order"]
            )


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
                "✅ Interactive A1 Lesson 22 seeded"
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
