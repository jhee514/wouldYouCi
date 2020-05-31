from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Movie, Onscreen
from accounts.serializers import RatingSerializer, SimpleRatingSerializer
from accounts.models import Rating
from .serializers import MovieSerializer
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg
from django.contrib.auth import get_user_model
User = get_user_model()
# import pandas as pd
# from sklearn.linear_model import Lasso
# import pymysql
# from sklearn.model_selection import RandomizedSearchCV
# from scipy.stats import uniform as sp_rand
# from wouldyouci_back.settings import BASE_DIR
# import os
#
#
# def contentsbased(user_id):
#     # conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
#     # sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
#     # ratings = pd.read_sql_query(sql, conn)
#     genres = pd.read_pickle(os.path.join(BASE_DIR, 'movies', 'genre_train.p'))
#
#     rating_test = Rating.objects.filter(user=user_id).values_list('score', flat=True)
#     print(rating_test)
#     rating_test = list(rating_test)
#
#     # test = pd.read_sql_query(rating_test)
#     # print(ratings)
#
#     # conn.close()
#
#     user_profile = rating_test.merge(genres, left_on='movie_id', right_index=True)
#     print(user_profile)
#     model = Lasso()
#     param_grid = {'alpha': sp_rand()}
#
#     research = RandomizedSearchCV(estimator=model,
#                                   param_distributions=param_grid,
#                                   n_iter=50,
#                                   cv=5,
#                                   random_state=406)
#
#     research.fit(user_profile[genres.columns], user_profile['score'])
#
#     predictions = research.best_estimator_.predict(genres)
#     genres.reset_index()
#
#     genres['predict'] = predictions
#
#     a = pd.DataFrame.to_json(genres['predict'])
#     print(a)
#     return pd.DataFrame.to_json(genres['predict'])


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


@permission_classes([IsAuthenticated])
class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SimpleRatingSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie', 0)
        movie = get_object_or_404(Movie, id=movie_id)
        queryset = (
            movie.ratings.filter(comment__isnull=False)
        )
        return queryset


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie)
    # contentsbased(9000006)

    paginator = Paginator(movie.ratings.all(), 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    ratings = SimpleRatingSerializer(page_obj.object_list, many=True)

    # datasets = {
    #     'meta': {
    #         # 'page': paginator.page_range
    #     },
    #     'documets': {
    #         'is_showing': Onscreen.objects.filter(movie=movie_id).exists(),
    #         'movie': serializer.data,
    #         'ratings': ratings.data,
    #
    #     }
    # }
    datasets = {
        'is_showing': Onscreen.objects.filter(movie=movie_id).exists(),
        'ratings': ratings.data,
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
    user = request.user
    if user.ratings.filter(movie=request.data['movie']).exists():
        return Response(status=403, data={'message': '이미 평가한 영화입니다.'})

    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        new_rating = serializer.save(user=user)

        movie = new_rating.movie
        ratings_count = movie.ratings.count()
        movie_rating = movie.score * (ratings_count - 1)
        movie_rating = (movie_rating + new_rating.score) / ratings_count
        movie.score = movie_rating
        movie.save()

        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)


@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def patch_delete_rating(request, rating_id):
    # user_id = 9000000
    rating = get_object_or_404(Rating, id=rating_id)
    origin_score = rating.score
    movie = rating.movie
    ratings_count = movie.ratings.count()
    movie_rating = movie.score * ratings_count - origin_score

    if rating.user.id == request.user.id:
        if request.method == 'PATCH':
            serializer = RatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid():
                update_rating = serializer.save()

                movie_rating = (movie_rating + update_rating.score) / ratings_count
                movie.score = movie_rating
                movie.save()

                return Response(serializer.data)
            return Response(status=400, data=serializer.errors)

        elif request.method == 'DELETE':
            rating.delete()

            if ratings_count - 1:
                movie_rating = movie_rating / (ratings_count - 1)
            else:
                movie_rating = 0

            movie.score = movie_rating
            movie.save()

            return Response(status=204)

    return Response(status=400, data={'message': '권한이 없습니다.'})
