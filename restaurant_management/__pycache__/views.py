from django.shortcuts import render

def serachpage(request):
    query=request.GET.get('search','')
    if query:
        menu_item=MenuItem.objects.filter(name_iconation=query)
    else:
        menu_item=MenuItem.objects.all()

        location=MenuItem.objects.first()
        context={
            'restaurant_name':settings.RESTAURANT_NAME,
            'location':location,
            'menu_item':menu_item,
            'query':query,
        }
        return render(request,'menulist.html',context)