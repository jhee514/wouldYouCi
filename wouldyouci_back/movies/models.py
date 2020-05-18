from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Genre(models.Model):
    genre = models.CharField(max_length=150)


class People(models.Model):
    name = models.CharField(max_length=50)
    # 일단 넣어는 놨는디 뺄까?
    name_eng = models.CharField(max_length=50)
    role = models.CharField(max_length=50)


class Movie(models.Model):
    name = models.CharField(max_length=150)
    name_eng = models.CharField(max_length=150, blank=True, null=True)
    watch_grade = models.CharField(max_length=150)
    running_time = models.CharField(max_length=50)
    summary = models.TextField()
    open_date = models.DateField()

    trailer = models.CharField(max_length=200, blank=True, null=True)
    poster = models.CharField(max_length=200, blank=True, null=True)

    director = models.ForeignKey(People, on_delete=models.CASCADE, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movie_genres')
    actors = models.ManyToManyField(People, related_name='movie_actors')
