from rest_framework import serializers
from catalogues.models.reservation import Reservation
from catalogues.models.representation import Representation
from catalogues.serializers.representation_serializer import RepresentationSerializer

class ReservationSerializer(serializers.ModelSerializer):
    representations = RepresentationSerializer(many=True)  # Sérialisation des représentations associées à la réservation

    class Meta:
        model = Reservation
        fields = ['id', 'booking_date', 'status', 'user', 'representations']
