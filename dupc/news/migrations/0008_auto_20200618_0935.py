# Generated by Django 3.0.6 on 2020-06-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='day',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='news',
            name='month',
            field=models.CharField(default='june', max_length=50),
        ),
        migrations.AddField(
            model_name='news',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
