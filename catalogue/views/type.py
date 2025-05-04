from django.shortcuts import render, get_object_or_404
from catalogue.models import Type

# Affiche la liste de tous les types
def index(request):
    types = Type.objects.all()
    return render(request, "type/index.html", {"types": types})

# Affiche un type spécifique selon son ID
def show(request, type_id):
    type_obj = get_object_or_404(Type, pk=type_id)
    return render(request, "type/show.html", {"type": type_obj})
