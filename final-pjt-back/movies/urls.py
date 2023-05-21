from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.review_list),
    # path('reviews/<int:review_pk>/', views.review_detail),
    # path('reviews/<int:review_pk>/comments/', views.comment_create),
    # path('test/', views.test)
]
