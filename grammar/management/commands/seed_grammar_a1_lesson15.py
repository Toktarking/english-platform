from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 15: "
        "There is / There are."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=15,
            defaults={
                "title": "Конструкция THERE IS / THERE ARE",
                "slug": "there-is-there-are",
                "theory_text": "There is / There are.",
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что означает THERE IS / THERE ARE",
                "body": """There is / there are используется, когда мы сообщаем, что:

где-то что-то есть;

где-то кто-то находится;

существует предмет, человек или явление.

Примеры:

There is a book on the table.

There are three students in the room.

There is some milk in the fridge.

Важно:

there в этой конструкции обычно не переводится буквально как «там».

Вся конструкция означает:

есть;
находится;
имеется.""",
            },

            {
                "order": 2,
                "title": "Когда используется THERE IS",
                "body": """There is используется, если после конструкции стоит:

один предмет;

один человек;

неисчисляемое существительное.

Примеры:

There is a chair in the room.

There is a student at the door.

There is some water in the bottle.

Также:

There is a problem.

There is a teacher in the classroom.

There is some milk in the fridge.""",
            },

            {
                "order": 3,
                "title": "Когда используется THERE ARE",
                "body": """There are используется, если после конструкции стоит существительное во множественном числе.

Примеры:

There are two books on the table.

There are many students in the classroom.

There are some apples in the bag.

There are no chairs in the room.

Запомните:

один предмет → there is

неисчисляемое → there is

несколько предметов → there are.""",
            },

            {
                "order": 4,
                "title": "Главная таблица",
                "body": """Сравните:

Один предмет:

There is a chair.

Один человек:

There is a teacher.

Неисчисляемое:

There is water.

Несколько предметов:

There are chairs.

Несколько людей:

There are students.

Коротко:

singular → there is

uncountable → there is

plural → there are.""",
            },

            {
                "order": 5,
                "title": "Порядок слов",
                "body": """Основная формула:

There is / There are
+
предмет или человек
+
место

Примеры:

There is a book on the table.

There are students in the room.

There is milk in the fridge.

Место можно поставить в начале:

On the table, there is a book.

Но для начинающего проще использовать основной порядок:

There is a book on the table.""",
            },

            {
                "order": 6,
                "title": "A / AN / SOME и числа",
                "body": """С одним исчисляемым существительным после there is обычно нужен определитель:

a;

an;

the;

my;

this.

Примеры:

There is a book on the table.

There is an apple in the bag.

Неправильно:

There is book on the table.

С множественным числом после there are можно использовать:

число;

some;

many;

a few;

no.

There are two books.

There are some students.

There are many trees.""",
            },

            {
                "order": 7,
                "title": "Неисчисляемые существительные",
                "body": """С неисчисляемыми существительными используется there is.

Можно использовать:

some;

much;

a little;

little;

no;

a lot of.

Примеры:

There is some water.

There is a little milk.

There is no information.

There is a lot of work.

Почему is?

Потому что неисчисляемые существительные грамматически обычно рассматриваются как единственное число.""",
            },

            {
                "order": 8,
                "title": "Отрицание",
                "body": """Отрицание строится при помощи not.

There is not...

There are not...

Сокращения:

there isn't;

there aren't.

Примеры:

There isn't a book on the table.

There isn't any milk.

There aren't any students in the room.

There aren't many cars outside.

Также можно использовать no:

There is no milk.

There are no students.

Сравните:

There isn't any milk.

There is no milk.

Значение одинаковое.""",
            },

            {
                "order": 9,
                "title": "Нельзя использовать двойное отрицание",
                "body": """Нельзя одновременно использовать not и no.

Неправильно:

There isn't no milk.

Правильно:

There isn't any milk.

Или:

There is no milk.

То же самое:

There aren't any students.

Или:

There are no students.""",
            },

            {
                "order": 10,
                "title": "Вопросы IS THERE / ARE THERE",
                "body": """Чтобы задать вопрос, is или are ставится перед there.

Утверждение:

There is a book on the table.

Вопрос:

Is there a book on the table?

Утверждение:

There are students in the room.

Вопрос:

Are there students in the room?

Формулы:

Is there + один предмет / неисчисляемое?

Are there + множественное число?

Примеры:

Is there a bank near here?

Is there any milk?

Are there any students?

Are there many shops nearby?""",
            },

            {
                "order": 11,
                "title": "Краткие ответы",
                "body": """На вопрос Is there...?:

Yes, there is.

No, there isn't.

На вопрос Are there...?:

Yes, there are.

No, there aren't.

Важно:

Is there a problem?

Правильно:

Yes, there is.

Не:

Yes, it is.

Если вопрос начинается с there, краткий ответ тоже содержит there.""",
            },

            {
                "order": 12,
                "title": "SOME и ANY",
                "body": """В утверждениях обычно используется some:

There are some books on the desk.

There is some juice in the fridge.

В вопросах обычно any:

Are there any books on the desk?

Is there any juice in the fridge?

В отрицаниях тоже any:

There aren't any books.

There isn't any juice.

Коротко:

утверждение → some

вопрос → any

отрицание → any.""",
            },

            {
                "order": 13,
                "title": "HOW MANY и HOW MUCH",
                "body": """HOW MANY используется с исчисляемыми существительными во множественном числе.

Формула:

How many + noun + are there?

Примеры:

How many students are there?

How many books are there?

How many rooms are there?

HOW MUCH используется с неисчисляемыми.

Формула:

How much + noun + is there?

Примеры:

How much water is there?

How much money is there?

How much time is there?

Нельзя:

How many are there students?

How much is there water?""",
            },

            {
                "order": 14,
                "title": "THERE IS / ARE, HAVE / HAS и IT / THEY",
                "body": """There is / there are сообщает о наличии или местонахождении.

There is a car outside.
— Снаружи стоит машина.

Have / has показывает принадлежность:

I have a car.
— У меня есть машина.

Сравните:

There are two children in the garden.

They have two children.

Также there is / are часто используется при первом упоминании:

There is a book on the table.

После этого можно использовать it:

It is very interesting.

Множественное число:

There are two books on the table.

They are mine.

Если после конструкции несколько существительных, для начального уровня можно ориентироваться на первое:

There is a book and two pens.

There are two books and a pen.""",
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
                "prompt": "There ___ a teacher in the classroom.",
                "options": ["are", "is", "am", "have"],
                "answer": "is",
                "explanation": "Teacher — один человек, поэтому there is.",
            },

            {
                "order": 2,
                "prompt": "There ___ many students in the classroom.",
                "options": ["is", "are", "am", "has"],
                "answer": "are",
                "explanation": "Students — множественное число, поэтому there are.",
            },

            {
                "order": 3,
                "prompt": "There ___ some coffee in the cup.",
                "options": ["are", "is", "be", "have"],
                "answer": "is",
                "explanation": "Coffee — неисчисляемое существительное.",
            },

            {
                "order": 4,
                "prompt": "There ___ a few apples in the bag.",
                "options": ["is", "are", "am", "has"],
                "answer": "are",
                "explanation": "Apples — множественное число.",
            },

            {
                "order": 5,
                "prompt": "___ there a hospital near here?",
                "options": ["Are", "Is", "Do", "Does"],
                "answer": "Is",
                "explanation": "Hospital — один объект: Is there...?",
            },

            {
                "order": 6,
                "prompt": "___ there any shops nearby?",
                "options": ["Is", "Are", "Do", "Does"],
                "answer": "Are",
                "explanation": "Shops — множественное число.",
            },

            {
                "order": 7,
                "prompt": "There isn't ___ sugar.",
                "options": ["some", "any", "many", "a few"],
                "answer": "any",
                "explanation": "В отрицании обычно используется any.",
            },

            {
                "order": 8,
                "prompt": "There aren't ___ chairs.",
                "options": ["any", "much", "a little", "an"],
                "answer": "any",
                "explanation": "Chairs — множественное число; в отрицании используется any.",
            },

            {
                "order": 9,
                "prompt": "There is ___ water in the bottle.",
                "options": ["a few", "some", "many", "several"],
                "answer": "some",
                "explanation": "Water — неисчисляемое, в утверждении подходит some.",
            },

            {
                "order": 10,
                "prompt": "There are ___ books on the shelf.",
                "options": ["some", "much", "a little", "an"],
                "answer": "some",
                "explanation": "Books — множественное число; some подходит.",
            },

            {
                "order": 11,
                "prompt": "How many rooms ___ there in the house?",
                "options": ["is", "are", "do", "does"],
                "answer": "are",
                "explanation": "How many + plural noun + are there?",
            },

            {
                "order": 12,
                "prompt": "How much money ___ there in the bag?",
                "options": ["are", "is", "do", "does"],
                "answer": "is",
                "explanation": "Money — неисчисляемое: How much money is there?",
            },

            {
                "order": 13,
                "prompt": "Is there a problem?",
                "options": [
                    "Yes, there is.",
                    "Yes, it is.",
                    "Yes, there are.",
                    "Yes, it does.",
                ],
                "answer": "Yes, there is.",
                "explanation": "В кратком ответе сохраняется there.",
            },

            {
                "order": 14,
                "prompt": "Are there any questions?",
                "options": [
                    "No, there isn't.",
                    "No, there aren't.",
                    "No, they aren't.",
                    "No, it isn't.",
                ],
                "answer": "No, there aren't.",
                "explanation": "Вопрос Are there...? → No, there aren't.",
            },

            {
                "order": 15,
                "prompt": "There ___ a book and two pens on the table.",
                "options": ["is", "are", "am", "have"],
                "answer": "is",
                "explanation": "Первым после конструкции стоит a book, поэтому для начального уровня используем there is.",
            },

            {
                "order": 16,
                "prompt": "There ___ two books and a pen on the table.",
                "options": ["is", "are", "am", "has"],
                "answer": "are",
                "explanation": "Первым стоит множественное two books.",
            },

            {
                "order": 17,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "There is book on the table.",
                    "There are a book on the table.",
                    "There is a book on the table.",
                    "There have a book on the table.",
                ],
                "answer": "There is a book on the table.",
                "explanation": "С одним исчисляемым существительным нужен there is + a/an.",
            },

            {
                "order": 18,
                "prompt": "Choose the correct negative sentence.",
                "options": [
                    "There isn't no milk.",
                    "There isn't any milk.",
                    "There don't have milk.",
                    "There isn't some milk.",
                ],
                "answer": "There isn't any milk.",
                "explanation": "Нельзя использовать двойное отрицание isn't + no.",
            },

            {
                "order": 19,
                "prompt": "Choose the equivalent sentence: 'There isn't any milk.'",
                "options": [
                    "There are no milk.",
                    "There is no milk.",
                    "There doesn't milk.",
                    "There is not no milk.",
                ],
                "answer": "There is no milk.",
                "explanation": "Not any и no могут передавать одинаковое отсутствие.",
            },

            {
                "order": 20,
                "prompt": "___ there any information in the report?",
                "options": ["Are", "Is", "Do", "Does"],
                "answer": "Is",
                "explanation": "Information — неисчисляемое, поэтому Is there...?",
            },

            {
                "order": 21,
                "prompt": "How many students ___ there in your group?",
                "options": ["is", "are", "do", "does"],
                "answer": "are",
                "explanation": "Students — множественное число.",
            },

            {
                "order": 22,
                "prompt": "Choose the sentence about location, not possession.",
                "options": [
                    "I have a car.",
                    "She has a phone.",
                    "There is a car outside.",
                    "They have two children.",
                ],
                "answer": "There is a car outside.",
                "explanation": "There is сообщает о наличии или местонахождении, а have/has — о принадлежности.",
            },

            {
                "order": 23,
                "prompt": "There are two books on the table. ___ are mine.",
                "options": ["It", "They", "There", "These is"],
                "answer": "They",
                "explanation": "После первого упоминания множественное books можно заменить на they.",
            },

            {
                "order": 24,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "There's two people outside.",
                    "There are two people outside.",
                    "There is two people outside.",
                    "There have two people outside.",
                ],
                "answer": "There are two people outside.",
                "explanation": "Для правильного тестового английского с plural используется there are.",
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
                "✅ A1 Lesson 15 seeded: "
                "THERE IS / THERE ARE"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
