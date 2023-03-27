from rest_framework import serializers
from cars import models as m


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CarModel
        fields = '__all__'


class CarBodyworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CarBodywork
        fields = '__all__'


class CarClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CarClass
        fields = '__all__'


class CarCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CarCoverage
        fields = '__all__'


class CarSalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CarSalon
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Car
        fields = '__all__'