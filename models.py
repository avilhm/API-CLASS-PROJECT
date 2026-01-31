from django.db import models
from categories.models import Category
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='series')
    
class Episode(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    season_number = models.IntegerField()
    episode_number = models.IntegerField()