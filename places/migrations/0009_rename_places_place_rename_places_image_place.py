# Generated by Django 4.0.3 on 2022-05-03 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_places_description_long'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Places',
            new_name='Place',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='places',
            new_name='place',
        ),
    ]
