# Generated by Django 4.1.7 on 2023-02-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_birthdate_user_is_employee_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=models.BooleanField(default=False)),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]