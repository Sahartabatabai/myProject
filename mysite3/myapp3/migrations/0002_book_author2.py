# Generated by Django 4.2.5 on 2023-10-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp3", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author2",
            field=models.CharField(default="", max_length=20),
        ),
    ]
