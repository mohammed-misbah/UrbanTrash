from rest_framework.serializers import ModelSerializer
from .models import AdminUser
from rest_framework import serializers


class UserSerializers(ModelSerializer):
    is_admin = serializers.BooleanField(default=True, write_only=True)

    class Meta:
        model = AdminUser
        fields = ['id', 'name', 'email', 'password', 'is_admin']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        is_admin = validated_data.pop('is_admin', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if is_admin is not None:
            instance.is_admin = is_admin
        instance.save()
        return instance

    

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ['id','name','email','is_active']