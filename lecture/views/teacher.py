from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 
from ..models import Teacher

from ..serializer import TeacherSerializer
from rest_framework.decorators import api_view



@api_view(['GET'])
def all_teacherview(request):
    data = Teacher.objects
    serializers = TeacherSerializer(data, many=True)
    return Response(
            data= serializers.data,
            status=status.HTTP_200_OK
        )

@api_view(['GET','PUT','POST','DELETE'])
def teacher_view(request):
    
    print(request)
    if request.method == 'GET':
        id = request.GET.get("id")
        data = Teacher.objects.filter(id=id).first()
        serializers = TeacherSerializer(data, many=False)
        return Response(
                data= serializers.data,
                status=status.HTTP_200_OK
            )
    elif request.method == 'PUT':
        data = JSONParser().parse(request) 
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    data= serializer.data,
                    status=status.HTTP_200_OK
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'POST':
        data = JSONParser().parse(request) 
        teacher = Teacher.objects.get(id=data['id'])
        serializer = TeacherSerializer(teacher,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    data= serializer.data,
                    status=status.HTTP_200_OK
                )
        else :
            print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        id = request.GET.get("id")
        data = Teacher.objects.filter(id=id).first()
        if data is not None:  
            data.delete()
            return Response(
                    status=status.HTTP_204_NO_CONTENT
                )
        