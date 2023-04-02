from django.contrib import admin
from organization import models as m


@admin.register(m.TireSize)
class TireSize(admin.ModelAdmin):
    list_display = [field.name for field in m.TireSize._meta.fields]

    class Meta:
        model = m.TireSize


@admin.register(m.OrderStorage)
class OrderStorage(admin.ModelAdmin):
    list_display = [field.name for field in m.OrderStorage._meta.fields]

    class Meta:
        model = m.OrderStorage


@admin.register(m.PeriodOfStorage)
class PeriodOfStorage(admin.ModelAdmin):
    list_display = [field.name for field in m.PeriodOfStorage._meta.fields]

    class Meta:
        model = m.PeriodOfStorage


@admin.register(m.QuantityOfTires)
class QuantityOfTires(admin.ModelAdmin):
    list_display = [field.name for field in m.QuantityOfTires._meta.fields]

    class Meta:
        model = m.QuantityOfTires


