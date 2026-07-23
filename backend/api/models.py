from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings

"""
    Custom user model
"""
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)

"""
    Artist model
"""
class Artist(models.Model):
    name = models.CharField(max_length=100)

"""
    Album model
"""
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField(null =True, blank=True)

"""
    Song model
"""
class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField(null=True, blank=True)

"""
    Scrobble model
"""
class Scrobble(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)