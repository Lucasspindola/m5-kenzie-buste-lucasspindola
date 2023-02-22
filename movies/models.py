from django.db import models
from users.models import User


class RatingsChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default=None, blank=True)
    rating = models.CharField(
        max_length=20,
        default=RatingsChoices.G,
        choices=RatingsChoices.choices,
        blank=True,
    )
    synopsis = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        "users.User",
        related_name="movie",
        on_delete=models.CASCADE,
        null=True,
    )


class MovieOrder(models.Model):
    price = models.DecimalField(decimal_places=2, null=False, max_digits=8)
    buyed_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
