def homepage(request):
    restaurant=Restaurant.objects.first()
    context={
        'restaurant_name':restaurant_name if restaurant else"unmaned restaturant
    }
    return render(request,homepage.html,context)



def home(request):
    restaurant=Restaurant.objects.first()
    phone_number=restaurant.phone if restaturant else 'not availabile'
    return render(request,'home.html',{'phone_number':phone_number})


def restaturant_list(request):
    try:
        restaturant=Restaurant.objects.all()
        return render(request,'home.html',{'restaurant':restaturant})
    except DatabaseError as e:
        print(f"Database error occurred:{e}")
        return HttpResponseServerError("An error ocuured while retrieving restaturants.Please try again later.")