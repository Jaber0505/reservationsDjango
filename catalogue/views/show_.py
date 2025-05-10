from django.shortcuts import render, get_object_or_404

from catalogue.models.show import Show

def index(request):
    shows = Show.objects.all()
    return render(request, 'show/index.html', {
        'shows': shows,
        'title': 'Liste des spectacles'
    })

def show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    return render(request, 'show/show.html', {
        'show': show,
        'title': f"Spectacle : {show.title}"
    })
