from collections import namedtuple
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from cars.api import views as v

router = routers.DefaultRouter()

router.register('car', v.CarViewSet)
router.register('car-brand', v.CarBrandViewSet)
router.register('car-model', v.CarModelViewSet)
router.register('car-bodywork', v.CarBodyworkViewSet)
router.register('car-class', v.CarClassViewSet)
router.register('car-salon', v.CarSalonViewSet)
router.register('car-coverage', v.CarCoverageViewSet)


urlpatterns = [
    path('', include(router.urls), name='api'),
]