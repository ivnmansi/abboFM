from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action
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

    """
        Get the queryset for the scrobbles viewset
    """
    def get_queryset(self):
        queryset = Scrobble.objects.all()
        user = self.request.query_params.get('user', None)

        if user is None:
            queryset = queryset.filter(user=self.request.user)

        elif user:
            queryset = queryset.filter(user=user)
        
        return queryset.order_by('-id')

    """
        Get the last scrobble for the current user
    """
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def last(self, request):
        last_scrobble = self.get_queryset().first()

        if last_scrobble:
            serializer = self.get_serializer(last_scrobble)
            return Response(serializer.data)

        return Response({"detail": "No scrobbles found."}, status=status.HTTP_404_NOT_FOUND)

    """
        Create a new scrobble for the current user
    """
    def create(self, request, *args, **kwargs):
        title = request.data.get('title') or request.data.get('song_title')
        artist_name = request.data.get('artist') or request.data.get('artist_name')
        album_title = request.data.get('album') or request.data.get('album_title') or "Sin Álbum"

        if not title or not artist_name:
            return Response(
                {"detail": "Missing required fields: title and artist_name are required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        artist_obj, _ = Artist.objects.get_or_create(name=artist_name)
        album_obj, _ = Album.objects.get_or_create(title=album_title, artist=artist_obj)
        song_obj, _ = Song.objects.get_or_create(title=title, album=album_obj)
        
        user = request.user
        user.total_scrobbles += 1
        user.save(update_fields=['total_scrobbles'])

        scrobble = Scrobble.objects.create(user=user, song=song_obj)
        serializer = self.get_serializer(scrobble)

        return Response(serializer.data, status=status.HTTP_201_CREATED)