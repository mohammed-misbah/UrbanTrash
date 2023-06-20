# from Address.models import Address
from .models import WastePickup, WastePickupDetail
from rest_framework import serializers
from Account.serializers import UserSerializer
from WasteCategory.serializers import WasteCategorySerializer
from Address.serializers import AddressSerializer



class WastePickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WastePickup
        fields = '__all__'


# =============================== #


class OrderDetailSerializer(serializers.ModelSerializer):
    biowaste = WasteCategorySerializer()
    customer = UserSerializer()
    address = AddressSerializer()
    def get_waste_type_name(self, obj):
        return obj.biowaste.name
    
    def get_costomer_name(self,obj):
        return obj.customer.name
    
    def get_address(self,obj):
        return obj.address
   
    class Meta:
        model = WastePickup
        fields = '__all__'



# class OrderDetailListSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     class Meta:
#         model = WastePickupDetail
#         fields = '__all__' 



