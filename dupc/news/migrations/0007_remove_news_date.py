# Generated by Django 3.0.6 on 2020-06-18 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
    ]
