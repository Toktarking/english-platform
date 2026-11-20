from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 54: Relative Pronouns."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=54,
            defaults={
                "title":
                    "Относительные местоимения: who, which, that, whose",

                "slug":
                    "relative-pronouns-who-which-that-whose",

                "theory_text":
                    "Relative pronouns: who, which, that and whose.",

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
                    "Что такое Relative Clause",

                "body":
                    """Relative Clause помогает
добавить информацию
о человеке или предмете.

The man is my teacher.

He lives next door.

Можно соединить:

The man who lives
next door is my teacher.

WHO связывает
две части предложения.""",
            },


            {
                "order": 2,
                "title":
                    "WHO — люди",

                "body":
                    """WHO используем
для людей.

The woman who works here
is very kind.

The student who answered
was correct.

The man who called me
is my uncle.

WHO = который / которая /
которые, если речь о людях.""",
            },


            {
                "order": 3,
                "title":
                    "WHICH — предметы",

                "body":
                    """WHICH используем
для предметов и животных.

The book which is
on the table is mine.

The car which broke down
belongs to my brother.

The dog which barked
all night is ours.

WHICH = который,
если речь не о человеке.""",
            },


            {
                "order": 4,
                "title":
                    "THAT",

                "body":
                    """THAT можно использовать
для людей и предметов
в defining clauses.

The man that called me...

The book that I bought...

Для людей часто естественнее WHO.

Для предметов:

WHICH или THAT.

The phone that I bought
is expensive.""",
            },


            {
                "order": 5,
                "title":
                    "WHOSE — принадлежность",

                "body":
                    """WHOSE показывает
принадлежность.

Значение:

чей / чья / чьи.

The woman whose car
was stolen called the police.

I know a student
whose father is a doctor.

После WHOSE обычно
сразу идёт noun:

whose car
whose father
whose house""",
            },


            {
                "order": 6,
                "title":
                    "Relative Pronoun как Subject",

                "body":
                    """Relative pronoun может
сам выполнять действие.

The man who lives here...

WHO = subject.

The book which is
on the table...

WHICH = subject.

Если после WHO / WHICH
сразу идёт verb,
relative pronoun обычно
является subject.""",
            },


            {
                "order": 7,
                "title":
                    "Relative Pronoun как Object",

                "body":
                    """Relative pronoun может
быть object.

The man who I met...

I = subject.

WHO = object.

The book which I bought...

I = subject.

WHICH = object.

Подсказка:

who + I/he/she/we/they
→ часто object.""",
            },


            {
                "order": 8,
                "title":
                    "Когда можно убрать pronoun",

                "body":
                    """Если relative pronoun
является object,
его часто можно убрать.

The man who I met...

=

The man I met...

The book which I bought...

=

The book I bought...

Но если pronoun = subject,
убирать его нельзя.""",
            },


            {
                "order": 9,
                "title":
                    "Defining и commas",

                "body":
                    """Defining clause даёт
важную информацию.

The man who lives next door
is a doctor.

Запятые обычно не нужны.

Дополнительная информация:

My brother,
who lives in Astana,
is a doctor.

После запятых
THAT не используем.

Используем WHO или WHICH.""",
            },


            {
                "order": 10,
                "title":
                    "Как выбрать слово",

                "body":
                    """Главная схема:

person
→ WHO / THAT

thing
→ WHICH / THAT

possession
→ WHOSE

После запятой:

WHO / WHICH

не THAT.

Если pronoun = object,
его иногда можно убрать.

Если pronoun = subject,
убирать нельзя.""",
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
                    "Choose the sentence with a Relative Clause.",
                "options": [
                    "The man who lives here is my teacher.",
                    "The man lives here.",
                    "Is the man your teacher?",
                    "The man is very tall.",
                ],
                "answer":
                    "The man who lives here is my teacher.",
                "explanation":
                    "WHO соединяет информацию о человеке.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "The woman ___ works here is my aunt.",
                "options": [
                    "who",
                    "which",
                    "where",
                    "when",
                ],
                "answer":
                    "who",
                "explanation":
                    "Woman = человек → WHO.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "choice",
                "prompt":
                    "The student ___ answered first got a prize.",
                "options": [
                    "who",
                    "which",
                    "whose answer",
                    "where",
                ],
                "answer":
                    "who",
                "explanation":
                    "Student = человек.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "The man ___ called me is my neighbour.",
                "options": [
                    "who",
                    "which",
                    "whose",
                    "when",
                ],
                "answer":
                    "who",
                "explanation":
                    "Man = человек → WHO.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "The book ___ is on the desk is mine.",
                "options": [
                    "which",
                    "who",
                    "whose",
                    "where",
                ],
                "answer":
                    "which",
                "explanation":
                    "Book = предмет → WHICH.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "The car ___ broke down is very old.",
                "options": [
                    "which",
                    "who",
                    "whose",
                    "when",
                ],
                "answer":
                    "which",
                "explanation":
                    "Car = предмет → WHICH.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "The phone ___ I bought is expensive.",
                "options": [
                    "that",
                    "who",
                    "whose",
                    "where",
                ],
                "answer":
                    "that",
                "explanation":
                    "Для предмета в defining clause можно использовать THAT.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "The teacher ___ helped me was patient.",
                "options": [
                    "that",
                    "where",
                    "when",
                    "whose teacher",
                ],
                "answer":
                    "that",
                "explanation":
                    "THAT может использоваться для человека в defining clause.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "The girl ___ brother is my friend lives here.",
                "options": [
                    "whose",
                    "who",
                    "which",
                    "that she",
                ],
                "answer":
                    "whose",
                "explanation":
                    "Brother принадлежит girl → WHOSE.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "The man ___ car is outside is my boss.",
                "options": [
                    "whose",
                    "who",
                    "which",
                    "that",
                ],
                "answer":
                    "whose",
                "explanation":
                    "Car принадлежит man → WHOSE CAR.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "In 'The woman who works here...', WHO is:",
                "options": [
                    "the subject",
                    "the object",
                    "a possessive adjective",
                    "an auxiliary verb",
                ],
                "answer":
                    "the subject",
                "explanation":
                    "WHO само выполняет действие WORKS.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "Which relative pronoun cannot be removed?",
                "options": [
                    "The man who lives here...",
                    "The man who I met...",
                    "The book which I bought...",
                    "The film that we watched...",
                ],
                "answer":
                    "The man who lives here...",
                "explanation":
                    "WHO = subject, поэтому убрать его нельзя.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "In 'The man who I met...', WHO is:",
                "options": [
                    "the object",
                    "the subject",
                    "the main verb",
                    "an auxiliary verb",
                ],
                "answer":
                    "the object",
                "explanation":
                    "I выполняет действие MET; WHO = object.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "The book which Anna bought was expensive. Who is the subject of BOUGHT?",
                "options": [
                    "Anna",
                    "which",
                    "the book",
                    "expensive",
                ],
                "answer":
                    "Anna",
                "explanation":
                    "Anna выполняет действие, WHICH = object.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "Which sentence is correct?",
                "options": [
                    "The film we watched was excellent.",
                    "The film watched was excellent.",
                    "The film who watched was excellent.",
                    "The film we watched it was excellent.",
                ],
                "answer":
                    "The film we watched was excellent.",
                "explanation":
                    "Object relative pronoun можно опустить.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "Which sentence is NOT correct?",
                "options": [
                    "The man lives next door is a doctor.",
                    "The man who lives next door is a doctor.",
                    "The book I bought is useful.",
                    "The phone we ordered arrived.",
                ],
                "answer":
                    "The man lives next door is a doctor.",
                "explanation":
                    "WHO является subject и не может быть удалено.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "Choose the correct non-defining clause.",
                "options": [
                    "My sister, who lives in Astana, is a doctor.",
                    "My sister, that lives in Astana, is a doctor.",
                    "My sister which lives in Astana is a doctor.",
                    "My sister, whose lives in Astana, is a doctor.",
                ],
                "answer":
                    "My sister, who lives in Astana, is a doctor.",
                "explanation":
                    "После запятых для человека используем WHO, не THAT.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "My car, ___ is ten years old, still works well.",
                "options": [
                    "which",
                    "that",
                    "who",
                    "whose car",
                ],
                "answer":
                    "which",
                "explanation":
                    "После запятой для предмета → WHICH.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Choose the correct pair.",
                "options": [
                    "person → who / thing → which",
                    "person → which / thing → who",
                    "person → where / thing → who",
                    "person → when / thing → whose",
                ],
                "answer":
                    "person → who / thing → which",
                "explanation":
                    "WHO для людей; WHICH для предметов.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "Which word shows possession?",
                "options": [
                    "whose",
                    "who",
                    "which",
                    "that",
                ],
                "answer":
                    "whose",
                "explanation":
                    "WHOSE = чей / чья / чьи.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "The doctor ___ treated me was very kind.",
                "options": [
                    "who",
                    "which",
                    "whose",
                    "where",
                ],
                "answer":
                    "who",
                "explanation":
                    "Doctor = человек → WHO.",
            },

            {
                "order": 22,
                "prompt":
                    "The computer ___ is in my office is new.",
                "options": [
                    "which",
                    "who",
                    "whose",
                    "when",
                ],
                "answer":
                    "which",
                "explanation":
                    "Computer = предмет → WHICH.",
            },

            {
                "order": 23,
                "prompt":
                    "The woman ___ daughter studies here is a teacher.",
                "options": [
                    "whose",
                    "who",
                    "which",
                    "that she",
                ],
                "answer":
                    "whose",
                "explanation":
                    "Daughter принадлежит woman → WHOSE.",
            },

            {
                "order": 24,
                "prompt":
                    "The jacket ___ I bought yesterday is too small.",
                "options": [
                    "that",
                    "who",
                    "whose",
                    "where",
                ],
                "answer":
                    "that",
                "explanation":
                    "Jacket = предмет; THAT возможно в defining clause.",
            },

            {
                "order": 25,
                "prompt":
                    "Which relative pronoun is the subject?",
                "options": [
                    "The woman who works here...",
                    "The woman who I called...",
                    "The book which I bought...",
                    "The film that we watched...",
                ],
                "answer":
                    "The woman who works here...",
                "explanation":
                    "WHO само выполняет действие WORKS.",
            },

            {
                "order": 26,
                "prompt":
                    "Which sentence correctly omits the relative pronoun?",
                "options": [
                    "The man I met was friendly.",
                    "The man lives here is friendly.",
                    "The book is on the table is mine.",
                    "The student answered was correct.",
                ],
                "answer":
                    "The man I met was friendly.",
                "explanation":
                    "Relative pronoun был object, поэтому его можно убрать.",
            },

            {
                "order": 27,
                "prompt":
                    "Choose the sentence without a redundant pronoun.",
                "options": [
                    "The phone that I bought is expensive.",
                    "The phone that I bought it is expensive.",
                    "The phone which I bought it is expensive.",
                    "The phone who I bought is expensive.",
                ],
                "answer":
                    "The phone that I bought is expensive.",
                "explanation":
                    "После THAT дополнительное IT не нужно.",
            },

            {
                "order": 28,
                "prompt":
                    "My uncle, ___ lives in London, is visiting us.",
                "options": [
                    "who",
                    "that",
                    "which",
                    "whose uncle",
                ],
                "answer":
                    "who",
                "explanation":
                    "Non-defining clause + person → WHO.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct WHOSE sentence.",
                "options": [
                    "The student whose laptop is broken is absent.",
                    "The student who's laptop is broken is absent.",
                    "The student who laptop is broken is absent.",
                    "The student which laptop is broken is absent.",
                ],
                "answer":
                    "The student whose laptop is broken is absent.",
                "explanation":
                    "WHOSE + noun показывает принадлежность.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct sequence.",
                "options": [
                    "person → who / thing → which / defining person or thing → that / possession → whose",
                    "person → which / thing → who / possession → that / after comma → that",
                    "person → whose / thing → who / possession → which / subject pronoun can always be omitted",
                    "person → where / thing → when / possession → who / after comma → that",
                ],
                "answer":
                    "person → who / thing → which / defining person or thing → that / possession → whose",
                "explanation":
                    "Это основная система выбора Relative Pronouns.",
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
                "✅ Interactive A1 Lesson 54 seeded"
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
