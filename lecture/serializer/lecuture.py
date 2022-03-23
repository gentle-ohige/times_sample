
from ..models import Lecture
from administer.serializers import UserSerializer, UserProfileSerializer
from django.db.models.fields import CharField
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .postion import *
from .teacher import *


class LectureSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    user = UserSerializer(many=False,required=False)
    title =  serializers.CharField()
    positions = PostionSerializer(many=True)
    teachers = TeacherSerializer(many=True)
    
    def create(self, validated_data, user):   
        lecture = Lecture(
            user = user,
            title = validated_data["title"],
        )
        lecture.save()
    
        for positionData in validated_data["positions"]:
            serializer = PostionSerializer(data=positionData)
            position = serializer.create(validated_data=positionData)
            lecture.positions.add(position)
            
        for teacherData in validated_data["teachers"]:
            teachres = Teacher.objects.filter(id__in=teacherData)
            lecture.teachers.set(teachres)
        
        return lecture
    
    def update(self, validated_data):
        lecture = Lecture.objects.get(id=validated_data["id"])
        
        title =  validated_data.get("title")
        if title is not None:
            lecture.title = title
    
        positionData = validated_data.get("positions")
        if positionData is not None:
            serializer = PostionSerializer(data=positionData)
            if serializer.is_valid():
                
                for old in lecture.positions :
                    old.delete()
                position = serializer.save()
                lecture.positions.set(position)
            
        teacherData = validated_data.get("teachers")  
        if teacherData is not None:
            teacher = Teacher.objects.filter(id__in = teacherData)
            lecture.teachers.set(teacher) 
            
        lecture.save()
        return lecture
    
    class Meta:
        model = Lecture
        fields = ('user','id','title','positions','teachers')

    
    


