# Generated by Django 2.2 on 2020-08-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0005_remove_publication_admin_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='body',
            field=models.TextField(default=False, max_length=5000),
        ),
    ]
