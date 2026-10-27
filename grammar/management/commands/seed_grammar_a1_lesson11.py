from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 11: "
        "Present Simple with ordinary verbs."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=11,
            defaults={
                "title": (
                    "Present Simple с обычными глаголами"
                ),
                "slug": "present-simple-verbs",
                "theory_text": (
                    "Present Simple with ordinary verbs."
                ),
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое Present Simple",
                "body": """Present Simple — это настоящее простое время.

Оно используется, когда мы говорим:

о регулярных действиях;

о привычках;

о фактах;

о расписании;

о постоянных ситуациях.

Примеры:

I work every day.

She lives in Astana.

They study English.

Water boils at 100°C.""",
            },

            {
                "order": 2,
                "title": "Обычный глагол",
                "body": """Обычный глагол обозначает действие.

Например:

work — работать;

live — жить;

study — учиться;

read — читать;

speak — говорить;

play — играть;

like — нравиться;

know — знать.

Сравните:

I am a teacher.

Здесь am — форма to be.

I work at a school.

Здесь work — обычный смысловой глагол.""",
            },

            {
                "order": 3,
                "title": "I, YOU, WE, THEY",
                "body": """С местоимениями:

I;

you;

we;

they

глагол обычно используется в начальной форме.

Примеры:

I work.

You work.

We work.

They work.

Ещё:

I live in Kazakhstan.

You speak English.

We study together.

They play football.""",
            },

            {
                "order": 4,
                "title": "HE, SHE, IT и окончание -S",
                "body": """С he, she, it к глаголу обычно добавляется -s.

Сравните:

I work.
He works.

They live.
She lives.

We read.
He reads.

Главная схема:

I work

you work

he works

she works

it works

we work

they work

Если подлежащее можно заменить на he, she или it, обычно нужен -s.""",
            },

            {
                "order": 5,
                "title": "Имена и существительные",
                "body": """Правило -s работает не только с местоимениями.

Marat = he:

Marat works here.

My sister = she:

My sister lives in Almaty.

The phone = it:

The phone costs a lot.

Но:

Marat and Aigul = they:

Marat and Aigul work here.

My parents = they:

My parents live in Karaganda.""",
            },

            {
                "order": 6,
                "title": "Окончание -ES",
                "body": """Если глагол заканчивается на:

-s;
-ss;
-sh;
-ch;
-x;
-o,

часто добавляется -es.

Примеры:

go → goes;

do → does;

watch → watches;

wash → washes;

teach → teaches;

fix → fixes;

miss → misses.

Предложения:

He goes to work by bus.

She watches television.

My father fixes computers.

The teacher teaches English.""",
            },

            {
                "order": 7,
                "title": "Глаголы на Y",
                "body": """Если глагол заканчивается на согласную + y:

y меняется на i + es.

study → studies;

try → tries;

carry → carries;

fly → flies.

Примеры:

He studies English.

She tries to help.

Но если перед y стоит гласная, просто добавляется -s:

play → plays;

stay → stays;

enjoy → enjoys;

buy → buys.

He plays football.

She enjoys music.""",
            },

            {
                "order": 8,
                "title": "HAVE и HAS",
                "body": """Глагол have означает «иметь».

С:

I;
you;
we;
they

используется have.

I have a car.

They have two children.

С:

he;
she;
it

используется has.

He has a car.

She has a new job.

Неправильно:

He haves a car.

Правильно:

He has a car.""",
            },

            {
                "order": 9,
                "title": "Когда используется Present Simple",
                "body": """Present Simple используется для регулярных действий:

I go to work every day.

She visits her parents on Sundays.

Для привычек:

I drink coffee in the morning.

He reads before bed.

Для фактов:

Water freezes at 0°C.

The Earth moves around the Sun.

Для постоянных ситуаций:

I live in Karaganda.

She works at a school.

Для расписания:

The train leaves at six.

The lesson starts at nine.""",
            },

            {
                "order": 10,
                "title": "Слова-маркеры",
                "body": """Present Simple часто используется со словами:

always — всегда;

usually — обычно;

often — часто;

sometimes — иногда;

rarely — редко;

never — никогда;

every day;

every week;

on Mondays;

once a week;

twice a month.

Примеры:

I always drink tea in the morning.

She usually walks to work.

He often calls his parents.

They never arrive late.""",
            },

            {
                "order": 11,
                "title": "Где ставить ALWAYS, OFTEN, NEVER",
                "body": """С обычным глаголом наречие частотности обычно ставится перед глаголом:

I often read.

She always comes early.

They never smoke.

He usually works at home.

Но с глаголом to be наречие ставится после am/is/are:

I am always tired.

She is usually at home.

They are often busy.

Сравните:

She often works at home.

She is often at home.""",
            },

            {
                "order": 12,
                "title": "Утвердительные предложения",
                "body": """Для I, you, we, they:

Подлежащее + глагол.

I work.

You study.

We live here.

They play tennis.

Для he, she, it:

Подлежащее + глагол с -s/-es.

He works.

She studies.

It starts at nine.

Сравните:

I read every day.

My brother reads every day.

They watch television.

He watches television.""",
            },

            {
                "order": 13,
                "title": "Present Simple и TO BE",
                "body": """Нельзя соединять am/is/are с обычным смысловым глаголом.

Неправильно:

I am work every day.

She is lives in Astana.

They are study English.

Правильно:

I work every day.

She lives in Astana.

They study English.

To be нужен, если мы говорим о:

профессии;

состоянии;

месте;

возрасте.

She is a teacher.

She is tired.

She is at work.

Но:

She teaches English.

She works hard.

She lives in Astana.""",
            },

            {
                "order": 14,
                "title": "Как выбрать форму глагола",
                "body": """Шаг 1. Найдите подлежащее.

My sister ___ English.

Шаг 2. Замените его местоимением.

My sister = she.

Шаг 3. Добавьте нужное окончание.

My sister speaks English.

Другой пример:

My parents ___ English.

My parents = they.

С they -s не добавляется.

My parents speak English.

Главное правило:

I / you / we / they → глагол без -s.

He / she / it → глагол с -s или -es.

Особые формы:

study → studies;

go → goes;

do → does;

have → has.""",
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
                "prompt": "I ___ at a university.",
                "options": ["works", "work", "working", "am work"],
                "answer": "work",
                "explanation": "С I обычный глагол используется без -s.",
            },

            {
                "order": 2,
                "prompt": "Marat ___ at a university.",
                "options": ["work", "working", "works", "is work"],
                "answer": "works",
                "explanation": "Marat = he, поэтому к work добавляется -s.",
            },

            {
                "order": 3,
                "prompt": "They ___ in Astana.",
                "options": ["lives", "live", "living", "are live"],
                "answer": "live",
                "explanation": "С they глагол используется без -s.",
            },

            {
                "order": 4,
                "prompt": "My sister ___ in Astana.",
                "options": ["live", "living", "lives", "is live"],
                "answer": "lives",
                "explanation": "My sister = she, поэтому lives.",
            },

            {
                "order": 5,
                "prompt": "He ___ English every day.",
                "options": ["study", "studys", "studies", "studying"],
                "answer": "studies",
                "explanation": "Study заканчивается на согласную + y: study → studies.",
            },

            {
                "order": 6,
                "prompt": "She ___ football on Sundays.",
                "options": ["plays", "plaies", "play", "is play"],
                "answer": "plays",
                "explanation": "В play перед y стоит гласная, поэтому просто добавляется -s.",
            },

            {
                "order": 7,
                "prompt": "The lesson ___ at nine.",
                "options": ["start", "starts", "starting", "is start"],
                "answer": "starts",
                "explanation": "The lesson = it, поэтому starts.",
            },

            {
                "order": 8,
                "prompt": "My father ___ a car.",
                "options": ["have", "haves", "has", "having"],
                "answer": "has",
                "explanation": "My father = he, поэтому используется has.",
            },

            {
                "order": 9,
                "prompt": "I ___ coffee every morning.",
                "options": ["drinks", "drink", "am drink", "drinking"],
                "answer": "drink",
                "explanation": "I → drink без окончания -s.",
            },

            {
                "order": 10,
                "prompt": "My wife ___ coffee every morning.",
                "options": ["drink", "drinks", "drinking", "is drink"],
                "answer": "drinks",
                "explanation": "My wife = she, поэтому drinks.",
            },

            {
                "order": 11,
                "prompt": "We ___ English twice a week.",
                "options": ["studies", "study", "studying", "are study"],
                "answer": "study",
                "explanation": "We → базовая форма study.",
            },

            {
                "order": 12,
                "prompt": "He ___ English twice a week.",
                "options": ["study", "studies", "studys", "is study"],
                "answer": "studies",
                "explanation": "He → studies.",
            },

            {
                "order": 13,
                "prompt": "They ___ television in the evening.",
                "options": ["watches", "watch", "watching", "are watch"],
                "answer": "watch",
                "explanation": "They → watch без -s.",
            },

            {
                "order": 14,
                "prompt": "She ___ television in the evening.",
                "options": ["watch", "watchs", "watches", "is watch"],
                "answer": "watches",
                "explanation": "Watch заканчивается на -ch, поэтому watches.",
            },

            {
                "order": 15,
                "prompt": "My parents ___ in Karaganda.",
                "options": ["lives", "live", "living", "are live"],
                "answer": "live",
                "explanation": "My parents = they, поэтому live.",
            },

            {
                "order": 16,
                "prompt": "My father ___ in Karaganda.",
                "options": ["live", "lives", "living", "is live"],
                "answer": "lives",
                "explanation": "My father = he, поэтому lives.",
            },

            {
                "order": 17,
                "prompt": "The shop ___ at nine.",
                "options": ["open", "opens", "opening", "is opens"],
                "answer": "opens",
                "explanation": "The shop = it. Также речь идёт о расписании.",
            },

            {
                "order": 18,
                "prompt": "The students ___ many questions.",
                "options": ["asks", "ask", "asking", "are ask"],
                "answer": "ask",
                "explanation": "Students = they, поэтому ask.",
            },

            {
                "order": 19,
                "prompt": "The teacher ___ many questions.",
                "options": ["ask", "asks", "asking", "is ask"],
                "answer": "asks",
                "explanation": "The teacher — один человек, поэтому asks.",
            },

            {
                "order": 20,
                "prompt": "She ___ two children.",
                "options": ["have", "haves", "has", "is have"],
                "answer": "has",
                "explanation": "С she используется особая форма has.",
            },

            {
                "order": 21,
                "prompt": "I usually ___ home at six.",
                "options": ["goes", "go", "going", "am go"],
                "answer": "go",
                "explanation": "I → go. Usually стоит перед обычным глаголом.",
            },

            {
                "order": 22,
                "prompt": "He always ___ his homework.",
                "options": ["do", "does", "dos", "is do"],
                "answer": "does",
                "explanation": "He → does. Always ставится перед смысловым глаголом.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She is works every day.",
                    "She work every day.",
                    "She works every day.",
                    "She working every day.",
                ],
                "answer": "She works every day.",
                "explanation": "С she нужен works, но to be перед обычным глаголом не ставится.",
            },

            {
                "order": 24,
                "prompt": "My brother and I ___ football on Saturdays.",
                "options": ["plays", "play", "playing", "are play"],
                "answer": "play",
                "explanation": "My brother and I = we, поэтому используется play без -s.",
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
                "✅ A1 Lesson 11 seeded: "
                "Present Simple с обычными глаголами"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
