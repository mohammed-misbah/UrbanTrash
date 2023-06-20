from django.urls import path
from .import views
from Address.views import AddressListAPIView,AddressPostAPIView,UserProfileAPIView

#url path is here

urlpatterns = [
    path('listAddress/<int:id>/', AddressListAPIView.as_view(), name='add_address'),
    path('addAddress', AddressPostAPIView.as_view(), name='address_post'),  
    path('profile/<int:id>/',UserProfileAPIView.as_view(), name='userprofile')
]

 


