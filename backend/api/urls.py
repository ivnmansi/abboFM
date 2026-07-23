from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'artists', views.ArtistsViewSet)
router.register(r'albums', views.AlbumsViewSet)
router.register(r'songs', views.SongsViewSet)
router.register(r'scrobbles', views.ScrobblesViewSet, basename='scrobble'  )

urlpatterns = [
    path('', include(router.urls)),
]