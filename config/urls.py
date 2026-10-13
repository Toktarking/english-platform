from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static

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
    # HOME REDIRECT
    # ==========================================

    path(
        "",
        lambda request:
            redirect(
                "vocabulary:home"
            ),
    ),

]


# ==============================================
# MEDIA FILES
# Только для локальной разработки
# ==============================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )