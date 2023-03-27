from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from cars.forms import CarForm


class CarListView(generic.ListView):
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return self.request.user.car_set.all()


class CarDetailView(generic.DetailView):
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

    def get_queryset(self):
        return self.request.user.car_set.all()


class CarDeleteView(generic.DeleteView):
    success_url = reverse_lazy('car_list')

    def get_queryset(self):
        return self.request.user.car_set.all()


class CarUpdateView(generic.UpdateView):
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_list')
    form_class = CarForm

    def get_queryset(self):
        return self.request.user.car_set.all()


class CarCreateView(generic.CreateView):
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_list')
    form_class = CarForm

    def get_initial(self):
        return {'owner': self.request.user}
