from django import forms
from organization import models as m
from django.contrib.auth import get_user_model


class OrderCreateForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(), widget=forms.HiddenInput())
    status = forms.IntegerField(widget=forms.HiddenInput())
    is_payed = forms.BooleanField(required=False, widget=forms.HiddenInput())
    payed_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)


    class Meta:
        model = m.OrderStorage
        fields = '__all__'