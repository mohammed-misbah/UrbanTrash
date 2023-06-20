from django.db import models

# Create your models here.

class ScrapCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='waste_category', blank=True)
    recyclable = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ScrapWaste(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ScrapCategory, on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='scrapwaste_images')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    



# class OrderListAPIView(APIView):
#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

