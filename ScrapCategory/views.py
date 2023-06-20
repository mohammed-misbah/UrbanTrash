from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ScrapWasteSerializer, ScrapCategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from .models import ScrapCategory, ScrapWaste
from rest_framework import generics


# Create your views here.

# =================== Scrap Category =========================#


class ScrapCategoryAPIView(APIView):

    serializer_class = ScrapCategorySerializer

    def get(self, request):
        try:
            waste_category = ScrapCategory.objects.all()
            serializer = self.serializer_class(waste_category, many=True)
            print("they are printing a scrapcategory but cant get this-----==========",serializer)
            return Response(serializer.data)
        except ScrapCategory.DoesNotExist:
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
        except ScrapCategory.DoesNotExist:
            return Response(
                {'detail': 'Not found.'},
                status=status.HTTP_404_NOT_FOUND
            )


# =========================== Scrap Category Edit ===========================#

class ScrapCategoryEditAPIVIEW(APIView):
    serializer_class = ScrapCategorySerializer
    def get_object(self, id):
        try:
            return ScrapCategory.objects.get(id = id)
        except ScrapCategory.DoesNotExist:
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
    

# ============================= Scrap Category LIst ============================#

class ScrapCategoryListAPIView(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                scrap_category = ScrapCategory.objects.get(id=id)
                serializer = ScrapCategorySerializer(scrap_category)
                return Response(serializer.data)
            except ScrapCategory.DoesNotExist:
                return Response({'error': 'Wast category not found'},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            scrap_categories = ScrapCategory.objects.all()
            serializer = ScrapCategorySerializer(scrap_categories, many= True)
            return Response(serializer.data)
        
# ========================== Scrap Waste =============================#

class ScrapWastes(APIView):
    serializer_class = ScrapWasteSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            print("/././././././././././././././././",request.data)
            if serializer.is_valid():
                    print("/././././././././.scrap Entered here but not saving >>>>>>")
                    serializer.save()
                    print("The problem is ==>>>")
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except APIException as e:
            return Response(
                {'Scrap_except': str(e)},
                  status=status.HTTP_400_BAD_REQUEST)
        

# ===================== Scrap Waste List =========================#


class ScrapWasteListAPIView(APIView):
    def get(self, request):
        try:
            scrap_waste = ScrapWaste.objects.all()
            serializer = ScrapWasteSerializer(scrap_waste, many = True)
            return Response(serializer.data)
        except ScrapWaste.DoesNotExist:
            return Response({'error': 'Scrap waste is not found'},
                            status=status.HTTP_404_NOT_FOUND)
        
# ======================== Scrap Waste Edit ======================#


class ScrapWasteEditAPIView(APIView):
    serializer_class = ScrapWasteSerializer

    def get_object(self, id):
        try:
            return ScrapWaste.objects.get(id= id)
        except ScrapWaste.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, id):
        scrap_waste = self.get_object(id)
        serializer = self.serializer_class(scrap_waste)
        return Response(serializer.data)
    
    def post(self, request, id):
        scrap_waste = self.get_object(id)
        serializer = self.serializer_class(scrap_waste, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        scrap_waste = self.get_object(id)
        scrap_waste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
