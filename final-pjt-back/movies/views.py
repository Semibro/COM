from django.shortcuts import get_list_or_404, get_object_or_404, redirect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieListSerializer, ReviewSerializer, CreditSerializer
from .models import Movie, Review, Credits
import requests



headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWI1MTViYzI0Y2I5N2VlMDdkNjU4ZjVmZDBhYTFhNyIsInN1YiI6IjYzZDMxOGY0NjZhZTRkMDA5NmI3M2EwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ryaRC-WBbFQHXdaZjys7Gjrz8AxKGeaj1k6KioWjYWc"
}


# Create your views here.
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = get_list_or_404(Movie)
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(serializer.data)
    

@api_view(['GET', 'POST'])
def movie_list(request):
    for i in range(1,4):
        popular_url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={i}"
        response = requests.get(popular_url, headers=headers).json()
        saved_movies = Movie.objects.values_list('title', flat=True)
        for re in response['results']:
            if re['title'] not in saved_movies:
                movie = Movie(
                id = re['id'],
                title=re['title'],
                overview=re['overview'],
                poster_path=re['poster_path'],
                release_date=re['release_date'],
                vote_average=re['vote_average'],
                vote_count=re['vote_count'])
                movie.save()
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request:
        credits_url = f"https://api.themoviedb.org/3/movie/{movie_pk}/credits?language=ko-KR"
        response = requests.get(credits_url, headers=headers).json()
        saved_movies = Credits.objects.values_list('id', flat=True)
        count = 0
        for re in response['cast']:
            if re['id'] not in saved_movies and count < 2:
                count += 1
                movie = Credits(
                id=re['id'],
                known_for_department=re['known_for_department'],
                name=re['name'],
                profile_path=re['profile_path'])
                movie.save()
        for re in response['crew'] and count == 2:
            if re['id'] not in saved_movies:
                movie = Credits(
                id=re['id'],
                known_for_department=re['known_for_department'],
                name=re['name'],
                profile_path=re['profile_path'])
                movie.save()
        movies = get_list_or_404(Credits)
        serializer = CreditSerializer(movies, many=True)
        return Response(serializer.data)


def review_list(request):
    pass