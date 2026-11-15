from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 21: Present Continuous affirmative."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=21,

                defaults={
                    "title":
                        "Present Continuous: утверждение",

                    "slug":
                        "present-continuous-affirmative",

                    "theory_text":
                        "Present Continuous affirmative.",

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


        # ================================================
        # 10 MICRO-RULES
        # ================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Когда нужен Present Continuous?",

                "body":
                    """Present Continuous описывает действие, которое происходит сейчас или вокруг настоящего момента.

I am reading now.

She is talking on the phone.

They are playing football.

Также он используется для временных ситуаций:

I am living in Almaty this month.

И для процессов изменения:

The weather is getting colder.

Главная идея:

действие происходит сейчас,
временно
или развивается.""",
            },


            {
                "order": 2,

                "title":
                    "Главная формула",

                "body":
                    """Present Continuous состоит из двух частей:

AM / IS / ARE
+
verb-ing

Примеры:

I am working.

He is working.

They are working.

TO BE обязательно.

Не:

I working.

She reading.

А:

I am working.

She is reading.""",
            },


            {
                "order": 3,

                "title":
                    "AM, IS или ARE?",

                "body":
                    """Используем:

I → AM

he / she / it → IS

you / we / they → ARE

Примеры:

I am reading.

She is cooking.

The phone is charging.

We are studying.

The children are sleeping.

Существительное тоже можно заменить местоимением:

Marat = HE → is

My parents = THEY → are.""",
            },


            {
                "order": 4,

                "title":
                    "Обычное правило -ING",

                "body":
                    """В большинстве случаев просто добавляем -ING.

work → working

read → reading

play → playing

speak → speaking

cook → cooking

listen → listening

Примеры:

She is working.

They are playing.

I am reading.""",
            },


            {
                "order": 5,

                "title":
                    "Немая E исчезает",

                "body":
                    """Если глагол заканчивается на немую E, она обычно убирается.

make → making

write → writing

come → coming

take → taking

drive → driving

Не:

makeing

writeing

А:

making

writing.""",
            },


            {
                "order": 6,

                "title":
                    "Когда удваивается согласная",

                "body":
                    """У некоторых коротких глаголов последняя согласная удваивается.

sit → sitting

run → running

swim → swimming

stop → stopping

get → getting

put → putting

Не:

runing

swiming

А:

running

swimming.""",
            },


            {
                "order": 7,

                "title":
                    "IE → Y, но Y сохраняется",

                "body":
                    """Если глагол заканчивается на -IE:

IE → Y + ING

lie → lying

die → dying

tie → tying

Если глагол заканчивается на Y, Y обычно сохраняется:

study → studying

play → playing

carry → carrying

enjoy → enjoying

Не:

studing

А:

studying.""",
            },


            {
                "order": 8,

                "title":
                    "NOW, AT THE MOMENT, LOOK!",

                "body":
                    """Типичные маркеры Present Continuous:

now

right now

at the moment

currently

today

this week

these days

look!

listen!

Примеры:

I am working now.

She is studying at the moment.

Look! The dog is running.

Listen! Someone is knocking.""",
            },


            {
                "order": 9,

                "title":
                    "Временная ситуация и изменение",

                "body":
                    """Present Continuous может описывать временную ситуацию:

She is studying English this year.

We are working on a new project.

He is living with his parents this month.

Также постепенное изменение:

The weather is getting colder.

Prices are rising.

My English is improving.

The child is growing quickly.""",
            },


            {
                "order": 10,

                "title":
                    "Present Simple или Continuous?",

                "body":
                    """Present Simple:

привычка;
регулярное действие;
факт;
постоянная ситуация.

I work every day.

She reads every evening.

Present Continuous:

действие сейчас;
временная ситуация;
изменяющийся процесс.

I am working now.

She is reading now.

Некоторые глаголы состояния обычно не используются в Continuous:

know

understand

like

love

want

need

believe

remember

Поэтому:

I know the answer.

He likes coffee.

Не:

I am knowing the answer.

He is liking coffee.""",
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
                    "Which sentence describes an action happening now?",

                "options": [
                    "She reads every evening.",
                    "She is reading now.",
                    "She usually reads before bed.",
                    "She reads on Sundays.",
                ],

                "answer":
                    "She is reading now.",

                "explanation":
                    "NOW показывает действие в момент речи.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ working at home today.",

                "options": [
                    "am",
                    "is",
                    "are",
                    "do",
                ],

                "answer":
                    "am",

                "explanation":
                    "TODAY описывает текущую временную ситуацию; I → AM.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She working now.",
                    "She is working now.",
                    "She is work now.",
                    "She works at the moment.",
                ],

                "answer":
                    "She is working now.",

                "explanation":
                    "Present Continuous требует IS + WORKING.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери правильное предложение.",

                "options": [
                    "They",
                    "are",
                    "playing",
                    "football",
                    "now",
                ],

                "answer":
                    "They are playing football now",

                "explanation":
                    "Правильная схема: subject + ARE + verb-ing.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "My brother ___ sleeping.",

                "options": [],

                "answer":
                    "is",

                "explanation":
                    "My brother = HE → IS.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "The children ___ playing outside.",

                "options": [
                    "is",
                    "am",
                    "are",
                    "does",
                ],

                "answer":
                    "are",

                "explanation":
                    "Children = THEY → ARE.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "She is ___ a book.",

                "options": [
                    "read",
                    "reads",
                    "reading",
                    "readed",
                ],

                "answer":
                    "reading",

                "explanation":
                    "READ → READING.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "They are ___ football.",

                "options": [
                    "play",
                    "playing",
                    "plays",
                    "plaing",
                ],

                "answer":
                    "playing",

                "explanation":
                    "PLAY → PLAYING; Y сохраняется.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "He is ___ dinner.",

                "options": [
                    "makeing",
                    "making",
                    "makes",
                    "make",
                ],

                "answer":
                    "making",

                "explanation":
                    "MAKE теряет немую E → MAKING.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct form of WRITE.",

                "options": [
                    "writeing",
                    "writing",
                    "writting",
                    "writesing",
                ],

                "answer":
                    "writing",

                "explanation":
                    "WRITE → WRITING.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "They are ___ in the park.",

                "options": [
                    "runing",
                    "running",
                    "runs",
                    "run",
                ],

                "answer":
                    "running",

                "explanation":
                    "RUN → RUNNING.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "The baby is ___ on the chair.",

                "options": [
                    "siting",
                    "sitting",
                    "sits",
                    "sit",
                ],

                "answer":
                    "sitting",

                "explanation":
                    "SIT → SITTING.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "The man is ___ on the sofa.",

                "options": [
                    "lieing",
                    "lying",
                    "liing",
                    "lies",
                ],

                "answer":
                    "lying",

                "explanation":
                    "LIE → LYING.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "We are ___ for the exam.",

                "options": [
                    "studing",
                    "studying",
                    "study",
                    "studies",
                ],

                "answer":
                    "studying",

                "explanation":
                    "STUDY → STUDYING; Y сохраняется.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Look! The cat ___ climbing the tree.",

                "options": [
                    "am",
                    "is",
                    "are",
                    "does",
                ],

                "answer":
                    "is",

                "explanation":
                    "LOOK! указывает на происходящее сейчас; cat = IT → IS.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Listen! Someone ___ knocking at the door.",

                "options": [
                    "is",
                    "are",
                    "am",
                    "do",
                ],

                "answer":
                    "is",

                "explanation":
                    "Someone рассматривается как singular → IS.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Which sentence describes a temporary situation?",

                "options": [
                    "I live in Karaganda.",
                    "I am living in Almaty this month.",
                    "Water boils at 100°C.",
                    "I work every day.",
                ],

                "answer":
                    "I am living in Almaty this month.",

                "explanation":
                    "THIS MONTH показывает временную ситуацию.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Which sentence shows a gradual change?",

                "options": [
                    "The weather gets cold every winter.",
                    "The weather is getting colder.",
                    "The weather cold now.",
                    "The weather is get colder.",
                ],

                "answer":
                    "The weather is getting colder.",

                "explanation":
                    "GETTING COLDER описывает развивающийся процесс.",
            },


            {
                "order": 19,
                "section": 10,
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
                    "KNOW — stative verb и обычно не используется в Continuous.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "She works every day. / She is working now.",
                    "She is working every day. / She works now.",
                    "She work every day. / She working now.",
                    "She is work every day. / She works at the moment now.",
                ],

                "answer":
                    "She works every day. / She is working now.",

                "explanation":
                    "EVERY DAY → Present Simple; NOW → Present Continuous.",
            },

        ]


        # ================================================
        # 10 FINAL TEST QUESTIONS
        # ================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "I ___ talking to my teacher right now.",

                "options": [
                    "am",
                    "is",
                    "are",
                    "do",
                ],

                "answer":
                    "am",

                "explanation":
                    "I → AM; RIGHT NOW требует текущего действия.",
            },


            {
                "order": 22,

                "prompt":
                    "My parents ___ travelling this week.",

                "options": [
                    "is",
                    "are",
                    "am",
                    "does",
                ],

                "answer":
                    "are",

                "explanation":
                    "My parents = THEY → ARE.",
            },


            {
                "order": 23,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "The baby sleeping.",
                    "The baby is sleeping.",
                    "The baby is sleep.",
                    "The baby sleeps at the moment.",
                ],

                "answer":
                    "The baby is sleeping.",

                "explanation":
                    "Present Continuous = IS + SLEEPING.",
            },


            {
                "order": 24,

                "prompt":
                    "She is ___ a letter.",

                "options": [
                    "writeing",
                    "writing",
                    "writting",
                    "writes",
                ],

                "answer":
                    "writing",

                "explanation":
                    "WRITE → WRITING.",
            },


            {
                "order": 25,

                "prompt":
                    "The boys are ___.",

                "options": [
                    "swiming",
                    "swimming",
                    "swim",
                    "swims",
                ],

                "answer":
                    "swimming",

                "explanation":
                    "SWIM → SWIMMING.",
            },


            {
                "order": 26,

                "prompt":
                    "Choose the correct form of LIE.",

                "options": [
                    "lieing",
                    "lying",
                    "liing",
                    "lieying",
                ],

                "answer":
                    "lying",

                "explanation":
                    "IE меняется на Y перед -ING.",
            },


            {
                "order": 27,

                "prompt":
                    "Which sentence is happening now?",

                "options": [
                    "They play tennis every Saturday.",
                    "They are playing tennis now.",
                    "They usually play after work.",
                    "They play tennis twice a week.",
                ],

                "answer":
                    "They are playing tennis now.",

                "explanation":
                    "NOW указывает на действие в момент речи.",
            },


            {
                "order": 28,

                "prompt":
                    "Which sentence describes a temporary situation?",

                "options": [
                    "He lives with his family.",
                    "He is living with his friend this month.",
                    "He usually lives near work.",
                    "He lives in Kazakhstan.",
                ],

                "answer":
                    "He is living with his friend this month.",

                "explanation":
                    "THIS MONTH делает ситуацию временной.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She is liking this book.",
                    "She likes this book.",
                    "She liking this book.",
                    "She is like this book.",
                ],

                "answer":
                    "She likes this book.",

                "explanation":
                    "LIKE обычно является stative verb и используется в Present Simple.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct set.",

                "options": [
                    "I am working now. / She is writing. / They are running.",
                    "I working now. / She is writeing. / They are runing.",
                    "I am work now. / She writing. / They is running.",
                    "I works now. / She is writes. / They are run.",
                ],

                "answer":
                    "I am working now. / She is writing. / They are running.",

                "explanation":
                    "Все три предложения правильно используют AM/IS/ARE + verb-ing.",
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
                "✅ Interactive A1 Lesson 21 seeded"
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
