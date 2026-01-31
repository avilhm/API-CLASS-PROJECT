import pytest
from rest_framework.test import APIClient
from apps.music.models import Artist, Track

@pytest.mark.django_db
def test_create_track_model():
    artist = Artist.objects.create(name="Ed Sheeran")
    track = Track.objects.create(
        title="Shape of You",
        artist=artist,
        duration_seconds=240,
        stream_url="https://cdn.test/shapeofyou.mp3"
    )

    assert track.id is not None
    assert track.title == "Shape of You"
    assert track.artist == artist

@pytest.mark.django_db
def test_track_api_list():
    artist = Artist.objects.create(name="Adele")
    Track.objects.create(
        title="Hello",
        artist=artist,
        duration_seconds=295,
        stream_url="https://cdn.test/hello.mp3"
    )

    client = APIClient()
    response = client.get("/api/tracks/")
    
    assert response.status_code == 200
    data = response.json()
    assert any(track["title"] == "Hello" for track in data)

@pytest.mark.django_db
def test_create_track_via_api():
    artist = Artist.objects.create(name="Coldplay")
    client = APIClient()

    response = client.post(
        "/api/tracks/",
        {
            "title": "Yellow",
            "artist": artist.id,
            "duration_seconds": 260,
            "stream_url": "https://cdn.test/yellow.mp3"
        },
        format="json"
    )
    
    assert response.status_code == 201
    assert response.json()["title"] == "Yellow"
