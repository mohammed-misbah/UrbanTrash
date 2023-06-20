# from Address.models import Address
from .models import ScrapPickup
from rest_framework import serializers
from .models import ScrapPickupDetail
from ScrapCategory.serializers import ScrapCategorySerializer
from Account.serializers import UserSerializer
from Address.serializers import AddressSerializer


class ScrapPickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapPickup
        fields = '__all__'


# =============================== #


class ScrapOrderDetailSerializer(serializers.ModelSerializer):
    scrapwaste = ScrapCategorySerializer()
    customer = UserSerializer()
    address = AddressSerializer()
    def get_waste_type_name(self, obj):
        return obj.scrapwaste.name
    
    def get_costomer_name(self,obj):
        return obj.customer.name
    
    def get_address(self,obj):
        return obj.address
   
    class Meta:
        model = ScrapPickup
        fields = '__all__'



# class ScrapOrderDetailListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScrapPickupDetail
#         fields = '__all__' 