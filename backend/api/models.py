from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings

"""
    Custom user model
"""
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)

    joined_date = models.DateTimeField(auto_now_add=True, editable=False)
    total_scrobbles = models.IntegerField(default=0)

"""
    Artist model
"""
class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    album_count = models.IntegerField(default=0)
    song_count = models.IntegerField(default=0)

    total_scrobbles = models.IntegerField(default=0)
"""
    Album model
"""
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    release_date = models.DateField(null =True, blank=True)

    song_count = models.IntegerField(default=0)

    total_scrobbles = models.IntegerField(default=0)
"""
    Song model
"""
class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    total_scrobbles = models.IntegerField(default=0)
"""
    Scrobble model
"""
class Scrobble(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

"""
    Payload for creating a new scrobble
"""
class CreateScrobblePayload(models.Model):
    song = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)