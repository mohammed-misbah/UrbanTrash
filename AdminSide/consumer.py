from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from Account.models import User
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response
import jwt
import json



class notification(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        try:
            token_key = self.scope['query_string'].decode().split('=')
            print(token_key, " Token key is printed")

            # Check if the token is a refresh token, in which case authentication is not needed
            decoded_token = jwt.decode(token_key[1], 'secret', algorithms=['HS256'])
    
            # Check if the token is a valid access token
            id = decoded_token.get('id')
            user = User.objects.get(id=id)
            self.scope['user'] = user

        except (jwt.exceptions.DecodeError, User.DoesNotExist, IndexError):
            raise AuthenticationFailed('Invalid token')
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()


    def disconnect(self, code):
        return super().disconnect(code)



    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        print(message,"message printed")

        serializer = NotificationSerializer(data={
           "user": self.scope['user'].id, # Provide the user ID here
           "message": message,
           "room_name": self.room_name
        })
    
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print("Data saved successfully:")
            print( self.scope['user'].is_admin)
            print( self.scope['user'].name)
            if self.scope['user'].is_admin == True:
                print("status")
                self.send(text_data=json.dumps({"message": message}))
        else:
            print("Serializer errors:", serializer.errors)
            raise AuthenticationFailed(f'AuthenticationFailed {serializer.errors}')
        # Send message to WebSocket
        


