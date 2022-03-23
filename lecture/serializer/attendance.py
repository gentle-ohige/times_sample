from ..models import Attendance
from ..models import Lecture
from administer.serializers import UserSerializer, UserProfileSerializer
from django.db.models.fields import CharField
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .postion import *


class AttendanceSerializer(serializers.ModelSerializer):

    def create(self, validated_data, user):   
        lecture = Lecture.objects.get(id=validated_data["lectureId"])
        attendance = Attendance(
            user = user,
            lecture = lecture,
            attendance = validated_data["attendance"],
            attendanceDate = validated_data["attendanceDate"]
        )
        attendance.save()
        return attendance
    
    def update(self, instance, validated_data):
        instance.attendance = validated_data["attendance"]
        instance.attendanceDate = validated_data["attendanceDate"]
        instance.save()
        return instance
    
    # def is_valid(self):
    #     return True
  
    class Meta:
        model = Attendance
        fields = '__all__' 

    
    
    


