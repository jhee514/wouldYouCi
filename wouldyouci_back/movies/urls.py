from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'', views.MovieViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'', views.RatingViewSet, basename="rating")

# urlpatterns = router.urls


urlpatterns = [
    path('rating/page/', include(router.urls)),
    # 상세정보
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    # 찜하기
    path('<int:movie_id>/pick/', views.pick_movie, name='pick_movie'),

    # 영화 레이팅
    path('rating/', views.create_rating, name='create_rating'),
    path('rating/<int:rating_id>/', views.patch_delete_rating, name='path_delete_rating'),
]
