from django import forms
from django.contrib.auth import get_user_model

from cars.models import Car


class CarForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=get_user_model().objects.all(),
        required=True, widget=forms.HiddenInput())

    class Meta:
        model = Car
        fields = ('brand', 'model', 'bodywork',
                  'salon', 'coverage', 'state_number', 'car_class', 'owner')
