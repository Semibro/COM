from django.shortcuts import get_list_or_404, get_object_or_404, redirect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieListSerializer, ReviewSerializer
from .models import Movie, Review
import requests



headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWI1MTViYzI0Y2I5N2VlMDdkNjU4ZjVmZDBhYTFhNyIsInN1YiI6IjYzZDMxOGY0NjZhZTRkMDA5NmI3M2EwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ryaRC-WBbFQHXdaZjys7Gjrz8AxKGeaj1k6KioWjYWc"
}


# Create your views here.
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

def test(request):
    for i in range(1,4):
        listurl = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={i}"
        response = requests.get(listurl, headers=headers).json()
        print(response)
        movies = []
        for re in response['results']:
            movie = Movie(title=re['title'],
                          overview=re['overview'],
                          poster_path=re['poster_path'],
                          release_date=re['release_date'],
                          vote_average=re['vote_average'],
                          vote_count=re['vote_count'])
            movie.save()
            movies += [movie]
        serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

def movie_detail(request):
    pass

def review_list(request):
    pass