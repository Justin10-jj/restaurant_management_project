def homepage(request):
    restaurant=Restaurant.objects.first()
    context={
        'restaurant_name':restaurant_name if restaurant else"unmaned restaturant
    }
    return render(request,homepage.html,context)