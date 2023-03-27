from django import forms
from django.contrib.auth import get_user_model

from profiles import models as m
from authentication.forms import UserEditForm


class ClientProfileForm(forms.ModelForm):
    photo = forms.ImageField(label='Фото')

    class Meta:
        model = get_user_model()
        fields = '__all__'


# class ClientProfileForm(forms.ModelForm):
#     class Meta:
#         model = m.ClientProfile
#         fields = ('photo', )