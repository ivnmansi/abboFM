from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Artist, Album, Song, Scrobble, User
from .serializers import UserSerializer, ArtistSerializer, AlbumSerializer, SongSerializer, ScrobbleSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'date_joined': request.user.date_joined,
        'total_scrobbles': request.user.total_scrobbles
    })

"""
    view users
"""
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.query_params.get('user', None)

        if user is not None:
            queryset = queryset.filter(username=user)
        
        return queryset

"""
    view artists, albums, songs, and scrobbles
"""
class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ScrobblesViewSet(viewsets.ModelViewSet):
    serializer_class = ScrobbleSerializer

    def get_queryset(self):
        queryset = Scrobble.objects.all()
        user = self.request.query_params.get('user', None)

        if user is None:
            queryset = queryset.filter(user=self.request.user)

        elif user:
            queryset = queryset.filter(user=user)
        
        return queryset

    def create(self, request, *args, **kwargs):
        song = request.data.get('song')
        artist = request.data.get('artist')
        album = request.data.get('album')

        artist, _ = Artist.objects.get_or_create(name=artist)
        album, _ = Album.objects.get_or_create(title=album, artist=artist)
        song, _ = Song.objects.get_or_create(title=song, album=album)
        User.objects.filter(id=request.user.id).update(total_scrobbles= User.objects.get(id=request.user.id).total_scrobbles + 1)

        scrobble = Scrobble.objects.create(user=request.user, song=song)

        scrobble.refresh_from_db()

        serializer = self.get_serializer(scrobble)

        return Response(serializer.data, status=status.HTTP_201_CREATED)