from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

class SignupView(APIView):
    def get(self,request):
        todos=User.objects.all()
        serializer=UserSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data) 
        if serializer.is_valid():
            token=serializer.validated_data
            return Response({"token":token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       