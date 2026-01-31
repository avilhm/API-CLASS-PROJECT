import pytest
from rest_framework.test import APIClient
from apps.music.models import Playlist, Artist, Track, PlaylistTrack

@pytest.mark.django_db
def test_create_playlist_model():
    playlist = Playlist.objects.create(name="My Favorites", description="Best songs ever")
    
    assert playlist.id is not None
    assert playlist.name == "My Favorites"

@pytest.mark.django_db
def test_add_track_to_playlist():
    artist = Artist.objects.create(name="Taylor Swift")
    track = Track.objects.create(
        title="Love Story",
        artist=artist,
        duration_seconds=230,
        stream_url="https://cdn.test/lovestory.mp3"
    )
    playlist = Playlist.objects.create(name="Chill Hits")

    playlist_track = PlaylistTrack.objects.create(playlist=playlist, track=track)
    
    assert playlist_track.playlist == playlist
    assert playlist_track.track == track

@pytest.mark.django_db
def test_playlist_api_list():
    Playlist.objects.create(name="Workout Mix")
    client = APIClient()
    response = client.get("/api/playlists/")
    
    assert response.status_code == 200
    data = response.json()
    assert any(pl["name"] == "Workout Mix" for pl in data)
