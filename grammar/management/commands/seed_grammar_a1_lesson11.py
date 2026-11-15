from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 11: Present Simple."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=11,

                defaults={
                    "title":
                        "Present Simple "
                        "с обычными глаголами",

                    "slug":
                        "present-simple-verbs",

                    "theory_text":
                        "Present Simple "
                        "with ordinary verbs.",

                    "estimated_minutes":
                        17,

                    "pass_score":
                        70,

                    "xp_reward":
                        100,

                    "is_published":
                        True,
                },
            )
        )


        # ================================================
        # 9 MICRO-RULES
        # ================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Когда нужен Present Simple?",

                "body":
                    """Present Simple используется, когда мы говорим о том, что происходит регулярно или является фактом.

Регулярные действия:

I work every day.

She visits her parents on Sundays.

Привычки:

I drink coffee in the morning.

He reads before bed.

Постоянные ситуации:

I live in Karaganda.

She works at a school.

Факты:

Water boils at 100°C.

Расписание:

The lesson starts at nine.""",
            },


            {
                "order": 2,

                "title":
                    "I, YOU, WE, THEY — обычная форма",

                "body":
                    """С I, YOU, WE и THEY обычный глагол используется без окончания -s.

I work.

You work.

We work.

They work.

Другие примеры:

I live in Kazakhstan.

You speak English.

We study together.

They play football.

Главная схема:

I / you / we / they
→ base verb.""",
            },


            {
                "order": 3,

                "title":
                    "HE, SHE, IT — добавляем -S",

                "body":
                    """С HE, SHE и IT к обычному глаголу обычно добавляется -s.

I work.
He works.

They live.
She lives.

We read.
He reads.

Это правило действует и с существительными.

Marat = he:

Marat works here.

My sister = she:

My sister lives in Almaty.

The phone = it:

The phone costs a lot.""",
            },


            {
                "order": 4,

                "title":
                    "Когда добавляется -ES?",

                "body":
                    """После некоторых окончаний обычно добавляется -es:

-s
-ss
-sh
-ch
-x
-o

Примеры:

go → goes

do → does

watch → watches

wash → washes

teach → teaches

fix → fixes

Примеры в предложениях:

He goes to work by bus.

She watches TV.

My father fixes computers.""",
            },


            {
                "order": 5,

                "title":
                    "STUDY → STUDIES, но PLAY → PLAYS",

                "body":
                    """Если глагол заканчивается на согласную + y:

y меняется на i + es.

study → studies

try → tries

carry → carries

fly → flies

He studies English.

Но если перед Y стоит гласная:

просто добавляем -s.

play → plays

stay → stays

enjoy → enjoys

buy → buys

She plays tennis.""",
            },


            {
                "order": 6,

                "title":
                    "HAVE превращается в HAS",

                "body":
                    """HAVE имеет особую форму.

I / you / we / they:

have

I have a car.

They have two children.

HE / SHE / IT:

has

He has a car.

She has a new job.

Не:

he haves

Правильно:

he has.""",
            },


            {
                "order": 7,

                "title":
                    "Always, usually, often, sometimes, never",

                "body":
                    """Present Simple часто используется с маркерами частоты:

always

usually

often

sometimes

rarely

never

every day

every week

on Mondays

once a week

twice a month

С обычным глаголом наречие частотности обычно стоит ПЕРЕД глаголом:

I often read.

She always comes early.

They never smoke.

Но с TO BE оно обычно стоит после AM / IS / ARE:

She is often at home.

They are usually busy.""",
            },


            {
                "order": 8,

                "title":
                    "Один человек или несколько?",

                "body":
                    """Сначала посмотри на подлежащее.

My brother = HE:

My brother works.

My parents = THEY:

My parents work.

Marat and Aigul = THEY:

Marat and Aigul live here.

The student = HE / SHE:

The student studies English.

The students = THEY:

The students study English.

Полезный способ:

замени подлежащее на местоимение.

HE / SHE / IT
→ -s / -es

I / YOU / WE / THEY
→ без -s.""",
            },


            {
                "order": 9,

                "title":
                    "Present Simple или TO BE?",

                "body":
                    """Не ставь AM / IS / ARE перед обычным смысловым глаголом.

TO BE нужен для описания:

She is a teacher.

She is tired.

She is at home.

Обычный глагол показывает действие:

She teaches English.

She works hard.

She lives in Astana.

Не:

She is works.

He is lives here.

They are study English.

А:

She works.

He lives here.

They study English.

Главный вопрос:

это состояние / описание?

→ TO BE

или действие?

→ обычный глагол.""",
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


        # ================================================
        # 20 TRAINING EXERCISES
        # ================================================

        training = [

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ coffee every morning.",

                "options": [
                    "drink",
                    "drinks",
                    "am drink",
                    "drinking",
                ],

                "answer":
                    "drink",

                "explanation":
                    "Это регулярное действие. "
                    "С I используется базовая форма.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "The lesson ___ at nine every day.",

                "options": [
                    "start",
                    "starts",
                    "starting",
                    "is start",
                ],

                "answer":
                    "starts",

                "explanation":
                    "The lesson = IT, "
                    "а расписание выражается Present Simple.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "We ___ in Karaganda. "
                    "(live)",

                "options": [],

                "answer":
                    "live",

                "explanation":
                    "WE → базовая форма LIVE.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "They ___ English twice a week.",

                "options": [
                    "studies",
                    "study",
                    "studys",
                    "are study",
                ],

                "answer":
                    "study",

                "explanation":
                    "THEY → STUDY без -s.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "Marat ___ at a university.",

                "options": [
                    "work",
                    "works",
                    "working",
                    "is work",
                ],

                "answer":
                    "works",

                "explanation":
                    "Marat = HE → WORKS.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "fill",

                "prompt":
                    "My sister ___ in Astana. "
                    "(live)",

                "options": [],

                "answer":
                    "lives",

                "explanation":
                    "My sister = SHE → LIVES.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "He ___ TV every evening.",

                "options": [
                    "watch",
                    "watchs",
                    "watches",
                    "is watch",
                ],

                "answer":
                    "watches",

                "explanation":
                    "WATCH заканчивается на -ch, "
                    "поэтому добавляется -es.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "My father ___ to work by car.",

                "options": [
                    "go",
                    "gos",
                    "goes",
                    "going",
                ],

                "answer":
                    "goes",

                "explanation":
                    "GO → GOES для HE / SHE / IT.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "She ___ English every day.",

                "options": [
                    "study",
                    "studys",
                    "studies",
                    "studyes",
                ],

                "answer":
                    "studies",

                "explanation":
                    "STUDY: согласная + Y → STUDIES.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "He ___ football on Sundays.",

                "options": [
                    "play",
                    "plaies",
                    "plays",
                    "playes",
                ],

                "answer":
                    "plays",

                "explanation":
                    "В PLAY перед Y стоит гласная, "
                    "поэтому просто добавляем -s.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "My parents ___ a car.",

                "options": [
                    "has",
                    "have",
                    "haves",
                    "are have",
                ],

                "answer":
                    "have",

                "explanation":
                    "My parents = THEY → HAVE.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "fill",

                "prompt":
                    "She ___ two children. "
                    "(have)",

                "options": [],

                "answer":
                    "has",

                "explanation":
                    "SHE → HAS.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I often read before bed.",
                    "I read often before bed.",
                    "I am often read before bed.",
                    "I often reads before bed.",
                ],

                "answer":
                    "I often read before bed.",

                "explanation":
                    "С обычным глаголом OFTEN "
                    "обычно ставится перед глаголом.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She always comes early.",
                    "She comes always early.",
                    "She is always comes early.",
                    "She always come early.",
                ],

                "answer":
                    "She always comes early.",

                "explanation":
                    "ALWAYS стоит перед смысловым глаголом, "
                    "а SHE требует COMES.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence with TO BE.",

                "options": [
                    "She often is at home.",
                    "She is often at home.",
                    "She is at often home.",
                    "She often at home.",
                ],

                "answer":
                    "She is often at home.",

                "explanation":
                    "С TO BE наречие частотности "
                    "обычно стоит после IS.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "My brother and I ___ football on Saturdays.",

                "options": [
                    "plays",
                    "play",
                    "playing",
                    "are play",
                ],

                "answer":
                    "play",

                "explanation":
                    "My brother and I = WE → PLAY.",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "The teacher ___ many questions.",

                "options": [
                    "ask",
                    "asks",
                    "asking",
                    "is ask",
                ],

                "answer":
                    "asks",

                "explanation":
                    "The teacher — один человек → ASKS.",
            },


            {
                "order": 18,
                "section": 8,
                "type": "choice",

                "prompt":
                    "The students ___ many questions.",

                "options": [
                    "asks",
                    "ask",
                    "asking",
                    "are ask",
                ],

                "answer":
                    "ask",

                "explanation":
                    "The students = THEY → ASK.",
            },


            {
                "order": 19,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She is works every day.",
                    "She work every day.",
                    "She works every day.",
                    "She is work every day.",
                ],

                "answer":
                    "She works every day.",

                "explanation":
                    "WORKS — обычный смысловой глагол. "
                    "IS перед ним не нужен.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "He is tired. / He works hard.",
                    "He tired. / He is works hard.",
                    "He is tired. / He is work hard.",
                    "He works tired. / He is hard.",
                ],

                "answer":
                    "He is tired. / He works hard.",

                "explanation":
                    "TIRED — состояние с TO BE. "
                    "WORKS — действие без IS.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "I ___ to work every day.",

                "options": [
                    "go",
                    "goes",
                    "am go",
                    "going",
                ],

                "answer":
                    "go",

                "explanation":
                    "I → базовая форма GO.",
            },


            {
                "order": 22,

                "prompt":
                    "My brother ___ to work every day.",

                "options": [
                    "go",
                    "goes",
                    "gos",
                    "is go",
                ],

                "answer":
                    "goes",

                "explanation":
                    "My brother = HE → GOES.",
            },


            {
                "order": 23,

                "prompt":
                    "The children ___ English at school.",

                "options": [
                    "studies",
                    "study",
                    "studys",
                    "are study",
                ],

                "answer":
                    "study",

                "explanation":
                    "Children = THEY → STUDY.",
            },


            {
                "order": 24,

                "prompt":
                    "Anna ___ English at university.",

                "options": [
                    "study",
                    "studys",
                    "studies",
                    "is study",
                ],

                "answer":
                    "studies",

                "explanation":
                    "Anna = SHE; STUDY → STUDIES.",
            },


            {
                "order": 25,

                "prompt":
                    "My father ___ his car every weekend.",

                "options": [
                    "wash",
                    "washs",
                    "washes",
                    "is wash",
                ],

                "answer":
                    "washes",

                "explanation":
                    "WASH заканчивается на -sh → WASHES.",
            },


            {
                "order": 26,

                "prompt":
                    "She ___ a new job.",

                "options": [
                    "have",
                    "haves",
                    "has",
                    "is have",
                ],

                "answer":
                    "has",

                "explanation":
                    "SHE → HAS.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "They usually eat lunch at one.",
                    "They eat usually lunch at one.",
                    "They are usually eat lunch at one.",
                    "They usually eats lunch at one.",
                ],

                "answer":
                    "They usually eat lunch at one.",

                "explanation":
                    "USUALLY стоит перед обычным глаголом; "
                    "THEY → EAT.",
            },


            {
                "order": 28,

                "prompt":
                    "The train ___ at 7:30 every morning.",

                "options": [
                    "leave",
                    "leaves",
                    "is leave",
                    "leaving",
                ],

                "answer":
                    "leaves",

                "explanation":
                    "Расписание выражается Present Simple. "
                    "The train = IT → LEAVES.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "My parents lives in Almaty.",
                    "My parents live in Almaty.",
                    "My parents are live in Almaty.",
                    "My parents living in Almaty.",
                ],

                "answer":
                    "My parents live in Almaty.",

                "explanation":
                    "My parents = THEY → LIVE.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct option.",

                "options": [
                    "She is a doctor and works at a hospital.",
                    "She doctor and is works at a hospital.",
                    "She is a doctor and is work at a hospital.",
                    "She works a doctor and is at hospital work.",
                ],

                "answer":
                    "She is a doctor and works at a hospital.",

                "explanation":
                    "Профессия требует IS, "
                    "а WORKS — самостоятельный смысловой глагол.",
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
                "✅ Interactive A1 Lesson 11 seeded"
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
