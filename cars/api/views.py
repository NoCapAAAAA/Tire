from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from cars import models as m
from cars.api import serializers as s


class CarBrandViewSet(viewsets.ModelViewSet):
    serializer_class = s.CarBrandSerializer
    queryset = m.CarBrand.objects.all()


class CarModelViewSet(viewsets.ModelViewSet):
    serializer_class = s.CarModelSerializer
    queryset = m.CarModel.objects.all()


class CarBodyworkViewSet(viewsets.ModelViewSet):
    serializer_class = s.CarBodyworkSerializer
    queryset = m.CarBodywork.objects.all()


class CarClassViewSet(viewsets.ModelViewSet):
    serializer_class = s.CarClassSerializer
    queryset = m.CarClass.objects.all()


class CarSalonViewSet(viewsets.ModelViewSet):
    serializer_class = s.CarSalonSerializer
    queryset = m.CarSalon.objects.all()


class CarCoverageViewSet(viewsets.ModelViewSet):
    serializer_class = s.CarCoverageSerializer
    queryset = m.CarCoverage.objects.all()


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = s.CarSerializer
    queryset = m.Car.objects.all()