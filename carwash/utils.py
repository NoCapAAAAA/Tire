from carwash import models as m


def get_order_total_sum(order_queryset):
    orders = order_queryset
    sum = 0
    for order in orders:
        if order.is_payed or order.status == m.OrderStatus.CANCELED: continue
        sum += order.price.price
    return sum