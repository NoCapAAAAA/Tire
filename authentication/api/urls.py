from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from authentication.api import views as v

router = routers.DefaultRouter()

router.register('user', v.UserViewSet)

urlpatterns = [
    path('', include(router.urls), name='api'),
]