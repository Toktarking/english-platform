from django.urls import path

from . import views


app_name = "vocabulary"


urlpatterns = [

    # ВАЖНО:
    # этот URL должен идти ДО <str:level_code>/
    path(
        "record-answer/",
        views.record_answer,
        name="record_answer",
    ),

    # ==========================================
    # COURSE ONBOARDING
    # ==========================================

    path(
        "course/setup/",
        views.course_setup,
        name="course_setup",
    ),

    path(
        "course/preview/",
        views.course_preview,
        name="course_preview",
    ),

    path(
        "course/confirm/",
        views.course_confirm,
        name="course_confirm",
    ),


    # ==========================================
    # DASHBOARD
    # ==========================================

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),

    path(
        "dashboard/start/",
        views.dashboard_start,
        name="dashboard_start",
    ),

    path(
        "review/today/",
        views.daily_review,
        name="daily_review",
    ),

    path(
        "",
        views.vocabulary_home,
        name="home",
    ),

    path(
        "<str:level_code>/",
        views.level_detail,
        name="level_detail",
    ),

    path(
        "<str:level_code>/group/<int:group_id>/",
        views.group_detail,
        name="group_detail",
    ),

    path(
        "<str:level_code>/lesson/<int:lesson_id>/",
        views.lesson_detail,
        name="lesson_detail",
    ),

    path(
        "<str:level_code>/lesson/<int:lesson_id>/practice/",
        views.lesson_practice,
        name="lesson_practice",
    ),

    path(
        "<str:level_code>/group/<int:group_id>/practice1/",
        views.group_practice1,
        name="group_practice1",
    ),

    path(
        "<int:group_id>/practice1/answer/",
        views.group_practice1_answer,
        name="group_practice1_answer",
    ),

    path(
        "<int:group_id>/practice1/restart/",
        views.group_practice1_restart,
        name="group_practice1_restart",
    ),

    path(
        "<str:level_code>/group/<int:group_id>/practice2/",
        views.group_practice2,
        name="group_practice2",
    ),

    path(
        "<int:group_id>/practice2/answer/",
        views.group_practice2_answer,
        name="group_practice2_answer",
    ),

    path(
        "<int:group_id>/practice2/restart/",
        views.group_practice2_restart,
        name="group_practice2_restart",
    ),

    path(
        "<str:level_code>/group/<int:group_id>/practice3/",
        views.group_practice3,
        name="group_practice3",
    ),

    path(
        "<int:group_id>/practice3/answer/",
        views.group_practice3_answer,
        name="group_practice3_answer",
    ),

    path(
        "<int:group_id>/practice3/restart/",
        views.group_practice3_restart,
        name="group_practice3_restart",
    ),


    path(
        "lesson/<int:lesson_id>/practice-progress/",
        views.lesson_practice_progress,
        name="lesson_practice_progress",
    ),


    # ==========================================
    # PRACTICE 4
    # LISTENING
    # ==========================================

    path(
        "<str:level_code>/group/<int:group_id>/practice4/",
        views.group_practice4,
        name="group_practice4",
    ),

    path(
        "<int:group_id>/practice4/answer/",
        views.group_practice4_answer,
        name="group_practice4_answer",
    ),

    path(
        "<int:group_id>/practice4/restart/",
        views.group_practice4_restart,
        name="group_practice4_restart",
    ),








]


