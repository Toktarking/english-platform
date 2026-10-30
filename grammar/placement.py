from django.db import transaction
from django.utils import timezone

from grammar.models import (
    GrammarAssessmentQuestion,
    GrammarBlock,
    GrammarPlacementAnswer,
    GrammarPlacementAttempt,
    GrammarTopicAssessment,
)


SCREENING_ROLE = GrammarAssessmentQuestion.Role.SCREENING
TOPIC_ROLE = GrammarAssessmentQuestion.Role.TOPIC


def start_placement(user):
    """
    Start a fresh Grammar Placement attempt.

    Any older unfinished attempt becomes ABANDONED.
    Old completed attempts remain in history.
    """
    now = timezone.now()

    with transaction.atomic():
        (
            GrammarPlacementAttempt.objects
            .select_for_update()
            .filter(
                user=user,
                status=GrammarPlacementAttempt.Status.IN_PROGRESS,
            )
            .update(
                status=GrammarPlacementAttempt.Status.ABANDONED,
                completed_at=now,
            )
        )

        attempt = GrammarPlacementAttempt.objects.create(
            user=user,
            status=GrammarPlacementAttempt.Status.IN_PROGRESS,
            stage=GrammarPlacementAttempt.Stage.SCREENING,
        )

    return attempt


def get_screening_questions():
    """
    Return the 40 active screening questions
    ordered by block and priority.
    """
    return (
        GrammarAssessmentQuestion.objects
        .filter(
            role=SCREENING_ROLE,
            is_active=True,
            exercise__lesson__level="A1",
            exercise__lesson__order__range=(1, 60),
            exercise__lesson__is_published=True,
        )
        .select_related(
            "exercise",
            "exercise__lesson",
            "exercise__lesson__block",
        )
        .order_by(
            "exercise__lesson__block__order",
            "priority",
            "pk",
        )
    )


def _get_topic_questions(lesson):
    return (
        GrammarAssessmentQuestion.objects
        .filter(
            role=TOPIC_ROLE,
            is_active=True,
            exercise__lesson=lesson,
        )
        .select_related(
            "exercise",
            "exercise__lesson",
        )
        .order_by(
            "priority",
            "pk",
        )
    )


def _answer_is_correct(assessment_question, selected_answer):
    expected = str(
        assessment_question.exercise.correct_answer
    ).strip()

    submitted = str(
        selected_answer
    ).strip()

    return submitted == expected


def _recalculate_attempt_score(attempt):
    answers = attempt.answers.all()

    attempt.correct_answers = answers.filter(
        is_correct=True,
    ).count()

    attempt.total_questions = answers.count()

    attempt.save(
        update_fields=[
            "correct_answers",
            "total_questions",
            "updated_at",
        ]
    )


def _write_topic_status(
    *,
    user,
    lesson,
    status,
    source,
    correct_answers=0,
    total_questions=0,
):
    assessment, _ = (
        GrammarTopicAssessment.objects
        .update_or_create(
            user=user,
            lesson=lesson,
            defaults={
                "status": status,
                "source": source,
                "correct_answers": correct_answers,
                "total_questions": total_questions,
            },
        )
    )

    return assessment


def _complete_attempt(attempt):
    _recalculate_attempt_score(attempt)

    attempt.status = (
        GrammarPlacementAttempt.Status.COMPLETED
    )
    attempt.stage = (
        GrammarPlacementAttempt.Stage.COMPLETE
    )
    attempt.completed_at = timezone.now()

    attempt.save(
        update_fields=[
            "status",
            "stage",
            "correct_answers",
            "total_questions",
            "completed_at",
            "updated_at",
        ]
    )

    return attempt


def finalize_screening(attempt):
    """
    Convert block screening results into an initial
    Knowledge Map.

    Rules for a 4-question block:

    4/4:
        all lessons -> PROVISIONAL_MASTERED

    3/4:
        most lessons -> PROVISIONAL_MASTERED
        lesson(s) behind wrong screening question(s) -> UNKNOWN
        and therefore receive 2 topic questions

    2/4:
        all lessons in the block -> UNKNOWN
        and therefore receive topic diagnosis

    0-1/4:
        all lessons in the block -> LEARN
        no extra diagnostic questions are needed
    """
    if attempt.status != GrammarPlacementAttempt.Status.IN_PROGRESS:
        return attempt

    screening_questions = list(
        get_screening_questions()
    )

    if not screening_questions:
        raise ValueError(
            "No active screening questions found."
        )

    question_ids = {
        item.id
        for item in screening_questions
    }

    answers = list(
        attempt.answers
        .filter(
            assessment_question_id__in=question_ids,
        )
        .select_related(
            "assessment_question",
            "assessment_question__exercise",
            "assessment_question__exercise__lesson",
            "assessment_question__exercise__lesson__block",
        )
    )

    if len(answers) != len(screening_questions):
        raise ValueError(
            "Screening is not complete yet."
        )

    answer_by_question_id = {
        answer.assessment_question_id: answer
        for answer in answers
    }

    blocks = (
        GrammarBlock.objects
        .filter(
            level="A1",
            is_published=True,
        )
        .order_by("order")
    )

    for block in blocks:
        block_questions = [
            item
            for item in screening_questions
            if item.exercise.lesson.block_id == block.id
        ]

        if not block_questions:
            raise ValueError(
                f"Block {block.order} has no screening questions."
            )

        block_answers = [
            answer_by_question_id[item.id]
            for item in block_questions
        ]

        correct = sum(
            1
            for answer in block_answers
            if answer.is_correct
        )

        total = len(block_answers)

        lessons = list(
            block.lessons
            .filter(
                level="A1",
                order__range=(1, 60),
                is_published=True,
            )
            .order_by("order")
        )

        if correct == total:
            # Strong block.
            for lesson in lessons:
                _write_topic_status(
                    user=attempt.user,
                    lesson=lesson,
                    status=(
                        GrammarTopicAssessment.Status
                        .PROVISIONAL_MASTERED
                    ),
                    source=(
                        GrammarTopicAssessment.Source
                        .PLACEMENT_SCREENING
                    ),
                )

        elif correct == total - 1:
            # Mostly strong.
            # Start by provisionally mastering the block.
            for lesson in lessons:
                _write_topic_status(
                    user=attempt.user,
                    lesson=lesson,
                    status=(
                        GrammarTopicAssessment.Status
                        .PROVISIONAL_MASTERED
                    ),
                    source=(
                        GrammarTopicAssessment.Source
                        .PLACEMENT_SCREENING
                    ),
                )

            # Only directly problematic topic(s)
            # require deeper diagnosis.
            wrong_lesson_ids = {
                answer.assessment_question.exercise.lesson_id
                for answer in block_answers
                if not answer.is_correct
            }

            for lesson in lessons:
                if lesson.id in wrong_lesson_ids:
                    _write_topic_status(
                        user=attempt.user,
                        lesson=lesson,
                        status=(
                            GrammarTopicAssessment.Status.UNKNOWN
                        ),
                        source=(
                            GrammarTopicAssessment.Source
                            .PLACEMENT_SCREENING
                        ),
                    )

        elif correct == total // 2:
            # Uncertain block.
            # Diagnose every topic.
            for lesson in lessons:
                _write_topic_status(
                    user=attempt.user,
                    lesson=lesson,
                    status=GrammarTopicAssessment.Status.UNKNOWN,
                    source=(
                        GrammarTopicAssessment.Source
                        .PLACEMENT_SCREENING
                    ),
                )

        else:
            # Weak block.
            # No reason to make the user answer
            # another 10-20 diagnostic questions.
            for lesson in lessons:
                _write_topic_status(
                    user=attempt.user,
                    lesson=lesson,
                    status=GrammarTopicAssessment.Status.LEARN,
                    source=(
                        GrammarTopicAssessment.Source
                        .PLACEMENT_SCREENING
                    ),
                )

    needs_topic_diagnosis = (
        GrammarTopicAssessment.objects
        .filter(
            user=attempt.user,
            status=GrammarTopicAssessment.Status.UNKNOWN,
        )
        .exists()
    )

    if needs_topic_diagnosis:
        attempt.stage = GrammarPlacementAttempt.Stage.TOPIC

        attempt.save(
            update_fields=[
                "stage",
                "updated_at",
            ]
        )
    else:
        _complete_attempt(attempt)

    return attempt


def refresh_topic_assessments(attempt):
    """
    Resolve every UNKNOWN lesson once its two
    TOPIC questions have been answered.

    2/2 -> MASTERED
    1/2 -> REVIEW
    0/2 -> LEARN
    """
    if attempt.status != GrammarPlacementAttempt.Status.IN_PROGRESS:
        return attempt

    unknown_items = list(
        GrammarTopicAssessment.objects
        .filter(
            user=attempt.user,
            status=GrammarTopicAssessment.Status.UNKNOWN,
        )
        .select_related(
            "lesson",
        )
        .order_by(
            "lesson__order",
        )
    )

    for topic_assessment in unknown_items:
        lesson = topic_assessment.lesson

        questions = list(
            _get_topic_questions(lesson)
        )

        if len(questions) != 2:
            raise ValueError(
                f"Lesson {lesson.order} must have exactly "
                f"2 active TOPIC questions; got "
                f"{len(questions)}."
            )

        question_ids = [
            question.id
            for question in questions
        ]

        answers = list(
            attempt.answers.filter(
                assessment_question_id__in=question_ids,
            )
        )

        if len(answers) < 2:
            continue

        correct = sum(
            1
            for answer in answers
            if answer.is_correct
        )

        if correct == 2:
            status = GrammarTopicAssessment.Status.MASTERED

        elif correct == 1:
            status = GrammarTopicAssessment.Status.REVIEW

        else:
            status = GrammarTopicAssessment.Status.LEARN

        _write_topic_status(
            user=attempt.user,
            lesson=lesson,
            status=status,
            source=(
                GrammarTopicAssessment.Source.PLACEMENT_TOPIC
            ),
            correct_answers=correct,
            total_questions=2,
        )

    still_unknown = (
        GrammarTopicAssessment.objects
        .filter(
            user=attempt.user,
            status=GrammarTopicAssessment.Status.UNKNOWN,
        )
        .exists()
    )

    if not still_unknown:
        _complete_attempt(attempt)

    return attempt


def get_next_question(attempt):
    """
    Return the next adaptive question.

    Returns None once Placement is completed.
    """
    attempt.refresh_from_db()

    if attempt.status != GrammarPlacementAttempt.Status.IN_PROGRESS:
        return None

    answered_ids = set(
        attempt.answers.values_list(
            "assessment_question_id",
            flat=True,
        )
    )

    if attempt.stage == GrammarPlacementAttempt.Stage.SCREENING:
        screening_questions = list(
            get_screening_questions()
        )

        for question in screening_questions:
            if question.id not in answered_ids:
                return question

        finalize_screening(attempt)
        return get_next_question(attempt)

    if attempt.stage == GrammarPlacementAttempt.Stage.TOPIC:
        refresh_topic_assessments(attempt)

        attempt.refresh_from_db()

        if attempt.status != GrammarPlacementAttempt.Status.IN_PROGRESS:
            return None

        unknown_topics = (
            GrammarTopicAssessment.objects
            .filter(
                user=attempt.user,
                status=GrammarTopicAssessment.Status.UNKNOWN,
            )
            .select_related("lesson")
            .order_by("lesson__order")
        )

        for topic in unknown_topics:
            for question in _get_topic_questions(topic.lesson):
                if question.id not in answered_ids:
                    return question

        refresh_topic_assessments(attempt)

        attempt.refresh_from_db()

        if attempt.status == GrammarPlacementAttempt.Status.COMPLETED:
            return None

        raise ValueError(
            "Placement has unresolved topics but "
            "no unanswered diagnostic questions."
        )

    return None


@transaction.atomic
def record_answer(
    *,
    attempt,
    assessment_question,
    selected_answer,
):
    """
    Save one immutable Placement answer and
    automatically advance the adaptive engine.
    """
    attempt = (
        GrammarPlacementAttempt.objects
        .select_for_update()
        .get(pk=attempt.pk)
    )

    if attempt.status != GrammarPlacementAttempt.Status.IN_PROGRESS:
        raise ValueError(
            "Placement attempt is not in progress."
        )

    if not assessment_question.is_active:
        raise ValueError(
            "Assessment question is inactive."
        )

    if attempt.stage == GrammarPlacementAttempt.Stage.SCREENING:
        expected_role = SCREENING_ROLE

    elif attempt.stage == GrammarPlacementAttempt.Stage.TOPIC:
        expected_role = TOPIC_ROLE

    else:
        raise ValueError(
            "Placement attempt is already complete."
        )

    if assessment_question.role != expected_role:
        raise ValueError(
            f"Question role {assessment_question.role} "
            f"does not match stage {attempt.stage}."
        )

    if attempt.answers.filter(
        assessment_question=assessment_question,
    ).exists():
        raise ValueError(
            "This question has already been answered."
        )

    answer = GrammarPlacementAnswer.objects.create(
        attempt=attempt,
        assessment_question=assessment_question,
        selected_answer=str(selected_answer),
        is_correct=_answer_is_correct(
            assessment_question,
            selected_answer,
        ),
    )

    _recalculate_attempt_score(attempt)

    if attempt.stage == GrammarPlacementAttempt.Stage.SCREENING:
        screening_ids = set(
            get_screening_questions().values_list(
                "id",
                flat=True,
            )
        )

        answered_screening_count = (
            attempt.answers
            .filter(
                assessment_question_id__in=screening_ids,
            )
            .count()
        )

        if answered_screening_count == len(screening_ids):
            finalize_screening(attempt)

    elif attempt.stage == GrammarPlacementAttempt.Stage.TOPIC:
        refresh_topic_assessments(attempt)

    return answer


def get_knowledge_summary(user):
    """
    Return counts for the user's current Knowledge Map.
    """
    statuses = [
        GrammarTopicAssessment.Status.UNKNOWN,
        GrammarTopicAssessment.Status.PROVISIONAL_MASTERED,
        GrammarTopicAssessment.Status.REVIEW,
        GrammarTopicAssessment.Status.LEARN,
        GrammarTopicAssessment.Status.MASTERED,
    ]

    return {
        status: GrammarTopicAssessment.objects.filter(
            user=user,
            status=status,
            lesson__level="A1",
            lesson__order__range=(1, 60),
        ).count()
        for status in statuses
    }


def get_personal_plan(user):
    """
    Topics requiring actual study.

    LEARN comes before REVIEW within lesson order.
    PROVISIONAL_MASTERED and MASTERED are skipped.
    """
    return (
        GrammarTopicAssessment.objects
        .filter(
            user=user,
            status__in=[
                GrammarTopicAssessment.Status.LEARN,
                GrammarTopicAssessment.Status.REVIEW,
            ],
            lesson__level="A1",
            lesson__order__range=(1, 60),
        )
        .select_related(
            "lesson",
            "lesson__block",
        )
        .order_by(
            "lesson__order",
        )
    )
