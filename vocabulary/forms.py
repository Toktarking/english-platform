from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import VocabularyLevel


User = get_user_model()


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "example@email.com",
                "autocomplete": "email",
            }
        ),
    )

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите имя пользователя",
                "autocomplete": "username",
            }
        ),
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                "autocomplete": "new-password",
            }
        ),
    )

    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Повторите пароль",
                "autocomplete": "new-password",
            }
        ),
    )

    class Meta:

        model = User

        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):

        email = (
            self.cleaned_data
            .get("email", "")
            .strip()
            .lower()
        )

        existing_users = (
            User.objects
            .filter(
                email__iexact=email,
            )
        )

        # При регистрации trial-пользователя
        # мы редактируем уже существующий User,
        # поэтому самого себя исключаем.
        if self.instance and self.instance.pk:
            existing_users = (
                existing_users
                .exclude(
                    pk=self.instance.pk,
                )
            )

        if existing_users.exists():

            raise forms.ValidationError(
                "Пользователь с таким email уже существует."
            )

        return email

    def save(
        self,
        commit=True,
    ):

        user = super().save(
            commit=False
        )

        user.email = (
            self.cleaned_data["email"]
            .strip()
            .lower()
        )

        if commit:
            user.save()

        return user






# =========================================================
# COURSE SETUP
# =========================================================


class CourseSetupForm(forms.Form):

    level = forms.ModelChoiceField(
        queryset=VocabularyLevel.objects.none(),
        label="Уровень",
        empty_label=None,
        widget=forms.Select(
            attrs={
                "class": "course-input",
            }
        ),
    )


    duration_days = forms.IntegerField(
        label="Количество дней",
        min_value=1,
        max_value=365,
        initial=60,
        widget=forms.NumberInput(
            attrs={
                "class": "course-input",
                "min": "1",
                "max": "365",
                "placeholder": "Например, 60",
            }
        ),
    )


    def __init__(
        self,
        *args,
        **kwargs,
    ):

        super().__init__(
            *args,
            **kwargs,
        )


        self.fields[
            "level"
        ].queryset = (
            VocabularyLevel.objects
            .filter(
                is_active=True,
            )
            .order_by(
                "order",
            )
        )
