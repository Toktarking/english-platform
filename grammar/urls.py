from django.urls import path

from . import block_practice, views


app_name = "grammar"


urlpatterns = [

    path(
        "",
        views.grammar_home,
        name="home",
    ),

    # IMPORTANT:
    # Placement routes must come BEFORE <slug:slug>/.
    path(
        "placement/",
        views.placement_disabled,
        name="placement",
    ),

    path(
        "placement/start/",
        views.placement_disabled,
        name="placement_start",
    ),

    path(
        "placement/answer/",
        views.placement_disabled,
        name="placement_answer",
    ),

    path(
        "placement/result/",
        views.placement_disabled,
        name="placement_result",
    ),

    path(
        "plan/",
        views.grammar_plan,
        name="plan",
    ),

    path(
        "plan/setup/",
        views.grammar_plan_setup,
        name="plan_setup",
    ),

    path(
        "exam-practice/",
        views.grammar_exam_practice,
        name="exam_practice",
    ),

    path(
        "exam-practice/start/",
        views.start_grammar_exam_practice,
        name="exam_practice_start",
    ),

    path(
        "exam-practice/answer/",
        views.answer_grammar_exam_practice,
        name="exam_practice_answer",
    ),

    path(
        "<slug:slug>/study-progress/",
        views.grammar_lesson_study_progress,
        name="study_progress",
    ),

    path(
        "<slug:slug>/final/",
        views.grammar_final_test,
        name="final_test",
    ),

    path(
        "block/1/practice/",
        block_practice.block_1_practice,
        name="block_1_practice",
    ),


    path(
        "block/2/practice/",
        block_practice.block_2_practice,
        name="block_2_practice",
    ),


    path(
        "block/<int:block_order>/practice/",
        block_practice.block_practice,
        name="block_practice",
    ),


    path(
        "balance/",
        views.grammar_balance,
        name="balance",
    ),

    path(
        "rewards/",
        views.grammar_rewards,
        name="rewards",
    ),

    path(
        "profile/",
        views.grammar_profile,
        name="profile",
    ),

    path(
        "<slug:slug>/",
        views.grammar_lesson,
        name="lesson",
    ),

    path(
        "<slug:slug>/complete/",
        views.complete_lesson,
        name="complete",
    ),

]
