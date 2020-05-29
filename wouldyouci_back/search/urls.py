from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.autocomplete_movie, name='autocomplete_movie'),
    path('movie/<str:words>/', views.search_movie, name='search_movie'),
    # path('', views.SearchView.as_view()),
]
