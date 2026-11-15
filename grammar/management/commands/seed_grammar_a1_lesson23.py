from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 23: Present Simple vs Present Continuous."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=23,

                defaults={
                    "title":
                        "Present Simple и "
                        "Present Continuous",

                    "slug":
                        "present-simple-vs-continuous",

                    "theory_text":
                        "Present Simple vs Present Continuous.",

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
                    "Обычно или прямо сейчас?",

                "body":
                    """Главное различие очень простое.

Present Simple:

что происходит обычно;
регулярно;
постоянно.

I work every day.

Present Continuous:

что происходит сейчас;
временно;
в текущий период.

I am working now.

Главный вопрос:

это ОБЫЧНО
или СЕЙЧАС?""",
            },


            {
                "order": 2,

                "title":
                    "Present Simple: привычки и факты",

                "body":
                    """Present Simple используется для:

привычек;

регулярных действий;

фактов;

постоянных ситуаций.

Примеры:

I get up at seven every day.

She lives in Astana.

They play football on Sundays.

Water boils at 100°C.

Частые маркеры:

always

usually

often

sometimes

never

every day

on Mondays.""",
            },


            {
                "order": 3,

                "title":
                    "Present Continuous: сейчас и временно",

                "body":
                    """Present Continuous используется для:

действия прямо сейчас;

временной ситуации;

процесса текущего периода.

Примеры:

I am working now.

She is talking on the phone.

We are studying for an exam this week.

He is living with his parents this month.

Частые маркеры:

now

right now

at the moment

today

this week

these days.""",
            },


            {
                "order": 4,

                "title":
                    "Постоянное или временное?",

                "body":
                    """Present Simple часто описывает постоянную ситуацию.

I live in Karaganda.

She works at a university.

Present Continuous показывает временность.

I am living in Almaty this month.

She is working at home this week.

Сравни:

He works in a bank.

He is working in another office this week.""",
            },


            {
                "order": 5,

                "title":
                    "Факт или изменение?",

                "body":
                    """Факты обычно требуют Present Simple.

Water freezes at 0°C.

The Earth moves around the Sun.

Children need care.

Изменения и развивающиеся процессы:

The weather is getting colder.

Prices are rising.

My English is improving.

The child is growing quickly.

Если ситуация постепенно меняется, часто нужен Present Continuous.""",
            },


            {
                "order": 6,

                "title":
                    "Расписание или личный план?",

                "body":
                    """Present Simple используется для официального расписания.

The lesson starts at nine.

The train leaves at six.

The shop opens at ten.

Present Continuous может использоваться для заранее согласованного личного плана.

I am meeting my teacher tomorrow.

We are having dinner with friends tonight.

She is flying to Astana on Friday.

Коротко:

schedule → Present Simple

personal arrangement → Present Continuous.""",
            },


            {
                "order": 7,

                "title":
                    "Вопросы и отрицания",

                "body":
                    """Present Simple использует DO / DOES.

Do you work here?

Does she live in Astana?

I don't work on Sundays.

She doesn't drive.

Present Continuous использует AM / IS / ARE.

Are you working now?

Is she sleeping?

I'm not working now.

She isn't driving.

Не смешивай системы:

Does she working? ❌

Is she work? ❌""",
            },


            {
                "order": 8,

                "title":
                    "Stative verbs",

                "body":
                    """Некоторые глаголы обычно описывают состояние, а не действие.

Частые примеры:

know

understand

like

love

want

need

believe

remember

prefer

own

belong

Поэтому обычно:

I know the answer.

He likes coffee.

They need help.

Не:

I am knowing the answer.

He is liking coffee.""",
            },


            {
                "order": 9,

                "title":
                    "THINK, HAVE, SEE и LOOK",

                "body":
                    """Некоторые глаголы меняют форму в зависимости от значения.

THINK = мнение:

I think he is right.

THINK = размышлять сейчас:

I am thinking about the problem.

HAVE = владеть:

I have a car.

HAVE = действие:

I am having lunch.

SEE = видеть:

I see a bird.

SEE = встречаться:

I am seeing the doctor tomorrow.

LOOK = выглядеть:

You look tired.

LOOK AT = смотреть:

He is looking at the picture.""",
            },


            {
                "order": 10,

                "title":
                    "Как быстро выбрать время",

                "body":
                    """Алгоритм:

1. Привычка, факт, постоянная ситуация?

→ Present Simple.

2. Происходит сейчас?

→ Present Continuous.

3. Временная ситуация?

→ Present Continuous.

4. Постепенное изменение?

→ Present Continuous.

5. Расписание?

→ Present Simple.

6. Личная договорённость на будущее?

→ Present Continuous.

И только после этого смотри на маркеры.

every day → обычно Simple

now → обычно Continuous

Но смысл важнее одного слова.""",
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
                    "I usually ___ at seven.",

                "options": [
                    "am getting up",
                    "get up",
                    "gets up",
                    "getting up",
                ],

                "answer":
                    "get up",

                "explanation":
                    "USUALLY показывает привычку → Present Simple.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ dressed right now.",

                "options": [
                    "get",
                    "gets",
                    "am getting",
                    "getting",
                ],

                "answer":
                    "am getting",

                "explanation":
                    "RIGHT NOW → действие происходит сейчас.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "She usually ___ tea in the morning.",

                "options": [
                    "drinks",
                    "is drinking",
                    "drink",
                    "drinking",
                ],

                "answer":
                    "drinks",

                "explanation":
                    "Обычная привычка; SHE → DRINKS.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Water ___ at 100°C.",

                "options": [
                    "is boiling",
                    "boils",
                    "boil",
                    "boiling",
                ],

                "answer":
                    "boils",

                "explanation":
                    "Общий факт → Present Simple.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "She ___ tea at the moment.",

                "options": [
                    "drinks",
                    "drink",
                    "is drinking",
                    "drinking",
                ],

                "answer":
                    "is drinking",

                "explanation":
                    "AT THE MOMENT → Present Continuous.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "fill",

                "prompt":
                    "We ___ studying for an exam this week. (be)",

                "options": [],

                "answer":
                    "are",

                "explanation":
                    "WE → ARE; THIS WEEK показывает текущую временную ситуацию.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "My brother normally ___ in Astana.",

                "options": [
                    "lives",
                    "is living",
                    "live",
                    "living",
                ],

                "answer":
                    "lives",

                "explanation":
                    "NORMALY здесь показывает обычную постоянную ситуацию.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "My brother ___ with us this month.",

                "options": [
                    "lives every month",
                    "is living",
                    "live",
                    "living",
                ],

                "answer":
                    "is living",

                "explanation":
                    "THIS MONTH делает ситуацию временной.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Which sentence describes a gradual change?",

                "options": [
                    "Prices rise every January.",
                    "Prices are rising.",
                    "Prices rises now.",
                    "Prices is rising.",
                ],

                "answer":
                    "Prices are rising.",

                "explanation":
                    "Развивающийся процесс → Present Continuous.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "The Earth ___ around the Sun.",

                "options": [
                    "is moving now",
                    "moves",
                    "move",
                    "moving",
                ],

                "answer":
                    "moves",

                "explanation":
                    "Научный факт → Present Simple.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "The train ___ at 7:15 tomorrow morning.",

                "options": [
                    "leaves",
                    "is leaving personally",
                    "leave",
                    "leaving",
                ],

                "answer":
                    "leaves",

                "explanation":
                    "Расписание поезда → Present Simple.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "We ___ our teacher tomorrow after lunch.",

                "options": [
                    "meet every day",
                    "are meeting",
                    "meets",
                    "meeting",
                ],

                "answer":
                    "are meeting",

                "explanation":
                    "Заранее согласованная личная встреча → Present Continuous.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct question about a regular job.",

                "options": [
                    "Are you work here?",
                    "Do you work here?",
                    "Are you working here every day now?",
                    "Do you working here?",
                ],

                "answer":
                    "Do you work here?",

                "explanation":
                    "Постоянная работа → Present Simple → DO.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct question about now.",

                "options": [
                    "Do you working now?",
                    "Are you working now?",
                    "Are you work now?",
                    "Does you work now?",
                ],

                "answer":
                    "Are you working now?",

                "explanation":
                    "Действие сейчас → ARE + YOU + WORKING.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I am knowing the answer.",
                    "I know the answer.",
                    "I knowing the answer.",
                    "I am know the answer.",
                ],

                "answer":
                    "I know the answer.",

                "explanation":
                    "KNOW — stative verb.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "He ___ this film.",

                "options": [
                    "is liking",
                    "likes",
                    "like",
                    "liking",
                ],

                "answer":
                    "likes",

                "explanation":
                    "LIKE обычно используется в Present Simple.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "I ___ he is right.",

                "options": [
                    "think",
                    "am thinking",
                    "thinking",
                    "thinks",
                ],

                "answer":
                    "think",

                "explanation":
                    "THINK здесь означает мнение → Present Simple.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "I ___ about changing my job this week.",

                "options": [
                    "think every day",
                    "am thinking",
                    "thinks",
                    "thinking",
                ],

                "answer":
                    "am thinking",

                "explanation":
                    "THINK означает процесс размышления → Continuous.",
            },


            {
                "order": 19,
                "section": 9,
                "type": "choice",

                "prompt":
                    "They ___ lunch at the moment.",

                "options": [
                    "have",
                    "are having",
                    "has",
                    "having",
                ],

                "answer":
                    "are having",

                "explanation":
                    "HAVE LUNCH — действие; AT THE MOMENT → Continuous.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "build",

                "prompt":
                    "Собери правильную пару.",

                "options": [
                    "She",
                    "reads",
                    "every",
                    "evening",
                    "/",
                    "She",
                    "is",
                    "reading",
                    "now",
                ],

                "answer":
                    "She reads every evening / She is reading now",

                "explanation":
                    "EVERY EVENING → Simple; NOW → Continuous.",
            },

        ]


        final_test = [

            {
                "order": 21,

                "prompt":
                    "He usually ___ to work by car.",

                "options": [
                    "is going",
                    "goes",
                    "go",
                    "going",
                ],

                "answer":
                    "goes",

                "explanation":
                    "USUALLY → Present Simple; HE → GOES.",
            },


            {
                "order": 22,

                "prompt":
                    "Look! He ___ to work now.",

                "options": [
                    "goes",
                    "go",
                    "is going",
                    "going",
                ],

                "answer":
                    "is going",

                "explanation":
                    "LOOK! и NOW показывают действие сейчас.",
            },


            {
                "order": 23,

                "prompt":
                    "Which sentence describes a permanent situation?",

                "options": [
                    "She works at a university.",
                    "She is working at home this week.",
                    "She is staying with friends this month.",
                    "She is working on a temporary project.",
                ],

                "answer":
                    "She works at a university.",

                "explanation":
                    "Постоянная работа → Present Simple.",
            },


            {
                "order": 24,

                "prompt":
                    "Which sentence describes a temporary situation?",

                "options": [
                    "I live in Kazakhstan.",
                    "I am staying in Astana this week.",
                    "I work every weekday.",
                    "My parents live in Karaganda.",
                ],

                "answer":
                    "I am staying in Astana this week.",

                "explanation":
                    "THIS WEEK показывает временность.",
            },


            {
                "order": 25,

                "prompt":
                    "The weather ___ warmer these days.",

                "options": [
                    "gets every day normally",
                    "is getting",
                    "get",
                    "getting",
                ],

                "answer":
                    "is getting",

                "explanation":
                    "Постепенное изменение → Present Continuous.",
            },


            {
                "order": 26,

                "prompt":
                    "The lesson ___ at 10:00 tomorrow.",

                "options": [
                    "starts",
                    "is starting as a personal plan",
                    "start",
                    "starting",
                ],

                "answer":
                    "starts",

                "explanation":
                    "Официальное расписание → Present Simple.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I am needing more time.",
                    "I need more time.",
                    "I needing more time.",
                    "I am need more time.",
                ],

                "answer":
                    "I need more time.",

                "explanation":
                    "NEED обычно является stative verb.",
            },


            {
                "order": 28,

                "prompt":
                    "Which sentence uses HAVE as an action?",

                "options": [
                    "She has two sisters.",
                    "He has a new car.",
                    "We are having dinner now.",
                    "The house has a garden.",
                ],

                "answer":
                    "We are having dinner now.",

                "explanation":
                    "HAVE DINNER — действие, поэтому Continuous возможен.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "Do they play on Sundays? / Are they playing now?",
                    "Are they play on Sundays? / Do they playing now?",
                    "Do they playing on Sundays? / Are they play now?",
                    "Are they playing every Sunday usually? / Does they play now?",
                ],

                "answer":
                    "Do they play on Sundays? / Are they playing now?",

                "explanation":
                    "Регулярность → Present Simple; NOW → Present Continuous.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct set.",

                "options": [
                    "I work every day. / I am working now. / The train leaves at six. / We are meeting Anna tonight.",
                    "I am working every day. / I work now. / The train is leave at six. / We meet Anna tonight right now.",
                    "I work every day. / I working now. / The train leave at six. / We are meet Anna tonight.",
                    "I am work every day. / I am working now. / The train leavesing at six. / We meeting Anna tonight.",
                ],

                "answer":
                    "I work every day. / I am working now. / The train leaves at six. / We are meeting Anna tonight.",

                "explanation":
                    "Привычка и расписание → Simple; действие сейчас и личная договорённость → Continuous.",
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
                "✅ Interactive A1 Lesson 23 seeded"
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
