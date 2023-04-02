from rest_framework import serializers
from organization import models as m


class TireSizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = m.TireSize
        fields = '__all__'