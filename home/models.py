from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .models import MenuItem 

# Create your models here.
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digit=8,decimal_place=2)
    is_daily_special=models.BooleanField(default=False)
    is_availabile=models.BooleanField(default=True)
    

class Table(models.Model):
    table_number=modles.PositiveIntegerField(unique=True)
    capacity=models.PositiveIntegerField()
    is_availabile=models.BooleanField(default=True)


class MenuCategoery(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True,null=True)

class UserReview(models.Model):
    User-models.Foreginkey(User,on_delete=models.CASCADE,relared_name'reviews)
    menu_item=models.Foreginkey('home.MenuItem',on_delete=models.CASCADE,related_name='review')
    rating=models.Integerfield()
    comment=models.TextField()
    review_date=models.DateTimeField(auto_now_add=True)



    
    