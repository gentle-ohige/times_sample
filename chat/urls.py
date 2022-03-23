from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('allmessage/', views.AllMessageRecordView.as_view(), name='allmessage'),
    path('roomMessage/', views.ChatMessageView.as_view(), name='roomMessgae'),
    path('chatInfo/', views.ChatInfoView.as_view(), name='chatInfo'),
    path('chatUserProfile/', views.ChatUserProfileView.as_view(), name='chatUserProfile'),
    
    ]
