# Generated by Django 2.2.6 on 2019-11-17 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20191113_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photos',
        ),
    ]