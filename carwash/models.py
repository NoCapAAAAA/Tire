from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from cars.models import Car, CarClass
from core.models import AbstractTimestampedModel


User = get_user_model()


class Service(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField(
        verbose_name='Описание', default='', blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Price(models.Model):
    service = models.ForeignKey(
        verbose_name='Услуга', to=Service, on_delete=models.CASCADE)
    car_class = models.ForeignKey(
        verbose_name='Класс', to=CarClass, on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name='Цена', max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'{self.service} {self.car_class} {self.price}'

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ('service', 'car_class')


class OrderStatus(models.IntegerChoices):
    NOT_DONE = 0, 'Не выполнено'
    DONE = 1, 'Выполнено'
    CANCELED = 2, 'Отменено'


class Order(AbstractTimestampedModel):
    client = models.ForeignKey(
        verbose_name='Клиент', to=User, on_delete=models.CASCADE)
    price = models.ForeignKey(
        verbose_name='Цена', to=Price, on_delete=models.CASCADE)
    car = models.ForeignKey(verbose_name='Авто', to=Car,
                            on_delete=models.CASCADE)
    is_payed = models.BooleanField(verbose_name='Оплачено', default=False)
    status = models.IntegerField(verbose_name='Состояние', choices=OrderStatus.choices, default=0)
    payed_at = models.DateTimeField(verbose_name='Дата оплаты', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

    def get_sum(self):
        return self.price.price

    def get_nds(self):
        from decimal import Decimal, ROUND_HALF_DOWN
        try:
            res = self.price.price * Decimal(0.2)
            return res.quantize(Decimal("1.00"), ROUND_HALF_DOWN)
        except:
            return None


    def __str__(self) -> str:
        return f'{self.client} {self.car}'

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


class CallApplication(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=16, verbose_name='Номер телефона')
    msg = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
