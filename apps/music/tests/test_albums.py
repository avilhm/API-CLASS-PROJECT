import pytest
from rest_framework.test import APIClient
from apps.music.models import Artist, Album

@pytest.mark.django_db
def test_create_album_model():
    artist = Artist.objects.create(name="Pink Floyd")
    album = Album.objects.create(title="The Dark Side of the Moon", artist=artist)
    
    assert album.id is not None
    assert album.title == "The Dark Side of the Moon"
    assert album.artist == artist

@pytest.mark.django_db
def test_album_api_list():
    artist = Artist.objects.create(name="Queen")
    Album.objects.create(title="A Night at the Opera", artist=artist)

    client = APIClient()
    response = client.get("/api/albums/")
    
    assert response.status_code == 200
    data = response.json()
    assert any(album["title"] == "A Night at the Opera" for album in data)
