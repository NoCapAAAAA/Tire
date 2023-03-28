from django.db import models
import datetime

from django.db.models import IntegerField


class TireSize(models.Model):
    size = models.IntegerField()

    def __str__(self) -> IntegerField:
        return self.size

    class Meta:
        verbose_name = 'Диаметр шины'
        verbose_name_plural = 'Диаметр шин'


class PeriodOfStorage(models.Model):
    period = models.IntegerField()

    def __int__(self) -> IntegerField:
        return self.period

    class Meta:
        verbose_name = 'Срок хранения'


class QuantityOfTires(models.Model):
    quantity = models.IntegerField()

    def __int__(self) -> IntegerField:
        return self.quantity

    class Meta:
        verbose_name = 'Количество шин'


