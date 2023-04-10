from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
user_model = get_user_model()


class SettingsProfile(auth_forms.UserChangeForm):
    password = None

    class Meta:
        model = user_model
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name', 'phone_number', 'gender', 'photo')