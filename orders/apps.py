from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        from.models import OrderStatus
        from.import ORDER_STATUES
        try:
            for status in ORDER_STATUES:
                OrderStatus.objects.get_or_create(name=status)
        except OperationalError:
            pass