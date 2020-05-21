from django.db import models
# from accounts.models import Rating
# from django.contrib.auth import get_user_model
# User = get_user_model()


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

    # ratings = models.ManyToManyField(User, through='Rating')
