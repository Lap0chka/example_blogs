# Generated by Django 5.0 on 2023-12-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="pictures",
            field=models.ImageField(blank=True, null=True, upload_to="post"),
        ),
    ]
