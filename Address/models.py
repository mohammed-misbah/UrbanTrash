from django.db import models
# from django.contrib.auth.models import User
from Account.models import User

# Create your models here.

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    email = models.EmailField(max_length=100, default='')
    phone_number = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.user.name
    

    

