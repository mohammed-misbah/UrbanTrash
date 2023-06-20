from django.shortcuts import render
from rest_framework import generics
from .models import WasteCategory,BioWaste
from .serializers import WasteCategorySerializer, BioWasteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.exceptions import NotFound,ValidationError
# from drf_spectacular.utils import extend_schema
from rest_framework import generics
# Create your views here.

# ================ Waste Category ======================#



class WasteCategoryAPIVIEW(APIView):
    
    serializer_class = WasteCategorySerializer

    def get(self, request):
        try:
            waste_category = WasteCategory.objects.all()
            serializer = self.serializer_class(waste_category, many=True)
            print("they are printing a wastecategory but cant get this-----==========",serializer)
            return Response(serializer.data)
        except WasteCategory.DoesNotExist:
            return Response(
                {'detail': 'Not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            print("printing a waste category data field==========",request.data)
            if serializer.is_valid():
                serializer.save()
                print("////////////////",request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WasteCategory.DoesNotExist:
            return Response(
                {'detail': 'Not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
# ======================== Waste Category Edit ========================#


class WasteCategoryEditAPIVIEW(APIView):

    serializer_class = WasteCategorySerializer
    
    def get_object(self, id):
        try:
            return WasteCategory.objects.get(id = id)
        except WasteCategory.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, id):
        waste_category = self.get_object(id)
        serializer = self.serializer_class(waste_category)
        return Response(serializer.data)
    
    def patch(self, request, id):
        waste_category = self.get_object(id)
        serializer = self.serializer_class(waste_category, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        waste_category = self.get_object(id)
        waste_category.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    

# =========================== Waste Category List =====================#


class WasteCategoryListAPIView(APIView):
    def get(self, request, id=None):  
        if id is not None:
            try:
                waste_category = WasteCategory.objects.get(id=id)
                serializer = WasteCategorySerializer(waste_category)
                return Response(serializer.data)
            except WasteCategory.DoesNotExist:
                return Response(
                    {'detail': 'Waste category not found.'},
                        status=status.HTTP_404_NOT_FOUND)
        else:
            waste_categories = WasteCategory.objects.all()
            serializer = WasteCategorySerializer(waste_categories, many=True)
            return Response(serializer.data)

# ========================= Bio Waste ==========================#


class BioWastes(APIView):
    serializer_class = BioWasteSerializer       

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            print("printing a biowaste fields=    = = = == = == = = == = =",request.data)
            if serializer.is_valid():
                
                serializer.save()
                print("///////////////////////////./././/////",serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print("serializer errror ", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except APIException as e:
            return Response(
                {'Biowaste_except': str(e)},
                 status=status.HTTP_400_BAD_REQUEST)
        

# ================ Bio Waste List ====================#

class BioWasteListAPIView(APIView):
    def get(self, request):
        try:
            bio_waste = BioWaste.objects.all()
            serializer = BioWasteSerializer(bio_waste, many = True)
            return Response(serializer.data)
        except BioWaste.DoesNotExist:
            return Response({'error': 'Bio waste is not found'}, 
                    status=status.HTTP_404_NOT_FOUND)


# ================================ Bio Waste Edit=========================== #


class BioWasteEditAPIVIEW(APIView):

    serializer_class = BioWasteSerializer

    def get_object(self, id):
        try:
            return BioWaste.objects.get(id = id)
        except BioWaste.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, id):
        bio_waste = self.get_object(id)
        serializer = self.serializer_class(bio_waste)
        return Response(serializer.data)
    
    def patch(self, request, id):
        bio_waste = self.get_object(id)
        serializer = self.serializer_class(bio_waste, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        bio_waste = self.get_object(id)
        bio_waste.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    



