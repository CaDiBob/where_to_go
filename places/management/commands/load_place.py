import os
import json
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place


def get_json(json_url):
    response = requests.get(json_url)
    response.raise_for_status()
    answer = response.json()
    return answer


def save_to_db(json_url):
    place = get_json(json_url)
    new_place = Place(
        title=place['title'],
        description_short=place['description_short'],
        description_long=place['description_long'],
        lng=place['coordinates']['lng'],
        lat=place['coordinates']['lat'],
    )
    new_place.save()

    for number, img in enumerate(place['imgs'], 1):
        response = requests.get(img)
        response.raise_for_status()
        image = response.content
        image = Image()
        image.image.save(f'image{number}.jpeg',
                         ContentFile(response.content),
                         save=False)
        image.place = new_place
        image.save()


class Command(BaseCommand):

    help = 'Testing'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='?', type=str)

    def handle(self, *args, **options):
        try:
            save_to_db(options['url'])
            print('Локация успешно добавлена.')
        except json.decoder.JSONDecodeError:
            print('Что-то пошло не так! Проверте ссылку и повторите.')
        except requests.exceptions.ConnectionError:
            print('Что-то пошло не так! Проверте ссылку и повторите.')
        except requests.exceptions.MissingSchema:
            print('Что-то пошло не так! Проверте ссылку и повторите.')
