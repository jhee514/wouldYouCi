from django.apps import AppConfig
from django.conf import settings
import os
import pandas as pd


class MoviesConfig(AppConfig):
    name = 'movies'

    movie_path = os.path.join(settings.BASE_DIR, 'utils', 'movie_director_train.p')
    genre_path = os.path.join(settings.BASE_DIR, 'utils', 'genres_train.p')
    genres = pd.read_pickle(genre_path)
    movies = pd.read_pickle(movie_path)
    print('Start movies app and load pickle file')
