from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator
from movies.models import Movies


# Create your models here.
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