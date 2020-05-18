from django.contrib import admin
from .models import Genre, People, Movie


class GenreModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


class PeopleModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


class MovieModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


admin.site.register(Genre, GenreModelAdmin)
admin.site.register(Movie, MovieModelAdmin)
admin.site.register(People, PeopleModelAdmin)
