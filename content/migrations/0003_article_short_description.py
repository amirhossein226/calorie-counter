# Generated by Django 4.2.6 on 2023-11-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_rename_amount_of_food_enten_foodeaten_amount_of_food_eaten"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="short_description",
            field=models.CharField(default=" ", max_length=250),
        ),
    ]
