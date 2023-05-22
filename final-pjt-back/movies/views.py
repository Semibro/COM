from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import Movie, Review, Comment

import requests

# Create your views here.
# api headers
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWI1MTViYzI0Y2I5N2VlMDdkNjU4ZjVmZDBhYTFhNyIsInN1YiI6IjYzZDMxOGY0NjZhZTRkMDA5NmI3M2EwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ryaRC-WBbFQHXdaZjys7Gjrz8AxKGeaj1k6KioWjYWc"
}


# movie / detail / credit / recommend
@api_view(['GET', 'POST'])
def movie_list(request):
    for page in range(1, 6):
        url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={page}"
        response = requests.get(url, headers=headers).json()
        saved_movies = Movie.objects.values_list('id', flat=True)
        for result in response['results']:
            if result['id'] not in saved_movies:
                try:
                    movie = Movie(
                    id = result['id'],
                    title=result['title'],
                    overview=result['overview'],
                    poster_path=result['poster_path'],
                    release_date=result['release_date'],
                    vote_average=result['vote_average'],
                    vote_count=result['vote_count'])
                    movie.save()
                except:
                    pass
    movies = get_list_or_404(Movie)
    serializer = PopularMovieListSerializer(movies, many=True)
    return Response(serializer.data)


# review / comment
@api_view(['POST', 'GET'])
def review_create_or_list(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    review = movie.review_set.all()
    if request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        serializer = ReviewListSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        data = f'{review_pk}번째 리뷰가 삭제됐습니다.'
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'DELETE'])
def comment_list(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.get(pk=review_pk)
    comment = review.comment_set.get()
    if request.method == 'GET':
        serializer = CommentListSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        comment.delete()
        data = '댓글이 삭제됐습니다.'
        return Response(data, status=status.HTTP_204_NO_CONTENT)