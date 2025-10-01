from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    STATUS_CHOICE=[
        ("PENDING","pending"),
        ("PROCESSING","processing"),
        ("CANCELLED","cancelled"),
        ("COMPLETED","completed"),
        ("DELIVERED","delivered"),
    ]
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amound=models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    status=models.CharField(max_length=10,default="pending",choice=STATUS_CHOICE)
    created_at=models.DateTimeFeild(auto_now_add=True)
    customer_name=models.CharField(max_length=255)


    def calculated_total(self):
        total=Decimal("0.00")
        for item in self.item.all():
            total +=item.price * item.quantity
            if hasattr(item,"discount_percent")and item.discount_percent:
                line_total=calculate_discount(line_total,item.discount_percent)
            total+=line_total
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
    discount_percent=models.DecimalField(max_length=5,decimal_places=2,null=True)



class OrderManager(models.Manager):
    def with_status(self,status):
        return self.filter(status=status)
    def pending(self):
        return self.with_status('pending')
    def completed(self):
        return self.with_status('completed')
    def cancelled(self):
        return self.with_status('cancelled')

class Order(models.Model):
    STATUS_CHOICE=[
        ('pending','pending'),
        ('completed','completed'),
        ('cancelled','cancelled'),
    ]
    customer=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=STATUS_CHOICE,default='pending')
    created_at=models.DateTimeFeild(auto_now_add=True)
    objects=OrderManager()