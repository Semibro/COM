from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PopularMovieListSerializer
from .models import Movie

import requests

# Create your views here.
headers = {
    "accept": "application/json",
    "Authorization": "Bearer cab515bc24cb97ee07d658f5fd0aa1a7"
}


@api_view(['GET'])
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