# Generated by Django 2.1.4 on 2024-05-12 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240511_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='permission',
            field=models.IntegerField(default=0),
        ),
    ]