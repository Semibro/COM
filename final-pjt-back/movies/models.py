from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator

import datetime

# Create your models here.
class Movie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listId = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField(null=True)
    release_date = models.DateField(null=True, default=datetime.date.today)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)


class Credits(models.Model):
    listId = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    known_for_department = models.TextField()
    name = models.TextField()
    profile_path = models.TextField(null=True)
    movie = models.ManyToManyField(Movie)

class Detail(models.Model):
    listId = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    title = models.TextField()
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.DateField(null=True, default=datetime.date.today)
    movie = models.ManyToManyField(Movie)


class Recommend(models.Model):
    listId = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    title = models.TextField()
    poster_path = models.TextField()
    movie = models.ManyToManyField(Movie)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)