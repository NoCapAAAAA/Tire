from django.urls import path, include
from rest_framework import routers

from carwash.api import views as v

router = routers.DefaultRouter()

router.register('service', v.ServiceViewSet)
router.register('order', v.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]