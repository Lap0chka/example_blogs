# Generated by Django 5.0 on 2023-12-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_post_tags_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="view",
            field=models.PositiveIntegerField(default=114),
        ),
    ]