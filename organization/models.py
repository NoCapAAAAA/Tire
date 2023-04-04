from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from core.models import AbstractTimestampedModel
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


class OrderStatus(models.IntegerChoices):
    CREATE = 0, 'Создан'
    STORAGE = 1, 'Находиться на хранении'
    CANCELED = 2, 'Отменено'
    FINISH = 3, 'Завершен'


class AdressSirvice(models.Model):
    adress = models.CharField(verbose_name='Адрес сервиса', max_length=125,)

    def __str__(self):
        return f'{self.adress}'

    class Meta:
        verbose_name = 'Адрес сервиса'
        verbose_name_plural = 'Адреса сервисов'


class OrderStorage(models.Model):
    user = models.ForeignKey(verbose_name='Клиент', to=User, on_delete=models.CASCADE)
    quantity = models.ForeignKey(verbose_name='Количество', to=QuantityOfTires, on_delete=models.CASCADE)
    size = models.ForeignKey(verbose_name='Размер шин', to=TireSize, on_delete=models.CASCADE)
    period = models.ForeignKey(verbose_name='Период хранение', to=PeriodOfStorage, on_delete=models.CASCADE)
    adress = models.ForeignKey(verbose_name='Адрес сервиса', to=AdressSirvice, on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name='Статус заказа', choices=OrderStatus.choices, default=0)
    is_payed = models.BooleanField(verbose_name='Оплачено', default=False)
    payed_at = models.DateTimeField(verbose_name='Дата оплаты', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return f'{self.user} {self.period}'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__original_is_payed = self.is_payed

    def save(self, force_insert=False, force_update=False, *args, **kwargs) -> None:
        if self.is_payed != self.__original_is_payed:
            self.payed_at = timezone.now()
            self.__original_is_payed = self.is_payed
        return super().save(force_insert, force_update, *args, **kwargs)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
