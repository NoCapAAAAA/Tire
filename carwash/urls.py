from django.http import HttpResponse
from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('contacts/', v.ContactsView.as_view(), name='contacts'),
    path('about/', v.AboutView.as_view(), name='about'),
    path('prices/', v.PricesView.as_view(), name='prices'),
    path('orders/', v.OrderListView.as_view(), name='order_list'),
    path('orders/create/', v.OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', v.OrderDetailView.as_view(), name='order_detail'),
    path('order-pay/<int:pk>/', v.order_pay, name='order_pay'),
    path('order-cancel/<int:pk>/', v.order_cancel, name='order_cancel'),
    path('order-cheque/<int:pk>/', v.cheque, name='order_cheque'),
    path('contactless-wash/', v.contactless_wash, name='contactless_wash'),
    path('complex-wash/', v.complex_wash, name='complex_wash'),
    path('nano-wash/', v.nano_wash, name='nano_wash'),
    path('ceramic-wash/', v.ceramic_wash, name='ceramic_wash'),
    path('bottom-wash/', v.bottom_wash, name='bottom_wash'),
    path('engine-wash/', v.engine_wash, name='engine_wash'),
]
