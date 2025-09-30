from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digit=8,decimal_place=2)
    is_daily_special=models.BooleanField(default=False)
    