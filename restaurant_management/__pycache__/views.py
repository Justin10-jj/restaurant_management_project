from django.shortcuts imoprt render
from.models import Restaurant

def cart(request):
    restaurant=MenuList.objects.all()
    cart_item_count=0
    if request.user.is_authentication:
        cart=created=cart.objects.get_or_create(user=request.user)
        cart_item_count=cart.total_item()

    return render(request,'homepage.html',
    {'restaurant':restaurant,
    'cart_item_count':cart_item_count})