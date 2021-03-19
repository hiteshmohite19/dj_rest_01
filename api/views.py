from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from api.models import User
from api.serializer import UserSerializer


@api_view(['GET'])
def api_list(request):
    data = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "ext":{
            "model": "Mustang",
            "year": 1964
        }
    }

    return Response(data)

@api_view(['GET'])
def users(request):
    users=User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer=UserSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()

    print(serializer.errors)
    return Response(request.data)

@api_view(['POST'])
def updateUser(request,pk):
    user=User.objects.get(id=pk)
    serializer=UserSerializer(instance=user,data=request.data)

    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response("Item deleted")