# Generated by Django 5.0 on 2023-12-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_pictures"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
