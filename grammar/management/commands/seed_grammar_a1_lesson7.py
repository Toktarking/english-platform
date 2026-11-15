from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 7: pronouns."
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
                order=7,
                defaults={
                    "title":
                        "Личные, объектные и "
                        "притяжательные местоимения",

                    "slug":
                        "personal-object-possessive-pronouns",

                    "theory_text":
                        "Personal, object and possessive pronouns.",

                    "estimated_minutes":
                        17,

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
                    "Зачем нужны местоимения?",

                "body":
                    """Местоимение заменяет имя или предмет, чтобы не повторять одно и то же слово.

Без местоимений:

Marat is a teacher.
Marat works at a university.

С местоимением:

Marat is a teacher.
He works at a university.

Ещё пример:

Aigul has a book.
She reads it every evening.

She заменяет Aigul.

It заменяет book.""",
            },


            {
                "order": 2,

                "title":
                    "Кто выполняет действие?",

                "body":
                    """Если местоимение выполняет действие, нужна форма подлежащего:

I
you
he
she
it
we
they

Примеры:

I work here.

He studies English.

She is a teacher.

We live in Karaganda.

They play football.

Перед обычным глаголом нельзя ставить объектную форму:

не:
Me work here.

а:
I work here.""",
            },


            {
                "order": 3,

                "title":
                    "HE, SHE, IT, WE, THEY",

                "body":
                    """HE используется для мужчины или мальчика:

Marat is a doctor.
He works at a hospital.

SHE — для женщины или девочки:

Aigul is a teacher.
She works at a school.

IT — для предметов и часто для животных, если пол неважен:

This is a book.
It is interesting.

IT также используется для:

погоды:
It is cold.

времени:
It is five o'clock.

расстояния:
It is five kilometres from here.

WE:

My wife and I → we

THEY:

Marat and Aigul → they

The books → they.""",
            },


            {
                "order": 4,

                "title":
                    "После глагола нужна объектная форма",

                "body":
                    """Если действие направлено на человека или предмет:

I → me
you → you
he → him
she → her
it → it
we → us
they → them

Сравни:

He works.
I know him.

She teaches.
I know her.

They live here.
I see them every day.

После глагола часто нужна именно объектная форма:

She knows me.

The teacher helps us.""",
            },


            {
                "order": 5,

                "title":
                    "После предлога тоже объектная форма",

                "body":
                    """После предлогов используется объектная форма:

with me

for him

about her

to us

from them

Примеры:

Come with me.

This gift is for him.

I spoke to her.

They talked about us.

Не:

with I
for he
to she.""",
            },


            {
                "order": 6,

                "title":
                    "MY, YOUR, HIS, HER, OUR, THEIR",

                "body":
                    """Если после местоимения идёт существительное, нужна притяжательная форма:

my book

your phone

his car

her family

its name

our house

their children

Примеры:

This is my book.

His car is new.

Her phone is expensive.

Our teacher speaks English.

The students opened their books.

Главный признак:

после MY / YOUR / HIS / HER / OUR / THEIR обычно стоит существительное.""",
            },


            {
                "order": 7,

                "title":
                    "HIS, HER и ITS — смотрим на владельца",

                "body":
                    """HIS выбираем, если владелец — мужчина:

Marat has a sister.
His sister is a teacher.

HER — если владелец женщина:

Aigul has a brother.
Her brother is a student.

Важно:

выбор зависит от владельца, а не от самого предмета.

ITS показывает принадлежность предмету или животному:

The dog is eating its food.

The company changed its name.

Не путай:

its = принадлежность

it's = it is / it has

The cat is in its box.

It's cold.""",
            },


            {
                "order": 8,

                "title":
                    "MY или MINE?",

                "body":
                    """Если существительное стоит после слова:

my book
your bag
her phone
our house
their car

Если существительное НЕ повторяется:

mine
yours
his
hers
ours
theirs

Сравни:

This is my book.

This book is mine.

This is her bag.

This bag is hers.

This is our house.

This house is ours.

Не:

mine book

А:

my book.""",
            },


            {
                "order": 9,

                "title":
                    "Главная таблица форм",

                "body":
                    """Запомни четыре позиции.

Подлежащее → объект → перед существительным → самостоятельно

I → me → my → mine

you → you → your → yours

he → him → his → his

she → her → her → hers

it → it → its

we → us → our → ours

they → them → their → theirs

Пример:

She works here.

I know her.

This is her bag.

The bag is hers.

Главный алгоритм:

до глагола → subject form

после глагола / предлога → object form

перед существительным → possessive adjective

без существительного → possessive pronoun.""",
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
                    "Marat is my friend. ___ works at a university.",

                "options": [
                    "Him",
                    "He",
                    "His",
                    "Her",
                ],

                "answer":
                    "He",

                "explanation":
                    "Marat выполняет действие, поэтому нужна форма HE.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "Aigul has a new phone. ___ uses it every day.",

                "options": [
                    "Her",
                    "She",
                    "Hers",
                    "Him",
                ],

                "answer":
                    "She",

                "explanation":
                    "Aigul выполняет действие, поэтому SHE.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "___ am learning English.",

                "options": [],

                "answer":
                    "I",

                "explanation":
                    "Перед глаголом нужна форма подлежащего I.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "My brother and I live together. ___ have a small flat.",

                "options": [
                    "Us",
                    "Our",
                    "We",
                    "Ours",
                ],

                "answer":
                    "We",

                "explanation":
                    "My brother and I = WE.",
            },


            {
                "order": 5,
                "section": 3,
                "type": "choice",

                "prompt":
                    "It's ten o'clock. What does IT describe here?",

                "options": [
                    "a man",
                    "time",
                    "a woman",
                    "ownership",
                ],

                "answer":
                    "time",

                "explanation":
                    "IT используется для обозначения времени.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "Marat and Aigul are teachers. ___ work at the same school.",

                "options": [
                    "Them",
                    "Their",
                    "They",
                    "Theirs",
                ],

                "answer":
                    "They",

                "explanation":
                    "Marat and Aigul = THEY.",
            },


            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "I know Marat. I see ___ every day.",

                "options": [
                    "he",
                    "his",
                    "him",
                    "hers",
                ],

                "answer":
                    "him",

                "explanation":
                    "После SEE нужна объектная форма HIM.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "fill",

                "prompt":
                    "The teacher helps ___. Мы получаем помощь.",

                "options": [],

                "answer":
                    "us",

                "explanation":
                    "После helps нужна объектная форма US.",
            },


            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Come with ___.",

                "options": [
                    "I",
                    "my",
                    "mine",
                    "me",
                ],

                "answer":
                    "me",

                "explanation":
                    "После WITH используется объектная форма ME.",
            },


            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "I spoke to Aigul. I spoke to ___.",

                "options": [
                    "she",
                    "her",
                    "hers",
                    "their",
                ],

                "answer":
                    "her",

                "explanation":
                    "После TO используется объектная форма HER.",
            },


            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "These students opened ___ books.",

                "options": [
                    "them",
                    "they",
                    "their",
                    "theirs",
                ],

                "answer":
                    "their",

                "explanation":
                    "Перед существительным BOOKS используется THEIR.",
            },


            {
                "order": 12,
                "section": 6,
                "type": "fill",

                "prompt":
                    "My wife and I have a child. ___ child is one year old.",

                "options": [],

                "answer":
                    "our",

                "explanation":
                    "Перед существительным CHILD используется OUR.",
            },


            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Marat has a sister. ___ sister is a teacher.",

                "options": [
                    "Her",
                    "His",
                    "Him",
                    "Its",
                ],

                "answer":
                    "His",

                "explanation":
                    "Владелец — Marat, поэтому HIS.",
            },


            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "The dog is eating ___ food.",

                "options": [
                    "it's",
                    "its",
                    "it",
                    "their",
                ],

                "answer":
                    "its",

                "explanation":
                    "ITS показывает принадлежность. IT'S = IT IS / IT HAS.",
            },


            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "This is my phone. The phone is ___.",

                "options": [
                    "my",
                    "mine",
                    "me",
                    "I",
                ],

                "answer":
                    "mine",

                "explanation":
                    "Существительное PHONE уже не повторяется, поэтому MINE.",
            },


            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "This bag belongs to Aigul. It is ___.",

                "options": [
                    "her",
                    "hers",
                    "she",
                    "him",
                ],

                "answer":
                    "hers",

                "explanation":
                    "Существительное не повторяется, поэтому HERS.",
            },


            {
                "order": 17,
                "section": 8,
                "type": "build",

                "prompt":
                    "Собери правильное предложение.",

                "options": [
                    "This",
                    "book",
                    "is",
                    "mine",
                ],

                "answer":
                    "This book is mine",

                "explanation":
                    "MINE используется самостоятельно, без существительного после него.",
            },


            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct sequence for SHE.",

                "options": [
                    "she → her → her → hers",
                    "she → hers → her → him",
                    "her → she → hers → her",
                    "she → him → his → hers",
                ],

                "answer":
                    "she → her → her → hers",

                "explanation":
                    "Правильная система: SHE → HER → HER → HERS.",
            },


            {
                "order": 19,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "Me know him.",
                    "I know him.",
                    "My know he.",
                    "Mine know his.",
                ],

                "answer":
                    "I know him.",

                "explanation":
                    "Перед глаголом нужна форма I, после глагола — HIM.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "our house / the house is ours",
                    "ours house / the house is our",
                    "us house / the house is we",
                    "we house / the house is us",
                ],

                "answer":
                    "our house / the house is ours",

                "explanation":
                    "OUR стоит перед существительным, OURS используется самостоятельно.",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "My father is a doctor. ___ works at a hospital.",

                "options": [
                    "Him",
                    "He",
                    "His",
                    "Hers",
                ],

                "answer":
                    "He",

                "explanation":
                    "Отец выполняет действие, поэтому HE.",
            },


            {
                "order": 22,

                "prompt":
                    "My friends invited ___ to dinner.",

                "options": [
                    "I",
                    "my",
                    "me",
                    "mine",
                ],

                "answer":
                    "me",

                "explanation":
                    "После invited нужна объектная форма ME.",
            },


            {
                "order": 23,

                "prompt":
                    "The students are in the classroom. The teacher is speaking to ___.",

                "options": [
                    "they",
                    "their",
                    "theirs",
                    "them",
                ],

                "answer":
                    "them",

                "explanation":
                    "После предлога TO используется THEM.",
            },


            {
                "order": 24,

                "prompt":
                    "Aigul has a brother. ___ brother studies medicine.",

                "options": [
                    "His",
                    "Her",
                    "Hers",
                    "She",
                ],

                "answer":
                    "Her",

                "explanation":
                    "Владелец — Aigul, поэтому HER.",
            },


            {
                "order": 25,

                "prompt":
                    "The company changed ___ name.",

                "options": [
                    "it's",
                    "its",
                    "it",
                    "their",
                ],

                "answer":
                    "its",

                "explanation":
                    "ITS показывает принадлежность компании.",
            },


            {
                "order": 26,

                "prompt":
                    "Is this ___ phone?",

                "options": [
                    "you",
                    "your",
                    "yours",
                    "yourself",
                ],

                "answer":
                    "your",

                "explanation":
                    "Перед PHONE нужна форма YOUR.",
            },


            {
                "order": 27,

                "prompt":
                    "No, this phone isn't ___.",

                "options": [
                    "my",
                    "mine",
                    "me",
                    "I",
                ],

                "answer":
                    "mine",

                "explanation":
                    "После MINE существительное уже не нужно.",
            },


            {
                "order": 28,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "Her helps us.",
                    "She helps us.",
                    "Hers helps we.",
                    "She helps we.",
                ],

                "answer":
                    "She helps us.",

                "explanation":
                    "SHE выполняет действие, US получает действие.",
            },


            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "their car / the car is theirs",
                    "theirs car / the car is their",
                    "them car / the car is they",
                    "they car / the car is them",
                ],

                "answer":
                    "their car / the car is theirs",

                "explanation":
                    "THEIR используется перед существительным, THEIRS — самостоятельно.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "She knows him, and this is his book.",
                    "Her knows he, and this is him book.",
                    "She knows he, and this is him book.",
                    "Hers knows him, and this is he book.",
                ],

                "answer":
                    "She knows him, and this is his book.",

                "explanation":
                    "SHE — подлежащее, HIM — объект, HIS — принадлежность перед существительным.",
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
                "✅ Interactive A1 Lesson 7 seeded"
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
