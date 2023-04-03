from rest_framework import viewsets

from organization import models as m
from organization.api import serializers as s


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = s.OrderSerializer
    queryset = m.OrderStorage.objects.all()

