from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, DetailView
from core.mixins import ExtraContextMixin
from organization import models as m
from django.contrib.auth import get_user_model
User = get_user_model()


class HomeView(generic.TemplateView, ExtraContextMixin):
    template_name = 'clientpart/home.html'


class AboutView(generic.TemplateView):
    template_name = 'clientpart/about_us.html'


class ContactView(generic.TemplateView):
    template_name = 'clientpart/contact.html'


# class StartOrder(generic.CreateView):
#     template_name = 'clientpart/order_create.html'
#     success_url = reverse_lazy('order-list')
#     form_class = f.OrderCreateForm
#     queryset = m.OrderStorage.objects.all()
#
#     def get_form(self, form_class=None):
#         from organization.models import TireSize, PeriodOfStorage, QuantityOfTires, AdressSirvice
#         if form_class is None:
#             form_class = self.get_form_class()
#         form = form_class(**self.get_form_kwargs())
#         form.fields['size'].queryset = TireSize.objects.all().order_by('size')
#         form.fields['period'].queryset = PeriodOfStorage.objects.all().order_by('period')
#         form.fields['quantity'].queryset = QuantityOfTires.objects.all().order_by('quantity')
#
#         return form
#
#     def get_form_kwargs(self):
#         ret = super().get_form_kwargs()
#         ret['initial'] = {
#             'user': self.request.user.pk,
#             'status': OrderStatus.CREATE,
#         }
#         return ret
class StartOrder(LoginRequiredMixin, TemplateView):
    template_name = "clientpart/order_create.html"
    success_url = reverse_lazy('order-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['size'] = m.TireSize.objects.all().order_by('size')
        context['period'] = m.PeriodOfStorage.objects.all().order_by('period')
        return context

    def post(self, request):
        data = dict(request.POST)
        print(data)
        tire_size = int(data.get('Tiresize')[0])
        price_3500 = [13, 14, 15]
        price_4000 = [16, 17, 18]
        price_4700 = [18, 19]
        price_5700 = [20, 21, 21]
        if tire_size in price_3500:
            price = 3500
            print("Цена услуги", price)
        elif tire_size in price_4000:
            price = 4000
            print("Цена услуги", price)
        elif tire_size in price_4700:
            price = 4700
            print("Цена услуги", price)
        elif tire_size in price_5700:
            price = 5700
            print("Цена услуги", price)
        create = m.OrderStorage.objects.create(user=self.request.user,
                                               size=data.get('Tiresize')[0],
                                               period=data.get('Period')[0],
                                               price=price
                                               )
        if create:
            print('Круто')
        else:
            print('Я тупая вагина')
        return HttpResponseRedirect(self.success_url)


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
