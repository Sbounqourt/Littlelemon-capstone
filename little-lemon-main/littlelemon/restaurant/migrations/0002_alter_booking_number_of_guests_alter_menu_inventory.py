# Generated by Django 5.1 on 2024-09-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="number_of_guests",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="menu",
            name="inventory",
            field=models.IntegerField(),
        ),
    ]
