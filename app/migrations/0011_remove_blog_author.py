# Generated by Django 5.0.4 on 2024-05-06 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
