from django.contrib import admin
from django.utils import timezone
from django.template.response import TemplateResponse
from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from carwash import models as m
from carwash.utils import get_order_total_sum


@admin.register(m.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(m.Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'car_class', 'price')
    list_filter = ('service', 'car_class')


@admin.register(m.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'car', 'is_payed', 'status', 'created_at', 'payed_at', 'price')
    list_editable = ('is_payed', 'status')
    list_filter = (('created_at', DateRangeFilter), 'status', 'is_payed', 'price')
    search_fields = ('client__username', 'car__state_number')
    actions = ('generate_report', )

    def get_rangefilter_created_at_default(self, request):
        return (timezone.now().today(), timezone.now().today())

    def get_rangefilter_created_at_title(self, request, field_path):
        return 'Дата оформления'

    @admin.action(description='Сформировать отчет')
    def generate_report(self, request, queryset):
        context = {
            'orders': queryset,
            'total_sum': get_order_total_sum(queryset),
            'today': timezone.now()
        }
        return TemplateResponse(request, 'carwash/order_report.html', context)

@admin.register(m.CallApplication)
class CallApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'phone_number')