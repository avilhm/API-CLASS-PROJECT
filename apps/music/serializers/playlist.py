from rest_framework import serializers
from apps.music.models import Playlist

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"
