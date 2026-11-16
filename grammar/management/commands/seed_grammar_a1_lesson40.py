from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 40: modal verbs."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=40,
            defaults={
                "title": (
                    "Модальные глаголы: must, have to, "
                    "should, may, might, need"
                ),
                "slug": (
                    "modal-verbs-must-have-to-should-"
                    "may-might-need"
                ),
                "theory_text": (
                    "Modal verbs and obligation."
                ),
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
                "title":
                    "Что делают модальные глаголы?",

                "body":
                    """Модальные глаголы помогают выразить:

обязанность;

совет;

разрешение;

возможность;

запрет.

Сегодня:

MUST
HAVE TO
SHOULD
MAY
MIGHT
NEED

После MUST, SHOULD, MAY, MIGHT
используется первая форма глагола:

You must leave.

She should rest.

He may come.""",
            },


            {
                "order": 2,
                "title":
                    "MUST — сильная обязанность",

                "body":
                    """MUST показывает сильную обязанность
или важное правило.

You must wear a seat belt.

Students must arrive on time.

I must finish this today.

MUST не меняется:

I must work.

He must work.

Не:

He musts work.

После MUST нет TO.""",
            },


            {
                "order": 3,
                "title":
                    "MUSTN'T — запрещено",

                "body":
                    """MUSTN'T означает:

нельзя;

запрещено.

You mustn't smoke here.

You mustn't touch this button.

Очень важно:

MUSTN'T ≠ DON'T HAVE TO

You mustn't go.

→ тебе нельзя уходить.

You don't have to go.

→ тебе необязательно уходить.""",
            },


            {
                "order": 4,
                "title":
                    "HAVE TO — внешняя необходимость",

                "body":
                    """HAVE TO показывает обязанность
из-за правил или обстоятельств.

I have to work tomorrow.

She has to wear a uniform.

We have to leave early.

Формы:

I / you / we / they
→ have to

he / she / it
→ has to

Причина обычно внешняя:

работа;

расписание;

закон;

правило.""",
            },


            {
                "order": 5,
                "title":
                    "Прошлое и будущее: HAD TO / WILL HAVE TO",

                "body":
                    """Для прошлого используем:

HAD TO

I had to work yesterday.

She had to leave early.

Не:

musted.

Для будущей необходимости:

WILL HAVE TO

I will have to work tomorrow.

They will have to wait.""",
            },


            {
                "order": 6,
                "title":
                    "SHOULD — совет",

                "body":
                    """SHOULD показывает совет
или рекомендацию.

You should rest.

She should study more.

We should leave now.

Отрицание:

SHOULDN'T

You shouldn't smoke.

Вопрос:

Should I call him?

MUST сильнее.

SHOULD = совет.

MUST = обязанность.""",
            },


            {
                "order": 7,
                "title":
                    "MAY и MIGHT — возможно",

                "body":
                    """MAY и MIGHT показывают возможность.

She may come later.

He might be at home.

It may rain.

They might not agree.

После MAY / MIGHT:

только base verb.

may come

might be

Не:

may comes

might to come.""",
            },


            {
                "order": 8,
                "title":
                    "MAY — разрешение",

                "body":
                    """MAY также используется
для вежливой просьбы о разрешении.

May I come in?

May I ask a question?

May I use your phone?

В разговорной речи часто используется CAN:

Can I use your phone?

MAY звучит немного формальнее.""",
            },


            {
                "order": 9,
                "title":
                    "NEED TO и отсутствие необходимости",

                "body":
                    """NEED TO = нужно сделать.

I need to work.

She needs to call the doctor.

Для he / she / it:

NEEDS TO.

Отсутствие необходимости:

don't need to

don't have to

needn't

You don't need to wait.

You don't have to wait.

You needn't wait.

Все означают:

ждать необязательно.""",
            },


            {
                "order": 10,
                "title":
                    "Как быстро выбрать форму",

                "body":
                    """Сильная обязанность?

→ MUST

Внешнее правило?

→ HAVE TO

Совет?

→ SHOULD

Возможно?

→ MAY / MIGHT

Разрешение?

→ MAY

Нет необходимости?

→ DON'T HAVE TO
→ DON'T NEED TO
→ NEEDN'T

Запрещено?

→ MUSTN'T

Главное:

MUSTN'T = нельзя.

DON'T HAVE TO = необязательно.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects.update_or_create(
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


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            # SECTION 1
            {
                "order": 1,
                "section": 1,
                "type": "choice",
                "prompt":
                    "After MUST, which form is correct?",
                "options": [
                    "go",
                    "goes",
                    "to go",
                    "going",
                ],
                "answer":
                    "go",
                "explanation":
                    "После модального MUST используется base verb.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Choose the correct sentence.",
                "options": [
                    "She should rest.",
                    "She should rests.",
                    "She should to rest.",
                    "She should resting.",
                ],
                "answer":
                    "She should rest.",
                "explanation":
                    "После SHOULD → base verb.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "Students ___ arrive on time.",
                "options": [
                    "must",
                    "might",
                    "needn't",
                    "may",
                ],
                "answer":
                    "must",
                "explanation":
                    "Сильное правило → MUST.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "build",
                "prompt":
                    "Собери предложение.",
                "options": [
                    "You",
                    "must",
                    "be",
                    "careful",
                ],
                "answer":
                    "You must be careful",
                "explanation":
                    "После MUST используется BE, а не ARE.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "You ___ smoke here. It is prohibited.",
                "options": [
                    "mustn't",
                    "don't have to",
                    "should",
                    "may",
                ],
                "answer":
                    "mustn't",
                "explanation":
                    "Запрет → MUSTN'T.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "You ___ come tomorrow. It is optional.",
                "options": [
                    "don't have to",
                    "mustn't",
                    "must",
                    "have to",
                ],
                "answer":
                    "don't have to",
                "explanation":
                    "Необязательно → DON'T HAVE TO.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "I ___ wear a uniform at work.",
                "options": [
                    "have to",
                    "has to",
                    "musts",
                    "should to",
                ],
                "answer":
                    "have to",
                "explanation":
                    "I → HAVE TO.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "She ___ leave early because her train is at six.",
                "options": [
                    "has to",
                    "have to",
                    "musts",
                    "has",
                ],
                "answer":
                    "has to",
                "explanation":
                    "SHE → HAS TO.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "I ___ work late yesterday.",
                "options": [
                    "had to",
                    "musted",
                    "have to tomorrow",
                    "shoulded",
                ],
                "answer":
                    "had to",
                "explanation":
                    "Прошедшая необходимость → HAD TO.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "We ___ take another exam next month.",
                "options": [
                    "will have to",
                    "will must",
                    "will had to",
                    "musted",
                ],
                "answer":
                    "will have to",
                "explanation":
                    "Будущая необходимость → WILL HAVE TO.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "You look tired. You ___ rest.",
                "options": [
                    "should",
                    "mustn't",
                    "might not",
                    "needn't",
                ],
                "answer":
                    "should",
                "explanation":
                    "Это совет → SHOULD.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "You ___ stay up so late every night.",
                "options": [
                    "shouldn't",
                    "must",
                    "have to",
                    "may",
                ],
                "answer":
                    "shouldn't",
                "explanation":
                    "Совет не делать что-то → SHOULDN'T.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "She ___ come later, but I'm not sure.",
                "options": [
                    "might",
                    "must",
                    "has to",
                    "should to",
                ],
                "answer":
                    "might",
                "explanation":
                    "Неуверенная возможность → MIGHT.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "It ___ rain tonight.",
                "options": [
                    "may",
                    "may to",
                    "may rains",
                    "may will",
                ],
                "answer":
                    "may",
                "explanation":
                    "MAY + base verb.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "___ I come in?",
                "options": [
                    "May",
                    "Do",
                    "Am",
                    "Must to",
                ],
                "answer":
                    "May",
                "explanation":
                    "MAY I...? — вежливая просьба о разрешении.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "Choose the polite request for permission.",
                "options": [
                    "May I ask a question?",
                    "Do I may ask a question?",
                    "May I to ask a question?",
                    "May I asks a question?",
                ],
                "answer":
                    "May I ask a question?",
                "explanation":
                    "MAY + subject + base verb.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "She ___ call the doctor.",
                "options": [
                    "needs to",
                    "need to",
                    "needs call",
                    "needn't to",
                ],
                "answer":
                    "needs to",
                "explanation":
                    "SHE → NEEDS TO + verb.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "You ___ wait. You can leave now.",
                "options": [
                    "don't need to",
                    "mustn't",
                    "have to",
                    "must",
                ],
                "answer":
                    "don't need to",
                "explanation":
                    "Нет необходимости ждать.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which sentence means 'запрещено'?",
                "options": [
                    "You mustn't enter.",
                    "You don't have to enter.",
                    "You should enter.",
                    "You may enter.",
                ],
                "answer":
                    "You mustn't enter.",
                "explanation":
                    "MUSTN'T = запрещено.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which sentence means 'это необязательно'?",
                "options": [
                    "You don't have to do it.",
                    "You mustn't do it.",
                    "You must do it.",
                    "You have to do it.",
                ],
                "answer":
                    "You don't have to do it.",
                "explanation":
                    "DON'T HAVE TO = нет необходимости.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "You ___ show your passport at the border.",
                "options": [
                    "must",
                    "might",
                    "needn't",
                    "shouldn't",
                ],
                "answer":
                    "must",
                "explanation":
                    "Обязательное правило → MUST.",
            },

            {
                "order": 22,
                "prompt":
                    "Visitors ___ touch the paintings.",
                "options": [
                    "mustn't",
                    "don't have to",
                    "might",
                    "should",
                ],
                "answer":
                    "mustn't",
                "explanation":
                    "Запрет → MUSTN'T.",
            },

            {
                "order": 23,
                "prompt":
                    "He ___ wear safety shoes at work because company rules require them.",
                "options": [
                    "has to",
                    "have to",
                    "musts",
                    "may",
                ],
                "answer":
                    "has to",
                "explanation":
                    "Внешнее правило + HE → HAS TO.",
            },

            {
                "order": 24,
                "prompt":
                    "We ___ leave early yesterday because of the weather.",
                "options": [
                    "had to",
                    "musted",
                    "will have to",
                    "have to tomorrow",
                ],
                "answer":
                    "had to",
                "explanation":
                    "Прошедшая необходимость → HAD TO.",
            },

            {
                "order": 25,
                "prompt":
                    "You have an exam tomorrow. You ___ go to bed early.",
                "options": [
                    "should",
                    "mustn't",
                    "may not",
                    "needn't",
                ],
                "answer":
                    "should",
                "explanation":
                    "Рекомендация → SHOULD.",
            },

            {
                "order": 26,
                "prompt":
                    "I'm not sure, but Aida ___ be at the office.",
                "options": [
                    "might",
                    "must to",
                    "has to",
                    "shoulds",
                ],
                "answer":
                    "might",
                "explanation":
                    "Неуверенная возможность → MIGHT.",
            },

            {
                "order": 27,
                "prompt":
                    "Choose the correct permission question.",
                "options": [
                    "May I use this chair?",
                    "May I to use this chair?",
                    "Do I may use this chair?",
                    "May I uses this chair?",
                ],
                "answer":
                    "May I use this chair?",
                "explanation":
                    "MAY + subject + base verb.",
            },

            {
                "order": 28,
                "prompt":
                    "You ___ bring food. We already have enough.",
                "options": [
                    "don't need to",
                    "mustn't",
                    "must",
                    "have to",
                ],
                "answer":
                    "don't need to",
                "explanation":
                    "Нет необходимости → DON'T NEED TO.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct comparison.",
                "options": [
                    "You mustn't park here. / You don't have to come tomorrow.",
                    "You don't have to park here. / You mustn't come tomorrow if it is optional.",
                    "You mustn't to park here. / You don't have come tomorrow.",
                    "You must parkn't here. / You don't must come tomorrow.",
                ],
                "answer":
                    "You mustn't park here. / You don't have to come tomorrow.",
                "explanation":
                    "MUSTN'T = запрещено; DON'T HAVE TO = необязательно.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct set.",
                "options": [
                    "You must leave. / You should rest. / She may come. / We will have to wait.",
                    "You must to leave. / You should to rest. / She may comes. / We will must wait.",
                    "You must leaves. / You should resting. / She might to come. / We musted wait.",
                    "You do must leave. / You shoulded rest. / She may will come. / We will had to wait.",
                ],
                "answer":
                    "You must leave. / You should rest. / She may come. / We will have to wait.",
                "explanation":
                    "После модальных глаголов используется base verb; будущая необходимость → WILL HAVE TO.",
            },

        ]


        all_exercises = training + final_test


        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

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
                "✅ Interactive A1 Lesson 40 seeded"
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
