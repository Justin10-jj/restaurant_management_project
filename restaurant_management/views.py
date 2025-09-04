from django.shortcuts import render
from.models import RestaurantLocation

def Homes(request):
    info=RestaurantLocation.objects.all()
    phone=info.phone_number if info else "phone number unavailabile"
    return render(request,'homepage.html',{'restaurant_phone':phone})

def homeee(request):
    crumbs=[]
    return render(request,'homepage.html',{
        'crumbs':crumbs,
        })

def menu(request):
    crumbs=[{'name':'menu','url':request.path},]
    return render(request,'menulist.html',{'crumbs':crumbs})



def desserts(request):
    crumbs=[
        {'name':'menu','url':'/menu/'},
        {'name':'Desserts'.'url'request.path}
    ]
    return render(request,'desserts.html',{'crumbs':crumbs})