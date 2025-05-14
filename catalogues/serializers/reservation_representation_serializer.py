from rest_framework import serializers
from catalogues.models.reservation_representation import ReservationRepresentation
from catalogues.serializers.reservation_serializer import ReservationSerializer
from catalogues.serializers.representation_serializer import RepresentationSerializer

class ReservationRepresentationSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer()  # Serialisation de l'objet Reservation
    representation = RepresentationSerializer()  # Serialisation de l'objet Representation

    class Meta:
        model = ReservationRepresentation
        fields = ['id', 'reservation', 'representation', 'quantity', 'price']
