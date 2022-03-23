from datetime import date
from ..models import Lecture
from ..serializer.lecuture import LectureSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view



@api_view(['GET'])
def all_lecture_view(request):
    if request.method == 'GET':
        myLecture = Lecture.objects.filter(user=request.user)
        serializers = LectureSerializer(myLecture, many=True)
        return Response(
            data= serializers.data,
            status=status.HTTP_200_OK
            )

@api_view(['GET','PUT','POST','DELETE'])
def lecture_view(request):
    if request.method == 'GET':
        if "id" in request.GET: 
            id = request.GET.get("id")
            myLecture = Lecture.objects.filter(id=id).first()
            serializer = LectureSerializer(myLecture, many=False)
            return Response(
                data= serializer.data,
                status=status.HTTP_200_OK
                )
        return Response(
            {
                "error": True,
                "error_msg": "New Prameter",
            },
            status=status.HTTP_400_BAD_REQUEST
        )



    elif request.method == 'PUT':
        data = JSONParser().parse(request) 
        lectureSerializer = LectureSerializer()
        lecture = lectureSerializer.create(validated_data=data,user=request.user)
       
        return Response(
            data = LectureSerializer(lecture, many= False).data,
            status = status.HTTP_200_OK
            )

    
    
    elif request.method == 'POST':
        data = JSONParser().parse(request) 
        serializer = LectureSerializer()
        lecture = serializer.update(data)
        return Response(
            data= LectureSerializer(lecture, many= False).data,
            status=status.HTTP_200_OK
            )
    

    elif request.method == 'DELETE':
        id = request.GET.get("id")
        data = Lecture.objects.filter(id=id).first()  
        data.delete()
        return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        
    

