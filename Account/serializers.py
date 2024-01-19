from rest_framework.serializers import ModelSerializer
from .models import User
import jwt, datetime
from rest_framework import exceptions
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
    

class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3000),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')

def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_secret', algorithm='HS256')    

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
    
