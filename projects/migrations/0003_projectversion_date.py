# Generated by Django 2.2.1 on 2019-05-27 03:04

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectversion',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
    ]
