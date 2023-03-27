from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from core.models import AbstractTimestampedModel


class CarBrand(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class CarModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class CarBodywork(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузовы'


class CarSalon(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class CarCoverage(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Покрытие'
        verbose_name_plural = 'Покрытия'


class CarClass(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Car(AbstractTimestampedModel):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')
    bodywork = models.ForeignKey(CarBodywork, on_delete=models.CASCADE, verbose_name='Кузов')
    salon = models.ForeignKey(CarSalon, on_delete=models.CASCADE, verbose_name='Салон')
    coverage = models.ForeignKey(CarCoverage, on_delete=models.CASCADE, verbose_name='Покрытие')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Владелец')
    state_number = models.CharField(max_length=20, verbose_name='Госномер')
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE, verbose_name='Класс авто')
    
    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})
    
    def get_car_class(self):
        if self.car_class is not None:
            return self.car_class
        return 'Не определен'
    
    def get_readable_name(self):
        return f'{self.brand} {self.model} ({self.state_number})'

    def __str__(self) -> str:
        return self.state_number

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
