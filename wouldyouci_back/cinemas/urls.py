from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.get_cinema_width, name='get_cinema_width'),
    path('map/center/', views.get_cinema_center, name='get_cinema_center'),
    path('map/<int:cinema_id>/movie/', views.get_fast_movie, name='get_fast_movie'),
]
