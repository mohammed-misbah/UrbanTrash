from django.shortcuts import render
from .serializers import ScrapPickupSerializer, ScrapOrderDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ScrapPickupDetail, ScrapPickup
# from rest_framework.decorators import api_view
from rest_framework import status
# from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException
from Account.models import User

# Create your views here.

# ================ Waste booking==================#

class ScrapBookings(APIView):
    def post(self, request):
        try:
            serializer = ScrapPickupSerializer(data=request.data)
            print('///////\\\\\\\\////////////\\\\\\\\\\\\>>>>>>>>>>><<<<<<<<<<>>>>>>>',request.data)
            if serializer.is_valid():
                print('<><><><><><><><><><><><><><><><><><><><><')
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print('===============<<<<<<<<<<<<<<<<>>>>>>>>>>>>>==================',request.data)
                errors = serializer.errors
                print(' <><><><><><><><><><><><><><><><><><><><><',request.data)
                if 'address' in errors and isinstance(errors['address'], list) and errors['address']:
                    if 'pk' in errors['address'][0]:
                        errors['address'] = ['Invalid address ID']
                        print('the values are atempt but cant ====================>>>>>>>>>>>>>>>>>>>>>>>')
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response(
                {'Waste_except': str(e)},
                  status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'Other_exception':
                  str(e)}, status=status.HTTP_400_BAD_REQUEST)



# ================= ScrapPickup Updates =====================#

class ScrapPickupUpdatesAPI(APIView):
    def get(self, request, id):
        scrap_pickup = ScrapPickup.objects.get(id = id)
        serializer = ScrapOrderDetailSerializer(scrap_pickup)
        return Response(serializer.data)
    
    def post(self, request, id):
        try:
            scrap_pickup = ScrapPickup.objects.get(id=  id)

            scrap_pickup.price = request.data["price"]
            print("scraaaaap price",scrap_pickup.price)
            scrap_pickup.scrap_weight = request.data["scrap_weight"]
            print("scraaap weight",scrap_pickup.scrap_weight)
            scrap_pickup.pickup_status = request.data["pickup_status"]
            print("scraaaaaap status",scrap_pickup.pickup_status)

            if 1 < 9:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        except (ScrapPickup.DoesNotExist, KeyError) as e:
            return Response({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        scrap_pickup = ScrapPickup.objects.get(id=id)
        if scrap_pickup:
            scrap_pickup.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

# =================Scrap Pickuplist on UI Side ====================#


class ScrapPickupList(APIView):
    def get(self, request, id):
        user = User.objects.get(id = id)
        scrap_pickups = ScrapPickup.objects.filter(customer = user)
        serializer = ScrapPickupSerializer(scrap_pickups,many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ScrapPickupSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(customer = request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

# =================Scrap Pickuplist on Admin Side ====================#

class AdminPickuplistAPIView(APIView):
    def get(self, request):
        pickups = ScrapPickup.objects.all()
        serializer = ScrapPickupSerializer(pickups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScrapPickupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













# ===================Order details =========================#


# class ScrapOrderDetailView(APIView):
#     def get(self, request):
#         scrap_items = ScrapPickupDetail.objects.all()
#         serializer = ScrapOrderDetailSerializer(scrap_items, many = True)
#         return Response(serializer.data)
    

#     def post(self, request):
#         try:
#             serializer = ScrapOrderDetailListSerializer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except APIException as e:
#             return Response({'status': 'error', 'message': str(e)},
#                                 status=status.HTTP_400_BAD_REQUEST
#                         )



# class ScrapOrderDetailListAPI(APIView):
#     def post(self, request,id):
#         try:
#             user = User.objects.get(id=id)
#             print("uuuuuuuuuuser enteeeeeeeeeered",user)
#             orders = ScrapPickupDetail.objects.filter(customer= user)
#             print("ooooooooooooooorder deeeeeeeeeeetails",orders, user)
#             serializer = ScrapOrderDetailSerializer(orders, many=True)
#             print("seeeeeeeeeeerilizer dataaaaaaaaaaaaaas",serializer)
#             return Response(serializer.data)
#         except APIException as e:
#             return Response({'Orderdetailist': str(e)},
#                                 status=status.HTTP_400_BAD_REQUEST
#                         )