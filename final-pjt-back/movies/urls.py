from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/reviews/', views.review_create_or_list),
    path('<int:movie_pk>/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/<int:review_pk>/comment/', views.comment_create_or_list),
    path('<int:movie_pk>/<int:review_pk>/comment/<int:comment_pk>/', views.comment_delete),
]