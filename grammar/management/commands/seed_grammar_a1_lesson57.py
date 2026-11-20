from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 57: Possessive Case."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=57,
            defaults={
                "title":
                    "Притяжательный падеж существительных",

                "slug":
                    "possessive-case",

                "theory_text":
                    "Possessive Case: 's, apostrophe, "
                    "of and ownership.",

                "estimated_minutes":
                    20,

                "pass_score":
                    70,

                "xp_reward":
                    100,

                "is_published":
                    True,
            },
        )


        # =================================================
        # 10 MICRO RULES
        # =================================================

        sections = [

            {
                "order": 1,
                "title":
                    "Один владелец: 'S",

                "body":
                    """Чтобы показать принадлежность,
обычно используем:

owner + 's + thing

Anna's phone

Tom's car

the teacher's desk

my brother's laptop

Сначала идёт владелец,
потом предмет.""",
            },


            {
                "order": 2,
                "title":
                    "Plural на -S",

                "body":
                    """Если владельцев несколько
и plural уже заканчивается на -s,
добавляем только apostrophe.

students → students'

the students' books

teachers → teachers'

the teachers' room

parents → parents'

my parents' house""",
            },


            {
                "order": 3,
                "title":
                    "Irregular Plural",

                "body":
                    """Если plural НЕ заканчивается
на -s, добавляем 's.

children → children's

men → men's

women → women's

people → people's

Примеры:

children's toys

men's clothes

women's shoes""",
            },


            {
                "order": 4,
                "title":
                    "Общая принадлежность",

                "body":
                    """Если один предмет
принадлежит двум людям вместе,
's ставим только у последнего.

Tom and Anna's house

= один общий дом.

Jack and Emma's office

= один общий офис.

Важно:

один общий предмет
→ possessive только у последнего.""",
            },


            {
                "order": 5,
                "title":
                    "Раздельная принадлежность",

                "body":
                    """Если у каждого человека
свой предмет,
's ставим у каждого имени.

Tom's and Anna's cars

= две разные машины.

Jack's and Emma's offices

= два разных офиса.

Сравни:

Tom and Anna's house
— общий дом

Tom's and Anna's houses
— разные дома""",
            },


            {
                "order": 6,
                "title":
                    "Люди, страны и время",

                "body":
                    """'S особенно естественно
используется с:

людьми

животными

организациями

странами

временем

Примеры:

my sister's room

the dog's tail

the company's policy

Kazakhstan's economy

today's meeting

tomorrow's lesson""",
            },


            {
                "order": 7,
                "title":
                    "Time expressions",

                "body":
                    """Possessive используется
с периодами времени.

Один период:

a day's work

a week's holiday

an hour's drive

Несколько:

two days' work

three weeks' holiday

ten minutes' walk

Если plural заканчивается на -s,
ставим только apostrophe.""",
            },


            {
                "order": 8,
                "title":
                    "OF",

                "body":
                    """С предметами и их частями
часто используем OF.

the door of the house

the roof of the building

the title of the article

the end of the road

С человеком обычно естественнее:

my brother's car

а не:

the car of my brother""",
            },


            {
                "order": 9,
                "title":
                    "A friend of mine",

                "body":
                    """Можно использовать:

a friend of mine

a colleague of hers

a neighbour of ours

a student of his

A friend of mine
означает:

один из моих друзей.

Также:

a friend of Tom's

one of Tom's friends.""",
            },


            {
                "order": 10,
                "title":
                    "Когда noun можно убрать",

                "body":
                    """Если предмет уже понятен,
noun можно не повторять.

This book is Anna's.

That car is my brother's.

Is this pen yours
or Kate's?

Также:

at the doctor's

at my parents'

We are staying
at my parents'.

= у моих родителей дома.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = GrammarLessonSection.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "title":
                        data["title"],

                    "body":
                        data["body"],
                },
            )

            section_objects[
                data["order"]
            ] = section


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            # SECTION 1
            {
                "order": 1,
                "section": 1,
                "prompt":
                    "This is the ___ office.",
                "options": [
                    "manager's",
                    "manager",
                    "managers",
                    "managers's",
                ],
                "answer":
                    "manager's",
                "explanation":
                    "Один владелец → 's.",
            },

            {
                "order": 2,
                "section": 1,
                "prompt":
                    "Choose the correct phrase.",
                "options": [
                    "Anna's phone",
                    "Anna phone's",
                    "the phone's Anna",
                    "Annas phone",
                ],
                "answer":
                    "Anna's phone",
                "explanation":
                    "Owner + 's + thing.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "prompt":
                    "The ___ books are on the table. Several students own them.",
                "options": [
                    "students'",
                    "student's",
                    "students's",
                    "students",
                ],
                "answer":
                    "students'",
                "explanation":
                    "Plural на -s → только apostrophe.",
            },

            {
                "order": 4,
                "section": 2,
                "prompt":
                    "This is my ___ house.",
                "options": [
                    "parents'",
                    "parent's",
                    "parents's",
                    "parents",
                ],
                "answer":
                    "parents'",
                "explanation":
                    "Parents = plural ending in -s.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "prompt":
                    "These are the ___ toys.",
                "options": [
                    "children's",
                    "childrens'",
                    "childrens's",
                    "children",
                ],
                "answer":
                    "children's",
                "explanation":
                    "CHILDREN — irregular plural → 's.",
            },

            {
                "order": 6,
                "section": 3,
                "prompt":
                    "The ___ clothes are upstairs.",
                "options": [
                    "men's",
                    "mens'",
                    "mens's",
                    "men",
                ],
                "answer":
                    "men's",
                "explanation":
                    "MEN не заканчивается на -s → MEN'S.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "prompt":
                    "Jack and Emma have one house together.",
                "options": [
                    "Jack and Emma's house",
                    "Jack's and Emma's house",
                    "Jack and Emmas' house",
                    "Jacks' and Emma house",
                ],
                "answer":
                    "Jack and Emma's house",
                "explanation":
                    "Общий предмет → 's только у последнего имени.",
            },

            {
                "order": 8,
                "section": 4,
                "prompt":
                    "Tom and Sara share one office.",
                "options": [
                    "Tom and Sara's office",
                    "Tom's and Sara's office",
                    "Tom and Saras office",
                    "Tom's and Sara office",
                ],
                "answer":
                    "Tom and Sara's office",
                "explanation":
                    "Один общий офис → possessive только у Sara.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "prompt":
                    "Tom and Anna each have their own car.",
                "options": [
                    "Tom's and Anna's cars",
                    "Tom and Anna's cars",
                    "Tom's and Anna cars",
                    "Tom and Annas' cars",
                ],
                "answer":
                    "Tom's and Anna's cars",
                "explanation":
                    "Раздельная принадлежность → 's у каждого.",
            },

            {
                "order": 10,
                "section": 5,
                "prompt":
                    "Jack and Emma each have a separate office.",
                "options": [
                    "Jack's and Emma's offices",
                    "Jack and Emma's offices",
                    "Jack's and Emma offices",
                    "Jack and Emmas' offices",
                ],
                "answer":
                    "Jack's and Emma's offices",
                "explanation":
                    "У каждого свой офис.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "prompt":
                    "The ___ policy has changed. One company.",
                "options": [
                    "company's",
                    "companies'",
                    "company",
                    "companys'",
                ],
                "answer":
                    "company's",
                "explanation":
                    "Одна организация → COMPANY'S.",
            },

            {
                "order": 12,
                "section": 6,
                "prompt":
                    "___ meeting starts at 10 a.m.",
                "options": [
                    "Today's",
                    "Todays",
                    "Today'",
                    "Todays'",
                ],
                "answer":
                    "Today's",
                "explanation":
                    "TODAY'S = сегодняшний.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "prompt":
                    "It is a two ___ journey.",
                "options": [
                    "hours'",
                    "hour's",
                    "hours's",
                    "hour",
                ],
                "answer":
                    "hours'",
                "explanation":
                    "Two hours = plural ending in -s → HOURS'.",
            },

            {
                "order": 14,
                "section": 7,
                "prompt":
                    "It's only ten ___ walk.",
                "options": [
                    "minutes'",
                    "minute's",
                    "minutes's",
                    "minutes",
                ],
                "answer":
                    "minutes'",
                "explanation":
                    "Ten minutes → MINUTES'.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "prompt":
                    "Choose the natural phrase.",
                "options": [
                    "the roof of the building",
                    "the building's of roof",
                    "the roof's the building",
                    "the building of roof",
                ],
                "answer":
                    "the roof of the building",
                "explanation":
                    "Для части предмета естественно использовать OF.",
            },

            {
                "order": 16,
                "section": 8,
                "prompt":
                    "Choose the more natural phrase for a person.",
                "options": [
                    "my brother's car",
                    "the car of my brother",
                    "my brother car's",
                    "the brother of my car",
                ],
                "answer":
                    "my brother's car",
                "explanation":
                    "С людьми обычно используем 's.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "prompt":
                    "A friend of ___ lives in London.",
                "options": [
                    "mine",
                    "my",
                    "me",
                    "I",
                ],
                "answer":
                    "mine",
                "explanation":
                    "Правильная форма: A FRIEND OF MINE.",
            },

            {
                "order": 18,
                "section": 9,
                "prompt":
                    "Choose the correct phrase.",
                "options": [
                    "a colleague of hers",
                    "a colleague of her",
                    "a hers colleague",
                    "a colleague hers",
                ],
                "answer":
                    "a colleague of hers",
                "explanation":
                    "OF + possessive pronoun.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "prompt":
                    "This book belongs to Anna. This book is ___.",
                "options": [
                    "Anna's",
                    "Anna",
                    "Annas",
                    "Annas'",
                ],
                "answer":
                    "Anna's",
                "explanation":
                    "После possessive form noun можно не повторять.",
            },

            {
                "order": 20,
                "section": 10,
                "prompt":
                    "We are staying at my ___ tonight.",
                "options": [
                    "parents'",
                    "parents",
                    "parents's",
                    "parent",
                ],
                "answer":
                    "parents'",
                "explanation":
                    "AT MY PARENTS' = у родителей дома.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "This is my ___ laptop. One sister.",
                "options": [
                    "sister's",
                    "sisters'",
                    "sister",
                    "sisters's",
                ],
                "answer":
                    "sister's",
                "explanation":
                    "Один владелец → 's.",
            },

            {
                "order": 22,
                "prompt":
                    "The ___ classroom is on the second floor. Several teachers use it.",
                "options": [
                    "teachers'",
                    "teacher's",
                    "teachers's",
                    "teachers",
                ],
                "answer":
                    "teachers'",
                "explanation":
                    "Plural teachers → TEACHERS'.",
            },

            {
                "order": 23,
                "prompt":
                    "The ___ playground is new.",
                "options": [
                    "children's",
                    "childrens'",
                    "childrens's",
                    "children",
                ],
                "answer":
                    "children's",
                "explanation":
                    "CHILDREN = irregular plural → 's.",
            },

            {
                "order": 24,
                "prompt":
                    "Ali and Dana share one apartment.",
                "options": [
                    "Ali and Dana's apartment",
                    "Ali's and Dana's apartment",
                    "Ali and Danas' apartment",
                    "Ali's and Dana apartment",
                ],
                "answer":
                    "Ali and Dana's apartment",
                "explanation":
                    "Общая принадлежность → 's у последнего.",
            },

            {
                "order": 25,
                "prompt":
                    "Ali and Dana each have their own phone.",
                "options": [
                    "Ali's and Dana's phones",
                    "Ali and Dana's phones",
                    "Ali's and Dana phones",
                    "Ali and Danas' phones",
                ],
                "answer":
                    "Ali's and Dana's phones",
                "explanation":
                    "Раздельная принадлежность → 's у каждого.",
            },

            {
                "order": 26,
                "prompt":
                    "Choose the correct time expression.",
                "options": [
                    "three days' work",
                    "three day's work",
                    "three days's work",
                    "three day work's",
                ],
                "answer":
                    "three days' work",
                "explanation":
                    "Plural DAYS заканчивается на -s.",
            },

            {
                "order": 27,
                "prompt":
                    "Choose the natural OF construction.",
                "options": [
                    "the end of the road",
                    "the road's of end",
                    "the end's the road",
                    "the road of end",
                ],
                "answer":
                    "the end of the road",
                "explanation":
                    "Для части/элемента предмета часто используем OF.",
            },

            {
                "order": 28,
                "prompt":
                    "One of my neighbours = ___.",
                "options": [
                    "a neighbour of mine",
                    "a neighbour of my",
                    "mine neighbour",
                    "a neighbour of me",
                ],
                "answer":
                    "a neighbour of mine",
                "explanation":
                    "Double possessive: A NEIGHBOUR OF MINE.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct possessive without repeating the noun.",
                "options": [
                    "That car is Peter's.",
                    "That car is Peter.",
                    "That car is Peters.",
                    "That car is Peters'.",
                ],
                "answer":
                    "That car is Peter's.",
                "explanation":
                    "Предмет уже назван, поэтому CAR можно не повторять.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "one owner → student's / plural on -s → students' / irregular plural → children's / shared ownership → Tom and Anna's / part of a thing → of",
                    "one owner → student' / plural on -s → students's / irregular plural → childrens' / shared ownership → Tom's and Anna's / part of a thing → to",
                    "one owner → students / plural on -s → student's / irregular plural → children' / shared ownership → Tom and Annas / part of a thing → from",
                    "one owner → student / plural on -s → students / irregular plural → childrens / shared ownership → Tom's Anna / part of a thing → for",
                ],
                "answer":
                    "one owner → student's / plural on -s → students' / irregular plural → children's / shared ownership → Tom and Anna's / part of a thing → of",
                "explanation":
                    "Это основная система Possessive Case.",
            },

        ]


        all_exercises = (
            training
            +
            final_test
        )

        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

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
                        "choice",

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
                "✅ Interactive A1 Lesson 57 seeded"
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
