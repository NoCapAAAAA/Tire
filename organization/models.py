from django.db import models
import datetime
from django.contrib.auth import get_user_model
from django.db.models import IntegerField

User = get_user_model()


class TireSize(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return f'{self.size}'

    class Meta:
        verbose_name = 'Диаметр шины'
        verbose_name_plural = 'Диаметр шин'


class PeriodOfStorage(models.Model):
    period = models.IntegerField()

    def __str__(self):
        return f'{self.period} Мес'

    class Meta:
        verbose_name = 'Срок хранения'


class QuantityOfTires(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity}'

    class Meta:
        verbose_name = 'Количество шин'


from django.conf import settings


class Status(models.TextChoices):
    CREATED = 'Создан', 'Создан'
    CANCELLED = 'Отменён', 'Отменён'
    WESTORE = 'На хранении', 'На хранении'
    COMLETED = 'Завершён', 'Завершён'
    INWORK = 'Передан в работу', 'Передан в работу'
    DONE = 'Готов к получению', 'Готов к получению'


class TireStore(models.Model):
    user = models.ForeignKey(verbose_name='Клиент', to=User, on_delete=models.CASCADE)
    quantity = models.ForeignKey(verbose_name='Количество', to=QuantityOfTires, on_delete=models.CASCADE)
    size = models.ForeignKey(verbose_name='Размер шин', to=TireSize, on_delete=models.CASCADE)
    period = models.ForeignKey(verbose_name='Период хранение', to=PeriodOfStorage, on_delete=models.CASCADE)
    status = models.CharField('Статус', default='Ожидает подтверждения', max_length=30,
                              choices=Status.choices, blank=True)
    def __str__(self):
        return f'{self.user}|{self.quantity}|{self.status}'
