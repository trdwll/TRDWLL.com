# Generated by Django 3.1 on 2020-10-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0012_auto_20201024_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='download_link',
            field=models.URLField(blank=True, help_text='A link to download this experiment. (should really be just a link to the repo if any)', null=True),
        ),
    ]
