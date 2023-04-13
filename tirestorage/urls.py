from django.http import HttpResponse
from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('order_crate_tire/', v.StartOrder.as_view(), name='order_crate_tire'),
    path('about_tire/', v.AboutView.as_view(), name='about_tire'),
    path('contact_tire/', v.ContactView.as_view(), name='contact_tire'),
    path('order_list_tire/', v.OrderListView.as_view(), name='order_list_tire'),
    path('order_list_tire/<int:pk>/', v.DetailOrderView.as_view(), name='detail_order_tire'),
    #
    path('order_pay_tire/<int:pk>/', v.order_pay_tire, name='order_pay_tire'),
    path('order_cancel_tire/<int:pk>/', v.order_cancel_tire, name='order_cancel_tire'),
    path('order_cheque_tire/<int:pk>/', v.cheque_tire, name='order_cheque_tire'),
]
