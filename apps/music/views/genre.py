from rest_framework.viewsets import ModelViewSet
from apps.music.models import Genre
from apps.music.serializers.genre import GenreSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
