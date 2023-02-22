from rest_framework import serializers
from .models import RatingsChoices, Movie
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
        # print(validated_data,)
        # ipdb.set_trace()
        return Movie.objects.create(**validated_data, )
        added_by_obj = validated_data.user.email
        movie = Movie.objects.create(**validated_data, added_by=added_by_obj)
        return movie
