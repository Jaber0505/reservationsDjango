from django.shortcuts import render
from django.http import Http404

from catalogue.models.price import Price

def index(request):
    prices = Price.objects.all()
    return render(request, "price/index.html", {
        "prices": prices,
        "title": "Liste des tarifs"
    })

def show(request, price_id):
    try:
        price = Price.objects.get(pk=price_id)
    except Price.DoesNotExist:
        raise Http404("Tarif inexistant")
    
    return render(request, "price/show.html", {
        "price": price,
        "title": "Fiche d'un tarif"
    })
