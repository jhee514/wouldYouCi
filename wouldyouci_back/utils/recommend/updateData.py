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

# 이건 처음 장르 테이블 가져오기 / 한번만 쓰고 더이상 안씀
def get_genre_info() :
    conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.movies_genre;"
    result = pd.read_sql_query(sql, conn)

    result.to_csv(r'genres.csv', index=True)

    conn.close()
