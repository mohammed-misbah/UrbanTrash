from django.db import models

# Create your models here.

class WasteCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='waste_category', blank=True)
    recyclable = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class BioWaste(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(WasteCategory, on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='biowaste_images')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


        
# class Subcategory(models.Model):
#     subcat_name     = models.CharField(max_length=100,unique=True)
#     subcat_image    = models.ImageField(upload_to='images/',blank=True)
#     subcat_list     = models.CharField(max_length=100,unique=True)
#     category        = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    
#     def __str__(self):
#         return self.subcat_name


#  hazardous = models.BooleanField(default=False)
#  created_at = models.DateTimeField(auto_now_add=True)

