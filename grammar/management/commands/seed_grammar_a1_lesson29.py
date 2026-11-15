from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 29: Past Simple vs Past Continuous."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=29,

                defaults={
                    "title":
                        "Past Simple и Past Continuous",

                    "slug":
                        "past-simple-vs-past-continuous",

                    "theory_text":
                        "Past Simple vs Past Continuous.",

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
                    "Факт или процесс?",

                "body":
                    """Оба времени говорят о прошлом, но показывают действие по-разному.

Past Simple:

I worked yesterday.

Это завершённый факт.

Past Continuous:

I was working at six yesterday.

Это процесс в конкретный момент прошлого.

Главный вопрос:

действие завершилось как событие

или

оно было в процессе?""",
            },


            {
                "order": 2,

                "title":
                    "Когда нужен Past Simple?",

                "body":
                    """Past Simple используется для:

завершённого действия;

короткого события;

последовательности действий;

привычки в прошлом;

состояния в прошлом.

Примеры:

I finished the report.

She called me.

They went home.

We played outside every day.

He was tired.""",
            },


            {
                "order": 3,

                "title":
                    "Когда нужен Past Continuous?",

                "body":
                    """Past Continuous используется для:

процесса в прошлом;

действия в конкретный момент прошлого;

фона истории;

действия, которое было прервано;

двух параллельных процессов.

Примеры:

I was working at six.

She was sleeping when I called.

They were playing while we were studying.

It was raining.""",
            },


            {
                "order": 4,

                "title":
                    "Сравни формы",

                "body":
                    """Past Simple:

правильный глагол:

work → worked

неправильный:

go → went

Примеры:

I worked.

She went home.

Past Continuous:

WAS / WERE + verb-ing

I was working.

They were playing.

То есть:

Past Simple → факт

Past Continuous → процесс.""",
            },


            {
                "order": 5,

                "title":
                    "Конкретный момент прошлого",

                "body":
                    """Если действие было в процессе в определённый момент:

Past Continuous.

At six, I was working.

At midnight, she was sleeping.

This time yesterday, we were flying to Astana.

Но если указывается момент завершённого события:

Past Simple.

I started work at six.

She went to bed at midnight.

We arrived at seven.""",
            },


            {
                "order": 6,

                "title":
                    "Длинное действие + короткое событие",

                "body":
                    """Когда одно действие уже происходило, а второе произошло во время него:

длинный процесс
→ Past Continuous

короткое событие
→ Past Simple

I was sleeping when the phone rang.

She was cooking when I arrived.

We were driving home when the car stopped.

Схема:

Past Continuous
+ WHEN
+ Past Simple.""",
            },


            {
                "order": 7,

                "title":
                    "WHEN и WHILE",

                "body":
                    """WHEN часто вводит короткое событие.

I was reading when she called.

WHILE часто вводит длительный процесс.

She called while I was working.

Если два процесса происходили одновременно:

While I was reading,
she was cooking.

I was cooking
while my wife was cleaning.

Коротко:

WHEN → часто короткое событие

WHILE → часто длительный процесс.""",
            },


            {
                "order": 8,

                "title":
                    "Последовательность или фон?",

                "body":
                    """Если действия происходят одно за другим:

Past Simple.

I woke up,
got dressed,
had breakfast
and left home.

Если описывается фон:

Past Continuous.

It was raining.

People were running home.

Cars were moving slowly.

А главное событие на этом фоне:

Suddenly, the lights went out.

То есть:

фон → Past Continuous

событие → Past Simple.""",
            },


            {
                "order": 9,

                "title":
                    "Вопросы и отрицания",

                "body":
                    """Past Simple:

I didn't work.

Did you work?

What did you do yesterday?

Past Continuous:

I wasn't working.

Were you working?

What were you doing at six?

Сравни:

What did you do yesterday?

→ что ты делал вчера в целом?

What were you doing at six?

→ что происходило именно в шесть?""",
            },


            {
                "order": 10,

                "title":
                    "Stative verbs и HAVE",

                "body":
                    """Глаголы состояния обычно не используются в Continuous.

know

understand

like

want

need

believe

remember

Поэтому:

I knew the answer.

Не:

I was knowing the answer.

HAVE зависит от значения.

Владение:

I had a car.

Действие:

I was having breakfast.

She was having a shower.

При выборе времени всегда сначала смотри на смысл.""",
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
                    "I ___ television when she called.",

                "options": [
                    "watched",
                    "was watching",
                    "watch",
                    "were watching",
                ],

                "answer":
                    "was watching",

                "explanation":
                    "Просмотр был процессом, который уже происходил.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "She ___ me at eight last night.",

                "options": [
                    "called",
                    "was calling for the whole evening",
                    "calls",
                    "call",
                ],

                "answer":
                    "called",

                "explanation":
                    "Один завершённый звонок → Past Simple.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "He ___ the door and entered the room.",

                "options": [
                    "was opening",
                    "opened",
                    "opens",
                    "opening",
                ],

                "answer":
                    "opened",

                "explanation":
                    "Последовательность завершённых действий → Past Simple.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "When I was a child, we ___ outside every day.",

                "options": [
                    "were playing right then",
                    "played",
                    "play",
                    "are playing",
                ],

                "answer":
                    "played",

                "explanation":
                    "Повторяющаяся привычка в прошлом → Past Simple.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "At midnight, the children ___.",

                "options": [
                    "slept as a completed event",
                    "were sleeping",
                    "sleep",
                    "was sleeping",
                ],

                "answer":
                    "were sleeping",

                "explanation":
                    "Процесс в конкретный момент прошлого → Past Continuous.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "While I was studying, my sister ___ music.",

                "options": [
                    "was listening to",
                    "listened once",
                    "listens to",
                    "did listening to",
                ],

                "answer":
                    "was listening to",

                "explanation":
                    "Два параллельных процесса → Past Continuous.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Continuous sentence.",

                "options": [
                    "They played at six at that moment.",
                    "They were playing at six.",
                    "They did playing at six.",
                    "They were play at six.",
                ],

                "answer":
                    "They were playing at six.",

                "explanation":
                    "Past Continuous = WERE + PLAYING.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct Past Simple sentence.",

                "options": [
                    "She was went home.",
                    "She went home.",
                    "She did went home.",
                    "She was going home as one completed fact.",
                ],

                "answer":
                    "She went home.",

                "explanation":
                    "GO → WENT в Past Simple.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "At 7 p.m. yesterday, I ___ dinner.",

                "options": [
                    "was having",
                    "have",
                    "am having",
                    "did having",
                ],

                "answer":
                    "was having",

                "explanation":
                    "Нас интересует процесс именно в семь часов.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "I ___ work at 7 p.m. yesterday.",

                "options": [
                    "finished",
                    "was finishing for the whole evening",
                    "finish",
                    "am finishing",
                ],

                "answer":
                    "finished",

                "explanation":
                    "FINISHED описывает завершённое событие.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "We ___ home when we saw the accident.",

                "options": [
                    "drove as one completed trip",
                    "were driving",
                    "drive",
                    "was driving",
                ],

                "answer":
                    "were driving",

                "explanation":
                    "DRIVING — длительный процесс; SAW — короткое событие.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "She was cooking when the phone ___.",

                "options": [
                    "was ringing continuously",
                    "rang",
                    "rings",
                    "is ringing",
                ],

                "answer":
                    "rang",

                "explanation":
                    "RANG — короткое завершённое событие.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "___ I was working, she was studying.",

                "options": [
                    "While",
                    "Ago",
                    "Last",
                    "Yesterday",
                ],

                "answer":
                    "While",

                "explanation":
                    "WHILE вводит длительный процесс.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "build",

                "prompt":
                    "Собери правильное предложение.",

                "options": [
                    "I",
                    "was",
                    "sleeping",
                    "when",
                    "the",
                    "phone",
                    "rang",
                ],

                "answer":
                    "I was sleeping when the phone rang",

                "explanation":
                    "Длительный процесс + WHEN + короткое событие.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct sequence of completed actions.",

                "options": [
                    "I woke up, got dressed and left.",
                    "I was waking up, was getting dressed and was leaving.",
                    "I was woke up, got dressed and leave.",
                    "I did wake up, got dressed and was left.",
                ],

                "answer":
                    "I woke up, got dressed and left.",

                "explanation":
                    "Последовательность завершённых действий → Past Simple.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the best background description.",

                "options": [
                    "It was raining and people were running home.",
                    "It rained once and people ran once.",
                    "It was rain and people were run.",
                    "It raining and people running.",
                ],

                "answer":
                    "It was raining and people were running home.",

                "explanation":
                    "Фон истории обычно описывается Past Continuous.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "What ___ you do yesterday?",

                "options": [
                    "were",
                    "did",
                    "was",
                    "are",
                ],

                "answer":
                    "did",

                "explanation":
                    "Вопрос о вчерашних действиях в целом → Past Simple.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "What ___ you doing at six yesterday?",

                "options": [
                    "did",
                    "were",
                    "was",
                    "do",
                ],

                "answer":
                    "were",

                "explanation":
                    "Вопрос о процессе в конкретный момент → Past Continuous.",
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
                    "I did knew the answer.",
                    "I was know the answer.",
                ],

                "answer":
                    "I knew the answer.",

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
                    "I had a car. / I was having breakfast.",
                    "I was having a car. / I had breakfast at that exact moment.",
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
                    "They ___ football when it started to rain.",

                "options": [
                    "played as a completed game",
                    "were playing",
                    "play",
                    "was playing",
                ],

                "answer":
                    "were playing",

                "explanation":
                    "Игра уже была в процессе, когда начался дождь.",
            },


            {
                "order": 22,

                "prompt":
                    "The teacher ___ the room while the students were talking.",

                "options": [
                    "entered",
                    "was entering for the whole lesson",
                    "enters",
                    "did entered",
                ],

                "answer":
                    "entered",

                "explanation":
                    "ENTERED — короткое завершённое событие.",
            },


            {
                "order": 23,

                "prompt":
                    "At this time yesterday, we ___ to Astana.",

                "options": [
                    "flew as a finished trip",
                    "were flying",
                    "fly",
                    "are flying",
                ],

                "answer":
                    "were flying",

                "explanation":
                    "THIS TIME YESTERDAY указывает на процесс в конкретный момент.",
            },


            {
                "order": 24,

                "prompt":
                    "Choose the correct sequence.",

                "options": [
                    "He opened the door, walked inside and sat down.",
                    "He was opening the door, was walking inside and was sitting down.",
                    "He opened the door, was walked inside and sat.",
                    "He did opened the door, walked inside and was sat.",
                ],

                "answer":
                    "He opened the door, walked inside and sat down.",

                "explanation":
                    "Последовательность завершённых действий → Past Simple.",
            },


            {
                "order": 25,

                "prompt":
                    "I ___ when somebody knocked at the door.",

                "options": [
                    "was sleeping",
                    "slept every night",
                    "am sleeping",
                    "did sleeping",
                ],

                "answer":
                    "was sleeping",

                "explanation":
                    "SLEEPING — процесс; KNOCKED — короткое событие.",
            },


            {
                "order": 26,

                "prompt":
                    "While she ___ dinner, I was setting the table.",

                "options": [
                    "was cooking",
                    "cooked once",
                    "cooks",
                    "did cooking",
                ],

                "answer":
                    "was cooking",

                "explanation":
                    "Два действия происходили одновременно.",
            },


            {
                "order": 27,

                "prompt":
                    "Choose the correct question about a specific past moment.",

                "options": [
                    "What did you do yesterday?",
                    "What were you doing at 8 p.m.?",
                    "What do you do every evening?",
                    "What are you doing now?",
                ],

                "answer":
                    "What were you doing at 8 p.m.?",

                "explanation":
                    "Вопрос о процессе именно в 8 вечера требует Past Continuous.",
            },


            {
                "order": 28,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She was understanding everything.",
                    "She understood everything.",
                    "She did understood everything.",
                    "She was understand everything.",
                ],

                "answer":
                    "She understood everything.",

                "explanation":
                    "UNDERSTAND — stative verb и обычно используется в Past Simple.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "I finished dinner at seven. / At seven, I was having dinner.",
                    "I was finished dinner at seven. / At seven, I had having dinner.",
                    "I did finished dinner at seven. / At seven, I was have dinner.",
                    "I finishing dinner at seven. / At seven, I were having dinner.",
                ],

                "answer":
                    "I finished dinner at seven. / At seven, I was having dinner.",

                "explanation":
                    "FINISHED показывает завершение; WAS HAVING — процесс в этот момент.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct set.",

                "options": [
                    "I was walking when I saw him. / While I was walking, she was driving. / Then I went home.",
                    "I walked when I was saw him. / While I walked, she driving. / Then I was went home.",
                    "I was walk when I saw him. / While I was walking, she was drive. / Then I did went home.",
                    "I did walking when I saw him. / While I were walking, she drove now. / Then I wented home.",
                ],

                "answer":
                    "I was walking when I saw him. / While I was walking, she was driving. / Then I went home.",

                "explanation":
                    "Процесс + короткое событие, два параллельных процесса и завершённое следующее действие выбраны правильно.",
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
                "✅ Interactive A1 Lesson 29 seeded"
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
