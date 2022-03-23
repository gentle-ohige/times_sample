
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def test_view(request):
    if request.method == 'GET':
        return Response(
            data= "test",
            status=status.HTTP_200_OK
            )
