
from ..models import *
from rest_framework import serializers

class MemoSerializer(serializers.ModelSerializer):

    def create(self, validated_data, user):   
        lecture = Lecture.objects.get(id=validated_data["lectureId"])
        attendance = Memo(
            user = user,
            lecture = lecture,
            
            content = validated_data["content"],

        )
        attendance.save()
        return attendance
    
 
    class Meta:
        model = Memo
        fields = '__all__' 
        extra_kwargs = {
            'user': {'read_only': True}
        }




