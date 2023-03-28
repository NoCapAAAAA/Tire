from django.shortcuts import render
from django.views.generic import FormView, UpdateView, DetailView, TemplateView


class DirectorHomeView(TemplateView):
    template_name = 'director/home.html'


class DirectorOrdersView(TemplateView):
    template_name = 'director/orders.html'


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
