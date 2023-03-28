from django.shortcuts import render


class Test(TemplateView):
    template_name = 'director/home.html'


class Test2(TemplateView):
    template_name = 'manager/home.html'
