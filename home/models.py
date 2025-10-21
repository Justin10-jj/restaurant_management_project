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


class Restaurant( odels.Model):
    name=models.CharField(max_length=255)
    address=models.TextField()
    phone_number=models.CharField(max_length=15)
    opening_hours=models.CharField(max_length=255)
    email=models.EmailField(blank=True,null=True)
    website=models.URLField(blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(blank=True,null=True)



    
    
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="menu_images/",blank=True,null=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    discount_percentage=models.DecimalField(
        max_digits=5,decimal_places=2,default=0.0,
        help_text="Discount percentage(eg,10 for 10%"
    )

    def get_final_price(self)->float:
        if self.discount_percentage>0:
            discount_amount=(self.price*self.discount_percentage)/100
            final_price=self.price-discount_amount
        else:
            final_price=self.price 
        return float(final_price) 


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=modles.CASCADE)
    rating=models.PositiveIntegerField()
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    restaurant=models.Foreginkey(Restaurant,on_delete=models.CASCADE)


