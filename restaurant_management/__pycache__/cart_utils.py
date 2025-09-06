from django.conf import settings
from.models import MenuItem
CART_SESSION_ID=getattr(setting,"CART_SESSION_ID","cart")
class cart:
    def __init__(self,request):
        self.session=request.session
        self.cart=self.session.get(CART_SESSION_ID,{})

    def add(self,item_id,name,price,qty=1):
        if str(item_id) in self.cart:
            self.cart[str(item_id)]["qty"]+=qty
        else:
            self.cart[str(item_id)]={
                "name":name,"price":price,"qty":qty
            }
            self.save()
    def remove(self,item_id):
        self.cart.pop(str(item_id),None)
        self.save()

    def clear(self):
        self.session[CART_SESSION_ID]={}
        slef.session.modified=True

    def save(self):
        self.session[CART_SESSION_ID]self.cart
        self.session.modified=True

    def items(self):
        return self.cart.values()
    def total_price(self):
        return sum(item["price"]*item["qty"] for item in self.items())
