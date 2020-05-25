from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.get_cinema, name='get_cinema'),
    path('map/<int:cinema_id>/movie/', views.get_fast_movie, name='get_fast_movie'),
]
