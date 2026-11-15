from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive "
        "A1 Grammar Lesson 4."
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
                order=4,
                defaults={
                    "title":
                        "Исчисляемые и неисчисляемые существительные",

                    "slug":
                        "countable-uncountable-nouns",

                    "theory_text":
                        "Countable and uncountable nouns.",

                    "estimated_minutes":
                        18,

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
        # 10 MICRO-RULES
        # =================================================

        sections = [

            {
                "order": 1,

                "title":
                    "Countable или uncountable?",

                "body":
                    """В английском существительные делятся на две важные группы.

COUNTABLE — исчисляемые:

book
chair
student
apple

Их можно посчитать:

one book
two books
three books

UNCOUNTABLE — неисчисляемые:

water
money
information
advice

Их обычно нельзя считать напрямую как отдельные предметы.

От типа существительного зависит выбор артикля и слов количества.""",
            },


            {
                "order": 2,

                "title":
                    "Исчисляемые существительные",

                "body":
                    """Исчисляемые существительные имеют единственное и множественное число:

a book → books
a car → cars
an apple → apples

Один исчисляемый предмет обычно нельзя оставить без определителя.

Нельзя:

I have book.

Можно:

I have a book.
I have the book.
I have my book.

С countable nouns используются:

a / an
many
a few
several.""",
            },


            {
                "order": 3,

                "title":
                    "Как образовать множественное число",

                "body":
                    """Обычно добавляем -s:

book → books
car → cars
student → students

После некоторых окончаний добавляется -es:

bus → buses
class → classes
dish → dishes
watch → watches
box → boxes
tomato → tomatoes

Если слово заканчивается на согласную + y:

city → cities
baby → babies
country → countries

Но после гласной + y:

boy → boys
toy → toys
day → days.""",
            },


            {
                "order": 4,

                "title":
                    "Неправильное множественное число",

                "body":
                    """Некоторые слова имеют особую форму:

man → men
woman → women
child → children
person → people
foot → feet
tooth → teeth
mouse → mice

Не говорим:

childs
womans

Некоторые формы вообще не меняются:

one sheep → two sheep

one fish → five fish.""",
            },


            {
                "order": 5,

                "title":
                    "Неисчисляемые существительные",

                "body":
                    """Uncountable nouns обычно нельзя считать напрямую.

Например:

water
milk
money
information
advice
furniture
work
knowledge
music
love

С ними обычно нельзя использовать A / AN:

не:
an information
an advice
a furniture

а:

information
advice
furniture

Также у них обычно нет обычной формы множественного числа:

не:
informations
advices
furnitures

а:

information
advice
furniture.""",
            },


            {
                "order": 6,

                "title":
                    "Information, news, homework и другие ловушки",

                "body":
                    """Особенно важно запомнить:

information
advice
knowledge
news
research

work
homework
housework

money
furniture
equipment
luggage
baggage

Они обычно неисчисляемые.

Правильно:

some information
useful advice
a lot of homework
new furniture

NEWS заканчивается на -s, но обычно требует глагол в единственном числе:

The news is good.

Не:

The news are good.

WORK обычно неисчисляемое:

I have a lot of work.

Но JOB — исчисляемое:

I have a new job.
She has two jobs.""",
            },


            {
                "order": 7,

                "title":
                    "Еда, напитки и как их считать",

                "body":
                    """Многие продукты неисчисляемые:

bread
rice
sugar
salt
cheese
meat
butter

Жидкости тоже обычно неисчисляемые:

water
milk
coffee
tea
juice
oil

Но можно считать упаковки, порции и части:

a glass of water
two bottles of milk

a piece of advice
three pieces of information

a loaf of bread
a slice of bread
a cup of tea
a bowl of rice
a kilo of sugar
a bottle of oil

Мы считаем glass, bottle, piece, loaf — а не само неисчисляемое слово.""",
            },


            {
                "order": 8,

                "title":
                    "Одно слово может быть countable и uncountable",

                "body":
                    """Иногда тип существительного зависит от значения.

COFFEE

I like coffee.
кофе как напиток

Two coffees, please.
две чашки кофе

CHICKEN

There is a chicken in the garden.
одна курица

We ate chicken for dinner.
куриное мясо

PAPER

Paper is made from wood.
материал

I read a paper.
статья или документ

HAIR

Her hair is long.
волосы как масса

I found a hair.
один волос

EXPERIENCE

She has a lot of experience.
опыт

It was an interesting experience.
отдельное событие.""",
            },


            {
                "order": 9,

                "title":
                    "Many, much, a few, a little",

                "body":
                    """С COUNTABLE во множественном числе:

many books
many students

a few friends
a few chairs

С UNCOUNTABLE:

much money
much time
much information

a little water
a little time

Сравни:

How many students are there?

How much money do you need?

A few означает «несколько».

A little означает «немного».

Few и little без A обычно подчёркивают, что количества очень мало:

few friends
little time.""",
            },


            {
                "order": 10,

                "title":
                    "Some, any и a lot of",

                "body":
                    """Некоторые слова подходят и к countable, и к uncountable nouns.

A LOT OF:

a lot of books
a lot of money

SOME:

some books
some water
some information

ANY часто встречается в вопросах и отрицаниях:

Do you have any books?

Do you have any money?

We don't have any chairs.

There isn't any milk.

Главный алгоритм:

Можно посчитать отдельными единицами?

Да → countable.

Нет → обычно uncountable.

И не переводи буквально с русского:

советы → advice
информация → information
мебель → furniture
домашняя работа → homework.""",
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
                    "Какое слово исчисляемое?",

                "options": [
                    "information",
                    "advice",
                    "book",
                    "money",
                ],

                "answer":
                    "book",

                "explanation":
                    "Book можно посчитать: one book, two books.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "Какое слово неисчисляемое?",

                "options": [
                    "chair",
                    "student",
                    "apple",
                    "furniture",
                ],

                "answer":
                    "furniture",

                "explanation":
                    "Furniture обычно неисчисляемое.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "I have ___ new book.",

                "options": [],

                "answer":
                    "a",

                "explanation":
                    "Book — исчисляемое существительное в единственном числе.",
            },


            {
                "order": 4,
                "section": 3,
                "type": "choice",

                "prompt":
                    "Выбери правильное множественное число: city → ?",

                "options": [
                    "citys",
                    "cities",
                    "cityes",
                    "citis",
                ],

                "answer":
                    "cities",

                "explanation":
                    "После согласной + y: y меняется на i + es.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "Выбери правильное множественное число: box → ?",

                "options": [
                    "boxs",
                    "boxes",
                    "boxies",
                    "boxen",
                ],

                "answer":
                    "boxes",

                "explanation":
                    "После -x обычно добавляется -es.",
            },


            {
                "order": 6,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Выбери правильное множественное число: child → ?",

                "options": [
                    "childs",
                    "childes",
                    "children",
                    "childrens",
                ],

                "answer":
                    "children",

                "explanation":
                    "Child имеет неправильную форму children.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "build",

                "prompt":
                    "Собери правильное выражение.",

                "options": [
                    "two",
                    "women",
                ],

                "answer":
                    "two women",

                "explanation":
                    "Woman → women.",
            },


            {
                "order": 8,
                "section": 5,
                "type": "choice",

                "prompt":
                    "I need ___ information.",

                "options": [
                    "an",
                    "a",
                    "some",
                    "many",
                ],

                "answer":
                    "some",

                "explanation":
                    "Information неисчисляемое. Правильно: some information.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Выбери правильный вариант.",

                "options": [
                    "two advices",
                    "an advice",
                    "some advice",
                    "many advice",
                ],

                "answer":
                    "some advice",

                "explanation":
                    "Advice — неисчисляемое существительное.",
            },


            {
                "order": 10,
                "section": 6,
                "type": "choice",

                "prompt":
                    "The news ___ good.",

                "options": [
                    "are",
                    "is",
                    "have",
                    "were",
                ],

                "answer":
                    "is",

                "explanation":
                    "News обычно грамматически используется как единственное число.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "The teacher gave us ___ homework.",

                "options": [
                    "many",
                    "an",
                    "some",
                    "a few",
                ],

                "answer":
                    "some",

                "explanation":
                    "Homework — неисчисляемое.",
            },


            {
                "order": 12,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I bought two ___ of bread.",

                "options": [
                    "breads",
                    "loaves",
                    "breades",
                    "bread",
                ],

                "answer":
                    "loaves",

                "explanation":
                    "Правильно: two loaves of bread.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "build",

                "prompt":
                    "Собери выражение «два совета».",

                "options": [
                    "two",
                    "pieces",
                    "of",
                    "advice",
                ],

                "answer":
                    "two pieces of advice",

                "explanation":
                    "Advice нельзя считать напрямую, поэтому используем pieces of advice.",
            },


            {
                "order": 14,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Какое предложение говорит о курином мясе?",

                "options": [
                    "There is a chicken in the garden.",
                    "We ate chicken for dinner.",
                    "Two chickens are outside.",
                    "A chicken is near the house.",
                ],

                "answer":
                    "We ate chicken for dinner.",

                "explanation":
                    "Chicken без артикля здесь означает мясо.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Какое предложение означает отдельное событие?",

                "options": [
                    "She has a lot of experience.",
                    "It was an interesting experience.",
                    "She has much experience.",
                    "Experience is important.",
                ],

                "answer":
                    "It was an interesting experience.",

                "explanation":
                    "Experience может быть исчисляемым, когда означает отдельное переживание или событие.",
            },


            {
                "order": 16,
                "section": 9,
                "type": "choice",

                "prompt":
                    "There are ___ students in the classroom.",

                "options": [
                    "much",
                    "many",
                    "little",
                    "a little",
                ],

                "answer":
                    "many",

                "explanation":
                    "Students — исчисляемое существительное во множественном числе.",
            },


            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "We don't have ___ time.",

                "options": [
                    "many",
                    "much",
                    "a few",
                    "several",
                ],

                "answer":
                    "much",

                "explanation":
                    "Time в значении времени — неисчисляемое.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "I have ___ friends here.",

                "options": [
                    "a few",
                    "a little",
                    "much",
                    "an",
                ],

                "answer":
                    "a few",

                "explanation":
                    "Friends — исчисляемое существительное во множественном числе.",
            },


            {
                "order": 19,
                "section": 9,
                "type": "choice",

                "prompt":
                    "We have ___ water left.",

                "options": [
                    "a few",
                    "a little",
                    "many",
                    "several",
                ],

                "answer":
                    "a little",

                "explanation":
                    "Water — неисчисляемое.",
            },


            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Какое выражение подходит и к books, и к money?",

                "options": [
                    "many",
                    "much",
                    "a few",
                    "a lot of",
                ],

                "answer":
                    "a lot of",

                "explanation":
                    "A lot of можно использовать и с countable, и с uncountable nouns.",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "Choose the countable noun.",

                "options": [
                    "equipment",
                    "luggage",
                    "job",
                    "knowledge",
                ],

                "answer":
                    "job",

                "explanation":
                    "Job можно посчитать: one job, two jobs.",
            },


            {
                "order": 22,

                "prompt":
                    "Choose the correct plural form: baby → ?",

                "options": [
                    "babys",
                    "babies",
                    "babyes",
                    "babyes",
                ],

                "answer":
                    "babies",

                "explanation":
                    "После согласной + y: y меняется на i + es.",
            },


            {
                "order": 23,

                "prompt":
                    "Choose the correct plural form: tooth → ?",

                "options": [
                    "tooths",
                    "toothes",
                    "teeth",
                    "tooth",
                ],

                "answer":
                    "teeth",

                "explanation":
                    "Tooth имеет неправильную форму множественного числа teeth.",
            },


            {
                "order": 24,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She gave me an advice.",
                    "She gave me some advice.",
                    "She gave me two advices.",
                    "She gave me many advice.",
                ],

                "answer":
                    "She gave me some advice.",

                "explanation":
                    "Advice — неисчисляемое существительное.",
            },


            {
                "order": 25,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "The news are interesting.",
                    "The news is interesting.",
                    "The news have interesting.",
                    "The news be interesting.",
                ],

                "answer":
                    "The news is interesting.",

                "explanation":
                    "News обычно требует глагол в единственном числе.",
            },


            {
                "order": 26,

                "prompt":
                    "We need three ___ of information.",

                "options": [
                    "informations",
                    "pieces",
                    "information",
                    "advices",
                ],

                "answer":
                    "pieces",

                "explanation":
                    "Правильно: three pieces of information.",
            },


            {
                "order": 27,

                "prompt":
                    "She has ___ experience as a teacher.",

                "options": [
                    "many",
                    "a lot of",
                    "a few",
                    "several",
                ],

                "answer":
                    "a lot of",

                "explanation":
                    "Experience в значении опыта обычно неисчисляемое.",
            },


            {
                "order": 28,

                "prompt":
                    "How ___ students are there, and how ___ water do we need?",

                "options": [
                    "many / much",
                    "much / many",
                    "many / many",
                    "much / much",
                ],

                "answer":
                    "many / much",

                "explanation":
                    "Students — countable plural, water — uncountable.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "a few chairs / a little milk",
                    "a little chairs / a few milk",
                    "much chairs / many milk",
                    "an chairs / a milk",
                ],

                "answer":
                    "a few chairs / a little milk",

                "explanation":
                    "A few используется с countable plural, a little — с uncountable.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "We bought a lot of furniture and some equipment.",
                    "We bought many furnitures and an equipment.",
                    "We bought a furniture and many equipments.",
                    "We bought furnitures and an equipment.",
                ],

                "answer":
                    "We bought a lot of furniture and some equipment.",

                "explanation":
                    "Furniture и equipment обычно неисчисляемые.",
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
                section["order"]
                for section in sections
            ],
        ).delete()


        self.stdout.write(
            self.style.SUCCESS(
                "✅ Interactive A1 Lesson 4 seeded"
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
