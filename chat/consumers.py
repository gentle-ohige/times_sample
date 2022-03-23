import json
from .serializers import MessageSerializer
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from .views import get_current_chat
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def new_message(self, data):
        messageStr = data['message']
        user_id = data['user_id']
        user = User.objects.filter(id=user_id).first()
        
        message = Message.objects.create(
            content = messageStr,
            user = user
            )
    
        current_chat = get_current_chat(data['room_id'])
        current_chat.messages.add(message)
        current_chat.save()
        return self.send_chat_message(message)
    
    
    commands = {
        'new_message': new_message
    }
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.new_message(data)
        # self.commands[data['command']](self, data)
        # message = text_data_json['message']

        # # Send message to room group
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message
        #     }
        # )

    def send_chat_message(self, message):
    
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'data': MessageSerializer(message, many=False).data
            }
        )
        
    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
        
        
