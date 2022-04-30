import os
from tkinter import Place
from django.shortcuts import render

from places.models import Places

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
