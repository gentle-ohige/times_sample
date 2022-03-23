
from ..models import *
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data, user):   
        lecture = Lecture.objects.get(id=validated_data["lectureId"])
        attendance = Task(
            user = user,
            lecture = lecture,
            done = validated_data["done"],
            title = validated_data["title"],
            memo = validated_data["memo"],
            deadline = validated_data["deadline"],
            validAlarm = validated_data["validAlarm"],
            alarm = validated_data["alarm"],
            url = validated_data["url"],
        )
        attendance.save()
        return attendance
    
    class Meta:
        model = Task
        fields = '__all__' 
        extra_kwargs = {
            'user': {'read_only': True}
        }




