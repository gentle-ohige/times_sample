
from .forms import IconImageForm
from .serializers import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from chat.models import *
from .models import *

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def record_user_profile(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=ValueError):
        user = serializer.create(validated_data=request.data, user = request.user)

        return Response(
            user.id,
            status=status.HTTP_201_CREATED
        )

    return Response(
        {
            "error": True,
            "error_msg": serializer.error_messages,
        },
        status=status.HTTP_400_BAD_REQUEST
    )

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, format=None):
        
        profile = UserProfile.objects.get(user=self.request.user) 
        profileSerializer = UserProfileSerializer(profile)
        return Response( 
                        profileSerializer.data,
                        status=status.HTTP_200_OK
                        )
        
    def post(self, request):
        
        user = self.request.user
        

        if 'username' in request.data.keys():
            user.username = request.data['username']
            
        if 'display_name' in request.data.keys():
            user.display_name = request.data['display_name']
            
        if 'email' in request.data.keys():
            user.email = request.data['email']
        
        user.date_time = timezone.now()
        user.save()
        
        return Response( 
                    UserProfileSerializer(user).data,
                    status=status.HTTP_200_OK
                    )
    



     
class ImageUploadView(APIView):
    def post(self, request):
        form = IconImageForm(request.POST, request.FILES)
        if form.is_valid():
            self.request.user.iconImage = request.FILES['iconImage']
            self.request.user.update_date = timezone.now()
            self.request.user.save()
            serializer = UserProfileSerializer(self.request.user)
            return Response( 
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
            {
                "error": True,
            },
            status=status.HTTP_400_BAD_REQUEST
            )
            