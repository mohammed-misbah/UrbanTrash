from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer,UserCreateSerializer
from rest_framework import status
from .models import User
import jwt , datetime
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import APIException
from .permissions import IsTokenVerified
from .serializers import UserSerializer
from jwt import DecodeError, ExpiredSignatureError
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.

    
class RegisterView(APIView):
    @extend_schema(responses=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return Response({'status': 'Please provide the mentioned details'})
        user = User.objects.filter(email=email).first()
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                return Response({'status': 'Password is incorrect'})
            print(user.is_admin,'User is')
            if user.is_admin==False:
                return Response({'status': 'User not admin'})

            if user is not None:
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
                    'iat': datetime.datetime.utcnow(),
                    'name': user.name
                }
                userdetails = {
                    'name': user.name,
                    'email': user.email,
                }

                token = jwt.encode(payload, 'secret', algorithm='HS256')
                return Response({'status': "Success", 'payload': payload, 'admin_jwt': token, 'admin': userdetails},status=status.HTTP_200_OK)
        except:
            if User.DoesNotExist:
                return Response("Email or Password is Wrong")
        
      
        
@api_view(['GET'])
@extend_schema(responses=UserSerializer)
def verify_token(request):
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        else:
            return Response({'status': 'Token Missing or Invalid'}, status=status.HTTP_400_BAD_REQUEST)

        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        id = decoded.get('id')
        user = User.objects.get(id=id)

        if user:
            userdetails = {
                'id': user.id,
                'name': user.name,
                'email': user.email,

            }

            return Response({'admin': userdetails})
        else:
            return Response({'status': 'Token Invalid'})
    except APIException as e:
        return Response(
            {
                'verify_errors': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    

class UserListView(APIView):
    # permission_classes = [IsTokenVerified]
    @extend_schema(responses=UserSerializer)
    def get(self, request):
        user = User.objects.all()
        serializer = UserCreateSerializer(user, many = True)
        return Response(serializer.data)


@api_view(['PATCH'])
def block_user(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return Response({'status': 'blocked'})


@api_view(['PATCH'])
def unblock_user(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return Response({'status': 'blocked'})
        






# class UserApi(APIView):

#     @extend_schema(responses=UserSerializer)
#     def get(request,id):
#         user = User.objects.all()
#         serializer = UserSerializer(user,many=True)
#         return Response(serializer.data)



#     def patch(request,id):
#         user = User.objects.get(id=id)
#         user.full_name = request.data["username"]
#         user.email = request.data["email"]
#         user.save()
#         return Response("User Updated")


#     def delete(request,id):
#         user = User.objects.get(id=id)
#         user.delete()
#         return Response("User deleted")


# class UserView(APIView):
#     JWT_SECRET = 'secret'
#     JWT_ALGORITHM = 'HS256'
#     @extend_schema(responses=UserSerializer)
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, self.JWT_SECRET, algorithms=[self.JWT_ALGORITHM])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

