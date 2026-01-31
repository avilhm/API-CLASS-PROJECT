from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeriesViewSet, EpisodeViewSet
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'episodes', EpisodeViewSet)
urlpatterns = router.urls