from django.db import models
from django.utils import timezone

class Review(models.Model):
    author = models.CharField(max_length=200)
    film = models.CharField(max_length=200)
    text = models.TextField()
    rate = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.film + " - " + self.author
