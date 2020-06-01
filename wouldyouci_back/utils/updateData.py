import pandas as pd
import pymysql
from datetime import datetime
from decouple import config
import os


def get_train_data():
    conn = pymysql.connect(host=config('HOST'), port=3306, user=config('USER'),
                           password=config('PASSWORD'), db=config('DB'))
    sql = "SELECT * FROM wouldyouci.movies_movie_genres"

    movie_genres = pd.read_sql_query(sql, conn, index_col='movie_id')
    path = os.path.join('.', 'utils', 'genres.csv')
    genres = pd.read_csv(path, index_col='id')

    movie_genres = movie_genres.drop('id', axis='columns')
    movie_genres['genre_id'] = movie_genres['genre_id'].apply(lambda x: genres.loc[x, 'name']+"|")
    movie_genres = movie_genres.groupby('movie_id').sum()

    genres_dummies = movie_genres['genre_id'].str.get_dummies(sep='|')

    path = os.path.join('.', 'utils', 'genres_train.p')
    genres_dummies.to_pickle(path)
    conn.close()


def get_genre_info():
    conn = pymysql.connect(host=config('HOST'), port=3306, user=config('USER'),
                           password=config('PASSWORD'), db=config('DB'))
    sql = "SELECT * FROM wouldyouci.movies_genre;"

    result = pd.read_sql_query(sql, conn)

    path = os.path.join('.', 'utils', 'genres.csv')
    result.to_csv(path, index=True)

    conn.close()


get_genre_info()
get_train_data()

