from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/reviews/', views.review_create_or_list),
    path('<int:review_pk>/detail/', views.review_detail),
    path('<int:review_pk>/comment/', views.comment_list),
]
