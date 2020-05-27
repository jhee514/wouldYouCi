from django.db import models
from cinemas.models import Cinema


class Genre(models.Model):
    name = models.CharField(max_length=150)


class People(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    name = models.CharField(max_length=150)
    name_eng = models.CharField(max_length=150, blank=True, null=True)
    watch_grade = models.CharField(max_length=150)
    running_time = models.CharField(max_length=50)
    summary = models.TextField()
    open_date = models.DateField()

    trailer = models.CharField(max_length=200, blank=True, null=True)
    poster = models.CharField(max_length=200, blank=True, null=True)

    directors = models.ManyToManyField(People, related_name='movie_directors')
    genres = models.ManyToManyField(Genre, related_name='movie_genres')
    actors = models.ManyToManyField(People, related_name='movie_actors')


class Onscreen(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='onscreens')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='onscreens')
    info = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False, auto_now=False)
    start_time = models.TimeField(auto_now_add=False, auto_now=False)
    end_time = models.TimeField(auto_now_add=False, auto_now=False)
    total_seats = models.CharField(max_length=5)
    seats = models.CharField(max_length=5)
    url = models.URLField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ('start_time',)
