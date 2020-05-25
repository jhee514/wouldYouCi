from rest_framework import serializers
from .models import Movie
from accounts.models import Rating
from accounts.serializers import RatingSerializer
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
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'name_eng', 'watch_grade', 'running_time', 'summary',
                  'open_date', 'trailer', 'poster', 'directors', 'genres', 'actors', 'ratings']

