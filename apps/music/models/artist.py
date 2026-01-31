from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
