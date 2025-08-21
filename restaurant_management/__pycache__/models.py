class Profile(model.Models):
    full_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    ph_number=modles.IntegerField(max_length=30)
   
class Feedbacks(models.Model):
    comment=models.TextField()
    submitted_at=models.DataTimeField(auto_now=True)


class ContactSubmittion(models.Model):
    name=modles.CharField(max_length=100)
    email=models.EmailField()
    submitted_at=models.DataTimeField(auto_now_add=True)
