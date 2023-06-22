from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from Account.models import User
import datetime

# Create your models here.

current_date = datetime.date.today()


class Notification(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    room_name = models.CharField(max_length=50,null=False, default="user")
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True, verbose_name='Read At')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created At')
    notification_day = models.CharField(max_length=50, default=current_date.day)
    notification_month = models.CharField(max_length=50, default=current_date.month)
    notification_year = models.CharField(max_length=50, default=current_date.year)

    def __str__(self) -> str:
        return self.user
    

    
     