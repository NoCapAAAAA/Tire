from django.shortcuts import render
from django import views
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
import datetime
from core.mixins import ExtraContextMixin


class HomeView(generic.TemplateView, ExtraContextMixin):
    template_name = 'clientpart/home.html'
    extra_context = {
        'header_selected_index': 0
    }