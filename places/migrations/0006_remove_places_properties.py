# Generated by Django 4.0.3 on 2022-05-01 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_places_properties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='properties',
        ),
    ]