from django.urls import path
# from notification import api
from .unifonic_channel import UnifonicChannel, UnifonicMessage
from .notification import HasDatabaseNotifications, RoutesNotifications
from .notification_sender import NotificationSender
# from notifiable import HasDatabaseNotifications, RoutesNotifications
from .mail_channel import MailChannel
from .database_channel import DatabaseChannel
from .base_channel import BaseChannel



urlpatterns = [
    path('unifonichannel/',UnifonicChannel,name='unofonic-channel'),
    path('unifonicmessage/',UnifonicMessage, name='unifonic-message'),
    path('databasenotification/',HasDatabaseNotifications,name='database-notification'),
    path('routenotification/',RoutesNotifications,name='route-notification'),
    path('notificationsender/',NotificationSender,name='notification-sender'),
    path('mailchannel/',MailChannel,name='mail-channel'),
    path('databasechannel/',DatabaseChannel,name='database-channel'),
    path('basechannel/',BaseChannel,name='base-channel'),
]