from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 9: Reflexive pronouns."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects
            .update_or_create(
                level="A1",
                order=9,
                defaults={
                    "title":
                        "Возвратные местоимения",

                    "slug":
                        "reflexive-pronouns",

                    "theory_text":
                        "Reflexive pronouns.",

                    "estimated_minutes":
                        15,

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
                    "Когда нужен reflexive pronoun?",

                "body":
                    """Возвратное местоимение используется, когда человек выполняет действие и это действие направлено на него же.

Сравни:

I see him.
Я вижу его.

I see myself in the mirror.
Я вижу себя.

Marat cut him.
Марат порезал другого мужчину.

Marat cut himself.
Марат порезался сам.

Главный вопрос:

кто выполняет действие?

и на кого направлено действие?

Если это один и тот же человек — часто нужен reflexive pronoun.""",
            },


            {
                "order": 2,
                "title":
                    "Главная таблица",

                "body":
                    """Формы нужно запомнить:

I → myself

you → yourself

he → himself

she → herself

it → itself

we → ourselves

you → yourselves

they → themselves

Обычно:

единственное число → -self

множественное число → -selves

Особенно запомни:

yourself = один человек

yourselves = несколько людей.""",
            },


            {
                "order": 3,
                "title":
                    "Действие направлено на самого себя",

                "body":
                    """Примеры:

I cut myself.

He hurt himself.

She looked at herself in the mirror.

The cat cleaned itself.

We introduced ourselves.

They prepared themselves.

Форма всегда должна соответствовать подлежащему:

I → myself

he → himself

she → herself

we → ourselves

they → themselves.""",
            },


            {
                "order": 4,
                "title":
                    "Частые конструкции",

                "body":
                    """Некоторые конструкции часто используются с reflexive pronouns:

introduce oneself
представиться

Let me introduce myself.

teach oneself
научиться самостоятельно

He taught himself English.

enjoy oneself
хорошо проводить время

We enjoyed ourselves.

hurt oneself
пораниться

She hurt herself.

help yourself
угощайся / бери сам

Help yourself to some cake.""",
            },


            {
                "order": 5,
                "title":
                    "Reflexive pronoun может означать «сам»",

                "body":
                    """Иногда действие не направлено на себя.

Reflexive pronoun просто подчёркивает:

сам
сама
сами
лично

I did it myself.
Я сделал это сам.

She wrote the report herself.

The director himself spoke to us.

We prepared the food ourselves.

В таком значении форма часто стоит:

после подлежащего

или

в конце предложения.

I myself checked it.

I checked it myself.""",
            },


            {
                "order": 6,
                "title":
                    "BY MYSELF = самостоятельно",

                "body":
                    """BY + reflexive pronoun часто означает:

самостоятельно;
без помощи;
в одиночестве.

I live by myself.
Я живу один.

She travelled by herself.
Она путешествовала одна.

He fixed the computer by himself.
Он починил компьютер без помощи.

Сравни:

I did it myself.
Я сделал это сам.

I did it by myself.
Я сделал это самостоятельно, без помощи.""",
            },


            {
                "order": 7,
                "title":
                    "Когда reflexive pronoun не нужен",

                "body":
                    """В английском некоторые действия обычно не требуют возвратного местоимения.

Обычно говорим:

I washed.

He dressed quickly.

She feels tired.

We met yesterday.

Не:

I feel myself tired.

А:

I feel tired.

Не:

We met ourselves yesterday.

А:

We met yesterday.

Английская конструкция не всегда совпадает с русским «-ся».""",
            },


            {
                "order": 8,
                "title":
                    "THEMSELVES или EACH OTHER?",

                "body":
                    """THEMSELVES означает:

себя / сами себя.

EACH OTHER означает:

друг друга.

Сравни:

They looked at themselves in the mirror.
Они посмотрели на себя.

They looked at each other.
Они посмотрели друг на друга.

The children dressed themselves.
Дети оделись сами.

The children helped each other.
Дети помогали друг другу.""",
            },


            {
                "order": 9,
                "title":
                    "Как быстро выбрать форму",

                "body":
                    """Шаг 1.

Найди подлежащее.

She hurt ___.

Подлежащее → SHE.

Шаг 2.

Действие направлено на неё же?

Да:

She hurt herself.

Нет:

She hurt him.

Шаг 3.

Проверь число:

one person:

myself
yourself
himself
herself
itself

plural:

ourselves
yourselves
themselves

Шаг 4.

Если смысл «самостоятельно, без помощи»:

by myself
by yourself
by himself
by herself
by ourselves
by themselves.""",
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
                    "I saw ___ in the mirror.",

                "options": [
                    "me",
                    "myself",
                    "mine",
                    "my",
                ],

                "answer":
                    "myself",

                "explanation":
                    "Говорящий видит самого себя.",
            },


            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "Marat cut ___ while cooking.",

                "options": [
                    "him",
                    "his",
                    "himself",
                    "he",
                ],

                "answer":
                    "himself",

                "explanation":
                    "Marat порезал самого себя.",
            },


            {
                "order": 3,
                "section": 2,
                "type": "fill",

                "prompt":
                    "She hurt ___.",

                "options": [],

                "answer":
                    "herself",

                "explanation":
                    "She → herself.",
            },


            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Please introduce ___. (one person)",

                "options": [
                    "yourself",
                    "yourselves",
                    "themselves",
                    "ourselves",
                ],

                "answer":
                    "yourself",

                "explanation":
                    "Обращение к одному человеку → YOURSELF.",
            },


            {
                "order": 5,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Please introduce ___. (several people)",

                "options": [
                    "yourself",
                    "yourselves",
                    "himself",
                    "herself",
                ],

                "answer":
                    "yourselves",

                "explanation":
                    "Обращение к нескольким людям → YOURSELVES.",
            },


            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "The cat cleaned ___.",

                "options": [
                    "itself",
                    "himself",
                    "themselves",
                    "ourselves",
                ],

                "answer":
                    "itself",

                "explanation":
                    "Cat здесь заменяется IT → ITSELF.",
            },


            {
                "order": 7,
                "section": 3,
                "type": "fill",

                "prompt":
                    "We looked at ___ in the photograph.",

                "options": [],

                "answer":
                    "ourselves",

                "explanation":
                    "We → ourselves.",
            },


            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "We enjoyed ___ at the party.",

                "options": [
                    "us",
                    "our",
                    "ourselves",
                    "ours",
                ],

                "answer":
                    "ourselves",

                "explanation":
                    "Устойчивая конструкция: enjoy oneself.",
            },


            {
                "order": 9,
                "section": 4,
                "type": "choice",

                "prompt":
                    "He taught ___ English.",

                "options": [
                    "him",
                    "his",
                    "himself",
                    "he",
                ],

                "answer":
                    "himself",

                "explanation":
                    "Teach oneself означает научиться самостоятельно.",
            },


            {
                "order": 10,
                "section": 4,
                "type": "choice",

                "prompt":
                    "___ to some cake.",

                "options": [
                    "Help yourself",
                    "Help you",
                    "Help yours",
                    "Help myself",
                ],

                "answer":
                    "Help yourself",

                "explanation":
                    "Help yourself — устойчивое выражение «угощайся».",
            },


            {
                "order": 11,
                "section": 5,
                "type": "choice",

                "prompt":
                    "I repaired the chair ___.",

                "options": [
                    "myself",
                    "me",
                    "mine",
                    "my",
                ],

                "answer":
                    "myself",

                "explanation":
                    "MYSELF здесь подчёркивает: «я сделал это сам».",
            },


            {
                "order": 12,
                "section": 5,
                "type": "choice",

                "prompt":
                    "The director ___ checked the documents.",

                "options": [
                    "himself",
                    "him",
                    "his",
                    "he",
                ],

                "answer":
                    "himself",

                "explanation":
                    "HIMSELF подчёркивает: сам директор лично.",
            },


            {
                "order": 13,
                "section": 6,
                "type": "choice",

                "prompt":
                    "She travelled by ___.",

                "options": [
                    "her",
                    "herself",
                    "hers",
                    "she",
                ],

                "answer":
                    "herself",

                "explanation":
                    "BY HERSELF означает одна / самостоятельно.",
            },


            {
                "order": 14,
                "section": 6,
                "type": "build",

                "prompt":
                    "Собери выражение «я сделал это самостоятельно».",

                "options": [
                    "I",
                    "did",
                    "it",
                    "by",
                    "myself",
                ],

                "answer":
                    "I did it by myself",

                "explanation":
                    "BY MYSELF подчёркивает отсутствие помощи.",
            },


            {
                "order": 15,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I feel ___ today.",

                "options": [
                    "myself tired",
                    "me tired",
                    "tired",
                    "myself tiring",
                ],

                "answer":
                    "tired",

                "explanation":
                    "После FEEL в таком значении reflexive pronoun не нужен.",
            },


            {
                "order": 16,
                "section": 7,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "We met ourselves yesterday.",
                    "We met yesterday.",
                    "We met us yesterday.",
                    "Ourselves met yesterday.",
                ],

                "answer":
                    "We met yesterday.",

                "explanation":
                    "С MEET возвратное местоимение здесь не нужно.",
            },


            {
                "order": 17,
                "section": 8,
                "type": "choice",

                "prompt":
                    "The students helped ___ during the project.",

                "options": [
                    "themselves",
                    "each other",
                    "ourselves",
                    "itself",
                ],

                "answer":
                    "each other",

                "explanation":
                    "Студенты помогали друг другу.",
            },


            {
                "order": 18,
                "section": 8,
                "type": "choice",

                "prompt":
                    "They looked at ___ in the mirror.",

                "options": [
                    "each other",
                    "themselves",
                    "himself",
                    "ourselves",
                ],

                "answer":
                    "themselves",

                "explanation":
                    "Они смотрели на самих себя.",
            },


            {
                "order": 19,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Aigul prepared ___ for the interview.",

                "options": [
                    "her",
                    "hers",
                    "herself",
                    "she",
                ],

                "answer":
                    "herself",

                "explanation":
                    "Aigul = SHE → HERSELF.",
            },


            {
                "order": 20,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "we → ourselves / they → themselves",
                    "we → themselves / they → ourselves",
                    "we → ourself / they → theirselves",
                    "we → yourself / they → itself",
                ],

                "answer":
                    "we → ourselves / they → themselves",

                "explanation":
                    "Правильные формы: WE → OURSELVES, THEY → THEMSELVES.",
            },

        ]


        # =================================================
        # 10 FINAL TEST QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "I introduced ___ to the new students.",

                "options": [
                    "me",
                    "myself",
                    "mine",
                    "my",
                ],

                "answer":
                    "myself",

                "explanation":
                    "I → myself.",
            },


            {
                "order": 22,

                "prompt":
                    "Did you hurt ___? (one person)",

                "options": [
                    "yourself",
                    "yourselves",
                    "himself",
                    "themselves",
                ],

                "answer":
                    "yourself",

                "explanation":
                    "Один собеседник → YOURSELF.",
            },


            {
                "order": 23,

                "prompt":
                    "The children dressed ___.",

                "options": [
                    "itself",
                    "himself",
                    "themselves",
                    "yourself",
                ],

                "answer":
                    "themselves",

                "explanation":
                    "Children = THEY → THEMSELVES.",
            },


            {
                "order": 24,

                "prompt":
                    "She wrote the whole report ___.",

                "options": [
                    "herself",
                    "her",
                    "hers",
                    "she",
                ],

                "answer":
                    "herself",

                "explanation":
                    "HERSELF здесь означает «сама».",
            },


            {
                "order": 25,

                "prompt":
                    "He fixed the computer by ___.",

                "options": [
                    "him",
                    "his",
                    "himself",
                    "he",
                ],

                "answer":
                    "himself",

                "explanation":
                    "BY HIMSELF означает самостоятельно, без помощи.",
            },


            {
                "order": 26,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "She feels herself tired.",
                    "She feels tired.",
                    "She feels her tired.",
                    "Herself feels tired.",
                ],

                "answer":
                    "She feels tired.",

                "explanation":
                    "После FEEL в таком значении reflexive pronoun не нужен.",
            },


            {
                "order": 27,

                "prompt":
                    "The two friends looked at ___.",

                "options": [
                    "themselves",
                    "each other",
                    "itself",
                    "ourselves",
                ],

                "answer":
                    "each other",

                "explanation":
                    "Два друга смотрели друг на друга.",
            },


            {
                "order": 28,

                "prompt":
                    "The door opened by ___.",

                "options": [
                    "itself",
                    "himself",
                    "herself",
                    "themselves",
                ],

                "answer":
                    "itself",

                "explanation":
                    "BY ITSELF означает, что дверь открылась сама.",
            },


            {
                "order": 29,

                "prompt":
                    "Please make ___ comfortable. (several people)",

                "options": [
                    "yourself",
                    "yourselves",
                    "ourselves",
                    "itself",
                ],

                "answer":
                    "yourselves",

                "explanation":
                    "Обращение к нескольким людям → YOURSELVES.",
            },


            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "They prepared themselves and then helped each other.",
                    "They prepared each other and helped themselves each other.",
                    "They prepared theirselves and helped themselves together.",
                    "Them prepared themselves and helped each other.",
                ],

                "answer":
                    "They prepared themselves and then helped each other.",

                "explanation":
                    "THEMSELVES означает себя, EACH OTHER — друг друга.",
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
                "✅ Interactive A1 Lesson 9 seeded"
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
