from django.db.models import Q
from haversine import haversine
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
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
    serializer = CinemaRatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        # serializer.save(user=user)
        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)


@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def patch_delete_cinema_rating(request, rating_id):
    # user_id = 9000000
    rating = get_object_or_404(CinemaRating, id=rating_id)
    if rating.user.id == request.user.id:
    # if rating.user.id == request.user.id:
        if request.method == 'PATCH':
            serializer = CinemaRatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=400, data=serializer.errors)

        elif request.method == 'DELETE':
            rating.delete()
            return Response(status=204)

    return Response(status=400, data={'message': '권한이 없습니다.'})
