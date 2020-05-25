from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'accounts/view/', views.AccountViewSet, basename='test')
# router.register(r'admin', views.AdminUserViewSet)

urlpatterns = [
    # path('', views.signup),
    path('login/', obtain_jwt_token),
    path('', views.AccountView.as_view()),

    # 회원가입시 최초 레이팅 페이지
    # path('rating/init/'),
    path('login/rating/', views.get_rating_tf, name='get_rating_tf'),
    # 로그인시 레이팅 페이지
]
