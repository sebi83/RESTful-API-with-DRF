# Generated by Django 4.0.4 on 2022-05-26 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("body", models.TextField(blank=True, max_length=1000, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        default="1",
                        null="True",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.usermodel",
                    ),
                ),
            ],
        ),
    ]
