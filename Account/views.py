from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, LoginSerializer
from .models import User
import jwt , datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from django.contrib.auth import authenticate
import base64
import json
import jwt
import cloudinary
from cloudinary.uploader import upload
from drf_spectacular.utils import extend_schema
from jwt import DecodeError, ExpiredSignatureError
# from .otp import send_request,verify_Otp


# Create your views here.


class RegisterView(APIView):
    @extend_schema(
        responses=UserSerializer,
        request=UserSerializer,)
    @extend_schema(responses=UserSerializer)
    def post(self, request):
        try:
            data = request.data
            email = data.get('email')
            if User.objects.filter(email=email).exists():
                # errors = {'email': ['Email already exists.']}
                return Response({"status": "Email already exists"}, status=status.HTTP_409_CONFLICT)

            serializer = UserSerializer(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = serializer.save()
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except APIException as e:
            return Response(
                {
                    'register_errors': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


# ============================= User Login ========================#


class LoginView(APIView):

    @extend_schema(
        responses=LoginSerializer,
        # Assuming the request schema is the same as the response schema
        request=LoginSerializer,
    )
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return Response({'status': 'Please provide the mentioned details'})
        user = User.objects.filter(email=email).first()
        # print(user.password)
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                Response({'status': 'Password is incorrect'})
            if user is not None:
                # user = LoginSerializer(user)
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
                    'iat': datetime.datetime.utcnow(),
                    'name': user.name
                }
                userdetails = {
                    'name': user.name,
                    'email': user.email,
                    'phone': user.phone,
                }

                token = jwt.encode(payload, 'secret', algorithm='HS256')

                return Response({'status': "Success", 'payload': payload, 'user_jwt': token, 'user': userdetails})
        except:
            if User.DoesNotExist:
                return Response("Email or Password is Wrong")

        

# ====================Verifying Token =====================#


@api_view(['GET'])
@extend_schema(responses=UserSerializer)
def verify_token(request):
    try:
        token = request.headers.get('Authorization')
        print(token, "getting a token")
        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        user_id = decoded.get('id')
        user = User.objects.filter(id=user_id).first()
        if user:
            # userdetails = UserSerializer(user,many=False)
            userdetails = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': user.phone,
            }

            return Response({'user': userdetails})
        else:
            return Response({'status': 'Token Invalid'})
    except (DecodeError, ExpiredSignatureError):
        return Response({'status': 'Token Invalid'}, status=status.HTTP_401_UNAUTHORIZED)
    

# ==================== OTP Login =====================# 


class OTPloginAPIView(APIView):
    def post(self, request):
        try:
            phone = request.data['phone']
            if User.objects.filter(phone = phone).exists():
                user = User.objects.get(phone = phone)
                if  user.is_blocked:
                    return Response({'status': 'user is blocked'})
                payload = {
                    'email' : user.email,
                    'name' : user.name,
                    'phone': user.phone,
                    'id' : user.id 
                }
                enpayload = base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')
                jwt_token = jwt.encode({'payload': enpayload}, 'secret', algorithm='HS256')
                response = Response({'status': 'Success', 'payload': enpayload, 'email': user.email,
                                            'name': user.name, 'jwt': jwt_token, 'role': 'user', 'id': user.id})
                return response
            else:
                return Response({'status':'User not found'})
        except Exception as e:
            print("error is >>",str(e))
            return Response({'status':"Error occur while otp generating"})

# ==================== LogOut ==========================#


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

# ================= Google Login ===================#


class GoogleLogin(APIView):
    def post(self, request):
        # data = request.data
        email = request.data['email']

        try:
            if User.objects.filter(email=email).exists():
                user = authenticate(email=email)
                user = User.objects.all()
                status = 'None'
                for i in user:
                    if i.email == email:
                        if i.is_blocked:
                            status = 'User is blocked'
                            break
                        payload = {
                            'email': email,
                            'name': i.name,
                            'id': i.id
                        }
                        enpayload = base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')
                        jwt_token = jwt.encode({'payload':enpayload}, 'secret', algorithm='HS256')
                        response = Response({'status': 'Success', 'payload': enpayload, 'email': email,
                                            'name': i.name, 'jwt': jwt_token, 'role': 'user', 'id': i.id})
                        return response
            else:
                data = request.data
                name = data['name']
                email = data['email']

                serializer = UserSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                user = authenticate(email=email)
                user = User.objects.all()
                status = 'None'
                for i in user:
                    if i.email == email:
                        if i.is_blocked:
                            status = 'User is blocked'
                            break

                        payload = {
                            'email': email,
                            'name': i.name,
                            'id': i.id
                        }
                        enpayload = base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')
                        jwt_token = jwt.encode({'payload': enpayload}, 'secret', algorithm='HS256')
                        response = Response({'status': 'Success', 'payload': enpayload, 'fullname': i.name,
                                            'jwt': jwt_token, "email": email, 'role': 'user', 'id': i.id})
                        return response
                return Response(serializer.data)
        except APIException as e:
            return Response(
                {'error': str(e)},status=status.HTTP_400_BAD_REQUEST
            )
        











                