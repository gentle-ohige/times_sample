from datetime import date
from ..models import Task
from ..serializer import TaskSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view



@api_view(['GET'])
def tasks_view(request):
    if request.method == 'GET':
        lectureId = request.GET.get("lectureId")
        tasks = Task.objects.filter(user=request.user, lecture__id = lectureId)
        serializers = TaskSerializer(tasks, many=True)
        return Response(
            data= serializers.data,
            status=status.HTTP_200_OK
            )

@api_view(['GET','PUT','POST','DELETE'])
def task_view(request):
    if request.method == 'GET':
        if "id" in request.GET: 
            id = request.GET.get("id")
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task)
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
        serializer = TaskSerializer()
        task = serializer.create(validated_data=data,user=request.user)
        return Response(
            data= TaskSerializer(task).data,
            status=status.HTTP_200_OK
            )

    
    
    elif request.method == 'POST':
        data = JSONParser().parse(request) 
        task = Task.objects.get(id=data['id'])

        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(
                data= TaskSerializer(task).data,
                status=status.HTTP_200_OK
                )
        else :
            print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    

    elif request.method == 'DELETE':
        id = request.GET.get("id")
        data = Task.objects.filter(id=id).first()  
        data.delete()
        return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        
    

