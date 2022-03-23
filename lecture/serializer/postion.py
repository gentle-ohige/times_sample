
from ..models import Position
from rest_framework import serializers


class PostionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('x','y')




