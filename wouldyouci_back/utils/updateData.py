import pandas as pd
import pymysql
from datetime import datetime
from decouple import config
import os


def get_train_data(base_dir):
    conn = pymysql.connect(host=config('HOST'), port=3306, user=config('USER'),
                           password=config('PASSWORD'), db=config('DB'))
    sql = "SELECT * FROM wouldyouci.movies_movie_genres"

    movie_genres = pd.read_sql_query(sql, conn, index_col='movie_id')

    path = os.path.join(base_dir, 'genres.csv')
    genres = pd.read_csv(path, index_col='id')

    movie_genres = movie_genres.drop('id', axis='columns')
    movie_genres['genre_id'] = movie_genres['genre_id'].apply(lambda x: genres.loc[x, 'name']+"|")
    movie_genres = movie_genres.groupby('movie_id').sum()

    genres_dummies = movie_genres['genre_id'].str.get_dummies(sep='|')

    path = os.path.join(base_dir, 'genres_train.p')
    genres_dummies.to_pickle(path)
    conn.close()


def get_genre_info(base_dir):
    conn = pymysql.connect(host=config('HOST'), port=3306, user=config('USER'),
                           password=config('PASSWORD'), db=config('DB'))
    sql = "SELECT * FROM wouldyouci.movies_genre;"

    result = pd.read_sql_query(sql, conn)

    path = os.path.join(base_dir, 'genres.csv')
    result.to_csv(path, index=True)

    conn.close()


def get_train_data2(base_dir):
    print("트레인 시작")
    conn = pymysql.connect(host=config('HOST'), port=3306, user=config('USER'),
                           password=config('PASSWORD'), db=config('DB'))
    sql = "SELECT * FROM wouldyouci.movies_movie_genres"
    sql2 = "SELECT * FROM wouldyouci.movies_movie_directors"
    sql3 = "SELECT * FROM wouldyouci.movies_movie_actors"
    sql4 = "SELECT * FROM wouldyouci.movies_people"

    movie_genres = pd.read_sql_query(sql, conn, index_col='movie_id')
    movie_directors = pd.read_sql_query(sql2, conn, index_col='movie_id')
    movie_actors = pd.read_sql_query(sql3, conn, index_col='movie_id')
    people = pd.read_sql_query(sql4, conn, index_col='id')

    path = os.path.join(base_dir, 'genres.csv')
    genres = pd.read_csv(path, index_col='id')

    movie_people = pd.concat([movie_directors, movie_actors])

    movie_genres = movie_genres.drop('id', axis='columns')
    movie_people = movie_people.drop('id', axis='columns')

    movie_genres['genre_id'] = movie_genres['genre_id'].apply(lambda x: genres.loc[x, 'name'] + "|")
    movie_people['people_id'] = movie_people['people_id'].apply(lambda x: people.loc[x, 'name'] + "|")

    movie_genres = movie_genres.groupby('movie_id').sum()
    movie_people = movie_people.groupby('movie_id').sum()

    genres_dummies = movie_genres['genre_id'].str.get_dummies(sep='|')
    people_dummies = movie_people['people_id'].str.get_dummies(sep='|')

    train = people_dummies.merge(genres_dummies, on='movie_id')

    path = os.path.join(base_dir, 'movie_train.p')
    train.to_pickle(path)
    print("트레인 끝")
    conn.close()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

get_genre_info(BASE_DIR)
get_train_data(BASE_DIR)
# get_train_data2(BASE_DIR)
