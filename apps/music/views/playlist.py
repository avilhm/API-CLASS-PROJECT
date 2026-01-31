from rest_framework.viewsets import ModelViewSet
from apps.music.models import Playlist
from apps.music.serializers.playlist import PlaylistSerializer

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
