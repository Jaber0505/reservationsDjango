from django.shortcuts import render, redirect, get_object_or_404
from catalogue.forms import ArtistForm
from catalogue.models import Artist

def index(request):
    artists = Artist.objects.all()
    return render(request, 'artist/index.html', {'artists': artists})

def show(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'artist/show.html', {'artist': artist})

def edit(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)

    if request.method == "POST":
        artist.firstname = request.POST.get("firstname")
        artist.lastname = request.POST.get("lastname")
        artist.save()
        return redirect("catalogue:artist-show", artist_id)

    return render(request, 'artist/edit.html', {'artist': artist})

def delete(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)

    if request.method == "POST":
        artist.delete()
        return redirect("catalogue:artist-index")

    return redirect("catalogue:artist-show", artist_id)

def create(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('catalogue:artist-show', artist.id)
    else:
        form = ArtistForm()

    return render(request, 'artist/create.html', {'form': form})
