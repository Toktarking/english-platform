from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 9: "
        "Reflexive pronouns."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=9,
            defaults={
                "title": "Возвратные местоимения",
                "slug": "reflexive-pronouns",
                "theory_text": "Reflexive pronouns.",
                "estimated_minutes": 30,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )

        sections = [

            {
                "order": 1,
                "title": "Что такое возвратные местоимения",
                "body": """Возвратные местоимения показывают, что действие направлено обратно на того, кто его выполняет.

Сравните:

I see him.
— Я вижу его.

I see myself in the mirror.
— Я вижу себя в зеркале.

В первом предложении действие направлено на другого человека.

Во втором — на самого говорящего.

Главный вопрос:

Кто выполняет действие?

И на кого направлено действие?

Если это один и тот же человек, часто используется возвратное местоимение.""",
            },

            {
                "order": 2,
                "title": "Основная таблица",
                "body": """Личное местоимение → возвратная форма:

I → myself

you → yourself

he → himself

she → herself

it → itself

we → ourselves

you → yourselves

they → themselves

Запомните:

единственное число часто заканчивается на -self;

множественное число — на -selves.""",
            },

            {
                "order": 3,
                "title": "Myself, yourself, himself, herself",
                "body": """Myself используется с I:

I cut myself.

I saw myself in the mirror.

I introduced myself.

Yourself используется, когда обращаемся к одному человеку:

Did you hurt yourself?

You should look after yourself.

Help yourself.

Himself используется с he:

He cut himself while cooking.

He introduced himself.

Herself используется с she:

She taught herself English.

She hurt herself.

She prepared herself for the interview.""",
            },

            {
                "order": 4,
                "title": "Itself, ourselves, yourselves, themselves",
                "body": """Itself используется с it:

The cat cleaned itself.

The door opened by itself.

The machine turns itself off.

Ourselves используется с we:

We introduced ourselves.

We enjoyed ourselves.

We did the work ourselves.

Yourselves используется при обращении к нескольким людям:

Please introduce yourselves.

Did you enjoy yourselves?

Themselves используется с they:

They introduced themselves.

The children dressed themselves.

They did everything themselves.""",
            },

            {
                "order": 5,
                "title": "Когда действие направлено на себя",
                "body": """Сравните:

Marat cut him.
— Марат порезал другого мужчину.

Marat cut himself.
— Марат порезался сам.

Aigul looked at her.
— Айгуль посмотрела на другую женщину.

Aigul looked at herself.
— Айгуль посмотрела на себя.

Простой алгоритм:

1. Найдите подлежащее.
2. Найдите объект действия.
3. Если это один и тот же человек — используйте возвратное местоимение.""",
            },

            {
                "order": 6,
                "title": "Частые конструкции",
                "body": """Возвратные местоимения часто встречаются после глаголов:

cut;
hurt;
burn;
introduce;
teach;
prepare;
blame;
enjoy;
help;
look at.

Полезные конструкции:

introduce oneself = представиться

Let me introduce myself.

teach oneself = научиться самостоятельно

He taught himself English.

enjoy oneself = хорошо проводить время

We enjoyed ourselves at the party.

help yourself = угощайся

Help yourself to some cake.""",
            },

            {
                "order": 7,
                "title": "Значение «сам»",
                "body": """Возвратное местоимение может не означать действие на себя.

Оно может просто усиливать значение:

сам;
сама;
сами;
лично.

Примеры:

I did it myself.
— Я сделал это сам.

She wrote the report herself.

The director himself spoke to us.

We prepared the food ourselves.

The children made the toys themselves.

Возвратная форма в этом случае подчёркивает, кто именно выполнил действие.""",
            },

            {
                "order": 8,
                "title": "Где ставится усилительная форма",
                "body": """Когда возвратное местоимение означает «сам», оно может стоять:

после подлежащего;

или в конце предложения.

Сравните:

I myself checked the document.

I checked the document myself.

Оба предложения означают:

Я сам проверил документ.

В разговорной речи вариант в конце предложения встречается особенно часто.""",
            },

            {
                "order": 9,
                "title": "By myself",
                "body": """Конструкция:

by + возвратное местоимение

часто означает:

самостоятельно;
без помощи;
в одиночестве.

Примеры:

I live by myself.
— Я живу один.

She travelled by herself.
— Она путешествовала одна.

He fixed the computer by himself.
— Он сам, без помощи, починил компьютер.

Сравните:

I did it myself.
— Я сделал это сам.

I did it by myself.
— Я сделал это самостоятельно, без помощи.""",
            },

            {
                "order": 10,
                "title": "Когда возвратное местоимение не нужно",
                "body": """В английском некоторые действия не требуют возвратного местоимения, хотя в русском часто звучат возвратно.

Обычно говорят:

I washed.
— Я умылся.

He dressed quickly.
— Он быстро оделся.

She feels tired.
— Она чувствует себя уставшей.

We met yesterday.
— Мы встретились вчера.

Неправильно:

I feel myself tired.

Правильно:

I feel tired.

Неправильно:

We met ourselves yesterday.

Правильно:

We met yesterday.""",
            },

            {
                "order": 11,
                "title": "Themselves или each other",
                "body": """Очень важно различать:

themselves = себя

each other = друг друга

Сравните:

They looked at themselves in the mirror.
— Они посмотрели на себя.

They looked at each other.
— Они посмотрели друг на друга.

Ещё пример:

The children dressed themselves.
— Дети оделись сами.

The children helped each other.
— Дети помогли друг другу.""",
            },

            {
                "order": 12,
                "title": "Согласование с подлежащим",
                "body": """Возвратное местоимение должно соответствовать подлежащему.

Правильно:

I hurt myself.

He hurt himself.

She hurt herself.

We hurt ourselves.

They hurt themselves.

Неправильно:

I hurt himself.

She hurt myself.

They hurt ourselves.

Также:

один человек → yourself

несколько людей → yourselves

Help yourself.

Help yourselves.""",
            },

            {
                "order": 13,
                "title": "Типичные ошибки",
                "body": """Неправильно:

I cut me.

Правильно:

I cut myself.

Неправильно:

Aigul introduced himself.

Правильно:

Aigul introduced herself.

Неправильно:

theirselves

Правильно:

themselves

Неправильно:

ourself

Правильно:

ourselves

Неправильно:

Myself did the work.

Правильно:

I did the work myself.""",
            },

            {
                "order": 14,
                "title": "Как быстро выбрать форму",
                "body": """1. Найдите подлежащее.

She hurt ___.

Подлежащее — she.

2. Проверьте, направлено ли действие на того же человека.

Если да:

She hurt herself.

Если на другого:

She hurt him.

3. Проверьте число.

Один человек:

myself;
yourself;
himself;
herself;
itself.

Несколько:

ourselves;
yourselves;
themselves.

4. Если речь о «самостоятельно, без помощи»:

by myself;
by yourself;
by himself;
by herself;
by ourselves;
by themselves.""",
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
                "prompt": "I saw ___ in the mirror.",
                "options": ["me", "myself", "mine", "my"],
                "answer": "myself",
                "explanation": "Человек видит самого себя, поэтому используется myself.",
            },

            {
                "order": 2,
                "prompt": "He cut ___ while cooking.",
                "options": ["him", "his", "himself", "he"],
                "answer": "himself",
                "explanation": "Он порезал сам себя: he → himself.",
            },

            {
                "order": 3,
                "prompt": "She taught ___ to play the guitar.",
                "options": ["her", "herself", "she", "hers"],
                "answer": "herself",
                "explanation": "Она самостоятельно научилась: teach oneself.",
            },

            {
                "order": 4,
                "prompt": "We enjoyed ___ at the party.",
                "options": ["us", "our", "ourselves", "ours"],
                "answer": "ourselves",
                "explanation": "Устойчивая конструкция: enjoy oneself.",
            },

            {
                "order": 5,
                "prompt": "Please introduce ___. (one person)",
                "options": ["yourself", "yourselves", "himself", "themselves"],
                "answer": "yourself",
                "explanation": "Обращение к одному человеку: yourself.",
            },

            {
                "order": 6,
                "prompt": "The children made the decorations ___.",
                "options": ["itself", "himself", "themselves", "ourselves"],
                "answer": "themselves",
                "explanation": "Children — множественное число: themselves.",
            },

            {
                "order": 7,
                "prompt": "I repaired the chair ___.",
                "options": ["myself", "me", "mine", "my"],
                "answer": "myself",
                "explanation": "Myself здесь означает «сам».",
            },

            {
                "order": 8,
                "prompt": "She lives by ___.",
                "options": ["her", "herself", "hers", "she"],
                "answer": "herself",
                "explanation": "By herself означает «одна / самостоятельно».",
            },

            {
                "order": 9,
                "prompt": "The students helped ___ during the project.",
                "options": ["themselves", "each other", "ourselves", "itself"],
                "answer": "each other",
                "explanation": "Студенты помогали друг другу, а не самим себе.",
            },

            {
                "order": 10,
                "prompt": "I feel ___ today.",
                "options": ["myself tired", "me tired", "tired", "myself tiring"],
                "answer": "tired",
                "explanation": "После feel в этом значении возвратное местоимение не нужно.",
            },

            {
                "order": 11,
                "prompt": "I introduced ___ to the new students.",
                "options": ["me", "myself", "mine", "my"],
                "answer": "myself",
                "explanation": "I → myself.",
            },

            {
                "order": 12,
                "prompt": "Did you hurt ___? (one person)",
                "options": ["yourselves", "yourself", "himself", "themselves"],
                "answer": "yourself",
                "explanation": "Обращение к одному человеку: yourself.",
            },

            {
                "order": 13,
                "prompt": "Marat looked at ___ in the mirror.",
                "options": ["him", "his", "himself", "he"],
                "answer": "himself",
                "explanation": "Marat посмотрел на самого себя.",
            },

            {
                "order": 14,
                "prompt": "Aigul prepared ___ for the examination.",
                "options": ["her", "hers", "herself", "she"],
                "answer": "herself",
                "explanation": "Aigul = she → herself.",
            },

            {
                "order": 15,
                "prompt": "The cat cleaned ___.",
                "options": ["itself", "himself", "themselves", "ourselves"],
                "answer": "itself",
                "explanation": "Cat здесь заменяется it → itself.",
            },

            {
                "order": 16,
                "prompt": "We completed the project ___.",
                "options": ["us", "our", "ourselves", "ours"],
                "answer": "ourselves",
                "explanation": "Ourselves здесь означает «сами».",
            },

            {
                "order": 17,
                "prompt": "Please make ___ comfortable. (several people)",
                "options": ["yourself", "yourselves", "themselves", "ourselves"],
                "answer": "yourselves",
                "explanation": "Обращение к нескольким людям: yourselves.",
            },

            {
                "order": 18,
                "prompt": "The children dressed ___.",
                "options": ["itself", "himself", "themselves", "yourselves"],
                "answer": "themselves",
                "explanation": "Children = they → themselves.",
            },

            {
                "order": 19,
                "prompt": "She travelled by ___.",
                "options": ["her", "herself", "hers", "she"],
                "answer": "herself",
                "explanation": "By herself означает «одна / самостоятельно».",
            },

            {
                "order": 20,
                "prompt": "The director ___ checked the documents.",
                "options": ["himself", "him", "his", "he"],
                "answer": "himself",
                "explanation": "Himself здесь усиливает значение: сам директор.",
            },

            {
                "order": 21,
                "prompt": "We looked at ___ in the photograph.",
                "options": ["us", "ourselves", "our", "ours"],
                "answer": "ourselves",
                "explanation": "Мы посмотрели на самих себя.",
            },

            {
                "order": 22,
                "prompt": "The two friends called ___ every day.",
                "options": ["themselves", "each other", "itself", "himself"],
                "answer": "each other",
                "explanation": "Друзья звонили друг другу.",
            },

            {
                "order": 23,
                "prompt": "He feels ___ after the holiday.",
                "options": ["himself better", "him better", "better", "himself well"],
                "answer": "better",
                "explanation": "После feel здесь возвратное местоимение не используется.",
            },

            {
                "order": 24,
                "prompt": "The door closed by ___.",
                "options": ["itself", "himself", "themselves", "herself"],
                "answer": "itself",
                "explanation": "By itself означает, что дверь закрылась сама.",
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
                "✅ A1 Lesson 9 seeded: "
                "Возвратные местоимения"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
