from rest_framework import serializers
from .models import MenuList

class MenuListSerializer(serializers.ModelSerializer):
    category=serializers.CharField(source="category.name")

    class Meta:
        modle=MenuList
        field=["id","name","description","price","availability","image","category"]