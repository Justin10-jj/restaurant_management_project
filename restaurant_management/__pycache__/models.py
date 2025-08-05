class Profile(model.Models):
    full_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    ph_number=modles.IntegerField(max_length=30)
    