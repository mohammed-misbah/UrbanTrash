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
# from .permissions import IsTokenVerified
from .serializers import UserSerializer
from jwt import DecodeError, ExpiredSignatureError

# Create your views here.

    
class RegisterView(APIView):
    @extend_schema(responses=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    # extend_schema
    def post(self, request):    
        print("enteeered")
        try:
            email = request.data['email']
            password = request.data['password']
            print(email, password, ">>>>>>>>>>")
        except:
            return Response({'status': 'Please provide the mentioned details'})
        print("111111111111")
        user = User.objects.filter(email=email).first()
        print(user, "<<<<<<<,")
        # user = User.objects.get(email=email)
        if user is None:
            return Response({'status': 'Email does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'status': 'Password is incorrect'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_admin:
            return Response({'status': 'User not admin'}, status=status.HTTP_403_FORBIDDEN)

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
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            print(token, "token has getting")
         
            return Response({'status': "Success", 'payload': payload, 'admin_jwt': token, 'admin': userdetails},status=status.HTTP_200_OK)
        
      
        
@api_view(['GET'])
@extend_schema(responses=UserSerializer)
def verify_token(request):
    # try:
    print("Entttttttteeeeeeeeredddddddddd")
    token = request.headers.get('Authorization')
    print(token, "getting a token")
    decoded = jwt.decode(token, 'secret', algorithms='HS256')
    user_id = decoded.get('id')
    print("1111111111111")
    print(user_id, "user ID is >>>>>>>")
    user = User.objects.filter(id=user_id).first()
    print("22222222222222222")
    print(user, "user details")
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
    # except (DecodeError, ExpiredSignatureError):
    #     return Response({'status': 'Token Invalid'}, status=status.HTTP_401_UNAUTHORIZED)





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


class BlockUser(APIView):
    def patch(request, id):
        user = User.objects.get(id=id)
        user.is_active = False
        user.save()
        return Response({'status': 'blocked'})

class UnBlockUser(APIView):
    def patch(request, id):
        user = User.objects.get(id=id)
        user.is_active = True
        user.save()
        return Response({'status': 'unblocked'})
        






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

