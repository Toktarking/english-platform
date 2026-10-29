from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 54: "
        "Relative Pronouns."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=54,
            defaults={
                "title": (
                    "Относительные местоимения: "
                    "who, which, that, whose"
                ),
                "slug": "relative-pronouns-who-which-that-whose",
                "theory_text": (
                    "Relative pronouns: who, which, that and whose."
                ),
                "estimated_minutes": 50,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое относительные местоимения",
                "body": """Относительные местоимения соединяют части предложения.

Они помогают дать информацию о:

человеке;

предмете;

животном;

владельце.

Основные слова:

who

which

that

whose

Пример:

The woman lives next door.
She is my teacher.

Можно соединить:

The woman who lives next door is my teacher.""",
            },

            {
                "order": 2,
                "title": "WHO — для людей",
                "body": """WHO используется для людей.

Примеры:

The man who called me is my uncle.

The woman who works here is very kind.

The students who study regularly get better results.

Если WHO выполняет действие, оно является подлежащим.

The man who lives next door...

WHO = человек, который живёт.""",
            },

            {
                "order": 3,
                "title": "WHICH — для предметов и животных",
                "body": """WHICH используется для предметов и животных.

Примеры:

The book which is on the table is mine.

The car which broke down belongs to my brother.

The dog which barked all night belongs to our neighbour.

Если WHICH выполняет действие или находится в состоянии, оно является подлежащим.

The phone which is on the desk...""",
            },

            {
                "order": 4,
                "title": "THAT — для людей и предметов",
                "body": """THAT может использоваться и для людей, и для предметов.

Для людей:

The man that called me is my uncle.

Для предметов:

The book that is on the table is mine.

Сравните:

The woman who works here...

The woman that works here...

Для людей WHO часто звучит естественнее.

Для предметов возможны:

which

that""",
            },

            {
                "order": 5,
                "title": "WHO / WHICH / THAT: главное правило",
                "body": """Для людей:

who

that

Для предметов:

which

that

Для животных:

which

that

Примеры:

The teacher who helped me was patient.

The car which is outside is mine.

The phone that I bought is expensive.

Главный вопрос:

о человеке или о предмете идёт речь?""",
            },

            {
                "order": 6,
                "title": "Relative pronoun как дополнение",
                "body": """Относительное местоимение может быть дополнением.

Пример:

The man who I met was friendly.

Кто выполняет действие?

I met the man.

Значит WHO — дополнение.

Другие примеры:

The book which I bought is interesting.

The car that we bought is reliable.

Если после relative pronoun уже есть другое подлежащее:

who I...

which I...

that we...

то relative pronoun часто является дополнением.""",
            },

            {
                "order": 7,
                "title": "Когда местоимение можно опустить",
                "body": """В defining relative clause относительное местоимение можно опустить, если оно является дополнением.

Правильно:

The man who I met was friendly.

The man I met was friendly.

The book which I bought is interesting.

The book I bought is interesting.

The film that we watched was boring.

The film we watched was boring.

Но если relative pronoun является подлежащим, убрать его нельзя.""",
            },

            {
                "order": 8,
                "title": "Когда местоимение нельзя опускать",
                "body": """Если relative pronoun выполняет действие, оно является подлежащим.

Тогда его нельзя убрать.

Правильно:

The man who lives next door is a doctor.

Нельзя:

The man lives next door is a doctor.

Правильно:

The book which is on the table is mine.

Правильно:

The student who answered was correct.

Подсказка:

who + verb → обычно subject

who + I/he/she/we/they → обычно object""",
            },

            {
                "order": 9,
                "title": "WHOSE — принадлежность",
                "body": """WHOSE показывает принадлежность.

Значение:

чей, чья, чьё, чьи

Примеры:

The woman whose car was stolen called the police.

I know a student whose father is a doctor.

The man whose phone rang left the room.

После WHOSE сразу идёт существительное:

whose car

whose brother

whose house

whose documents

WHOSE может относиться также к организациям и предметам.""",
            },

            {
                "order": 10,
                "title": "WHOSE и WHO'S",
                "body": """Не путайте WHOSE и WHO'S.

WHOSE:

чей?

Whose book is this?

WHO'S:

сокращение от who is или who has.

Who's that man?

= Who is that man?

Who's finished the work?

= Who has finished the work?

Пример:

The girl whose bag is red...

Не:

The girl who's bag is red...""",
            },

            {
                "order": 11,
                "title": "Defining relative clauses",
                "body": """Defining relative clause даёт необходимую информацию.

Без неё непонятно, о каком человеке или предмете идёт речь.

Пример:

The student who got the highest score received a prize.

Какой студент?

Тот, который получил лучший результат.

В defining clauses обычно нет запятых.

Примеры:

The man who lives next door is a doctor.

The book that you gave me is interesting.""",
            },

            {
                "order": 12,
                "title": "Non-defining relative clauses",
                "body": """Non-defining clause даёт дополнительную информацию.

Пример:

My brother, who lives in Astana, is a doctor.

Мы уже знаем, о каком брате идёт речь.

Часть:

who lives in Astana

просто добавляет информацию.

В таких предложениях используются запятые.

Важно:

после запятой THAT не используется.

Правильно:

My brother, who lives in Astana, is a doctor.

Не:

My brother, that lives in Astana...""",
            },

            {
                "order": 13,
                "title": "WHERE, WHEN и предлоги",
                "body": """WHERE используется для места:

This is the house where I grew up.

Также:

This is the house that I grew up in.

This is the house I grew up in.

WHEN используется для времени:

I remember the day when we first met.

Также:

I remember the day that we first met.

С предлогом в разговорной речи:

The person who I spoke to...

В формальном стиле:

The person to whom I spoke...

После предлога THAT не используется.""",
            },

            {
                "order": 14,
                "title": "Как выбрать relative pronoun",
                "body": """Речь идёт о человеке?

→ who / that

Речь идёт о предмете или животном?

→ which / that

Нужно показать принадлежность?

→ whose

Есть запятые?

→ не используйте that

Relative pronoun является дополнением в defining clause?

→ его можно опустить

Relative pronoun является подлежащим?

→ его нельзя опустить

Главные формы:

who → люди

which → предметы / животные

that → люди / предметы в defining clauses

whose → принадлежность""",
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
                "prompt": (
                    "The student ___ answered the question "
                    "got a prize."
                ),
                "options": [
                    "which",
                    "who",
                    "whose answer he",
                    "where",
                ],
                "answer": "who",
                "explanation": (
                    "Student = человек; WHO является подлежащим."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "The laptop ___ I use belongs "
                    "to the university."
                ),
                "options": [
                    "who",
                    "which",
                    "whose",
                    "where",
                ],
                "answer": "which",
                "explanation": (
                    "Laptop = предмет → which."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "The woman ___ son studies with me "
                    "is a doctor."
                ),
                "options": [
                    "who",
                    "which",
                    "whose",
                    "that she",
                ],
                "answer": "whose",
                "explanation": (
                    "Нужно показать принадлежность: her son → whose son."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "This is the house ___ we bought last year."
                ),
                "options": [
                    "who",
                    "which",
                    "whose",
                    "where only as subject",
                ],
                "answer": "which",
                "explanation": (
                    "House = предмет; which является дополнением."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "The teacher ___ helped me was very patient."
                ),
                "options": [
                    "who",
                    "which",
                    "whose",
                    "where",
                ],
                "answer": "who",
                "explanation": (
                    "Teacher = человек, который выполняет действие."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "The film ___ we saw yesterday was excellent."
                ),
                "options": [
                    "who",
                    "that",
                    "whose",
                    "where",
                ],
                "answer": "that",
                "explanation": (
                    "Film = предмет; that возможно в defining clause."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "My uncle, ___ lives in London, "
                    "is visiting us."
                ),
                "options": [
                    "that",
                    "who",
                    "which",
                    "whose house he",
                ],
                "answer": "who",
                "explanation": (
                    "Non-defining clause с человеком → who, не that."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "The phone, ___ is only a year old, "
                    "has stopped working."
                ),
                "options": [
                    "that",
                    "which",
                    "who",
                    "whose person",
                ],
                "answer": "which",
                "explanation": (
                    "После запятой для предмета используется which."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "The company ___ products are sold worldwide "
                    "is very successful."
                ),
                "options": [
                    "who",
                    "which",
                    "whose",
                    "that its",
                ],
                "answer": "whose",
                "explanation": (
                    "Products принадлежат company → whose products."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "The man ___ I called didn't answer."
                ),
                "options": [
                    "who",
                    "whose",
                    "where",
                    "which",
                ],
                "answer": "who",
                "explanation": (
                    "Man = человек; WHO здесь дополнение."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "The book ___ is on the shelf belongs to Anna."
                ),
                "options": [
                    "who",
                    "which",
                    "whose",
                    "where",
                ],
                "answer": "which",
                "explanation": (
                    "Which является подлежащим: which is..."
                ),
            },

            {
                "order": 12,
                "prompt": (
                    "The book ___ Anna gave me is very useful."
                ),
                "options": [
                    "who",
                    "which",
                    "whose",
                    "where",
                ],
                "answer": "which",
                "explanation": (
                    "Anna — подлежащее, which — дополнение."
                ),
            },

            {
                "order": 13,
                "prompt": "Everything ___ he said was true.",
                "options": [
                    "who",
                    "that",
                    "whose",
                    "where",
                ],
                "answer": "that",
                "explanation": (
                    "После everything часто используется that."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "She is the only person ___ understands me."
                ),
                "options": [
                    "who",
                    "which",
                    "whose",
                    "where",
                ],
                "answer": "who",
                "explanation": (
                    "Person = человек; who здесь звучит естественно."
                ),
            },

            {
                "order": 15,
                "prompt": "The chair on ___ I sat was broken.",
                "options": [
                    "who",
                    "which",
                    "that",
                    "whose",
                ],
                "answer": "which",
                "explanation": (
                    "После предлога нельзя использовать that."
                ),
            },

            {
                "order": 16,
                "prompt": (
                    "Which relative pronoun can be omitted?"
                ),
                "options": [
                    "The man who called me...",
                    "The book which I bought...",
                    "The student who answered...",
                    "The car which stopped...",
                ],
                "answer": "The book which I bought...",
                "explanation": (
                    "Which является дополнением: I bought the book."
                ),
            },

            {
                "order": 17,
                "prompt": (
                    "Which relative pronoun cannot be omitted?"
                ),
                "options": [
                    "The film that we watched...",
                    "The man who I called...",
                    "The book which is on the table...",
                    "The car that I bought...",
                ],
                "answer": (
                    "The book which is on the table..."
                ),
                "explanation": (
                    "Which является подлежащим: which is..."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "The woman which works here is my aunt.",
                    "The woman who works here is my aunt.",
                    "The woman who she works here is my aunt.",
                    "The woman whose works here is my aunt.",
                ],
                "answer": (
                    "The woman who works here is my aunt."
                ),
                "explanation": (
                    "Для человека используется who; лишнее she не нужно."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "The book who is on the table is mine.",
                    "The book which is on the table is mine.",
                    "The book whose is on the table is mine.",
                    "The book which it is on the table is mine.",
                ],
                "answer": (
                    "The book which is on the table is mine."
                ),
                "explanation": (
                    "Book = предмет → which."
                ),
            },

            {
                "order": 20,
                "prompt": "Choose the sentence without a redundant object.",
                "options": [
                    "The phone that I bought it is expensive.",
                    "The phone that I bought is expensive.",
                    "The phone which I bought it was expensive.",
                    "The phone who I bought is expensive.",
                ],
                "answer": (
                    "The phone that I bought is expensive."
                ),
                "explanation": (
                    "That уже заменяет phone; второе it не нужно."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct non-defining clause.",
                "options": [
                    (
                        "My sister, that lives in Astana, "
                        "is a doctor."
                    ),
                    (
                        "My sister, who lives in Astana, "
                        "is a doctor."
                    ),
                    (
                        "My sister who, lives in Astana, "
                        "is a doctor."
                    ),
                    (
                        "My sister, which lives in Astana, "
                        "is a doctor."
                    ),
                ],
                "answer": (
                    "My sister, who lives in Astana, "
                    "is a doctor."
                ),
                "explanation": (
                    "После запятых that не используется."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct WHOSE sentence.",
                "options": [
                    "The girl who's father is a teacher is my friend.",
                    "The girl whose father is a teacher is my friend.",
                    "The girl who father is a teacher is my friend.",
                    "The girl whose is father a teacher is my friend.",
                ],
                "answer": (
                    "The girl whose father is a teacher is my friend."
                ),
                "explanation": (
                    "Whose + noun показывает принадлежность."
                ),
            },

            {
                "order": 23,
                "prompt": (
                    "Choose the correct subject/object pair."
                ),
                "options": [
                    (
                        "The man who called me... = subject / "
                        "The man who I called... = object"
                    ),
                    (
                        "The man who called me... = object / "
                        "The man who I called... = subject"
                    ),
                    (
                        "Both are always subjects",
                    ),
                    (
                        "Both are always objects",
                    ),
                ],
                "answer": (
                    "The man who called me... = subject / "
                    "The man who I called... = object"
                ),
                "explanation": (
                    "Who + verb → subject; who + I → object."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "person → who / "
                        "thing → which / "
                        "person or thing in defining clause → that / "
                        "possession → whose"
                    ),
                    (
                        "person → which / "
                        "thing → who / "
                        "possession → that / "
                        "after commas → that"
                    ),
                    (
                        "person → whose only / "
                        "thing → who / "
                        "possession → which / "
                        "after commas → that"
                    ),
                    (
                        "person → where / "
                        "thing → when / "
                        "possession → who / "
                        "after commas → that"
                    ),
                ],
                "answer": (
                    "person → who / "
                    "thing → which / "
                    "person or thing in defining clause → that / "
                    "possession → whose"
                ),
                "explanation": (
                    "Это основная система выбора relative pronouns."
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
                "✅ A1 Lesson 54 seeded: Relative Pronouns"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
