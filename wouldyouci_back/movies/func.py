import os
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import uniform as sp_rand
from django.conf import settings
from django.core.cache import cache
from .apps import MoviesConfig
from .models import Movie
from accounts.models import Rating
from django.contrib.auth import get_user_model
User = get_user_model()


def recommend_userbased(user_id):
    path = os.path.join(settings.BASE_DIR, 'utils', 'KNN.p')
    df = pd.read_pickle(path)
    movie_list = df.loc[df['user_id'] == user_id, 'movie_id'].unique()

    return movie_list[:10]


def contentsbased_onscreen(user_id):
    genres = MoviesConfig.genres

    ratings = pd.DataFrame(list(Rating.objects.filter(user=user_id).values('score', 'movie_id')))

    user_profile = ratings.merge(genres, left_on='movie_id', right_index=True)

    model = Lasso()
    param_grid = {'alpha': sp_rand()}

    research = RandomizedSearchCV(estimator=model,
                                  param_distributions=param_grid,
                                  n_iter=30,
                                  cv=5,
                                  random_state=406)

    research.fit(user_profile[genres.columns], user_profile['score'])

    predictions = research.best_estimator_.predict(genres)
    genres.reset_index()

    genres['predict'] = predictions

    onscreen_id_set = Movie.objects.exclude(onscreens=None).exclude(genres=None)
    onscreen_id_set = onscreen_id_set.values_list('id', flat=True)

    score_info = []

    for _id in onscreen_id_set:
        try:
            score_info.append((_id, genres.at[_id, 'predict']))
        except KeyError:
            print('{}가 피클파일에 없어요. 피클을 업데이트 해야합니다.'.format(_id))

    score_info = sorted(score_info, key=lambda x: -x[1])[:10]
    onscreen_id_set = [x for x, y in score_info]

    return onscreen_id_set


def contentsbased_by_genres_and_directors(user_id, movie_id):
    data = cache.get(f'recommend_{user_id}')

    if data is None:
        movies = MoviesConfig.movies

        ratings = pd.DataFrame(list(Rating.objects.filter(user=user_id).values('score', 'movie_id')))
        ratings = ratings.merge(movies, left_on='movie_id', right_index=True)
        x_train, x_test, y_train, y_test = train_test_split(ratings[movies.columns],
                                                            ratings['score'],
                                                            random_state=406,
                                                            test_size=0.1)
        reg = LinearRegression()
        reg.fit(x_train, y_train)

        predictions = reg.predict(movies)
        movies.reset_index()

        movies['predict'] = predictions
        data = movies[['predict']]

        cache.set(f'recommend_{user_id}', data)

    predicted_score = data.at[movie_id, 'predict']

    predicted_score = predicted_score - 0.2
    if predicted_score >= 5.0:
        predicted_score = 4.9

    if predicted_score < 0:
        predicted_score = 0.1

    return round(predicted_score * 20, 1)
