from django.urls import path
from .views import ScrapBookings, ScrapPickupUpdatesAPI, ScrapPickupList, AdminPickuplistAPIView

urlpatterns = [ 
        path('scrap_booking/', ScrapBookings.as_view(), name='waste_booking'),
        path('scrappickup_detail/<int:id>/', ScrapPickupList.as_view(), name='pickup-details'),
        path('scrappickup_detailist/',AdminPickuplistAPIView.as_view(),name='scraporder_detail'),
        path('scrapickup_update/<int:id>/',ScrapPickupUpdatesAPI.as_view(),name='scrap-update')
]

