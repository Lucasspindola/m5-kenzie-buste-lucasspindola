from django.db import models


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
    