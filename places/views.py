from audioop import reverse

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places import views
from places.models import Place


def show_palaces(request):
    places = Place.objects.all()
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
                    'detailsUrl': reverse(
                        views.show_place, kwargs={'place_id':place.id}
                    ),
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
    place = get_object_or_404(Place, pk=place_id)
    return JsonResponse(
        get_place(place), json_dumps_params={'ensure_ascii': False, 'indent': 4}
        )
