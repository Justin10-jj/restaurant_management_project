from django.shortcuts import render
from.models import RestaurantLocation

def Homes(request):
    info=RestaurantLocation.objects.all()
    phone=info.phone_number if info else "phone number unavailabile"
    return render(request,'homepage.html',{'restaurant_phone':phone})