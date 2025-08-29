def homepage(request):
    restaurant=RestaurantLocation.objects.all()
    return render(request,'homepage.html',{'restaurant':restaurant})