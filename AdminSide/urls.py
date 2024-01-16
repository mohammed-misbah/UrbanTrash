from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserListView
from . import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('verify_token/',views.verify_token,name='verify_token'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('userlist/', UserListView.as_view(), name="userlist"),
    path('block_user/<int:id>/', views.block_user, name='block_user'),
    path('unblock_user/<int:id>/', views.unblock_user, name='block_user'),
    # path('user', UserView.as_view(), name="user"),
    # path('userapi/', UserApi.as_view(), name="userapi"),
]

 