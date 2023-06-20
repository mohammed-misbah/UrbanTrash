from rest_framework import serializers
from .models import ScrapWaste,ScrapCategory



class ScrapCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapCategory
        fields = '__all__'



class ScrapWasteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=ScrapCategory.objects.all(), allow_null=True)

    class Meta:
        model = ScrapWaste
        fields = '__all__'