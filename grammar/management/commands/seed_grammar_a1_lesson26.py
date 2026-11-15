from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 26: Past Simple irregular verbs."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=26,

                defaults={
                    "title":
                        "Past Simple с неправильными глаголами",

                    "slug":
                        "past-simple-irregular-verbs",

                    "theory_text":
                        "Past Simple with irregular verbs.",

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
                    "Почему глаголы называются неправильными?",

                "body":
                    """Правильные глаголы обычно получают -ED:

work → worked

play → played

Но неправильные глаголы имеют особую форму Past Simple.

go → went

see → saw

have → had

come → came

take → took

Нельзя просто добавить -ED.

Не:

goed

seed

comed

taked

Форму нужно запоминать.""",
            },


            {
                "order": 2,

                "title":
                    "Вторая форма — только в утверждении",

                "body":
                    """В утвердительном Past Simple используется вторая форма глагола.

I went home.

She saw him.

They had lunch.

He took a taxi.

Форма одинакова для всех лиц:

I went.

He went.

They went.

Не:

He wents.

Главное правило:

утверждение
→ V2.""",
            },


            {
                "order": 3,

                "title":
                    "GO, COME, SEE, LEAVE",

                "body":
                    """Частые глаголы движения:

go → went

come → came

leave → left

run → ran

Примеры:

I went to work.

She came home late.

They left early.

He ran to the bus stop.

SEE:

see → saw

I saw him yesterday.

Важно:

go = идти / ехать туда

come = приходить / приезжать сюда.""",
            },


            {
                "order": 4,

                "title":
                    "HAVE, DO, TAKE, GET, MAKE",

                "body":
                    """Частые формы:

have → had

do → did

take → took

get → got

make → made

Примеры:

I had breakfast.

She did her homework.

He took a taxi.

We got home late.

They made a mistake.

Важно:

DID может быть смысловым глаголом:

I did my homework.

И вспомогательным:

Did you do your homework?

После вспомогательного DID используется DO, не DID.""",
            },


            {
                "order": 5,

                "title":
                    "GIVE, FIND, KNOW, THINK",

                "body":
                    """give → gave

find → found

know → knew

think → thought

Примеры:

She gave me a book.

I found my keys.

He knew the answer.

We thought about the problem.

Эти формы нельзя строить по правилу -ED — их нужно запомнить.""",
            },


            {
                "order": 6,

                "title":
                    "SAY или TELL?",

                "body":
                    """say → said

tell → told

SAY обычно используется без прямого указания человека:

She said hello.

He said that he was tired.

TELL часто требует человека:

She told me the truth.

He told us a story.

Сравни:

She said that she was tired.

She told me that she was tired.

Не:

She said me.

Обычно:

She told me.""",
            },


            {
                "order": 7,

                "title":
                    "Ещё важные неправильные глаголы",

                "body":
                    """buy → bought

bring → brought

write → wrote

speak → spoke

eat → ate

drink → drank

feel → felt

sleep → slept

wake → woke

Примеры:

I bought a phone.

She brought the documents.

He wrote an email.

We spoke to the teacher.

They ate dinner.

I drank coffee.

She felt tired.

He woke up at seven.""",
            },


            {
                "order": 8,

                "title":
                    "READ: написание одинаковое",

                "body":
                    """READ — особый случай.

Настоящее:

read /riːd/

I read every day.

Прошедшее:

read /red/

I read this book yesterday.

Написание одинаковое:

READ → READ

Но произношение меняется.

Поэтому время определяем по контексту:

every day → Present Simple

yesterday → Past Simple.""",
            },


            {
                "order": 9,

                "title":
                    "DIDN'T и DID возвращают первую форму",

                "body":
                    """В отрицании:

DIDN'T + V1

I didn't go.

She didn't see him.

They didn't come.

Не:

didn't went

didn't saw

didn't came

В вопросе:

DID + subject + V1?

Did you go?

Did she see him?

Did they come?

Вторая форма используется только в утверждении.""",
            },


            {
                "order": 10,

                "title":
                    "Специальные вопросы и WHO",

                "body":
                    """Обычный специальный вопрос:

question word
+ DID
+ subject
+ V1?

Where did you go?

What did she buy?

Why did he leave?

Who did you call?

Но если WHO само выполняет действие, DID не нужен:

Who came yesterday?

Who saw the accident?

Who took my phone?

Who wrote this message?

Сравни:

Who called you?
→ кто позвонил тебе

Who did you call?
→ кому позвонил ты.""",
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
                    "We ___ to Astana last week.",

                "options": [
                    "went",
                    "goed",
                    "go",
                    "did went",
                ],

                "answer":
                    "went",

                "explanation":
                    "GO → WENT.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ an interesting film yesterday.",

                "options": [
                    "saw",
                    "seed",
                    "see",
                    "did saw",
                ],

                "answer":
                    "saw",

                "explanation":
                    "SEE → SAW.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "She ___ home late yesterday. (come)",

                "options": [],

                "answer":
                    "came",

                "explanation":
                    "В утверждении используется V2: COME → CAME.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Simple sentence.",

                "options": [
                    "He wents home.",
                    "He went home.",
                    "He did went home.",
                    "He goed home.",
                ],

                "answer":
                    "He went home.",

                "explanation":
                    "V2 глагола GO — WENT; форма одинакова для всех лиц.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "They ___ the office early.",

                "options": [
                    "leaved",
                    "left",
                    "leave",
                    "did left",
                ],

                "answer":
                    "left",

                "explanation":
                    "LEAVE → LEFT.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "She ___ to my house at six.",

                "options": [
                    "came",
                    "comed",
                    "come",
                    "did came",
                ],

                "answer":
                    "came",

                "explanation":
                    "COME → CAME.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "He ___ breakfast at seven.",

                "options": [
                    "had",
                    "have",
                    "haved",
                    "has",
                ],

                "answer":
                    "had",

                "explanation":
                    "HAVE → HAD.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She ___ a taxi to the airport.",

                "options": [
                    "taked",
                    "took",
                    "take",
                    "taken",
                ],

                "answer":
                    "took",

                "explanation":
                    "TAKE → TOOK.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "I ___ my keys under the sofa.",

                "options": [
                    "finded",
                    "found",
                    "find",
                    "founded",
                ],

                "answer":
                    "found",

                "explanation":
                    "FIND → FOUND.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "She ___ he was right.",

                "options": [
                    "thinked",
                    "thought",
                    "think",
                    "thinks",
                ],

                "answer":
                    "thought",

                "explanation":
                    "THINK → THOUGHT.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "He ___ me the truth.",

                "options": [
                    "said",
                    "told",
                    "telled",
                    "tell",
                ],

                "answer":
                    "told",

                "explanation":
                    "TELL + person → HE TOLD ME.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "She ___ that she was tired.",

                "options": [
                    "said",
                    "told",
                    "telled",
                    "say",
                ],

                "answer":
                    "said",

                "explanation":
                    "SAY → SAID; здесь после глагола нет прямого объекта-человека.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I ___ a new phone yesterday.",

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
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "We ___ dinner at eight.",

                "options": [
                    "eated",
                    "ate",
                    "eat",
                    "eaten",
                ],

                "answer":
                    "ate",

                "explanation":
                    "EAT → ATE.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Yesterday I ___ this article.",

                "options": [
                    "read",
                    "readed",
                    "rode",
                    "did readed",
                ],

                "answer":
                    "read",

                "explanation":
                    "READ в Past Simple пишется так же: READ, но произносится /red/.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "He ___ up at seven yesterday.",

                "options": [
                    "waked",
                    "woke",
                    "wake",
                    "woken",
                ],

                "answer":
                    "woke",

                "explanation":
                    "WAKE → WOKE; WAKE UP → WOKE UP.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "She didn't ___ home early.",

                "options": [
                    "went",
                    "go",
                    "gone",
                    "going",
                ],

                "answer":
                    "go",

                "explanation":
                    "После DIDN'T используется V1 → GO.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Did you ___ him yesterday?",

                "options": [
                    "saw",
                    "see",
                    "seen",
                    "seeing",
                ],

                "answer":
                    "see",

                "explanation":
                    "После DID используется V1 → SEE.",
            },


            {
                "order": 19,
                "section": 10,
                "type": "build",

                "prompt":
                    "Собери правильный вопрос.",

                "options": [
                    "Where",
                    "did",
                    "you",
                    "go",
                ],

                "answer":
                    "Where did you go",

                "explanation":
                    "WHERE + DID + YOU + V1.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Who ___ this message?",

                "options": [
                    "did wrote",
                    "wrote",
                    "did write who",
                    "written",
                ],

                "answer":
                    "wrote",

                "explanation":
                    "WHO само является подлежащим → DID не нужен.",
            },

        ]


        final_test = [

            {
                "order": 21,

                "prompt":
                    "She ___ home very late last night.",

                "options": [
                    "came",
                    "comed",
                    "come",
                    "did came",
                ],

                "answer":
                    "came",

                "explanation":
                    "COME → CAME.",
            },


            {
                "order": 22,

                "prompt":
                    "We ___ a lot of photos on holiday.",

                "options": [
                    "taked",
                    "took",
                    "take",
                    "taken",
                ],

                "answer":
                    "took",

                "explanation":
                    "TAKE → TOOK.",
            },


            {
                "order": 23,

                "prompt":
                    "He ___ me his phone number.",

                "options": [
                    "gived",
                    "gave",
                    "give",
                    "given",
                ],

                "answer":
                    "gave",

                "explanation":
                    "GIVE → GAVE.",
            },


            {
                "order": 24,

                "prompt":
                    "They ___ the answer immediately.",

                "options": [
                    "knowed",
                    "knew",
                    "know",
                    "known",
                ],

                "answer":
                    "knew",

                "explanation":
                    "KNOW → KNEW.",
            },


            {
                "order": 25,

                "prompt":
                    "She ___ an email to her manager.",

                "options": [
                    "writed",
                    "wrote",
                    "written",
                    "write",
                ],

                "answer":
                    "wrote",

                "explanation":
                    "WRITE → WROTE.",
            },


            {
                "order": 26,

                "prompt":
                    "I didn't ___ breakfast this morning.",

                "options": [
                    "had",
                    "have",
                    "has",
                    "having",
                ],

                "answer":
                    "have",

                "explanation":
                    "После DIDN'T используется V1 → HAVE.",
            },


            {
                "order": 27,

                "prompt":
                    "Did she ___ the documents?",

                "options": [
                    "brought",
                    "bring",
                    "brings",
                    "bringing",
                ],

                "answer":
                    "bring",

                "explanation":
                    "После DID используется V1 → BRING.",
            },


            {
                "order": 28,

                "prompt":
                    "What did they ___ at the restaurant?",

                "options": [
                    "ate",
                    "eat",
                    "eaten",
                    "eating",
                ],

                "answer":
                    "eat",

                "explanation":
                    "После DID используется базовая форма EAT.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "Who took my phone?",
                    "Who did took my phone?",
                    "Who did take my phone did?",
                    "Who taken my phone?",
                ],

                "answer":
                    "Who took my phone?",

                "explanation":
                    "WHO выполняет действие → используем V2 без DID.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sequence.",

                "options": [
                    "She went. / She didn't go. / Did she go?",
                    "She went. / She didn't went. / Did she went?",
                    "She go. / She didn't went. / Did she go?",
                    "She was went. / She didn't go. / Was she go?",
                ],

                "answer":
                    "She went. / She didn't go. / Did she go?",

                "explanation":
                    "V2 используется в утверждении; после DIDN'T и DID возвращаемся к V1.",
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
                "✅ Interactive A1 Lesson 26 seeded"
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
