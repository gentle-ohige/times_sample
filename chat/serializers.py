from rest_framework import serializers
from .models import Chat, Message

from django.contrib.auth import get_user_model
from rest_framework.serializers import SerializerMethodField

User = get_user_model()

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ('id','content','user','timestamp')


class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')  
    
  

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'room', 'participants')
      
      