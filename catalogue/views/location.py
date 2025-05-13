from django.shortcuts import render, get_object_or_404

from catalogue.models.location import Location

def index(request):
    locations = Location.objects.all()
    return render(request, 'location/index.html', {
        'locations': locations,
        'title': 'Lieux de spectacle'
    })

def show(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    return render(request, 'location/show.html', {
        'location': location,
        'title': 'Détails du lieu'
    })
