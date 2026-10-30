import random

from grammar.models import (
    GrammarExercise,
    GrammarTopicAssessment,
)


SESSION_KEY = "grammar_mixed_exam_practice"


def _spread_sample(
    exercises,
    count,
):
    """
    Spread questions across lessons instead of
    drawing many questions from one topic.
    """

    exercises = list(
        exercises
    )

    if not exercises or count <= 0:
        return []

    rng = random.SystemRandom()

    by_lesson = {}

    for exercise in exercises:

        by_lesson.setdefault(
            exercise.lesson_id,
            [],
        ).append(
            exercise
        )

    lesson_ids = list(
        by_lesson.keys()
    )

    rng.shuffle(
        lesson_ids
    )

    for lesson_id in lesson_ids:
        rng.shuffle(
            by_lesson[
                lesson_id
            ]
        )

    selected = []

    while (
        lesson_ids
        and
        len(selected) < count
    ):

        next_round = []

        rng.shuffle(
            lesson_ids
        )

        for lesson_id in lesson_ids:

            bucket = (
                by_lesson[
                    lesson_id
                ]
            )

            if bucket:

                selected.append(
                    bucket.pop()
                )

                if (
                    len(selected)
                    >= count
                ):
                    break

            if bucket:
                next_round.append(
                    lesson_id
                )

        lesson_ids = (
            next_round
        )

    return selected


def build_exam_question_ids(
    user,
    count=20,
):
    """
    70% from LEARN / REVIEW topics.
    30% from the rest of the course.

    Questions themselves never expose
    the lesson/topic to the learner.
    """

    all_exercises = list(
        GrammarExercise.objects
        .filter(
            is_published=True,
            lesson__is_published=True,
            lesson__level="A1",
            lesson__order__range=(1, 60),
        )
        .select_related(
            "lesson",
        )
    )

    if not all_exercises:
        return []

    weak_lesson_ids = set(
        GrammarTopicAssessment.objects
        .filter(
            user=user,
            status__in=[
                GrammarTopicAssessment
                .Status
                .LEARN,

                GrammarTopicAssessment
                .Status
                .REVIEW,
            ],
        )
        .values_list(
            "lesson_id",
            flat=True,
        )
    )

    weak_pool = [
        exercise
        for exercise in all_exercises
        if (
            exercise.lesson_id
            in weak_lesson_ids
        )
    ]

    other_pool = [
        exercise
        for exercise in all_exercises
        if (
            exercise.lesson_id
            not in weak_lesson_ids
        )
    ]

    weak_target = round(
        count
        * 0.70
    )

    selected = []

    if weak_pool:

        selected.extend(
            _spread_sample(
                weak_pool,
                weak_target,
            )
        )

    selected_ids = {
        exercise.id
        for exercise in selected
    }

    remaining = (
        count
        - len(selected)
    )

    if remaining > 0:

        available_other = [
            exercise
            for exercise in other_pool
            if (
                exercise.id
                not in selected_ids
            )
        ]

        extra = (
            _spread_sample(
                available_other,
                remaining,
            )
        )

        selected.extend(
            extra
        )

    selected_ids = {
        exercise.id
        for exercise in selected
    }

    remaining = (
        count
        - len(selected)
    )

    if remaining > 0:

        fallback = [
            exercise
            for exercise in all_exercises
            if (
                exercise.id
                not in selected_ids
            )
        ]

        selected.extend(
            _spread_sample(
                fallback,
                remaining,
            )
        )

    rng = random.SystemRandom()

    rng.shuffle(
        selected
    )

    return [
        exercise.id
        for exercise in selected[:count]
    ]


def start_exam_session(
    request,
    count=20,
):

    question_ids = (
        build_exam_question_ids(
            request.user,
            count=count,
        )
    )

    state = {
        "question_ids":
            question_ids,

        "index":
            0,

        "correct":
            0,

        "answers":
            [],
    }

    request.session[
        SESSION_KEY
    ] = state

    request.session.modified = True

    return state


def get_exam_state(request):

    return request.session.get(
        SESSION_KEY
    )


def get_current_exam_question(
    request,
):

    state = get_exam_state(
        request
    )

    if not state:
        return None

    index = state.get(
        "index",
        0,
    )

    question_ids = state.get(
        "question_ids",
        [],
    )

    if index >= len(
        question_ids
    ):
        return None

    question_id = (
        question_ids[
            index
        ]
    )

    return (
        GrammarExercise.objects
        .select_related(
            "lesson",
        )
        .get(
            pk=question_id
        )
    )


def submit_exam_answer(
    request,
    selected_answer,
):

    state = get_exam_state(
        request
    )

    if not state:
        raise ValueError(
            "No active exam practice."
        )

    question = (
        get_current_exam_question(
            request
        )
    )

    if question is None:
        raise ValueError(
            "Exam practice is complete."
        )

    selected_answer = str(
        selected_answer
    ).strip()

    allowed_answers = [
        str(option)
        for option in question.options
    ]

    if (
        selected_answer
        not in allowed_answers
    ):
        raise ValueError(
            "Invalid answer."
        )

    expected = str(
        question.correct_answer
    ).strip()

    is_correct = (
        selected_answer
        == expected
    )

    if is_correct:

        state["correct"] = (
            state.get(
                "correct",
                0,
            )
            + 1
        )

    state.setdefault(
        "answers",
        [],
    ).append(
        {
            "question_id":
                question.id,

            "prompt":
                question.prompt,

            "selected":
                selected_answer,

            "correct":
                expected,

            "is_correct":
                is_correct,

            "explanation":
                question.explanation,

            # Saved only for result analysis.
            # Not shown while answering.
            "lesson_order":
                question.lesson.order,

            "lesson_title":
                question.lesson.title,
        }
    )

    state["index"] = (
        state.get(
            "index",
            0,
        )
        + 1
    )

    request.session[
        SESSION_KEY
    ] = state

    request.session.modified = True

    return is_correct
