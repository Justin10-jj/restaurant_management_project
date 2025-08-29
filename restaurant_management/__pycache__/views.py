def Contact_view(request):
    if request.method=='POST':
        if form.is_valid():
            email=form.cleaned_data['email']
            message=form.cleaned_data{'message'}

            return render(request,'restaurantcontact.html',{'forms':form})


def homepagephone(request):
    restaurant=Restaurant.objects.all()
    return render(request,'homepage.html',{'restaurant':restaurant})