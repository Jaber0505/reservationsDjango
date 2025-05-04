from django.shortcuts import render
from django.http import Http404

from catalogue.models import Locality

def index(request):
    localities = Locality.objects.all()
    return render(request, "locality/index.html", {
        "localities": localities,
        "title": "Liste des localités"
    })

def show(request, locality_id):
    try:
        locality = Locality.objects.get(pk=locality_id)
    except Locality.DoesNotExist:
        raise Http404("Localité inexistante")
    
    return render(request, "locality/show.html", {
        "locality": locality,
        "title": "Fiche d'une localité"
    })
