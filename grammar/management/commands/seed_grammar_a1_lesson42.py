from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 42: "
        "Infinitive and Gerund."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=42,
            defaults={
                "title": "Инфинитив и герундий",
                "slug": "infinitive-and-gerund",
                "theory_text": "Infinitive and Gerund.",
                "estimated_minutes": 50,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Инфинитив и герундий",
                "body": """Инфинитив обычно имеет форму:

to + verb

Примеры:

to work

to study

to read

to travel

I want to study.

She decided to leave.

Герундий имеет форму:

verb-ing

Примеры:

working

studying

reading

travelling

I enjoy reading.

Swimming is good for your health.""",
            },

            {
                "order": 2,
                "title": "Почему нужно знать разницу",
                "body": """После одних глаголов используется инфинитив:

want to go

decide to stay

hope to win

После других используется герундий:

enjoy reading

avoid talking

finish working

Некоторые глаголы допускают обе формы.

Иногда значение при этом меняется.

Поэтому часто нужно запоминать не отдельный глагол, а конструкцию целиком.""",
            },

            {
                "order": 3,
                "title": "Глаголы + TO DO",
                "body": """Частые глаголы с инфинитивом:

want to do

would like to do

decide to do

plan to do

hope to do

promise to do

agree to do

refuse to do

learn to do

manage to do

fail to do

expect to do

need to do

Примеры:

I want to learn English.

She decided to leave.

We plan to travel.

He promised to help.""",
            },

            {
                "order": 4,
                "title": "Глаголы + DOING",
                "body": """Частые глаголы с герундием:

enjoy doing

finish doing

avoid doing

mind doing

suggest doing

consider doing

keep doing

practise doing

miss doing

stop doing

Примеры:

I enjoy reading.

She finished cleaning.

He avoids talking about money.

I suggest taking a taxi.

Keep working.""",
            },

            {
                "order": 5,
                "title": "После предлога — герундий",
                "body": """После предлога обычно используется verb-ing.

Примеры:

Thank you for helping me.

She left without saying goodbye.

He is interested in learning English.

Before leaving, call me.

After finishing the work, we went home.

Важно:

иногда TO является предлогом.

Например:

look forward to

be used to

get used to

После такого TO также используется -ing:

I look forward to seeing you.""",
            },

            {
                "order": 6,
                "title": "Герундий как подлежащее",
                "body": """Герундий может называть действие как процесс или занятие.

Он может стоять в начале предложения.

Примеры:

Reading is useful.

Swimming is good exercise.

Learning English takes time.

Smoking is dangerous.

Здесь действие рассматривается как понятие.""",
            },

            {
                "order": 7,
                "title": "Инфинитив для цели",
                "body": """Инфинитив часто показывает цель действия.

Пример:

I went to the shop to buy bread.

То есть:

я пошёл в магазин, чтобы купить хлеб.

Другие примеры:

She called me to ask a question.

He went to the bank to withdraw money.

We study English to communicate with foreigners.

Не:

I went to the shop for buy bread.""",
            },

            {
                "order": 8,
                "title": "TO DO и FOR DOING",
                "body": """Инфинитив часто показывает цель конкретного действия.

I went to the shop to buy bread.

FOR + gerund может показывать назначение предмета.

This machine is for cutting paper.

This brush is for cleaning shoes.

Сравните:

I went to the shop to buy bread.
— цель действия.

This knife is for cutting bread.
— назначение предмета.""",
            },

            {
                "order": 9,
                "title": "LIKE, LOVE, HATE, PREFER",
                "body": """После некоторых глаголов возможны обе формы.

LIKE:

I like reading.

I like to check my email in the morning.

LOVE:

I love reading.

I love to read before bed.

HATE:

She hates waiting.

She hates to be late.

PREFER:

I prefer walking.

I prefer to walk to work.

Разница между формами иногда небольшая.""",
            },

            {
                "order": 10,
                "title": "STOP: форма меняет значение",
                "body": """STOP DOING:

прекратить действие.

He stopped smoking.

Он перестал курить.

STOP TO DO:

остановиться, чтобы выполнить другое действие.

He stopped to smoke.

Он остановился, чтобы покурить.

Сравните:

She stopped talking.
— перестала говорить.

She stopped to talk to her friend.
— остановилась, чтобы поговорить.""",
            },

            {
                "order": 11,
                "title": "REMEMBER, FORGET и TRY",
                "body": """REMEMBER DOING:

помнить совершённое действие.

I remember locking the door.

REMEMBER TO DO:

не забыть сделать действие.

Remember to lock the door.

FORGET TO DO:

забыть выполнить действие.

I forgot to call her.

TRY TO DO:

пытаться сделать.

I tried to open the door.

TRY DOING:

попробовать способ.

Try restarting the computer.""",
            },

            {
                "order": 12,
                "title": "Инфинитив без TO",
                "body": """После модальных глаголов используется глагол без TO:

can swim

must go

should rest

may come

После LET:

let + object + verb

Let me help you.

После MAKE в активном залоге:

make + object + verb

She made me apologise.

После HELP возможны обе формы:

She helped me carry the bags.

She helped me to carry the bags.""",
            },

            {
                "order": 13,
                "title": "Прилагательное + инфинитив",
                "body": """После многих прилагательных используется инфинитив.

Примеры:

happy to help

ready to start

difficult to understand

easy to use

important to remember

Также:

too + adjective + to do

The bag is too heavy to carry.

adjective + enough + to do

He is old enough to drive.

enough + noun + to do

We have enough time to finish.""",
            },

            {
                "order": 14,
                "title": "Объект + инфинитив и алгоритм выбора",
                "body": """Частые модели:

want someone to do

I want you to help me.

ask someone to do

I asked him to come.

tell someone to do

She told me to sit down.

advise someone to do

The doctor advised me to rest.

Как выбирать форму:

после want/decide/hope → to do;

после enjoy/finish/avoid → doing;

после предлога → doing;

для цели → to do;

после модального глагола → verb без to;

со stop, remember, forget, try значение может зависеть от формы.""",
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
                "prompt": "I hope ___ you soon.",
                "options": [
                    "seeing",
                    "to see",
                    "see to",
                    "saw",
                ],
                "answer": "to see",
                "explanation": "После hope используется to + verb.",
            },

            {
                "order": 2,
                "prompt": "She avoids ___ late.",
                "options": [
                    "arrive",
                    "to arrive",
                    "arriving",
                    "arrived",
                ],
                "answer": "arriving",
                "explanation": "После avoid используется gerund.",
            },

            {
                "order": 3,
                "prompt": "We plan ___ next year.",
                "options": [
                    "travel",
                    "travelling only",
                    "to travel",
                    "travelled",
                ],
                "answer": "to travel",
                "explanation": "Plan to + verb.",
            },

            {
                "order": 4,
                "prompt": "He suggested ___ a taxi.",
                "options": [
                    "take",
                    "to take",
                    "taking",
                    "took",
                ],
                "answer": "taking",
                "explanation": "Suggest + verb-ing.",
            },

            {
                "order": 5,
                "prompt": "Do you mind ___ the window?",
                "options": [
                    "open",
                    "to open",
                    "opening",
                    "opened",
                ],
                "answer": "opening",
                "explanation": "Mind + verb-ing.",
            },

            {
                "order": 6,
                "prompt": "She promised ___ me.",
                "options": [
                    "help",
                    "helping",
                    "to help",
                    "helped",
                ],
                "answer": "to help",
                "explanation": "Promise to + verb.",
            },

            {
                "order": 7,
                "prompt": "They kept ___.",
                "options": [
                    "talk",
                    "talking",
                    "to talk only",
                    "talked",
                ],
                "answer": "talking",
                "explanation": "Keep + verb-ing.",
            },

            {
                "order": 8,
                "prompt": "He refused ___ the document.",
                "options": [
                    "sign",
                    "signing",
                    "to sign",
                    "signed",
                ],
                "answer": "to sign",
                "explanation": "Refuse to + verb.",
            },

            {
                "order": 9,
                "prompt": "I am interested in ___ English.",
                "options": [
                    "learn",
                    "to learn",
                    "learning",
                    "learned",
                ],
                "answer": "learning",
                "explanation": "После предлога in используется gerund.",
            },

            {
                "order": 10,
                "prompt": "She left without ___ goodbye.",
                "options": [
                    "say",
                    "to say",
                    "saying",
                    "said",
                ],
                "answer": "saying",
                "explanation": "После without используется verb-ing.",
            },

            {
                "order": 11,
                "prompt": "I called him ___ about the meeting.",
                "options": [
                    "asking",
                    "to ask",
                    "ask for",
                    "asked",
                ],
                "answer": "to ask",
                "explanation": "Инфинитив показывает цель звонка.",
            },

            {
                "order": 12,
                "prompt": "You can ___ here.",
                "options": [
                    "to sit",
                    "sitting",
                    "sit",
                    "sat",
                ],
                "answer": "sit",
                "explanation": "После modal can используется verb без to.",
            },

            {
                "order": 13,
                "prompt": "The teacher made us ___ the task again.",
                "options": [
                    "to do",
                    "doing",
                    "do",
                    "did",
                ],
                "answer": "do",
                "explanation": "Make + object + bare infinitive.",
            },

            {
                "order": 14,
                "prompt": "I want you ___ me.",
                "options": [
                    "help",
                    "helping",
                    "to help",
                    "helped",
                ],
                "answer": "to help",
                "explanation": "Want + object + to + verb.",
            },

            {
                "order": 15,
                "prompt": "He is too tired ___.",
                "options": [
                    "working",
                    "to work",
                    "work to",
                    "worked",
                ],
                "answer": "to work",
                "explanation": "Too + adjective + to + verb.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I enjoy to read.",
                    "I enjoy reading.",
                    "I enjoy read.",
                    "I enjoying reading.",
                ],
                "answer": "I enjoy reading.",
                "explanation": "Enjoy + gerund.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She decided going home.",
                    "She decided to go home.",
                    "She decided go home.",
                    "She decided to going home.",
                ],
                "answer": "She decided to go home.",
                "explanation": "Decide to + verb.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "After to finish the work, we left.",
                    "After finishing the work, we left.",
                    "After finish the work, we left.",
                    "After finished the work, we left.",
                ],
                "answer": "After finishing the work, we left.",
                "explanation": "После предлога after используется gerund.",
            },

            {
                "order": 19,
                "prompt": (
                    "He stopped smoking. What does it mean?"
                ),
                "options": [
                    "He stopped in order to smoke.",
                    "He stopped the habit of smoking.",
                    "He plans to smoke.",
                    "He forgot to smoke.",
                ],
                "answer": "He stopped the habit of smoking.",
                "explanation": "Stop doing = прекратить действие.",
            },

            {
                "order": 20,
                "prompt": (
                    "He stopped to smoke. What does it mean?"
                ),
                "options": [
                    "He stopped smoking forever.",
                    "He stopped another action in order to smoke.",
                    "He forgot smoking.",
                    "He avoided smoking.",
                ],
                "answer": (
                    "He stopped another action in order to smoke."
                ),
                "explanation": (
                    "Stop to do = остановиться, чтобы сделать другое действие."
                ),
            },

            {
                "order": 21,
                "prompt": "Remember ___ the door before you leave.",
                "options": [
                    "locking yesterday",
                    "to lock",
                    "lock to",
                    "locked",
                ],
                "answer": "to lock",
                "explanation": (
                    "Remember to do = не забыть выполнить действие."
                ),
            },

            {
                "order": 22,
                "prompt": (
                    "The computer is slow. Try ___ it."
                ),
                "options": [
                    "restart",
                    "to restarted",
                    "restarting",
                    "restarted",
                ],
                "answer": "restarting",
                "explanation": (
                    "Try doing = попробовать способ решения проблемы."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct pair.",
                "options": [
                    (
                        "I went to the shop to buy bread. / "
                        "This knife is for cutting bread."
                    ),
                    (
                        "I went to the shop for buy bread. / "
                        "This knife is to cutting bread."
                    ),
                    (
                        "I went to shop buying bread purpose. / "
                        "This knife is for cut bread."
                    ),
                    (
                        "I went to the shop to buying bread. / "
                        "This knife is for to cut bread."
                    ),
                ],
                "answer": (
                    "I went to the shop to buy bread. / "
                    "This knife is for cutting bread."
                ),
                "explanation": (
                    "To do = цель действия; for doing = назначение."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "I want to learn. / "
                        "I enjoy learning. / "
                        "Thank you for helping. / "
                        "You should rest."
                    ),
                    (
                        "I want learning. / "
                        "I enjoy to learn. / "
                        "Thank you for to help. / "
                        "You should to rest."
                    ),
                    (
                        "I want learn to. / "
                        "I enjoy learn. / "
                        "Thank you helping for. / "
                        "You should resting."
                    ),
                    (
                        "I wanting to learn. / "
                        "I enjoy learned. / "
                        "Thank you to helping. / "
                        "You shoulded rest."
                    ),
                ],
                "answer": (
                    "I want to learn. / "
                    "I enjoy learning. / "
                    "Thank you for helping. / "
                    "You should rest."
                ),
                "explanation": (
                    "Want → to do; enjoy → doing; "
                    "after preposition → doing; modal → bare infinitive."
                ),
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
                "✅ A1 Lesson 42 seeded: Infinitive and Gerund"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
