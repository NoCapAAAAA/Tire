from rest_framework import serializers
from carwash import models as m


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Service
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Order
        fields = '__all__'
