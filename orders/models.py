from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amound=models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    status=models.CharField(max_length=10,default=0)
    created_at=models.DateTimeFeild(auto_now_add=True)


class coupon(models.Model):
    code=models.CharField(max_length=20,unique=True)
    discount=models.DecimalField(max_length=5,decimal_places=2,default=0.00)
    active=models.BooleanField(default=True)


class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(staus__in=['pending','processing'])




class Order(models.Model):
    STATUS_CHOICE=[('pending','pending'),('processing','processing'),('completing','completeing'),('cancelled','cancelled')]

    customer_name=models.CharField(max_length=100)
    status=model.CharField(max_length=20,choice=STATUS_CHOICE,default='pending')
    created_at=models.DateTimeFeild(auto_now_add=True)
    short_id=models.CharField(max_length=10,unique=True)
    total_amound=models.DecimalField(max_digits=20,choice=STATUS_CHOICE,default='pending')

    objects=ActiveOrderManager()

    