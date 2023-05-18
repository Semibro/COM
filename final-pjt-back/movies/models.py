from django.db import models
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