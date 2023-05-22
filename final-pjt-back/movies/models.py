from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator

import datetime

# Create your models here.
# movie
class Movie(models.Model):
    listId = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    release_date = models.DateField(null=True, default=datetime.date.today)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)


# review / comment
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)], null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)