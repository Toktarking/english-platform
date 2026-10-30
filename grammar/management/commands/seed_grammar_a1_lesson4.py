from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 4: "
        "Countable and Uncountable Nouns."
    )

    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=4,
                defaults={
                    "title": (
                        "Исчисляемые и неисчисляемые "
                        "существительные"
                    ),
                    "slug": (
                        "countable-uncountable-nouns"
                    ),
                    "theory_text": (
                        "Countable and uncountable nouns."
                    ),
                    "estimated_minutes": 30,
                    "pass_score": 70,
                    "xp_reward": 100,
                    "is_published": True,
                },
            )
        )

        # ==================================================
        # THEORY
        # ==================================================

        sections = [

            {
                "order": 1,
                "title": (
                    "Исчисляемые и неисчисляемые "
                    "существительные"
                ),
                "body": """Существительное — это слово, которое называет человека, животное, предмет, место, явление, чувство или понятие.

Примеры:

teacher — учитель;
cat — кошка;
book — книга;
city — город;
rain — дождь;
love — любовь;
information — информация.

В английском языке существительные делятся на две важные группы:

1. countable nouns — исчисляемые;
2. uncountable nouns — неисчисляемые.

От этого зависит, какие артикли и слова количества можно использовать перед существительным.""",
            },

            {
                "order": 2,
                "title": "Исчисляемые существительные",
                "body": """Исчисляемое существительное обозначает предмет, который можно посчитать отдельно.

Например:

one book;
two books;
three books.

Также:

a chair;
two chairs;

a student;
five students;

an apple;
six apples.

Если предмет можно посчитать как отдельные единицы, существительное обычно исчисляемое.

Исчисляемые существительные имеют единственное и множественное число:

a book → books;
a car → cars;
a student → students;
an apple → apples.

В единственном числе обычное исчисляемое существительное нельзя просто оставить без определителя.

Неправильно:

I have book.

Правильно:

I have a book.
I have the book.
I have my book.""",
            },

            {
                "order": 3,
                "title": "Как образуется множественное число",
                "body": """Обычно к существительному добавляется -s:

book → books;
car → cars;
student → students.

После некоторых окончаний часто добавляется -es:

bus → buses;
class → classes;
dish → dishes;
watch → watches;
box → boxes;
tomato → tomatoes.

Если слово заканчивается на согласную + y:

city → cities;
baby → babies;
country → countries.

Но после гласной + y просто добавляется -s:

boy → boys;
toy → toys;
day → days.""",
            },

            {
                "order": 4,
                "title": "Неправильное множественное число",
                "body": """Некоторые существительные имеют особую форму множественного числа.

man → men;
woman → women;
child → children;
person → people;
foot → feet;
tooth → teeth;
mouse → mice.

Неправильно:

childs;
womans.

Некоторые формы не меняются:

one sheep → two sheep;
one fish → five fish.""",
            },

            {
                "order": 5,
                "title": "Неисчисляемые существительные",
                "body": """Неисчисляемое существительное обозначает то, что обычно не считают отдельными предметами.

Это могут быть:

жидкости;
вещества;
материалы;
абстрактные понятия;
информация;
деятельность.

Примеры:

water;
milk;
sugar;
rice;
money;
information;
advice;
work;
love;
happiness.

Нельзя сказать:

one water;
two informations;
three advices.

С неисчисляемыми существительными обычно нельзя использовать a/an.

Неправильно:

a water;
a money;
an information;
an advice;
a furniture.

Правильно:

water;
money;
information;
advice;
furniture.""",
            },

            {
                "order": 6,
                "title": (
                    "У неисчисляемых обычно нет "
                    "множественного числа"
                ),
                "body": """Обычно неисчисляемые существительные не имеют формы множественного числа.

Неправильно:

informations;
advices;
furnitures;
moneys;
knowledges.

Правильно:

information;
advice;
furniture;
money;
knowledge.

Примеры:

This information is useful.
Her advice was helpful.
The furniture is new.

Обратите внимание: такие слова часто требуют глагол в единственном числе.

The information is important.

The news is good.

Хотя news заканчивается на -s, грамматически это обычно единственное число.""",
            },

            {
                "order": 7,
                "title": (
                    "Важные неисчисляемые слова"
                ),
                "body": """Особенно важно запомнить следующие неисчисляемые существительные:

information;
knowledge;
news;
advice;
research;

work;
homework;
housework;

money;

furniture;
equipment;
luggage;
baggage.

Примеры:

I need some information.
She has a lot of knowledge.
The news is good.
He gave me useful advice.
The research is important.

I have a lot of work.
The teacher gave us homework.

Но job — исчисляемое:

a job;
two jobs.

Сравните:

I have a lot of work.
I have a new job.""",
            },

            {
                "order": 8,
                "title": "Еда и жидкости",
                "body": """Многие продукты неисчисляемые:

bread;
rice;
sugar;
salt;
cheese;
meat;
butter;
food.

Примеры:

We need some bread.
There is little sugar.
I do not eat much meat.

Но есть и исчисляемые продукты:

an apple;
a banana;
an egg;
a tomato;
a sandwich.

Жидкости обычно неисчисляемые:

water;
milk;
coffee;
tea;
juice;
oil.

I drink water.
She wants some coffee.
There is a little milk in the fridge.

В кафе можно услышать:

two coffees;
three teas.

Это сокращённо означает две чашки кофе или три чашки чая.""",
            },

            {
                "order": 9,
                "title": (
                    "Как считать неисчисляемые "
                    "существительные"
                ),
                "body": """Само неисчисляемое существительное нельзя считать напрямую, но можно считать его порции, упаковки или части.

Например:

a glass of water;
two glasses of water;

a bottle of milk;
three bottles of milk.

Можно считать glass или bottle, а не water или milk.

Очень полезно выражение piece of:

a piece of advice;
two pieces of advice;

a piece of information;
three pieces of information;

a piece of furniture;
a piece of news.

Другие примеры:

a loaf of bread;
a slice of bread;
a cup of tea;
a bowl of rice;
a kilo of sugar;
a bottle of oil;
a bar of chocolate;
a sheet of paper.""",
            },

            {
                "order": 10,
                "title": (
                    "Слова, которые могут быть "
                    "исчисляемыми и неисчисляемыми"
                ),
                "body": """Некоторые слова могут быть и исчисляемыми, и неисчисляемыми — значение меняется.

COFFEE

I like coffee.
— кофе как напиток вообще.

Two coffees, please.
— две чашки кофе.

CHICKEN

There is a chicken in the garden.
— одна курица.

We ate chicken for dinner.
— куриное мясо.

PAPER

Paper is made from wood.
— бумага как материал.

I read a paper this morning.
— статья, документ или газета.

HAIR

Her hair is long.
— волосы как масса.

I found a hair on my jacket.
— один волос.

EXPERIENCE

She has a lot of experience.
— опыт вообще.

It was an interesting experience.
— отдельное событие.

TIME

I do not have much time.
— время.

I have visited London three times.
— три раза.""",
            },

            {
                "order": 11,
                "title": "Many, much, a few и a little",
                "body": """MANY используется с исчисляемыми существительными во множественном числе:

many books;
many students;
many people.

How many students are there?

MUCH используется с неисчисляемыми:

much money;
much time;
much water;
much information.

How much money do you need?

A FEW используется с исчисляемыми:

a few books;
a few friends.

A LITTLE используется с неисчисляемыми:

a little water;
a little time.

Сравните:

I have a few friends.
We have a little time.""",
            },

            {
                "order": 12,
                "title": (
                    "Few / little и слова для обеих групп"
                ),
                "body": """Few и little означают, что чего-то очень мало.

few books — мало книг;
little water — мало воды.

A few / a little обычно звучат более положительно:

a few books — несколько книг;
a little water — немного воды.

Некоторые слова подходят к обеим группам.

A LOT OF:

a lot of books;
a lot of money.

SOME:

some books;
some water;
some information.

ANY часто используется в вопросах и отрицаниях:

Do you have any books?
Do you have any money?

We do not have any chairs.
There is not any milk.""",
            },

            {
                "order": 13,
                "title": (
                    "Как определить тип "
                    "существительного"
                ),
                "body": """Задайте простой вопрос:

Можно ли посчитать это как отдельные предметы?

Например:

one book;
two books.

Можно — значит book исчисляемое.

Но нельзя нормально сказать:

one information;
two advices;
three furnitures.

Значит, information, advice и furniture — неисчисляемые.

Важно не переводить буквально с русского.

В русском мы говорим:

советы;
сведения;
новости;
деньги;
мебель.

Но в английском обычно:

advice;
information;
news;
money;
furniture.

Все эти слова неисчисляемые.""",
            },

            {
                "order": 14,
                "title": (
                    "Главные правила и типичные ошибки"
                ),
                "body": """Запомните основные правила.

ИСЧИСЛЯЕМЫЕ:

можно посчитать;

one book;
two books;

используются:

a/an;
many;
a few.

НЕИСЧИСЛЯЕМЫЕ:

напрямую не считаются;

water;
money;
information;

обычно нельзя использовать a/an и множественное число;

используются:

much;
a little.

С ОБЕИМИ ГРУППАМИ:

a lot of;
some;
any.

Типичные ошибки:

an information ❌
some information ✅

two advices ❌
two pieces of advice ✅

many money ❌
much money / a lot of money ✅

many furnitures ❌
a lot of furniture ✅

many homeworks ❌
a lot of homework ✅

The news are good. ❌
The news is good. ✅""",
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


        # ==================================================
        # PRACTICE — 24 QUESTIONS
        # ==================================================

        exercises = [

            {
                "order": 1,
                "prompt": (
                    "Choose the countable noun."
                ),
                "options": [
                    "information",
                    "advice",
                    "book",
                    "money",
                ],
                "answer": "book",
                "explanation": (
                    "Book можно посчитать: "
                    "one book, two books."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "Choose the uncountable noun."
                ),
                "options": [
                    "chair",
                    "student",
                    "apple",
                    "furniture",
                ],
                "answer": "furniture",
                "explanation": (
                    "Furniture обычно "
                    "неисчисляемое."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "I need ___ information."
                ),
                "options": [
                    "an",
                    "a",
                    "some",
                    "many",
                ],
                "answer": "some",
                "explanation": (
                    "Information — неисчисляемое. "
                    "Правильно: some information."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "There are ___ students "
                    "in the classroom."
                ),
                "options": [
                    "much",
                    "many",
                    "little",
                    "a little",
                ],
                "answer": "many",
                "explanation": (
                    "Students — исчисляемое "
                    "существительное во "
                    "множественном числе."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "We do not have ___ money."
                ),
                "options": [
                    "many",
                    "a few",
                    "much",
                    "several",
                ],
                "answer": "much",
                "explanation": (
                    "Money — неисчисляемое, "
                    "поэтому используется much."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "She gave me ___ useful advice."
                ),
                "options": [
                    "an",
                    "a",
                    "some",
                    "many",
                ],
                "answer": "some",
                "explanation": (
                    "Advice — неисчисляемое."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "I bought two ___ of bread."
                ),
                "options": [
                    "breads",
                    "loaf",
                    "loaves",
                    "breades",
                ],
                "answer": "loaves",
                "explanation": (
                    "Правильно: two loaves "
                    "of bread."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "The news ___ surprising."
                ),
                "options": [
                    "are",
                    "were",
                    "is",
                    "have",
                ],
                "answer": "is",
                "explanation": (
                    "News обычно грамматически "
                    "употребляется как "
                    "единственное число."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "Choose the correct plural form."
                ),
                "options": [
                    "childs",
                    "childes",
                    "children",
                    "childrens",
                ],
                "answer": "children",
                "explanation": (
                    "Child имеет неправильную "
                    "форму множественного числа: "
                    "children."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "Choose the correct plural form "
                    "of 'city'."
                ),
                "options": [
                    "citys",
                    "cities",
                    "cityes",
                    "citis",
                ],
                "answer": "cities",
                "explanation": (
                    "Согласная + y: "
                    "y меняется на i + es."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "We have ___ time "
                    "before the lesson."
                ),
                "options": [
                    "a few",
                    "many",
                    "a little",
                    "several",
                ],
                "answer": "a little",
                "explanation": (
                    "Time в значении времени "
                    "неисчисляемое."
                ),
            },

            {
                "order": 12,
                "prompt": (
                    "She bought ___ new chairs."
                ),
                "options": [
                    "a few",
                    "a little",
                    "much",
                    "an",
                ],
                "answer": "a few",
                "explanation": (
                    "Chairs — исчисляемое "
                    "во множественном числе."
                ),
            },

            {
                "order": 13,
                "prompt": (
                    "The teacher gave us ___ homework."
                ),
                "options": [
                    "many",
                    "an",
                    "some",
                    "a few",
                ],
                "answer": "some",
                "explanation": (
                    "Homework — неисчисляемое."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "I heard ___ interesting news."
                ),
                "options": [
                    "an",
                    "a",
                    "some",
                    "many",
                ],
                "answer": "some",
                "explanation": (
                    "News — неисчисляемое."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "We need two ___ of information."
                ),
                "options": [
                    "informations",
                    "pieces",
                    "advices",
                    "information",
                ],
                "answer": "pieces",
                "explanation": (
                    "Правильно: two pieces "
                    "of information."
                ),
            },

            {
                "order": 16,
                "prompt": (
                    "She has ___ experience "
                    "as a teacher."
                ),
                "options": [
                    "many",
                    "a lot of",
                    "a few",
                    "several",
                ],
                "answer": "a lot of",
                "explanation": (
                    "Experience в значении "
                    "опыта обычно неисчисляемое."
                ),
            },

            {
                "order": 17,
                "prompt": (
                    "There are only ___ students "
                    "in the room, but they are enough."
                ),
                "options": [
                    "a little",
                    "little",
                    "a few",
                    "much",
                ],
                "answer": "a few",
                "explanation": (
                    "Students — исчисляемое "
                    "множественное число."
                ),
            },

            {
                "order": 18,
                "prompt": (
                    "Choose the correct sentence."
                ),
                "options": [
                    "I need an information.",
                    "I need an informations.",
                    "I need some information.",
                    "I need many information.",
                ],
                "answer": (
                    "I need some information."
                ),
                "explanation": (
                    "Information — неисчисляемое."
                ),
            },

            {
                "order": 19,
                "prompt": (
                    "Choose the correct sentence."
                ),
                "options": [
                    "She gave me two advices.",
                    "She gave me two pieces of advice.",
                    "She gave me an advice.",
                    "She gave me many advice.",
                ],
                "answer": (
                    "She gave me two pieces of advice."
                ),
                "explanation": (
                    "Advice нельзя считать напрямую. "
                    "Используем pieces of advice."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "Choose the correct sentence."
                ),
                "options": [
                    "We bought many furnitures.",
                    "We bought a furniture.",
                    "We bought a lot of furniture.",
                    "We bought furnitures.",
                ],
                "answer": (
                    "We bought a lot of furniture."
                ),
                "explanation": (
                    "Furniture — неисчисляемое."
                ),
            },

            {
                "order": 21,
                "prompt": (
                    "Which sentence means "
                    "'one separate event'?"
                ),
                "options": [
                    "She has a lot of experience.",
                    "It was an interesting experience.",
                    "She has much experiences.",
                    "She has an experience knowledge.",
                ],
                "answer": (
                    "It was an interesting experience."
                ),
                "explanation": (
                    "Experience может быть "
                    "исчисляемым, когда означает "
                    "отдельное событие."
                ),
            },

            {
                "order": 22,
                "prompt": (
                    "Which sentence is about "
                    "chicken meat?"
                ),
                "options": [
                    "There is a chicken in the garden.",
                    "We ate chicken for dinner.",
                    "There are two chickens outside.",
                    "A chicken is walking near the house.",
                ],
                "answer": (
                    "We ate chicken for dinner."
                ),
                "explanation": (
                    "Chicken без артикля здесь "
                    "означает куриное мясо."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct sentence."
                ),
                "options": [
                    "He has many money.",
                    "He has a few money.",
                    "He has a lot of money.",
                    "He has several money.",
                ],
                "answer": (
                    "He has a lot of money."
                ),
                "explanation": (
                    "Money — неисчисляемое. "
                    "A lot of подходит."
                ),
            },

            {
                "order": 24,
                "prompt": (
                    "Which option works with BOTH "
                    "countable and uncountable nouns?"
                ),
                "options": [
                    "many",
                    "much",
                    "a few",
                    "a lot of",
                ],
                "answer": "a lot of",
                "explanation": (
                    "A lot of можно использовать "
                    "и с countable, и с "
                    "uncountable nouns."
                ),
            },

        ]


        for data in exercises:

            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "exercise_type":
                        GrammarExercise.Type.CHOICE,

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


        self.stdout.write(
            self.style.SUCCESS(
                "✅ A1 Lesson 4 seeded: "
                "Исчисляемые и неисчисляемые "
                "существительные"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
