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
    class Meta:
        model=Order
        field=["status"]
    def validate_status(self,value):
        allowed_statuses=[choice[0]for choice in Order.STATUS.CHOICES]

        if value not in allowed_statuses:
            raise serializer.validationError(f"Invalid status.Allowed:{allowed_statuses}) 
        return value    



class CouponSerializer(serializer.ModelSerializer):
    class Meta:
        model=coupon 
        field = ["code","discount_percentage"]