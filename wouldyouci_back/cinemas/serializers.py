from rest_framework import serializers
from .models import Cinema
from accounts.serializers import SimpleCinemaRatingSerializer
from movies.serializers import OnscreenSerializer


class SimpleCinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id', 'name', 'type', 'img', 'address', 'tel', 'x', 'y', 'url')


class CinemaSerializer(serializers.ModelSerializer):
    onscreens = OnscreenSerializer(many=True, read_only=True)
    cinema_ratings = SimpleCinemaRatingSerializer(many=True, read_only=True)

    class Meta:
        model = Cinema
        fields = ('id', 'name', 'type', 'img', 'address', 'url', 'tel',
                  'public', 'parking', 'onscreens', 'score', 'cinema_ratings')


class SearchCinemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cinema
        fields = ('id', 'name', 'address', 'type', 'img')
