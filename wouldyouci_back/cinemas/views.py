from django.db.models import Q
from haversine import haversine
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from movies.models import Onscreen
from movies.serializers import OnscreenSerializer
from .models import Cinema
from .serializers import SimpleCinemaSerializer
import datetime


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cinema(request):
    x = float(request.query_params.get('x'))
    y = float(request.query_params.get('y'))
    radius = request.query_params.get('radius')
    radius = int(radius) if radius else 1

    if not x or not y:
        return Response(status=400, data={'message': 'x, y 값은 필수입니다.'})

    position = (y, x)
    condition = (
            Q(y__range=(y - 0.005*radius, y + 0.005*radius)) |
            Q(x__range=(x - 0.008*radius, x + 0.008*radius))
    )

    cinema_infos = (
        Cinema.objects.filter(condition)
    )

    near_cinema = [cinema for cinema in cinema_infos
                   if haversine(position, (float(cinema.y), float(cinema.x))) <= radius]

    serializer = SimpleCinemaSerializer(near_cinema, many=True)

    datasets = {
        'meta': {
            'total': len(near_cinema)
        },
        'documents': serializer.data
    }

    return Response(status=200, data=datasets, content_type='application.json')


@api_view(['GET'])
@permission_classes([AllowAny])
def get_fast_movie(request, cinema_id):
    date = request.query_params.get('date')
    date = date if date else datetime.date.today()
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
