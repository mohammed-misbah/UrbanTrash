from django.shortcuts import render
from .serializers import WastePickupSerializer, OrderDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WastePickupDetail
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException
from Account.models import User
from .models import WastePickup
# Create your views here.

# ================ Waste booking==================#

class WasteBookings(APIView):
    def post(self, request):
        try:
            serializer = WastePickupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                errors = serializer.errors
                if 'address' in errors and isinstance(errors['address'], list) and errors['address']:
                    if 'pk' in errors['address'][0]:
                        errors['address'] = ['Invalid address ID']
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response(
                {'Waste_except': str(e)},
                  status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'Other_exception':
                  str(e)}, status=status.HTTP_400_BAD_REQUEST)



# ===================== WasteOrder Updates ==================#


class   WasteOrderUpdatesAPI(APIView):
    def get(self, request,id):
        pickup = WastePickup.objects.get(id = id)
        serializer = OrderDetailSerializer(pickup)
        return Response(serializer.data)
       
        
    def post(self, request, id):
        try:
            pickup = WastePickup.objects.get(id=id)
        
            pickup.price = request.data['price'] 
            pickup.waste_weight = request.data['waste_weight']
            pickup.status = request.data['status']
            pickup.save()

            if 1 < 9:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        except (WastePickup.DoesNotExist, KeyError) as e:
            return Response({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)
          

    def delete(self, request, id):
        waste_pickup = WastePickup.objects.get(id=id)
        
        if waste_pickup:
            waste_pickup.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

# =================Waste Pickuplist on UI Side ====================#
        
class WastePickupList(APIView):
    def get(self, request, id):
        user = User.objects.get(id=id)
        waste_pickups = WastePickup.objects.filter(customer=user)
        serializer = WastePickupSerializer(waste_pickups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WastePickupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
# =================Waste Pickuplist on Admin Side ====================#    

class PickupListAPIView(APIView):
    def get(self, request):
        orders = WastePickup.objects.all()
        serializer = WastePickupSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WastePickupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
        
    





# ===================Order details =========================#


# class WasteOrderDetailView(APIView):
#     def get(self, request):
#         pickup_items = WastePickupDetail.objects.all()
#         serializer = OrderDetailSerializer(pickup_items, many = True)
#         return Response (serializer.data)
    

#     def post(self, request):
#         try:
#             serializer = OrderDetailListSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except APIException as e:
#             return Response({'Orderdetail': str(e)},
#                             status=status.HTTP_400_BAD_REQUEST
#                             )
        

# class WasteOrderDetailListAPI(APIView):
#     def post(self, request,id):
#         try:
#             user = User.objects.get(id=id)
#             orders = WastePickDetail.objects.filter(customer= user)
#             serializer = OrderDetailSerializer(orders, many=True)
#             return Response(serializer.data)
#         except APIException as e:
#             return Response({'Orderdetailist': str(e)},
#                                 status=status.HTTP_400_BAD_REQUEST
#                         )