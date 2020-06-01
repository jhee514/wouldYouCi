from rest_framework import serializers
from .models import Movie, Onscreen
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

    class Meta:
        model = Movie
        fields = ('id', 'score', 'name', 'name_eng', 'watch_grade', 'running_time', 'summary',
                  'open_date', 'trailer', 'poster', 'directors', 'genres', 'actors')


class TasteMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'name', 'poster')



class SimpleMovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Movie
        fields = ('id', 'name', 'poster', 'genres', 'running_time', 'watch_grade')


class SearchMovieSerializer(serializers.ModelSerializer):
    ratings_count = serializers.IntegerField(
        source='ratings.count',
        read_only=True
    )

    class Meta:
        model = Movie
        fields = ('id', 'name', 'name_eng', 'poster', 'watch_grade', 'score', 'ratings_count')


class SoonMovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    pick_users_count = serializers.IntegerField(
        source='pick_users.count',
        read_only=True
    )
    directors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Movie
        fields = ('id', 'name', 'poster', 'open_date', 'running_time', 'pick_users_count',
                  'genres', 'directors', 'actors')



class OnscreenSerializer(serializers.ModelSerializer):
    movie = SimpleMovieSerializer(read_only=True)

    class Meta:
        model = Onscreen
        fields = ('movie', 'info', 'date', 'start_time', 'end_time', 'total_seats', 'seats', 'url')
