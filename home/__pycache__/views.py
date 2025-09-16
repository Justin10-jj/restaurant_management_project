from rest_framework.generics import ListAPIView
from .models import MenuCatagory
from.serializer import MenuCatagorySerializer

class MenuCatagoryListenView(ListAPIView):
    queryset=MenuCatagory.objects.all()
    serializer_class=MenuCatagorySerializer

