from django.db import models
from .playlist import Playlist
from .track import Track

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.CASCADE,
        related_name="playlist_tracks"
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("playlist", "track")
