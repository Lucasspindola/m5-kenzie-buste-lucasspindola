# Generated by Django 4.1.7 on 2023-02-22 00:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_alter_movie_synopsis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(blank=True, null=True),
        ),
    ]
