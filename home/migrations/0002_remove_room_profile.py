# Generated by Django 2.2.5 on 2019-12-09 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='profile',
        ),
    ]
