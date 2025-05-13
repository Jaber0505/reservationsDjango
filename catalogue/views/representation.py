from django.shortcuts import render, get_object_or_404

from catalogue.models.representation import Representation

def index(request):
    representations = Representation.objects.all()
    return render(request, 'representation/index.html', {
        'representations': representations,
        'title': 'Liste des représentations'
    })

def show(request, representation_id):
    representation = get_object_or_404(Representation, id=representation_id)
    return render(request, 'representation/show.html', {
        'representation': representation,
        'title': "Détails de la représentation"
    })
