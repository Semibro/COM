from rest_framework import serializers
from .models import User
from movies.models import *

class UserSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    like_movies = MovieSerializer(many=True)
    
    class Meta:
        model = User
        fields = '__all__'