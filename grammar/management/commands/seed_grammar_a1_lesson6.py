from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 6: "
        "Some, any, no and compounds."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=6,
            defaults={
                "title": (
                    "Some, any, no и их производные"
                ),
                "slug": "some-any-no",
                "theory_text": (
                    "Some, any, no and compounds."
                ),
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Some, any и no",
                "body": """Эти слова помогают говорить о неопределённом количестве людей, предметов или вещества.

Some — немного, несколько, какие-то.

Any — какие-нибудь, сколько-нибудь, никакие.

No — никакой, ни один, нисколько.

Сравните:

I have some books.
— У меня есть несколько книг.

Do you have any books?
— У тебя есть какие-нибудь книги?

I have no books.
— У меня нет книг.""",
            },

            {
                "order": 2,
                "title": "Когда используется some",
                "body": """Some чаще всего используется в утвердительных предложениях.

Оно употребляется:

с исчисляемыми существительными во множественном числе;

с неисчисляемыми существительными.

Примеры:

some books;
some students;
some apples;
some questions;

some water;
some money;
some information;
some advice.

Предложения:

I bought some apples.

There are some students in the classroom.

We need some information.

She gave me some advice.""",
            },

            {
                "order": 3,
                "title": "Когда используется any",
                "body": """Any чаще всего используется:

в вопросах;

в отрицательных предложениях.

Примеры:

any books;
any students;
any water;
any money;
any information.

Вопросы:

Do you have any questions?

Is there any milk in the fridge?

Did she give you any information?

Отрицания:

I do not have any money.

There are not any books on the table.

We did not receive any information.""",
            },

            {
                "order": 4,
                "title": "Some в вопросах",
                "body": """Обычно в вопросах используется any.

Но some часто используется, когда:

1. мы что-то предлагаем;
2. мы о чём-то просим;
3. ожидаем положительный ответ.

Предложение:

Would you like some tea?

Would you like some cake?

Do you want some coffee?

Просьба:

Can I have some water, please?

Could you give me some information?

Can you lend me some money?

Сравните:

Is there any coffee?
— Мы просто спрашиваем, есть ли кофе.

Would you like some coffee?
— Мы предлагаем кофе.""",
            },

            {
                "order": 5,
                "title": "No и not any",
                "body": """No означает полное отсутствие чего-либо.

Оно ставится непосредственно перед существительным.

Примеры:

no money;
no students;
no time;
no information.

I have no money.

There is no milk in the fridge.

There are no students in the classroom.

No и not any часто имеют одинаковое значение:

I have no money.

I do not have any money.

Оба предложения означают, что денег нет.""",
            },

            {
                "order": 6,
                "title": "Двойное отрицание",
                "body": """В стандартном английском обычно не используется двойное отрицание в одном простом предложении.

Неправильно:

I do not have no money.

Здесь одновременно:

do not
и
no.

Правильно:

I do not have any money.

Или:

I have no money.

То же правило действует с nobody, nothing и nowhere.""",
            },

            {
                "order": 7,
                "title": "Производные от some",
                "body": """От some образуются:

somebody — кто-то;

someone — кто-то;

something — что-то;

somewhere — где-то, куда-то.

Примеры:

Somebody is at the door.

Someone called you.

I want to eat something.

There is something in the box.

My keys are somewhere in the room.

Let us go somewhere quiet.""",
            },

            {
                "order": 8,
                "title": "Производные от any",
                "body": """От any образуются:

anybody — кто-нибудь;

anyone — кто-нибудь;

anything — что-нибудь;

anywhere — где-нибудь, куда-нибудь.

Они часто используются в вопросах и отрицаниях.

Is anybody at home?

Did anyone call me?

I do not know anybody here.

Do you want anything?

I did not see anything.

Did you go anywhere yesterday?

We did not go anywhere.""",
            },

            {
                "order": 9,
                "title": "Производные от no",
                "body": """От no образуются:

nobody — никто;

no one — никто;

nothing — ничего;

nowhere — нигде, никуда.

Эти слова уже имеют отрицательное значение.

Поэтому дополнительное not не нужно.

Правильно:

Nobody knows the answer.

No one came to the meeting.

I know nothing about this problem.

There is nothing in the bag.

We have nowhere to go.

Неправильно:

Nobody does not know the answer.""",
            },

            {
                "order": 10,
                "title": "Nothing и anything",
                "body": """Сравните:

I know nothing.

I do not know anything.

Оба предложения означают:

Я ничего не знаю.

Но нельзя смешивать две конструкции:

I do not know nothing. ❌

Правильно:

I do not know anything. ✅

или:

I know nothing. ✅

То же самое:

I saw nobody.

I did not see anybody.""",
            },

            {
                "order": 11,
                "title": "Everybody, everyone, everything, everywhere",
                "body": """Полезно знать производные от every:

everybody — все;

everyone — все;

everything — всё;

everywhere — везде.

Примеры:

Everybody is ready.

Everyone likes holidays.

Everything is fine.

I looked everywhere.

Важно:

Everybody, everyone и everything грамматически употребляются как единственное число.

Правильно:

Everybody is here.

Everyone knows the answer.

Everything looks good.

Неправильно:

Everybody are here.

Everyone know the answer.""",
            },

            {
                "order": 12,
                "title": "Прилагательное после something",
                "body": """После слов:

something;
anything;
nothing;
someone;
anybody

прилагательное обычно ставится после них.

Правильно:

something interesting;

nothing new;

someone famous;

anything useful.

Неправильно:

interesting something.

Правильно:

something interesting.""",
            },

            {
                "order": 13,
                "title": "Any в значении «любой»",
                "body": """Иногда any используется в утвердительном предложении.

Тогда оно означает:

любой;
любая;
любое;
где угодно.

Примеры:

You can choose any book.
— Ты можешь выбрать любую книгу.

Come any day next week.

Anyone can learn English.

You can sit anywhere.

То есть any не всегда означает только вопрос или отрицание.""",
            },

            {
                "order": 14,
                "title": "Как выбрать правильное слово",
                "body": """Шаг 1. Определите тип предложения.

Утверждение:

some;
somebody;
something;
somewhere.

Вопрос:

any;
anybody;
anything;
anywhere.

Отрицание с not:

any;
anybody;
anything;
anywhere.

Отрицание без not:

no;
nobody;
nothing;
nowhere.

Шаг 2. Определите значение.

Человек:

somebody;
anybody;
nobody.

Предмет или действие:

something;
anything;
nothing.

Место:

somewhere;
anywhere;
nowhere.

Количество перед существительным:

some;
any;
no.

И помните исключение:

в предложениях и просьбах в вопросе часто используется some.""",
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
                "prompt": "I bought ___ apples.",
                "options": ["any", "some", "no", "anything"],
                "answer": "some",
                "explanation": "Это обычное утвердительное предложение, поэтому используется some.",
            },

            {
                "order": 2,
                "prompt": "Do you have ___ questions?",
                "options": ["some", "no", "any", "something"],
                "answer": "any",
                "explanation": "Это обычный вопрос, поэтому используется any.",
            },

            {
                "order": 3,
                "prompt": "We do not have ___ information.",
                "options": ["some", "any", "no", "something"],
                "answer": "any",
                "explanation": "В предложении уже есть отрицание do not, поэтому используется any.",
            },

            {
                "order": 4,
                "prompt": "There is ___ milk in the fridge.",
                "options": ["no", "any", "anything", "somebody"],
                "answer": "no",
                "explanation": "No milk означает полное отсутствие молока без дополнительного not.",
            },

            {
                "order": 5,
                "prompt": "Would you like ___ tea?",
                "options": ["any", "no", "some", "anything"],
                "answer": "some",
                "explanation": "Это предложение напитка, поэтому в вопросе используется some.",
            },

            {
                "order": 6,
                "prompt": "Can I have ___ water, please?",
                "options": ["any", "some", "no", "anything"],
                "answer": "some",
                "explanation": "Это просьба, поэтому используется some.",
            },

            {
                "order": 7,
                "prompt": "Is ___ at the door?",
                "options": ["something", "anywhere", "anybody", "nothing"],
                "answer": "anybody",
                "explanation": "Речь идёт о человеке и это вопрос.",
            },

            {
                "order": 8,
                "prompt": "I did not see ___.",
                "options": ["nobody", "anybody", "somebody", "everybody"],
                "answer": "anybody",
                "explanation": "После did not нельзя использовать nobody, иначе получится двойное отрицание.",
            },

            {
                "order": 9,
                "prompt": "___ knows the answer.",
                "options": ["Anybody", "Nothing", "Nobody", "Anywhere"],
                "answer": "Nobody",
                "explanation": "Nobody уже содержит отрицательное значение и не требует not.",
            },

            {
                "order": 10,
                "prompt": "She told me ___.",
                "options": [
                    "interesting something",
                    "something interesting",
                    "anything interest",
                    "some interesting",
                ],
                "answer": "something interesting",
                "explanation": "Прилагательное ставится после something.",
            },

            {
                "order": 11,
                "prompt": "You can choose ___ seat.",
                "options": ["any", "no", "nobody", "somewhere"],
                "answer": "any",
                "explanation": "Здесь any означает «любой».",
            },

            {
                "order": 12,
                "prompt": "There are ___ books on the desk.",
                "options": ["some", "any", "no one", "anything"],
                "answer": "some",
                "explanation": "Это утвердительное предложение.",
            },

            {
                "order": 13,
                "prompt": "Are there ___ books on the desk?",
                "options": ["some", "any", "nothing", "somewhere"],
                "answer": "any",
                "explanation": "Это обычный вопрос.",
            },

            {
                "order": 14,
                "prompt": "There are not ___ books on the desk.",
                "options": ["some", "any", "no", "somebody"],
                "answer": "any",
                "explanation": "После отрицания not используется any.",
            },

            {
                "order": 15,
                "prompt": "There are ___ books on the desk. It is empty.",
                "options": ["some", "any", "no", "something"],
                "answer": "no",
                "explanation": "Стол пустой, поэтому there are no books.",
            },

            {
                "order": 16,
                "prompt": "Did ___ call me?",
                "options": ["somebody", "anybody", "nobody", "something"],
                "answer": "anybody",
                "explanation": "Это вопрос о человеке.",
            },

            {
                "order": 17,
                "prompt": "I did not tell ___ about the problem.",
                "options": ["nobody", "anybody", "somebody", "everybody"],
                "answer": "anybody",
                "explanation": "После did not используется anybody.",
            },

            {
                "order": 18,
                "prompt": "___ came to the lesson because the school was closed.",
                "options": ["Anybody", "Somebody", "Nobody", "Everybody"],
                "answer": "Nobody",
                "explanation": "Никто не пришёл; nobody уже содержит отрицание.",
            },

            {
                "order": 19,
                "prompt": "I am hungry. I want ___ to eat.",
                "options": ["anything", "nothing", "something", "anywhere"],
                "answer": "something",
                "explanation": "Это утвердительное предложение: something to eat.",
            },

            {
                "order": 20,
                "prompt": "There is ___ useful in this article.",
                "options": [
                    "useful something",
                    "something useful",
                    "some useful",
                    "useful anything",
                ],
                "answer": "something useful",
                "explanation": "Прилагательное useful ставится после something.",
            },

            {
                "order": 21,
                "prompt": "We did not go ___ during the weekend.",
                "options": ["somewhere", "nowhere", "anywhere", "everywhere"],
                "answer": "anywhere",
                "explanation": "После did not используется anywhere.",
            },

            {
                "order": 22,
                "prompt": "I looked ___, but I could not find my keys.",
                "options": ["everywhere", "nowhere", "something", "nobody"],
                "answer": "everywhere",
                "explanation": "Everywhere означает «везде».",
            },

            {
                "order": 23,
                "prompt": "___ is ready for the test.",
                "options": ["Everybody", "Anybody", "Nothing", "Somewhere"],
                "answer": "Everybody",
                "explanation": "Everybody означает «все» и требует глагол в единственном числе.",
            },

            {
                "order": 24,
                "prompt": "There is ___ in the box. The box is empty.",
                "options": ["something", "anything", "nothing", "somebody"],
                "answer": "nothing",
                "explanation": "Коробка пустая, поэтому there is nothing.",
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
                "✅ A1 Lesson 6 seeded: "
                "Some, any, no и их производные"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
