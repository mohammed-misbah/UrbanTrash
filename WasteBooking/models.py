from django.db import models
from Account.models import User
from Address.models import Address
from WasteCategory.models import WasteCategory,BioWaste
from ScrapCategory.models import ScrapCategory
import datetime

# Create your models here.

current_date = datetime.date.today()

class WastePickup(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    biowaste = models.ForeignKey(WasteCategory,on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    waste_weight = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    status = models.CharField(max_length=270, default='pending')
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    notes = models.TextField()
    pickup_day = models.IntegerField(default=current_date.day)
    pickup_month = models.IntegerField(default=current_date.month)
    pickup_year = models.IntegerField(default=current_date.year)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"WastePickup #{self.pk} - {self.customer.name}"
    
 

class WastePickupDetail(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    customer = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,default=None)
    biowaste = models.ForeignKey(WasteCategory,on_delete=models.CASCADE)
    waste_weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pickup_date = models.DateField(default=None)
    pickup_time = models.TimeField(default=None)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    wastepickup = models.ForeignKey(WastePickup, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order Detail #{self.pk} - Order #{self.wastepickup.pk}"
    



