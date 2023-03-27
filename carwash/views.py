from django import views
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
import datetime
from django.db.models import Sum

from carwash.models import Service, OrderStatus
from core.mixins import ExtraContextMixin
from carwash import forms as f
from carwash.utils import get_order_total_sum
from carwash.models import OrderStatus
from carwash import models as m


class AboutView(generic.TemplateView):
    template_name = 'carwash/about.html'
    extra_context = {
        'header_selected_index': 2
    }

class PricesView(generic.TemplateView):
    template_name = 'carwash/prices.html'
    extra_context = {
        'services': Service.objects.all(), 
        'header_selected_index': 1
    }

class HomeView(generic.TemplateView, ExtraContextMixin):
    template_name = 'carwash/home.html'
    extra_context = {
        'header_selected_index': 0
    }

class ContactsView(generic.CreateView):
    template_name = 'carwash/contacts.html'
    extra_context = {
        'header_selected_index': 3,
    }
    model = m.CallApplication
    success_url = reverse_lazy('contacts')
    fields = '__all__'


class OrderListView(generic.ListView):
    template_name = 'carwash/order_list.html'
    template_name_report = 'carwash/order_report.html'
    context_object_name = 'orders'
    def is_report(self):
        is_report = self.request.GET.get('report', None)
        return is_report is not None
    def get_template_names(self) -> list[str]:
        if self.is_report():
            return self.template_name_report
        return self.template_name
    # def get_order_total_sum(self):
    #     orders = self.get_queryset()
    #     sum = 0
    #     for i in orders:
    #         sum += i.price.price
    #     return sum

    def get_date_range_default(self):
        date1 = self.request.user.get_first_order_date()
        date2 = timezone.now()
        return date1, date2

    def get_date_range(self):
        strptime = datetime.datetime.strptime
        try:
            date1 = (strptime(self.request.GET.get('date_from'), r'%Y-%m-%d'))
            date2 = (strptime(self.request.GET.get('date_until'), r'%Y-%m-%d'))
        except TypeError:
            date1, date2 = self.get_date_range_default()
        
        if date1 > date2:
            date1, date2 = date2, date1
        return date1, date2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date1, date2 = self.get_date_range()
        context['date_from'], context['date_until'] = (
            date1.strftime(r'%Y-%m-%d'), date2.strftime(r'%Y-%m-%d'))
        context['total_sum'] = get_order_total_sum(self.get_queryset())
        context['today'] = timezone.now()
        return context

    def get_queryset(self):
        queryset = self.request.user.order_set.all()
        date_from, date_until = self.get_date_range()
        queryset = queryset.filter(
            created_at__gte=datetime.datetime.combine(date_from, datetime.time.min),
            created_at__lte=datetime.datetime.combine(date_until, datetime.time.max)
        )
        return queryset


class OrderDetailView(generic.DetailView):
    template_name = 'carwash/order_detail.html'
    context_object_name = 'order'
    extra_context = {
        'status_cancelled': m.OrderStatus.CANCELED
    }

    def get_queryset(self):
        return self.request.user.order_set.all()


class OrderCreateView(generic.CreateView):
    template_name = 'carwash/order_create.html'
    success_url = reverse_lazy('order_list')
    form_class = f.OrderCreateForm
    queryset = m.Order.objects.all()

    def get_form(self, form_class=None):
        from cars.models import Car
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        form.fields['car'].queryset = Car.objects.filter(owner__pk=self.request.user.pk)
        return form

    def get_form_kwargs(self):
        ret = super().get_form_kwargs()
        ret['initial'] = {
            'client': self.request.user.pk,
            'status': OrderStatus.NOT_DONE
        }
        return ret


def order_pay(request, pk):
    order = get_object_or_404(m.Order, pk=pk)
    order.is_payed = True
    order.save()
    print(order.payed_at)
    return redirect(reverse_lazy('order_list'))

def order_cancel(request, pk):
    order = get_object_or_404(m.Order, pk=pk)
    order.status = m.OrderStatus.CANCELED
    order.save()
    return redirect(reverse_lazy('order_detail', kwargs={'pk': pk}))

def cheque(request, pk):
    order = get_object_or_404(m.Order, pk=pk)
    context = {
        'order': order
    }
    return render(request, 'carwash/cheque.html', context)


class CallApplicationCreateView(generic.CreateView):
    from carwash.models import CallApplication
    template_name = 'carwash/call_application.html'
    # success_url = 
    form_class = f.CallApplicationForm
    queryset = CallApplication.objects.all()

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        print(form)
        return form


def contactless_wash(request):
    return render(request, 'carwash/contactless_wash.html')

def complex_wash(request):
    return render(request, 'carwash/complex_wash.html')

def nano_wash(request):
    return render(request, 'carwash/nano_wash.html')

def ceramic_wash(request):
    return render(request, 'carwash/ceramic_wash.html')

def bottom_wash(request):
    return render(request, 'carwash/bottom_wash.html')

def engine_wash(request):
    return render(request, 'carwash/engine_wash.html')