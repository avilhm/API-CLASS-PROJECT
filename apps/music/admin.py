from django.contrib import admin
from apps.music.models import (
    Genre,
    Artist,
    Album,
    Track,
    Playlist,
    PlaylistTrack
)

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)
# Register your models here.
