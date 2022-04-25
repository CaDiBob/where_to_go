from django.db import models

class Places(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.CharField('Короткое описание', max_length=250)
    description_long = models.TextField('Описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title
