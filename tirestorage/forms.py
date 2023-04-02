from django import forms
from organization import models as m
from django.contrib.auth import get_user_model


class OrderCreateForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = m.TireStore
        fields = '__all__'