# Generated by Django 3.0.2 on 2020-01-23 14:15

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0007_auto_20200109_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='learned_list',
            field=tinymce.models.HTMLField(blank=True, help_text='Things that I learned during the development of this experiment?'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='published_date',
            field=models.DateTimeField(help_text='When was this experiment created?'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='struggled_list',
            field=tinymce.models.HTMLField(blank=True, help_text='Things that I struggled with during the development of this experiment?'),
        ),
    ]
