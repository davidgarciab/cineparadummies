from django.db import models
from django.utils import timezone

class Film(models.Model):
    name = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=1,decimal_places=1, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.CharField(max_length=200)
    film = models.ForeignKey(Film)
    text = models.TextField()
    rate = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.film.name + " - " + self.author
