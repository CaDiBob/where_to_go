# Generated by Django 4.0.3 on 2022-04-30 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_options_image_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='places',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='places.places', verbose_name='Места'),
        ),
    ]
