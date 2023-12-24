from django.urls import path
from .views import RegisterView, LoginView, LogoutView,UserListView,BlockUser,UnBlockUser
from . import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('verify_token/',views.verify_token,name='verify_token'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('userlist/', UserListView.as_view(), name="userlist"),
    path('block_user/<int:id>/', BlockUser.as_view(), name="block_user"),
    path('unblock_user/<int:id>/', UnBlockUser.as_view(), name="unblock_user")
    # path('user', UserView.as_view(), name="user"),
    # path('userapi/', UserApi.as_view(), name="userapi"),
]

 