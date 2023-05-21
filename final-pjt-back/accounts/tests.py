from django.test import TestCase

# Create your tests here.
import requests
from movies.models import Movie
# Create your tests here.


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWI1MTViYzI0Y2I5N2VlMDdkNjU4ZjVmZDBhYTFhNyIsInN1YiI6IjYzZDMxOGY0NjZhZTRkMDA5NmI3M2EwNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ryaRC-WBbFQHXdaZjys7Gjrz8AxKGeaj1k6KioWjYWc"
}


for i in range(1,4):
    listurl = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={i}"
    response = requests.get(listurl, headers=headers).json()
    movies = []
    # saved_movies = Movie.objects.values_list('title', flat=True)
    for re in response['results']:
        # if re['title'] not in saved_movies:
            movie = Movie(title=re['title'],
            overview=re['overview'],
            poster_path=re['poster_path'],
            release_date=re['release_date'],
            vote_average=re['vote_average'],
            vote_count=re['vote_count'])
            movie.save()
    print(movies)