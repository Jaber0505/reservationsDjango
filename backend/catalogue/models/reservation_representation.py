from django.db import models

from catalogue.models.reservation import Reservation
from catalogue.models.representation import Representation

class ReservationRepresentation(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservation_representations")
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, related_name="representation_reservations")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reservation {self.reservation.id} - Representation {self.representation.id}"

    class Meta:
        db_table = "reservation_representation"
