from datetime import date

from ..serializer import MemoSerializer
from ..models import Memo
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view



@api_view(['GET'])
def memos_view(request):
    if request.method == 'GET':
        lectureId = request.GET.get("lectureId")
        tasks = Memo.objects.filter(user=request.user, lecture__id = lectureId)
        serializers = MemoSerializer(tasks, many=True)
        return Response(
            data= serializers.data,
            status=status.HTTP_200_OK
            )

@api_view(['GET','PUT','POST','DELETE'])
def memo_view(request):
    if request.method == 'GET':
        if "id" in request.GET: 
            id = request.GET.get("id")
            task = Memo.objects.get(id=id)
            serializer = MemoSerializer(task)
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
        serializer = MemoSerializer()
        memo = serializer.create(validated_data=data, user=request.user)
        return Response(
            data= MemoSerializer(memo).data,
            status=status.HTTP_200_OK
            )

    
    elif request.method == 'POST':
        data = JSONParser().parse(request) 
        task = Memo.objects.get(id=data['id'])

        serializer = MemoSerializer(task, data=data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(
                data= MemoSerializer(task).data,
                status=status.HTTP_200_OK
                )
        else :
            print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    

    elif request.method == 'DELETE':
        id = request.GET.get("id")
        data = Memo.objects.filter(id=id).first()  
        data.delete()
        return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        
    

