# Data Crawling

 영화추천을 위한 데이터와 상영 정보를 제공하기 위한 영화사들로부터의 데이터를 크롤링하였고, 가공을 통해 Django와 mySQL에 업데이트할 수 있도록 하였습니다. 서울시의 84개의 영화관을 기준으로 매일 2500개정도의 상영 정보를 얻을 수 있습니다. 

## 00. Requirements

- Python - 3.8.2
- Libraries - `requirements.txt`

- `.env` - NAVER API  KEY, YOUTUBE API KEY, 네이버 ID, PW



## 01. User Review

 빅데이터 추천 알고리즘을 위해 네이버 영화를 기준으로 유저가 남긴 리뷰 데이터를 가공하여 json 파일로 만들었습니다. 지난 3년간 네이버 영화랭킹에서 상위 작품에 리뷰를 남긴 유저를 대상으로 리뷰를 크롤링하였으며, 그 결과 16394명의 유저로부터 117,000 개의 리뷰 데이터를 얻을 수 있었습니다.

```json
{
    "pk": 16859921,
    "model": "accounts.rating",
    "fields": {
        "movie": movie_code, # 영화 코드
        "score": score, # 평가 점수
        "user": user_id,
        "comment": comment, # 리뷰 내용
        "created_at": created_at,
        "updated_at": updated_at
        }
}
```



## 02. Movie Detail

 유저가 남긴 리뷰를 대상으로 영화 데이터를 크롤링 하였습니다. 영화 데이터의 경우 NAVER API와 셀레니움을 이용한 크롤링으로 영화에 대한 상세 정보를 저장하였습니다.  네이버 영화 상세 페이지의 경우 청소년 관람 불가일 경우 로그인이 필요합니다.

- 셀레니움에서의 네이버 로그인

```python
IDxPath='//*[@id="id"]'
PasswordxPath='//*[@id="pw"]'

ID=NAVER_ID
Password=NAVER_PW

copyInput(driver, IDxPath, ID)
copyInput(driver,PasswordxPath,Password)
driver.find_element_by_xpath('//*[@value="로그인"]').click()
```



## 03. Movie on Screen

 서울시 84개의 영화관을 대상으로 당일과 다음날의 영화 정보가 크롤링됩니다. CGV, 메가박스, 롯데시네마는 해당 영화사이트를 셀레니움을 통해 각 영화사마다의 영화 제목과 코드를 저장하였고, 이를 통해 영화 상세정보 코드와 연결하였습니다. DB에 없는 데이터일 경우 영화 상영정보를 추가하고, 네이버에 검색이 되지 않을 경우에는 못찾은 데이터로 연결됩니다.

- `onscreen.json`

```json
{
    "pk": review_pk,
    "model": "movies.onscreen",
    "fields": {
        "cinema": cinema_pk,
        "movie": movie_pk,
        "date": screen_date,
        "info": hall_info,   		# 상영관 정보
        "start_time": start_time,
        "end_time": end_time,
        "total_seats": total_seats,
        "seats": seats, 			# 잔여 좌석
        "url": book_url,  			# 예매 url
        "cm_code": com_code  		# 영화사의 영화 코드
        "score": score  			# 
    }
}
```



## 04. Updating Seats

상영정보를 기준으로 현재 남은 좌석수를 크롤링합니다. 일정 시간마다 크롤링이 진행되며 크롤링한 데이터를 MySQL 서버로 바로 업데이트하게 됩니다. 

- MySQL data updating

```python
# mysql 데이터 조회
sql_base = "SELECT *  FROM movies_onscreen WHERE "
sql_option = 'cinema_id = ' + str(cinema_pk) + ' AND date = \"' + tg_date + '\"' + ' AND start_time = \"' + start_time + '\"'  + ' AND cm_code = ' + str(cm_code) + ' AND total_seats = \"' + seat_total + '\"'
sql = sql_base + sql_option
cursor.execute(sql)

# 찾은 데이터에 좌석수를 업데이트
if tg_row['seats'] != seats:
    update_sql = 'UPDATE wouldyouci.movies_onscreen SET seats = ' + '\"' + seats + '\"' + ' WHERE id = ' + str(tg_idx) + ';'
    cursor.execute(update_sql)
    conn.commit()
```

