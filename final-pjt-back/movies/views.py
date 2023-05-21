from django.shortcuts import get_list_or_404, get_object_or_404, redirect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieListSerializer, ReviewSerializer, DetailSerializer
from .models import Movie, Review, Credits, Detail, Recommend
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
# lst = [502356, 385687, 713704, 640146, 882569, 842675, 447365, 594767, 758323, 840326, 76600, 868759, 552688, 654374, 649609, 677179, 603692, 1037644, 1102776, 934433, 620705, 868985, 785759, 948713, 493529, 727340, 420808, 315162, 638974, 1111140, 876969, 964980, 804150, 325358, 385128, 505642, 32516, 507250, 447277, 816904, 436270, 384018, 980078, 283995, 67308, 997776, 1121116, 337339, 455476, 700391, 1048300, 1085103, 736790, 701952, 747355, 458220, 168259, 631842, 1120558, 579884, 1079078, 946310, 1033219, 758009, 1008005, 849869, 646389, 994128, 1118721, 536554, 842945, 826942, 985939, 876792, 265712, 667538, 634649, 296271, 1105014, 1104040, 966220, 943822, 875104, 616037, 507086, 650270, 869626, 1084225, 984105, 776835, 361743, 1011679, 983282, 774752, 635302, 676710, 1114905, 785084, 1076605]

@api_view(['GET', 'POST'])
def movie_list(request):
    for i in range(1, 6):
        popular_url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={i}"
        response = requests.get(popular_url, headers=headers).json()
        saved_movies = Movie.objects.values_list('id', flat=True)
        for re in response['results']:
            if re['id'] not in saved_movies:
                try:
                    movie = Movie(
                    id = re['id'],
                    title=re['title'],
                    overview=re['overview'],
                    poster_path=re['poster_path'],
                    release_date=re['release_date'],
                    vote_average=re['vote_average'],
                    vote_count=re['vote_count'])
                    movie.save()
                except:
                    pass
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request:
        # Credit
        credits_url = f"https://api.themoviedb.org/3/movie/{movie_pk}/credits?language=ko-KR"
        response = requests.get(credits_url, headers=headers).json()
        saved_movies = Credits.objects.values_list('id', flat=True)
        for re in response['cast']:
            if re['id'] not in saved_movies:
                movie = Credits(
                id=re['id'],
                known_for_department=re['known_for_department'],
                name=re['name'],
                profile_path=re['profile_path'])
                movie.save()
        for re in response['crew']:
            if re['id'] not in saved_movies:
                movie = Credits(
                id=re['id'],
                known_for_department=re['known_for_department'],
                name=re['name'],
                profile_path=re['profile_path'])
                movie.save()
        credits = get_list_or_404(Credits)
        # serializer = CreditSerializer(movies, many=True)

        # Detail
        detail_url = f'https://api.themoviedb.org/3/movie/{movie_pk}?language=ko-KR'
        response = requests.get(credits_url, headers=headers).json()
        saved_movies = Credits.objects.values_list('id', flat=True)
        for re in response['results']:
            if re['id'] not in saved_movies:
                movie = Detail(
                id=re['id'],
                title=re['title'],
                overview=re['overview'],
                poster_path=re['poster_path'],
                release_date=re['release_date'])
                movie.save()
        details = get_list_or_404(Detail)
        context = {credits, details}
        serializer = DetailSerializer(context, many=True)
        return Response(serializer.data)


def review_list(request):
    pass


def movie_detail(request, movie_pk):
    pass