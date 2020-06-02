import pandas as pd
import numpy as np
import pymysql

from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
import os
from decouple import config
from scipy.stats import uniform as sp_rand
from datetime import datetime
import time


def contentsbased(user_id, movie_id, genres_pk):
    print('======== 전체영화 예상평점 - GENRE ===========')
    print('START TIME : ', str(datetime.now())[10:19])
    start = time.time()

    conn = pymysql.connect(host=config('HOST'), port=3306, user=config('USER'),
                           password=config('PASSWORD'), db=config('DB'))
    sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
    ratings = pd.read_sql_query(sql, conn)
    genres = genres_pk

    conn.close()

    user_profile = ratings.merge(genres, left_on='movie_id', right_index=True)

    model = Lasso()
    param_grid = {'alpha': sp_rand()}

    research = RandomizedSearchCV(estimator=model,
                                  param_distributions=param_grid,
                                  n_iter=20,
                                  cv=5,
                                  random_state=406)

    print('학습 : ', str(datetime.now())[10:19])
    research.fit(user_profile[genres.columns], user_profile['score'])
    predictions = research.best_estimator_.predict(genres)
    genres.reset_index()

    print('점수 예측 : ', str(datetime.now())[10:19])
    genres['predict'] = predictions
    print('END TIME : ', str(datetime.now())[10:19])
    end = time.time()
    print('TOTAL TIME : ', end-start)
    # print(genres['predict'])
    print('EXPECTED SCORE : ', genres.at[movie_id, 'predict'])
    print()
    return pd.DataFrame.to_json(genres['predict'])


def contentsbased2(user_id, movie_id, movies_pk):
    print('======== 전체 영화 예상평점 - GENRE & ACTOR ===========')
    print('START TIME : ', str(datetime.now())[10:19])
    start = time.time()

    conn = pymysql.connect(host=config('HOST'), port=3306, user=config('USER'),
                           password=config('PASSWORD'), db=config('DB'))
    sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
    ratings = pd.read_sql_query(sql, conn)
    movies = movies_pk

    conn.close()

    ratings = ratings.merge(movies, left_on='movie_id', right_index=True)
    x_train, x_test, y_train, y_test = train_test_split(ratings[movies.columns],
                                                        ratings['score'],
                                                        random_state=406,
                                                        test_size=.1)

    reg = LinearRegression()

    reg.fit(x_train, y_train)

    print('점수예측 : ', str(datetime.now())[10:19])

    predictions = reg.predict(movies)
    movies.reset_index()

    movies['predict'] = predictions

    print('END TIME : ', str(datetime.now())[10:19])
    predicted_score = movies.at[movie_id, 'predict']

    end = time.time()
    print('TOTAL TIME : ', end-start)
    # print(movies['predict'])
    print('EXPECTED SCORE : ', predicted_score)
    print()
    return pd.DataFrame.to_json(movies['predict'])


def contentsbased3(user_id, movie_id, movies_pk):
    print('======== 특정 영화 예상평점 - GENRE & ACTOR ===========')
    print('START TIME : ', str(datetime.now())[10:19])

    start = time.time()
    conn = pymysql.connect(host=config('HOST'), port=3306, user=config('USER'),
                           password=config('PASSWORD'), db=config('DB'))
    sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
    ratings = pd.read_sql_query(sql, conn)
    movies = movies_pk

    conn.close()

    ratings = ratings.merge(movies, left_on='movie_id', right_index=True)

    train, test = train_test_split(ratings, test_size=0.1, random_state=406)

    x_train = train[movies.columns]
    y_train = train['score']

    reg = Lasso(alpha=0.03)
    reg.fit(x_train, y_train)

    user_profile = []
    user_profile.append([reg.intercept_, *reg.coef_])

    user_profile = pd.DataFrame(user_profile,
                                index=train['user_id'].unique(),
                                columns=['intercept', *movies.columns])

    intercept = user_profile.loc[user_id, 'intercept']

    columns_score = sum(user_profile.loc[user_id, movies.columns] * movies.loc[movie_id, movies.columns])

    expected_score = intercept + columns_score
    print('END TIME : ', str(datetime.now())[10:19])
    end = time.time()
    print('TOTAL TIME : ', end-start)
    print('EXPECTED SCORE : ', expected_score)
    return expected_score


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
genres = pd.read_pickle(os.path.join(BASE_DIR, 'genres_train.p'))
a = time.time()
movies = pd.read_pickle(os.path.join(BASE_DIR, 'movie_train.p'))
print()
print('Time to read pickle file: ', time.time() - a)
print()
contentsbased(9000007, 10016, genres)
contentsbased2(9000007, 10016, movies)
contentsbased3(9000007, 10016, movies)
