from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializer import UserSerializer, UserLoginSerializer
from .models import User
from rest_framework.views import APIView


# Create your views here.
class Registration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUser(APIView):
    def delete(self, request, pk):

        if user := User.objects.filter(pk=pk):
            user.delete()
            return Response(data={'delete completed'}, status=status.HTTP_204_NO_CONTENT )
        return Response(data={'member doesn\'t exist'}, status=status.HTTP_400_BAD_REQUEST)



class Login(APIView):
    permission_classes = []
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(data={'invalid username or/end password'}, status=status.HTTP_204_NO_CONTENT)

        login(request, user)
        return Response(data={'logged in'}, status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)



@api_view(["GET"])
def user_list(request):
    users = User.objects.all()

    if users:
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data={'No members yet'}, status=status.HTTP_200_OK)



# TODO: add user edit logic