import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone

from .course_plan import (
    get_required_grammar_step,
    sync_grammar_plan,
    update_grammar_daily_progress,
)

from .models import (
    GrammarBlock,
    GrammarBlockPracticeProgress,
    GrammarExercise,
    GrammarLesson,
)


QUESTIONS_PER_LESSON = 2
PASS_SCORE = 70


def _session_key(
    block_order,
):

    return (
        f"grammar_block_"
        f"{block_order}_practice"
    )


def _get_block(
    block_order,
):

    return get_object_or_404(
        GrammarBlock,
        level="A1",
        order=block_order,
        is_published=True,
    )


def _get_block_lessons(
    block,
):

    return list(
        GrammarLesson.objects
        .filter(
            block=block,
            level="A1",
            is_published=True,
        )
        .order_by(
            "order"
        )
    )


def _build_question_ids(
    block,
):

    question_ids = []


    for lesson in (
        _get_block_lessons(
            block
        )
    ):

        pool = list(
            GrammarExercise.objects
            .filter(
                lesson=lesson,
                section__isnull=True,
                is_published=True,
                exercise_type="choice",
            )
            .values_list(
                "id",
                flat=True,
            )
        )


        if (
            len(pool)
            <
            QUESTIONS_PER_LESSON
        ):

            raise ValueError(
                f"Lesson {lesson.order}: "
                "недостаточно вопросов Final Test."
            )


        question_ids.extend(
            random.sample(
                pool,
                QUESTIONS_PER_LESSON,
            )
        )


    random.shuffle(
        question_ids
    )

    return question_ids


def _get_questions(
    question_ids,
):

    exercise_map = {
        exercise.id:
            exercise

        for exercise in (
            GrammarExercise.objects
            .filter(
                id__in=question_ids,
                is_published=True,
            )
            .select_related(
                "lesson"
            )
        )
    }


    return [
        exercise_map[
            question_id
        ]

        for question_id
        in question_ids

        if question_id
        in exercise_map
    ]


@login_required
def block_practice(
    request,
    block_order,
):

    block = (
        _get_block(
            block_order
        )
    )


    if block.order not in {
        1,
        2,
        3,
    }:

        return redirect(
            "grammar:home"
        )


    progress, _ = (
        GrammarBlockPracticeProgress.objects
        .get_or_create(
            user=request.user,
            block=block,
        )
    )


    required_step = (
        get_required_grammar_step(
            request.user
        )
    )


    available = (
        progress.is_completed

        or

        (
            required_step[
                "type"
            ]
            ==
            "practice"

            and

            required_step[
                "block"
            ].id
            ==
            block.id
        )
    )


    if not available:

        return redirect(
            "grammar:home"
        )


    lessons = (
        _get_block_lessons(
            block
        )
    )


    expected_total = (
        len(lessons)
        *
        QUESTIONS_PER_LESSON
    )


    session_key = (
        _session_key(
            block.order
        )
    )


    if (
        request.GET.get(
            "new"
        )
        ==
        "1"

        or

        session_key
        not in request.session
    ):

        question_ids = (
            _build_question_ids(
                block
            )
        )

        request.session[
            session_key
        ] = {
            "question_ids":
                question_ids,
        }

        request.session.modified = (
            True
        )


    question_ids = (
        request.session[
            session_key
        ][
            "question_ids"
        ]
    )


    questions = (
        _get_questions(
            question_ids
        )
    )


    if (
        len(questions)
        !=
        expected_total
    ):

        request.session.pop(
            session_key,
            None,
        )

        return redirect(
            request.path
        )


    if (
        request.method
        ==
        "POST"
    ):

        correct = 0

        lesson_results = {}

        wrong_results = []


        for exercise in questions:

            lesson_order = (
                exercise.lesson.order
            )


            lesson_results.setdefault(
                lesson_order,
                {
                    "lesson":
                        exercise.lesson,

                    "correct":
                        0,

                    "total":
                        0,
                },
            )


            lesson_results[
                lesson_order
            ][
                "total"
            ] += 1


            submitted = (
                request.POST
                .get(
                    f"answer_{exercise.id}",
                    "",
                )
                .strip()
            )


            expected = (
                exercise.correct_answer
                .strip()
            )


            if (
                submitted
                ==
                expected
            ):

                correct += 1

                lesson_results[
                    lesson_order
                ][
                    "correct"
                ] += 1

            else:

                wrong_results.append(
                    {
                        "lesson_order":
                            lesson_order,

                        "lesson_title":
                            exercise.lesson.title,

                        "prompt":
                            exercise.prompt,

                        "submitted":
                            (
                                submitted
                                or
                                "Нет ответа"
                            ),

                        "correct_answer":
                            expected,

                        "explanation":
                            exercise.explanation,
                    }
                )


        total = len(
            questions
        )


        score = (
            round(
                correct
                /
                total
                *
                100
            )

            if total

            else 0
        )


        passed = (
            score
            >=
            PASS_SCORE
        )


        progress.attempts += 1

        progress.best_score = max(
            progress.best_score,
            score,
        )


        if passed:

            progress.is_completed = (
                True
            )

            if (
                progress.completed_at
                is None
            ):

                progress.completed_at = (
                    timezone.now()
                )


        progress.save(
            update_fields=[
                "attempts",
                "best_score",
                "is_completed",
                "completed_at",
                "updated_at",
            ]
        )


        request.session.pop(
            session_key,
            None,
        )


        if passed:

            # Сначала проверяем сегодняшний
            # Grammar-plan ДО перераспределения.
            update_grammar_daily_progress(
                request.user
            )

            sync_grammar_plan(
                request.user
            )


        return render(
            request,
            "grammar/block_practice.html",
            {
                "mode":
                    "result",

                "block":
                    block,

                "correct":
                    correct,

                "total":
                    total,

                "score":
                    score,

                "passed":
                    passed,

                "topic_results":
                    [
                        lesson_results[
                            key
                        ]

                        for key in sorted(
                            lesson_results
                        )
                    ],

                "wrong_results":
                    wrong_results,

                "lesson_count":
                    len(lessons),

                "questions_per_lesson":
                    QUESTIONS_PER_LESSON,

                "expected_total":
                    expected_total,

                "first_lesson_order":
                    lessons[0].order,

                "last_lesson_order":
                    lessons[-1].order,

                "practice_progress":
                    progress,
            },
        )


    return render(
        request,
        "grammar/block_practice.html",
        {
            "mode":
                "test",

            "block":
                block,

            "questions":
                questions,

            "total":
                len(questions),

            "lesson_count":
                len(lessons),

            "questions_per_lesson":
                QUESTIONS_PER_LESSON,

            "expected_total":
                expected_total,

            "first_lesson_order":
                lessons[0].order,

            "last_lesson_order":
                lessons[-1].order,

            "practice_progress":
                progress,
        },
    )


@login_required
def block_1_practice(
    request,
):

    return block_practice(
        request,
        block_order=1,
    )


@login_required
def block_2_practice(
    request,
):

    return block_practice(
        request,
        block_order=2,
    )


@login_required
def block_3_practice(
    request,
):

    return block_practice(
        request,
        block_order=3,
    )
