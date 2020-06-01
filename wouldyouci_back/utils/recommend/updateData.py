import pandas as pd
import pymysql
from datetime import datetime

# 최신작 영화 긁어올때마다 한번씩
def get_train_data() :
    conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.movies_movie_genres"

    movie_genres = pd.read_sql_query(sql, conn, index_col='movie_id')
    genres = pd.read_csv('./genres.csv', index_col='id')

    movie_genres = movie_genres.drop('id', axis='columns')
    movie_genres['genre_id'] = movie_genres['genre_id'].apply(lambda x: genres.loc[x, 'name']+"|")
    movie_genres = movie_genres.groupby('movie_id').sum()

    genres_dummies = movie_genres['genre_id'].str.get_dummies(sep='|')

    genres_dummies.to_pickle('./genre_train.p')
    conn.close()


def get_train_data2() :
    print("시작")
    conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.movies_movie_genres"
    sql2 = "SELECT * FROM wouldyouci.movies_movie_directors"
    sql3 = "SELECT * FROM wouldyouci.movies_movie_actors"
    sql4 = "SELECT * FROM wouldyouci.movies_people"

    movie_genres = pd.read_sql_query(sql, conn, index_col='movie_id')
    movie_directors = pd.read_sql_query(sql2, conn, index_col='movie_id')
    movie_actors = pd.read_sql_query(sql3, conn, index_col='movie_id')
    people = pd.read_sql_query(sql4, conn, index_col='id')

    genres = pd.read_csv('./genres.csv', index_col='id')

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

    train.to_pickle('./movie_train.p')
    print("끝")
    conn.close()

# 이건 처음 장르 테이블 가져오기 / 한번만 쓰고 더이상 안씀
def get_genre_info() :
    conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.movies_genre;"
    result = pd.read_sql_query(sql, conn)

    result.to_csv(r'genres.csv', index=True)

    conn.close()


get_train_data2()