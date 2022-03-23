# chat/views.py
from django.core.checks import messages
from django.http import request
from rest_framework import status

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chat, Message
from .serializers import ChatSerializer, ChatUserSerializer, MessageSerializer

def index(request):
    return render(request, 'index.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
    
    
def get_current_chat(chatId):
    return get_object_or_404(Chat,room=chatId)



class AllMessageRecordView(APIView):
    def get(self, format=None):
    
        message = Message.objects.all()
        serializer = MessageSerializer(message, many = True)
        print(serializer.data)
        return Response(serializer.data)
    

class ChatInfoView(APIView):
    def get(self, request):
    
        if "roomId" in request.GET:
            roomID = request.GET.get("roomId")
            chat = Chat.objects.filter(room=roomID).first()
            serializer = ChatSerializer(chat, many = False)
            print(serializer.data)
            return Response(serializer.data)
        return Response(
        {
            "error": True,
            "error_msg": "New Prameter",
        },
        status=status.HTTP_400_BAD_REQUEST
        )
    

class ChatMessageView(APIView):
    def get(self, request):
        if "roomId" in request.GET:
            roomID = request.GET.get("roomId")
            chat = Chat.objects.filter(room=roomID).first()
            messages =  MessageSerializer(chat.messages,many=True)
            return Response(messages.data)
        return Response(
            {
                "error": True,
                "error_msg": "New Prameter",
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    

# class ChatProfileView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request):
#         userIds = request.data["userIds"]
#         profile = UserProfile.objects.filter(reduce(operator.and_, (Q(user__id=x) for x in userIds)))
#         serializer = ProfileSerializer(profile, many=True)
        
#         return Response( 
#                         serializer.data,
#                         status=status.HTTP_200_OK
#                         )


class ChatUserProfileView(APIView):
    def post(self, request):
        serializer =  ChatUserSerializer(data=request.data())
        if serializer.is_valid:
            return Response(serializer.data)
        return Response(
            {
                "error": True,
                "error_msg": "New Prameter",
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
   
    