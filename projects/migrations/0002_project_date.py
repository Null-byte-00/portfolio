# Generated by Django 5.0.4 on 2024-05-01 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
