from django.contrib.auth.models import AbstractBaseUser
from django.db import models
import datetime

current_date = datetime.date.today()

class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255,unique=True)
    phone = models.CharField(max_length=12,blank=False)
    password = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    signup_day = models.CharField(max_length=50, default=current_date.day)
    signup_month = models.CharField(max_length=50, default=current_date.month)
    signup_year = models.CharField(max_length=50, default=current_date.year)
    is_blocked = models.BooleanField(default=False)
    fromGoogle=models.BooleanField(default=False)
    is_anonymous = False
    first_name = None
    last_name =None
    username= None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.name
