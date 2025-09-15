class Profile(model.Models):
    full_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    ph_number=modles.IntegerField(max_length=30)
   
class Feedbacks(models.Model):
    comment=models.TextField()
    submitted_at=models.DataTimeField(auto_now=True)


class ContactSubmission(models.Model):
    name=modles.CharField(max_length=100)
    email=models.EmailField()
    submitted_at=models.DataTimeField(auto_now_add=True)

class MenuList(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DeciamlField(max_digit=6,decimal_places=2)
    image=models.ImageField(upload_to='menu_images/',blank=True,null=True)
    availability=models.BooleanField(default=True)


    # python manage.py makemigrations
    # python manage.py migrate


class RestaurantLocation(models.Model):
    address=models.CharField(max_length=225)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=60)
    opening_hour=models.JSONField(default=DEFAULT_OPENING_HOURS)
    phone_number=models.IntegerField(max_length=30)
    history=models.TextField(null=True,blank=True)
    mission=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='restaurant/',blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    
DEFAULT_OPENING_HOURS={
    "monday":"9:00 am - 5:00 pm",
    "tue":"9:00 am - 5:00 pm",
    "wed":"9:00am - 5:00pn",
    "thur":"9:00 am - 5:00pm",
    "fri":"closed",
    "sat":"closed",
    "sun":"closed",
}

class Carts(models,Model):
    user=models.OneToOneField(user,on_delete=models.CASCADE,related_name='cart')
    def total_items(self):
        return sum(item.quantity for item in self.item.all())
    class cartItem(models.Model):
        cart-models.ForeignKey(cart,related_name='items',on_delete=models.CASCADE)
        product=models.ForeignKey(product,on_delete=models.CASCADE)
        quantity=models.PositiveIntegerField(default=1)


class Feedbackss(models.Model):
    name=model.CharField(max_length=100)
    message=models.TextField()
    submitted_at=models.DataTimeField(auto_now_add=True)


class Special(models.Model):
    name=models.CharField(max_length=100)
    description=model.TextField()
    price=models.DeciamlField(max_digit=6,decimal_places=2)


class Chef(models.Model):
    name=modles.CharField(max_length=100)
    bi0=modles.TextField()
    image=models.ImageField(upload_to='chef_image/',blank=True,null=True)



class OrderStaus(models.Model):
    name=models.CharField(max_length=50)



class Order(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    item=models.ManyTManyField(MenuList,through="OrderItem")
    status=models.ForeignKey(OrderStaus,on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(MenuList,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


class MenuCategory(models.Model):
    name=models.CharField(max_length=100,unique=True)