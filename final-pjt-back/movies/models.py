from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings
import datetime


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=300)
    overview = models.TextField()
    poster_path = models.TextField(null=True)
    release_date = models.DateField(null=True, default=datetime.date.today)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Credits(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    director_name = models.CharField(max_length=100)
    director_profile_path = models.TextField(null=True)
    actor_name_1 = models.CharField(max_length=100, null=True)
    actor_profile_path_1 = models.TextField(null=True)
    actor_name_2 = models.CharField(max_length=100, null=True)
    actor_profile_path_2 = models.TextField(null=True)


class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='reviews')
    rate = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE, related_name='comments')
    comments = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)