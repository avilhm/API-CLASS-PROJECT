from django.db import models
from .artist import Artist

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="albums"
    )
    release_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='album_covers/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
