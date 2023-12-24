from rest_framework.serializers import ModelSerializer
from .models import Notification
from rest_framework import serializers
from Account.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.is_admin = True
        instance.save()
        return instance

    

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','is_active']


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    class Meta:
        model = Notification
        fields = '__all__'
