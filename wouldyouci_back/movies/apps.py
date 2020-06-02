from django.apps import AppConfig
from django.conf import settings
import os
import pandas as pd


class MoviesConfig(AppConfig):
    name = 'movies'

    path = os.path.join(settings.BASE_DIR, 'utils', 'movie_train.p')
    movies = pd.read_pickle(path)
    print('Start movies app and load pickle file')
