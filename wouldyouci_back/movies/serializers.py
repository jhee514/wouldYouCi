from rest_framework import serializers
from .models import Movie, Onscreen
from accounts.serializers import SimpleRatingSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class MovieSerializer(serializers.ModelSerializer):
    directors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    ratings = SimpleRatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'name_eng', 'watch_grade', 'running_time', 'summary',
                  'open_date', 'trailer', 'poster', 'directors', 'genres', 'actors', 'ratings']



class SimpleMovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Movie
        fields = ('id', 'name', 'poster', 'genres', 'running_time', 'watch_grade')



class OnscreenSerializer(serializers.ModelSerializer):
    movie = SimpleMovieSerializer(read_only=True)

    class Meta:
        model = Onscreen
        fields = ('movie', 'info', 'date', 'start_time', 'end_time', 'total_seats', 'seats', 'url')
