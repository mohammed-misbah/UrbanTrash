from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import datetime

# Create your models here.

current_date = datetime.date.today()


class AdminUser(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255, unique=True)
    password = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    signup_day = models.CharField(max_length=50, default=current_date.day)
    signup_month = models.CharField(max_length=50, default=current_date.month)
    signup_year = models.CharField(max_length=50, default=current_date.year)
    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.name

    
     