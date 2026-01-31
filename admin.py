from django.contrib import admin
from .models import Movie, Series, Episode

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'release_year', 'rating', 'views')
    search_fields = ('title', 'description')
    list_filter = ('country', 'release_year', 'category')
    ordering = ('-release_year',)
    readonly_fields = ('views',)
    
@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'country', 'category')
    search_fields = ('title',)
    list_filter = ('country', 'category')
    inlines = [EpisodeInline]
    
@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'series', 'season_number', 'episode_number')
    list_filter = ('season_number',)
    ordering = ('series', 'season_number', 'episode_number')