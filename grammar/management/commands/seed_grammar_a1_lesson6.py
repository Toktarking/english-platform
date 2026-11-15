from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 6: Some, any, no and compounds."
    )


    def handle(
        self,
        *args,
        **options,
    ):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=6,
                defaults={
                    "title":
                        "Some, any, no и их производные",

                    "slug":
                        "some-any-no",

                    "theory_text":
                        "Some, any, no and compounds.",

                    "estimated_minutes":
                        16,

                    "pass_score":
                        70,

                    "xp_reward":
                        100,

                    "is_published":
                        True,
                },
            )
        )


        # =================================================
        # 9 MICRO-RULES
        # =================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Some, any или no?",

                "body":
                    """Эти слова показывают неопределённое количество.

SOME:

some books
some water

ANY:

any books
any water

NO:

no books
no water

Базовая схема:

утверждение → SOME

вопрос → ANY

отрицание с NOT → ANY

отрицание без NOT → NO

Сравни:

I have some books.

Do you have any books?

I don't have any books.

I have no books.""",
            },


            {
                "order": 2,

                "title":
                    "SOME — обычно в утверждениях",

                "body":
                    """SOME используется и с countable plural, и с uncountable nouns.

Countable:

some books
some students
some apples

Uncountable:

some water
some money
some information
some advice

Примеры:

I bought some apples.

We need some information.

She gave me some advice.""",
            },


            {
                "order": 3,

                "title":
                    "ANY — вопросы и отрицания",

                "body":
                    """ANY часто используется в обычных вопросах:

Do you have any questions?

Is there any milk?

Did you receive any information?

И в отрицаниях с NOT:

I don't have any money.

There aren't any books here.

We didn't receive any information.

Если отрицание уже выражено через NOT, обычно не добавляем NO.""",
            },


            {
                "order": 4,

                "title":
                    "Почему в вопросе иногда SOME?",

                "body":
                    """Вопрос не всегда требует ANY.

SOME часто используется, если мы:

предлагаем что-то;

просим что-то;

ожидаем положительный ответ.

Предложение:

Would you like some tea?

Do you want some coffee?

Просьба:

Can I have some water, please?

Could you give me some information?

Сравни:

Is there any coffee?
Просто спрашиваем, есть ли кофе.

Would you like some coffee?
Предлагаем кофе.""",
            },


            {
                "order": 5,

                "title":
                    "NO = NOT ANY",

                "body":
                    """NO означает полное отсутствие чего-либо.

I have no money.

There is no milk.

There are no students here.

Часто NO и NOT ANY дают одинаковый смысл:

I have no money.

I don't have any money.

Но нельзя использовать оба отрицания одновременно:

не:

I don't have no money.

а:

I don't have any money.

или:

I have no money.""",
            },


            {
                "order": 6,

                "title":
                    "Somebody, anybody, nobody",

                "body":
                    """Для людей:

somebody / someone
кто-то

anybody / anyone
кто-нибудь

nobody / no one
никто

Примеры:

Someone called you.

Is anybody at home?

I didn't see anybody.

Nobody knows the answer.

Важно:

NOBODY уже содержит отрицание.

Не:

Nobody doesn't know.

А:

Nobody knows.""",
            },


            {
                "order": 7,

                "title":
                    "Something, anything, nothing и места",

                "body":
                    """Для предметов, событий или действий:

something
что-то

anything
что-нибудь

nothing
ничего

Примеры:

I want something to eat.

Do you need anything?

I don't know anything.

I know nothing.

Для места:

somewhere
где-то / куда-то

anywhere
где-нибудь / куда-нибудь

nowhere
нигде / некуда

Примеры:

Let's go somewhere quiet.

Did you go anywhere?

We didn't go anywhere.

We have nowhere to go.""",
            },


            {
                "order": 8,

                "title":
                    "Everybody и порядок слов",

                "body":
                    """Полезная группа EVERY:

everybody / everyone
все

everything
всё

everywhere
везде

Everybody, everyone и everything грамматически обычно требуют единственное число:

Everybody is ready.

Everyone knows the answer.

Everything looks good.

Ещё одно важное правило:

после something, anything, nothing и похожих слов прилагательное ставится ПОСЛЕ.

something interesting

anything useful

nothing new

someone famous

Не:

interesting something.""",
            },


            {
                "order": 9,

                "title":
                    "ANY может означать «любой»",

                "body":
                    """ANY не всегда используется только в вопросах и отрицаниях.

В утвердительном предложении ANY может означать:

любой;
какой угодно;
где угодно.

You can choose any book.

Come any day next week.

Anyone can learn English.

You can sit anywhere.

Итоговая схема:

утверждение → SOME

вопрос → ANY

NOT → ANY

отрицание без NOT → NO

предложение / просьба → часто SOME

«любой» → ANY.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects
                .update_or_create(
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

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I bought ___ apples.",

                "options": [
                    "any",
                    "some",
                    "no",
                    "anything",
                ],

                "answer":
                    "some",

                "explanation":
                    "Обычное утвердительное предложение → SOME.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "Do you have ___ questions?",

                "options": [
                    "some",
                    "no",
                    "any",
                    "something",
                ],

                "answer":
                    "any",

                "explanation":
                    "Обычный вопрос → ANY.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "We need ___ information.",

                "options": [],

                "answer":
                    "some",

                "explanation":
                    "Утверждение с information → SOME.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "There are ___ students in the classroom.",

                "options": [
                    "some",
                    "any",
                    "nothing",
                    "anybody",
                ],

                "answer":
                    "some",

                "explanation":
                    "Это утвердительное предложение.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "Is there ___ milk in the fridge?",

                "options": [],

                "answer":
                    "any",

                "explanation":
                    "Обычный вопрос → ANY.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "We didn't receive ___ information.",

                "options": [
                    "some",
                    "any",
                    "no",
                    "nothing",
                ],

                "answer":
                    "any",

                "explanation":
                    "После DIDN'T используется ANY.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Would you like ___ tea?",

                "options": [
                    "any",
                    "some",
                    "no",
                    "anything",
                ],

                "answer":
                    "some",

                "explanation":
                    "Это предложение напитка, поэтому используем SOME.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Can I have ___ water, please?",

                "options": [
                    "any",
                    "some",
                    "no",
                    "nothing",
                ],

                "answer":
                    "some",

                "explanation":
                    "Это просьба, поэтому SOME.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "There is ___ milk in the fridge. It's empty.",

                "options": [
                    "some",
                    "any",
                    "no",
                    "anything",
                ],

                "answer":
                    "no",

                "explanation":
                    "NO показывает полное отсутствие молока.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I don't have no money.",
                    "I don't have any money.",
                    "I don't have nothing money.",
                    "I no have money.",
                ],

                "answer":
                    "I don't have any money.",

                "explanation":
                    "После отрицания DON'T используется ANY, а не NO.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Is ___ at the door?",

                "options": [
                    "something",
                    "anywhere",
                    "anybody",
                    "nothing",
                ],

                "answer":
                    "anybody",

                "explanation":
                    "Речь о человеке и это вопрос → ANYBODY.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "I didn't see ___.",

                "options": [
                    "nobody",
                    "anybody",
                    "somebody",
                    "everybody",
                ],

                "answer":
                    "anybody",

                "explanation":
                    "После DIDN'T используется ANYBODY.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "fill",

                "prompt":
                    "___ knows the answer. Никто не знает ответ.",

                "options": [],

                "answer":
                    "nobody",

                "explanation":
                    "NOBODY уже содержит отрицательное значение.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I'm hungry. I want ___ to eat.",

                "options": [
                    "anything",
                    "nothing",
                    "something",
                    "anywhere",
                ],

                "answer":
                    "something",

                "explanation":
                    "Обычное утверждение → SOMETHING.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "choice",

                "prompt":
                    "We didn't go ___ last weekend.",

                "options": [
                    "somewhere",
                    "nowhere",
                    "anywhere",
                    "everywhere",
                ],

                "answer":
                    "anywhere",

                "explanation":
                    "После DIDN'T используется ANYWHERE.",
            },


            {
                "order": 16,
                "section": 7,
                "type": "choice",

                "prompt":
                    "The bag is empty. There is ___ inside.",

                "options": [
                    "something",
                    "anything",
                    "nothing",
                    "somebody",
                ],

                "answer":
                    "nothing",

                "explanation":
                    "NOTHING уже означает «ничего».",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "___ is ready for the lesson.",

                "options": [
                    "Everybody",
                    "Anything",
                    "Nothing",
                    "Somewhere",
                ],

                "answer":
                    "Everybody",

                "explanation":
                    "Everybody означает «все» и требует IS.",
            },


            {
                "order": 18,
                "section": 8,
                "type": "build",

                "prompt":
                    "Собери правильное выражение.",

                "options": [
                    "something",
                    "interesting",
                ],

                "answer":
                    "something interesting",

                "explanation":
                    "Прилагательное ставится после SOMETHING.",
            },


            {
                "order": 19,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Choose the correct phrase.",

                "options": [
                    "new nothing",
                    "nothing new",
                    "nothing a new",
                    "no new nothing",
                ],

                "answer":
                    "nothing new",

                "explanation":
                    "Прилагательное ставится после NOTHING.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "You can choose ___ book you like.",

                "options": [
                    "some",
                    "any",
                    "no",
                    "nothing",
                ],

                "answer":
                    "any",

                "explanation":
                    "Здесь ANY означает «любую книгу».",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "There are ___ cookies on the table.",

                "options": [
                    "some",
                    "any",
                    "no one",
                    "anything",
                ],

                "answer":
                    "some",

                "explanation":
                    "Обычное утвердительное предложение → SOME.",
            },


            {
                "order": 22,

                "prompt":
                    "Are there ___ cookies left?",

                "options": [
                    "some",
                    "any",
                    "no",
                    "nothing",
                ],

                "answer":
                    "any",

                "explanation":
                    "Обычный вопрос → ANY.",
            },


            {
                "order": 23,

                "prompt":
                    "Would you like ___ cake?",

                "options": [
                    "some",
                    "any",
                    "no",
                    "nothing",
                ],

                "answer":
                    "some",

                "explanation":
                    "В предложении еды или напитка обычно используется SOME.",
            },


            {
                "order": 24,

                "prompt":
                    "Choose the sentence with the same meaning as 'There is no food.'",

                "options": [
                    "There isn't any food.",
                    "There isn't no food.",
                    "There is any food.",
                    "There isn't some food.",
                ],

                "answer":
                    "There isn't any food.",

                "explanation":
                    "NO и NOT ANY могут выражать одинаковое отрицание.",
            },


            {
                "order": 25,

                "prompt":
                    "Did ___ call while I was out?",

                "options": [
                    "somebody",
                    "anybody",
                    "nobody",
                    "nothing",
                ],

                "answer":
                    "anybody",

                "explanation":
                    "Обычный вопрос о человеке → ANYBODY.",
            },


            {
                "order": 26,

                "prompt":
                    "___ came to the meeting. The room was empty.",

                "options": [
                    "Anybody",
                    "Somebody",
                    "Nobody",
                    "Everybody",
                ],

                "answer":
                    "Nobody",

                "explanation":
                    "NOBODY означает «никто» и не требует NOT.",
            },


            {
                "order": 27,

                "prompt":
                    "I don't need ___ from the shop.",

                "options": [
                    "nothing",
                    "anything",
                    "something",
                    "nowhere",
                ],

                "answer":
                    "anything",

                "explanation":
                    "После DON'T используется ANYTHING.",
            },


            {
                "order": 28,

                "prompt":
                    "Let's go ___ quiet this weekend.",

                "options": [
                    "somewhere",
                    "anywhere",
                    "nowhere",
                    "anything",
                ],

                "answer":
                    "somewhere",

                "explanation":
                    "Утвердительное предложение о неопределённом месте → SOMEWHERE.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "Everybody are ready.",
                    "Everybody is ready.",
                    "Everybody be ready.",
                    "Everybody am ready.",
                ],

                "answer":
                    "Everybody is ready.",

                "explanation":
                    "Everybody грамматически требует глагол в единственном числе.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "You can choose any book, and I can recommend something interesting.",
                    "You can choose some book, and I can recommend interesting something.",
                    "You can choose no book, and I can recommend anything interestingly.",
                    "You can choose nothing book, and I can recommend some interesting.",
                ],

                "answer":
                    "You can choose any book, and I can recommend something interesting.",

                "explanation":
                    "ANY означает «любой», а после SOMETHING прилагательное ставится после него.",
            },

        ]


        valid_orders = []


        for data in (
            training
            +
            final_test
        ):

            valid_orders.append(
                data["order"]
            )


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
                "✅ Interactive A1 Lesson 6 seeded"
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
