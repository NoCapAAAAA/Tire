from django.urls import path, include
from rest_framework import routers

from organization.api import views as v

router = routers.DefaultRouter()

router.register('order', v.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]