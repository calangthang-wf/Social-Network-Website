# Generated by Django 3.2.16 on 2022-11-11 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newfeed', '0002_post_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='newfeed.post_content'),
        ),
    ]
