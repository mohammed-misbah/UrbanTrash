from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import AddressSerializer,UserProfileSerializer,AddressPostSerializer
from rest_framework import generics
from .models import UserProfile
from Account.models import User
from django.http import Http404
# from drf_spectacular.utils import extend_schema 
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from .models import Address
# from django.contrib.auth import get_user_model
from django.utils.functional import SimpleLazyObject
from rest_framework.exceptions import APIException
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

# =================== Add address =================#


class AddressListAPIView(APIView):

    def get(self, request,id):
        try:
            userId = id 
            address = Address.objects.filter(user=userId)
            serializer = AddressSerializer(address, many=True)
            return Response(serializer.data)
        except APIException as e:
            return Response(
                {'Addres_error': str(e)},
                    status=status.HTTP_400_BAD_REQUEST)

class AddressPostAPIView(APIView):
        def post(self, request):
            try:
                serializer = AddressPostSerializer(data=request.data)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except APIException as e:
                return Response(
                    {'Address_errors': str(e)},
                        status=status.HTTP_400_BAD_REQUEST)

#=============== User Profile =====================# 


class UserProfileAPIView(APIView):
    serializer_class = UserProfileSerializer

    def get(self, id):
        name = User.objects.get(id=id) 
        serializer = self.serializer_class(name, many=False) 
        return Response(serializer.data)

        
    def post(self, request, id):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response({'profile': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        



        

