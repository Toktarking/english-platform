from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = "Create/update the first A1 grammar lesson."

    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                slug="articles-a-an",
                defaults={
                    "title": "Артикли A и AN",
                    "level": "A1",
                    "order": 1,
                    "theory_text": (
                        "Артикли A и AN."
                    ),
                    "estimated_minutes": 15,
                    "pass_score": 70,
                    "xp_reward": 100,
                    "is_published": True,
                },
            )
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое артикль",
                "body": """В русском языке артиклей нет.

Мы говорим:
книга;
яблоко;
учитель.

В английском языке перед исчисляемым предметом в единственном числе часто нужно поставить маленькое слово:

a book — книга;
an apple — яблоко;
a teacher — учитель.

Слова a и an называются артиклями.

Самостоятельно они обычно не переводятся. Они показывают, что речь идёт об одном предмете.""",
            },

            {
                "order": 2,
                "title": "Когда используется A",
                "body": """Артикль a ставится перед словом, которое начинается с согласного звука.

a book — книга;
a cat — кошка;
a dog — собака;
a teacher — учитель;
a student — студент.

Обратите внимание:

a book

Когда мы говорим об одном обычном исчисляемом предмете, существительному обычно нужен определитель.

Правильно:

This is a book. — Это книга.
I have a cat. — У меня есть кошка.
He is a teacher. — Он учитель.""",
            },

            {
                "order": 3,
                "title": "Когда используется AN",
                "body": """Артикль an ставится перед словом, которое начинается с гласного звука.

Основные гласные буквы:
a, e, i, o, u

Примеры:

an apple — яблоко;
an egg — яйцо;
an orange — апельсин;
an umbrella — зонтик;
an idea — идея.

Предложения:

This is an apple. — Это яблоко.
She has an umbrella. — У неё есть зонтик.
It is an interesting book. — Это интересная книга.""",
            },

            {
                "order": 4,
                "title": "A или AN зависит от звука",
                "body": """Важно смотреть не только на букву, но и на первый звук.

A university

Слово university начинается с буквы U, но произносится примерно как «юниверсити».

Первый звук — «й», то есть согласный.

Поэтому:

a university;
a university student.

An hour

В слове hour буква H не произносится.

Слово начинается со звука «ау».

Поэтому:

an hour;
an honest person.""",
            },

            {
                "order": 5,
                "title": "Артикль перед прилагательным",
                "body": """Посмотрите:

a car — машина;
a new car — новая машина;
an expensive car — дорогая машина.

Артикль ставится перед всей группой слов:

артикль + прилагательное + существительное

Примеры:

a good teacher — хороший учитель;
a small house — маленький дом;
an old house — старый дом;
an interesting story — интересная история.

Выбор a или an зависит от слова, которое идёт сразу после артикля:

a useful book;
an interesting book.""",
            },

            {
                "order": 6,
                "title": "Когда A и AN не используются",
                "body": """Артикли a/an означают один предмет. Поэтому их нельзя использовать непосредственно перед существительными во множественном числе.

Неправильно:

a books;
an apples;
a students.

Правильно:

a book — одна книга;
books — книги;
an apple — одно яблоко;
apples — яблоки.

Также a/an обычно не используются с неисчисляемыми существительными:

water — вода;
money — деньги;
information — информация;
happiness — счастье.

Неправильно:

a water;
a money;
an information.

Правильно:

some water;
some money;
some information.""",
            },

            {
                "order": 7,
                "title": "Сравним A и AN",
                "body": """A:

a book
a teacher
a cat
a house
a university

AN:

an apple
an engineer
an animal
an old house
an umbrella""",
            },

        ]

        section_objects = {}

        for data in sections:

            section, _ = (
                GrammarLessonSection
                .objects
                .update_or_create(
                    lesson=lesson,
                    order=data["order"],
                    defaults={
                        "title": data["title"],
                        "body": data["body"],
                    },
                )
            )

            section_objects[
                data["order"]
            ] = section


        exercises = [

            {
                "order": 1,
                "prompt": "This is ___ book.",
                "options": [
                    "a",
                    "an",
                    "the",
                    "—",
                ],
                "answer": "a",
                "explanation": (
                    "Book начинается с "
                    "согласного звука."
                ),
            },

            {
                "order": 2,
                "prompt": "She has ___ apple.",
                "options": [
                    "a",
                    "an",
                    "some",
                    "—",
                ],
                "answer": "an",
                "explanation": (
                    "Apple начинается с "
                    "гласного звука."
                ),
            },

            {
                "order": 3,
                "prompt": "He is ___ teacher.",
                "options": [
                    "a",
                    "an",
                    "some",
                    "—",
                ],
                "answer": "a",
                "explanation": (
                    "Teacher — исчисляемое "
                    "существительное в "
                    "единственном числе."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "It is ___ interesting film."
                ),
                "options": [
                    "a",
                    "an",
                    "some",
                    "—",
                ],
                "answer": "an",
                "explanation": (
                    "Interesting начинается "
                    "с гласного звука."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "She studies at ___ university."
                ),
                "options": [
                    "a",
                    "an",
                    "some",
                    "—",
                ],
                "answer": "a",
                "explanation": (
                    "University начинается "
                    "со звука /j/, похожего "
                    "на русский «й»."
                ),
            },

            {
                "order": 6,
                "prompt": "It takes ___ hour.",
                "options": [
                    "a",
                    "an",
                    "some",
                    "—",
                ],
                "answer": "an",
                "explanation": (
                    "В hour буква h "
                    "не произносится."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "This is ___ useful book."
                ),
                "options": [
                    "a",
                    "an",
                    "some",
                    "—",
                ],
                "answer": "a",
                "explanation": (
                    "Useful начинается "
                    "со звука /j/."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "She is ___ English teacher."
                ),
                "options": [
                    "a",
                    "an",
                    "some",
                    "—",
                ],
                "answer": "an",
                "explanation": (
                    "English начинается "
                    "с гласного звука."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "Choose the correct phrase."
                ),
                "options": [
                    "an information",
                    "a information",
                    "some information",
                    "an informations",
                ],
                "answer": "some information",
                "explanation": (
                    "Information — "
                    "неисчисляемое существительное."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "Choose the correct phrase."
                ),
                "options": [
                    "an European country",
                    "a European country",
                    "a European countries",
                    "an European countries",
                ],
                "answer": "a European country",
                "explanation": (
                    "European начинается "
                    "со звука /j/."
                ),
            },

        ]

        for data in exercises:

            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "exercise_type": (
                        GrammarExercise.Type.CHOICE
                    ),
                    "prompt": data["prompt"],
                    "options": data["options"],
                    "correct_answer": data["answer"],
                    "explanation": data[
                        "explanation"
                    ],
                    "is_published": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ A1 Lesson 1 seeded: "
                "Артикли A и AN"
            )
        )

        self.stdout.write(
            f"Sections: "
            f"{lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: "
            f"{lesson.exercises.count()}"
        )
