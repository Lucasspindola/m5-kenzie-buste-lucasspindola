from django.urls import path
from . import views
from .views import MovieDetailView
urlpatterns = [
    path("movies/", views.MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),
]
