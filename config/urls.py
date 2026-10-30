from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path
from django.views.static import serve

from vocabulary import views as vocabulary_views


urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),


    # ==========================================
    # AUTH
    # ==========================================

    path(
        "accounts/register/",
        vocabulary_views.register_view,
        name="register",
    ),

    path(
        "accounts/",
        include(
            "django.contrib.auth.urls"
        ),
    ),


    # ==========================================
    # VOCABULARY
    # ==========================================

    path(
        "vocabulary/",
        include(
            "vocabulary.urls"
        ),
    ),


    # ==========================================
    # GRAMMAR
    # ==========================================

    path(
        "grammar/",
        include("grammar.urls"),
    ),



    # ==========================================
    # HOME REDIRECT
    # ==========================================

    path(
        "",
        lambda request:
            redirect(
                "vocabulary:home"
            ),
    ),


    path(
        "commitment/",
        include("commitments.urls"),
    ),


]


# ==============================================
# MEDIA FILES
# ==============================================

if settings.DEBUG:

    # Локальная разработка
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

else:

    # Временное решение для тестовой
    # версии на Railway.
    # Наши MP3 уже находятся в репозитории.
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root":
                    settings.MEDIA_ROOT,
            },
        ),
    ]