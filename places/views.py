import json
import os

from django.http import JsonResponse
from places.models import Places

from django.shortcuts import render
from django.shortcuts import get_object_or_404


def show_palaces(request):
    detail = os.path.join('static', 'places')
    places = Places.objects.all()
    places_info = {
        'type': 'FeatureCollection',
        'features': []
    }
    for place in places:
        feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': os.path.join(
                        'static', 'places', 'moscow_legends.json'
                    )
                }
            }
        places_info['features'].append(feature)
    context = {'places_info': places_info}

    return render(request, 'index.html', context)


def get_place(place):
    place_detail = {
        'title': place.title,
        'imgs': [img.image.url for img in place.collection.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        }
    }
    return place_detail


def show_place(request, place_id):
    place = get_object_or_404(Places, pk=place_id)
    return JsonResponse(
        get_place(place), json_dumps_params={'ensure_ascii': False, 'indent': 4}
        )
