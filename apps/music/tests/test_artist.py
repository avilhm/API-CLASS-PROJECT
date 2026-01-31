import pytest
from rest_framework.test import APIClient
from apps.music.models import Artist

@pytest.mark.django_db
def test_create_artist_model():
    artist = Artist.objects.create(name="The Beatles", country="UK")
    
    assert artist.id is not None
    assert artist.name == "The Beatles"
    assert artist.country == "UK"

@pytest.mark.django_db
def test_artist_api_list():
    Artist.objects.create(name="Nirvana")
    Artist.objects.create(name="Radiohead")

    client = APIClient()
    response = client.get("/api/artists/")
    
    assert response.status_code == 200
    data = response.json()
    assert any(artist["name"] == "Nirvana" for artist in data)
