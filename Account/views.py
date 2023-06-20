from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
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
# from .otp import send_request,verify_Otp


# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# ============================= User Login ========================#

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        # response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    
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
                print('payload iiissssssssss', payload)
                enpayload = base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')
                jwt_token = jwt.encode({'payload': enpayload}, 'secret', algorithm='HS256')
                response = Response({'status': 'Success', 'payload': enpayload, 'email': user.email,
                                            'name': user.name, 'jwt': jwt_token, 'role': 'user', 'id': user.id})
                return response
            else:
                return Response({'status':'User not found'})
        except Exception as e:
            return Response({'status':"Error occur while otp generating"})
        

# ====================Verifying Token =====================#


@api_view(['GET'])
def verify_token(request):
    token = request.headers.get('Authorization')
    print(token,'token is printed')
    try:
        token = request.headers.get('Authorization')
        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        id = decoded.get('id')
        user = User.objects.get(id=id)  

        if user:
            userdetails ={
                        'id':user.id,
                        'name': user.name,
                        'email' : user.email,
                        'phone': user.phone,
                    }
        
            return Response({'user':userdetails})
        else:
            return Response({'status' : 'Token Invalid'})
    except APIException as e:
        return Response(
                {'verify_errors': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

# ==================== LogOut ==========================#


class LogoutView(APIView):
    def post(self, request):
        print("===============>>>>>>>>>>>>")
        response = Response()
        print("<<<<<<<<<<<=============")
        response.delete_cookie('jwt')
        print('deleted')
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
                    print(i, "entering gooogle signin page")
                    if i.email == email:
                        print("checking email in fine ")
                        if i.is_blocked:
                            status = 'User is blocked'
                            break
                        payload = {
                            'email': email,
                            'name': i.name,
                            'id': i.id
                        }
                        print('payload', payload)
                        enpayload = base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')
                        jwt_token = jwt.encode({'payload':enpayload}, 'secret', algorithm='HS256')
                        response = Response({'status': 'Success', 'payload': enpayload, 'email': email,
                                            'name': i.name, 'jwt': jwt_token, 'role': 'user', 'id': i.id})
                        return response
            else:
                data = request.data
                name = data['name']
                print("name is printed...??",name)
                email = data['email']
                print("email is printed...???",email)

                print("google details fetched successfully")

                serializer = UserSerializer(data=request.data)
                print(serializer,"user created using google")
                serializer.is_valid(raise_exception=True)
                serializer.save()

                user = authenticate(email=email)
                user = User.objects.all()
                status = 'None'
                for i in user:
                    print(i, "entering gooogle signin page")
                    if i.email == email:
                        print("checking email in fine ")
                        if i.is_blocked:
                            status = 'User is blocked'
                            break

                        payload = {
                            'email': email,
                            'name': i.name,
                            'id': i.id
                        }
                        print('payload', payload)
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
        











                