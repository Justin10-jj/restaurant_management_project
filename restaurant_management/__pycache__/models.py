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

    # python manage.py makemigrations
    # python manage.py migrate


class RestaurantLocation(models.Model):
    address=models.CharField(max_length=225)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=60)
    opening_hour=models.JSONField(default=dict)

DEFAULT_OPENING_HOURS={
    "monday":"9:00 am - 5:00 pm",
    "tue":"9:00 am - 5:00 pm",
    "wed":"9:00am - 5:00pn",
    "thur":"9:00 am - 5:00pm",
    "fri":"closed",
    "sat":"closed",
    "sun":"closed",
}