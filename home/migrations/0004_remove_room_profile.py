# Generated by Django 2.2.5 on 2019-12-14 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_room_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='profile',
        ),
    ]
