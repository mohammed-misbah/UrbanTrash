from django.db import models
from Account.models import User
from ScrapCategory.models import ScrapCategory
from Address.models import Address
import datetime

# Create your models here.

current_date = datetime.date.today()

class ScrapPickup(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    scrapwaste = models.ForeignKey(ScrapCategory,on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    scrap_weight = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    pickup_status = models.CharField(max_length=20, default='pending')
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    notes = models.TextField()
    pickup_day = models.IntegerField(default=current_date.day)
    pickup_month = models.IntegerField(default=current_date.month)
    pickup_year = models.IntegerField(default=current_date.year)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"ScrapPickup #{self.pk} - {self.customer.name}"
    

class ScrapPickupDetail(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None)
    scrapwaste = models.ForeignKey(ScrapCategory,on_delete=models.CASCADE)
    scrap_weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pickup_date = models.DateField(default=None)
    pickup_time = models.TimeField(default=None)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    scrappickup = models.ForeignKey(ScrapPickup, on_delete=models.CASCADE)

    def __str__(self):
        return f"ScrapPickup Detail #{self.pk} - Pickup #{self.scrappickup.pk}"
