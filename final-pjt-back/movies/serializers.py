from rest_framework import serializers
from .models import Movie, Review, Credits


class MovieListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'title', 'overview', 'username')


# class CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', )


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credits
        fields = '__all__'