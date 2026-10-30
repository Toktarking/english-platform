from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 7: "
        "Personal, object and possessive pronouns."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=7,
            defaults={
                "title": (
                    "Личные, объектные и "
                    "притяжательные местоимения"
                ),
                "slug": "personal-object-possessive-pronouns",
                "theory_text": (
                    "Personal, object and possessive pronouns."
                ),
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое местоимение",
                "body": """Местоимение заменяет существительное и помогает не повторять одно и то же имя или предмет.

Без местоимений:

Marat is a teacher.
Marat works at a university.
Marat likes his job.

С местоимениями:

Marat is a teacher.
He works at a university.
He likes his job.

He заменяет Marat.

Ещё пример:

Aigul has a book.
She reads it every evening.

She заменяет Aigul.
It заменяет book.""",
            },

            {
                "order": 2,
                "title": "Личные местоимения — подлежащее",
                "body": """Подлежащее показывает, кто или что выполняет действие.

Marat works.

Marat выполняет действие.

Можно сказать:

He works.

Основные личные местоимения:

I — я
you — ты, вы
he — он
she — она
it — оно, это
we — мы
they — они

Примеры:

I am a teacher.
You are my friend.
He works here.
She speaks English.
It is cold.
We study together.
They live in Astana.""",
            },

            {
                "order": 3,
                "title": "I, you, he и she",
                "body": """I всегда пишется с большой буквы.

I am a student.

My friend and I work together.

You может означать:

ты;
вы;
Вы;
вы во множественном числе.

He используется для мужчины или мальчика:

Marat is a doctor.
He works at a hospital.

She используется для женщины или девочки:

Aigul is a teacher.
She works at a school.""",
            },

            {
                "order": 4,
                "title": "It, we и they",
                "body": """It используется для:

предметов;
животных, если пол неважен;
погоды;
времени;
расстояния.

This is a book.
It is interesting.

It is cold.

It is five o'clock.

It is five kilometres from here.

We означает «мы»:

My wife and I live here.
We live here.

They означает «они»:

Marat and Aigul are teachers.
They are teachers.

The books are new.
They are new.""",
            },

            {
                "order": 5,
                "title": "Объектные местоимения",
                "body": """Когда действие направлено на человека или предмет, используется объектная форма.

Сравните:

He sees Marat.

He выполняет действие.
Marat получает действие.

Вместо Marat:

He sees him.

Таблица:

I → me
you → you
he → him
she → her
it → it
we → us
they → them

Примеры:

She knows me.
I know him.
I know her.
The teacher helps us.
I know them.""",
            },

            {
                "order": 6,
                "title": "После глагола и предлога",
                "body": """Объектная форма обычно ставится после глагола.

I see him.
She knows me.
We like them.
They help us.

После предлога тоже используется объектная форма:

with me;
for him;
about her;
to us;
from them.

Примеры:

Come with me.

This gift is for him.

I spoke to her.

They talked about us.

Нельзя:

with I;
for he;
to she.""",
            },

            {
                "order": 7,
                "title": "Притяжательные слова",
                "body": """Притяжательные слова показывают, кому принадлежит предмет.

Они стоят перед существительным.

I → my
you → your
he → his
she → her
it → its
we → our
they → their

Примеры:

my book;
your phone;
his car;
her family;
its name;
our house;
their children.

Предложения:

This is my book.

What is your name?

His car is new.

Her phone is new.

Our teacher speaks English.

The students opened their books.""",
            },

            {
                "order": 8,
                "title": "His, her и its",
                "body": """His выбирается, если владелец — мужчина.

Marat has a car.
His car is new.

Her выбирается, если владелец — женщина.

Aigul has a phone.
Her phone is new.

Важно: выбор зависит от владельца, а не от предмета.

Marat has a sister.
His sister is a teacher.

Aigul has a brother.
Her brother is a student.

Its означает принадлежность предмету или животному:

The dog is eating its food.

The company changed its name.

Не путайте:

its = его / её

it's = it is или it has

The cat is in its box.

It's cold.""",
            },

            {
                "order": 9,
                "title": "Притяжательные местоимения",
                "body": """Иногда существительное можно не повторять.

Сравните:

This is my book.

This book is mine.

Формы:

my → mine
your → yours
his → his
her → hers
our → ours
their → theirs

Примеры:

This book is mine.

Is this bag yours?

This book is his.

This phone is hers.

This house is ours.

These books are theirs.""",
            },

            {
                "order": 10,
                "title": "My или mine",
                "body": """My используется перед существительным:

my book;
my phone;
my car.

Mine используется самостоятельно:

This book is mine.
The phone is mine.
That car is mine.

Неправильно:

This is mine book.

Правильно:

This is my book.

Или:

This book is mine.

То же правило:

your bag → the bag is yours

her phone → the phone is hers

our house → the house is ours

their books → the books are theirs.""",
            },

            {
                "order": 11,
                "title": "Полная система форм",
                "body": """Запомните четыре позиции.

I:
I → me → my → mine

You:
you → you → your → yours

He:
he → him → his → his

She:
she → her → her → hers

It:
it → it → its

We:
we → us → our → ours

They:
they → them → their → theirs

Пример с he:

He works here.
I know him.
This is his book.
This book is his.

Пример с she:

She is a teacher.
I know her.
This is her bag.
This bag is hers.""",
            },

            {
                "order": 12,
                "title": "Порядок слов",
                "body": """Перед глаголом обычно нужна форма подлежащего:

I know him.
She helps us.
They like her.

Нельзя:

Me know him.
Her helps us.
Them like her.

После глагола нужна объектная форма:

She knows me.

I called him.

Перед существительным:

my book;
your phone;
his car;
her family;
our house;
their children.

Без существительного:

mine;
yours;
his;
hers;
ours;
theirs.""",
            },

            {
                "order": 13,
                "title": "Особенности английского",
                "body": """В английском подлежащее обычно нельзя пропускать.

По-русски:

Работаю в университете.

По-английски:

I work at a university.

Притяжательные слова не меняются по роду и числу предмета:

my house;
my book;
my name;
my friends.

Выбор his/her зависит от владельца.

Marat has a sister.
His sister is a teacher.

Aigul has a brother.
Her brother is a student.""",
            },

            {
                "order": 14,
                "title": "Как быстро выбрать форму",
                "body": """1. Перед глаголом, если местоимение выполняет действие:

I;
you;
he;
she;
it;
we;
they.

She works.

2. После глагола или предлога:

me;
you;
him;
her;
it;
us;
them.

I know her.
Come with us.

3. Перед существительным:

my;
your;
his;
her;
its;
our;
their.

my book;
their house.

4. Без существительного:

mine;
yours;
his;
hers;
ours;
theirs.

This book is mine.

Главная схема:

I work.

She knows me.

This is my book.

This book is mine.""",
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
                "prompt": "Marat is my friend. ___ works at a university.",
                "options": ["Him", "He", "His", "Her"],
                "answer": "He",
                "explanation": "Marat выполняет действие, поэтому нужна форма подлежащего He.",
            },

            {
                "order": 2,
                "prompt": "I know Marat. I see ___ every day.",
                "options": ["he", "his", "him", "hers"],
                "answer": "him",
                "explanation": "После глагола see нужна объектная форма him.",
            },

            {
                "order": 3,
                "prompt": "Aigul is a teacher. ___ students like her.",
                "options": ["She", "Hers", "Her", "Him"],
                "answer": "Her",
                "explanation": "После пропуска стоит существительное students, поэтому нужна форма Her.",
            },

            {
                "order": 4,
                "prompt": "This is my phone. The phone is ___.",
                "options": ["my", "mine", "me", "I"],
                "answer": "mine",
                "explanation": "Существительное не повторяется, поэтому используется mine.",
            },

            {
                "order": 5,
                "prompt": "My brother and I live together. ___ have a small flat.",
                "options": ["They", "Us", "We", "Our"],
                "answer": "We",
                "explanation": "My brother and I = we.",
            },

            {
                "order": 6,
                "prompt": "The teacher gave ___ a difficult task.",
                "options": ["we", "our", "ours", "us"],
                "answer": "us",
                "explanation": "После gave нужна объектная форма us.",
            },

            {
                "order": 7,
                "prompt": "These students have books. These are ___ books.",
                "options": ["them", "they", "their", "theirs"],
                "answer": "their",
                "explanation": "Перед существительным books используется their.",
            },

            {
                "order": 8,
                "prompt": "These books belong to the students. They are ___.",
                "options": ["their", "theirs", "them", "they"],
                "answer": "theirs",
                "explanation": "Существительное не повторяется, поэтому используется theirs.",
            },

            {
                "order": 9,
                "prompt": "The cat is playing with ___ toy.",
                "options": ["it's", "its", "it", "his"],
                "answer": "its",
                "explanation": "Its показывает принадлежность. It's = it is / it has.",
            },

            {
                "order": 10,
                "prompt": "Come with ___.",
                "options": ["I", "my", "mine", "me"],
                "answer": "me",
                "explanation": "После предлога with используется объектная форма me.",
            },

            {
                "order": 11,
                "prompt": "___ am learning English.",
                "options": ["Me", "My", "I", "Mine"],
                "answer": "I",
                "explanation": "Перед глаголом нужна форма подлежащего I.",
            },

            {
                "order": 12,
                "prompt": "My father is a doctor. ___ works at a hospital.",
                "options": ["Him", "He", "His", "Her"],
                "answer": "He",
                "explanation": "Отец выполняет действие, поэтому He.",
            },

            {
                "order": 13,
                "prompt": "I often call ___.",
                "options": ["he", "his", "him", "himself"],
                "answer": "him",
                "explanation": "После call нужна объектная форма him.",
            },

            {
                "order": 14,
                "prompt": "My mother is a teacher. ___ school is near our house.",
                "options": ["She", "Hers", "Her", "Him"],
                "answer": "Her",
                "explanation": "Перед существительным school используется Her.",
            },

            {
                "order": 15,
                "prompt": "This bag belongs to my mother. It is ___.",
                "options": ["her", "hers", "she", "them"],
                "answer": "hers",
                "explanation": "Существительное bag не повторяется, поэтому hers.",
            },

            {
                "order": 16,
                "prompt": "My friends invited ___ to dinner.",
                "options": ["I", "my", "me", "mine"],
                "answer": "me",
                "explanation": "После invited нужна объектная форма me.",
            },

            {
                "order": 17,
                "prompt": "My wife and I have a child. ___ child is one year old.",
                "options": ["Us", "We", "Ours", "Our"],
                "answer": "Our",
                "explanation": "Перед существительным child используется Our.",
            },

            {
                "order": 18,
                "prompt": "This house belongs to us. It is ___.",
                "options": ["our", "us", "ours", "we"],
                "answer": "ours",
                "explanation": "Существительное не повторяется, поэтому ours.",
            },

            {
                "order": 19,
                "prompt": "Marat and Aigul sold ___ car.",
                "options": ["them", "theirs", "their", "they"],
                "answer": "their",
                "explanation": "Перед существительным car используется their.",
            },

            {
                "order": 20,
                "prompt": "The car was ___.",
                "options": ["their", "theirs", "them", "they"],
                "answer": "theirs",
                "explanation": "После was существительное не повторяется, поэтому theirs.",
            },

            {
                "order": 21,
                "prompt": "The students are in the classroom. The teacher is speaking to ___.",
                "options": ["they", "their", "theirs", "them"],
                "answer": "them",
                "explanation": "После предлога to используется объектная форма them.",
            },

            {
                "order": 22,
                "prompt": "The dog moved ___ tail.",
                "options": ["it's", "its", "it", "theirs"],
                "answer": "its",
                "explanation": "Its означает принадлежность: хвост собаки.",
            },

            {
                "order": 23,
                "prompt": "Is this ___ phone?",
                "options": ["you", "your", "yours", "yourself"],
                "answer": "your",
                "explanation": "Перед существительным phone используется your.",
            },

            {
                "order": 24,
                "prompt": "No, it is not ___. It belongs to my brother.",
                "options": ["my", "me", "mine", "I"],
                "answer": "mine",
                "explanation": "После not существительное не повторяется, поэтому mine.",
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
                "✅ A1 Lesson 7 seeded: "
                "Личные, объектные и "
                "притяжательные местоимения"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
