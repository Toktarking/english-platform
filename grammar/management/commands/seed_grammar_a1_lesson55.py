from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update A1 Grammar Lesson 55: "
        "Word Formation."
    )

    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=55,
            defaults={
                "title": "Словообразование в английском языке",
                "slug": "word-formation",
                "theory_text": (
                    "Word Formation: prefixes, suffixes "
                    "and word families."
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
                "title": "Что такое словообразование",
                "body": """Словообразование — это образование новых слов.

Основные способы:

приставка;

суффикс;

изменение части речи;

соединение слов;

изменение формы слова.

Примеры:

happy → unhappy

teach → teacher

beauty → beautiful

careful → carefully

work + place → workplace

Важно видеть не отдельное слово, а его word family.""",
            },

            {
                "order": 2,
                "title": "Корень и семья слова",
                "body": """Корень несёт основное значение слова.

Примеры:

help

work

use

care

act

Из одного корня можно получить разные части речи:

act → action → active → actively → activity → actor

success → succeed → success → successful → successfully

Главная идея:

одно значение может иметь несколько грамматических форм.""",
            },

            {
                "order": 3,
                "title": "Отрицательные приставки",
                "body": """Приставка ставится перед словом и меняет его значение.

Частые отрицательные приставки:

un-

in-

im-

il-

ir-

dis-

Примеры:

happy → unhappy

correct → incorrect

possible → impossible

legal → illegal

regular → irregular

honest → dishonest

Нельзя механически использовать UN- со всеми словами.

Не:

unpossible

Правильно:

impossible""",
            },

            {
                "order": 4,
                "title": "RE-, MIS-, OVER-, UNDER-",
                "body": """RE- означает «снова»:

write → rewrite

read → reread

start → restart

MIS- означает «неправильно»:

understand → misunderstand

spell → misspell

calculate → miscalculate

OVER- означает «слишком»:

overwork

overcook

overestimate

UNDER- означает «недостаточно»:

underpay

underestimate

undercooked""",
            },

            {
                "order": 5,
                "title": "Суффиксы существительных",
                "body": """Частые noun suffixes:

-er / -or

-ist

-ment

-tion / -sion

-ness

-ity

-ance / -ence

Примеры:

teach → teacher

act → actor

science → scientist

develop → development

decide → decision

happy → happiness

responsible → responsibility

perform → performance

Часто суффикс меняет часть речи.""",
            },

            {
                "order": 6,
                "title": "Суффиксы прилагательных",
                "body": """Частые adjective suffixes:

-ful

-less

-ous

-al

-ive

-able / -ible

-y

Примеры:

care → careful

help → helpful

use → useful

use → useless

danger → dangerous

culture → cultural

effect → effective

comfort → comfortable

rain → rainy

Перед существительным часто требуется adjective:

a successful manager

an important decision""",
            },

            {
                "order": 7,
                "title": "Суффиксы глаголов",
                "body": """Частые verb suffixes:

-ize / -ise

-en

-ify

-ate

Примеры:

modern → modernize

special → specialize

wide → widen

strong → strengthen

simple → simplify

clear → clarify

active → activate

motive → motivate

После TO обычно нужен глагол:

to improve

to simplify

to modernize""",
            },

            {
                "order": 8,
                "title": "Наречия на -LY",
                "body": """Большинство наречий образуется:

adjective + -ly

slow → slowly

careful → carefully

quick → quickly

correct → correctly

complete → completely

Есть изменения написания:

happy → happily

easy → easily

simple → simply

terrible → terribly

После глагола часто требуется adverb:

She answered correctly.

He worked carefully.""",
            },

            {
                "order": 9,
                "title": "Как определить нужную часть речи",
                "body": """Смотрите на позицию слова.

После артикля часто нужно существительное:

a decision

Перед существительным часто нужно прилагательное:

an important decision

После TO BE часто нужно прилагательное:

The task is difficult.

После обычного глагола часто нужно наречие:

She answered correctly.

После TO часто нужен глагол:

to improve

Главный вопрос:

какая часть речи нужна именно здесь?""",
            },

            {
                "order": 10,
                "title": "Word family: SUCCESS",
                "body": """Семья слова SUCCESS:

succeed — глагол

success — существительное

successful — прилагательное

successfully — наречие

unsuccessful — отрицательное прилагательное

Сравните:

She hopes to succeed.

The project was a success.

She is successful.

She completed the task successfully.

Контекст определяет нужную форму.""",
            },

            {
                "order": 11,
                "title": "Word family: EMPLOY и EDUCATE",
                "body": """EMPLOY:

employ — нанимать

employer — работодатель

employee — работник

employment — занятость

unemployed — безработный

unemployment — безработица

EDUCATE:

educate — обучать

education — образование

educational — образовательный

educator — педагог

educated — образованный

Важно различать значение и часть речи.""",
            },

            {
                "order": 12,
                "title": "Орфографические изменения",
                "body": """При словообразовании написание может меняться.

Y → I:

happy → happiness

easy → easily

busy → business

Конечная E иногда исчезает:

create → creative

fame → famous

decide → decision

Иногда согласная удваивается:

begin → beginner

run → runner

swim → swimmer

Некоторые формы нужно просто запомнить:

strong → strength

choose → choice

die → death""",
            },

            {
                "order": 13,
                "title": "Compound words и conversion",
                "body": """Compound words состоят из двух или более слов.

Примеры:

classroom

workplace

website

airport

bus stop

post office

Сложные прилагательные часто пишутся через дефис:

well-known

part-time

user-friendly

ten-year-old

Conversion:

слово меняет часть речи без изменения формы.

work:

I work every day.
— verb

I have a lot of work.
— noun""",
            },

            {
                "order": 14,
                "title": "Алгоритм словообразования",
                "body": """Шаг 1.

Прочитайте всё предложение.

Шаг 2.

Определите часть речи:

noun;

verb;

adjective;

adverb.

Шаг 3.

Проверьте, нужно ли отрицательное значение.

Шаг 4.

Выберите подходящую приставку или суффикс.

Шаг 5.

Проверьте написание.

Пример:

She is a very ___ manager.
SUCCESS

Перед manager нужен adjective:

successful.

She completed the project ___.
SUCCESS

После completed нужен adverb:

successfully.""",
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
                    "She gave a very ___ explanation. "
                    "HELP"
                ),
                "options": [
                    "help",
                    "helpful",
                    "helpfully",
                    "helplessly",
                ],
                "answer": "helpful",
                "explanation": (
                    "Перед существительным explanation нужен adjective."
                ),
            },

            {
                "order": 2,
                "prompt": (
                    "He explained the rule ___. "
                    "CLEAR"
                ),
                "options": [
                    "clear",
                    "clearly",
                    "clearness",
                    "clarify",
                ],
                "answer": "clearly",
                "explanation": (
                    "Слово описывает действие explained → adverb."
                ),
            },

            {
                "order": 3,
                "prompt": (
                    "The country needs economic ___. "
                    "DEVELOP"
                ),
                "options": [
                    "develop",
                    "development",
                    "developing only",
                    "developer",
                ],
                "answer": "development",
                "explanation": (
                    "После adjective economic нужно существительное."
                ),
            },

            {
                "order": 4,
                "prompt": (
                    "She is a highly ___ employee. "
                    "RESPONSIBILITY"
                ),
                "options": [
                    "responsibly",
                    "responsible",
                    "responsibility",
                    "irresponsible in all contexts",
                ],
                "answer": "responsible",
                "explanation": (
                    "Перед employee нужен adjective."
                ),
            },

            {
                "order": 5,
                "prompt": (
                    "The result was completely ___. "
                    "EXPECT"
                ),
                "options": [
                    "expectedly",
                    "unexpected",
                    "expectation",
                    "expect",
                ],
                "answer": "unexpected",
                "explanation": (
                    "После was нужен adjective; по смыслу — unexpected."
                ),
            },

            {
                "order": 6,
                "prompt": (
                    "They made an important ___. "
                    "DECIDE"
                ),
                "options": [
                    "decisive",
                    "decision",
                    "decide",
                    "decisively",
                ],
                "answer": "decision",
                "explanation": (
                    "После an important требуется существительное."
                ),
            },

            {
                "order": 7,
                "prompt": (
                    "The service was very ___. "
                    "PROFESSION"
                ),
                "options": [
                    "professionally",
                    "professional",
                    "profession",
                    "professor",
                ],
                "answer": "professional",
                "explanation": (
                    "После was very нужен adjective."
                ),
            },

            {
                "order": 8,
                "prompt": (
                    "He behaved ___. "
                    "POLITE"
                ),
                "options": [
                    "polite",
                    "politely",
                    "politeness",
                    "impolite adjective only",
                ],
                "answer": "politely",
                "explanation": (
                    "Behaved описывается наречием."
                ),
            },

            {
                "order": 9,
                "prompt": (
                    "The new system is more ___. "
                    "EFFECT"
                ),
                "options": [
                    "effectively",
                    "effective",
                    "effect",
                    "effectiveness",
                ],
                "answer": "effective",
                "explanation": (
                    "После is more нужен adjective."
                ),
            },

            {
                "order": 10,
                "prompt": (
                    "She works for an international ___. "
                    "ORGANIZE"
                ),
                "options": [
                    "organized",
                    "organization",
                    "organizer",
                    "organizational adjective only",
                ],
                "answer": "organization",
                "explanation": (
                    "После an international требуется существительное."
                ),
            },

            {
                "order": 11,
                "prompt": (
                    "The instructions were ___. "
                    "UNDERSTAND"
                ),
                "options": [
                    "understandable",
                    "understanding noun",
                    "understandably only",
                    "understoodly",
                ],
                "answer": "understandable",
                "explanation": (
                    "-able образует adjective со значением возможности."
                ),
            },

            {
                "order": 12,
                "prompt": (
                    "This behaviour is completely ___. "
                    "ACCEPT"
                ),
                "options": [
                    "acceptable",
                    "unacceptable",
                    "acceptance",
                    "acceptably",
                ],
                "answer": "unacceptable",
                "explanation": (
                    "Нужен adjective с отрицательным значением."
                ),
            },

            {
                "order": 13,
                "prompt": (
                    "He is currently ___. "
                    "EMPLOY"
                ),
                "options": [
                    "employment",
                    "unemployed",
                    "employee",
                    "employer",
                ],
                "answer": "unemployed",
                "explanation": (
                    "После is currently нужен adjective: unemployed."
                ),
            },

            {
                "order": 14,
                "prompt": (
                    "There has been a rise in ___. "
                    "EMPLOY"
                ),
                "options": [
                    "unemployment",
                    "unemployed",
                    "employer",
                    "employable adjective only",
                ],
                "answer": "unemployment",
                "explanation": (
                    "После in требуется noun; по смыслу unemployment."
                ),
            },

            {
                "order": 15,
                "prompt": (
                    "She completed the task ___. "
                    "EFFICIENT"
                ),
                "options": [
                    "efficiency",
                    "efficient",
                    "efficiently",
                    "inefficient adjective only",
                ],
                "answer": "efficiently",
                "explanation": (
                    "Completed описывается наречием."
                ),
            },

            {
                "order": 16,
                "prompt": "Choose the correct negative form of POSSIBLE.",
                "options": [
                    "unpossible",
                    "impossible",
                    "inpossible",
                    "dispossible",
                ],
                "answer": "impossible",
                "explanation": (
                    "Перед p используется im-: impossible."
                ),
            },

            {
                "order": 17,
                "prompt": "Choose the correct negative form of LEGAL.",
                "options": [
                    "unlegal",
                    "inlegal",
                    "illegal",
                    "dislegal",
                ],
                "answer": "illegal",
                "explanation": (
                    "Перед l используется il-."
                ),
            },

            {
                "order": 18,
                "prompt": "Choose the correct noun from IMPROVE.",
                "options": [
                    "improval",
                    "improvement",
                    "improveness",
                    "improvely",
                ],
                "answer": "improvement",
                "explanation": (
                    "Improve → improvement."
                ),
            },

            {
                "order": 19,
                "prompt": "Choose the correct word family sequence.",
                "options": [
                    (
                        "succeed → success → successful → successfully"
                    ),
                    (
                        "success → succeedful → successfuly → succeeding"
                    ),
                    (
                        "succeed → successfulnessly → success → succeedly"
                    ),
                    (
                        "successful → successly → succeedment → succeeded"
                    ),
                ],
                "answer": (
                    "succeed → success → successful → successfully"
                ),
                "explanation": (
                    "Verb → noun → adjective → adverb."
                ),
            },

            {
                "order": 20,
                "prompt": (
                    "Which word means a person employed by a company?"
                ),
                "options": [
                    "employment",
                    "employer",
                    "employee",
                    "unemployment",
                ],
                "answer": "employee",
                "explanation": (
                    "Employee = работник; employer = работодатель."
                ),
            },

            {
                "order": 21,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "She is a successfully manager.",
                    "She is a successful manager.",
                    "She is a successly manager.",
                    "She is a success manager.",
                ],
                "answer": "She is a successful manager.",
                "explanation": (
                    "Перед manager нужен adjective successful."
                ),
            },

            {
                "order": 22,
                "prompt": "Choose the correct sentence.",
                "options": [
                    "He completed the work successful.",
                    "He completed the work successfully.",
                    "He completed the work success.",
                    "He completed the work successfulness.",
                ],
                "answer": (
                    "He completed the work successfully."
                ),
                "explanation": (
                    "После completed нужен adverb successfully."
                ),
            },

            {
                "order": 23,
                "prompt": "Choose the correct spelling pair.",
                "options": [
                    (
                        "happy → happiness / "
                        "easy → easily"
                    ),
                    (
                        "happy → happyness / "
                        "easy → easyly"
                    ),
                    (
                        "happy → happyness / "
                        "easy → easynessly"
                    ),
                    (
                        "happy → happyment / "
                        "easy → easiful"
                    ),
                ],
                "answer": (
                    "happy → happiness / "
                    "easy → easily"
                ),
                "explanation": (
                    "Перед некоторыми suffixes конечная y меняется на i."
                ),
            },

            {
                "order": 24,
                "prompt": "Choose the fully correct sequence.",
                "options": [
                    (
                        "develop → development / "
                        "success → successful / "
                        "careful → carefully / "
                        "simple → simplify / "
                        "possible → impossible"
                    ),
                    (
                        "develop → developement / "
                        "success → successly / "
                        "careful → carefulnessly / "
                        "simple → simpleness verb / "
                        "possible → unpossible"
                    ),
                    (
                        "develop → developingly / "
                        "success → succesfuly / "
                        "careful → carely / "
                        "simple → simpleness / "
                        "possible → dispossible"
                    ),
                    (
                        "develop → developerly / "
                        "success → successment / "
                        "careful → carefulful / "
                        "simple → simplefyly / "
                        "possible → inpossible"
                    ),
                ],
                "answer": (
                    "develop → development / "
                    "success → successful / "
                    "careful → carefully / "
                    "simple → simplify / "
                    "possible → impossible"
                ),
                "explanation": (
                    "Нужно правильно определить часть речи, "
                    "а затем выбрать suffix/prefix и написание."
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
                "✅ A1 Lesson 55 seeded: Word Formation"
            )
        )

        self.stdout.write(
            f"Sections: {lesson.sections.count()}"
        )

        self.stdout.write(
            f"Exercises: {lesson.exercises.count()}"
        )
