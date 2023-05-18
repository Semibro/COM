from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


User = get_user_model()


# 영화리스트
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('pk', 'title', 'overview', 'vote_average')


# 리뷰의 댓글
class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Reviews
            fields = ('pk')

    review = ReviewSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ('pk', 'user', 'review', 'comments', 'created_at')


# 영화 추천 리스트
class RecommendMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('pk', 'title', 'poster_path')


# 유저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'nickname')  # hotfix


# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = '__all__'
        read_only_fields = ('movie',)


# 리뷰 리스트
class ReviewListSerializer(serializers.ModelSerializer):
     
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = ('pk', 'rate', 'user', 'content', 'created_at', 'updated_at')


# 영화 디테일
class MovieSerialzier(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class CreditSerializer(serializers.ModelSerializer):
        class Meta:
            model = Credits
            fields = '__all__'

    credits = CreditSerializer(read_only=True, many=True)

    class Meta:
        model = Movies
        exclude = ('like_users')


# 좋아요 누른 영화 리스트
class UserLikeMovieListSerialzier(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movies
            fields = ('pk', 'title', 'poster_path')

    like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'like_movies')