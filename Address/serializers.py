from rest_framework import serializers
from .models import Address,UserProfile
from Account.models import User
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.serializers import ModelSerializer
from Account.serializers import UserSerializer



class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Address
        fields = '__all__'

class AddressPostSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'



# ==========================


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['email', 'profile_picture','phone_number']

   
# ==========================










