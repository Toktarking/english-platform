from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 28: Past Continuous."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=28,

                defaults={
                    "title":
                        "Past Continuous",

                    "slug":
                        "past-continuous",

                    "theory_text":
                        "Past Continuous.",

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
        )


        sections = [

            {
                "order": 1,

                "title":
                    "Что такое Past Continuous?",

                "body":
                    """Past Continuous показывает действие, которое было в процессе в прошлом.

Примеры:

I was working at six yesterday.

She was sleeping at midnight.

They were playing football at that moment.

Главная идея:

мы смотрим не просто на факт действия,
а на процесс в определённый момент прошлого.""",
            },


            {
                "order": 2,

                "title":
                    "Главная формула",

                "body":
                    """Past Continuous строится так:

subject
+ WAS / WERE
+ verb-ing

Примеры:

I was working.

She was reading.

They were playing.

Без WAS / WERE время не строится.

Не:

I working.

They playing.

А:

I was working.

They were playing.""",
            },


            {
                "order": 3,

                "title":
                    "WAS или WERE?",

                "body":
                    """Используем:

I → WAS

he → WAS

she → WAS

it → WAS

you → WERE

we → WERE

they → WERE

Примеры:

I was sleeping.

He was driving.

She was cooking.

You were waiting.

We were studying.

They were playing.""",
            },


            {
                "order": 4,

                "title":
                    "Как образуется -ING?",

                "body":
                    """Обычный случай:

work → working

read → reading

play → playing

Немая E исчезает:

write → writing

make → making

come → coming

Некоторые короткие глаголы удваивают согласную:

sit → sitting

run → running

swim → swimming

IE меняется на Y:

lie → lying

die → dying.""",
            },


            {
                "order": 5,

                "title":
                    "Процесс в конкретный момент прошлого",

                "body":
                    """Past Continuous часто отвечает на вопрос:

Что происходило в тот момент?

I was working at five yesterday.

She was sleeping at midnight.

They were having dinner at seven.

Частые выражения:

at five yesterday

at midnight

at that moment

this time yesterday

from six to eight

Сравни:

I had dinner at seven.
→ факт

I was having dinner at seven.
→ процесс в семь часов.""",
            },


            {
                "order": 6,

                "title":
                    "Длинное действие + короткое событие",

                "body":
                    """Часто одно действие уже происходило, когда случилось другое.

Длительный процесс:

Past Continuous

Короткое событие:

Past Simple

Пример:

I was sleeping when you called.

was sleeping
→ процесс

called
→ короткое событие

Ещё:

She was cooking when the phone rang.

We were driving home when the car stopped.""",
            },


            {
                "order": 7,

                "title":
                    "WHEN или WHILE?",

                "body":
                    """WHEN часто вводит короткое событие:

I was reading when she came.

He was sleeping when I called.

WHILE часто вводит длительный процесс:

She called while I was working.

Если два действия происходили одновременно:

While I was reading,
she was cooking.

They were playing
while we were studying.

Коротко:

WHEN → часто Past Simple

WHILE → часто Past Continuous.""",
            },


            {
                "order": 8,

                "title":
                    "Past Continuous как фон",

                "body":
                    """Past Continuous может описывать фон истории.

The sun was shining.

The birds were singing.

People were walking in the park.

Children were playing.

Затем происходит главное событие:

Suddenly, a car stopped.

Здесь:

Past Continuous
→ фон

Past Simple
→ главное завершённое событие.""",
            },


            {
                "order": 9,

                "title":
                    "Отрицания и вопросы",

                "body":
                    """Отрицание:

subject
+ wasn't / weren't
+ verb-ing

I wasn't sleeping.

They weren't waiting.

Вопрос:

Was / Were
+ subject
+ verb-ing?

Was she working?

Were they playing?

Краткие ответы:

Yes, she was.

No, she wasn't.

Yes, they were.

No, they weren't.

Специальный вопрос:

What were you doing?

Where was she going?""",
            },


            {
                "order": 10,

                "title":
                    "Stative verbs и HAVE",

                "body":
                    """Некоторые глаголы состояния обычно не используются в Continuous.

know

understand

like

want

need

believe

Поэтому:

I knew the answer.

Не:

I was knowing the answer.

HAVE зависит от значения.

Действие:

I was having breakfast.

She was having a shower.

Владение:

I had a car.

Не:

I was having a car.

Главное:

процесс → Past Continuous

состояние → обычно Past Simple.""",
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
                    "At nine last night, I ___ a book.",

                "options": [
                    "read",
                    "was reading",
                    "am reading",
                    "did reading",
                ],

                "answer":
                    "was reading",

                "explanation":
                    "Действие было в процессе в конкретный момент прошлого.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "This time yesterday, they ___ football.",

                "options": [
                    "played every day",
                    "were playing",
                    "are playing",
                    "did playing",
                ],

                "answer":
                    "were playing",

                "explanation":
                    "THIS TIME YESTERDAY → процесс в прошлом.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She working at six.",
                    "She was working at six.",
                    "She did working at six.",
                    "She was work at six.",
                ],

                "answer":
                    "She was working at six.",

                "explanation":
                    "Past Continuous = WAS + verb-ing.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери правильное предложение.",

                "options": [
                    "They",
                    "were",
                    "waiting",
                    "for",
                    "the",
                    "bus",
                ],

                "answer":
                    "They were waiting for the bus",

                "explanation":
                    "Правильная схема: THEY + WERE + WAITING.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "My brother ___ sleeping at midnight.",

                "options": [],

                "answer":
                    "was",

                "explanation":
                    "My brother = HE → WAS.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "My parents ___ watching TV.",

                "options": [
                    "was",
                    "were",
                    "did",
                    "are",
                ],

                "answer":
                    "were",

                "explanation":
                    "My parents = THEY → WERE.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She was ___ an email.",

                "options": [
                    "writeing",
                    "writing",
                    "writting",
                    "wrote",
                ],

                "answer":
                    "writing",

                "explanation":
                    "WRITE → WRITING.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "They were ___ in the park.",

                "options": [
                    "runing",
                    "running",
                    "ran",
                    "run",
                ],

                "answer":
                    "running",

                "explanation":
                    "RUN → RUNNING.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "At 8 p.m. yesterday, we ___ dinner.",

                "options": [
                    "had as a completed fact",
                    "were having",
                    "have",
                    "are having",
                ],

                "answer":
                    "were having",

                "explanation":
                    "Нас интересует процесс именно в 8 вечера.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Which sentence focuses on the process at seven?",

                "options": [
                    "I had dinner at seven.",
                    "I was having dinner at seven.",
                    "I have dinner at seven.",
                    "I am having dinner at seven.",
                ],

                "answer":
                    "I was having dinner at seven.",

                "explanation":
                    "Past Continuous показывает процесс в конкретный момент.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "I ___ when you called.",

                "options": [
                    "was sleeping",
                    "slept every night",
                    "am sleeping",
                    "did sleeping",
                ],

                "answer":
                    "was sleeping",

                "explanation":
                    "SLEEPING — длительный процесс; CALLED — короткое событие.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "She was cooking when the phone ___.",

                "options": [
                    "was ringing",
                    "rang",
                    "rings",
                    "is ringing",
                ],

                "answer":
                    "rang",

                "explanation":
                    "Короткое событие → Past Simple: RANG.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "___ I was studying, my brother was watching TV.",

                "options": [
                    "While",
                    "Yesterday",
                    "Ago",
                    "Last",
                ],

                "answer":
                    "While",

                "explanation":
                    "WHILE вводит длительный процесс.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "She called me ___ I was driving.",

                "options": [
                    "while",
                    "ago",
                    "last",
                    "at",
                ],

                "answer":
                    "while",

                "explanation":
                    "WHILE I WAS DRIVING описывает процесс.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "The sun ___ and the birds were singing.",

                "options": [
                    "was shining",
                    "shined suddenly once",
                    "is shining",
                    "did shining",
                ],

                "answer":
                    "was shining",

                "explanation":
                    "Это фон происходящего → Past Continuous.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "People were walking in the park when a car suddenly ___.",

                "options": [
                    "was stopping",
                    "stopped",
                    "stops",
                    "is stopping",
                ],

                "answer":
                    "stopped",

                "explanation":
                    "Главное короткое событие → Past Simple.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "They didn't waiting.",
                    "They weren't waiting.",
                    "They weren't wait.",
                    "They not were waiting.",
                ],

                "answer":
                    "They weren't waiting.",

                "explanation":
                    "Past Continuous negative = WEREN'T + verb-ing.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "___ you sleeping at midnight?",

                "options": [
                    "Did",
                    "Was",
                    "Were",
                    "Are",
                ],

                "answer":
                    "Were",

                "explanation":
                    "YOU → WERE: WERE YOU SLEEPING?",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I was knowing the answer.",
                    "I knew the answer.",
                    "I was know the answer.",
                    "I did knew the answer.",
                ],

                "answer":
                    "I knew the answer.",

                "explanation":
                    "KNOW — stative verb; здесь нужен Past Simple.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "I had a car. / I was having breakfast.",
                    "I was having a car. / I had breakfast at that moment.",
                    "I was have a car. / I was had breakfast.",
                    "I had having a car. / I was have breakfast.",
                ],

                "answer":
                    "I had a car. / I was having breakfast.",

                "explanation":
                    "Владение → HAD; действие HAVE BREAKFAST → WAS HAVING.",
            },

        ]


        final_test = [

            {
                "order": 21,

                "prompt":
                    "At 10 p.m. yesterday, she ___ for the exam.",

                "options": [
                    "studied as a completed fact",
                    "was studying",
                    "is studying",
                    "did studying",
                ],

                "answer":
                    "was studying",

                "explanation":
                    "Конкретный момент прошлого + процесс → Past Continuous.",
            },


            {
                "order": 22,

                "prompt":
                    "The children ___ outside when it started to rain.",

                "options": [
                    "were playing",
                    "played every day",
                    "are playing",
                    "did playing",
                ],

                "answer":
                    "were playing",

                "explanation":
                    "PLAYING — процесс; STARTED — короткое событие.",
            },


            {
                "order": 23,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "He was drive home.",
                    "He was driving home.",
                    "He did driving home.",
                    "He were driving home.",
                ],

                "answer":
                    "He was driving home.",

                "explanation":
                    "HE → WAS + DRIVING.",
            },


            {
                "order": 24,

                "prompt":
                    "We were ___ when you arrived.",

                "options": [
                    "writeing",
                    "writing",
                    "wrote",
                    "write",
                ],

                "answer":
                    "writing",

                "explanation":
                    "WRITE → WRITING.",
            },


            {
                "order": 25,

                "prompt":
                    "I was walking home when I ___ the accident.",

                "options": [
                    "was seeing",
                    "saw",
                    "see",
                    "am seeing",
                ],

                "answer":
                    "saw",

                "explanation":
                    "SEE — короткое завершённое событие → SAW.",
            },


            {
                "order": 26,

                "prompt":
                    "___ she was cooking, he was setting the table.",

                "options": [
                    "While",
                    "Ago",
                    "Last",
                    "Yesterday",
                ],

                "answer":
                    "While",

                "explanation":
                    "Два параллельных процесса удобно связывать через WHILE.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Did they waiting?",
                    "Were they waiting?",
                    "Was they waiting?",
                    "Did they were waiting?",
                ],

                "answer":
                    "Were they waiting?",

                "explanation":
                    "Past Continuous question = WERE + THEY + WAITING.",
            },


            {
                "order": 28,

                "prompt":
                    "What ___ you doing at eight yesterday?",

                "options": [
                    "did",
                    "was",
                    "were",
                    "are",
                ],

                "answer":
                    "were",

                "explanation":
                    "YOU → WERE: WHAT WERE YOU DOING?",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence about possession.",

                "options": [
                    "She was having a new car.",
                    "She had a new car.",
                    "She was have a new car.",
                    "She did having a new car.",
                ],

                "answer":
                    "She had a new car.",

                "explanation":
                    "HAVE в значении владения обычно используется в Past Simple.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sequence.",

                "options": [
                    "I was driving when the phone rang. / While I was driving, she was sleeping.",
                    "I drove when the phone was rang. / While I drove, she was sleeping now.",
                    "I was drive when the phone rang. / While I was driving, she slept every moment.",
                    "I did driving when the phone rang. / While I were driving, she was sleep.",
                ],

                "answer":
                    "I was driving when the phone rang. / While I was driving, she was sleeping.",

                "explanation":
                    "WHEN связывает процесс с коротким событием; WHILE может связывать два параллельных процесса.",
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
                "✅ Interactive A1 Lesson 28 seeded"
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
