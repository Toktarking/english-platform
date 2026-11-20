from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 52: Types of Questions."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=52,
            defaults={
                "title":
                    "Типы вопросов в английском языке",

                "slug":
                    "types-of-questions",

                "theory_text":
                    "General, special, alternative, subject, "
                    "tag and indirect questions.",

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
                    "General Questions",

                "body":
                    """General Question требует
ответа Yes или No.

Are you tired?

Do you work here?

Did she call?

Have they arrived?

Will he come?

Can you swim?

Главное:

вспомогательный глагол
ставится перед subject.""",
            },


            {
                "order": 2,
                "title":
                    "DO, DOES, DID",

                "body":
                    """Present Simple:

DO / DOES + subject + V1?

Do you work?

Does she work?

Не:

Does she works?

Past Simple:

DID + subject + V1?

Did he go?

Не:

Did he went?""",
            },


            {
                "order": 3,
                "title":
                    "BE и другие auxiliaries",

                "body":
                    """С глаголом BE
DO не нужен.

Are you ready?

Was she at home?

Другие примеры:

Are they working?

Have you finished?

Will she come?

Can he swim?

Auxiliary просто ставится
перед subject.""",
            },


            {
                "order": 4,
                "title":
                    "Special Questions",

                "body":
                    """Special Question начинается
с question word.

WHAT

WHERE

WHEN

WHY

WHO

HOW

Формула:

Question word
+ auxiliary
+ subject
+ verb?

Where do you live?

Why did she leave?""",
            },


            {
                "order": 5,
                "title":
                    "HOW и сочетания",

                "body":
                    """HOW = как?

How are you?

Частые формы:

How old?

How much?

How many?

How often?

How long?

How far?

Примеры:

How many students are there?

How often do you exercise?

How long does it take?""",
            },


            {
                "order": 6,
                "title":
                    "Alternative Questions",

                "body":
                    """Alternative Question
предлагает выбор.

Используем OR.

Do you want
tea or coffee?

Will you go
by bus or by train?

Ответ обычно не Yes / No.

Tea, please.

By train.""",
            },


            {
                "order": 7,
                "title":
                    "Subject Questions",

                "body":
                    """Subject Question спрашивает:

КТО выполняет действие?

Who called you?

Who lives here?

What happened?

Главное правило:

обычно НЕ используем
do / does / did.

Не:

Who did call you?

Правильно:

Who called you?""",
            },


            {
                "order": 8,
                "title":
                    "Subject vs Object Question",

                "body":
                    """Сравни:

Who called Anna?

WHO = subject.

Кто позвонил Анне?

Who did Anna call?

ANNA = subject.

WHO = object.

Кому позвонила Анна?

Если WHO — object,
нужна обычная
question structure.""",
            },


            {
                "order": 9,
                "title":
                    "Tag Questions",

                "body":
                    """Tag Question просит
подтверждение.

You are tired,
aren't you?

She works here,
doesn't she?

He can't swim,
can he?

Правило:

positive sentence
→ negative tag

negative sentence
→ positive tag.""",
            },


            {
                "order": 10,
                "title":
                    "Indirect Questions",

                "body":
                    """Indirect Question звучит
более вежливо.

Direct:

Where is the bank?

Indirect:

Can you tell me
where the bank is?

Важно:

после introductory phrase
используем обычный порядок слов.

Не:

where is the bank

Правильно:

where the bank is.""",
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
                "type": "choice",
                "prompt":
                    "Choose the correct Yes/No question.",
                "options": [
                    "Do you work here?",
                    "You work here?",
                    "Where do you work?",
                    "Who works here?",
                ],
                "answer":
                    "Do you work here?",
                "explanation":
                    "General Question → auxiliary before subject.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "___ she at home?",
                "options": [
                    "Is",
                    "Does",
                    "Do",
                    "Did",
                ],
                "answer":
                    "Is",
                "explanation":
                    "С BE дополнительный DO не нужен.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "___ she speak English?",
                "options": [
                    "Does",
                    "Do",
                    "Is",
                    "Did yesterday",
                ],
                "answer":
                    "Does",
                "explanation":
                    "Present Simple, SHE → DOES.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "Did he ___ to work yesterday?",
                "options": [
                    "go",
                    "went",
                    "gone",
                    "goes",
                ],
                "answer":
                    "go",
                "explanation":
                    "После DID используется V1.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "___ they working now?",
                "options": [
                    "Are",
                    "Do",
                    "Did",
                    "Have work",
                ],
                "answer":
                    "Are",
                "explanation":
                    "Present Continuous → ARE + subject + verb-ing.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "___ you finished the task?",
                "options": [
                    "Have",
                    "Do",
                    "Are",
                    "Did finish",
                ],
                "answer":
                    "Have",
                "explanation":
                    "Present Perfect → HAVE + subject + V3.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "Where ___ you live?",
                "options": [
                    "do",
                    "are",
                    "does",
                    "is",
                ],
                "answer":
                    "do",
                "explanation":
                    "WHERE + DO + YOU + V1.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "Why ___ she leave yesterday?",
                "options": [
                    "did",
                    "does",
                    "is",
                    "has",
                ],
                "answer":
                    "did",
                "explanation":
                    "Yesterday → Past Simple → DID.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "___ students are in the class?",
                "options": [
                    "How many",
                    "How much",
                    "How long",
                    "How often",
                ],
                "answer":
                    "How many",
                "explanation":
                    "Students = countable plural → HOW MANY.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "___ do you exercise?",
                "options": [
                    "How often",
                    "How many",
                    "How far money",
                    "How much times",
                ],
                "answer":
                    "How often",
                "explanation":
                    "HOW OFTEN = как часто.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "Do you want tea ___ coffee?",
                "options": [
                    "or",
                    "and",
                    "because",
                    "but",
                ],
                "answer":
                    "or",
                "explanation":
                    "Alternative Question использует OR.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "Which is an Alternative Question?",
                "options": [
                    "Will you go by bus or by train?",
                    "Will you go by bus?",
                    "Where will you go?",
                    "Who will go?",
                ],
                "answer":
                    "Will you go by bus or by train?",
                "explanation":
                    "В вопросе предлагаются два варианта.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "___ called you last night?",
                "options": [
                    "Who",
                    "Who did",
                    "Who does",
                    "Who was do",
                ],
                "answer":
                    "Who",
                "explanation":
                    "WHO = subject, поэтому DID не нужен.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "Choose the correct Subject Question.",
                "options": [
                    "Who broke the window?",
                    "Who did break the window?",
                    "Who did she call?",
                    "Who does she know?",
                ],
                "answer":
                    "Who broke the window?",
                "explanation":
                    "WHO выполняет действие.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "Which is an Object Question?",
                "options": [
                    "Who did Anna call?",
                    "Who called Anna?",
                    "Who arrived?",
                    "What happened?",
                ],
                "answer":
                    "Who did Anna call?",
                "explanation":
                    "Anna = subject, WHO = object.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "Choose the Subject Question.",
                "options": [
                    "Who saw Tom?",
                    "Who did Tom see?",
                    "Who does Tom know?",
                    "Who did Tom call?",
                ],
                "answer":
                    "Who saw Tom?",
                "explanation":
                    "WHO само выполняет действие SEE.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "You are tired, ___?",
                "options": [
                    "aren't you",
                    "don't you",
                    "are you",
                    "isn't she",
                ],
                "answer":
                    "aren't you",
                "explanation":
                    "Positive ARE → negative AREN'T.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "He doesn't work here, ___?",
                "options": [
                    "does he",
                    "doesn't he",
                    "is he",
                    "did he",
                ],
                "answer":
                    "does he",
                "explanation":
                    "Negative statement → positive tag.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Can you tell me where the bank ___?",
                "options": [
                    "is",
                    "is it",
                    "does be",
                    "does it is",
                ],
                "answer":
                    "is",
                "explanation":
                    "Indirect Question → обычный порядок слов.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Do you know when the lesson ___?",
                "options": [
                    "starts",
                    "does start",
                    "start does",
                    "is start",
                ],
                "answer":
                    "starts",
                "explanation":
                    "После introductory phrase не используем question order.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "Choose the correct Present Simple question.",
                "options": [
                    "Does he work here?",
                    "Does he works here?",
                    "He does work here?",
                    "Is he work here?",
                ],
                "answer":
                    "Does he work here?",
                "explanation":
                    "DOES + subject + V1.",
            },

            {
                "order": 22,
                "prompt":
                    "Choose the correct Past Simple question.",
                "options": [
                    "When did they arrive?",
                    "When did they arrived?",
                    "When they did arrive?",
                    "When do they arrived?",
                ],
                "answer":
                    "When did they arrive?",
                "explanation":
                    "DID + subject + V1.",
            },

            {
                "order": 23,
                "prompt":
                    "___ money do you need?",
                "options": [
                    "How much",
                    "How many",
                    "How often",
                    "How old",
                ],
                "answer":
                    "How much",
                "explanation":
                    "Money = uncountable → HOW MUCH.",
            },

            {
                "order": 24,
                "prompt":
                    "Choose the Alternative Question.",
                "options": [
                    "Do you prefer coffee or tea?",
                    "Do you prefer coffee?",
                    "What do you prefer?",
                    "Who prefers coffee?",
                ],
                "answer":
                    "Do you prefer coffee or tea?",
                "explanation":
                    "Alternative Question предлагает выбор через OR.",
            },

            {
                "order": 25,
                "prompt":
                    "Choose the Subject Question.",
                "options": [
                    "Who opened the door?",
                    "Who did you call?",
                    "Who does she know?",
                    "Who did they invite?",
                ],
                "answer":
                    "Who opened the door?",
                "explanation":
                    "WHO само выполняет действие.",
            },

            {
                "order": 26,
                "prompt":
                    "Choose the Object Question.",
                "options": [
                    "Who did Peter invite?",
                    "Who invited Peter?",
                    "Who arrived first?",
                    "What happened?",
                ],
                "answer":
                    "Who did Peter invite?",
                "explanation":
                    "Peter = subject; WHO = object.",
            },

            {
                "order": 27,
                "prompt":
                    "She can drive, ___?",
                "options": [
                    "can't she",
                    "doesn't she",
                    "can she",
                    "isn't she",
                ],
                "answer":
                    "can't she",
                "explanation":
                    "Positive CAN → negative CAN'T.",
            },

            {
                "order": 28,
                "prompt":
                    "They aren't ready, ___?",
                "options": [
                    "are they",
                    "aren't they",
                    "do they",
                    "were they",
                ],
                "answer":
                    "are they",
                "explanation":
                    "Negative statement → positive tag.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct indirect question.",
                "options": [
                    "Could you tell me where she lives?",
                    "Could you tell me where does she live?",
                    "Could you tell me where she does live?",
                    "Could you tell me where lives she?",
                ],
                "answer":
                    "Could you tell me where she lives?",
                "explanation":
                    "Indirect Question → subject + verb.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "Do you work here? / Where do you work? / Who works here? / Can you tell me where you work?",
                    "Do you work here? / Where you work? / Who does work here? / Can you tell me where do you work?",
                    "Are you work here? / Where does you work? / Who do works here? / Can you tell me where are you work?",
                    "Does you work here? / Where did you works? / Who did works here? / Can you tell me where does you work?",
                ],
                "answer":
                    "Do you work here? / Where do you work? / Who works here? / Can you tell me where you work?",
                "explanation":
                    "General → DO; Special → question word + DO; Subject → no DO; Indirect → normal word order.",
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
                "✅ Interactive A1 Lesson 52 seeded"
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
