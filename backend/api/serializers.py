from rest_framework import serializers
from .models import User, Artist, Album, Song, Scrobble

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='artist.name', read_only=True)
    biography = serializers.CharField(source='artist.biography', read_only=True)
    image = serializers.ImageField(source='artist.image', read_only=True)
    album_count = serializers.IntegerField(source='artist.album_count', read_only=True)
    song_count = serializers.IntegerField(source='artist.song_count', read_only=True)
    total_scrobbles = serializers.IntegerField(source='artist.total_scrobbles', read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='album.title', read_only=True)
    artist_name = serializers.CharField(source='album.artist.name', read_only=True)
    release_date = serializers.DateField(source='album.release_date', read_only=True)
    total_scrobbles = serializers.IntegerField(source='album.total_scrobbles', read_only=True)
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='song.title', read_only=True)
    album_title = serializers.CharField(source='song.album.title', read_only=True)
    artist_name = serializers.CharField(source='song.album.artist.name', read_only=True)
    total_scrobbles = serializers.IntegerField(source='song.total_scrobbles', read_only=True)
    class Meta:
        model = Song
        fields = '__all__'

class ScrobbleSerializer(serializers.ModelSerializer):
    song_title = serializers.CharField(source='song.title', read_only=True)
    artist_name = serializers.CharField(source='song.album.artist.name', read_only=True)
    album_title = serializers.CharField(source='song.album.title', read_only=True)
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Scrobble
        fields = '__all__'
        read_only_fields = ('usuario',)
