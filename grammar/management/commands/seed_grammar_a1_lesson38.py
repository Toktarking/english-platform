from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 38: "
        "Present Continuous for future arrangements."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=38,
            defaults={
                "title": "Present Continuous для будущего",
                "slug": "present-continuous-future",
                "theory_text": (
                    "Present Continuous for future arrangements."
                ),
                "estimated_minutes": 40,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Present Continuous может говорить о будущем",
                "body": """Present Continuous используется не только для действия, которое происходит сейчас.

Он также может описывать будущее, если действие:

уже запланировано;

согласовано с другим человеком;

организовано;

связано с конкретным временем или местом.

Примеры:

I am meeting my teacher tomorrow.

We are flying to Astana on Friday.

She is seeing the doctor at ten.""",
            },

            {
                "order": 2,
                "title": "Основная формула",
                "body": """Формула:

subject + am/is/are + verb-ing + future time

Примеры:

I am working tomorrow.

She is coming tonight.

We are leaving on Monday.

They are meeting us at six.

Формы TO BE:

I → am

he/she/it → is

you/we/they → are""",
            },

            {
                "order": 3,
                "title": "Почему это будущее",
                "body": """Форма Present Continuous может быть одинаковой для настоящего и будущего.

Сравните:

I am meeting my teacher now.
— действие происходит сейчас.

I am meeting my teacher tomorrow.
— действие запланировано на будущее.

Будущее значение показывает контекст:

tomorrow;

tonight;

next week;

on Monday;

at six;

this weekend.""",
            },

            {
                "order": 4,
                "title": "Конкретная договорённость",
                "body": """Present Continuous часто используется, когда план уже согласован.

Пример:

I am meeting Marat at six.

Обычно это означает:

встреча уже согласована;

время известно;

другой человек знает о встрече.

Другие примеры:

I am having lunch with my manager tomorrow.

She is meeting her clients on Monday.

They are playing football with us tonight.""",
            },

            {
                "order": 5,
                "title": "Назначенные встречи",
                "body": """Present Continuous особенно часто используется для назначенных встреч.

Примеры:

I am seeing the doctor tomorrow.

She is meeting the dean at eleven.

We are talking to the client this afternoon.

He is having a lesson at five.

SEE в таком контексте означает встречу:

I am seeing the dentist tomorrow.

Это означает, что встреча со стоматологом уже назначена.""",
            },

            {
                "order": 6,
                "title": "Поездки и организованные планы",
                "body": """Present Continuous часто используется с глаголами движения:

come;

go;

leave;

arrive;

fly;

travel;

drive;

return;

stay.

Примеры:

We are flying to Almaty tomorrow.

She is leaving on Friday.

They are arriving at ten.

I am staying at a hotel next week.

Обычно уже есть конкретные детали: билеты, время, место или бронь.""",
            },

            {
                "order": 7,
                "title": "Отрицание",
                "body": """Отрицательная форма:

subject + am/is/are not + verb-ing

Примеры:

I am not working tomorrow.

She isn't coming tonight.

We aren't travelling next week.

They aren't meeting us on Monday.

Сокращения:

I'm not

isn't

aren't""",
            },

            {
                "order": 8,
                "title": "Вопросы и краткие ответы",
                "body": """Вопрос:

Am/Is/Are + subject + verb-ing?

Примеры:

Are you working tomorrow?

Is she coming tonight?

Are they travelling next week?

Is he meeting the manager?

Краткие ответы:

Yes, I am.

No, I'm not.

Yes, she is.

No, she isn't.

Yes, they are.

No, they aren't.""",
            },

            {
                "order": 9,
                "title": "Специальные вопросы",
                "body": """Формула:

Question word + am/is/are + subject + verb-ing?

Примеры:

What are you doing tomorrow?

Where is she staying?

When are they leaving?

Who are you meeting?

Why is he coming?

Вопрос:

What are you doing tomorrow?

часто означает:

Какие у тебя планы на завтра?""",
            },

            {
                "order": 10,
                "title": "Present Continuous или BE GOING TO",
                "body": """BE GOING TO показывает:

намерение;

общий план;

решение, принятое заранее.

Пример:

I am going to visit the doctor next week.

Present Continuous показывает:

конкретную договорённость;

назначенное время;

организованный план.

Пример:

I am seeing the doctor on Tuesday at ten.

Сравните:

I'm going to meet Marat soon.

I'm meeting Marat at six tomorrow.""",
            },

            {
                "order": 11,
                "title": "Present Continuous или WILL",
                "body": """WILL используется для:

спонтанного решения;

обещания;

предположения.

Пример:

I'll call her now.

Present Continuous показывает заранее организованное действие.

Пример:

I'm calling her at six tomorrow.

Сравните:

I'll meet him tomorrow.
— простое решение или обещание.

I'm meeting him tomorrow at ten.
— конкретная договорённость.""",
            },

            {
                "order": 12,
                "title": "Present Continuous или Present Simple",
                "body": """Present Simple используется для официального расписания.

Примеры:

The train leaves at six.

The lesson starts at nine.

The plane arrives at ten.

Present Continuous используется для личного плана.

Примеры:

We are taking the six o'clock train.

I am attending the lesson tomorrow.

She is flying on Monday.

Сравните:

The train leaves at six.
— расписание.

We are leaving at six.
— наш план.""",
            },

            {
                "order": 13,
                "title": "Типичные ошибки",
                "body": """Неправильно:

I meeting him tomorrow.

Правильно:

I am meeting him tomorrow.

Неправильно:

She are coming tonight.

Правильно:

She is coming tonight.

Неправильно:

They are leave tomorrow.

Правильно:

They are leaving tomorrow.

Неправильно:

Do you meeting him tomorrow?

Правильно:

Are you meeting him tomorrow?""",
            },

            {
                "order": 14,
                "title": "Как выбрать форму будущего",
                "body": """Шаг 1.

Решение принято сейчас?

→ WILL

I'll answer the phone.

Шаг 2.

Есть намерение, но детали ещё не обязательно согласованы?

→ BE GOING TO

I'm going to look for a new job.

Шаг 3.

Есть конкретная договорённость?

→ Present Continuous

I'm meeting the manager at eleven.

Шаг 4.

Это официальное расписание?

→ Present Simple

The meeting starts at eleven.""",
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
                "prompt": "We ___ having dinner with friends tonight.",
                "options": ["am", "is", "are", "do"],
                "answer": "are",
                "explanation": "We используется с are.",
            },

            {
                "order": 2,
                "prompt": "My sister ___ flying to Astana tomorrow.",
                "options": ["am", "is", "are", "does"],
                "answer": "is",
                "explanation": "My sister = she, поэтому is.",
            },

            {
                "order": 3,
                "prompt": "I am ___ the manager at ten.",
                "options": ["meet", "met", "meeting", "meets"],
                "answer": "meeting",
                "explanation": "Present Continuous: am + verb-ing.",
            },

            {
                "order": 4,
                "prompt": "They aren't ___ with us tomorrow.",
                "options": ["come", "came", "coming", "comes"],
                "answer": "coming",
                "explanation": "После are not используется verb-ing.",
            },

            {
                "order": 5,
                "prompt": "___ he working this weekend?",
                "options": ["Does", "Is", "Will does", "Did"],
                "answer": "Is",
                "explanation": "Вопрос Present Continuous начинается с Is.",
            },

            {
                "order": 6,
                "prompt": "Are you meeting Marat?",
                "options": [
                    "Yes, I am.",
                    "Yes, I do.",
                    "Yes, I will be.",
                    "Yes, I have.",
                ],
                "answer": "Yes, I am.",
                "explanation": "Краткий ответ повторяет форму am.",
            },

            {
                "order": 7,
                "prompt": "Where ___ she staying?",
                "options": ["does", "is", "will", "has"],
                "answer": "is",
                "explanation": "Where is she staying?",
            },

            {
                "order": 8,
                "prompt": "When ___ they leaving?",
                "options": ["are", "do", "will do", "did"],
                "answer": "are",
                "explanation": "When are they leaving?",
            },

            {
                "order": 9,
                "prompt": "Who ___ coming tonight?",
                "options": ["are", "is", "does", "will be to"],
                "answer": "is",
                "explanation": "Who как подлежащее обычно используется с is.",
            },

            {
                "order": 10,
                "prompt": (
                    "I have an appointment. "
                    "I ___ the doctor tomorrow."
                ),
                "options": [
                    "will see suddenly",
                    "am seeing",
                    "see every day",
                    "am see",
                ],
                "answer": "am seeing",
                "explanation": "Назначенная встреча → Present Continuous.",
            },

            {
                "order": 11,
                "prompt": "The train ___ at seven.",
                "options": [
                    "is leaving every day",
                    "leaves",
                    "leave",
                    "will leaving",
                ],
                "answer": "leaves",
                "explanation": "Расписание → Present Simple.",
            },

            {
                "order": 12,
                "prompt": (
                    "We ___ the seven o'clock train tomorrow."
                ),
                "options": [
                    "take every day",
                    "are taking",
                    "will to take",
                    "taking",
                ],
                "answer": "are taking",
                "explanation": "Личный организованный план → Present Continuous.",
            },

            {
                "order": 13,
                "prompt": "The phone is ringing. I ___ answer it.",
                "options": [
                    "am answering tomorrow",
                    "will",
                    "am going every day",
                    "do",
                ],
                "answer": "will",
                "explanation": "Спонтанное решение → will.",
            },

            {
                "order": 14,
                "prompt": (
                    "I have decided to study abroad. "
                    "I ___ apply next year."
                ),
                "options": [
                    "am going to",
                    "will suddenly",
                    "am applying at this second only",
                    "do",
                ],
                "answer": "am going to",
                "explanation": "Намерение, принятое заранее → be going to.",
            },

            {
                "order": 15,
                "prompt": (
                    "The appointment is confirmed. "
                    "I ___ the director at three."
                ),
                "options": [
                    "am meeting",
                    "will meet suddenly",
                    "meet every day",
                    "am going meet",
                ],
                "answer": "am meeting",
                "explanation": "Подтверждённая встреча → Present Continuous.",
            },

            {
                "order": 16,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "I meeting him tomorrow.",
                    "I am meeting him tomorrow.",
                    "I am meet him tomorrow.",
                    "I do meeting him tomorrow.",
                ],
                "answer": "I am meeting him tomorrow.",
                "explanation": "Нужна форма am + verb-ing.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She are coming tonight.",
                    "She is coming tonight.",
                    "She is come tonight.",
                    "She does coming tonight.",
                ],
                "answer": "She is coming tonight.",
                "explanation": "She → is + coming.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct question.",
                "options": [
                    "Do you meeting him tomorrow?",
                    "Are you meeting him tomorrow?",
                    "Will you meeting him tomorrow?",
                    "Are you meet him tomorrow?",
                ],
                "answer": "Are you meeting him tomorrow?",
                "explanation": "Вопрос Present Continuous: Are + subject + verb-ing?",
            },

            {
                "order": 19,
                "prompt": "Which sentence shows a concrete arrangement?",
                "options": [
                    "I'm going to meet Marat sometime soon.",
                    "I'm meeting Marat at six tomorrow.",
                    "I think I will meet Marat one day.",
                    "I meet Marat every Friday.",
                ],
                "answer": "I'm meeting Marat at six tomorrow.",
                "explanation": "Есть конкретное время и договорённость.",
            },

            {
                "order": 20,
                "prompt": "Which sentence shows a general intention?",
                "options": [
                    "I'm meeting the manager at eleven.",
                    "I'm going to look for a new job.",
                    "The meeting starts at eleven.",
                    "I'll answer the phone now.",
                ],
                "answer": "I'm going to look for a new job.",
                "explanation": "Намерение без конкретной договорённости → be going to.",
            },

            {
                "order": 21,
                "prompt": "Which sentence describes an official timetable?",
                "options": [
                    "We're leaving at six.",
                    "The train leaves at six.",
                    "We're going to leave sometime.",
                    "We'll leave because I just decided.",
                ],
                "answer": "The train leaves at six.",
                "explanation": "Официальное расписание → Present Simple.",
            },

            {
                "order": 22,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "She doesn't coming tonight.",
                    "She isn't coming tonight.",
                    "She won't coming tonight.",
                    "She not is come tonight.",
                ],
                "answer": "She isn't coming tonight.",
                "explanation": "Present Continuous negative: is not + verb-ing.",
            },

            {
                "order": 23,
                "prompt": "Choose the best future-form pair.",
                "options": [
                    (
                        "I'll answer the phone. / "
                        "I'm meeting the manager at eleven."
                    ),
                    (
                        "I'm answering suddenly the phone tomorrow. / "
                        "I meet manager at eleven arrangement."
                    ),
                    (
                        "I will answering the phone. / "
                        "I'm meet the manager."
                    ),
                    (
                        "I answer will the phone. / "
                        "I am going meeting manager."
                    ),
                ],
                "answer": (
                    "I'll answer the phone. / "
                    "I'm meeting the manager at eleven."
                ),
                "explanation": (
                    "Will → решение сейчас; "
                    "Present Continuous → конкретная договорённость."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct comparison.",
                "options": [
                    (
                        "I'm going to visit the doctor next week. / "
                        "I'm seeing the doctor on Tuesday at ten."
                    ),
                    (
                        "I'm going visit the doctor. / "
                        "I'm see the doctor at ten."
                    ),
                    (
                        "I will going to visit the doctor. / "
                        "I'm seeing to doctor."
                    ),
                    (
                        "I'm going to visiting the doctor. / "
                        "I am see the doctor."
                    ),
                ],
                "answer": (
                    "I'm going to visit the doctor next week. / "
                    "I'm seeing the doctor on Tuesday at ten."
                ),
                "explanation": (
                    "Going to → намерение; "
                    "Present Continuous → назначенная встреча."
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
                "✅ A1 Lesson 38 seeded: "
                "Present Continuous for future"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
