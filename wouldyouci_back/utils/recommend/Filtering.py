import pandas as pd
import numpy as np
import pymysql
import surprise
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from datetime import datetime

# 전체 영화 예상평점
def contentsbased(user_id):
    print('START TIME : ',str(datetime.now())[10:19] )

    conn = pymysql.connect(host='k02a4061.p.ssafy.io', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
    ratings = pd.read_sql_query(sql, conn)

    # movies = pd.read_pickle('./movie_train.p')

    # 감독만
    movies = pd.read_pickle('./movie_director_train.p')


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


def userbased(user_id):
    df = pd.read_pickle("./KNN.p")
    return df.loc[df['user_id'] == user_id	, 'movie_id'].unique()


contentsbased(9000009)
# print(userbased(9000009))
# k = userbased(9000009)
# print(k[1])
