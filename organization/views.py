from django.shortcuts import render
from django.views.generic import FormView, UpdateView, DetailView, TemplateView
from . import models as m

class DirectorHomeView(TemplateView):
    template_name = 'director/home.html'


class DirectorOrdersView(TemplateView):
    template_name = 'director/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = m.OrderStorage.objects.all()
        return context


class DirectorUsersView(TemplateView):
    template_name = 'director/users.html'


class DirectorStuffView(TemplateView):
    template_name = 'director/stuff.html'


class DirectorClientsView(TemplateView):
    template_name = 'director/clients.html'


class DirectorStatisticsView(TemplateView):
    template_name = 'director/statistics.html'


class ManagerHomeView(TemplateView):
    template_name = 'manager/home.html'


class ManagerOrdersView(TemplateView):
    template_name = 'manager/orders.html'
