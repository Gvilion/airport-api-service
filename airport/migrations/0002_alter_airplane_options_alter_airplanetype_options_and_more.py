# Generated by Django 4.2.4 on 2023-08-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("airport", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="airplane",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="airplanetype",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="airport",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="crew",
            options={"ordering": ["first_name", "last_name"]},
        ),
        migrations.AlterModelOptions(
            name="flight",
            options={"ordering": ["-departure_time"]},
        ),
        migrations.AlterModelOptions(
            name="route",
            options={"ordering": ["source", "destination"]},
        ),
        migrations.AddField(
            model_name="flight",
            name="crew",
            field=models.ManyToManyField(related_name="flights", to="airport.crew"),
        ),
        migrations.AlterUniqueTogether(
            name="route",
            unique_together={("source", "destination")},
        ),
    ]
