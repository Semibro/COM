from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('reviews/<int:review_pk>/', views.review_detail),
    # path('reviews/', views.review_list),
]