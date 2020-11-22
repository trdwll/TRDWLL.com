# Generated by Django 3.1 on 2020-11-21 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRDWLL', '0010_auto_20201101_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorPageHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When the visitor viewed the page.')),
                ('ip_address', models.GenericIPAddressField(help_text='The IP address of the visitor.')),
                ('ip_country', models.CharField(help_text='The country location of the ip address.', max_length=100)),
                ('page_url', models.CharField(help_text='The url that was accessed.', max_length=200)),
                ('user_agent', models.CharField(help_text='The useragent that the visitor is using.', max_length=300)),
                ('referer', models.CharField(blank=True, default='', help_text='The page that this visitor came from.', max_length=150)),
            ],
            options={
                'db_table': 'analytics_visitorpagehit',
                'ordering': ['-created'],
            },
        ),
    ]
