# Generated by Django 3.2.16 on 2022-10-25 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newfeed', '0025_alter_post_content_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comment',
            name='user_name',
            field=models.ForeignKey(blank=True, default=django_currentuser.middleware.get_current_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
