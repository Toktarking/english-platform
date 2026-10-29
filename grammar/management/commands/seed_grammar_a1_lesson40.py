from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 40: "
        "Modal verbs must, have to, should, may, might, need."
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
                "theory_text": "Modal verbs and obligation.",
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что выражают модальные глаголы",
                "body": """Модальные глаголы помогают выражать:

обязанность;

необходимость;

совет;

разрешение;

вероятность;

возможность;

отсутствие необходимости;

запрет.

В этом уроке:

must;

have to;

should;

may;

might;

need.

После must, should, may и might используется первая форма глагола без TO.

You must leave.

She should study.

He may come.

They might help.""",
            },

            {
                "order": 2,
                "title": "MUST — сильная обязанность",
                "body": """MUST выражает:

сильную обязанность;

необходимость;

правило;

приказ;

настоятельное требование.

Примеры:

You must wear a seat belt.

Students must arrive on time.

I must finish this report today.

You must be careful.

MUST не меняется по лицам:

I must work.

He must work.

She must work.

Не:

He musts work.""",
            },

            {
                "order": 3,
                "title": "MUSTN'T — запрет",
                "body": """MUST NOT сокращается до:

mustn't

И означает:

нельзя;

запрещено.

Примеры:

You mustn't smoke here.

Students mustn't use phones during the exam.

You mustn't touch this button.

Важно:

MUSTN'T не означает «не нужно».

Сравните:

You mustn't go.
— тебе нельзя уходить.

You don't have to go.
— тебе не нужно уходить.""",
            },

            {
                "order": 4,
                "title": "HAVE TO — внешняя необходимость",
                "body": """HAVE TO выражает обязанность из-за внешних обстоятельств.

Примеры:

I have to work tomorrow.

She has to wear a uniform.

We have to leave early.

They have to follow the rules.

Формы:

I/you/we/they → have to

he/she/it → has to

Пример:

I have to get up at six because my work starts at eight.

Причина — расписание, а не личное решение.""",
            },

            {
                "order": 5,
                "title": "MUST или HAVE TO",
                "body": """Оба выражают обязанность, но акцент различается.

MUST:

личное ощущение необходимости;

требование говорящего;

сильный приказ;

правило.

HAVE TO:

внешняя необходимость;

расписание;

закон;

обстоятельства.

Сравните:

I must exercise more.
— я сам считаю это необходимым.

I have to wear a uniform at work.
— это правило работы.""",
            },

            {
                "order": 6,
                "title": "Прошлое и будущее: HAD TO и WILL HAVE TO",
                "body": """У MUST нет обычной прошедшей формы.

Для прошлого используется:

had to

Примеры:

I had to work yesterday.

She had to leave early.

They had to wait.

Не:

I musted work.

Для будущего часто используется:

will have to

Примеры:

I will have to work tomorrow.

She will have to take an exam.

They will have to move.""",
            },

            {
                "order": 7,
                "title": "SHOULD — совет",
                "body": """SHOULD выражает:

совет;

рекомендацию;

правильное действие;

мягкую обязанность.

Примеры:

You should rest.

She should study more.

We should leave now.

You should see a doctor.

Отрицание:

shouldn't

You shouldn't smoke.

Вопрос:

Should I call him?

What should I do?

MUST сильнее, чем SHOULD.""",
            },

            {
                "order": 8,
                "title": "MAY и MIGHT — возможность",
                "body": """MAY и MIGHT могут выражать вероятность.

Примеры:

She may come later.

He might be at home.

It may rain.

They might not agree.

Оба часто переводятся как:

«возможно».

MIGHT обычно может выражать немного меньшую уверенность.

Сравните:

She may come.

She might come.

Разница часто небольшая.""",
            },

            {
                "order": 9,
                "title": "MAY — разрешение",
                "body": """MAY также используется для вежливой просьбы о разрешении.

Примеры:

May I come in?

May I ask a question?

May I use your phone?

May I leave early?

MAY звучит более официально.

CAN чаще используется в обычной разговорной речи:

Can I use your phone?

May I use your phone?

Оба варианта возможны, но стиль разный.""",
            },

            {
                "order": 10,
                "title": "NEED и NEED TO",
                "body": """NEED может быть обычным глаголом.

Примеры:

I need help.

She needs more time.

Также используется:

need to + verb

I need to work.

You need to rest.

She needs to call the doctor.

They need to leave.

Обратите внимание:

he/she/it → needs to

I/you/we/they → need to""",
            },

            {
                "order": 11,
                "title": "DON'T NEED TO, DON'T HAVE TO и NEEDN'T",
                "body": """Все эти формы могут выражать отсутствие необходимости.

You don't need to wait.

You don't have to wait.

You needn't wait.

Значение:

ждать необязательно.

После NEEDN'T нет TO:

Правильно:

You needn't wait.

Неправильно:

You needn't to wait.

В современном разговорном английском don't need to используется чаще.""",
            },

            {
                "order": 12,
                "title": "Как строить вопросы",
                "body": """С настоящими модальными глаголами DO/DOES не нужны.

Правильно:

Must I go?

Should she call?

May I come in?

Не:

Do I must go?

Does she should call?

Но HAVE TO — другая конструкция.

С ней используются DO и DOES:

Do you have to work?

Does she have to wear a uniform?

Важно:

Does she have to work?

Не:

Does she has to work?""",
            },

            {
                "order": 13,
                "title": "MAY/MIGHT + BE и HAVE",
                "body": """После MAY и MIGHT используется первая форма.

С BE:

She may be tired.

He might be at work.

It might be dangerous.

С HAVE:

She may have the key.

He might have enough money.

We might have time.

Для будущего:

She might call later.

They may move next year.

Не нужно добавлять WILL:

Неправильно:

She may will come.

Правильно:

She may come.""",
            },

            {
                "order": 14,
                "title": "Как выбрать правильную форму",
                "body": """Сильная обязанность или приказ?

→ MUST

You must stop.

Внешняя необходимость?

→ HAVE TO

I have to wear a uniform.

Совет?

→ SHOULD

You should rest.

Возможно?

→ MAY / MIGHT

She may come.

Нет необходимости?

→ DON'T HAVE TO / DON'T NEED TO / NEEDN'T

You don't have to wait.

Запрещено?

→ MUSTN'T

You mustn't smoke here.

Главное различие:

MUSTN'T = запрещено

DON'T HAVE TO = необязательно""",
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
                "prompt": "Students ___ arrive on time.",
                "options": [
                    "must",
                    "might",
                    "needn't",
                    "may not perhaps",
                ],
                "answer": "must",
                "explanation": (
                    "Правило или сильная обязанность → must."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "You ___ use your phone during the exam."
                ),
                "options": [
                    "don't have to",
                    "mustn't",
                    "should",
                    "may",
                ],
                "answer": "mustn't",
                "explanation": (
                    "Запрет → mustn't."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "I ___ get up early because "
                    "my train leaves at seven."
                ),
                "options": [
                    "have to",
                    "might",
                    "shouldn't",
                    "may not",
                ],
                "answer": "have to",
                "explanation": (
                    "Расписание создаёт внешнюю необходимость."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "She ___ work late today because "
                    "there is an urgent task."
                ),
                "options": [
                    "has to",
                    "have to",
                    "musts",
                    "should to",
                ],
                "answer": "has to",
                "explanation": (
                    "She → has to."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "You have a headache. "
                    "You ___ see a doctor."
                ),
                "options": [
                    "should",
                    "mustn't",
                    "may not",
                    "needn't",
                ],
                "answer": "should",
                "explanation": (
                    "Это рекомендация → should."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "He ___ be at home, but I'm not sure."
                ),
                "options": [
                    "must because it is certain",
                    "might",
                    "has to",
                    "should to",
                ],
                "answer": "might",
                "explanation": (
                    "Неуверенная возможность → might."
                ),
            },

            {
                "order": 7,
                "prompt": "___ I come in?",
                "options": [
                    "May",
                    "Do",
                    "Must to",
                    "Am",
                ],
                "answer": "May",
                "explanation": (
                    "May I...? — вежливая просьба о разрешении."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "You ___ pay now. You can pay later."
                ),
                "options": [
                    "mustn't",
                    "don't have to",
                    "have to",
                    "should",
                ],
                "answer": "don't have to",
                "explanation": (
                    "Платить сейчас необязательно."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "We ___ hurry. We have plenty of time."
                ),
                "options": [
                    "mustn't",
                    "needn't",
                    "must",
                    "have to",
                ],
                "answer": "needn't",
                "explanation": (
                    "Нет необходимости торопиться."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "She ___ tell anyone. It is a secret."
                ),
                "options": [
                    "mustn't",
                    "doesn't have to",
                    "might",
                    "should",
                ],
                "answer": "mustn't",
                "explanation": (
                    "Разглашать секрет запрещено → mustn't."
                ),
            },

            {
                "order": 11,
                "prompt": "Does he ___ work on Saturdays?",
                "options": [
                    "has to",
                    "have to",
                    "musts",
                    "needs",
                ],
                "answer": "have to",
                "explanation": (
                    "После does используется have to."
                ),
            },

            {
                "order": 12,
                "prompt": "I ___ work yesterday.",
                "options": [
                    "musted",
                    "had to",
                    "have to tomorrow",
                    "shoulded",
                ],
                "answer": "had to",
                "explanation": (
                    "Прошедшая необходимость → had to."
                ),
            },

            {
                "order": 13,
                "prompt": "We ___ work next weekend.",
                "options": [
                    "will have to",
                    "will must",
                    "musted",
                    "will should",
                ],
                "answer": "will have to",
                "explanation": (
                    "Будущая необходимость → will have to."
                ),
            },

            {
                "order": 14,
                "prompt": "Maybe she is tired.",
                "options": [
                    "She may be tired.",
                    "She may tired.",
                    "She maybe tired.",
                    "She might is tired.",
                ],
                "answer": "She may be tired.",
                "explanation": (
                    "May + base form be."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "You ___ worry. Everything is fine."
                ),
                "options": [
                    "shouldn't",
                    "mustn't always",
                    "have to",
                    "may",
                ],
                "answer": "shouldn't",
                "explanation": (
                    "Совет не беспокоиться → shouldn't."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I must to go.",
                    "I must go.",
                    "I must going.",
                    "I must goes.",
                ],
                "answer": "I must go.",
                "explanation": (
                    "После must используется первая форма без to."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "He musts work.",
                    "He must work.",
                    "He must to work.",
                    "He does must work.",
                ],
                "answer": "He must work.",
                "explanation": (
                    "Must не получает окончание -s."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct question.",
                "options": [
                    "Does she should call?",
                    "Should she call?",
                    "Should she calls?",
                    "Do she should call?",
                ],
                "answer": "Should she call?",
                "explanation": (
                    "С should вспомогательный do/does не нужен."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "Which sentence means 'парковаться запрещено'?"
                ),
                "options": [
                    "You don't have to park here.",
                    "You mustn't park here.",
                    "You shouldn't to park here.",
                    "You may park here.",
                ],
                "answer": "You mustn't park here.",
                "explanation": (
                    "Mustn't означает запрет."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "Which sentence means 'приходить необязательно'?"
                ),
                "options": [
                    "You mustn't come.",
                    "You don't have to come.",
                    "You must come.",
                    "You may not come because it is forbidden.",
                ],
                "answer": "You don't have to come.",
                "explanation": (
                    "Don't have to = отсутствует необходимость."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct sentence with NEED.",
                "options": [
                    "She need to call the doctor.",
                    "She needs to call the doctor.",
                    "She needs call to doctor.",
                    "She needn't to call the doctor.",
                ],
                "answer": "She needs to call the doctor.",
                "explanation": (
                    "Need как обычный глагол: she needs to + verb."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence with NEEDN'T.",
                "options": [
                    "You needn't to wait.",
                    "You needn't wait.",
                    "You don't need wait.",
                    "You needn't waiting.",
                ],
                "answer": "You needn't wait.",
                "explanation": (
                    "После модального needn't TO не используется."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct possibility sentence.",
                "options": [
                    "She may will come later.",
                    "She might come later.",
                    "She might comes later.",
                    "She may to come later.",
                ],
                "answer": "She might come later.",
                "explanation": (
                    "После might используется первая форма без will и to."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct comparison.",
                "options": [
                    (
                        "You mustn't enter. / "
                        "You don't have to enter. / "
                        "You should rest. / "
                        "She might come."
                    ),
                    (
                        "You don't must enter. / "
                        "You mustn't to enter. / "
                        "You should to rest. / "
                        "She might comes."
                    ),
                    (
                        "You must not to enter. / "
                        "You don't have enter. / "
                        "You should resting. / "
                        "She may will come."
                    ),
                    (
                        "You musts enter. / "
                        "You doesn't have to enter. / "
                        "You shoulded rest. / "
                        "She might to come."
                    ),
                ],
                "answer": (
                    "You mustn't enter. / "
                    "You don't have to enter. / "
                    "You should rest. / "
                    "She might come."
                ),
                "explanation": (
                    "Mustn't = запрет; don't have to = необязательно; "
                    "should = совет; might = возможность."
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
                "✅ A1 Lesson 40 seeded: Modal verbs"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
