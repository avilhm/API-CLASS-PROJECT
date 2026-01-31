from rest_framework.viewsets import ModelViewSet
from apps.music.models import Artist
from apps.music.serializers.artist import ArtistSerializer

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
