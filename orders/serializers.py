from rest_framework import serializers
from .models import Order
from home.models import MenuItem

class MenuItemSerializer(serializer.ModelSerializer):
    class Meta:
        model=MenuItemfield=["id","name","price"]


class OrderSerializer(serializers.ModelSerializer):
    customer=serializers.StringRelatedField()
    items=MenuItemSerializer(many=True)

    class Meta:
        model=Order
        filed=["id","customer","item","total_price","created_at"]



class OrderStatusUpdateSerializer(serializers.serializer):
    order_id=serializers.IntegerField()
    new_status=serializers.ChoiceField(choice=order.STATUS_CHOICES)