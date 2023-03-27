from django.contrib import admin
from cars import models as m


@admin.register(m.CarBodywork, m.CarBrand, m.CarCoverage,
                m.CarModel, m.CarSalon, m.CarClass)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(m.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'car_class', 'bodywork', 'salon', 'coverage', 'owner', 'state_number')
    list_filter = ('brand', 'model', 'car_class', 'bodywork', 'salon', 'coverage', )
    search_fields = ('state_number', 'owner__first_name', 'owner__last_name', 
        'owner__middle_name', 'owner__phone_number', 'owner__username', 'owner__email')