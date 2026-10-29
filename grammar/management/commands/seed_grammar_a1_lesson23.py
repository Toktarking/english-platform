from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 23: "
        "Present Simple vs Present Continuous."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=23,
            defaults={
                "title": (
                    "Present Simple и "
                    "Present Continuous"
                ),
                "slug": "present-simple-vs-continuous",
                "theory_text": (
                    "Present Simple vs "
                    "Present Continuous."
                ),
                "estimated_minutes": 35,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Главное различие",
                "body": """Present Simple и Present Continuous относятся к настоящему времени, но используются по-разному.

Present Simple:

I work every day.

Это привычка или регулярное действие.

Present Continuous:

I am working now.

Это действие прямо сейчас.

Главный вопрос:

это обычно происходит или происходит сейчас?""",
            },

            {
                "order": 2,
                "title": "Когда нужен Present Simple",
                "body": """Present Simple используется для:

привычек;

регулярных действий;

постоянных ситуаций;

фактов;

расписаний.

Примеры:

I go to work every day.

She lives in Astana.

They play football on Sundays.

Water boils at 100°C.

The lesson starts at nine.""",
            },

            {
                "order": 3,
                "title": "Когда нужен Present Continuous",
                "body": """Present Continuous используется для:

действия прямо сейчас;

временной ситуации;

процесса текущего периода;

изменения и развития;

заранее договорённого будущего действия.

Примеры:

I am working now.

She is staying with her sister this week.

They are studying for an exam.

Prices are rising.

We are meeting the teacher tomorrow.""",
            },

            {
                "order": 4,
                "title": "Сравнение форм",
                "body": """Present Simple:

I work.

She works.

They play.

He reads.

Present Continuous:

I am working.

She is working.

They are playing.

He is reading.

Запомните:

Present Simple → обычный глагол.

Present Continuous → am/is/are + verb-ing.""",
            },

            {
                "order": 5,
                "title": "Регулярно или прямо сейчас",
                "body": """Сравните:

I drink coffee every morning.

I am drinking coffee now.

She walks to work every day.

She is walking to work now.

He reads every evening.

He is reading now.

Every day / usually → чаще Present Simple.

Now / at the moment → чаще Present Continuous.""",
            },

            {
                "order": 6,
                "title": "Слова-маркеры",
                "body": """Частые маркеры Present Simple:

always;

usually;

often;

sometimes;

never;

every day;

on Mondays;

once a month.

Частые маркеры Present Continuous:

now;

right now;

at the moment;

today;

this week;

these days;

look;

listen.

Но смысл предложения важнее одного слова-маркера.""",
            },

            {
                "order": 7,
                "title": "Постоянное или временное",
                "body": """Present Simple описывает постоянную ситуацию.

I live in Karaganda.

She works at a university.

Present Continuous описывает временную ситуацию.

I am living in Almaty this month.

She is working at home this week.

Сравните:

He works in a bank.

He is working in another office this week.""",
            },

            {
                "order": 8,
                "title": "Факт или изменение",
                "body": """Для фактов используется Present Simple.

Water freezes at 0°C.

The Earth moves around the Sun.

Children need care.

Для постепенных изменений используется Present Continuous.

The weather is getting colder.

Prices are increasing.

My English is improving.

The child is growing quickly.""",
            },

            {
                "order": 9,
                "title": "Расписание или личный план",
                "body": """Present Simple используется для расписаний.

The lesson starts at nine.

The train leaves at six.

The shop opens at ten.

Present Continuous может использоваться для личной договорённости или согласованного плана.

I am meeting the teacher tomorrow.

We are having dinner with friends tonight.

She is flying to Astana on Friday.""",
            },

            {
                "order": 10,
                "title": "Вопросы и отрицания",
                "body": """Present Simple использует do/does.

Do you work here?

Does she live in Astana?

I don't work on Sundays.

She doesn't drive.

Present Continuous использует am/is/are.

Are you working now?

Is she sleeping?

I'm not working now.

She isn't driving.

Не смешивайте две системы.""",
            },

            {
                "order": 11,
                "title": "Глаголы состояния",
                "body": """Некоторые глаголы обычно описывают состояние, а не действие.

Например:

know;

understand;

like;

love;

want;

need;

believe;

remember;

prefer;

own;

belong.

Обычно используется Present Simple:

I know the answer.

He likes coffee.

They need help.

Обычно неправильно:

I am knowing the answer.

He is liking coffee.""",
            },

            {
                "order": 12,
                "title": "THINK, HAVE, SEE, LOOK",
                "body": """Некоторые глаголы могут менять значение.

THINK как мнение:

I think he is right.

THINK как процесс размышления:

I am thinking about the problem.

HAVE как владение:

I have a car.

HAVE как действие:

I am having breakfast.

SEE как видеть:

I see a bird.

SEE как встречаться:

I am seeing the doctor tomorrow.

LOOK как внешний вид:

You look tired.

LOOK как действие:

He is looking at the picture.""",
            },

            {
                "order": 13,
                "title": "ALWAYS в двух временах",
                "body": """Present Simple + always обычно описывает нейтральную привычку.

He always comes early.

She always helps me.

Present Continuous + always может выражать раздражение.

He is always losing his keys.

She is always interrupting me.

They are always coming late.

То есть форма времени может менять оттенок смысла.""",
            },

            {
                "order": 14,
                "title": "Как выбрать время",
                "body": """Шаг 1.

Это привычка, факт, расписание или постоянная ситуация?

→ Present Simple.

Шаг 2.

Это происходит сейчас, временно или меняется?

→ Present Continuous.

Шаг 3.

Проверьте маркеры:

every day → Simple

usually → Simple

now → Continuous

at the moment → Continuous

Но всегда сначала смотрите на смысл.

Сравните:

I work every day.

I am working now.""",
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
                "prompt": "I usually ___ at seven.",
                "options": [
                    "am getting up",
                    "get up",
                    "gets up",
                    "getting up",
                ],
                "answer": "get up",
                "explanation": "Usually показывает регулярное действие → Present Simple.",
            },

            {
                "order": 2,
                "prompt": "I ___ up now.",
                "options": [
                    "get",
                    "gets",
                    "am getting",
                    "getting",
                ],
                "answer": "am getting",
                "explanation": "Now → Present Continuous.",
            },

            {
                "order": 3,
                "prompt": "My brother ___ in Astana.",
                "options": [
                    "is living permanently",
                    "lives",
                    "live",
                    "living",
                ],
                "answer": "lives",
                "explanation": "Постоянное место жительства → Present Simple.",
            },

            {
                "order": 4,
                "prompt": "My brother ___ with us this month.",
                "options": [
                    "lives every month",
                    "is living",
                    "live",
                    "living",
                ],
                "answer": "is living",
                "explanation": "This month показывает временную ситуацию.",
            },

            {
                "order": 5,
                "prompt": "She usually ___ tea.",
                "options": [
                    "drinks",
                    "is drinking",
                    "drink",
                    "drinking",
                ],
                "answer": "drinks",
                "explanation": "Usually → Present Simple; she → drinks.",
            },

            {
                "order": 6,
                "prompt": "She ___ tea at the moment.",
                "options": [
                    "drinks",
                    "drink",
                    "is drinking",
                    "drinking",
                ],
                "answer": "is drinking",
                "explanation": "At the moment → Present Continuous.",
            },

            {
                "order": 7,
                "prompt": "We ___ English twice a week.",
                "options": [
                    "are studying",
                    "study",
                    "studies",
                    "studying",
                ],
                "answer": "study",
                "explanation": "Twice a week показывает регулярность.",
            },

            {
                "order": 8,
                "prompt": "We ___ for an exam this week.",
                "options": [
                    "study every week",
                    "are studying",
                    "studies",
                    "studying",
                ],
                "answer": "are studying",
                "explanation": "This week показывает текущий временный процесс.",
            },

            {
                "order": 9,
                "prompt": "The train ___ at six.",
                "options": [
                    "is leaving every day",
                    "leaves",
                    "leave",
                    "leaving",
                ],
                "answer": "leaves",
                "explanation": "Расписание → Present Simple.",
            },

            {
                "order": 10,
                "prompt": "We ___ our teacher tomorrow.",
                "options": [
                    "meet every day",
                    "are meeting",
                    "meets",
                    "meeting",
                ],
                "answer": "are meeting",
                "explanation": "Заранее согласованная встреча → Present Continuous.",
            },

            {
                "order": 11,
                "prompt": "He ___ this film.",
                "options": [
                    "is liking",
                    "likes",
                    "like",
                    "liking",
                ],
                "answer": "likes",
                "explanation": "Like — глагол состояния и обычно используется в Present Simple.",
            },

            {
                "order": 12,
                "prompt": "I ___ this is a good idea.",
                "options": [
                    "think",
                    "am thinking",
                    "thinking",
                    "thinks",
                ],
                "answer": "think",
                "explanation": "Think здесь означает мнение → Present Simple.",
            },

            {
                "order": 13,
                "prompt": "I ___ about the problem now.",
                "options": [
                    "think every day",
                    "am thinking",
                    "thinks",
                    "thinking",
                ],
                "answer": "am thinking",
                "explanation": "Think означает процесс размышления прямо сейчас.",
            },

            {
                "order": 14,
                "prompt": "They ___ lunch now.",
                "options": [
                    "have",
                    "are having",
                    "has",
                    "having",
                ],
                "answer": "are having",
                "explanation": "Have lunch — действие; now → Present Continuous.",
            },

            {
                "order": 15,
                "prompt": "She ___ a new car.",
                "options": [
                    "is having",
                    "has",
                    "have",
                    "having",
                ],
                "answer": "has",
                "explanation": "Have означает владение → Present Simple.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence for an action happening now.",
                "options": [
                    "I work now.",
                    "I am working now.",
                    "I working now.",
                    "I am work now.",
                ],
                "answer": "I am working now.",
                "explanation": "Действие сейчас требует Present Continuous.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence for a habit.",
                "options": [
                    "I am going to work every day.",
                    "I go to work every day.",
                    "I going to work every day.",
                    "I am go to work every day.",
                ],
                "answer": "I go to work every day.",
                "explanation": "Every day показывает привычку → Present Simple.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct question.",
                "options": [
                    "Do you working now?",
                    "Are you working now?",
                    "Are you work now?",
                    "Does you work now?",
                ],
                "answer": "Are you working now?",
                "explanation": "В Present Continuous используется are + subject + verb-ing.",
            },

            {
                "order": 19,
                "prompt": "Choose the correct question about a regular job.",
                "options": [
                    "Are you work here?",
                    "Do you work here?",
                    "Are you working here every day now?",
                    "Do you working here?",
                ],
                "answer": "Do you work here?",
                "explanation": "Вопрос о постоянной работе → Present Simple.",
            },

            {
                "order": 20,
                "prompt": "Which sentence describes a gradual change?",
                "options": [
                    "Prices increase every January.",
                    "Prices are increasing.",
                    "Prices increases now.",
                    "Prices is increasing.",
                ],
                "answer": "Prices are increasing.",
                "explanation": "Постепенное изменение → Present Continuous.",
            },

            {
                "order": 21,
                "prompt": "Which sentence expresses a fact?",
                "options": [
                    "Water is boiling at 100°C every time.",
                    "Water boils at 100°C.",
                    "Water boiling at 100°C.",
                    "Water is boil at 100°C.",
                ],
                "answer": "Water boils at 100°C.",
                "explanation": "Общий факт → Present Simple.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I am knowing the answer.",
                    "I know the answer.",
                    "I knowing the answer.",
                    "I am know the answer.",
                ],
                "answer": "I know the answer.",
                "explanation": "Know — глагол состояния.",
            },

            {
                "order": 23,
                "prompt": "Which sentence shows a temporary situation?",
                "options": [
                    "She works at a university.",
                    "She is working at home this week.",
                    "She work at home every week.",
                    "She is work at a university.",
                ],
                "answer": "She is working at home this week.",
                "explanation": "This week + временная ситуация → Present Continuous.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct pair.",
                "options": [
                    "She reads every evening. / She is reading now.",
                    "She is reading every evening. / She reads now.",
                    "She reading every evening. / She is reads now.",
                    "She reads every evening. / She reading now.",
                ],
                "answer": "She reads every evening. / She is reading now.",
                "explanation": "Регулярное действие → Simple; действие сейчас → Continuous.",
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
                "✅ A1 Lesson 23 seeded: "
                "Present Simple vs Present Continuous"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
