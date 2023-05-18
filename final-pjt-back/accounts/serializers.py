from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movies, Reviews


User = get_user_model()


# 사용자
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# 사용자가 작성한 영화 리뷰
class ReviewMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('pk', 'title', 'poster_path', 'vote_average')