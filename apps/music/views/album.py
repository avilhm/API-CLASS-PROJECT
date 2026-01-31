from rest_framework.viewsets import ModelViewSet
from apps.music.models import Album
from apps.music.serializers.album import AlbumSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
