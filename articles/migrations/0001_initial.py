# Generated by Django 5.0.4 on 2024-04-27 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="images/")),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("tags", models.ManyToManyField(to="articles.tag")),
            ],
        ),
    ]
