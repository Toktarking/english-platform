from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 42: Infinitive and Gerund."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=42,
            defaults={
                "title": "Инфинитив и герундий",
                "slug": "infinitive-and-gerund",
                "theory_text": "Infinitive and Gerund.",
                "estimated_minutes": 20,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )


        # =================================================
        # 10 MICRO RULES
        # =================================================

        sections = [

            {
                "order": 1,
                "title": "TO DO и DOING",
                "body": """Есть две частые формы:

to + verb

to work
to study
to travel

и:

verb-ing

working
studying
travelling

Примеры:

I want to study.

I enjoy studying.""",
            },

            {
                "order": 2,
                "title": "Глаголы + TO DO",
                "body": """После некоторых глаголов
используем TO + verb.

want to

decide to

plan to

hope to

promise to

need to

Примеры:

I want to learn English.

She decided to leave.

We plan to travel.""",
            },

            {
                "order": 3,
                "title": "Глаголы + DOING",
                "body": """После других глаголов
используем verb-ing.

enjoy doing

finish doing

avoid doing

mind doing

suggest doing

keep doing

Примеры:

I enjoy reading.

She finished working.

He avoids driving at night.""",
            },

            {
                "order": 4,
                "title": "После предлога → DOING",
                "body": """После предлога обычно
используем verb-ing.

for helping

without saying

after finishing

before leaving

interested in learning

Пример:

Thank you for helping me.

She left without saying goodbye.""",
            },

            {
                "order": 5,
                "title": "Инфинитив показывает цель",
                "body": """TO + verb часто показывает:

зачем?

I went to the shop
to buy bread.

She called me
to ask a question.

We study English
to communicate.

То есть:

действие + цель → TO DO.""",
            },

            {
                "order": 6,
                "title": "После модальных глаголов — без TO",
                "body": """После CAN, MUST, SHOULD,
MAY, MIGHT используется
обычная форма глагола.

You can swim.

You must go.

You should rest.

Не:

can to swim

must to go.""",
            },

            {
                "order": 7,
                "title": "STOP DOING и STOP TO DO",
                "body": """STOP DOING:

перестать делать действие.

He stopped smoking.

→ он бросил курить.

STOP TO DO:

остановиться,
чтобы сделать другое действие.

He stopped to smoke.

→ он остановился,
чтобы покурить.""",
            },

            {
                "order": 8,
                "title": "REMEMBER и FORGET",
                "body": """REMEMBER TO DO:

не забыть сделать.

Remember to call her.

REMEMBER DOING:

помнить уже сделанное.

I remember calling her.

FORGET TO DO:

забыть сделать.

I forgot to call her.""",
            },

            {
                "order": 9,
                "title": "TRY TO DO и TRY DOING",
                "body": """TRY TO DO:

пытаться сделать что-то.

I tried to open the door.

TRY DOING:

попробовать способ.

The computer is slow.

Try restarting it.

То есть:

TRY TO DO → попытка

TRY DOING → эксперимент / способ.""",
            },

            {
                "order": 10,
                "title": "Как быстро выбрать форму",
                "body": """want / decide / plan / hope

→ TO DO

enjoy / finish / avoid / suggest

→ DOING

после предлога

→ DOING

цель действия

→ TO DO

после modal

→ verb без TO

stop / remember / try

→ форма может менять значение.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = GrammarLessonSection.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "title": data["title"],
                    "body": data["body"],
                },
            )

            section_objects[data["order"]] = section


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            # SECTION 1
            {
                "order": 1,
                "section": 1,
                "type": "choice",
                "prompt": "I want ___ English.",
                "options": [
                    "to learn",
                    "learning",
                    "learned",
                    "to learning",
                ],
                "answer": "to learn",
                "explanation": "WANT → TO + verb.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt": "I enjoy ___ English.",
                "options": [
                    "learning",
                    "to learn",
                    "learn",
                    "learned",
                ],
                "answer": "learning",
                "explanation": "ENJOY → verb-ing.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt": "She decided ___ home.",
                "options": [
                    "to go",
                    "going",
                    "go",
                    "went",
                ],
                "answer": "to go",
                "explanation": "DECIDE → TO DO.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt": "We plan ___ next year.",
                "options": [
                    "to travel",
                    "travelling",
                    "travelled",
                    "travel to",
                ],
                "answer": "to travel",
                "explanation": "PLAN → TO DO.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt": "She finished ___ the report.",
                "options": [
                    "writing",
                    "to write",
                    "write",
                    "wrote",
                ],
                "answer": "writing",
                "explanation": "FINISH → DOING.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt": "He suggested ___ a taxi.",
                "options": [
                    "taking",
                    "to take",
                    "take",
                    "took",
                ],
                "answer": "taking",
                "explanation": "SUGGEST → DOING.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt": "Thank you for ___ me.",
                "options": [
                    "helping",
                    "to help",
                    "help",
                    "helped",
                ],
                "answer": "helping",
                "explanation": "После FOR → verb-ing.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt": "She left without ___ goodbye.",
                "options": [
                    "saying",
                    "to say",
                    "say",
                    "said",
                ],
                "answer": "saying",
                "explanation": "После WITHOUT → verb-ing.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt": "I went to the shop ___ some milk.",
                "options": [
                    "to buy",
                    "buying",
                    "buy",
                    "bought",
                ],
                "answer": "to buy",
                "explanation": "Инфинитив показывает цель.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "build",
                "prompt": "Собери предложение с целью.",
                "options": [
                    "She",
                    "called",
                    "me",
                    "to",
                    "ask",
                    "a",
                    "question",
                ],
                "answer": "She called me to ask a question",
                "explanation": "TO ASK показывает цель звонка.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt": "You should ___ more.",
                "options": [
                    "rest",
                    "to rest",
                    "resting",
                    "rested",
                ],
                "answer": "rest",
                "explanation": "После SHOULD → bare infinitive.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt": "She can ___ very well.",
                "options": [
                    "swim",
                    "to swim",
                    "swimming",
                    "swam",
                ],
                "answer": "swim",
                "explanation": "После CAN → verb без TO.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt": "He stopped smoking. What does it mean?",
                "options": [
                    "He quit smoking.",
                    "He stopped in order to smoke.",
                    "He forgot to smoke.",
                    "He plans to smoke.",
                ],
                "answer": "He quit smoking.",
                "explanation": "STOP DOING = прекратить действие.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt": "He stopped to drink some water. What does it mean?",
                "options": [
                    "He stopped another action in order to drink water.",
                    "He stopped drinking water forever.",
                    "He forgot to drink water.",
                    "He avoided drinking water.",
                ],
                "answer": "He stopped another action in order to drink water.",
                "explanation": "STOP TO DO = остановиться, чтобы сделать другое действие.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt": "Remember ___ the door before you leave.",
                "options": [
                    "to lock",
                    "locking yesterday",
                    "lock to",
                    "locked",
                ],
                "answer": "to lock",
                "explanation": "REMEMBER TO DO = не забыть сделать.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt": "I remember ___ him at the conference.",
                "options": [
                    "meeting",
                    "to meet tomorrow",
                    "meet",
                    "met",
                ],
                "answer": "meeting",
                "explanation": "REMEMBER DOING = помнить уже совершённое действие.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt": "I tried ___ the box, but it was too heavy.",
                "options": [
                    "to lift",
                    "lifting as a method",
                    "lifted",
                    "to lifting",
                ],
                "answer": "to lift",
                "explanation": "TRY TO DO = пытаться выполнить действие.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt": "The computer is slow. Try ___ it.",
                "options": [
                    "restarting",
                    "to restarted",
                    "restart to",
                    "restarted",
                ],
                "answer": "restarting",
                "explanation": "TRY DOING = попробовать способ.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I hope to see you soon.",
                    "I hope seeing you soon.",
                    "I hope see to you soon.",
                    "I hope to seeing you soon.",
                ],
                "answer": "I hope to see you soon.",
                "explanation": "HOPE → TO DO.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She avoids driving at night.",
                    "She avoids to drive at night.",
                    "She avoids drive at night.",
                    "She avoiding to drive at night.",
                ],
                "answer": "She avoids driving at night.",
                "explanation": "AVOID → DOING.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt": "They hope ___ the match.",
                "options": [
                    "to win",
                    "winning",
                    "win to",
                    "won",
                ],
                "answer": "to win",
                "explanation": "HOPE → TO DO.",
            },

            {
                "order": 22,
                "prompt": "I don't mind ___ here.",
                "options": [
                    "waiting",
                    "to wait",
                    "wait",
                    "waited",
                ],
                "answer": "waiting",
                "explanation": "MIND → DOING.",
            },

            {
                "order": 23,
                "prompt": "After ___ dinner, we went for a walk.",
                "options": [
                    "finishing",
                    "to finish",
                    "finish",
                    "finished",
                ],
                "answer": "finishing",
                "explanation": "После AFTER → verb-ing.",
            },

            {
                "order": 24,
                "prompt": "He went to the bank ___ some money.",
                "options": [
                    "to withdraw",
                    "withdrawing",
                    "withdraw",
                    "withdrew",
                ],
                "answer": "to withdraw",
                "explanation": "TO + verb показывает цель.",
            },

            {
                "order": 25,
                "prompt": "You must ___ now.",
                "options": [
                    "leave",
                    "to leave",
                    "leaving",
                    "left",
                ],
                "answer": "leave",
                "explanation": "После MUST используется bare infinitive.",
            },

            {
                "order": 26,
                "prompt": "She stopped ___ because the doctor told her to.",
                "options": [
                    "smoking",
                    "to smoke",
                    "smoke",
                    "smoked",
                ],
                "answer": "smoking",
                "explanation": "STOP DOING = прекратить действие.",
            },

            {
                "order": 27,
                "prompt": "We stopped ___ a photo.",
                "options": [
                    "to take",
                    "taking forever",
                    "take",
                    "took",
                ],
                "answer": "to take",
                "explanation": "STOP TO DO = остановиться, чтобы сделать что-то.",
            },

            {
                "order": 28,
                "prompt": "Don't forget ___ me tonight.",
                "options": [
                    "to call",
                    "calling yesterday",
                    "call to",
                    "called",
                ],
                "answer": "to call",
                "explanation": "FORGET TO DO = забыть выполнить действие.",
            },

            {
                "order": 29,
                "prompt": "Choose the correct pair.",
                "options": [
                    "I want to learn English. / I enjoy learning English.",
                    "I want learning English. / I enjoy to learn English.",
                    "I want learn English. / I enjoy learn English.",
                    "I want to learning English. / I enjoy learned English.",
                ],
                "answer": "I want to learn English. / I enjoy learning English.",
                "explanation": "WANT → TO DO; ENJOY → DOING.",
            },

            {
                "order": 30,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    "She decided to leave. / He finished working. / Thank you for helping. / You should rest.",
                    "She decided leaving. / He finished to work. / Thank you for to help. / You should to rest.",
                    "She decided leave. / He finished work to. / Thank you helping for. / You should resting.",
                    "She decided to leaving. / He finished worked. / Thank you to helping. / You shoulded rest.",
                ],
                "answer": "She decided to leave. / He finished working. / Thank you for helping. / You should rest.",
                "explanation": "DECIDE → TO DO; FINISH → DOING; after preposition → DOING; modal → bare infinitive.",
            },

        ]


        all_exercises = training + final_test

        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

            section = (
                section_objects[data["section"]]
                if data["order"] <= 20
                else None
            )


            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "section": section,
                    "exercise_type": data.get(
                        "type",
                        "choice",
                    ),
                    "prompt": data["prompt"],
                    "options": data["options"],
                    "correct_answer": data["answer"],
                    "explanation": data["explanation"],
                    "is_published": True,
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
                "✅ Interactive A1 Lesson 42 seeded"
            )
        )

        self.stdout.write(
            f"Micro rules: {lesson.sections.count()}"
        )

        self.stdout.write(
            "Training exercises: "
            f"{lesson.exercises.filter(section__isnull=False).count()}"
        )

        self.stdout.write(
            "Final test: "
            f"{lesson.exercises.filter(section__isnull=True).count()}"
        )
