from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 27: Past Simple complete review."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=27,

                defaults={
                    "title":
                        "Past Simple: полное обобщение",

                    "slug":
                        "past-simple-complete-review",

                    "theory_text":
                        "Complete review of Past Simple.",

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
                    "Три системы Past Simple",

                "body":
                    """В Past Simple есть три основные системы.

1. TO BE:

was / were

I was tired.

They were at home.

2. Правильные глаголы:

verb + ed

I worked yesterday.

3. Неправильные глаголы:

V2

I went home.

Главное сначала понять:

это состояние
или действие?""",
            },


            {
                "order": 2,

                "title":
                    "Когда используется Past Simple?",

                "body":
                    """Past Simple используется для завершённого прошлого.

I finished the report yesterday.

She called me last night.

Также:

конкретный момент:

He arrived at six.

последовательность:

I woke up, had breakfast and went to work.

привычка в прошлом:

We played outside every day.

состояние в прошлом:

I was tired.""",
            },


            {
                "order": 3,

                "title":
                    "Маркеры прошлого",

                "body":
                    """Частые маркеры:

yesterday

last night

last week

last year

two days ago

five years ago

in 2020

when I was a child

then

after that

Примеры:

I worked yesterday.

She went home last night.

They moved here three years ago.""",
            },


            {
                "order": 4,

                "title":
                    "WAS / WERE",

                "body":
                    """WAS / WERE используются для состояния, места, профессии и возраста.

I / he / she / it → WAS

you / we / they → WERE

Примеры:

She was tired.

He was at work.

They were students.

Отрицание:

wasn't / weren't

Вопрос:

Was she tired?

Were they ready?

DID здесь не нужен.""",
            },


            {
                "order": 5,

                "title":
                    "Правильные и неправильные глаголы",

                "body":
                    """Правильные глаголы:

work → worked

play → played

study → studied

stop → stopped

Неправильные глаголы:

go → went

see → saw

have → had

do → did

take → took

buy → bought

write → wrote

eat → ate

В утверждении используется Past Simple форма.""",
            },


            {
                "order": 6,

                "title":
                    "Отрицание: DIDN'T + V1",

                "body":
                    """С обычными глаголами:

subject
+ didn't
+ base verb

I didn't work.

She didn't study.

They didn't go.

He didn't see her.

После DIDN'T всегда первая форма.

worked → didn't work

went → didn't go

saw → didn't see

Но с TO BE:

I wasn't tired.

They weren't ready.""",
            },


            {
                "order": 7,

                "title":
                    "Вопрос: DID + V1",

                "body":
                    """С обычным глаголом:

Did + subject + base verb?

Did you work?

Did she study?

Did they go?

После DID снова первая форма.

Не:

Did she worked?

Не:

Did they went?

С TO BE:

Was she tired?

Were they at home?

DID с WAS/WERE не используется.""",
            },


            {
                "order": 8,

                "title":
                    "Краткие и специальные вопросы",

                "body":
                    """Обычный глагол:

Did you work?

Yes, I did.

No, I didn't.

TO BE:

Was she busy?

Yes, she was.

No, she wasn't.

Специальный вопрос:

Where did you work?

Why did they leave?

What did he buy?

После DID используется V1.""",
            },


            {
                "order": 9,

                "title":
                    "WHO и особый случай с DID",

                "body":
                    """Если WHO спрашивает об объекте:

Who did you call?

Здесь YOU выполняет действие.

Но если WHO само выполняет действие:

Who called you?

Who came yesterday?

Who wrote this message?

DID тогда не нужен.

Сравни:

Who called you?
→ кто позвонил тебе

Who did you call?
→ кому позвонил ты.""",
            },


            {
                "order": 10,

                "title":
                    "Состояние или действие?",

                "body":
                    """Самый важный алгоритм:

Состояние / место / профессия / возраст?

→ WAS / WERE

She was tired.

He was at work.

Действие?

→ Past Simple глагола

She worked.

He went home.

Отрицание действия?

→ DIDN'T + V1

She didn't work.

Вопрос о действии?

→ DID + subject + V1

Did she work?

Но:

Was she tired?""",
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
                    "We ___ busy yesterday.",

                "options": [
                    "was",
                    "were",
                    "did",
                    "worked",
                ],

                "answer":
                    "were",

                "explanation":
                    "BUSY — состояние; WE → WERE.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "My sister ___ me last night.",

                "options": [
                    "called",
                    "call",
                    "did called",
                    "was call",
                ],

                "answer":
                    "called",

                "explanation":
                    "CALL — действие; правильный Past Simple → CALLED.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "They ___ to the cinema yesterday.",

                "options": [
                    "went",
                    "goed",
                    "did went",
                    "were go",
                ],

                "answer":
                    "went",

                "explanation":
                    "GO → WENT.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "I ___ breakfast and then went to work.",

                "options": [
                    "had",
                    "haved",
                    "have",
                    "did had",
                ],

                "answer":
                    "had",

                "explanation":
                    "HAVE → HAD.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "Choose the correct time expression.",

                "options": [
                    "ago two days",
                    "two days ago",
                    "two ago days",
                    "last two days ago",
                ],

                "answer":
                    "two days ago",

                "explanation":
                    "AGO ставится после периода времени.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "She moved here three years ___.",

                "options": [
                    "ago",
                    "last",
                    "yesterday",
                    "before ago",
                ],

                "answer":
                    "ago",

                "explanation":
                    "THREE YEARS AGO — правильное выражение.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "I ___ not tired yesterday.",

                "options": [
                    "did",
                    "wasn't",
                    "didn't be",
                    "weren't",
                ],

                "answer":
                    "wasn't",

                "explanation":
                    "TIRED — состояние; I → WASN'T.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "___ you at work yesterday?",

                "options": [
                    "Did",
                    "Was",
                    "Were",
                    "Are",
                ],

                "answer":
                    "Were",

                "explanation":
                    "AT WORK — место; YOU → WERE.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "She ___ English yesterday evening.",

                "options": [
                    "studied",
                    "studyed",
                    "did studied",
                    "was study",
                ],

                "answer":
                    "studied",

                "explanation":
                    "STUDY → STUDIED.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "He ___ a new phone last week.",

                "options": [
                    "buyed",
                    "bought",
                    "buy",
                    "did bought",
                ],

                "answer":
                    "bought",

                "explanation":
                    "BUY → BOUGHT.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "She didn't ___ English yesterday.",

                "options": [
                    "studied",
                    "study",
                    "studies",
                    "studying",
                ],

                "answer":
                    "study",

                "explanation":
                    "После DIDN'T используется V1.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "They didn't ___ the answer.",

                "options": [
                    "knew",
                    "know",
                    "known",
                    "knowing",
                ],

                "answer":
                    "know",

                "explanation":
                    "KNEW возвращается к KNOW после DIDN'T.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "___ she call you last night?",

                "options": [
                    "Was",
                    "Did",
                    "Were",
                    "Does",
                ],

                "answer":
                    "Did",

                "explanation":
                    "CALL — обычное действие → DID.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Did they ___ home early?",

                "options": [
                    "went",
                    "go",
                    "gone",
                    "going",
                ],

                "answer":
                    "go",

                "explanation":
                    "После DID используется V1 → GO.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Were they ready?",

                "options": [
                    "Yes, they did.",
                    "Yes, they were.",
                    "Yes, they was.",
                    "Yes, they are.",
                ],

                "answer":
                    "Yes, they were.",

                "explanation":
                    "Вопрос с WERE → ответ с WERE.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "build",

                "prompt":
                    "Собери правильный вопрос.",

                "options": [
                    "Where",
                    "did",
                    "she",
                    "work",
                ],

                "answer":
                    "Where did she work",

                "explanation":
                    "WHERE + DID + SHE + V1.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Who ___ this message?",

                "options": [
                    "did write",
                    "wrote",
                    "write",
                    "written",
                ],

                "answer":
                    "wrote",

                "explanation":
                    "WHO само является подлежащим → DID не нужен.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Who did you ___ yesterday?",

                "options": [
                    "called",
                    "call",
                    "calls",
                    "calling",
                ],

                "answer":
                    "call",

                "explanation":
                    "Здесь YOU выполняет действие, поэтому DID + CALL.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the sentence about a state.",

                "options": [
                    "She worked yesterday.",
                    "She was tired yesterday.",
                    "She studied yesterday.",
                    "She went home yesterday.",
                ],

                "answer":
                    "She was tired yesterday.",

                "explanation":
                    "TIRED — состояние → WAS.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the sentence about an action.",

                "options": [
                    "He was at work yesterday.",
                    "He was tired yesterday.",
                    "He worked yesterday.",
                    "He was a doctor.",
                ],

                "answer":
                    "He worked yesterday.",

                "explanation":
                    "WORKED описывает действие.",
            },

        ]


        final_test = [

            {
                "order": 21,

                "prompt":
                    "My parents ___ at home last night.",

                "options": [
                    "was",
                    "were",
                    "did",
                    "worked",
                ],

                "answer":
                    "were",

                "explanation":
                    "My parents = THEY → WERE.",
            },


            {
                "order": 22,

                "prompt":
                    "She ___ the office at six yesterday.",

                "options": [
                    "left",
                    "leaved",
                    "leave",
                    "did left",
                ],

                "answer":
                    "left",

                "explanation":
                    "LEAVE → LEFT.",
            },


            {
                "order": 23,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "He didn't went home.",
                    "He didn't go home.",
                    "He wasn't go home.",
                    "He didn't gone home.",
                ],

                "answer":
                    "He didn't go home.",

                "explanation":
                    "После DIDN'T используется V1 → GO.",
            },


            {
                "order": 24,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Did she worked yesterday?",
                    "Did she work yesterday?",
                    "Was she work yesterday?",
                    "Did she working yesterday?",
                ],

                "answer":
                    "Did she work yesterday?",

                "explanation":
                    "DID + subject + V1.",
            },


            {
                "order": 25,

                "prompt":
                    "Was he tired after work?",

                "options": [
                    "Yes, he did.",
                    "Yes, he was.",
                    "Yes, he were.",
                    "Yes, he does.",
                ],

                "answer":
                    "Yes, he was.",

                "explanation":
                    "Вопрос с WAS → ответ с WAS.",
            },


            {
                "order": 26,

                "prompt":
                    "What did she ___ at the shop?",

                "options": [
                    "bought",
                    "buy",
                    "buys",
                    "buying",
                ],

                "answer":
                    "buy",

                "explanation":
                    "После DID используется V1 → BUY.",
            },


            {
                "order": 27,

                "prompt":
                    "Who ___ you yesterday?",

                "options": [
                    "did call",
                    "called",
                    "did called",
                    "calling",
                ],

                "answer":
                    "called",

                "explanation":
                    "WHO само выполняет действие → CALLED без DID.",
            },


            {
                "order": 28,

                "prompt":
                    "I ___ breakfast, then I ___ to work.",

                "options": [
                    "had / went",
                    "have / went",
                    "had / go",
                    "did have / did went",
                ],

                "answer":
                    "had / went",

                "explanation":
                    "В последовательности завершённых действий используем HAD и WENT.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "She was at work. / She worked.",
                    "She did at work. / She was worked.",
                    "She were at work. / She did worked.",
                    "She was work. / She worked was.",
                ],

                "answer":
                    "She was at work. / She worked.",

                "explanation":
                    "WAS AT WORK = состояние/место; WORKED = действие.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct set.",

                "options": [
                    "She went. / She didn't go. / Did she go? / She was tired. / Was she tired?",
                    "She went. / She didn't went. / Did she went? / She did tired. / Did she was tired?",
                    "She go. / She didn't went. / Did she go? / She were tired. / Was she tired?",
                    "She was went. / She didn't go. / Was she go? / She tired. / Did she tired?",
                ],

                "answer":
                    "She went. / She didn't go. / Did she go? / She was tired. / Was she tired?",

                "explanation":
                    "Действие использует V2/DID; состояние с TO BE использует WAS без DID.",
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
                "✅ Interactive A1 Lesson 27 seeded"
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
