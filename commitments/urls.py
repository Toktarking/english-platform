from django.urls import path

from . import views


app_name = "commitments"


urlpatterns = [
    path(
        "<int:user_course_id>/setup/",
        views.commitment_setup,
        name="setup",
    ),
    path(
        "<int:user_course_id>/declaration/",
        views.commitment_declaration,
        name="declaration",
    ),
    path(
        "<int:user_course_id>/started/",
        views.commitment_started,
        name="started",
    ),


    path(
        "reward/<int:notification_id>/seen/",
        views.reward_notification_seen,
        name="reward_notification_seen",
    ),

]