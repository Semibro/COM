from rest_framework import serializers
from .models import *


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('title', 'overview',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ('id', 'title', 'content',)


class ReviewDetailSerializer(ReviewSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta(ReviewSerializer.Meta):
        fields = ReviewSerializer.Meta.fields + (
            'movie_title',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['movie'] = rep.pop('movie_title', [])
        return rep


class MovieDetailSerializer(serializers.ModelSerializer):

    class ReviewContentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Reviews
            fields = ('title', 'content',)

    review_set = ReviewContentSerializer(many=True, read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'