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

class Cinema(models.Model):
    region = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20)
    tel = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=50)
    x = models.CharField(max_length=50)
    y = models.CharField(max_length=50)
    url = models.URLField(max_length=250)
    public = models.TextField(blank=True, null=True)
    parking = models.TextField(blank=True, null=True)
    type = models.CharField(default='기타')
    img = models.URLField(max_length=250, blank=True, null=True)

class Onscreen(models.Model) :
    # movie = models.ManyToManyField(Movie)
    # cinema = models.ManyToManyField(Cinema)
    date = models.DateField()
    start_time : models.CharField(max_length=10)
    end_time: models.CharField(max_length=10)
    total_seats: models.CharField(max_length=5)
    seats: models.CharField(max_length=5)
    url : models.URLField(max_length=250, blank=True, null=True)
