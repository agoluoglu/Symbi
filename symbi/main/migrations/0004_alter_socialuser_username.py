# Generated by Django 4.2.6 on 2023-11-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_interesttag_socialuser_age_socialuser_major_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="socialuser",
            name="username",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]