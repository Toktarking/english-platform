from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 21: "
        "Present Continuous affirmative."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=21,
            defaults={
                "title": "Present Continuous: утверждение",
                "slug": "present-continuous-affirmative",
                "theory_text": (
                    "Present Continuous affirmative."
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
                "title": "Что такое Present Continuous",
                "body": """Present Continuous — настоящее продолженное время.

Оно используется, когда действие:

происходит прямо сейчас;

происходит в настоящий момент;

продолжается в текущий период;

является временным;

постепенно меняется или развивается.

Примеры:

I am reading now.

She is talking on the phone.

They are playing football.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Present Continuous состоит из двух частей:

1. формы глагола to be;
2. смыслового глагола с окончанием -ing.

Формула:

Подлежащее + am/is/are + глагол-ing

Примеры:

I am working.

He is working.

They are working.

Важно:

to be нельзя пропускать.""",
            },

            {
                "order": 3,
                "title": "AM, IS или ARE",
                "body": """Используйте:

I → am

you → are

he → is

she → is

it → is

we → are

they → are

Примеры:

I am reading.

You are reading.

He is reading.

She is reading.

We are reading.

They are reading.""",
            },

            {
                "order": 4,
                "title": "Один человек и множественное число",
                "body": """IS используется с:

he;
she;
it;
одним человеком;
одним предметом.

Примеры:

Marat is sleeping.

My sister is cooking.

The child is crying.

The phone is charging.

ARE используется с:

you;
we;
they;
множественным числом.

The students are writing.

My parents are travelling.

The children are sleeping.""",
            },

            {
                "order": 5,
                "title": "Как добавить -ING",
                "body": """В обычном случае просто добавляется -ing.

work → working

read → reading

play → playing

speak → speaking

listen → listening

cook → cooking

Примеры:

She is working.

They are playing.

I am reading.""",
            },

            {
                "order": 6,
                "title": "Глаголы на немую E",
                "body": """Если глагол заканчивается на немую e, она обычно убирается.

make → making

write → writing

come → coming

take → taking

drive → driving

dance → dancing

Неправильно:

writeing

makeing

Правильно:

writing

making""",
            },

            {
                "order": 7,
                "title": "Удвоение последней согласной",
                "body": """У коротких глаголов типа:

согласная + гласная + согласная

последняя согласная часто удваивается.

Примеры:

sit → sitting

run → running

swim → swimming

stop → stopping

get → getting

put → putting

Неправильно:

runing

swiming

Правильно:

running

swimming""",
            },

            {
                "order": 8,
                "title": "Глаголы на IE и Y",
                "body": """Если глагол заканчивается на -ie:

ie → y

lie → lying

die → dying

tie → tying

Если глагол заканчивается на y, буква y обычно сохраняется:

study → studying

play → playing

carry → carrying

enjoy → enjoying

Не:

studing

Правильно:

studying""",
            },

            {
                "order": 9,
                "title": "Действие прямо сейчас",
                "body": """Главное значение Present Continuous — действие в момент речи.

Примеры:

I am reading now.

She is talking to her teacher.

They are having lunch.

The baby is sleeping.

Также:

Look! It is snowing.

Listen! Someone is knocking.

Be quiet. The child is sleeping.

Wait. I am coming.""",
            },

            {
                "order": 10,
                "title": "Слова-маркеры",
                "body": """С Present Continuous часто используются:

now;

right now;

at the moment;

currently;

today;

this week;

these days;

look;

listen.

Примеры:

I am working now.

She is studying at the moment.

They are staying with friends this week.

Look! The dog is running away.""",
            },

            {
                "order": 11,
                "title": "Временная ситуация",
                "body": """Present Continuous может описывать временную ситуацию, даже если действие происходит не именно в эту секунду.

Примеры:

I am reading an interesting book.

She is studying English this year.

We are working on a new project.

He is living with his parents this month.

They are preparing for an exam.

Сравните:

I live in Karaganda.
— постоянная ситуация.

I am living in Almaty this month.
— временная ситуация.""",
            },

            {
                "order": 12,
                "title": "Изменения и развитие",
                "body": """Present Continuous используется для процессов, которые постепенно меняются.

Примеры:

The weather is getting colder.

Prices are rising.

The child is growing quickly.

My English is improving.

Technology is developing rapidly.

Частые глаголы:

get;

grow;

change;

increase;

decrease;

improve;

rise;

fall.""",
            },

            {
                "order": 13,
                "title": "Present Simple или Present Continuous",
                "body": """Present Simple используется для:

привычек;

регулярных действий;

фактов;

постоянных ситуаций.

I work every day.

Present Continuous используется для:

действия сейчас;

временной ситуации;

текущего процесса.

I am working now.

Сравните:

She reads every evening.

She is reading now.

They play football on Sundays.

They are playing football now.""",
            },

            {
                "order": 14,
                "title": "TO BE обязателен и глаголы состояния",
                "body": """Нельзя использовать только глагол с -ing.

Неправильно:

I reading.

She working.

They playing.

Правильно:

I am reading.

She is working.

They are playing.

Некоторые глаголы состояния обычно не используются в Continuous:

know;

understand;

like;

love;

want;

need;

believe;

remember;

own.

Правильно:

I know the answer.

He likes coffee.

We need more time.

Обычно неправильно:

I am knowing the answer.

He is liking coffee.""",
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
                "prompt": "I ___ waiting for the bus.",
                "options": ["is", "am", "are", "do"],
                "answer": "am",
                "explanation": "С I используется am.",
            },

            {
                "order": 2,
                "prompt": "My brother ___ sleeping.",
                "options": ["am", "are", "is", "does"],
                "answer": "is",
                "explanation": "My brother = he, поэтому is.",
            },

            {
                "order": 3,
                "prompt": "The children ___ playing outside.",
                "options": ["is", "am", "are", "be"],
                "answer": "are",
                "explanation": "Children = they, поэтому are.",
            },

            {
                "order": 4,
                "prompt": "She is ___ a book.",
                "options": ["read", "reads", "reading", "readed"],
                "answer": "reading",
                "explanation": "Present Continuous: is + verb-ing.",
            },

            {
                "order": 5,
                "prompt": "He is ___ dinner.",
                "options": ["makeing", "making", "makes", "make"],
                "answer": "making",
                "explanation": "Make теряет немую e: make → making.",
            },

            {
                "order": 6,
                "prompt": "They are ___ in the park.",
                "options": ["runing", "running", "runs", "run"],
                "answer": "running",
                "explanation": "Run → running с удвоением n.",
            },

            {
                "order": 7,
                "prompt": "We are ___ for an exam.",
                "options": ["study", "studies", "studying", "studied"],
                "answer": "studying",
                "explanation": "Study → studying; y сохраняется.",
            },

            {
                "order": 8,
                "prompt": "The baby is ___.",
                "options": ["cry", "cries", "crying", "cryying"],
                "answer": "crying",
                "explanation": "Cry → crying.",
            },

            {
                "order": 9,
                "prompt": "Look! The cat ___ climbing the tree.",
                "options": ["am", "is", "are", "does"],
                "answer": "is",
                "explanation": "Cat = it, поэтому is.",
            },

            {
                "order": 10,
                "prompt": "Listen! Someone ___ knocking at the door.",
                "options": ["is", "are", "am", "do"],
                "answer": "is",
                "explanation": "Someone рассматривается как единственное число.",
            },

            {
                "order": 11,
                "prompt": "My parents ___ travelling this week.",
                "options": ["is", "are", "am", "be"],
                "answer": "are",
                "explanation": "Parents = they, поэтому are.",
            },

            {
                "order": 12,
                "prompt": "I ___ working at home today.",
                "options": ["is", "are", "am", "do"],
                "answer": "am",
                "explanation": "I → am.",
            },

            {
                "order": 13,
                "prompt": "The weather is ___ colder.",
                "options": ["get", "gets", "getting", "geting"],
                "answer": "getting",
                "explanation": "Get → getting.",
            },

            {
                "order": 14,
                "prompt": "My English ___ improving.",
                "options": ["am", "is", "are", "does"],
                "answer": "is",
                "explanation": "My English = it, поэтому is.",
            },

            {
                "order": 15,
                "prompt": "She ___ the answer.",
                "options": [
                    "is knowing",
                    "knows",
                    "knowing",
                    "is know",
                ],
                "answer": "knows",
                "explanation": "Know — глагол состояния и обычно не используется в Continuous.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She working now.",
                    "She is working now.",
                    "She is work now.",
                    "She works now at the moment.",
                ],
                "answer": "She is working now.",
                "explanation": "Present Continuous требует is + working.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct form of WRITE.",
                "options": [
                    "writeing",
                    "writing",
                    "writting",
                    "writesing",
                ],
                "answer": "writing",
                "explanation": "Немая e убирается: write → writing.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct form of SWIM.",
                "options": [
                    "swiming",
                    "swimming",
                    "swimingg",
                    "swims",
                ],
                "answer": "swimming",
                "explanation": "Последняя согласная удваивается: swim → swimming.",
            },

            {
                "order": 19,
                "prompt": "Choose the correct form of LIE.",
                "options": ["lieing", "lying", "liing", "lies"],
                "answer": "lying",
                "explanation": "Глаголы на -ie: ie → y + ing.",
            },

            {
                "order": 20,
                "prompt": "Which sentence describes a temporary situation?",
                "options": [
                    "I live in Karaganda.",
                    "I am living in Almaty this month.",
                    "Water boils at 100°C.",
                    "I work every day.",
                ],
                "answer": "I am living in Almaty this month.",
                "explanation": "This month показывает временную ситуацию.",
            },

            {
                "order": 21,
                "prompt": "Which sentence describes an action happening now?",
                "options": [
                    "She reads every evening.",
                    "She is reading now.",
                    "She usually reads books.",
                    "She reads on Sundays.",
                ],
                "answer": "She is reading now.",
                "explanation": "Now — типичный маркер Present Continuous.",
            },

            {
                "order": 22,
                "prompt": "They ___ lunch at the moment.",
                "options": [
                    "have",
                    "are having",
                    "has",
                    "is having",
                ],
                "answer": "are having",
                "explanation": "Have здесь означает действие: have lunch → are having lunch.",
            },

            {
                "order": 23,
                "prompt": "Choose the correct sentence about possession.",
                "options": [
                    "I am having a car.",
                    "I have a car.",
                    "I having a car.",
                    "I am have a car.",
                ],
                "answer": "I have a car.",
                "explanation": "Have в значении владения обычно не используется в Continuous.",
            },

            {
                "order": 24,
                "prompt": "Which sentence shows a gradual change?",
                "options": [
                    "The weather gets cold every winter.",
                    "The weather is getting colder.",
                    "The weather cold now.",
                    "The weather is get colder.",
                ],
                "answer": "The weather is getting colder.",
                "explanation": "Present Continuous используется для постепенных изменений.",
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
                "✅ A1 Lesson 21 seeded: "
                "Present Continuous — утверждение"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
