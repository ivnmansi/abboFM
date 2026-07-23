from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'artists', views.ArtistsViewSet)
router.register(r'albums', views.AlbumsViewSet)
router.register(r'songs', views.SongsViewSet)
router.register(r'scrobbles', views.ScrobblesViewSet, basename='scrobble'  )

urlpatterns = [
    path('user/', views.current_user, name='current_user'),
    path('', include(router.urls)),
]