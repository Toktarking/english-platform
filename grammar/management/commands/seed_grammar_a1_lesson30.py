from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 30: Present Perfect."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=30,

                defaults={
                    "title":
                        "Present Perfect: HAVE / HAS + третья форма",

                    "slug":
                        "present-perfect",

                    "theory_text":
                        "Present Perfect.",

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
        )


        # =================================================
        # 10 MICRO RULES
        # =================================================

        sections = [

            {
                "order": 1,
                "title":
                    "Что показывает Present Perfect?",

                "body":
                    """Present Perfect связывает прошлое с настоящим.

Действие произошло раньше,
но сейчас важен его результат или опыт.

I have finished the report.

Отчёт уже готов сейчас.

She has lost her keys.

Она потеряла ключи,
и сейчас у неё их нет.

Главная идея:

прошлое действие
→ результат важен сейчас.""",
            },


            {
                "order": 2,
                "title":
                    "HAVE или HAS?",

                "body":
                    """Формула Present Perfect:

HAVE / HAS + третья форма глагола

HAVE:

I
you
we
they

HAS:

he
she
it

Примеры:

I have finished.

We have arrived.

She has finished.

He has arrived.""",
            },


            {
                "order": 3,
                "title":
                    "Третья форма глагола",

                "body":
                    """После HAVE / HAS нужна третья форма глагола.

У правильных глаголов:

work → worked → worked
play → played → played

У неправильных:

go → went → gone
see → saw → seen
write → wrote → written
eat → ate → eaten
do → did → done

Важно:

I have gone.

Не:

I have went.""",
            },


            {
                "order": 4,
                "title":
                    "Утверждение, отрицание и вопрос",

                "body":
                    """Утверждение:

I have finished.

She has arrived.

Отрицание:

I haven't finished.

She hasn't arrived.

Вопрос:

Have you finished?

Has she arrived?

Короткий ответ:

Yes, I have.
No, I haven't.

Yes, she has.
No, she hasn't.""",
            },


            {
                "order": 5,
                "title":
                    "Результат важен сейчас",

                "body":
                    """Present Perfect часто используется,
когда мы видим результат сейчас.

I have lost my phone.

→ телефона сейчас нет.

She has broken her glasses.

→ очки сейчас сломаны.

We have finished the work.

→ работа сейчас готова.

Точное время действия не важно.""",
            },


            {
                "order": 6,
                "title":
                    "EVER и NEVER",

                "body":
                    """Present Perfect используется для жизненного опыта.

EVER = когда-нибудь

Have you ever been to London?

Has she ever tried sushi?

NEVER = никогда

I have never been to London.

She has never tried sushi.

После NEVER дополнительное NOT не нужно.

Правильно:

I have never seen it.""",
            },


            {
                "order": 7,
                "title":
                    "JUST, ALREADY и YET",

                "body":
                    """JUST = только что

I have just finished.

ALREADY = уже

She has already eaten.

JUST и ALREADY обычно стоят между
HAVE / HAS и третьей формой.

YET обычно стоит в конце.

Have you finished yet?

I haven't finished yet.""",
            },


            {
                "order": 8,
                "title":
                    "BEEN или GONE?",

                "body":
                    """BEEN TO:

человек был где-то и уже вернулся.

Marat has been to Astana.

→ Марат был в Астане и вернулся.

GONE TO:

человек ушёл или уехал
и ещё не вернулся.

Marat has gone to Astana.

→ сейчас он ещё там или в пути.""",
            },


            {
                "order": 9,
                "title":
                    "FOR, SINCE и HOW LONG",

                "body":
                    """Present Perfect может показывать действие,
которое началось раньше и продолжается сейчас.

FOR = сколько времени

for two hours
for five years

I have lived here for five years.

SINCE = с какого момента

since Monday
since 2020

I have lived here since 2020.

Вопрос:

How long have you lived here?""",
            },


            {
                "order": 10,
                "title":
                    "Present Perfect или Past Simple?",

                "body":
                    """Если указано завершённое время прошлого:

yesterday
last week
two days ago
in 2020

→ Past Simple

I saw him yesterday.

Если точное время не называется
и важен результат или опыт:

→ Present Perfect

I have seen this film.

Сравни:

I visited Turkey in 2024.

I have visited Turkey.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = (
                GrammarLessonSection.objects.update_or_create(
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
        # 2 after every micro rule
        # =================================================

        training = [

            # SECTION 1

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I ___ finished the report.",

                "options": [
                    "have",
                    "has",
                    "did",
                    "am",
                ],

                "answer":
                    "have",

                "explanation":
                    "I используется с HAVE.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "She has lost her keys. What is important now?",

                "options": [
                    "She does not have the keys now.",
                    "We know exactly when she lost them.",
                    "She loses them every day.",
                    "She is losing them now.",
                ],

                "answer":
                    "She does not have the keys now.",

                "explanation":
                    "Present Perfect показывает текущий результат.",
            },


            # SECTION 2

            {
                "order": 3,
                "section": 2,
                "type": "choice",

                "prompt":
                    "My parents ___ arrived.",

                "options": [
                    "has",
                    "have",
                    "is",
                    "did",
                ],

                "answer":
                    "have",

                "explanation":
                    "Parents = THEY, поэтому HAVE.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "My sister ___ finished her work.",

                "options": [
                    "have",
                    "has",
                    "did",
                    "are",
                ],

                "answer":
                    "has",

                "explanation":
                    "My sister = SHE, поэтому HAS.",
            },


            # SECTION 3

            {
                "order": 5,
                "section": 3,
                "type": "fill",

                "prompt":
                    "go → went → ___",

                "options": [],

                "answer":
                    "gone",

                "explanation":
                    "Третья форма GO — GONE.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",

                "prompt":
                    "He has ___ the email.",

                "options": [
                    "wrote",
                    "written",
                    "write",
                    "writing",
                ],

                "answer":
                    "written",

                "explanation":
                    "WRITE → WROTE → WRITTEN.",
            },


            # SECTION 4

            {
                "order": 7,
                "section": 4,
                "type": "build",

                "prompt":
                    "Собери правильное предложение.",

                "options": [
                    "I",
                    "have",
                    "finished",
                    "the",
                    "task",
                ],

                "answer":
                    "I have finished the task",

                "explanation":
                    "Утверждение: subject + HAVE/HAS + V3.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Have you finished?",
                    "Did you finished?",
                    "Have you finish?",
                    "Do you have finished?",
                ],

                "answer":
                    "Have you finished?",

                "explanation":
                    "Вопрос: HAVE + subject + V3.",
            },


            # SECTION 5

            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "Anna can't use her phone because she ___ it.",

                "options": [
                    "has broken",
                    "broke yesterday at 8",
                    "breaks",
                    "is break",
                ],

                "answer":
                    "has broken",

                "explanation":
                    "Важен результат сейчас: телефон сломан.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "We can go home now. We ___ the work.",

                "options": [
                    "have finished",
                    "finish yesterday",
                    "were finish",
                    "has finished",
                ],

                "answer":
                    "have finished",

                "explanation":
                    "Работа закончена, и результат важен сейчас.",
            },


            # SECTION 6

            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Have you ___ been to Italy?",

                "options": [
                    "ever",
                    "never",
                    "yesterday",
                    "ago",
                ],

                "answer":
                    "ever",

                "explanation":
                    "EVER используется в вопросах о жизненном опыте.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I have never tried sushi.",
                    "I haven't never tried sushi.",
                    "I did never tried sushi.",
                    "I have never try sushi.",
                ],

                "answer":
                    "I have never tried sushi.",

                "explanation":
                    "NEVER уже имеет отрицательное значение.",
            },


            # SECTION 7

            {
                "order": 13,
                "section": 7,
                "type": "build",

                "prompt":
                    "Собери предложение с JUST.",

                "options": [
                    "She",
                    "has",
                    "just",
                    "arrived",
                ],

                "answer":
                    "She has just arrived",

                "explanation":
                    "JUST стоит между HAS и V3.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I haven't finished the report ___.",

                "options": [
                    "yet",
                    "already",
                    "just",
                    "yesterday",
                ],

                "answer":
                    "yet",

                "explanation":
                    "YET обычно стоит в конце отрицательного предложения.",
            },


            # SECTION 8

            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Aruzhan is back home. She has ___ to Almaty.",

                "options": [
                    "been",
                    "gone",
                    "went",
                    "going",
                ],

                "answer":
                    "been",

                "explanation":
                    "BEEN TO означает: была там и вернулась.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "Dad isn't home. He has ___ to the shop.",

                "options": [
                    "gone",
                    "been",
                    "went",
                    "go",
                ],

                "answer":
                    "gone",

                "explanation":
                    "GONE TO означает: ушёл и ещё не вернулся.",
            },


            # SECTION 9

            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "I have lived here ___ five years.",

                "options": [
                    "for",
                    "since",
                    "ago",
                    "last",
                ],

                "answer":
                    "for",

                "explanation":
                    "FOR показывает продолжительность.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "She has worked here ___ 2022.",

                "options": [
                    "since",
                    "for",
                    "ago",
                    "during",
                ],

                "answer":
                    "since",

                "explanation":
                    "SINCE показывает начальную точку.",
            },


            # SECTION 10

            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "I ___ this film yesterday.",

                "options": [
                    "saw",
                    "have seen",
                    "have saw",
                    "seen",
                ],

                "answer":
                    "saw",

                "explanation":
                    "YESTERDAY → завершённое прошлое → Past Simple.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "I ___ this film before.",

                "options": [
                    "have seen",
                    "saw yesterday",
                    "have saw",
                    "am seeing",
                ],

                "answer":
                    "have seen",

                "explanation":
                    "Опыт без точного времени → Present Perfect.",
            },

        ]


        # =================================================
        # FINAL TEST
        # 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "Tom ___ already eaten.",

                "options": [
                    "has",
                    "have",
                    "did",
                    "is",
                ],

                "answer":
                    "has",

                "explanation":
                    "Tom = HE → HAS.",
            },

            {
                "order": 22,

                "prompt":
                    "They have ___ the problem.",

                "options": [
                    "solved",
                    "solve",
                    "solving",
                    "did solve",
                ],

                "answer":
                    "solved",

                "explanation":
                    "После HAVE нужна третья форма.",
            },

            {
                "order": 23,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "She hasn't finished yet.",
                    "She doesn't finished yet.",
                    "She hasn't finish yet.",
                    "She didn't finished yet.",
                ],

                "answer":
                    "She hasn't finished yet.",

                "explanation":
                    "Present Perfect negative = HASN'T + V3.",
            },

            {
                "order": 24,

                "prompt":
                    "___ you ever seen snow in May?",

                "options": [
                    "Have",
                    "Did",
                    "Has",
                    "Are",
                ],

                "answer":
                    "Have",

                "explanation":
                    "YOU используется с HAVE.",
            },

            {
                "order": 25,

                "prompt":
                    "Ali is still in Dubai. He has ___ there.",

                "options": [
                    "gone",
                    "been",
                    "went",
                    "go",
                ],

                "answer":
                    "gone",

                "explanation":
                    "Он ещё там → HAS GONE TO.",
            },

            {
                "order": 26,

                "prompt":
                    "We have known each other ___ ten years.",

                "options": [
                    "for",
                    "since",
                    "ago",
                    "last",
                ],

                "answer":
                    "for",

                "explanation":
                    "TEN YEARS — продолжительность → FOR.",
            },

            {
                "order": 27,

                "prompt":
                    "She has lived in Karaganda ___ 2020.",

                "options": [
                    "since",
                    "for",
                    "ago",
                    "from",
                ],

                "answer":
                    "since",

                "explanation":
                    "2020 — начальная точка → SINCE.",
            },

            {
                "order": 28,

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "I saw him last week.",
                    "I have seen him last week.",
                    "I have saw him last week.",
                    "I seen him last week.",
                ],

                "answer":
                    "I saw him last week.",

                "explanation":
                    "LAST WEEK требует Past Simple.",
            },

            {
                "order": 29,

                "prompt":
                    "Choose the sentence about life experience.",

                "options": [
                    "I have visited Japan.",
                    "I visited Japan in 2023.",
                    "I am visiting Japan yesterday.",
                    "I have visited Japan last year.",
                ],

                "answer":
                    "I have visited Japan.",

                "explanation":
                    "Опыт без точного времени → Present Perfect.",
            },

            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sentence.",

                "options": [
                    "She has just finished her work.",
                    "She just has finish her work.",
                    "She has just finish her work.",
                    "She did just finished her work.",
                ],

                "answer":
                    "She has just finished her work.",

                "explanation":
                    "HAS + JUST + V3.",
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


        # Удаляем старые упражнения.
        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        # Удаляем старые секции 11–14.
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
                "✅ Interactive A1 Lesson 30 seeded"
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
