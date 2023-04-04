from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django import views
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
import datetime

from django.views.generic import TemplateView, DetailView

from core.mixins import ExtraContextMixin
from organization import models as m
from django.shortcuts import HttpResponseRedirect
from organization.models import OrderStatus


class HomeView(generic.TemplateView, ExtraContextMixin):
    template_name = 'clientpart/home.html'


class AboutView(generic.TemplateView):
    template_name = 'clientpart/about_us.html'


class ContactView(generic.TemplateView):
    template_name = 'clientpart/contact.html'



from tirestorage import forms as f





class StartOrder(generic.CreateView):
    template_name = 'clientpart/order_create.html'
    success_url = reverse_lazy('order-list')
    form_class = f.OrderCreateForm
    queryset = m.OrderStorage.objects.all()

    def get_form(self, form_class=None):
        from organization.models import TireSize, PeriodOfStorage, QuantityOfTires, AdressSirvice
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        form.fields['size'].queryset = TireSize.objects.all().order_by('size')
        form.fields['period'].queryset = PeriodOfStorage.objects.all().order_by('period')
        form.fields['quantity'].queryset = QuantityOfTires.objects.all().order_by('quantity')
        form.fields['adress'].queryset = AdressSirvice.objects.all().order_by('adress')
        return form

    def get_form_kwargs(self):
        ret = super().get_form_kwargs()
        ret['initial'] = {
            'user': self.request.user.pk,
            'status': OrderStatus.CREATE,
        }
        return ret


class OrderListView(LoginRequiredMixin, TemplateView):
    template_name = "clientpart/order-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = m.OrderStorage.objects.filter(user=self.request.user)
        return context


class DetailOrderView(DetailView):
    template_name = "clientpart/order-detail.html"
    model = m.OrderStorage
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = m.OrderStorage.objects.filter(pk=self.kwargs['pk'])
        return context