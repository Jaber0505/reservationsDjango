from django.shortcuts import render, get_object_or_404

from catalogue.models.show import Show

def detail(request, show_id):
    # Récupère le show par son ID
    show = get_object_or_404(Show, id=show_id)

    # Récupère tous les prix associés à ce show
    prices = show.prices.all()

    # Affiche les données dans le template
    return render(request, 'show/show_detail.html', {
        'show': show,
        'prices': prices,
    })
