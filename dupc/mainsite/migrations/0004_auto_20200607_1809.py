# Generated by Django 3.0.6 on 2020-06-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20200605_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
