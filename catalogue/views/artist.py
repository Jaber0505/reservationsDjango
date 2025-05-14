from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from catalogue.forms import ArtistForm
from catalogue.models import Artist, Type
#from accounts.permissions import group_required

# Affiche la liste de tous les artistes
def index(request):
    artists = Artist.objects.all()
    return render(request, 'artist/index.html', {'artists': artists})

# Affiche les détails d’un artiste donné
def show(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'artist/show.html', {'artist': artist})

# Édite un artiste (accessible uniquement aux membres du groupe ADMIN connectés)
@login_required
#@group_required('ADMIN')
def edit(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)

    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, "Artiste modifié avec succès.")
            return redirect('catalogue:artist-show', artist.id)
        else:
            messages.error(request, "Échec de la modification de l’artiste.")

    return render(request, 'artist/edit.html', {'artist': artist})

# Supprime un artiste (seulement via POST, pour un ADMIN connecté)
@login_required
#@group_required('ADMIN')
def delete(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)

    if request.method == "POST":
        artist.delete()
        messages.success(request, "Artiste supprimé avec succès.")
        return redirect("catalogue:artist-index")
    else:
        messages.error(request, "Échec de la suppression : requête invalide.")
        return redirect("catalogue:artist-show", artist_id)

# Crée un nouvel artiste (réservé aux ADMIN connectés)
@login_required
#@group_required('ADMIN')
def create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nouvel artiste créé avec succès.")
            return redirect('catalogue:artist-index')
        else:
            messages.error(request, "Échec de la création de l’artiste.")
    else:
        form = ArtistForm()

    return render(request, 'artist/create.html', {'form': form})
