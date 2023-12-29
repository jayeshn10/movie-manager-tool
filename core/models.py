from django.db import models

# Create your models here.
class Movie(models.Model):
    TYPE_CHOICES = ( 
        ("action", "Action"), 
        ("drama", "Drama"),
        ("comedy", "Comedy"),
        ("sifi", "Si-Fi"),
        ("adventure", "Adventure"),
        ("horror", "Horror"),
        ("romance", "Romance"),
        ("family", "Family"),
        ("animation", "Animation"),
        ("documentary", "Documentary")
    )
    RATING_CHOICES = ( 
        ("g", "G"), 
        ("pg", "PG"),
        ("pg-13", "PG-13"),
        ("r", "R"),
        ("nc-17", "NC-17"),
        ("unrated", "Unrated"),
    )
    title = models.CharField(max_length=255)
    type = models.CharField(  max_length = 20, choices = TYPE_CHOICES)
    director = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    rating = models.CharField(  max_length = 20, choices = RATING_CHOICES) 