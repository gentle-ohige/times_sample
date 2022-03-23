from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, UserIcon
from chat.models import *


class UserSerializer(serializers.ModelSerializer):
    def create(self,user, validated_data):

        userProfile = UserProfile.objects.create(
            user = user
        )
        userProfile.room = "room_" + str(user.id)
        userProfile.save()
        chat = Chat.objects.create(
                room = userProfile.room
            )
        chat.participants.add(user)
        
        return user
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )


class UserProfileSerializer(serializers.ModelSerializer):
      class Meta:
        model = UserProfile
        fields = '__all__'

     
class IconImageSerializer(serializers.ModelSerializer):
      class Meta:
        model = UserIcon
        fields = (
            'iconImage',
        )

     
    
