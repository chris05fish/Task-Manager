# Generated by Django 3.0.9 on 2021-03-24 20:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='TasksEntry',
        ),
    ]
