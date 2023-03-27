from rest_framework import viewsets

from carwash import models as m
from carwash.api import serializers as s


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = s.ServiceSerializer
    queryset = m.Service.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = s.OrderSerializer
    queryset = m.Order.objects.all()