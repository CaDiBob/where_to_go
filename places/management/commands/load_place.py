import os
import json
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place


class Command(BaseCommand):

    help = 'Testing'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='?', type=str)

    def dowload_json(self, json_url):
        response = requests.get(json_url)
        response.raise_for_status()
        with open('place.json', 'w') as file:
            file.write(response.text)

    def handle(self, *args, **options):

        self.dowload_json(options['url'])

        with open('place.json', 'r') as file:
            place = json.load(file)
        new_place = Place(
            title=place['title'],
            description_short=place['description_short'],
            description_long=place['description_long'],
            lng=place['coordinates']['lng'],
            lat=place['coordinates']['lat'],
        )
        new_place.save()

        for number, img in enumerate(place['imgs'], 1):
            try:
                response = requests.get(img)
                response.raise_for_status()
                image = response.content
                image = Image()
                image.image.save(f'image{number}.jpeg',
                                 ContentFile(response.content),
                                 save=False)
                image.place = new_place
                image.save()
            except Exception:
                continue

        os.remove('place.json')

        print('Локация успешно добавлена.')
