# Generated by Django 4.0.1 on 2022-10-02 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newfeed', '0008_post_content_image_alter_post_content_time_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_content',
            name='time_create',
        ),
    ]
