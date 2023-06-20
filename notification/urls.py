from django.urls import path
from notification import api

urlpatterns = [
    path('getnotifications/',api.NotificationAPI.as_view(),name='api-get-notification'),
    path('createinvitation/',api.NotificationAPI.as_view(), name='api-create-invitation'),
    path('deletenotification/',api.NotificationAPI.as_view(),name='api-delete-notification'),
    path('invitation/<int:pk>/',api.acceptInvitation,name='api-accept-invitation'),
    path('invitation/request/',api.ReqToJoinServer,name='api-req-to-join'),
]