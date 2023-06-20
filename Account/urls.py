from django.urls import path
from .views import RegisterView, LoginView, LogoutView, GoogleLogin, OTPloginAPIView
from . import views

urlpatterns = [
    path('register', RegisterView.as_view(),name='regiater'),
    path('login', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('verify_token/',views.verify_token,name='verify_token'),
    path('google/', GoogleLogin.as_view()),
    path('OTPlogin/',OTPloginAPIView.as_view())
]