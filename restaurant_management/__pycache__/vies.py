from django.shortcuts import render
def menu_list(request):
    menu_list=[{
        'name':'cheeseburger','description':'grilled beef patty with cheese,lectture,and tomato',
        'price':10.99,
        'is_avalibile':True
    },
    {
        'name':'grilled chicken sandwitch',
        'description':'chicken breast sandwich with mayo pickles',
        'price':9.49,
        'is_availbile':False
            },]

    return render(request,'menu/menu_list.html',{'menu_items':menu_items})



def homepage(request):
    return render(request,'homepage.html',{'restaurant_name':settings.RESTAURANT_NAME})