from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 57: "
        "Possessive Case."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=57,
            defaults={
                "title": "Притяжательный падеж существительных",
                "slug": "possessive-case",
                "theory_text": (
                    "Possessive Case: 's, apostrophe, of "
                    "and double possessive."
                ),
                "estimated_minutes": 45,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое притяжательный падеж",
                "body": """Притяжательный падеж показывает:

кому принадлежит предмет;

с кем или с чем он связан.

Обычно используется:

's

Примеры:

Tom's car

Anna's book

the teacher's desk

my brother's phone

Главная схема:

owner + 's + thing""",
            },

            {
                "order": 2,
                "title": "Один владелец: 'S",
                "body": """Если владелец стоит в единственном числе, обычно добавляется:

's

Примеры:

the girl's bag

the student's notebook

the doctor's office

my father's car

Порядок слов:

сначала владелец;

потом предмет.

Правильно:

Anna's phone

Не:

the phone's Anna""",
            },

            {
                "order": 3,
                "title": "Множественное число на -S",
                "body": """Если plural noun уже заканчивается на -s, добавляется только апостроф:

'

Примеры:

the students' books

the teachers' room

my parents' house

the workers' uniforms

Сравните:

the student's book
— книга одного студента

the students' books
— книги студентов""",
            },

            {
                "order": 4,
                "title": "Неправильное множественное число",
                "body": """Если plural noun НЕ заканчивается на -s, используется:

's

Примеры:

children's toys

men's clothes

women's shoes

people's opinions

Важно:

children уже plural.

Поэтому:

children's

Не:

childrens'

То же правило:

men's

women's

people's""",
            },

            {
                "order": 5,
                "title": "Имена на S",
                "body": """С именами, которые заканчиваются на S, встречаются два варианта:

James's car

James' car

В современном английском часто используется:

James's

Пример:

James's office is on the second floor.

Для учебных заданий удобно ориентироваться на:

name + 's

если инструкция не требует другого варианта.""",
            },

            {
                "order": 6,
                "title": "Общая и раздельная принадлежность",
                "body": """Если один предмет принадлежит двум людям вместе, 's ставится только у последнего имени.

Tom and Anna's house

= один общий дом.

Если у каждого свой предмет:

Tom's and Anna's cars

= у Тома своя машина и у Анны своя.

Сравните:

Jack and Emma's office
— один общий офис

Jack's and Emma's offices
— два разных офиса""",
            },

            {
                "order": 7,
                "title": "Люди, животные, организации, страны и время",
                "body": """'S особенно естественно используется с:

людьми;

животными;

организациями;

странами;

городами;

временем.

Примеры:

my sister's room

the dog's tail

the company's policy

Kazakhstan's economy

London's museums

today's meeting

tomorrow's lesson

next year's budget""",
            },

            {
                "order": 8,
                "title": "Периоды времени и расстояние",
                "body": """Possessive form используется с периодами времени.

Один период:

a day's work

a week's holiday

an hour's drive

Несколько периодов:

two days' work

three weeks' holiday

ten minutes' walk

two hours' journey

Если plural уже заканчивается на -s:

ставится только апостроф.""",
            },

            {
                "order": 9,
                "title": "Конструкция OF",
                "body": """OF часто используется с:

предметами;

частями вещей;

абстрактными понятиями;

длинными конструкциями.

Формула:

thing + of + owner

Примеры:

the door of the house

the roof of the building

the title of the article

the end of the road

С человеком чаще естественнее:

Anna's phone

С частью предмета:

the cover of the book""",
            },

            {
                "order": 10,
                "title": "'S или OF",
                "body": """С людьми обычно выбирайте 's:

my brother's car

а не:

the car of my brother

С предметами часто используется OF:

the door of the car

the roof of the building

С организациями и странами возможны оба варианта:

the company's policy

the policy of the company

Kazakhstan's economy

the economy of Kazakhstan""",
            },

            {
                "order": 11,
                "title": "A FRIEND OF MINE",
                "body": """Конструкция:

a/an + noun + of + possessive pronoun

Примеры:

a friend of mine

a colleague of hers

a neighbour of ours

a student of his

A friend of mine означает:

один из моих друзей.

Сравните:

my friend
— мой друг

a friend of mine
— один из моих друзей

Также возможно:

a friend of Tom's""",
            },

            {
                "order": 12,
                "title": "Существительное можно не повторять",
                "body": """Если предмет уже понятен, существительное после possessive form можно не повторять.

Примеры:

This book is Anna's.

That car is my brother's.

Is this pen yours or Kate's?

Также можно опустить название места:

at the doctor's

at the dentist's

at my parents'

Пример:

We are staying at my parents'.

= у моих родителей дома.""",
            },

            {
                "order": 13,
                "title": "Составные формы и артикль",
                "body": """Если владелец состоит из нескольких слов, 's ставится в конце всей группы.

Примеры:

my older brother's car

my mother-in-law's house

John Smith's office

someone else's bag

После possessive form перед предметом артикль не нужен.

Правильно:

my brother's car

Anna's phone

Неправильно:

my brother's the car

Anna's the phone""",
            },

            {
                "order": 14,
                "title": "Как выбрать форму",
                "body": """Один владелец?

→ 's

the girl's bag

Plural на -s?

→ только '

the girls' bags

Irregular plural?

→ 's

the children's bags

Один общий предмет у двух людей?

→ 's только у последнего

Tom and Anna's house

У каждого свой предмет?

→ 's у каждого

Tom's and Anna's cars

Предмет или часть предмета?

→ часто OF

the roof of the building

Один из группы?

→ a friend of mine""",
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
                "prompt": "This is the ___ office.",
                "options": [
                    "manager",
                    "manager's",
                    "managers",
                    "managers's",
                ],
                "answer": "manager's",
                "explanation": (
                    "Один владелец → 's."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "The ___ uniforms are new. "
                    "Речь о нескольких работниках."
                ),
                "options": [
                    "worker's",
                    "workers'",
                    "workers's",
                    "worker",
                ],
                "answer": "workers'",
                "explanation": (
                    "Plural workers уже заканчивается на -s → только apostrophe."
                ),
            },

            {
                "order": 3,
                "prompt": "The ___ clothes are upstairs.",
                "options": [
                    "mens",
                    "men's",
                    "mens'",
                    "men",
                ],
                "answer": "men's",
                "explanation": (
                    "Men — irregular plural → добавляем 's."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "We visited ___ house. "
                    "Один общий дом Джека и Эммы."
                ),
                "options": [
                    "Jack's and Emma's",
                    "Jack and Emma's",
                    "Jacks and Emma",
                    "Jack and Emmas'",
                ],
                "answer": "Jack and Emma's",
                "explanation": (
                    "Общая принадлежность → 's только у последнего имени."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "These are ___ offices. "
                    "У Анны и Марии разные офисы."
                ),
                "options": [
                    "Anna and Maria's",
                    "Anna's and Maria's",
                    "Annas' and Maria",
                    "Anna's and Maria",
                ],
                "answer": "Anna's and Maria's",
                "explanation": (
                    "Раздельная принадлежность → 's у каждого имени."
                ),
            },

            {
                "order": 6,
                "prompt": "The ___ decision was unexpected.",
                "options": [
                    "company",
                    "company's",
                    "companies",
                    "companys'",
                ],
                "answer": "company's",
                "explanation": (
                    "Одна компания → company's decision."
                ),
            },

            {
                "order": 7,
                "prompt": "The ___ population is growing.",
                "options": [
                    "city's",
                    "citys",
                    "cities",
                    "city'",
                ],
                "answer": "city's",
                "explanation": (
                    "Один город → city's."
                ),
            },

            {
                "order": 8,
                "prompt": "Tomorrow's lesson means:",
                "options": [
                    "урок вчера",
                    "сегодняшний урок",
                    "завтрашний урок",
                    "недельный урок",
                ],
                "answer": "завтрашний урок",
                "explanation": (
                    "Tomorrow's = относящийся к завтрашнему дню."
                ),
            },

            {
                "order": 9,
                "prompt": "A friend of ___ works here.",
                "options": [
                    "my",
                    "mine",
                    "me",
                    "I",
                ],
                "answer": "mine",
                "explanation": (
                    "Правильная конструкция: a friend of mine."
                ),
            },

            {
                "order": 10,
                "prompt": "The title ___ the article is unclear.",
                "options": [
                    "'s",
                    "of",
                    "from",
                    "for",
                ],
                "answer": "of",
                "explanation": (
                    "С частью/элементом предмета естественно: the title of the article."
                ),
            },

            {
                "order": 11,
                "prompt": "This is ___ bag.",
                "options": [
                    "someone else's",
                    "someone's else",
                    "someone else",
                    "someones else's",
                ],
                "answer": "someone else's",
                "explanation": (
                    "'s ставится в конце всей группы: someone else's."
                ),
            },

            {
                "order": 12,
                "prompt": "The ___ website has been updated.",
                "options": [
                    "university's",
                    "universities",
                    "universitys'",
                    "university",
                ],
                "answer": "university's",
                "explanation": (
                    "Организация может использовать possessive 's."
                ),
            },

            {
                "order": 13,
                "prompt": "We need two ___ work.",
                "options": [
                    "days",
                    "day's",
                    "days'",
                    "days's",
                ],
                "answer": "days'",
                "explanation": (
                    "Two days → plural ending in -s → days' work."
                ),
            },

            {
                "order": 14,
                "prompt": "This book is ___.",
                "options": [
                    "Anna",
                    "Annas",
                    "Anna's",
                    "Annas'",
                ],
                "answer": "Anna's",
                "explanation": (
                    "Существительное book можно не повторять: This book is Anna's."
                ),
            },

            {
                "order": 15,
                "prompt": "We are staying at my ___ tonight.",
                "options": [
                    "parents",
                    "parents'",
                    "parent",
                    "parents's",
                ],
                "answer": "parents'",
                "explanation": (
                    "At my parents' = у моих родителей дома."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct plural possessive.",
                "options": [
                    "the student's books",
                    "the students' books",
                    "the students's books",
                    "the student books' all",
                ],
                "answer": "the students' books",
                "explanation": (
                    "Если владельцев несколько и plural заканчивается на -s → apostrophe."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct irregular plural possessive.",
                "options": [
                    "the childrens' toys",
                    "the children's toys",
                    "the childrens's toys",
                    "the children toys'",
                ],
                "answer": "the children's toys",
                "explanation": (
                    "Children не заканчивается на -s → children's."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct common ownership form.",
                "options": [
                    "Tom's and Anna's house",
                    "Tom and Anna's house",
                    "Tom and Annas house",
                    "Toms' and Anna house",
                ],
                "answer": "Tom and Anna's house",
                "explanation": (
                    "Один общий дом → 's только у последнего."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct separate ownership form.",
                "options": [
                    "Tom and Anna's cars",
                    "Tom's and Anna's cars",
                    "Tom and Annas' cars",
                    "Tom's and Anna cars",
                ],
                "answer": "Tom's and Anna's cars",
                "explanation": (
                    "У каждого своя машина → 's у каждого."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the more natural phrase for a person.",
                "options": [
                    "the car of my brother",
                    "my brother's car",
                    "my brother car's",
                    "the brother of my car",
                ],
                "answer": "my brother's car",
                "explanation": (
                    "С людьми обычно естественнее 's."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the natural OF construction.",
                "options": [
                    "the building's of roof",
                    "the roof of the building",
                    "the roof's the building",
                    "the building of roof",
                ],
                "answer": "the roof of the building",
                "explanation": (
                    "Для части предмета естественна конструкция OF."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct time expression.",
                "options": [
                    "ten minute's walk",
                    "ten minutes' walk",
                    "ten minutes's walk",
                    "ten minute walk's",
                ],
                "answer": "ten minutes' walk",
                "explanation": (
                    "Plural minutes заканчивается на -s → только apostrophe."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct double possessive pair.",
                "options": [
                    (
                        "my friend / "
                        "a friend of mine"
                    ),
                    (
                        "my friend / "
                        "a friend of my"
                    ),
                    (
                        "mine friend / "
                        "a friend of me"
                    ),
                    (
                        "my friend / "
                        "a mine's friend"
                    ),
                ],
                "answer": (
                    "my friend / "
                    "a friend of mine"
                ),
                "explanation": (
                    "A friend of mine = один из моих друзей."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "one owner → student's / "
                        "plural on -s → students' / "
                        "irregular plural → children's / "
                        "shared ownership → Tom and Anna's / "
                        "part of a thing → of"
                    ),
                    (
                        "one owner → student' / "
                        "plural on -s → students's / "
                        "irregular plural → childrens' / "
                        "shared ownership → Tom's and Anna's / "
                        "part of a thing → to"
                    ),
                    (
                        "one owner → students / "
                        "plural on -s → student's / "
                        "irregular plural → children' / "
                        "shared ownership → Tom and Annas / "
                        "part of a thing → from"
                    ),
                    (
                        "one owner → student / "
                        "plural on -s → students / "
                        "irregular plural → childrens / "
                        "shared ownership → Tom's Anna / "
                        "part of a thing → for"
                    ),
                ],
                "answer": (
                    "one owner → student's / "
                    "plural on -s → students' / "
                    "irregular plural → children's / "
                    "shared ownership → Tom and Anna's / "
                    "part of a thing → of"
                ),
                "explanation": (
                    "Это основная система выбора possessive form."
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
                "✅ A1 Lesson 57 seeded: Possessive Case"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
