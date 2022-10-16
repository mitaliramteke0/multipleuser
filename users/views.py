from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Users
from .serializers import UserSerializer


# Create your views here.
@api_view(["GET","POST"])
def usersListView(request):
    if request.method == "GET":
        users = Users.objects.all()
        UserSerializer = UserSerializer(users,many = True)
        return Response(UserSerializer.data)
    elif request.method == "POST":
        UserSerializer = UserSerializer(data=request.data)
        if UserSerializer.is_valid():
            UserSerializer.save()
            return Response(UserSerializer.data,status=status.HTTP_201_CREATED)
        return Response(UserSerializer.errors)


@api_view(["GET","PUT","DELETE"])
def usersDetailView(request,pk):
    try:
        users=Users.objects.get(pk = pk)
    except users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        UserSerializer = UserSerializer(Users)
        return Response(UserSerializer.data)
    elif request.method == "PUT":
        UserSerializer = UserSerializer(data=request.data)
        if UserSerializer.is_valid():
            UserSerializer.save()
            return Response(UserSerializer.data)
        return Response(UserSerializer.errors)


    if request.method == "DELETE":
        Users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


