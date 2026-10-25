from django.urls import path

from . import views


app_name = "grammar"


urlpatterns = [

    path(
        "",
        views.grammar_home,
        name="home",
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
