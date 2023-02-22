from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from users.permissions import IsAdminOrReadOnly, isAnAuthorizedUser
from django.shortcuts import get_object_or_404
import ipdb


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    # def patch(self, req: Request, pet_id: int):
    #     ...
    # return Response(serializer.data, status.HTTP_200_OK)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def delete(self, req: Request, movie_id: int):
        movie_delete_exists = get_object_or_404(Movie, id=movie_id)
        movie_delete_exists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, req: Request, movie_id: int):
        movie_exists = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie_exists)
        return Response(serializer.data, status.HTTP_200_OK)


class MovieOrderView(APIView):
    # Apenas autenticado
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAnAuthorizedUser]

    def post(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        user_order = req.user
        serializer = MovieOrderSerializer(data=req.data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save(user=user_order, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)


