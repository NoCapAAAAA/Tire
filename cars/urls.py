from django.http import HttpResponse
from django.urls import path
from cars import views as v


urlpatterns = [
    path('', v.CarListView.as_view(), name='car_list'),
    path('create/', v.CarCreateView.as_view(), name='car_create'),
    path('<int:pk>/', v.CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/edit/', v.CarUpdateView.as_view(), name='car_edit'),
    path('<int:pk>/delete/', v.CarDeleteView.as_view(), name='car_delete'),
]