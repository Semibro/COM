from django.db import models

import datetime

# Create your models here.
class Movie(models.Model):
    listId = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    release_date = models.DateField(null=True, default=datetime.date.today)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)