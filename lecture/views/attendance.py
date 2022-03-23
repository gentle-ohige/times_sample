from datetime import date
from ..serializer.attendance import AttendanceSerializer
from ..models import *
from ..serializer.lecuture import LectureSerializer
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import serializers, status

class AttendanceView(APIView):
    def get(self, request):
        if "id" in request.GET: 
            id = request.GET.get("id")
            data = Attendance.objects.filter(id=id).first()
            serializer = AttendanceSerializer(data, many=False)
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
        
    def post(self, request):
                
        if "id" in request.data:
            attendance = Attendance.objects.get(id=request.data["id"])
            attendance = AttendanceSerializer().update(instance= attendance,validated_data=request.data)
        else :
            attendance = AttendanceSerializer().create(validated_data=request.data,user=request.user)
    
        serializer = AttendanceSerializer(Attendance.objects.get(id=attendance.id), many= False)
        return Response(
            data= serializer.data,
            status=status.HTTP_200_OK
            )
         
    def delete(self, request):
        id = request.GET.get("id")
        attendance = Attendance.objects.filter(id=id).first()
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AllAttendanceView(APIView):
    def get(self, request):
        if "lectureId" in request.GET: 
            lectureId = request.GET.get("lectureId")
            data = Attendance.objects.filter(user=request.user,lecture__id=lectureId)
            serializers = AttendanceSerializer(data, many=True)
            return Response(
                data= serializers.data,
                status=status.HTTP_200_OK
                )
        return Response(status=status.HTTP_400_BAD_REQUEST)

