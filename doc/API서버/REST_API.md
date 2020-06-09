# REST API

# 백앤드 주소  [https://](http://15.164.96.65:80/)k02a4061.p.ssafy.io

# Notice

- 질문 달아주시면 확인하는대로 답변 드립니다.
- `blah` 된 것은 만든 API, 'blah'는 작성해야할 API
- Django 는 요청 url 끝에 / 붙여줘야 합니다.
    
- 연결 확인 된 API 에 스티커 달아놔주면 땡큐베리감삼다~
    
- **접근 권한**에 대해서 Headers 설정은 다음처럼 해주심 됩니당

    ```sql
    AlloAny : 누구든 접근 가능
    IsAuthenticated : 접근 권한 필요
    				headers: { Authorization: `JWT ${token}` }  
    ```

## Swagger

- GET `swagger/`  👌
    - debug = True 일 때만!

## User

- POST `user/login/`  로그인 👌
    - JWT 인증 토큰
    - AllowAny
    - Request

        ```python
        {
          "username": "string",
          "password": "string"
        }
        ```

    - Response

        ```python
        {
          "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InRlc3RlcmpheSIsImV4cCI6MTU5MDU0NjM4NCwiZW1haWwiOiJ0dHRlc3RlckBhZy5jb20iLCJvcmlnX2lhdCI6MTU4OTk0MTU4NH0.DP5TBNaDENMCxS2gSxZouOQimsziUZAthvoMeR68rSo"
        }
        ```

- POST `user/signup/`  회원가입 👌
    - 회원가입
    - AllowAny
    - Request
        - get_agreement 는 회원가입시 필수 입력 사항이 아니게 만들어두었읍니다. default=false

        ```python
        {
          "username": "string",
          "password": "string",
          "get_agreement": true, (0 or 1 가능, boolean field)
          "email": "user@example.com"
        }
        ```

    - Response
        - 200 - 'message': '회원가입 되었습니다.'
        - 400 - serializer error 에 따라서 이런저런 경우

            ```
            ex1)
            {
                "username": ["user의 username은/는 이미 존재합니다."]
            }

            ex2)
            {
            		"email": ["이 필드는 필수 항목입니다."]

            }

            ex3)
            {

                "username": ["user의 username은/는 이미 존재합니다."],

                "email": ["이 필드는 필수 항목입니다."],

            }
            ```

- GET  `user/login/rating/`  rating 10개 이상 했는지 확인하는 API 👌👌
    - IsAuthenticated (로그인 되어있어야 - header 에 담아보내는 방법 잠시만)
    - Response
        - 최초로 평점 입력하는게 아닐 수 도 있으니까 유저가 지금까지 몇 개 평점 남겼는지를 여기다 보낼게요 혹시 저장 가능한지...?

        ```python
        지금까지 평가한 영화가 10개 이상이면 True 아니면 False

        {
            "rating_tf": false,
        }
        ```

- GET   `user/rating/page/`  영화취향 알기 위해서 영화 리스트 요청 👌
    - IsAuthenticated
    - Request
        - query params
        - 옵션: page

        ```sql
        http://localhost:8000/user/taste/?page=2
        ```

    - Response
        - 유저가 평가하지 않은 영화 중에서
        - 청소년 관람불가 및 성인 영화 제외
        - 2015년 이후 만들어진 영화 중에 댓글 많고 평균 평점 높은 순 정렬
        - 20개씩 페이지네이션

        ```sql
        {
            "count": 3361,
            "next": "http://localhost:8000/user/taste/?page=3",
            "previous": "http://localhost:8000/user/taste/",
            "results": [
        				- 생략 -
                {
                    "id": 163788,
                    "name": "알라딘",
                    "poster": "https://movie-phinf.pstatic.net/20190524_104/1558663170174Q2mmw_JPEG/movie_image.jpg"
                },
                {
                    "id": 85579,
                    "name": "신과함께-죄와 벌",
                    "poster": "https://movie-phinf.pstatic.net/20171201_181/1512109983114kcQVl_JPEG/movie_image.jpg"
                },
                {
                    "id": 146469,
                    "name": "택시운전사",
                    "poster": "https://movie-phinf.pstatic.net/20170717_298/1500253295782rcIkE_JPEG/movie_image.jpg"
                },
                {
                    "id": 181925,
                    "name": "클로젯",
                    "poster": "https://movie-phinf.pstatic.net/20200116_23/1579154974413LvtIf_JPEG/movie_image.jpg"
                },
            ]
        }
        ```

- POST `user/rating/`  유저가 선택한 영화취향 별점 정보 입력 👌
    - IsAuthenticated
    - Request
        - body 에 이런 식으로 json 담아서 주는거 가능한가유? 리스트 안에 object로..
        - movie 는 movie_id
        - movie, score 필수

        ```sql
        {"data": [{"movie": 85579, "score": 5}, {"movie":173123, "score":5}]}
        ```

    - Response

        ```sql
        203  -- data x

        400  -- movie 나 score 없을 시
        				{
        			    "movie": [
        			        "이 필드는 필수 항목입니다."
        			    ],
        		      "score": [
        			        "이 필드는 필수 항목입니다."
        			    ]
        				}
        ```

- GET  `user/rating/`  유저 평점 목록  👌
    - IsAuthenticated
    - Request
    - Response

        ```sql
        [
            {
                "id": 117260,
                "movie": {
                    "id": 173123,
                    "name": "스파이더맨: 파 프롬 홈",
                    "poster": "https://movie-phinf.pstatic.net/20190527_181/1558933159657a210P_JPEG/movie_image.jpg"
                },
                "score": 5.0
            },
            {
                "id": 1,
                "movie": {
                    "id": 152691,
                    "name": "레이니 데이 인 뉴욕",
                    "poster": "https://movie-phinf.pstatic.net/20200417_176/1587098239671MiQEL_JPEG/movie_image.jpg"
                },
                "score": 0.5
            }
        ]
        ```

        - movie, score 만 보내주면 됩니다.
        - Score 수정시 : PATCH  `movie/rating/<int:rating_id>/` 영화 리뷰 수정하기 참고

- GET  `user/` 마이페이지 들어갔을 때  👌
    - IsAuthenticated
    - Response
        - meta
            - rating_tf : 유저가 rating 10개 이상 했는지 여부
                - 미만이면 recommend 부분이 빈 리스트 []
            - 개수 정
        - data
            - user
            - pick_cinemas
            - pick_movies
            - recommend_movies
                - 유저와 유사한 유저들이 좋아하는 영화 최대 10개
            - recommend_onscreen
                - 유저가 좋아할 것 같은 상영중인 영화들 최대 10개

        ```json
        {
            "meta": {
                "rating_tf": true,
                "pick_cinemas": 1,
                "pick_movies": 1,
                "recommend_movies": 10,
                "recommend_onscreen": 10
            },
            "data": {
                "user": {
                    "id": 9000000,
                    "username": "mrWoo0",
                    "file": [
                        "media/profile/202006011730685811.jpeg"
                    ]
                },
        	    "pick_cinemas": [
        	        {
        	            "id": 1,
        	            "name": "CGV 강남",
        	            "type": "CGV",
        	            "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVgangnam.jpg",
        	            "address": "서울 강남구 강남대로 438",
        	            "tel": "1544-1122",
        	            "x": "127.026391177132",
        	            "y": "37.5016573944824",
        	            "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0056"
        	        }
        	    ],
        	    "pick_movies": [
        	        {
        	            "id": 85579,
        	            "name": "신과함께-죄와 벌",
        	            "poster": "https://movie-phinf.pstatic.net/20171201_181/1512109983114kcQVl_JPEG/movie_image.jpg",
        	            "genres": [
        	                "드라마",
        	                "판타지"
        	            ],
        	            "running_time": "139분",
        	            "watch_grade": "12세 관람가"
        	        }
        	    ],
        	    "recommend_movies": [
        	        {
        	            "id": 129095,
        	            "name": "지오스톰",
        	            "poster": "https://movie-phinf.pstatic.net/20170922_133/1506059018478U7ur6_JPEG/movie_image.jpg",
        	            "genres": [
        	                "스릴러",
        	                "SF",
        	                "액션"
        	            ],
        	            "running_time": "109분",
        	            "watch_grade": "12세 관람가"
        	        },
        	    ],
        	    "recommend_onscreen": [
        	
        	        {
        	            "id": 73588,
        	            "name": "블루 발렌타인",
        	            "poster": "https://movie-phinf.pstatic.net/20120510_83/133664363400782vFQ_JPEG/movie_image.jpg",
        	            "genres": [
        	                "드라마",
        	                "로맨스"
        	            ],
        	            "running_time": "114분",
        	            "watch_grade": "청소년 관람불가"
        	        }
        	    ]
        	}
        }
        ```

- POST  `user/profile/`  프사 생성 및 변경하기 👌
    - IsAuthenticated
    - 생성 및 수정이 둘 다 같은 API 입니당! 형태도 같아요! 걍 새 image를 POST 만 해주면 됨!!
    - 사용자가 아직 이미지 등록 안 한 경우 기본 이미지는 제 쪽에서 갖구 있을까요 지금처럼 지선이 만들어놓은 이미지로 해놓을까욥? 우리 회원가입 때 이미지 안 받으니까 기본 이미지가 있는거라고 생각했거든욥
    - Request

        ```json
        "Content-Type": "multipart/form-data"

        {"file": file}
        ```

    - Response

        ```json
        {
            "file": "media/profile/202005262135276053.jpeg"
        }

        src 예시: http://localhost:8000/media/profile/202005262135276053.jpeg
        ```

    - ER

        ```
        파일 형식이 문제있는 경우
        - status=400, {'message': '유효하지 않은 파일입니다.'}

        이미지 파일을 첨부하지 않은 경우
        - status=403, {'message': '이미지는 필수입니다.'}
        ```

- DELETE `user/profile/`  프사 삭제하기 👌
    - IsAuthenticated
    - Return

        ```json
        204  --- data X
        ```

- PATCH  `user/password/`   비번 변경하기 👌
    - IsAuthenticated
    - Request

        ```json
        {
           "~~password": '1234',~~
           "new_password": '5678'
        }
        ```

    - Response

        ```json
        203  --- data X
        ```

    - Error

        ```json
        status=400  {'message': '필수 데이터가 누락되었습니다.'}
        status=403  {'message': '비밀번호가 일치하지 않습니다.'}
        ```

## Home

- GET `cinema/map/`   위치 기반 주변 영화관 조회   👌
    - AllowAny
    - Request
        - query params
            - 필수 : x1, ,x2, y1, y2
            - 방식은 기존이랑 똑같아용
            - 기존의 x, y 중심좌표만 보내던건 일단 남겨둠: cinema/map/center/
            - ~~옵션: radius (default 1km)  — radius 를 어케 할지 함 논의 필요~~
            - x = 127.033311 = 'longitude' = '경도'
            - y = 37.5611326 = 'latitude' = '위도'

        ```python
        ~~http://localhost:8000/cinema/map/center/?x=127.033311&y=37.5611326~~
        https://wouldyouci.ga/cinema/map/?x1=127.033311&y1=37.5611326&x2=127.033312&y2=37.5611327
        ```

    - Response

        ```python
        {
            "meta": {
                "total": 1  --- doc 개수
            },
            "documents": [
                {
                    "id": 47,  --- 더 주었으면 정보가 있다면 말씀해주세용 (글 하단 모델 참고)
                    "name": "메가박스 코엑스",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "address": "서울 강남구 영동대로 513",
                    "tel": "1544-0070",
                    "x": "127.058215118259",
                    "y": "37.5130779481089",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1351"
                }
            ]
        }
        ```

- GET `cinema/map/<int:cinema_id>/movie/`  상영중인 영화 빠른 시간 순 정렬 👌
    - AllowAny
    - queryparams
        - 필수 X
        - 옵션: date, start_time  (default = 오늘, 현재 시간)
            - date는 당일 기준 3일만 제공 (오늘이 수요일이면 수, 목 금)
            - 실시간 잔여좌석수는 일단 당일 것 만 제공
    - Request
        - id 1번하고 31번 (강남 CGV, 강남 메가박스) 데이터 있어용

        ```json
        http://localhost:8000/cinema/map/31/movie/
        http://localhost:8000/cinema/map/31/movie/?start_time=18:00
        ```

    - Response  — 먼가 더 필요하다, 넣자 싶은 데이터가 있다면 알려주세용

        ```json
        {
            "meta": {
                "total": 1
            },
            "documents": [
                {
                    "movie": {
                        "id": 129095,
                        "name": "지오스톰",
                        "poster": "https://movie-phinf.pstatic.net/20170922_133/1506059018478U7ur6_JPEG/movie_image.jpg",
                        "genres": [
                            "느와르",
                            "액션",
                            "무협"
                        ],
                        "running_time": "109분",
                        "watch_grade": "12세 관람가"
                    },
                    "info": "3관",
                    "date": "2020-05-25",
                    "start_time": "18:30:00",
                    "end_time": "20:00:00",
                    "total_seats": "53",
                    "seats": "14",
                    "url": "https://www.megabox.co.kr/booking/seat?playSchdlNo=2005251372021"
                }
            ]
        }
        ```

## Search

- GET  `search/`   검색페이지 들어갔을 때 👌
    - IsAuthenticated
    - Request
        - query params
        - x, y 없을 수 도 있으니까 (위치 안 켠 경우) 여기는 옵션입니당.
        - x = 127.033311 = 'longitude' = '경도'
        - y = 37.5611326 = 'latitude' = '위도'

        ```json
        http://localhost:8000/cinema/search/?x=127.033311&y=37.5611326
        ```

    - Response
        - 근처 영화관은 반경 2km 내에 있는 영화관입니다
        - 없으면 반경 2키로 이내에 영화관 없다고 보여주면 되지않을까 했어유

        - comming_soon:  개봉예정작 중 한 달 이내 개봉 예정작 (꽤 많아서 범위 같이 정해야 할듯? [https://movie.naver.com/movie/running/premovie.nhn](https://movie.naver.com/movie/running/premovie.nhn))

            찜한 수 같이 갑니당 

        - popular_movies:  상영중인 영화 중에서 평점 많은 순으로 10개? 댓글수랑 같이 갑니당

        
```json
        {
    "meta": {
                "near_cinema": 0,
        "popular_movies": 10,
                "comming_soon": 8
            },
            "near_cinema": [],
            "popular_movies": [
                {
                    "id": 167613,
                    "name": "조커",
                    "name_eng": "Joker",
                    "poster": "https://movie-phinf.pstatic.net/20190906_128/1567761736426S6Fje_JPEG/movie_image.jpg",
                    "watch_grade": "15세 관람가",
                    "score": 4.27,
                    "ratings_count": 863
                },
                - 생략 -
                {
                    "id": 179181,
                    "name": "지푸라기라도 잡고 싶은 짐승들",
                    "name_eng": "BEASTS CLAWING AT STRAWS",
                    "poster": "https://movie-phinf.pstatic.net/20200211_156/1581402209718zyQ9B_JPEG/movie_image.jpg",
                    "watch_grade": "청소년 관람불가",
                    "score": 3.32,
                    "ratings_count": 415
                }
            ],
            "comming_soon": [
                {
                    "id": 10001,
                    "open_date": "1990-07-07",
                    "running_time": "124분",
                    "pick_users_count": 0,
                    "genres": [
                        "드라마",
                        "로맨스"
                    ],
                    "directors": [
                        "쥬세페 토르나토레"
                    ],
                    "actors": [
                        "브리지트 포시",
                        "필립 느와레",
                        "자크 페렝",
                        "마르코 레오나르디",
                        "살바토레 카스치오"
                    ]
                },
                - 생략 -
                {
                    "id": 10012,
                    "open_date": "1988-09-24",
                    "running_time": "131분",
                    "pick_users_count": 0,
                    "genres": [
                        "스릴러",
                        "범죄",
                        "액션"
                    ],
                    "directors": [
                        "존 맥티어난"
                    ],
                    "actors": [
                        "브루스 윌리스"
                    ]
                }
            ]
        }
        ```
    
- GET  `search/movie/`   영화 검색 (for 자동완성) 👌
    - AllowAny (그냥 이게 더 빠를 것 같아서..)
    - Request
        - query params : words

        ```json
        http://localhost:8000/search/movie/?words=해리포
        ```

    - Response
        - 일부러 리스트로 했는데 (for 문 돌리면 되나 싶어서) 다른 형태 - objects 등이 편하면 알려주세용
        - 최대 10개만 보냄

        ```json
        [
            "해리 포터와 마법사의 돌",
            "해리 포터와 비밀의 방",
            "해리 포터와 아즈카반의 죄수",
            "해리 포터와 불의 잔",
            "해리 포터와 죽음의 성물 - 2부",
            "해리 포터와 불사조 기사단",
            "해리 포터와 혼혈 왕자",
            "해리 포터와 죽음의 성물 - 1부"
        ]
        ```

- GET  `search/movie/<str:words>/`   영화 검색 👌
    - AllowAny
    - Request

        ```json
        http://localhost:8000/search/movie/신과 함께/
        ```

    - Response
        - meta 필요 없을 것 같으면 뺄게욤
        - similar_result 는 뭐냐면 신과함께를 예로 들면 되는데

            search_result 는 사용자가 입력한 그대로 검색합니당. 

            sim_result 는 검색 방법이 좀 달라요. 

            1. '신과 함께' 를 검색하면 '신과함께-웅앵' 이 안 나옴
            2. 그 때 sim에는 나올 수 있음. 

            그런데 sim_result 검색은 'search_result' 에 있는 결과와 동일한 결과는 안 나옵니당

            1. '신과함께' 를 검색하면 '신과함께-웅앵' 이 나옴
            2. 그 때는 sim 이 빈 리스트. (검색어에 따라 아닐 수 도 있긴 함)

            그래서 sim_ 은 찾으시는 결과가 없으신가요? 

            유사한 검색결과는 다음과 같습니다. 유사한 제목의 영화입니다. 

            정도로 쓰면 어떨까 해서 포함해봤습니다. 

            즉 우리 검색 기능의 한계 극뽁용....

        - '신과 함께' 검색의 경우 Response

            ```json
            {
              "meta": {
                "search_result": 10,
                "similar_result": 2
              },
              "search_result": [
                {
                  "id": 10020,
                  "name": "바람과 함께 사라지다",
                  "poster": "https://movie-phinf.pstatic.net/20111223_100/13245711831524mp33_JPEG/movie_image.jpg",
                  "genres": [
                    "드라마",
                    "로맨스",
                    "전쟁"
                  ],
                  "running_time": "222분",
                  "watch_grade": "12세 관람가"
                },

                - 생략 -

              ],
              "similar_result": [
                {
                  "id": 85579,
                  "name": "신과함께-죄와 벌",
                  "poster": "https://movie-phinf.pstatic.net/20171201_181/1512109983114kcQVl_JPEG/movie_image.jpg",
                  "genres": [
                    "드라마",
                    "판타지"
                  ],
                  "running_time": "139분",
                  "watch_grade": "12세 관람가"
                },
                {
                  "id": 167697,
                  "name": "신과함께-인과 연",
                  "poster": "https://movie-phinf.pstatic.net/20180703_65/15305852198817R6a1_JPEG/movie_image.jpg",
                  "genres": [
                    "드라마",
                    "판타지"
                  ],
                  "running_time": "141분",
                  "watch_grade": "12세 관람가"
                }
              ]
            }
            ```

        - '신과함께' 검색의 경우 Response

            ```json
            {
              "meta": {
                "search_result": 2,
                "similar_result": 0
              },
              "search_result": [
                {
                  "id": 85579,
                  "name": "신과함께-죄와 벌",
                  "poster": "https://movie-phinf.pstatic.net/20171201_181/1512109983114kcQVl_JPEG/movie_image.jpg",
                  "genres": [
                    "드라마",
                    "판타지"
                  ],
                  "running_time": "139분",
                  "watch_grade": "12세 관람가"
                },
                {
                  "id": 167697,
                  "name": "신과함께-인과 연",
                  "poster": "https://movie-phinf.pstatic.net/20180703_65/15305852198817R6a1_JPEG/movie_image.jpg",
                  "genres": [
                    "드라마",
                    "판타지"
                  ],
                  "running_time": "141분",
                  "watch_grade": "12세 관람가"
                }
              ],
              "similar_result": []
            }
            ```

- GET  `search/cinema/`  지역별 영화관 검색 (for 자동완성) 👌
    - AllowAny
    - Request
        - queryparams  words

        ```sql
        http://localhost:8000/search/cinema/?words=강
        ```

    - Response

        ```sql
        [
            "강남구",
            "강서구",
            "강북구",
            "강동구"
        ]
        ```

- GET  `search/cinema/<str:words>/`   지역별 영화관 검색 👌
    - AllowAny
    - Request

        ```sql
        http://localhost:8000/search/cinema/서대문/
        ```

    - Response
        - 몬가 불편한데.. 어케 개선해야할지 몰르겠고 머.. 이거면 되지않을까 싶기도 하궁...
        - 이게 구 단위라서.. 신촌 이라고 검색하면 아무것도 안 나온단 말이쥬...
        말 안듣는 user 를 위해 similar 를 추가해보았습니다.. 둘이 겹칠 일은 없어유

        ```sql
        1. 서대문이라고 검색한 경우 

        {
          "meta": {
            "search_result": 4,
            "similar_result": 0
          },
          "search_result": [
            - 생략 -
            {
              "id": 82,
              "name": "필름포럼",
              "address": "서울 서대문구 성산로 527",
              "type": "기타",
              "img": "http://www.filmforum.kr/img/filmforum/mv01.jpg"
            }
          ],
          "similar_result": []
        }

        ```

        ```sql
        2. 신촌이라고 검색한 경우

        {
          "meta": {
            "search_result": 0,
            "similar_result": 2
          },
          "search_result": [],
          "similar_result": [
            {
              "id": 17,
              "name": "CGV 신촌아트레온",
              "address": "서울 서대문구 신촌로 129",
              "type": "CGV",
              "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVsinchonartreon.jpg"
            },
            {
              "id": 43,
              "name": "메가박스 신촌",
              "address": "서울 서대문구 신촌역로 30",
              "type": "메가박스",
              "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg"
            }
          ]
        }
        ```

- GET  `cinema/<int:cinema_id>/`   영화관 상세정보 👌
    - IsAuthenticated
    - Response
        - 총 세 파트
        - 영화관 | 상영중인영화 | 댓글

        ```json
        {
        		"score": 5.0,
            "id": 1,
            "name": "CGV강남",
            "type": "CGV",
            "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVgangnam.jpg",
            "address": "서울 강남구 강남대로 438",
            "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0056",
            "tel": "1544-1122",
            "public": "# 지하철\n2호선 | 강남역 11번 출구\n9호선 | 신논현역 5번출구\n\n# 버스\n- 분당지역\n   좌석버스: 1005-1, 1005-2, 6800, 5500-2\n   간선버스: 408, 462\n   광역버스: 9404, 9408\n- 강북지역\n   간선버스: 140, 144, 145, 471\n- 강서지역\n   좌석버스: 1500\n   간선버스: 360\n- 강동지역\n   간선버스: 402, 420, 470, 407\n- 인근경기지역\n   좌석버스: 3030, 2002, 2002-1\n   광역버스: 9409, 9500, 9501, 9503, 9700, 9711",
            "parking": "# 주차정보\n- 위치: 건물 지하2F ~ 지하4F\n\n# 주차요금\n- CGV 영화 관람 시 주차 3시간 6,000원\n- 주차시간 (3시간) 초과 시 10분 당 1,000원\n※ 발렛서비스 운영시간 : 오전 8시 이후 ~ 오후 20시\n※ 발렛 무료 서비스는 영화 관람 고객 한 함.  (영화 미관람 시 건물 주차장에서 별도 정산)\n※ 20시 이후 입차 차량은 발렛서비스 이용이 제한될 수 있으며, 별도 운영되는 주차팀의 사정에 따라 변경될 수 있습니다.\n\n# 이용안내\n- 주차공간이 협소하여 평일 오후/주말은 주차가 어렵습니다.\n- 편리한 대중교통 이용을 이용하여 주시기 바랍니다.",
            "onscreens": [
                {
                    "movie": {
                        "id": 85579,
                        "name": "신과함께-죄와 벌",
                        "poster": "https://movie-phinf.pstatic.net/20171201_181/1512109983114kcQVl_JPEG/movie_image.jpg",
                        "genres": [
                            "판타지",
                            "서부"
                        ],
                        "running_time": "139분",
                        "watch_grade": "12세 관람가"
                    },
                    "info": "2관 | 3D",
                    "date": "2020-05-27",
                    "start_time": "05:00:00",
                    "end_time": "08:00:00",
                    "total_seats": "521",
                    "seats": "24",
                    "url": "https://www.megabox.co.kr/booking/seat?playSchdlNo=2005251372021"
                },
            ],
            "cinema_ratings": [
                {
                    "id": 1,
                    "comment": "blah",
                    "score": 5,
                    "updated_at": "2020-05-27T12:31:13.702559+09:00",
                    "user": {
                        "id": 9000000,
                        "username": "mrWoo0"
                    }
                }
            ]
        }
        ```

- GET  `cinema/<int:cinema_id>/pick/`    자주가는 영화관 등록 토글 👌
    - IsAuthenticated
    - Response

        ```json
        {
            "pick_cinemas": true
        }
        ```

- POST  `cinema/rating/`    영화관 리뷰 남기기 👌 **⇒ 유저하나당 리뷰한개 수정 👌!!**👌
    - IsAuthenticated
    - Request
    - Response

        ```json
        {
            "id": 1,
            "comment": "blah",
            "cinema": 1,
            "score": 5,
            "created_at": "2020-05-27T12:31:13.702559+09:00",
            "updated_at": "2020-05-27T12:31:13.702559+09:00"
        }
        ```

    - Error
        - 400

        ```json
        {
            "cinema": [
                "이 필드는 필수 항목입니다."
            ]
        }

        {
            "score": [
                "이 필드는 필수 항목입니다."
            ],
            "cinema": [
                "유효하지 않은 pk \"999\" - 객체가 존재하지 않습니다."
            ]
        }
        ```

        - score 가 0.5 보다 작을 때

        ```sql
        {
            "score": [
                "이 값이 0.5보다 크거나 같은지 확인하십시오."
            ]
        }
        ```

        - 이미 평가 한 영화인 경우에는 403

        ```sql
        status=403, {'message': '이미 평가한 영화입니다.'}
        ```

- PATCH  `cinema/rating/<int:rating_id>/`   영화관 리뷰 수정하기  👌
    - IsAuthenticated
    - Request

        ```json
        http://localhost:8000/user/cinema/rating/1/

        {
        	"comment": 'testest2',
          "score": 5,
          "cinema": 1
        }
        ```

    - Response

        ```json
        {
            "id": 2,
            "user": {
                "id": 9000000,
                "username": "mrWoo0"
            },
            "comment": "testest",
            "score": 5,
            "created_at": "2020-05-26T12:35:09.323348+09:00",
            "updated_at": "2020-05-26T12:39:03.941535+09:00",
            "cinema": 1
        }
        ```

    - POST 요청과 마찬가지로 필수 항목 - cinema, score 를 보내지 않으면 400

        ```json
        {
            "cinema": [
                "이 필드는 필수 항목입니다."
            ]
        }
        ```

    - rating 작성자 user_id 와 요청을 보낸 user_id가 일치하지 않으면 400

        ```json
        {
            "message": "권한이 없습니다."
        }
        ```

- DELETE  `cinema/rating/<int:rating_id>/`  영화관 리뷰 삭제하기 👌
    - IsAuthenticated
    - Request
    - Response

        ```json
        204 --- data 없음
        ```

    - PATCH 와 마찬가지로 작성자와 요청자가 일치하지 않으면 400

- GET  `movie/rating/page/`  영화 리뷰 가져오기  👌
    - IsAuthenticated
    - Request
        - query params
            - 필수: movie
            - 옵션: page

        ```sql
        http://localhost:8000/movie/rating/page/?movie=85579
        http://localhost:8000/movie/rating/page/?movie=85579&page=2
        ```

    - Response

        ```sql
        {
            "count": 308,
            "next": "http://localhost:8000/movie/rating/page/?movie=85579&page=2",
            "previous": null,
            "results": [
                {
                    "id": 117248,
                    "comment": "far",
                    "score": 5.0,
                    "updated_at": "2020-05-31T17:47:11.203910+09:00",
                    "user": {
                        "id": 9016371,
                        "username": "hello"
                    }
                },
                
        				- 생략 - 
                
                {
                    "id": 117239,
                    "comment": "work",
                    "score": 3.0,
                    "updated_at": "2020-05-31T17:27:40.443216+09:00",
                    "user": {
                        "id": 9016371,
                        "username": "hello"
                    }
                }
            ]
        }
        ```

        ```sql

        ```

    - Error

        ```sql
        필수 queryparams movie 없는 경우

        404

        {
            "detail": "찾을 수 없습니다."
        }
        ```

- GET  `cinema/rating/page/`  영화관 리뷰 가져오기  👌
    - IsAuthenticated
    - Request
        - query params
            - 필수: cinema
            - 옵션: page

        ```sql
        http://localhost:8000/movie/rating/page/?cinema=1
        http://localhost:8000/movie/rating/page/?cinema=1&page=2
        ```

    - Response

        ```sql
        {
            "count": 0,
            "next": null,
            "previous": null,
            "results": []
        }
        ```

    - Error

        ```sql
        필수 queryparams cinema 없는 경우

        404

        {
            "detail": "찾을 수 없습니다."
        }
        ```

- GET `movie/<int:movie_id>/`  영화 상세정보   👌
    - IsAuthenticated
    - is_showing 이 추가 되었습니다. 상영중(예매가능)이면 is_showing: true
        
        - 추가기능을 한다면, 상영중이면 → 버튼을 클릭하면 모달로 예매 할 수 있는 시간, 사이트 간단하게 띄워주면 어떨까 해요
    - has_score : 혹시 몰라서 만드는김에.. 유저가 평점 남겼는지 여부 알려줍니다
    - pick_movies : 찜 했는지 여부
    - Response
        - 유저가 평점 기록한 내역이 10개 이상이면 결과값 * 20
    - 미만인 경우 0
    
        ```json
        {
          "has_score": false,
          "pick_movies": true,
        	"is_showing": true,
        	"predicted_score": 0,
        	"score": 3.03,
          "id": 152691,
          "name": "레이니 데이 인 뉴욕",
          "name_eng": "A Rainy Day in New York",
          "watch_grade": "15세 관람가",
          "running_time": "92분",
          "summary": "상상해 봐요 \n막 떨어지기 시작한 빗방울 \n센트럴 파크 델라코트 시계 아래 \n누군가 당신을 기다리고 있다면…\n재즈를 사랑하는 ‘개츠비’(티모시 샬라메)\n 영화에 푹 빠진 ‘애슐리’(엘르 패닝)\n 낭만을 꿈꾸는 ‘챈’(셀레나 고메즈)\n 매력적인 세 남녀가 선사하는 낭만적인 하루!\n \n 운명 같은 만남을 기대하며\n 봄비 내리는 뉴욕에서\n 로맨틱한 하루를 함께 하실래요?",
          "open_date": "2020-05-06",
          "trailer": "https://www.youtube.com/embed/yIVRldiVDL8",
          "poster": "https://movie-phinf.pstatic.net/20200417_176/1587098239671MiQEL_JPEG/movie_image.jpg",
          "directors": [
            "우디 앨런"
          ],
          "genres": [
            "모험"
          ],
          "actors": [
            "주드 로",
            "리브 슈라이버",
            "엘르 패닝",
            "셀레나 고메즈",
            "티모시 샬라메"
          ],
        }
    ```
    
- PATCH  `movie/<int:movie_id>/pick/`    보고싶은 영화 등록 토글   👌
    - IsAuthenticated
    - request
    - response

        ```json
        {
            "pick_movies": true
        }
        ```

- POST  `movie/rating/`    영화 리뷰 남기기   👌
    - IsAuthenticated
    - Request

        ```json
        {
        	"comment": 'text',
          "score": 5,
          "movie": 152691  ---movie id
        }
        ```

    - Response

        ```json
        {
            "id": 216859940,
            "comment": "blah",
            "movie": 85579,
            "score": 5,
            "created_at": "2020-05-27T12:27:56.211048+09:00",
            "updated_at": "2020-05-27T12:27:56.211048+09:00"
        }
        ```

    - comment 는 필수가 아니지만 score, movie 정보가 누락되거나 없는 movie_id 를 제출하면 400 error

        ```json
        {
            "movie": [
                "이 필드는 필수 항목입니다."
            ]
        }

        {
            "score": [
                "이 필드는 필수 항목입니다."
            ],
            "movie": [
                "유효하지 않은 pk \"1\" - 객체가 존재하지 않습니다."
            ]
        }
        ```

    - score 가 0.5 보다 작을 때

        ```sql
        {
            "score": [
                "이 값이 0.5보다 크거나 같은지 확인하십시오."
            ]
        }
        ```

    - 이미 평가 한 영화인 경우에는 403

        ```sql
        status=403, {'message': '이미 평가한 영화입니다.'}
        ```

- PATCH  `movie/rating/<int:rating_id>/`   영화 리뷰 수정하기   👌
    - IsAuthenticated
    - Request
        - comment 는 필수는 아닙니다

        ```json
        http://localhost:8000/user/movie/rating/216859933/

        {
        	"comment": 'testest2',
          "score": 5,
          "movie": 85579
        }

        {
          "score": 5,
          "movie": 85579
        }
        ```

    - Response

        ```json
        {
            "id": 216859933,
            "user": {
                "id": 9000000,
                "username": "mrWoo0"
            },
            "comment": "testest2",
            "score": 5,
            "created_at": "2020-05-26T12:35:09.323348+09:00",
            "updated_at": "2020-05-26T12:39:03.941535+09:00",
            "movie": 85579
        }
        ```

    - POST 요청과 마찬가지로 필수 항목 - movie, score 를 보내지 않으면 400

        ```json
        {
            "movie": [
                "이 필드는 필수 항목입니다."
            ]
        }
        ```

    - rating 작성자 user_id 와 요청을 보낸 user_id가 일치하지 않으면 400

        ```json
        {
            "message": "권한이 없습니다."
        }
        ```

- DELETE  `movie/rating/<int:rating_id>/`   영화 리뷰 삭제하기  👌
    - IsAuthenticated
    - Request
    - Response

        ```json
        204 --- data 없음
        ```

    - PATCH 와 마찬가지로 작성자와 요청자가 일치하지 않으면 400

- GET  `movie/<int:movie_id>/onscreen/`  상영중인 영화 영화관 정보 찾기 👌
    - IsAuthenticated
    - Request
    - Response

        ```
        {
            "area": [
                "강남구",
                "광진구",
                "구로구",
                "종로구",
                "중구",
                "강서구",
                "양천구",
                "강북구",
                "은평구",
                "중랑구",
                "성북구",
                "송파구",
                "서대문구",
                "영등포구",
                "성동구",
                "용산구",
                "노원구",
                "강동구",
                "마포구",
                "서초구",
                "동작구",
                "도봉구",
                "금천구",
                "관악구",
                "동대문구"
            ],
            "data": [
                {
                    "id": 1,
                    "area": "강남구",
                    "name": "CGV 강남",
                    "address": "서울 강남구 강남대로 438",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVgangnam.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0056"
                },
                {
                    "id": 2,
                    "area": "광진구",
                    "name": "CGV 강변",
                    "address": "서울 광진구 광나루로56길 85",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2019/0107/15468415578940.png",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0001"
                },
                {
                    "id": 3,
                    "area": "광진구",
                    "name": "CGV 건대입구",
                    "address": "서울 광진구 아차산로30길 26",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2018/0212/15184234292340.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0229"
                },
                {
                    "id": 4,
                    "area": "구로구",
                    "name": "CGV 구로",
                    "address": "서울 구로구 구로중앙로 152",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/noimage_final(40).jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0010"
                },
                {
                    "id": 5,
                    "area": "종로구",
                    "name": "CGV 대학로",
                    "address": "서울 종로구 대명길 28",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2015/1027/%EB%8C%80%ED%95%99%EB%A1%9C%EB%AC%B8%ED%99%94%EA%B7%B9%EC%9E%A504.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0063"
                },
                {
                    "id": 6,
                    "area": "중구",
                    "name": "CGV 동대문",
                    "address": "서울 중구 장충단로13길 20",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2017/1218/15135627350570.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0252"
                },
                {
                    "id": 7,
                    "area": "강서구",
                    "name": "CGV 등촌",
                    "address": "서울 강서구 공항대로45길 63",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2019/0411/15549505447290.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0230"
                },
                {
                    "id": 8,
                    "area": "중구",
                    "name": "CGV 명동",
                    "address": "서울 중구 명동길 14",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVmyeongdong.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0009"
                },
                {
                    "id": 10,
                    "area": "양천구",
                    "name": "CGV 목동",
                    "address": "서울 양천구 목동동로 257",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/noimage_final(42).jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0011"
                },
                {
                    "id": 11,
                    "area": "강북구",
                    "name": "CGV 미아",
                    "address": "서울 강북구 도봉로 34",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVmia.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0057"
                },
                {
                    "id": 12,
                    "area": "은평구",
                    "name": "CGV 불광",
                    "address": "서울 은평구 불광로 20",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/noimage_final(43).jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0030"
                },
                {
                    "id": 13,
                    "area": "중랑구",
                    "name": "CGV 상봉",
                    "address": "서울 중랑구 상봉로 131",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2016/0216/sangbong_1.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0046"
                },
                {
                    "id": 14,
                    "area": "성북구",
                    "name": "CGV 성신여대입구",
                    "address": "서울 성북구 동소문로 106",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2019/1001/15699285160670.png",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0300"
                },
                {
                    "id": 15,
                    "area": "송파구",
                    "name": "CGV 송파",
                    "address": "서울 송파구 충민로 66",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVsongpa.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0088"
                },
                {
                    "id": 16,
                    "area": "강북구",
                    "name": "CGV 수유",
                    "address": "서울 강북구 도봉로 399",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2018/0319/15214226265340.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0276"
                },
                {
                    "id": 17,
                    "area": "서대문구",
                    "name": "CGV 신촌아트레온",
                    "address": "서울 서대문구 신촌로 129",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVsinchonartreon.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0150"
                },
                {
                    "id": 18,
                    "area": "강남구",
                    "name": "CGV 압구정",
                    "address": "서울 강남구 압구정로30길 45",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2017/0308/14889569732790.JPG",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0040"
                },
                {
                    "id": 19,
                    "area": "영등포구",
                    "name": "CGV 여의도",
                    "address": "서울 영등포구 국제금융로 10",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/R2014/images/sub/specialtheater/yeouido/yeouido01.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0112"
                },
                {
                    "id": 20,
                    "area": "영등포구",
                    "name": "CGV 영등포",
                    "address": "서울 영등포구 영중로 15",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/cgvyoungdeungpo.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0059"
                },
                {
                    "id": 21,
                    "area": "성동구",
                    "name": "CGV 왕십리",
                    "address": "서울 성동구 왕십리광장로 17",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2020/0120/15794807818480.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0074"
                },
                {
                    "id": 22,
                    "area": "용산구",
                    "name": "CGV 용산아이파크몰",
                    "address": "서울 용산구 한강대로23길 55",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2017/1020/15084871764830.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013"
                },
                {
                    "id": 23,
                    "area": "노원구",
                    "name": "CGV 중계",
                    "address": "서울 노원구 동일로204가길 12",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/cgvjunggae.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0131"
                },
                {
                    "id": 24,
                    "area": "강동구",
                    "name": "CGV 천호",
                    "address": "서울 강동구 양재대로 1571",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2015/0710/CGV%EC%B2%9C%ED%98%B8%20_%EA%B7%B9%EC%9E%A5%EC%86%8C%EA%B0%9C%20_%EC%8A%A4%ED%94%BC%EC%96%B4%EC%97%91%EC%8A%A4.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0199"
                },
                {
                    "id": 25,
                    "area": "강남구",
                    "name": "CGV 청담씨네시티",
                    "address": "서울 강남구 도산대로 323",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/R2014/images/sub/specialtheater/chungdam/main_chungdam.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0107"
                },
                {
                    "id": 26,
                    "area": "종로구",
                    "name": "CGV 피카디리1958",
                    "address": "서울 종로구 돈화문로5가길 1",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2016/0218/picadiri.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0223"
                },
                {
                    "id": 27,
                    "area": "노원구",
                    "name": "CGV 하계",
                    "address": "서울 노원구 섬밭로 258",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/cgvhagae.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0164"
                },
                {
                    "id": 28,
                    "area": "마포구",
                    "name": "CGV 홍대",
                    "address": "서울 마포구 양화로 153",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/cgvhongdae.jpg",
                    "url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0191"
                },
                {
                    "id": 29,
                    "area": "강남구",
                    "name": "씨네드쉐프 압구정",
                    "address": "서울 강남구 압구정로30길 45",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2017/0308/14889569732790.JPG",
                    "url": "http://www.cgv.co.kr/theaters/special/show-times.aspx?regioncode=103&theatercode=0040"
                },
                {
                    "id": 30,
                    "area": "용산구",
                    "name": "씨네드쉐프 용산아이파크몰",
                    "address": "서울 용산구 한강대로23길 55",
                    "type": "CGV",
                    "img": "http://img.cgv.co.kr/Theater/Theater/2017/1020/15084871764830.jpg",
                    "url": "http://www.cgv.co.kr/theaters/special/show-times.aspx?regioncode=103&theatercode=0013"
                },
                {
                    "id": 31,
                    "area": "서초구",
                    "name": "메가박스 강남",
                    "address": "서울 서초구 서초대로77길 3",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1372"
                },
                {
                    "id": 32,
                    "area": "강남구",
                    "name": "메가박스 강남대로(씨티)",
                    "address": "서울 강남구 강남대로 422",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1359"
                },
                {
                    "id": 33,
                    "area": "강동구",
                    "name": "메가박스 강동",
                    "address": "서울 강동구 성내로 48",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1341"
                },
                {
                    "id": 34,
                    "area": "광진구",
                    "name": "메가박스 군자",
                    "address": "서울 광진구 능동로 289",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1431"
                },
                {
                    "id": 35,
                    "area": "중구",
                    "name": "메가박스 동대문",
                    "address": "서울 중구 장충단로 247",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1003"
                },
                {
                    "id": 36,
                    "area": "강서구",
                    "name": "메가박스 마곡",
                    "address": "서울 강서구 공항대로 247",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1572"
                },
                {
                    "id": 37,
                    "area": "양천구",
                    "name": "메가박스 목동",
                    "address": "서울 양천구 목동동로 309",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1581"
                },
                {
                    "id": 38,
                    "area": "중랑구",
                    "name": "메가박스 상봉",
                    "address": "서울 중랑구 망우로30길 3",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1311"
                },
                {
                    "id": 39,
                    "area": "마포구",
                    "name": "메가박스 상암월드컵경기장",
                    "address": "서울 마포구 월드컵로 240",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1211"
                },
                {
                    "id": 40,
                    "area": "성동구",
                    "name": "메가박스 성수",
                    "address": "서울 성동구 왕십리로 50",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1331"
                },
                {
                    "id": 41,
                    "area": "서초구",
                    "name": "메가박스 센트럴",
                    "address": "서울 서초구 신반포로 176",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1371"
                },
                {
                    "id": 42,
                    "area": "송파구",
                    "name": "메가박스 송파파크하비오",
                    "address": "서울 송파구 송파대로 111",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1381"
                },
                {
                    "id": 43,
                    "area": "서대문구",
                    "name": "메가박스 신촌",
                    "address": "서울 서대문구 신촌역로 30",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1202"
                },
                {
                    "id": 45,
                    "area": "동작구",
                    "name": "메가박스 이수",
                    "address": "서울 동작구 동작대로 89",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1561"
                },
                {
                    "id": 46,
                    "area": "도봉구",
                    "name": "메가박스 창동",
                    "address": "서울 도봉구 도봉로 558",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1321"
                },
                {
                    "id": 47,
                    "area": "강남구",
                    "name": "메가박스 코엑스",
                    "address": "서울 강남구 영동대로 513",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1351"
                },
                {
                    "id": 48,
                    "area": "마포구",
                    "name": "메가박스 홍대",
                    "address": "서울 마포구 양화로 147",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1212"
                },
                {
                    "id": 49,
                    "area": "강서구",
                    "name": "메가박스 화곡",
                    "address": "서울 강서구 화곡로 142",
                    "type": "메가박스",
                    "img": "https://image2.megabox.co.kr/mop/home/appbunpage/URLVIEW.jpg",
                    "url": "https://www.megabox.co.kr/theater/time?brchNo=1571"
                },
                {
                    "id": 51,
                    "area": "금천구",
                    "name": "롯데시네마 가산디지털",
                    "address": "서울 금천구 디지털로10길 9",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1013"
                },
                {
                    "id": 52,
                    "area": "강서구",
                    "name": "롯데시네마 가양",
                    "address": "서울 강서구 양천로 476",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1018"
                },
                {
                    "id": 53,
                    "area": "강동구",
                    "name": "롯데시네마 강동",
                    "address": "서울 강동구 천호옛길 85",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=9010"
                },
                {
                    "id": 54,
                    "area": "광진구",
                    "name": "롯데시네마 건대입구",
                    "address": "서울 광진구 아차산로 272",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1004"
                },
                {
                    "id": 55,
                    "area": "강서구",
                    "name": "롯데시네마 김포공항",
                    "address": "서울 강서구 하늘길 지하 77",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1009"
                },
                {
                    "id": 56,
                    "area": "노원구",
                    "name": "롯데시네마 노원",
                    "address": "서울 노원구 동일로 1414",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1003"
                },
                {
                    "id": 57,
                    "area": "금천구",
                    "name": "롯데시네마 독산",
                    "address": "서울 금천구 시흥대로 399",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1017"
                },
                {
                    "id": 58,
                    "area": "강남구",
                    "name": "롯데시네마 브로드웨이(신사)",
                    "address": "서울 강남구 도산대로8길 8",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=9056"
                },
                {
                    "id": 59,
                    "area": "관악구",
                    "name": "롯데시네마 서울대입구",
                    "address": "서울 관악구 남부순환로 1820",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1012"
                },
                {
                    "id": 60,
                    "area": "노원구",
                    "name": "롯데시네마 수락산",
                    "address": "서울 노원구 동일로 1660",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1019"
                },
                {
                    "id": 61,
                    "area": "강북구",
                    "name": "롯데시네마 수유",
                    "address": "서울 강북구 도봉로 308",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1022"
                },
                {
                    "id": 62,
                    "area": "구로구",
                    "name": "롯데시네마 신도림",
                    "address": "서울 구로구 경인로 662",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1015"
                },
                {
                    "id": 63,
                    "area": "관악구",
                    "name": "롯데시네마 신림",
                    "address": "서울 관악구 신림로 330",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1007"
                },
                {
                    "id": 64,
                    "area": "중구",
                    "name": "롯데시네마 에비뉴엘(명동)",
                    "address": "서울 중구 남대문로 73",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1001"
                },
                {
                    "id": 65,
                    "area": "영등포구",
                    "name": "롯데시네마 영등포",
                    "address": "서울 영등포구 경인로 846",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1002"
                },
                {
                    "id": 66,
                    "area": "용산구",
                    "name": "롯데시네마 용산",
                    "address": "서울 용산구 청파로 74",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1014"
                },
                {
                    "id": 67,
                    "area": "송파구",
                    "name": "롯데시네마 월드타워",
                    "address": "서울 송파구 올림픽로 300",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1016"
                },
                {
                    "id": 68,
                    "area": "은평구",
                    "name": "롯데시네마 은평(롯데몰)",
                    "address": "서울 은평구 통일로 1050",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1021"
                },
                {
                    "id": 69,
                    "area": "동대문구",
                    "name": "롯데시네마 장안",
                    "address": "서울 동대문구 답십리로 288",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=9053"
                },
                {
                    "id": 70,
                    "area": "동대문구",
                    "name": "롯데시네마 청량리",
                    "address": "서울 동대문구 왕산로 214",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1008"
                },
                {
                    "id": 71,
                    "area": "마포구",
                    "name": "롯데시네마 합정",
                    "address": "서울 마포구 양화로 45",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1010"
                },
                {
                    "id": 72,
                    "area": "마포구",
                    "name": "롯데시네마 홍대입구",
                    "address": "서울 마포구 양화로 176",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1005"
                },
                {
                    "id": 73,
                    "area": "중구",
                    "name": "롯데시네마 황학",
                    "address": "서울 중구 청계천로 400",
                    "type": "롯데시네마",
                    "img": "https://lh3.googleusercontent.com/QghPZ2dGHR9ni0n4-tclx0P4yjW3k3ry4rZMNKOlj3wpMug8dwmp8fHOXzK8tq5sO5I",
                    "url": "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1011"
                },
                {
                    "id": 74,
                    "area": "중구",
                    "name": "대한극장(서울)",
                    "address": "서울 중구 퇴계로 212",
                    "type": "기타",
                    "img": "http://www.daehancinema.co.kr/images/dh_photo07.jpg",
                    "url": "http://www.daehancinema.co.kr/Reserve/Reserve_Play.asp"
                }
            ]
        }
        ```

- GET `movie/<int:movie_id>/score/`   영화 평균 평점 👌
    - IsAuthenticated
    - Response

        ```sql
        http://localhost:8000/movie/85579/score/

        {
            "score": 3.15
        }
        ```

---

# Model

1. User
2. Movie

    ```python
    {
        "id": 85579,
        "directors": [
          "김용화"
        ],
        "genres": [
          "판타지",
          "서부"
        ],
        "actors": [
          "차태현",
          "하정우",
          "김동욱",
          "주지훈",
          "김향기"
        ],
        "name": "신과함께-죄와 벌",
        "name_eng": "Along With the Gods: The Two Worlds",
        "watch_grade": "12세 관람가",
        "running_time": "139분",
        "summary": "저승 법에 의하면, 모든 인간은 사후 49일 동안 7번의 재판을 거쳐야만 한다. 살인, 나태, 거짓, 불의, 배신, 폭력, 천륜 7개의 지옥에서 7번의 재판을 무사히 통과한 망자만이 환생하여 새로운 삶을 시작할 수 있다.   “김자홍 씨께선, 오늘 예정 대로 무사히 사망하셨습니다”  화재 사고 현장에서 여자아이를 구하고 죽음을 맞이한 소방관 자홍, 그의 앞에 저승차사 해원맥과 덕춘이 나타난다. 자신의 죽음이 아직 믿기지도 않는데 덕춘은 정의로운 망자이자 귀인이라며 그를 치켜세운다. 저승으로 가는 입구, 초군문에서 그를 기다리는 또 한 명의 차사 강림, 그는 차사들의 리더이자 앞으로 자홍이 겪어야 할 7개의 재판에서 변호를 맡아줄 변호사이기도 하다. 염라대왕에게 천년 동안 49명의 망자를 환생시키면 자신들 역시 인간으로 환생시켜 주겠다는 약속을 받은 삼차사들, 그들은 자신들이 변호하고 호위해야 하는 48번째 망자이자 19년 만에 나타난 의로운 귀인 자홍의 환생을 확신하지만, 각 지옥에서 자홍의 과거가 하나 둘씩 드러나면서 예상치 못한 고난과 맞닥뜨리는데…  누구나 가지만 아무도 본 적 없는 곳, 새로운 세계의 문이 열린다!",
        "open_date": "2017-12-20",
        "trailer": "https://www.youtube.com/embed/sD7dmu-IWNw",
        "poster": "https://movie-phinf.pstatic.net/20171201_181/1512109983114kcQVl_JPEG/movie_image.jpg"
     }
    ```

3. Cinema

    ```python
    {
    			"region": "서울",
    			"area": "강남구",
    			"name": "CGV강남",
    			"code": "0056",
    			"tel": "1544-1122",
    			"address": "서울 강남구 강남대로 438",
    			"x": "127.026391177132",
    			"y": "37.5016573944824",
    			"url": "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0056",
    			"public": "# 지하철\n2호선 | 강남역 11번 출구\n9호선 | 신논현역 5번출구\n\n# 버스\n- 분당지역\n   좌석버스: 1005-1, 1005-2, 6800, 5500-2\n   간선버스: 408, 462\n   광역버스: 9404, 9408\n- 강북지역\n   간선버스: 140, 144, 145, 471\n- 강서지역\n   좌석버스: 1500\n   간선버스: 360\n- 강동지역\n   간선버스: 402, 420, 470, 407\n- 인근경기지역\n   좌석버스: 3030, 2002, 2002-1\n   광역버스: 9409, 9500, 9501, 9503, 9700, 9711",
    			"parking": "# 주차정보\n- 위치: 건물 지하2F ~ 지하4F\n\n# 주차요금\n- CGV 영화 관람 시 주차 3시간 6,000원\n- 주차시간 (3시간) 초과 시 10분 당 1,000원\n※ 발렛서비스 운영시간 : 오전 8시 이후 ~ 오후 20시\n※ 발렛 무료 서비스는 영화 관람 고객 한 함.  (영화 미관람 시 건물 주차장에서 별도 정산)\n※ 20시 이후 입차 차량은 발렛서비스 이용이 제한될 수 있으며, 별도 운영되는 주차팀의 사정에 따라 변경될 수 있습니다.\n\n# 이용안내\n- 주차공간이 협소하여 평일 오후/주말은 주차가 어렵습니다.\n- 편리한 대중교통 이용을 이용하여 주시기 바랍니다.",
    			"type": "CGV",
    			"img": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVgangnam.jpg"
    		}
    ```