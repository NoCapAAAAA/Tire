from django.http import HttpResponse
from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('order/', v.StartOrder.as_view(), name='order'),
    path('about/', v.AboutView.as_view(), name='about-us'),
    path('contact/', v.ContactView.as_view(), name='contact'),
    path('order-list/', v.OrderListView.as_view(), name='order-list'),
    path('order-list/<int:pk>/', v.DetailOrderView.as_view(), name='detail-order'),
]