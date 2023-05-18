from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


# @api_view(['GET'])
# def review_list(request):
#     reviews = get_list_or_404(Reviews)
#     serializer = ReviewListSerializer(reviews, many=True)
#     return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Reviews, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'review {review_pk} is deleted'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)

    if request.method == 'POST':
        serializer = ReviewDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
