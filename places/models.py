from django.db import models


class Places(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.CharField('Короткое описание', max_length=250)
    description_long = models.TextField('Описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    places = models.ForeignKey(
        Places, verbose_name='Места', on_delete=models.CASCADE, related_name='collection'
    )
    image = models.ImageField('Картинка')
    object_id = models.PositiveIntegerField(verbose_name='Позиция', blank=True, default=0)

    class Meta:
        ordering = ['object_id']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.places.title
