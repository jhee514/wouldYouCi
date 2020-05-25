from django.db.models import Q
from haversine import haversine
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Cinema
from .serializers import SimpleCinemaSerializer

# SELECT name,
# 	(6371*acos(cos(radians(37.5611326))*cos(radians(cinema.y))*cos(radians(cinema.x)
# 	-radians(127.033311))+sin(radians(37.5611326))*sin(radians(cinema.y))))
# 	AS distance
# FROM wouldyouci.movies_cinema AS cinema
# HAVING distance <= 1
# ORDER BY distance
# LIMIT 0,10

# x = 127.033311 = 'longitude' = '경도'
# y = 37.5611326 = 'latitude' = '위도'
# longitude = float(request.GET.get('longitude', None))
# latitude = float(request.GET.get('latitude', None))
@api_view(['GET'])
@permission_classes([AllowAny])
def get_cinema(request):
    x = float(request.query_params.get('x'))
    y = float(request.query_params.get('y'))
    radius = request.query_params.get('radius')
    radius = int(radius) if radius else 1
    # x = 127.033311
    # y = 37.5611326
    # radius = 1

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


