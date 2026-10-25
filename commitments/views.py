from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render

from vocabulary.models import UserCourse

from .models import (
    CommitmentPlan,
    CourseCommitment,
    CommitmentRewardNotification,
)
from .services import (
    CommitmentAlreadyExistsError,
    CommitmentError,
    activate_commitment,
    create_commitment_draft,
)

from django.urls import reverse
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST


def build_declaration_text(commitment):
    """
    Финальный текст обещания сохраняется как snapshot.
    После принятия он больше не зависит от изменений
    текста интерфейса или CommitmentPlan.
    """

    deadline_text = f"{commitment.duration_days} дней"

    return (
        f"Я, {commitment.signed_name or '[имя пользователя]'}, "
        f"начинаю программу английского языка "
        f"{commitment.plan.level.code}.\n\n"

        f"Моя цель:\n"
        f"{commitment.goal_text}\n\n"

        f"Почему эта цель важна для меня:\n"
        f"{commitment.motivation_text}\n\n"

        f"Я выбираю пройти программу за "
        f"{commitment.duration_days} дней.\n\n"

        f"Стоимость обучения составляет "
        f"{commitment.tuition_amount:.0f} ₸.\n"

        f"Возвратная часть программы составляет "
        f"{commitment.refundable_amount:.0f} ₸.\n\n"

        f"За каждый завершённый Lesson я могу вернуть "
        f"{commitment.lesson_reward:.0f} ₸.\n"

        f"За каждый завершённый Unified Practice я могу вернуть "
        f"{commitment.unified_practice_reward:.0f} ₸.\n\n"

        f"Ошибки во время обучения не уменьшают мой депозит.\n"

        f"Я понимаю, что невыполнение учебных этапов "
        f"в предусмотренные сроки может уменьшить сумму возврата.\n\n"

        f"Я беру это обязательство прежде всего перед собой."
    )


@login_required
def commitment_setup(request, user_course_id):
    user_course = get_object_or_404(
        UserCourse,
        id=user_course_id,
        user=request.user,
    )

    existing = CourseCommitment.objects.filter(
        user_course=user_course,
    ).first()

    if existing:
        if existing.status == CourseCommitment.Status.DRAFT:
            return redirect(
                "commitments:declaration",
                user_course_id=user_course.id,
            )

        return redirect(
            "commitments:started",
            user_course_id=user_course.id,
        )

    plan = get_object_or_404(
        CommitmentPlan,
        level=user_course.level,
        is_active=True,
    )

    if request.method == "POST":
        goal_text = request.POST.get(
            "goal_text",
            "",
        ).strip()

        motivation_text = request.POST.get(
            "motivation_text",
            "",
        ).strip()

        if len(goal_text) < 10:
            return render(
                request,
                "commitments/setup.html",
                {
                    "user_course": user_course,
                    "plan": plan,
                    "goal_text": goal_text,
                    "motivation_text": motivation_text,
                    "error": (
                        "Опишите вашу цель немного подробнее."
                    ),
                },
            )

        if len(motivation_text) < 10:
            return render(
                request,
                "commitments/setup.html",
                {
                    "user_course": user_course,
                    "plan": plan,
                    "goal_text": goal_text,
                    "motivation_text": motivation_text,
                    "error": (
                        "Напишите, почему эта цель действительно "
                        "важна для вас."
                    ),
                },
            )

        try:
            create_commitment_draft(
                user_course=user_course,
                plan=plan,
                goal_text=goal_text,
                motivation_text=motivation_text,
            )

        except CommitmentAlreadyExistsError:
            pass

        return redirect(
            "commitments:declaration",
            user_course_id=user_course.id,
        )

    return render(
        request,
        "commitments/setup.html",
        {
            "user_course": user_course,
            "plan": plan,
        },
    )


@login_required
def commitment_declaration(request, user_course_id):
    user_course = get_object_or_404(
        UserCourse,
        id=user_course_id,
        user=request.user,
    )

    commitment = get_object_or_404(
        CourseCommitment,
        user_course=user_course,
    )

    if commitment.status != CourseCommitment.Status.DRAFT:
        return redirect(
            "commitments:started",
            user_course_id=user_course.id,
        )

    if request.method == "POST":
        signed_name = request.POST.get(
            "signed_name",
            "",
        ).strip()

        accept_rules = (
            request.POST.get("accept_rules") == "on"
        )

        accept_refund = (
            request.POST.get("accept_refund") == "on"
        )

        accept_commitment = (
            request.POST.get("accept_commitment") == "on"
        )

        if len(signed_name) < 2:
            return render(
                request,
                "commitments/declaration.html",
                {
                    "commitment": commitment,
                    "error": "Введите ваше имя.",
                },
            )

        if not (
            accept_rules
            and accept_refund
            and accept_commitment
        ):
            return render(
                request,
                "commitments/declaration.html",
                {
                    "commitment": commitment,
                    "signed_name": signed_name,
                    "error": (
                        "Для начала программы необходимо "
                        "подтвердить все три пункта."
                    ),
                },
            )

        # Имя временно устанавливаем объекту,
        # чтобы оно попало в declaration snapshot.
        commitment.signed_name = signed_name

        declaration_snapshot = build_declaration_text(
            commitment
        )

        try:
            activate_commitment(
                commitment=commitment,
                signed_name=signed_name,
                declaration_snapshot=declaration_snapshot,
            )

        except CommitmentError as exc:
            return HttpResponseBadRequest(str(exc))

        return redirect(
            "commitments:started",
            user_course_id=user_course.id,
        )

    return render(
        request,
        "commitments/declaration.html",
        {
            "commitment": commitment,
        },
    )


@login_required
def commitment_started(request, user_course_id):
    user_course = get_object_or_404(
        UserCourse,
        id=user_course_id,
        user=request.user,
    )

    commitment = get_object_or_404(
        CourseCommitment,
        user_course=user_course,
    )

    milestone_count = (
        commitment.milestones.count()
    )

    checkpoint_count = (
        commitment.checkpoints.count()
    )

    return render(
        request,
        "commitments/started.html",
        {
            "user_course": user_course,
            "commitment": commitment,
            "milestone_count": milestone_count,
            "checkpoint_count": checkpoint_count,
        },
    )


@login_required
@require_POST
def reward_notification_seen(
    request,
    notification_id,
):
    notification = get_object_or_404(
        CommitmentRewardNotification,
        id=notification_id,
        commitment__user_course__user=request.user,
    )

    if not notification.is_seen:
        notification.is_seen = True
        notification.seen_at = timezone.now()

        notification.save(
            update_fields=[
                "is_seen",
                "seen_at",
            ]
        )

    next_url = request.POST.get("next", "").strip()

    if not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = reverse("vocabulary:dashboard")

    return redirect(next_url)
