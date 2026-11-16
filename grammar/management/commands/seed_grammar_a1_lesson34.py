from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 34: Past Perfect."
    )


    def handle(self, *args, **options):

        lesson, _ = (
            GrammarLesson.objects.update_or_create(
                level="A1",
                order=34,

                defaults={
                    "title":
                        "Past Perfect",

                    "slug":
                        "past-perfect",

                    "theory_text":
                        "Past Perfect: HAD + third form.",

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
                    "Прошлое до прошлого",

                "body":
                    """Past Perfect показывает действие,
которое произошло раньше другого
действия в прошлом.

I had finished the work
before he arrived.

Сначала:

I had finished the work.

Потом:

he arrived.

Главная схема:

раньше → Past Perfect

позже → Past Simple.""",
            },


            {
                "order": 2,
                "title":
                    "Формула HAD + V3",

                "body":
                    """Формула Past Perfect:

HAD + третья форма глагола

I had finished.

She had arrived.

They had gone.

HAD одинаков для всех:

I
you
he
she
it
we
they

Никаких HAVE или HAS
в Past Perfect нет.""",
            },


            {
                "order": 3,
                "title":
                    "Нужна третья форма",

                "body":
                    """После HAD всегда используется V3.

Правильные глаголы:

finish → finished
work → worked

Неправильные:

go → went → gone

see → saw → seen

write → wrote → written

eat → ate → eaten

Правильно:

had gone

had seen

had written

Не:

had went
had saw
had wrote.""",
            },


            {
                "order": 4,
                "title":
                    "Два события в прошлом",

                "body":
                    """Когда есть два события,
Past Perfect показывает,
какое произошло первым.

When I arrived,
they had left.

Порядок событий:

1. They left.
2. I arrived.

Даже если в предложении
ARRIVED стоит первым,
форма HAD LEFT показывает,
что уход произошёл раньше.""",
            },


            {
                "order": 5,
                "title":
                    "BEFORE и AFTER",

                "body":
                    """BEFORE = до того как.

She had finished the report
before she went home.

AFTER = после того как.

After she had finished the report,
she went home.

В обоих случаях:

более раннее действие
→ Past Perfect

более позднее
→ Past Simple.""",
            },


            {
                "order": 6,
                "title":
                    "BY THE TIME",

                "body":
                    """BY THE TIME означает:

к тому времени как.

By the time I arrived,
the meeting had started.

Сначала:

the meeting started.

Потом:

I arrived.

Ещё пример:

By the time we reached the airport,
the plane had left.""",
            },


            {
                "order": 7,
                "title":
                    "ALREADY, JUST и NEVER",

                "body":
                    """Эти слова часто используются
с Past Perfect.

ALREADY:

They had already eaten.

JUST:

She had just left
when I called.

NEVER:

I had never seen snow
before that trip.

ALREADY / JUST обычно стоят
между HAD и V3.""",
            },


            {
                "order": 8,
                "title":
                    "Отрицание",

                "body":
                    """Отрицание:

HAD NOT

или

HADN'T

I hadn't finished.

She hadn't arrived.

They hadn't eaten.

После HADN'T тоже нужна V3.

Правильно:

hadn't gone

Не:

hadn't went.""",
            },


            {
                "order": 9,
                "title":
                    "Вопросы",

                "body":
                    """В вопросе HAD ставится
перед подлежащим.

Had you finished?

Had she arrived?

Had they left?

Краткие ответы:

Yes, I had.

No, I hadn't.

Yes, she had.

No, she hadn't.

DID здесь не нужен.""",
            },


            {
                "order": 10,
                "title":
                    "Когда Past Perfect не нужен?",

                "body":
                    """Не каждое прошлое действие
нужно ставить в Past Perfect.

Если события просто идут
одно за другим:

I woke up,
had breakfast
and went to work.

→ Past Simple.

Past Perfect нужен,
когда мы возвращаемся
к более раннему событию:

I arrived late because
I had missed the bus.

Сначала пропустил автобус,
потом опоздал.""",
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

            # SECTION 1

            {
                "order": 1,
                "section": 1,
                "type": "choice",

                "prompt":
                    "When I arrived, they ___ home.",

                "options": [
                    "had gone",
                    "went after me",
                    "have gone",
                    "had went",
                ],

                "answer":
                    "had gone",

                "explanation":
                    "Они ушли раньше моего приезда.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",

                "prompt":
                    "I was hungry because I ___ breakfast.",

                "options": [
                    "hadn't eaten",
                    "haven't eaten",
                    "didn't ate",
                    "hadn't ate",
                ],

                "answer":
                    "hadn't eaten",

                "explanation":
                    "Отсутствие завтрака произошло раньше состояния hungry.",
            },


            # SECTION 2

            {
                "order": 3,
                "section": 2,
                "type": "build",

                "prompt":
                    "Собери Past Perfect.",

                "options": [
                    "She",
                    "had",
                    "finished",
                    "the",
                    "report",
                ],

                "answer":
                    "She had finished the report",

                "explanation":
                    "Past Perfect = HAD + V3.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",

                "prompt":
                    "Choose the correct sentence.",

                "options": [
                    "They had arrived.",
                    "They have arrived yesterday.",
                    "They had arrive.",
                    "They did had arrived.",
                ],

                "answer":
                    "They had arrived.",

                "explanation":
                    "HAD используется со всеми подлежащими.",
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
                    "She had ___ the message.",

                "options": [
                    "seen",
                    "saw",
                    "see",
                    "seeing",
                ],

                "answer":
                    "seen",

                "explanation":
                    "SEE → SAW → SEEN.",
            },


            # SECTION 4

            {
                "order": 7,
                "section": 4,
                "type": "choice",

                "prompt":
                    "When we reached the station, the train ___.",

                "options": [
                    "had left",
                    "has left",
                    "leave",
                    "had leave",
                ],

                "answer":
                    "had left",

                "explanation":
                    "Поезд ушёл раньше нашего приезда.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",

                "prompt":
                    "When I entered the room, the lesson ___.",

                "options": [
                    "had started",
                    "has started",
                    "start",
                    "had start",
                ],

                "answer":
                    "had started",

                "explanation":
                    "Урок начался до того, как я вошёл.",
            },


            # SECTION 5

            {
                "order": 9,
                "section": 5,
                "type": "choice",

                "prompt":
                    "She had eaten before she ___ home.",

                "options": [
                    "went",
                    "had went",
                    "has gone",
                    "go",
                ],

                "answer":
                    "went",

                "explanation":
                    "Более позднее действие обычно стоит в Past Simple.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",

                "prompt":
                    "After he ___ the work, he left the office.",

                "options": [
                    "had finished",
                    "has finished",
                    "had finish",
                    "finishes",
                ],

                "answer":
                    "had finished",

                "explanation":
                    "Сначала закончил работу, потом ушёл.",
            },


            # SECTION 6

            {
                "order": 11,
                "section": 6,
                "type": "choice",

                "prompt":
                    "By the time we arrived, the film ___.",

                "options": [
                    "had started",
                    "started after us",
                    "has started",
                    "had start",
                ],

                "answer":
                    "had started",

                "explanation":
                    "BY THE TIME показывает действие, завершившееся раньше.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",

                "prompt":
                    "By the time she called, I ___ the office.",

                "options": [
                    "had left",
                    "have left",
                    "leave",
                    "had leave",
                ],

                "answer":
                    "had left",

                "explanation":
                    "Уход произошёл до звонка.",
            },


            # SECTION 7

            {
                "order": 13,
                "section": 7,
                "type": "choice",

                "prompt":
                    "They had ___ eaten when we arrived.",

                "options": [
                    "already",
                    "ago",
                    "last",
                    "yesterday",
                ],

                "answer":
                    "already",

                "explanation":
                    "ALREADY обычно стоит между HAD и V3.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",

                "prompt":
                    "I had ___ seen the ocean before that trip.",

                "options": [
                    "never",
                    "ago",
                    "last",
                    "yet yesterday",
                ],

                "answer":
                    "never",

                "explanation":
                    "HAD NEVER SEEN = до того момента никогда не видел.",
            },


            # SECTION 8

            {
                "order": 15,
                "section": 8,
                "type": "choice",

                "prompt":
                    "He ___ finished the report when the manager came.",

                "options": [
                    "hadn't",
                    "didn't had",
                    "hasn't",
                    "wasn't",
                ],

                "answer":
                    "hadn't",

                "explanation":
                    "Отрицание Past Perfect = HADN'T + V3.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",

                "prompt":
                    "She hadn't ___ before the trip.",

                "options": [
                    "flown",
                    "flew",
                    "fly",
                    "flying",
                ],

                "answer":
                    "flown",

                "explanation":
                    "FLY → FLEW → FLOWN.",
            },


            # SECTION 9

            {
                "order": 17,
                "section": 9,
                "type": "choice",

                "prompt":
                    "___ they finished before you arrived?",

                "options": [
                    "Had",
                    "Did",
                    "Have",
                    "Were",
                ],

                "answer":
                    "Had",

                "explanation":
                    "Вопрос Past Perfect начинается с HAD.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",

                "prompt":
                    "Had she seen the film?",

                "options": [
                    "Yes, she had.",
                    "Yes, she did.",
                    "Yes, she has.",
                    "Yes, she was.",
                ],

                "answer":
                    "Yes, she had.",

                "explanation":
                    "Краткий ответ повторяет HAD.",
            },


            # SECTION 10

            {
                "order": 19,
                "section": 10,
                "type": "choice",

                "prompt":
                    "Choose the natural sequence.",

                "options": [
                    "I woke up, ate breakfast and left.",
                    "I had woken up, had eaten and had left.",
                    "I had wake up and went.",
                    "I woke up, had ate and had went.",
                ],

                "answer":
                    "I woke up, ate breakfast and left.",

                "explanation":
                    "Обычная последовательность событий → Past Simple.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",

                "prompt":
                    "I was late because I ___ the bus.",

                "options": [
                    "had missed",
                    "have missed",
                    "missed later",
                    "had miss",
                ],

                "answer":
                    "had missed",

                "explanation":
                    "Автобус был пропущен раньше, чем человек опоздал.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,

                "prompt":
                    "When I got home, my family ___ dinner.",

                "options": [
                    "had already eaten",
                    "has already eaten",
                    "had already ate",
                    "already eat",
                ],

                "answer":
                    "had already eaten",

                "explanation":
                    "Ужин произошёл до возвращения домой.",
            },

            {
                "order": 22,

                "prompt":
                    "She couldn't enter because she ___ her key.",

                "options": [
                    "had forgotten",
                    "has forgotten",
                    "had forgot",
                    "forget",
                ],

                "answer":
                    "had forgotten",

                "explanation":
                    "Ключ был забыт раньше возникшей проблемы.",
            },

            {
                "order": 23,

                "prompt":
                    "Before we arrived, they ___ the room.",

                "options": [
                    "had cleaned",
                    "have cleaned",
                    "had clean",
                    "cleaning",
                ],

                "answer":
                    "had cleaned",

                "explanation":
                    "Уборка завершилась до нашего прихода.",
            },

            {
                "order": 24,

                "prompt":
                    "By eight o'clock, he ___ the presentation.",

                "options": [
                    "had prepared",
                    "was prepare",
                    "has prepared",
                    "had prepare",
                ],

                "answer":
                    "had prepared",

                "explanation":
                    "BY EIGHT → действие было завершено к прошлому моменту.",
            },

            {
                "order": 25,

                "prompt":
                    "Choose the correct negative sentence.",

                "options": [
                    "We hadn't seen the message.",
                    "We didn't had seen the message.",
                    "We hadn't saw the message.",
                    "We haven't saw the message.",
                ],

                "answer":
                    "We hadn't seen the message.",

                "explanation":
                    "HADN'T + V3.",
            },

            {
                "order": 26,

                "prompt":
                    "Choose the correct question.",

                "options": [
                    "Had you met him before?",
                    "Did you had met him before?",
                    "Had you meet him before?",
                    "Have you met him yesterday before?",
                ],

                "answer":
                    "Had you met him before?",

                "explanation":
                    "HAD + subject + V3.",
            },

            {
                "order": 27,

                "prompt":
                    "When the police arrived, the thief ___.",

                "options": [
                    "had escaped",
                    "has escaped",
                    "had escape",
                    "escapes",
                ],

                "answer":
                    "had escaped",

                "explanation":
                    "Побег произошёл раньше приезда полиции.",
            },

            {
                "order": 28,

                "prompt":
                    "Which sentence means she left BEFORE I arrived?",

                "options": [
                    "When I arrived, she had left.",
                    "When I arrived, she left.",
                    "When I arrived, she leaves.",
                    "When I had arrived, she has left.",
                ],

                "answer":
                    "When I arrived, she had left.",

                "explanation":
                    "HAD LEFT показывает более раннее действие.",
            },

            {
                "order": 29,

                "prompt":
                    "Choose the correct pair.",

                "options": [
                    "At six, he was working. / By six, he had finished.",
                    "At six, he had working. / By six, he was finished.",
                    "At six, he has worked. / By six, he had finish.",
                    "At six, he worked now. / By six, he has finished.",
                ],

                "answer":
                    "At six, he was working. / By six, he had finished.",

                "explanation":
                    "AT = процесс в момент; BY = результат к моменту.",
            },

            {
                "order": 30,

                "prompt":
                    "Choose the fully correct sequence.",

                "options": [
                    "After she had finished the exam, she went home.",
                    "After she has finished the exam, she went home.",
                    "After she had finish the exam, she had went home.",
                    "After she finished had the exam, she gone home.",
                ],

                "answer":
                    "After she had finished the exam, she went home.",

                "explanation":
                    "Более раннее действие → Past Perfect; позднее → Past Simple.",
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
                "✅ Interactive A1 Lesson 34 seeded"
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
