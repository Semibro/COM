from rest_framework import serializers
from .models import Movie, Review, Comment
from accounts.models import User


# movie
class PopularMovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'

    user = UserSerializer(read_only=True)
    like_movies = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'


# review, comment
class ReviewListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class MovieTPSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path',)
    
    movie = MovieTPSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieTPSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path',)

    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content',)
        read_only_fields = ('movie', 'user',)


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)
        read_only_fields = ('user', 'movie', 'review',)