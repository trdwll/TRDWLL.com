# Generated by Django 3.1 on 2020-12-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRDWLL', '0013_alert_short_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorpagehit',
            name='theme',
            field=models.CharField(blank=True, help_text='What theme is this visitor using?', max_length=32),
        ),
    ]
