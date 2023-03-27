from django import forms
from carwash import models as m
from django.contrib.auth import get_user_model


class OrderCreateForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=get_user_model().objects.all(), widget=forms.HiddenInput())
    is_payed = forms.BooleanField(required=False, widget=forms.HiddenInput())
    status = forms.IntegerField(widget=forms.HiddenInput())
    payed_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = m.Order
        fields = '__all__'


class CallApplicationForm(forms.ModelForm):
    class Meta:
        model = m.CallApplication
        fields = '__all__'