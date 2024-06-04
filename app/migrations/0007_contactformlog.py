# Generated by Django 5.0.4 on 2024-05-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_frequentlyaskquestion_frequentlyaskedquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('action_time', models.DateTimeField(blank=True, null=True)),
                ('is_success', models.BooleanField(default=False)),
                ('is_error', models.BooleanField(default=False)),
            ],
        ),
    ]
