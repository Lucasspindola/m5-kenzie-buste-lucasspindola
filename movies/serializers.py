from rest_framework import serializers
from .models import RatingsChoices, Movie, MovieOrder
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        allow_null=True,
        default=None,
    )
    rating = serializers.ChoiceField(
        choices=RatingsChoices.choices,
        default=RatingsChoices.G,
        allow_null=True,
    )
    synopsis = serializers.CharField(
        allow_null=True,
        default=None,
    )
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, req) -> str:
        return req.user.email

    def create(self, validated_data):
        return Movie.objects.create(
            **validated_data,
        )


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=8)
    title = serializers.CharField(read_only=True, allow_null=True, source="movie.title")
    buyed_by = serializers.CharField(read_only=True, source="user.email")
    buyed_at = serializers.DateTimeField(read_only=True, allow_null=True)

    def create(self, validated_data):
        order_movie = MovieOrder.objects.create(**validated_data)
        return order_movie
