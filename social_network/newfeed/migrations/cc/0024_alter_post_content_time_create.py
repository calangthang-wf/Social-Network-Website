# Generated by Django 4.0.1 on 2022-10-19 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfeed', '0023_alter_post_content_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_content',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 10, 46, 58, 583193)),
        ),
    ]
