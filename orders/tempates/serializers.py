from rest_framework import serializers
from.models import Oredr,OrderItem

class OrderItemSerializer(serializer.ModelSerializer):
    class Meta:
        model=OrderItem
        field=["product_name","quantity","price"]

class OrderItemSerializer(serializer.ModelSerializer):
    item=OrderItemSerializer(many=True,read_only=True)

    class Meta:
        model=Oredrfield=["id","created_at","total_amound","status","item"]