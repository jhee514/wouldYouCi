from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'', views.ProfileViewSet, basename='profile')
# router.register(r'movie/rating', views.RatingViewSet)

urlpatterns = [
    # path('profile/', include(router.urls)),
    path('signup/', views.create_user, name='create_user'),
    path('login/', obtain_jwt_token),

    path('', views.user_detail, name='user_detail'),
    path('profile/', views.change_profile, name='change_profile'),
    path('password/', views.change_password, name='change_password'),

    # rating tf
    path('login/rating/', views.get_rating_tf, name='get_rating_tf'),
]
