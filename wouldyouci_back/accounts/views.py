from django.db.models import Count
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import os
from wouldyouci_back.settings import MEDIA_ROOT
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from movies.models import Movie
from movies.serializers import TasteMovieSerializer
from .models import Profile
from .serializers import UserCreationSerializer, UserDetailSerializer, \
    ProfileSerializer, RatingSerializer, RatingPosterSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    if request.method == 'POST':
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(status=200, data={'message': '회원가입 되었습니다.'})

        return Response(status=400, data={'message': serializer.errors})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_rating_tf(request):
    user = request.user
    if user.ratings.count() > 9:
        data = {'rating_tf': True, 'rating_cnt': user.ratings.count()}
    else:
        data = {'rating_tf': False, 'rating_cnt': user.ratings.count()}
    return Response(status=200, data=data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_index(request):
    # TODO
    user = get_object_or_404(User, id=request.user.id)
    serializer = UserDetailSerializer(user)

    recommend_movies = []
    maybe_likes_willscreen = []

    return Response(status=200, data=serializer.data)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def change_profile(request):
    user = request.user
    if user.file.exists():
        profile = Profile.objects.get(user=user.id)
        os.remove(os.path.join(MEDIA_ROOT, f"{profile.file}"))
        profile.delete()
    if request.method == 'POST':
        if request.FILES:
            serializer = ProfileSerializer(request.POST, request.FILES)
            if serializer.is_valid():
                profile = serializer.create(serializer.validated_data)
                profile.user_id = user.id
                profile.save()
                return Response(status=200, data={'file': f"media/{profile.file}"})
            return Response(status=400, data={'message': '유효하지 않은 파일입니다.'})
        return Response(status=403, data={'message': '이미지는 필수입니다.'})
    elif request.method == 'DELETE':
        return Response(status=204)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = get_object_or_404(User, id=request.user.id)
    new_password = request.data.get('new_password')

    if not new_password:
        return Response(status=400, data={'message': '필수 데이터가 누락되었습니다.'})

    user.set_password(new_password)
    user.save()
    return Response(status=203)


class SmallPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50


class TasteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TasteMovieSerializer
    pagination_class = SmallPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        id_set = [21, 25, 29, 9]
        rated_id = user.ratings.values_list('movie', flat=True)
        queryset = (
            Movie.objects
                .exclude(id__in=rated_id)
                .exclude(genres__in=id_set)
                .exclude(watch_grade='청소년 관람불가')
                .filter(open_date__gte='2015')
                .annotate(num_rating=Count('ratings'))
                .order_by('-num_rating', '-score')
        )
        return queryset


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_create_dummy_rating(request):
    user = request.user
    if request.method == 'GET':
        ratings = user.ratings.all()
        serializer = RatingPosterSerializer(ratings, many=True)
        return Response(status=200, data=serializer.data)

    elif request.method == 'POST':
        for data in request.data['data']:
            if user.ratings.filter(movie=data['movie']).exists():
                continue

            serializer = RatingSerializer(data=data)
            if serializer.is_valid():
                new_rating = serializer.save(user=user)
                movie = new_rating.movie
                ratings_count = movie.ratings.count()
                movie_rating = movie.score * (ratings_count - 1)
                movie_rating = (movie_rating + new_rating.score) / ratings_count
                movie.score = movie_rating
                movie.save()
            else:
                return Response(status=400, data=serializer.errors)

        return Response(status=203)
