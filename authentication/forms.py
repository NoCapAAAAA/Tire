from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import forms as auth_forms

from profiles.models import ClientProfile


user_model = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # todo check if I need this form
    class Meta:
        model = user_model
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    # todo
    class Meta:
        model = user_model
        fields = ('email',)


class LoginForm(auth_forms.AuthenticationForm):
    pass


class UserEditForm(auth_forms.UserChangeForm):
    password = None
    class Meta:
        model = user_model
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name',
            'phone_number', 'gender', 'photo')


class RegisterForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

    class Meta:
        model = user_model
        fields = ('username', 'email', 'first_name', 'last_name',
            'middle_name', 'gender', 'phone_number', 'password1', 'password2')


class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
