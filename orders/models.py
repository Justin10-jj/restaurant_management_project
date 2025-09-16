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