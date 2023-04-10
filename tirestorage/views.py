from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, DetailView, ListView
from core.mixins import ExtraContextMixin
from organization import models as m
from django.contrib.auth import get_user_model
from tirestorage import forms as f
from organization.models import OrderStatus

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
#         print(form.fields['size'])
#
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


class CreateOrderTire(LoginRequiredMixin, TemplateView):
    template_name = "clientpart/order_create.html"
    success_url = reverse_lazy('order_list_tire')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['size'] = m.TireSize.objects.all().order_by('size')
        context['period'] = m.PeriodOfStorage.objects.all().order_by('period')
        return context

    # noinspection PyUnboundLocalVariable
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
        elif tire_size in price_4000:
            price = 4000
        elif tire_size in price_4700:
            price = 4700
        elif tire_size in price_5700:
            price = 5700
        create = m.OrderStorage.objects.create(user=self.request.user,
                                               size=data.get('Tiresize')[0],
                                               period=data.get('Period')[0],
                                               price=price
                                               )
        if create:
            print('Успех')
        else:
            print('Не успех')
        return HttpResponseRedirect(self.success_url)


class OrderListView(LoginRequiredMixin, ListView):
    model = m.OrderStorage
    template_name = "clientpart/order-list.html"
    context_object_name = 'orders'
    paginate_by = 5
    def get_queryset(self):
        return m.OrderStorage.objects.filter(user=self.request.user)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['orders'] = m.OrderStorage.objects.filter(user=self.request.user)
    #     return context


class DetailOrderView(DetailView):
    template_name = "clientpart/order-detail.html"
    model = m.OrderStorage
    extra_context = {
        'status_cancelled': m.OrderStatus.CANCELED
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = m.OrderStorage.objects.filter(pk=self.kwargs['pk'])
        return context


def order_pay_tire(request, pk):
    order = get_object_or_404(m.OrderStorage, pk=pk)
    order.is_payed = True
    order.save()
    print(order.payed_at)
    return redirect(reverse_lazy('detail_order_tire', kwargs={'pk': pk}))


def order_cancel_tire(request, pk):
    order = get_object_or_404(m.OrderStorage, pk=pk)
    order.status = m.OrderStatus.CANCELED
    order.save()
    return redirect(reverse_lazy('detail_order_tire', kwargs={'pk': pk}))


def cheque_tire(request, pk):
    order = get_object_or_404(m.OrderStorage, pk=pk)
    context = {
        'order': order
    }
    return render(request, 'clientpart/cheque.html', context)
