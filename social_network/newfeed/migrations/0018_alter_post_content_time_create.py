# Generated by Django 4.0.1 on 2022-10-05 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfeed', '0017_alter_post_content_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_content',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 3, 18, 8, 200652)),
        ),
    ]
