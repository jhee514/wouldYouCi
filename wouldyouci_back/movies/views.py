from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Movie, Onscreen
from accounts.serializers import RatingSerializer
from accounts.models import Rating
from .serializers import MovieSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie)

    datasets = {
        "is_showing": Onscreen.objects.filter(movie=movie_id).exists(),
    }
    datasets.update(serializer.data)

    return Response(status=200, data=datasets)



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def pick_movie(request, movie_id):
    # user = get_object_or_404(User, id=9000000)
    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)
    if movie.pick_users.filter(id=user.id).exists():
        movie.pick_users.remove(user)
        return Response(status=200, data={"pick_movies": False})
    else:
        movie.pick_users.add(user)
        return Response(status=200, data={"pick_movies": True})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_rating(request):
    # user = get_object_or_404(User, id=9000000)
    # print(request.body)
    # print(request.data)
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)


@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def patch_delete_rating(request, rating_id):
    # user_id = 9000001
    rating = get_object_or_404(Rating, id=rating_id)
    if rating.user.id == request.user.id:
        if request.method == 'PATCH':
            serializer = RatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=400, data=serializer.errors)

        elif request.method == 'DELETE':
            rating.delete()
            return Response(status=204)

    return Response(status=400, data={'message': '권한이 없습니다.'})
