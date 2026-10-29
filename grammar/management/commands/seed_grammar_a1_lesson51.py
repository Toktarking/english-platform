from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 51: "
        "Direct and Reported Speech."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=51,
            defaults={
                "title": "Прямая и косвенная речь",
                "slug": "reported-speech",
                "theory_text": (
                    "Direct and Reported Speech: "
                    "statements, questions and commands."
                ),
                "estimated_minutes": 50,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Прямая и косвенная речь",
                "body": """Прямая речь передаёт точные слова человека.

Anna said, "I am tired."

Косвенная речь передаёт смысл сказанного:

Anna said that she was tired.

При переходе в косвенную речь могут меняться:

местоимения;

времена;

слова времени и места;

порядок слов;

форма вопроса;

форма команды.

Кавычки в косвенной речи исчезают.""",
            },

            {
                "order": 2,
                "title": "SAY, TELL и THAT",
                "body": """SAY обычно используется без человека:

He said that he was tired.

Не:

He said me...

TELL требует человека:

He told me that he was tired.

Не:

He told that...

Сравните:

He said that he was tired.

He told me that he was tired.

THAT часто можно опустить:

She said that she was busy.

She said she was busy.""",
            },

            {
                "order": 3,
                "title": "Сдвиг времён: Present",
                "body": """Если reporting verb стоит в прошлом, время часто сдвигается назад.

Present Simple → Past Simple

"I work every day."

→ He said that he worked every day.

Present Continuous → Past Continuous

"I am working now."

→ He said that he was working then.

Этот сдвиг называется:

backshift.""",
            },

            {
                "order": 4,
                "title": "Сдвиг времён: Past и Perfect",
                "body": """Past Simple → Past Perfect

"I finished the work."

→ He said that he had finished the work.

Present Perfect → Past Perfect

"I have finished."

→ He said that he had finished.

Past Continuous → Past Perfect Continuous

"I was working."

→ He said that he had been working.

Past Perfect обычно не меняется.""",
            },

            {
                "order": 5,
                "title": "Модальные глаголы",
                "body": """При обычном backshift:

will → would

can → could

may → might

must → часто had to

Примеры:

"I will call you."

→ He said that he would call me.

"I can swim."

→ She said that she could swim.

"I may come."

→ She said that she might come.

Should, could, might и would обычно не меняются.""",
            },

            {
                "order": 6,
                "title": "Когда время можно не менять",
                "body": """Backshift нужен не всегда.

Если reporting verb стоит в настоящем:

She says, "I am tired."

→ She says that she is tired.

Если сообщается общий факт:

The teacher said, "Water boils at 100°C."

→ The teacher said that water boils at 100°C.

Если ситуация всё ещё актуальна, настоящее время иногда можно сохранить.""",
            },

            {
                "order": 7,
                "title": "Изменение местоимений",
                "body": """Местоимения меняются по смыслу.

Ali said, "I am busy."

→ Ali said that he was busy.

They said, "We are ready."

→ They said that they were ready.

She said to me, "You are late."

→ She told me that I was late.

He said, "My car is new."

→ He said that his car was new.

Важно понять: кто говорит и кому.""",
            },

            {
                "order": 8,
                "title": "Слова времени и места",
                "body": """Частые изменения:

now → then

today → that day

yesterday → the day before

tomorrow → the next day

last week → the week before

next week → the following week

ago → before

here → there

this → that

these → those

Пример:

"I will call you tomorrow."

→ She said that she would call me the next day.""",
            },

            {
                "order": 9,
                "title": "Утверждения и отрицания",
                "body": """Для утверждения:

said that + sentence

"I am tired."

→ She said that she was tired.

Если указываем человека:

told + person + that + sentence

→ She told me that she was tired.

Отрицание сохраняет смысл:

"I don't like coffee."

→ He said that he didn't like coffee.

"I won't come."

→ He said that he wouldn't come.""",
            },

            {
                "order": 10,
                "title": "Общие вопросы: IF / WHETHER",
                "body": """Для вопросов Yes/No используются:

if

whether

Формула:

asked + if/whether + прямой порядок слов

"Are you tired?"

→ She asked if I was tired.

"Did she call?"

→ He asked whether she had called.

Важно:

в косвенном вопросе нет вопросительного порядка слов.

Не:

She asked if was I tired.

Правильно:

She asked if I was tired.""",
            },

            {
                "order": 11,
                "title": "Специальные вопросы",
                "body": """Вопросительное слово сохраняется:

what

where

when

why

who

how

Формула:

asked + question word + прямой порядок слов

"Where do you live?"

→ She asked where I lived.

"What are you doing?"

→ He asked what I was doing.

Do, does и did в косвенном вопросе исчезают.""",
            },

            {
                "order": 12,
                "title": "Команды и просьбы",
                "body": """Для приказов и просьб используется:

tell/ask + person + to + V1

"Sit down."

→ The teacher told us to sit down.

"Please help me."

→ She asked me to help her.

Отрицательная команда:

tell/ask + person + not to + V1

"Don't open the door."

→ He told me not to open the door.""",
            },

            {
                "order": 13,
                "title": "Другие reporting verbs",
                "body": """Совет:

"You should rest."

→ The doctor advised me to rest.

Предложение помощи:

"I'll help you."

→ He offered to help me.

Обещание:

"I'll call you."

→ She promised to call me.

Отказ:

"I won't do it."

→ He refused to do it.

Предложение идеи:

"Let's take a taxi."

→ She suggested taking a taxi.

После suggest обычно:

doing

или

that + sentence.""",
            },

            {
                "order": 14,
                "title": "Алгоритм Reported Speech",
                "body": """Шаг 1.

Определите тип:

утверждение;

вопрос;

приказ;

просьба;

совет;

предложение.

Шаг 2.

Выберите reporting verb:

said;

told;

asked;

advised;

promised;

suggested.

Шаг 3.

Измените местоимения.

Шаг 4.

При необходимости сделайте backshift.

Шаг 5.

Измените слова времени и места.

Шаг 6.

Уберите кавычки.

Самое важное:

в косвенных вопросах используется прямой порядок слов.""",
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
                "prompt": (
                    '"I work in a bank," he said.'
                ),
                "options": [
                    "He said that he worked in a bank.",
                    "He said that he works yesterday.",
                    "He told that he worked in a bank.",
                    "He asked if he worked in a bank.",
                ],
                "answer": "He said that he worked in a bank.",
                "explanation": (
                    "Present Simple → Past Simple after said."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    '"I am studying now," she said.'
                ),
                "options": [
                    "She said that she was studying then.",
                    "She said that she is studying yesterday.",
                    "She told that she studied now.",
                    "She asked if she studied.",
                ],
                "answer": (
                    "She said that she was studying then."
                ),
                "explanation": (
                    "Present Continuous → Past Continuous; "
                    "now → then."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    '"I saw him yesterday," he said.'
                ),
                "options": [
                    "He said that he saw him tomorrow.",
                    (
                        "He said that he had seen him "
                        "the day before."
                    ),
                    "He told that he had saw him.",
                    "He asked if he saw him.",
                ],
                "answer": (
                    "He said that he had seen him "
                    "the day before."
                ),
                "explanation": (
                    "Past Simple → Past Perfect; "
                    "yesterday → the day before."
                ),
            },

            {
                "order": 4,
                "prompt": '"I have finished," she said.',
                "options": [
                    "She said that she had finished.",
                    "She said that she has finished yesterday.",
                    "She told that she finished now.",
                    "She asked if she had finished.",
                ],
                "answer": "She said that she had finished.",
                "explanation": (
                    "Present Perfect → Past Perfect."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    '"I will come tomorrow," he said.'
                ),
                "options": [
                    (
                        "He said that he would come "
                        "the next day."
                    ),
                    "He said that he will come yesterday.",
                    "He told that he would came.",
                    "He asked if he came.",
                ],
                "answer": (
                    "He said that he would come "
                    "the next day."
                ),
                "explanation": (
                    "Will → would; tomorrow → the next day."
                ),
            },

            {
                "order": 6,
                "prompt": '"Can you swim?" she asked.',
                "options": [
                    "She asked can I swim.",
                    "She asked if I could swim.",
                    "She told me if I could swim.",
                    "She said whether could I swim.",
                ],
                "answer": "She asked if I could swim.",
                "explanation": (
                    "Yes/No question → asked if; "
                    "can → could; direct word order."
                ),
            },

            {
                "order": 7,
                "prompt": '"What are you doing?" he asked.',
                "options": [
                    "He asked what was I doing.",
                    "He asked what I was doing.",
                    "He said what I did.",
                    "He asked what did I do.",
                ],
                "answer": "He asked what I was doing.",
                "explanation": (
                    "Wh-word сохраняется, но порядок слов прямой."
                ),
            },

            {
                "order": 8,
                "prompt": '"Why did she leave?" he asked.',
                "options": [
                    "He asked why had she left.",
                    "He asked why she had left.",
                    "He said why she left.",
                    "He asked why did she leave.",
                ],
                "answer": "He asked why she had left.",
                "explanation": (
                    "Did исчезает; Past Simple → Past Perfect."
                ),
            },

            {
                "order": 9,
                "prompt": '"Please wait," she said.',
                "options": [
                    "She asked me to wait.",
                    "She said me wait.",
                    "She told that I waited.",
                    "She asked if I waited.",
                ],
                "answer": "She asked me to wait.",
                "explanation": (
                    "Просьба: ask + person + to + V1."
                ),
            },

            {
                "order": 10,
                "prompt": '"Don\'t touch it," he said.',
                "options": [
                    "He told me not to touch it.",
                    "He said me don't touch it.",
                    "He asked me to not touching it.",
                    "He told that I didn't touch it.",
                ],
                "answer": "He told me not to touch it.",
                "explanation": (
                    "Отрицательная команда: "
                    "tell + person + not to + V1."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    '"You should rest," the doctor said.'
                ),
                "options": [
                    "The doctor advised me to rest.",
                    "The doctor said me to rest.",
                    "The doctor asked if I rested.",
                    "The doctor suggested to rest me.",
                ],
                "answer": "The doctor advised me to rest.",
                "explanation": (
                    "Совет можно передать через advise + person + to."
                ),
            },

            {
                "order": 12,
                "prompt": '"I\'ll help you," he said.',
                "options": [
                    "He offered to help me.",
                    "He offered helping me to.",
                    "He said me help.",
                    "He asked if I helped.",
                ],
                "answer": "He offered to help me.",
                "explanation": (
                    "Предложение помощи → offered to help."
                ),
            },

            {
                "order": 13,
                "prompt": '"I won\'t do it," he said.',
                "options": [
                    "He refused to do it.",
                    "He refused doing it.",
                    "He said me not do it.",
                    "He asked not to do it.",
                ],
                "answer": "He refused to do it.",
                "explanation": (
                    "Отказ → refuse + to + V1."
                ),
            },

            {
                "order": 14,
                "prompt": '"Let\'s meet at six," she said.',
                "options": [
                    "She suggested meeting at six.",
                    "She suggested to meet at six.",
                    "She told meeting at six.",
                    "She asked if meet at six.",
                ],
                "answer": "She suggested meeting at six.",
                "explanation": (
                    "Suggest обычно используется с verb-ing."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    '"Do you know the answer?" he asked.'
                ),
                "options": [
                    "He asked if I knew the answer.",
                    "He asked did I know the answer.",
                    "He told me if I know the answer.",
                    "He said whether knew I the answer.",
                ],
                "answer": "He asked if I knew the answer.",
                "explanation": (
                    "Yes/No question → if + direct word order."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct SAY/TELL sentence.",
                "options": [
                    "He said me that he was tired.",
                    "He told me that he was tired.",
                    "He told that he was tired.",
                    "He said me he tired.",
                ],
                "answer": "He told me that he was tired.",
                "explanation": (
                    "Tell требует человека: told me."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence with SAY.",
                "options": [
                    "She said that she was busy.",
                    "She said me that she was busy.",
                    "She told that she was busy.",
                    "She said to that she busy.",
                ],
                "answer": "She said that she was busy.",
                "explanation": (
                    "Say обычно не требует объекта person."
                ),
            },

            {
                "order": 18,
                "prompt": (
                    "Choose the correct indirect question."
                ),
                "options": [
                    "Can you tell me where is the bank?",
                    "Can you tell me where the bank is?",
                    "Can you tell me where does the bank be?",
                    "Can you tell me where the bank does is?",
                ],
                "answer": (
                    "Can you tell me where the bank is?"
                ),
                "explanation": (
                    "В косвенном вопросе используется прямой порядок слов."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    '"I can help," she said.'
                ),
                "options": [
                    "She said that she could help.",
                    "She said that she can helped.",
                    "She told that she could help.",
                    "She said that she could to help.",
                ],
                "answer": "She said that she could help.",
                "explanation": (
                    "Can → could."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    '"I may come," he said.'
                ),
                "options": [
                    "He said that he might come.",
                    "He said that he may came.",
                    "He told that he might to come.",
                    "He asked that he might come.",
                ],
                "answer": "He said that he might come.",
                "explanation": (
                    "May → might."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "Choose the correct time-word changes."
                ),
                "options": [
                    (
                        "now → then / "
                        "yesterday → the day before / "
                        "tomorrow → the next day"
                    ),
                    (
                        "now → tomorrow / "
                        "yesterday → next day / "
                        "tomorrow → before"
                    ),
                    (
                        "now → there / "
                        "yesterday → then / "
                        "tomorrow → ago"
                    ),
                    (
                        "now → that / "
                        "yesterday → here / "
                        "tomorrow → those"
                    ),
                ],
                "answer": (
                    "now → then / "
                    "yesterday → the day before / "
                    "tomorrow → the next day"
                ),
                "explanation": (
                    "Это стандартные изменения слов времени."
                ),
            },

            {
                "order": 22,
                "prompt": (
                    '"I am tired," Anna said.'
                ),
                "options": [
                    "Anna said that she was tired.",
                    "Anna said that I was tired.",
                    "Anna told that she was tired.",
                    "Anna asked if she tired.",
                ],
                "answer": "Anna said that she was tired.",
                "explanation": (
                    "I меняется на she по смыслу; am → was."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct command/request pair."
                ),
                "options": [
                    (
                        "He told me to wait. / "
                        "She asked me not to be late."
                    ),
                    (
                        "He told me that wait. / "
                        "She asked me don't be late."
                    ),
                    (
                        "He said me to wait. / "
                        "She asked that I not late."
                    ),
                    (
                        "He told to me wait. / "
                        "She asked me to not late."
                    ),
                ],
                "answer": (
                    "He told me to wait. / "
                    "She asked me not to be late."
                ),
                "explanation": (
                    "Command/request: person + to V1; "
                    "negative: person + not to V1."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "She said that she was tired. / "
                        "He asked if I was ready. / "
                        "She asked where I lived. / "
                        "He told me not to leave."
                    ),
                    (
                        "She said me that she was tired. / "
                        "He asked was I ready. / "
                        "She asked where did I live. / "
                        "He told me don't leave."
                    ),
                    (
                        "She told that she was tired. / "
                        "He asked if was I ready. / "
                        "She asked where do I live. / "
                        "He said me not leave."
                    ),
                    (
                        "She said that she is tired yesterday. / "
                        "He told if I ready. / "
                        "She asked where I did live. / "
                        "He told that not to leave."
                    ),
                ],
                "answer": (
                    "She said that she was tired. / "
                    "He asked if I was ready. / "
                    "She asked where I lived. / "
                    "He told me not to leave."
                ),
                "explanation": (
                    "Утверждение → said that; "
                    "Yes/No question → asked if; "
                    "Wh-question → direct word order; "
                    "negative command → told + person + not to."
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
                "✅ A1 Lesson 51 seeded: Reported Speech"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
