from django.db import models
from .artist import Artist
from .album import Album
from .genre import Genre

class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="tracks"
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tracks"
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tracks"
    )
    duration_seconds = models.PositiveIntegerField()
    stream_url = models.URLField()
    bitrate = models.PositiveIntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
