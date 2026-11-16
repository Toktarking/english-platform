from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 43: Comparatives and Superlatives."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=43,
            defaults={
                "title":
                    "Степени сравнения прилагательных",

                "slug":
                    "comparatives-and-superlatives",

                "theory_text":
                    "Comparatives and Superlatives.",

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
                    "Три формы прилагательного",

                "body":
                    """У прилагательного может быть
три формы.

Обычная:

tall

Сравнительная:

taller

Превосходная:

the tallest

Ещё пример:

beautiful

more beautiful

the most beautiful.""",
            },


            {
                "order": 2,
                "title":
                    "Сравниваем два объекта",

                "body":
                    """Comparative используется,
когда сравниваем два объекта.

Tom is taller than Jack.

This car is faster than mine.

Today is colder than yesterday.

После comparative часто стоит:

THAN

taller than

cheaper than

more interesting than.""",
            },


            {
                "order": 3,
                "title":
                    "Короткие слова: -ER",

                "body":
                    """К коротким прилагательным
обычно добавляем -ER.

tall → taller

small → smaller

fast → faster

old → older

Если слово заканчивается на E:

nice → nicer

large → larger.""",
            },


            {
                "order": 4,
                "title":
                    "BIG → BIGGER, HAPPY → HAPPIER",

                "body":
                    """Иногда последняя согласная удваивается.

big → bigger

hot → hotter

thin → thinner

Если слово заканчивается на Y:

happy → happier

easy → easier

busy → busier

Y меняется на I.""",
            },


            {
                "order": 5,
                "title":
                    "Длинные слова: MORE",

                "body":
                    """С длинными прилагательными
обычно используем MORE.

more beautiful

more expensive

more interesting

more difficult

Не используем одновременно
MORE и -ER.

Неправильно:

more easier

Правильно:

easier.""",
            },


            {
                "order": 6,
                "title":
                    "Superlative: самый",

                "body":
                    """Superlative показывает,
что объект выделяется среди группы.

Tom is the tallest
in the class.

This is the most expensive car.

Короткие слова:

tall → the tallest

Длинные:

expensive
→ the most expensive

Перед superlative обычно нужен THE.""",
            },


            {
                "order": 7,
                "title":
                    "Правописание Superlative",

                "body":
                    """Правила похожи
на comparative.

big → the biggest

hot → the hottest

happy → the happiest

easy → the easiest

nice → the nicest

То есть:

-er → -est

more → the most.""",
            },


            {
                "order": 8,
                "title":
                    "GOOD, BAD и другие исключения",

                "body":
                    """Некоторые формы нужно запомнить.

good
→ better
→ the best

bad
→ worse
→ the worst

many / much
→ more
→ the most

little
→ less
→ the least.""",
            },


            {
                "order": 9,
                "title":
                    "AS ... AS",

                "body":
                    """Если два объекта одинаковы:

AS + adjective + AS

She is as tall as her sister.

This phone is as expensive as mine.

Если не одинаковы:

NOT AS ... AS

This task is not as difficult
as the last one.""",
            },


            {
                "order": 10,
                "title":
                    "LESS, FEWER и усиление",

                "body":
                    """LESS используется
с неисчисляемыми словами.

less time

less money

FEWER используется
с исчисляемыми во множественном числе.

fewer students

fewer mistakes

Comparative можно усилить:

much better

a lot bigger

much easier.""",
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

            section_objects[data["order"]] = section


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            # SECTION 1
            {
                "order": 1,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Choose the comparative form of TALL.",
                "options": [
                    "taller",
                    "tallest",
                    "more tall",
                    "the taller",
                ],
                "answer":
                    "taller",
                "explanation":
                    "TALL → TALLER.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Choose the superlative form of TALL.",
                "options": [
                    "the tallest",
                    "taller",
                    "more tall",
                    "the more taller",
                ],
                "answer":
                    "the tallest",
                "explanation":
                    "TALL → TALLER → THE TALLEST.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "My car is ___ than yours.",
                "options": [
                    "faster",
                    "fastest",
                    "the fast",
                    "more fastest",
                ],
                "answer":
                    "faster",
                "explanation":
                    "Сравниваются два автомобиля → comparative.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "build",
                "prompt":
                    "Собери предложение.",
                "options": [
                    "This",
                    "book",
                    "is",
                    "cheaper",
                    "than",
                    "that",
                    "one",
                ],
                "answer":
                    "This book is cheaper than that one",
                "explanation":
                    "Comparative часто используется с THAN.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "This road is ___ than that one.",
                "options": [
                    "longer",
                    "more long",
                    "longest",
                    "the longer",
                ],
                "answer":
                    "longer",
                "explanation":
                    "LONG — короткое прилагательное → LONGER.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "This place is ___ than the other one.",
                "options": [
                    "nicer",
                    "niceer",
                    "more nicer",
                    "nicest",
                ],
                "answer":
                    "nicer",
                "explanation":
                    "NICE заканчивается на E → NICER.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "This house is ___ than ours.",
                "options": [
                    "bigger",
                    "biger",
                    "more big",
                    "biggest",
                ],
                "answer":
                    "bigger",
                "explanation":
                    "BIG → BIGGER.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "Today I am ___ than yesterday.",
                "options": [
                    "happier",
                    "happyer",
                    "more happier",
                    "happiest",
                ],
                "answer":
                    "happier",
                "explanation":
                    "HAPPY → HAPPIER.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "This hotel is ___ than ours.",
                "options": [
                    "more expensive",
                    "expensiver",
                    "more expensiver",
                    "the most expensive",
                ],
                "answer":
                    "more expensive",
                "explanation":
                    "EXPENSIVE → MORE EXPENSIVE.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "Choose the correct form.",
                "options": [
                    "easier",
                    "more easier",
                    "more easyer",
                    "easyer",
                ],
                "answer":
                    "easier",
                "explanation":
                    "EASY → EASIER; нельзя MORE EASIER.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "He is ___ student in the class.",
                "options": [
                    "the tallest",
                    "taller",
                    "more tall",
                    "tallest than",
                ],
                "answer":
                    "the tallest",
                "explanation":
                    "Один человек выделяется из группы → superlative.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "This is ___ building in the city.",
                "options": [
                    "the most beautiful",
                    "more beautiful",
                    "the beautifuler",
                    "most beautiful than",
                ],
                "answer":
                    "the most beautiful",
                "explanation":
                    "Длинное adjective → THE MOST.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "Choose the correct superlative of BIG.",
                "options": [
                    "the biggest",
                    "the bigest",
                    "the most big",
                    "bigger",
                ],
                "answer":
                    "the biggest",
                "explanation":
                    "BIG → BIGGER → THE BIGGEST.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "Choose the correct superlative of EASY.",
                "options": [
                    "the easiest",
                    "the easyest",
                    "the most easier",
                    "easier",
                ],
                "answer":
                    "the easiest",
                "explanation":
                    "EASY → EASIER → THE EASIEST.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "This book is ___ than that one.",
                "options": [
                    "better",
                    "gooder",
                    "more good",
                    "the best",
                ],
                "answer":
                    "better",
                "explanation":
                    "GOOD → BETTER.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "That was ___ result of the year.",
                "options": [
                    "the worst",
                    "worse",
                    "the baddest",
                    "more bad",
                ],
                "answer":
                    "the worst",
                "explanation":
                    "BAD → WORSE → THE WORST.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "She is ___ tall ___ her sister.",
                "options": [
                    "as / as",
                    "more / than",
                    "as / than",
                    "so / than",
                ],
                "answer":
                    "as / as",
                "explanation":
                    "Равенство → AS + adjective + AS.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "This test is not ___ difficult ___ the last one.",
                "options": [
                    "as / as",
                    "more / as",
                    "as / than",
                    "less / than as",
                ],
                "answer":
                    "as / as",
                "explanation":
                    "NOT AS + adjective + AS.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "I have ___ time today than yesterday.",
                "options": [
                    "less",
                    "fewer",
                    "few",
                    "the least",
                ],
                "answer":
                    "less",
                "explanation":
                    "TIME неисчисляемое → LESS.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "This class has ___ students than ours.",
                "options": [
                    "fewer",
                    "less",
                    "little",
                    "the least",
                ],
                "answer":
                    "fewer",
                "explanation":
                    "STUDENTS исчисляемое множественное → FEWER.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "My new phone is ___ than my old one.",
                "options": [
                    "smaller",
                    "smallest",
                    "more smaller",
                    "the small",
                ],
                "answer":
                    "smaller",
                "explanation":
                    "SMALL → SMALLER.",
            },

            {
                "order": 22,
                "prompt":
                    "This exam is ___ than the previous one.",
                "options": [
                    "more difficult",
                    "difficulter",
                    "the most difficult",
                    "more difficulter",
                ],
                "answer":
                    "more difficult",
                "explanation":
                    "DIFFICULT → MORE DIFFICULT.",
            },

            {
                "order": 23,
                "prompt":
                    "Which is the correct form of HOT?",
                "options": [
                    "hotter",
                    "hoter",
                    "more hot",
                    "the hotter than",
                ],
                "answer":
                    "hotter",
                "explanation":
                    "HOT → HOTTER.",
            },

            {
                "order": 24,
                "prompt":
                    "She is ___ person in our team.",
                "options": [
                    "the busiest",
                    "busier",
                    "the busyer",
                    "the most busier",
                ],
                "answer":
                    "the busiest",
                "explanation":
                    "BUSY → BUSIER → THE BUSIEST.",
            },

            {
                "order": 25,
                "prompt":
                    "This restaurant is ___ in the area.",
                "options": [
                    "the most expensive",
                    "more expensive",
                    "the expensivest",
                    "more expensiver",
                ],
                "answer":
                    "the most expensive",
                "explanation":
                    "Superlative длинного adjective → THE MOST.",
            },

            {
                "order": 26,
                "prompt":
                    "Her second result was ___ than the first.",
                "options": [
                    "worse",
                    "badder",
                    "the worst",
                    "more bad",
                ],
                "answer":
                    "worse",
                "explanation":
                    "BAD → WORSE.",
            },

            {
                "order": 27,
                "prompt":
                    "This is ___ restaurant I've visited here.",
                "options": [
                    "the best",
                    "better",
                    "the goodest",
                    "more good",
                ],
                "answer":
                    "the best",
                "explanation":
                    "GOOD → BETTER → THE BEST.",
            },

            {
                "order": 28,
                "prompt":
                    "My apartment is as ___ as yours.",
                "options": [
                    "large",
                    "larger",
                    "largest",
                    "more large",
                ],
                "answer":
                    "large",
                "explanation":
                    "AS ... AS использует обычную форму adjective.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct comparison.",
                "options": [
                    "This car is much faster than mine. / We have fewer mistakes now.",
                    "This car is very faster than mine. / We have less mistakes now.",
                    "This car is more faster than mine. / We have fewer mistake now.",
                    "This car is much fastest than mine. / We have little mistakes now.",
                ],
                "answer":
                    "This car is much faster than mine. / We have fewer mistakes now.",
                "explanation":
                    "MUCH может усиливать comparative; FEWER используется с countable nouns.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "big → bigger → the biggest / beautiful → more beautiful → the most beautiful / good → better → the best",
                    "big → biger → the bigest / beautiful → beautifuler → the beautifulest / good → gooder → the goodest",
                    "big → more bigger → the most biggest / beautiful → most beautiful → more beautiful / good → best → better",
                    "big → bigger → biggest than / beautiful → more beautifuler → most beautifulest / good → more good → most good",
                ],
                "answer":
                    "big → bigger → the biggest / beautiful → more beautiful → the most beautiful / good → better → the best",
                "explanation":
                    "Короткие adjectives → -er/-est; длинные → more/the most; GOOD имеет неправильные формы.",
            },

        ]


        all_exercises = training + final_test

        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

            if data["order"] <= 20:
                section = section_objects[data["section"]]
            else:
                section = None


            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "section": section,

                    "exercise_type": data.get(
                        "type",
                        "choice",
                    ),

                    "prompt": data["prompt"],

                    "options": data["options"],

                    "correct_answer": data["answer"],

                    "explanation": data["explanation"],

                    "is_published": True,
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
                "✅ Interactive A1 Lesson 43 seeded"
            )
        )

        self.stdout.write(
            f"Micro rules: {lesson.sections.count()}"
        )

        self.stdout.write(
            "Training exercises: "
            f"{lesson.exercises.filter(section__isnull=False).count()}"
        )

        self.stdout.write(
            "Final test: "
            f"{lesson.exercises.filter(section__isnull=True).count()}"
        )
