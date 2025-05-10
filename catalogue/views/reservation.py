from django.shortcuts import render, get_object_or_404

from catalogue.models.reservation import Reservation

def reservation_index(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation/index.html', {
        'reservations': reservations,
    })

def reservation_detail(request, reservation_id):
    # Récupère la réservation par son ID
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    # Récupère toutes les représentations associées à cette réservation
    representations = reservation.representations.all()
    
    # Afficher les données dans le template
    return render(request, 'reservation/show.html', {
        'reservation': reservation,
        'representations': representations,
    })
