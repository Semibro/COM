from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_pic = ProcessedImageField(
        blank = True,
        upload_to = 'profile/images',
        processors = [ResizeToFill(300, 300)],
        format = 'PNG',
        options = {'quality': 90},
    )