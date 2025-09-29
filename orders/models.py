from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amound=models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    status=models.CharField(max_length=10,default=0)
    created_at=models.DateTimeFeild(auto_now_add=True)
    customer_name=models.CharField(max_length=255)


    def calculated_total(models.Model):
        total=Decimal("0.00")
        for item in self.item.all():
            total +=item.price * item.quantity
        return total 


class coupon(models.Model):
    code=models.CharField(max_length=20,unique=True)
    discount=models.DecimalField(max_length=5,decimal_places=2,default=0.00)
    active=models.BooleanField(default=True)


class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(staus__in=['pending','processing'])




class Oredr(models.Model):
    STATUS_CHOICE=[('pending','pending'),('processing','processing'),('completing','completeing'),('cancelled','cancelled')]

    customer_name=models.CharField(max_length=100)
    status=model.CharField(max_length=20,choice=STATUS_CHOICE,default='pending')
    created_at=models.DateTimeFeild(auto_now_add=True)

    objects=ActiveOrderManager()

class MenuItem(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)


class OredrItem(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE,related_name="item")
    menu_item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=8,decimal_places=2)