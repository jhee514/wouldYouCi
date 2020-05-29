import pandas as pd
from sklearn.linear_model import Lasso
import pymysql
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform as sp_rand

def contentsbased(user_id, movie_id):
    conn = pymysql.connect(host='15.164.96.65', port=3306, user='root', password='wouldyoucinema', db='wouldyouci')
    sql = "SELECT * FROM wouldyouci.accounts_rating where user_id=" + str(user_id)
    ratings = pd.read_sql_query(sql, conn)
    genres = pd.read_pickle('./genre_train.p')

    conn.close()

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
    genres['predict'] = predictions

    # print("예상평점:",genres.loc[movie_id, 'predict'])


