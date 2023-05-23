from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User

# Create your views here.
@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serilaizer = UserSerializer(person)
        return Response(serilaizer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def follow(request, username):
    user = request.user
    person = get_object_or_404(User, username=username)
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
        serializer = UserSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK) 