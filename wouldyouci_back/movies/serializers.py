from rest_framework import serializers
from .models import Movie
from accounts.models import Rating
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
        fields = '__all__'

