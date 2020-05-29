from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from movies.serializers import SimpleMovieSerializer
from movies.models import Movie
from elasticsearch import Elasticsearch
from .documents import MoviesDocument
import json


@api_view(['GET'])
@permission_classes([AllowAny])
def autocomplete_movie(request):
    words = request.query_params.get('words')

    if not words:
        return Response(status=203, data=[])

    movies = Movie.objects.filter(name__startswith=words[0])

    for w in words:
        movies = movies.filter(name__contains=w)

    results = movies.values_list('name', flat=True).distinct()

    return Response(status=200, data=results[:10])


@api_view(['GET'])
@permission_classes([AllowAny])
def search_movie(request, words):

    s4 = MoviesDocument.search().query({
        "bool": {
            "should": [
                {"match": {"name": {"query": words, "boost": 20}}},
                {"match": {"summary": {"query": words}}},
            ]
        }
    })

    id_set = [hit.id for hit in s4]

    search_movies = []
    for _id in id_set:
        movie = Movie.objects.get(id=_id)
        serializer = SimpleMovieSerializer(movie)
        search_movies.append(serializer.data)

    sim_movies = Movie.objects.exclude(id__in=id_set).filter(name__startswith=words[0])

    for w in words:
        sim_movies = sim_movies.filter(name__contains=w)

    sim_serializer = SimpleMovieSerializer(sim_movies, many=True)


    dataset = {
        'meta': {
            'search_result': len(id_set),
            'similar_result': sim_movies.count()
        },
        'search_result': search_movies,
        'similar_result': sim_serializer.data
    }

    return Response(status=200, data=dataset)

