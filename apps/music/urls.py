from django.urls import path
from .views.artist import ArtistViewSet
from .views.album import AlbumViewSet
from .views.track import TrackViewSet
from .views.genre import GenreViewSet
from .views.playlist import PlaylistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'playlists', PlaylistViewSet)

urlpatterns = router.urls
