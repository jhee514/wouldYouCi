from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.get_cinema, name='get_cinema'),
]

# Create your views here.
