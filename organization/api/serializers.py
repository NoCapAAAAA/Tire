from rest_framework import serializers
from organization import models as m

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.OrderStorage
        fields = '__all__'
