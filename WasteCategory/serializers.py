from rest_framework import serializers
from .models import WasteCategory,BioWaste
# from django import forms


class WasteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteCategory
        fields = '__all__'




class BioWasteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=WasteCategory.objects.all(), allow_null = True)

    class Meta:
        model = BioWaste
        fields = '__all__'

