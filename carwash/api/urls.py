from django.urls import path, include
from rest_framework import routers

from carwash.api import views as v

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
]