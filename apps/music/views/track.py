from rest_framework.viewsets import ModelViewSet
from apps.music.models import Track
from apps.music.serializers.track import TrackSerializer

class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
