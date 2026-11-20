from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 51: Direct and Reported Speech."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=51,
            defaults={
                "title":
                    "Прямая и косвенная речь",

                "slug":
                    "reported-speech",

                "theory_text":
                    "Direct and Reported Speech: "
                    "statements, questions and commands.",

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
                    "Direct Speech и Reported Speech",

                "body":
                    """Direct Speech передаёт
точные слова человека.

Anna said:
"I am tired."

Reported Speech передаёт
смысл этих слов.

Anna said that
she was tired.

Кавычки исчезают,
а некоторые слова меняются.""",
            },


            {
                "order": 2,
                "title":
                    "SAY и TELL",

                "body":
                    """SAY обычно используется
без человека после глагола.

He said that he was tired.

Не:

He said me...

TELL требует человека.

He told me
that he was tired.

Не:

He told that...

SAY + that

TELL + person + that""",
            },


            {
                "order": 3,
                "title":
                    "Present → Past",

                "body":
                    """Если SAY стоит в прошлом,
время часто сдвигается назад.

Present Simple
→ Past Simple

"I work here."

He said that
he worked there.

Present Continuous
→ Past Continuous

"I am working."

He said that
he was working.""",
            },


            {
                "order": 4,
                "title":
                    "Past и Present Perfect",

                "body":
                    """Past Simple
часто становится Past Perfect.

"I saw Anna."

He said that
he had seen Anna.

Present Perfect
тоже становится Past Perfect.

"I have finished."

She said that
she had finished.

Past Perfect обычно
не меняется.""",
            },


            {
                "order": 5,
                "title":
                    "WILL, CAN, MAY",

                "body":
                    """Частые изменения:

will → would

can → could

may → might

"I will call you."

He said that
he would call me.

"I can swim."

She said that
she could swim.""",
            },


            {
                "order": 6,
                "title":
                    "Местоимения",

                "body":
                    """Местоимения меняются
по смыслу.

Ali said:
"I am busy."

Ali said that
he was busy.

Sara said to me:
"You are late."

Sara told me that
I was late.

Нужно понимать:

кто говорит
и кому.""",
            },


            {
                "order": 7,
                "title":
                    "NOW, TODAY, TOMORROW",

                "body":
                    """Частые изменения:

now → then

today → that day

yesterday → the day before

tomorrow → the next day

here → there

this → that

"I'll call tomorrow."

She said that
she would call
the next day.""",
            },


            {
                "order": 8,
                "title":
                    "Yes / No questions",

                "body":
                    """Для вопросов без
question word используем:

ASKED + IF / WHETHER

"Are you tired?"

She asked
if I was tired.

Важно:

в Reported Speech
обычный порядок слов.

Не:

if was I tired

Правильно:

if I was tired.""",
            },


            {
                "order": 9,
                "title":
                    "WH-questions",

                "body":
                    """Question word сохраняется.

"Where do you live?"

She asked
where I lived.

"What are you doing?"

He asked
what I was doing.

DO / DOES / DID
исчезают.

После question word
идёт обычный порядок слов.""",
            },


            {
                "order": 10,
                "title":
                    "Команды и просьбы",

                "body":
                    """Команда:

TELL + person + TO + V1

"Sit down."

The teacher told us
to sit down.

Просьба:

ASK + person + TO + V1

"Please help me."

She asked me
to help her.

Отрицание:

NOT TO + V1

"Don't open it."

He told me
not to open it.""",
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
                    '"I am tired," Anna said. Choose Reported Speech.',
                "options": [
                    "Anna said that she was tired.",
                    "Anna asked if she was tired.",
                    "Anna told that she tired.",
                    "Anna said that I was tired.",
                ],
                "answer":
                    "Anna said that she was tired.",
                "explanation":
                    "Direct Speech превращаем в Reported Speech без кавычек.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "Which sentence is Reported Speech?",
                "options": [
                    "Tom said that he was busy.",
                    'Tom said, "I am busy."',
                    '"I am busy," Tom said.',
                    '"Are you busy?" Tom asked.',
                ],
                "answer":
                    "Tom said that he was busy.",
                "explanation":
                    "Reported Speech передаёт смысл без кавычек.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "Choose the correct sentence with TELL.",
                "options": [
                    "She told me that she was tired.",
                    "She told that she was tired.",
                    "She said me that she was tired.",
                    "She told me she is tired yesterday.",
                ],
                "answer":
                    "She told me that she was tired.",
                "explanation":
                    "TELL требует объект: told me.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "Choose the correct sentence with SAY.",
                "options": [
                    "He said that he was busy.",
                    "He said me that he was busy.",
                    "He told that he was busy.",
                    "He said me he busy.",
                ],
                "answer":
                    "He said that he was busy.",
                "explanation":
                    "SAY обычно не требует человека сразу после глагола.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    '"I work at home," he said.',
                "options": [
                    "He said that he worked at home.",
                    "He said that he works yesterday.",
                    "He told that he worked at home.",
                    "He asked if he worked at home.",
                ],
                "answer":
                    "He said that he worked at home.",
                "explanation":
                    "Present Simple → Past Simple.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    '"I am studying," she said.',
                "options": [
                    "She said that she was studying.",
                    "She said that she studied now.",
                    "She said that she is studied.",
                    "She asked if she was study.",
                ],
                "answer":
                    "She said that she was studying.",
                "explanation":
                    "Present Continuous → Past Continuous.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    '"I saw the film," he said.',
                "options": [
                    "He said that he had seen the film.",
                    "He said that he had saw the film.",
                    "He said that he has seen the film.",
                    "He told that he had seen the film.",
                ],
                "answer":
                    "He said that he had seen the film.",
                "explanation":
                    "Past Simple → Past Perfect; SEE → SEEN.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    '"I have finished the work," she said.',
                "options": [
                    "She said that she had finished the work.",
                    "She said that she has finish the work.",
                    "She said that she finished tomorrow.",
                    "She asked if she had finished the work.",
                ],
                "answer":
                    "She said that she had finished the work.",
                "explanation":
                    "Present Perfect → Past Perfect.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    '"I will call you," he said.',
                "options": [
                    "He said that he would call me.",
                    "He said that he will called me.",
                    "He told that he would call me.",
                    "He said that he would called me.",
                ],
                "answer":
                    "He said that he would call me.",
                "explanation":
                    "WILL → WOULD.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    '"I can help you," she said.',
                "options": [
                    "She said that she could help me.",
                    "She said that she can helped me.",
                    "She told that she could help me.",
                    "She said that she could to help me.",
                ],
                "answer":
                    "She said that she could help me.",
                "explanation":
                    "CAN → COULD.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    'Ali said, "I am hungry."',
                "options": [
                    "Ali said that he was hungry.",
                    "Ali said that I was hungry.",
                    "Ali told that he was hungry.",
                    "Ali asked if he was hungry.",
                ],
                "answer":
                    "Ali said that he was hungry.",
                "explanation":
                    "I относится к Ali, поэтому меняется на HE.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    'Sara said to me, "You are late."',
                "options": [
                    "Sara told me that I was late.",
                    "Sara said me that you were late.",
                    "Sara told that I was late.",
                    "Sara asked me if she was late.",
                ],
                "answer":
                    "Sara told me that I was late.",
                "explanation":
                    "YOU относится к слушателю, поэтому здесь → I.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    '"I will call you tomorrow," she said.',
                "options": [
                    "She said that she would call me the next day.",
                    "She said that she will call me yesterday.",
                    "She told that she would call tomorrow.",
                    "She said that she would called me the next day.",
                ],
                "answer":
                    "She said that she would call me the next day.",
                "explanation":
                    "WILL → WOULD; TOMORROW → THE NEXT DAY.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    '"I saw him yesterday," he said.',
                "options": [
                    "He said that he had seen him the day before.",
                    "He said that he saw him the next day.",
                    "He said that he had saw him yesterday.",
                    "He asked if he had seen him tomorrow.",
                ],
                "answer":
                    "He said that he had seen him the day before.",
                "explanation":
                    "YESTERDAY → THE DAY BEFORE.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    '"Are you ready?" she asked.',
                "options": [
                    "She asked if I was ready.",
                    "She asked if was I ready.",
                    "She said if I was ready.",
                    "She told me was I ready.",
                ],
                "answer":
                    "She asked if I was ready.",
                "explanation":
                    "Yes/No question → ASKED IF + обычный порядок слов.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    '"Did Tom call?" he asked.',
                "options": [
                    "He asked whether Tom had called.",
                    "He asked whether had Tom called.",
                    "He said whether Tom called.",
                    "He asked did Tom call.",
                ],
                "answer":
                    "He asked whether Tom had called.",
                "explanation":
                    "DID исчезает; Past Simple → Past Perfect.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    '"Where do you live?" she asked.',
                "options": [
                    "She asked where I lived.",
                    "She asked where did I live.",
                    "She asked where do I live.",
                    "She said where I lived.",
                ],
                "answer":
                    "She asked where I lived.",
                "explanation":
                    "WH-word сохраняется, но порядок слов становится обычным.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    '"What are you doing?" he asked.',
                "options": [
                    "He asked what I was doing.",
                    "He asked what was I doing.",
                    "He asked what did I do.",
                    "He said what I was doing.",
                ],
                "answer":
                    "He asked what I was doing.",
                "explanation":
                    "После WHAT используется subject + verb.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    '"Please wait here," she said.',
                "options": [
                    "She asked me to wait there.",
                    "She said me wait there.",
                    "She asked if I waited there.",
                    "She told that I wait here.",
                ],
                "answer":
                    "She asked me to wait there.",
                "explanation":
                    "Просьба → ASK + person + TO + V1.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    '"Don\'t open the door," he said.',
                "options": [
                    "He told me not to open the door.",
                    "He told me don't open the door.",
                    "He said me not open the door.",
                    "He asked if I didn't open the door.",
                ],
                "answer":
                    "He told me not to open the door.",
                "explanation":
                    "Отрицательная команда → NOT TO + V1.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    '"I live in London," Kate said.',
                "options": [
                    "Kate said that she lived in London.",
                    "Kate told that she lived in London.",
                    "Kate said that I lived in London.",
                    "Kate asked if she lived in London.",
                ],
                "answer":
                    "Kate said that she lived in London.",
                "explanation":
                    "Present Simple → Past Simple; I → SHE.",
            },

            {
                "order": 22,
                "prompt":
                    '"I am watching TV now," Ben said.',
                "options": [
                    "Ben said that he was watching TV then.",
                    "Ben said that he watched TV tomorrow.",
                    "Ben told that he was watching TV now.",
                    "Ben asked if he watched TV then.",
                ],
                "answer":
                    "Ben said that he was watching TV then.",
                "explanation":
                    "Present Continuous → Past Continuous; NOW → THEN.",
            },

            {
                "order": 23,
                "prompt":
                    '"I may visit you tomorrow," Lisa said.',
                "options": [
                    "Lisa said that she might visit me the next day.",
                    "Lisa said that she may visited me tomorrow.",
                    "Lisa told that she might visit me the next day.",
                    "Lisa said that she might visited me the next day.",
                ],
                "answer":
                    "Lisa said that she might visit me the next day.",
                "explanation":
                    "MAY → MIGHT; TOMORROW → THE NEXT DAY.",
            },

            {
                "order": 24,
                "prompt":
                    '"We finished the project," they said.',
                "options": [
                    "They said that they had finished the project.",
                    "They said that we had finished the project.",
                    "They told that they finished the project.",
                    "They asked if they had finished the project.",
                ],
                "answer":
                    "They said that they had finished the project.",
                "explanation":
                    "Past Simple → Past Perfect; WE → THEY.",
            },

            {
                "order": 25,
                "prompt":
                    '"Can you drive?" Tom asked me.',
                "options": [
                    "Tom asked me if I could drive.",
                    "Tom asked me could I drive.",
                    "Tom told me if I can drive.",
                    "Tom said whether could I drive.",
                ],
                "answer":
                    "Tom asked me if I could drive.",
                "explanation":
                    "Yes/No question → IF; CAN → COULD.",
            },

            {
                "order": 26,
                "prompt":
                    '"Why are you laughing?" she asked.',
                "options": [
                    "She asked why I was laughing.",
                    "She asked why was I laughing.",
                    "She asked why did I laugh.",
                    "She said why I was laughing.",
                ],
                "answer":
                    "She asked why I was laughing.",
                "explanation":
                    "WHY сохраняется, далее обычный порядок слов.",
            },

            {
                "order": 27,
                "prompt":
                    '"Please close the window," the teacher said.',
                "options": [
                    "The teacher asked me to close the window.",
                    "The teacher asked me close the window.",
                    "The teacher said me to close the window.",
                    "The teacher asked if I closed the window.",
                ],
                "answer":
                    "The teacher asked me to close the window.",
                "explanation":
                    "Просьба → ASK + person + TO + V1.",
            },

            {
                "order": 28,
                "prompt":
                    '"Don\'t be late," my mother said.',
                "options": [
                    "My mother told me not to be late.",
                    "My mother told me don't be late.",
                    "My mother said me not to be late.",
                    "My mother asked if I wasn't late.",
                ],
                "answer":
                    "My mother told me not to be late.",
                "explanation":
                    "Отрицательная команда → TOLD + person + NOT TO.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct SAY / TELL pair.",
                "options": [
                    "He said that he was tired. / He told me that he was tired.",
                    "He said me that he was tired. / He told that he was tired.",
                    "He told that he was tired. / He said me he was tired.",
                    "He said to that he was tired. / He told me he tired.",
                ],
                "answer":
                    "He said that he was tired. / He told me that he was tired.",
                "explanation":
                    "SAY без объекта; TELL + person.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "She said that she was busy. / He asked if I was ready. / She asked where I lived. / He told me not to leave.",
                    "She said me that she was busy. / He asked was I ready. / She asked where did I live. / He told me don't leave.",
                    "She told that she was busy. / He asked if was I ready. / She asked where do I live. / He said me not leave.",
                    "She said that she busy. / He told if I ready. / She asked where I did live. / He told that not to leave.",
                ],
                "answer":
                    "She said that she was busy. / He asked if I was ready. / She asked where I lived. / He told me not to leave.",
                "explanation":
                    "Statement → said that; Yes/No → asked if; WH-question → normal word order; command → told + person + not to.",
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


        # Удаляем старые лишние упражнения
        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        # Удаляем старые Sections 11–14
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
                "✅ Interactive A1 Lesson 51 seeded"
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
