from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
