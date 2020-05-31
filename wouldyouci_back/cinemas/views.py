from django.db.models import Q
from haversine import haversine
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from movies.models import Onscreen
from movies.serializers import OnscreenSerializer
from .models import Cinema
from .serializers import SimpleCinemaSerializer, CinemaSerializer
from accounts.models import CinemaRating
from accounts.serializers import CinemaRatingSerializer
from django.contrib.auth import get_user_model

from accounts.serializers import SimpleCinemaRatingSerializer

User = get_user_model()
import datetime


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cinema_width(request):
    x1 = float(request.query_params.get('x1'))
    x2 = float(request.query_params.get('x2'))
    y1 = float(request.query_params.get('y1'))
    y2 = float(request.query_params.get('y2'))

    if not x1 or not x2 or not y1 or not y2:
        return Response(status=400, data={'message': 'x, y 값은 필수입니다.'})

    cinemas = Cinema.objects.filter(y__gte=y1,
                                    y__lte=y2,
                                    x__gte=x1,
                                    x__lte=x2
                                    )

    serializer = SimpleCinemaSerializer(cinemas, many=True)

    datasets = {
        'meta': {
            'total': cinemas.count()
        },
        'documents': serializer.data
    }

    return Response(status=200, data=datasets, content_type='application.json')


@api_view(['GET'])
@permission_classes([AllowAny])
def get_fast_movie(request, cinema_id):
    date = datetime.date.today()
    start_time = request.query_params.get('start_time')
    start_time = start_time if start_time else datetime.datetime.now().time()

    onscreen = Onscreen.objects.filter(cinema=cinema_id,
                                       date=date,
                                       start_time__gte=start_time)

    serializer = OnscreenSerializer(onscreen, many=True)

    datasets = {
        'meta': {
            'total': onscreen.count()
        },
        'documents': serializer.data
    }

    return Response(status=200, data=datasets, content_type='application.json')



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cinema_detail(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    serializer = CinemaSerializer(cinema)
    return Response(status=200, data=serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def pick_cinema(request, cinema_id):
    # user = get_object_or_404(User, id=9000000)
    user = request.user
    cinema = get_object_or_404(Cinema, id=cinema_id)
    if cinema.pick_users.filter(id=user.id).exists():
        cinema.pick_users.remove(user)
        return Response(status=200, data={"pick_cinemas": False})
    else:
        cinema.pick_users.add(user)
        return Response(status=200, data={"pick_cinemas": True})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_cinema_rating(request):
    # user = get_object_or_404(User, id=9000000)
    # cinema_id = request.data.get('cinema_id')
    serializer = CinemaRatingSerializer(data=request.data)
    if serializer.is_valid():
        new_rating = serializer.save(user=request.user)
        # serializer.save(user=user)

        cinema = new_rating.cinema
        ratings_count = cinema.cinema_ratings.count()
        cinema_rating = cinema.score * (ratings_count - 1)
        cinema_rating = (cinema_rating + new_rating.score) / ratings_count
        cinema.score = cinema_rating
        cinema.save()

        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)


@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def patch_delete_cinema_rating(request, rating_id):
    # user_id = 9000000
    rating = get_object_or_404(CinemaRating, id=rating_id)
    origin_score = rating.score
    cinema = rating.cinema
    ratings_count = cinema.cinema_ratings.count()
    cinema_rating = cinema.score * ratings_count - origin_score

    if rating.user.id == request.user.id:
        if request.method == 'PATCH':
            serializer = CinemaRatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid():
                update_rating = serializer.save()

                cinema_rating = (cinema_rating + update_rating.score) / ratings_count
                cinema.score = cinema_rating
                cinema.save()

                return Response(serializer.data)
            return Response(status=400, data=serializer.errors)

        elif request.method == 'DELETE':
            rating.delete()

            if ratings_count - 1:
                cinema_rating = cinema_rating / (ratings_count - 1)
            else:
                cinema_rating = 0

            cinema.score = cinema_rating
            cinema.save()

            return Response(status=204)

    return Response(status=400, data={'message': '권한이 없습니다.'})


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


@permission_classes([AllowAny])
class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SimpleCinemaRatingSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        cinema_id = self.request.query_params.get('cinema', 0)
        cinema = get_object_or_404(Cinema, id=cinema_id)
        queryset = (
            cinema.cinema_ratings.all()
        )
        return queryset
