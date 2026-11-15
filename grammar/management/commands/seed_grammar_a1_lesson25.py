from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 25: Past Simple regular verbs."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=25,

                defaults={
                    "title":
                        "Past Simple с правильными глаголами",

                    "slug":
                        "past-simple-regular-verbs",

                    "theory_text":
                        "Past Simple with regular verbs.",

                    "estimated_minutes":
                        19,

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
                    "Когда нужен Past Simple?",

                "body":
                    """Past Simple используется для завершённых действий в прошлом.

I worked yesterday.

She called me last night.

They visited Almaty last year.

Также он используется для:

последовательности действий;

повторяющихся действий в прошлом.

Примеры:

I opened the door, entered the room and turned on the light.

We played outside every day when we were children.""",
            },


            {
                "order": 2,

                "title":
                    "Правильный глагол + ED",

                "body":
                    """У правильных глаголов Past Simple обычно образуется через -ED.

work → worked

play → played

clean → cleaned

watch → watched

visit → visited

Форма одинакова для всех:

I worked.

She worked.

They worked.

В Past Simple не добавляем отдельное -S для HE / SHE / IT.""",
            },


            {
                "order": 3,

                "title":
                    "Если глагол заканчивается на E",

                "body":
                    """Если глагол уже заканчивается на E, добавляем только -D.

live → lived

love → loved

move → moved

dance → danced

arrive → arrived

Не:

liveed

А:

lived.""",
            },


            {
                "order": 4,

                "title":
                    "Y → IED или Y остаётся?",

                "body":
                    """Если перед Y стоит согласная:

Y → IED

study → studied

carry → carried

try → tried

cry → cried

Если перед Y стоит гласная, Y сохраняется:

play → played

stay → stayed

enjoy → enjoyed

Сравни:

study → studied

play → played.""",
            },


            {
                "order": 5,

                "title":
                    "Удвоение согласной",

                "body":
                    """У некоторых коротких глаголов последняя согласная удваивается.

stop → stopped

plan → planned

shop → shopped

drop → dropped

Но W, X и Y обычно не удваиваются:

snow → snowed

fix → fixed

play → played.

Важно запоминать форму вместе с глаголом.""",
            },


            {
                "order": 6,

                "title":
                    "Как произносится -ED?",

                "body":
                    """Окончание -ED может звучать по-разному.

/t/:

worked

watched

helped

/d/:

played

cleaned

called

/ɪd/:

wanted

needed

started

visited

Написание одно — ED, но произношение зависит от последнего звука глагола.""",
            },


            {
                "order": 7,

                "title":
                    "Отрицание: DIDN'T + base verb",

                "body":
                    """Отрицание строится через DIDN'T.

I didn't work.

She didn't play.

They didn't study.

После DIDN'T глагол возвращается в базовую форму.

She worked.

→ She didn't work.

Не:

She didn't worked.

DIDN'T уже показывает прошедшее время.""",
            },


            {
                "order": 8,

                "title":
                    "Вопросы: DID + subject + verb?",

                "body":
                    """Вопрос:

DID + subject + base verb?

Did you work yesterday?

Did she call you?

Did they study English?

После DID снова используется базовая форма.

Не:

Did she worked?

А:

Did she work?

Краткие ответы:

Yes, I did.

No, I didn't.""",
            },


            {
                "order": 9,

                "title":
                    "WHERE DID...? и WHO",

                "body":
                    """Специальный вопрос:

question word
+ DID
+ subject
+ base verb?

Where did you work?

When did she arrive?

Why did they stop?

Who did you call?

Но если WHO само выполняет действие, DID обычно не нужен:

Who called you?

Who opened the door?

Сравни:

Who called you?
→ кто позвонил

Who did you call?
→ кому позвонил ты.""",
            },


            {
                "order": 10,

                "title":
                    "WAS/WERE или обычный Past Simple?",

                "body":
                    """WAS / WERE используются для состояния, места, профессии и возраста.

She was tired.

He was at work.

They were students.

Обычный Past Simple используется для действия.

She worked yesterday.

He studied English.

Сравни:

He was at work yesterday.
→ был на работе

He worked yesterday.
→ работал

Не:

He was worked yesterday.

И не смешивай вопросы:

Was he tired?

Did he work?""",
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
                    "We ___ the room yesterday.",

                "options": [
                    "clean",
                    "cleaned",
                    "cleaning",
                    "did cleaned",
                ],

                "answer":
                    "cleaned",

                "explanation":
                    "YESTERDAY → завершённое действие в прошлом.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "She ___ me last night.",

                "options": [
                    "call",
                    "called",
                    "calling",
                    "did called",
                ],

                "answer":
                    "called",

                "explanation":
                    "CALL — правильный глагол → CALLED.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "They ___ football yesterday. (play)",

                "options": [],

                "answer":
                    "played",

                "explanation":
                    "PLAY → PLAYED.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Simple sentence.",

                "options": [
                    "He works yesterday.",
                    "He worked yesterday.",
                    "He did worked yesterday.",
                    "He working yesterday.",
                ],

                "answer":
                    "He worked yesterday.",

                "explanation":
                    "Утверждение Past Simple → WORKED.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "They ___ in London for two years.",

                "options": [
                    "lived",
                    "liveed",
                    "living",
                    "did lived",
                ],

                "answer":
                    "lived",

                "explanation":
                    "LIVE заканчивается на E → добавляем только D.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Simple form of MOVE.",

                "options": [
                    "moveed",
                    "moved",
                    "movied",
                    "moving",
                ],

                "answer":
                    "moved",

                "explanation":
                    "MOVE → MOVED.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Simple form of STUDY.",

                "options": [
                    "studyed",
                    "studied",
                    "studyd",
                    "studing",
                ],

                "answer":
                    "studied",

                "explanation":
                    "Согласная + Y → Y меняется на IED.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Simple form of PLAY.",

                "options": [
                    "plaied",
                    "played",
                    "playd",
                    "playyed",
                ],

                "answer":
                    "played",

                "explanation":
                    "Перед Y стоит гласная → Y сохраняется.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Simple form of STOP.",

                "options": [
                    "stoped",
                    "stopped",
                    "stopt",
                    "stopping",
                ],

                "answer":
                    "stopped",

                "explanation":
                    "STOP → STOPPED с удвоением P.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Simple form of PLAN.",

                "options": [
                    "planed",
                    "planned",
                    "planied",
                    "planning",
                ],

                "answer":
                    "planned",

                "explanation":
                    "PLAN → PLANNED.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Which word has -ED pronounced as /ɪd/?",

                "options": [
                    "worked",
                    "played",
                    "wanted",
                    "helped",
                ],

                "answer":
                    "wanted",

                "explanation":
                    "WANTED произносится с отдельным слогом /ɪd/.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Which word has -ED pronounced as /d/?",

                "options": [
                    "watched",
                    "called",
                    "wanted",
                    "helped",
                ],

                "answer":
                    "called",

                "explanation":
                    "CALLED оканчивается на звук /d/.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "She didn't ___ the question.",

                "options": [
                    "answered",
                    "answer",
                    "answers",
                    "answering",
                ],

                "answer":
                    "answer",

                "explanation":
                    "После DIDN'T используется базовая форма.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "She didn't worked yesterday.",
                    "She didn't work yesterday.",
                    "She wasn't work yesterday.",
                    "She doesn't worked yesterday.",
                ],

                "answer":
                    "She didn't work yesterday.",

                "explanation":
                    "DIDN'T уже показывает прошлое → WORK без -ED.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Did they ___ you yesterday?",

                "options": [
                    "helped",
                    "help",
                    "helps",
                    "helping",
                ],

                "answer":
                    "help",

                "explanation":
                    "DID + base verb → HELP.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Did she visit Almaty?",

                "options": [
                    "Yes, she did.",
                    "Yes, she was.",
                    "Yes, she visited did.",
                    "Yes, she does.",
                ],

                "answer":
                    "Yes, she did.",

                "explanation":
                    "Вопрос с DID → краткий ответ с DID.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "build",

                "prompt":
                    "Собери правильный вопрос.",

                "options": [
                    "Where",
                    "did",
                    "you",
                    "work",
                ],

                "answer":
                    "Where did you work",

                "explanation":
                    "Question word + DID + subject + base verb.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Who ___ the door?",

                "options": [
                    "did opened",
                    "opened",
                    "did open it who",
                    "opening",
                ],

                "answer":
                    "opened",

                "explanation":
                    "WHO само является подлежащим → DID не нужен.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the sentence about an action.",

                "options": [
                    "He was at work yesterday.",
                    "He worked yesterday.",
                    "He was tired yesterday.",
                    "He was a student.",
                ],

                "answer":
                    "He worked yesterday.",

                "explanation":
                    "WORKED описывает действие.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "Was she tired? / Did she work?",
                    "Did she tired? / Was she work?",
                    "Was she tired? / Was she worked?",
                    "Did she was tired? / Did she worked?",
                ],

                "answer":
                    "Was she tired? / Did she work?",

                "explanation":
                    "Состояние → WAS; действие → DID + WORK.",
            },

        ]


        final_test = [

            {
                "order": 21,

                "prompt":
                    "They ___ the office last week.",

                "options": [
                    "paint",
                    "painted",
                    "painting",
                    "did painted",
                ],

                "answer":
                    "painted",

                "explanation":
                    "Правильный глагол PAINT → PAINTED.",
            },


            {
                "order": 22,

                "prompt":
                    "She ___ in Almaty in 2022.",

                "options": [
                    "liveed",
                    "lived",
                    "living",
                    "did lived",
                ],

                "answer":
                    "lived",

                "explanation":
                    "LIVE → LIVED.",
            },


            {
                "order": 23,

                "prompt":
                    "Choose the correct form of TRY.",

                "options": [
                    "tryed",
                    "tried",
                    "tryd",
                    "trying",
                ],

                "answer":
                    "tried",

                "explanation":
                    "Согласная + Y → TRIED.",
            },


            {
                "order": 24,

                "prompt":
                    "Choose the correct form of DROP.",

                "options": [
                    "droped",
                    "dropped",
                    "dropied",
                    "dropping",
                ],

                "answer":
                    "dropped",

                "explanation":
                    "DROP → DROPPED.",
            },


            {
                "order": 25,

                "prompt":
                    "Which word has -ED pronounced as /t/?",

                "options": [
                    "played",
                    "visited",
                    "helped",
                    "needed",
                ],

                "answer":
                    "helped",

                "explanation":
                    "HELPED заканчивается произношением /t/.",
            },


            {
                "order": 26,

                "prompt":
                    "We didn't ___ the window.",

                "options": [
                    "opened",
                    "open",
                    "opens",
                    "opening",
                ],

                "answer":
                    "open",

                "explanation":
                    "После DIDN'T используется базовая форма.",
            },


            {
                "order": 27,

                "prompt":
                    "___ she call you yesterday?",

                "options": [
                    "Was",
                    "Did",
                    "Does",
                    "Were",
                ],

                "answer":
                    "Did",

                "explanation":
                    "CALL — обычное действие → DID SHE CALL...?",
            },


            {
                "order": 28,

                "prompt":
                    "Why did they ___ the meeting early?",

                "options": [
                    "stopped",
                    "stop",
                    "stops",
                    "stopping",
                ],

                "answer":
                    "stop",

                "explanation":
                    "После DID используется базовая форма STOP.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "Who called you last night?",
                    "Who did called you last night?",
                    "Who did call you last night did?",
                    "Who was called you last night?",
                ],

                "answer":
                    "Who called you last night?",

                "explanation":
                    "WHO здесь само выполняет действие, поэтому DID не нужен.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct set.",

                "options": [
                    "She worked. / She didn't work. / Did she work?",
                    "She worked. / She didn't worked. / Did she worked?",
                    "She was worked. / She didn't work. / Was she work?",
                    "She work. / She wasn't work. / Did she worked?",
                ],

                "answer":
                    "She worked. / She didn't work. / Did she work?",

                "explanation":
                    "Утверждение → WORKED; после DIDN'T и DID → WORK.",
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
                "✅ Interactive A1 Lesson 25 seeded"
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
