from django.urls import path

from . import views


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
        views.grammar_placement,
        name="placement",
    ),

    path(
        "placement/start/",
        views.start_grammar_placement,
        name="placement_start",
    ),

    path(
        "placement/answer/",
        views.answer_grammar_placement,
        name="placement_answer",
    ),

    path(
        "placement/result/",
        views.grammar_placement_result,
        name="placement_result",
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
