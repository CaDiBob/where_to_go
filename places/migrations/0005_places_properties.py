# Generated by Django 4.0.3 on 2022-05-01 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='properties',
            field=models.TextField(blank=True, verbose_name='Свойства'),
        ),
    ]
