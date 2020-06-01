import pandas as pd
import numpy as np
import pymysql

from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV

from scipy.stats import uniform as sp_rand
from datetime import datetime



def contentsbased(user_id):
    print('START TIME : ',str(datetime.now())[10:19] )
    conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
    ratings = pd.read_sql_query(sql, conn)
    genres = pd.read_pickle('./movie_train.p')

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
    print('END : ', str(datetime.now())[10:19])
    predictions = research.best_estimator_.predict(genres)
    genres.reset_index()

    print('예측 : ', str(datetime.now())[10:19])
    genres['predict'] = predictions
    print('END TIME : ', str(datetime.now())[10:19])
    return pd.DataFrame.to_json(genres['predict'])

# 전체 영화 예상평점
def contentsbased2(user_id):
    print('START TIME : ',str(datetime.now())[10:19] )

    conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
    ratings = pd.read_sql_query(sql, conn)
    movies = pd.read_pickle('./movie_train.p')

    conn.close()

    ratings = ratings.merge(movies, left_on='movie_id', right_index=True)
    x_train, x_test, y_train, y_test = train_test_split(ratings[movies.columns],
                                                        ratings['score'],
                                                        random_state=406,
                                                        test_size=.1)

    # 리뷰수가 적을수록 Lasso가 좋다는데 Linear가 더 잘나오는거 같음...
    reg = LinearRegression()
    # reg = Lasso(alpha=0.05)

    reg.fit(x_train, y_train)

    print('점수예측 : ', str(datetime.now())[10:19])

    predictions = reg.predict(movies)
    movies.reset_index()

    movies['predict'] = predictions

    print('END TIME : ', str(datetime.now())[10:19])
    return pd.DataFrame.to_json(movies['predict'])


# 해당 영화 예상평점
def contentsbased3(user_id, movie_id):
    print('START TIME : ', str(datetime.now())[10:19])

    conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
    ratings = pd.read_sql_query(sql, conn)
    movies = pd.read_pickle('./movie_train.p')

    conn.close()

    ratings = ratings.merge(movies, left_on='movie_id', right_index=True)

    train, test = train_test_split(ratings, test_size=0.1, random_state=406)


    x_train = train[movies.columns]  # feature, x
    y_train = train['score']  # label, y

    #     reg = LinearRegression()
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
    return expected_score

# print(contentsbased(9000007))
# print(contentsbased2(9000007))
# print(contentsbased3(9000007, 10016))