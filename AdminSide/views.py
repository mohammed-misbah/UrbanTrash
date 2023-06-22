from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializers,UserCreateSerializer
from rest_framework import status
from .models import User
import jwt , datetime
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import APIException

# Create your views here.

    
class RegisterView(APIView):
    @extend_schema(responses=UserSerializers)
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except KeyError:
            return Response({'status': 'Please provide the required details'})

        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise AuthenticationFailed('Password is incorrect')

            if not user.is_admin:
                raise AuthenticationFailed('User is not an admin')

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

            return Response({'status': "Success", 'payload': payload, 'admin_jwt': token, 'admin': userdetails}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise AuthenticationFailed('Email or Password is incorrect')




class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
    

@api_view(['GET'])
@extend_schema(responses=UserSerializers)
def userlist(request):
    user = User.objects.all()
    print("The user List is ==================>>>>>>>>>>>>>>>>>>>",user)
    serializer = UserCreateSerializer(user,many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
def block_user(request, id):
    user = User.objects.get(id=id)
    print(user)
    user.is_active = False
    user.save()
    return Response({'status': 'blocked'})

@api_view(['PATCH'])
def unblock_user(request, id):
    user = User.objects.get(id=id)
    print(user)
    user.is_active = True
    user.save()
    return Response({'status': 'unblocked'})








# class UserApi(APIView):

#     @extend_schema(responses=UserSerializer)
#     def get(request,id):
#         user = User.objects.all()
#         print(user)
#         serializer = UserSerializer(user,many=True)
#         print(serializer.data)
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
#         print(request)
#         token = request.COOKIES.get('jwt')
#         print(token)
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, self.JWT_SECRET, algorithms=[self.JWT_ALGORITHM])
#             print(payload)
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)