from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from django.contrib.auth.models import User
from django.core import serializers


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_user(request):
    if(request.auth):
        user = User.objects.filter(username=request.query_params.get('name'),is_active=True)
        if user:
            data = serializers.serialize('json',user)
            return JsonResponse(data=data,safe=False)
        else:
            return Response({"message":"No user found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message":"Authentiation Error"},status=status.HTTP_400_BAD_REQUEST)
