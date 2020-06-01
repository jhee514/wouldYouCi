from rest_framework import serializers
from .models import Rating, Profile, CinemaRating
from movies.serializers import TasteMovieSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'get_agreement', 'email')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class UserDetailSerializer(serializers.ModelSerializer):
    file = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'file', 'pick_movies', 'pick_cinemas')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('file',)


class RatingSerializer(serializers.ModelSerializer):
    score = serializers.FloatField(required=True, min_value=0.5, max_value=5)

    class Meta:
        model = Rating
        fields = ('id', 'comment', 'movie', 'score', 'created_at', 'updated_at')


class SimpleRatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'comment', 'score', 'updated_at', 'user')


class RatingPosterSerializer(serializers.ModelSerializer):
    movie = TasteMovieSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'movie', 'score')


class CinemaRatingSerializer(serializers.ModelSerializer):
    score = serializers.FloatField(required=True, min_value=0.5, max_value=5)

    class Meta:
        model = CinemaRating
        fields = ('id', 'comment', 'cinema', 'score', 'created_at', 'updated_at')


class SimpleCinemaRatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CinemaRating
        fields = ('id', 'comment', 'score', 'updated_at', 'user')
