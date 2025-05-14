from rest_framework import generics
from catalogues.models.reservation_representation import ReservationRepresentation
from catalogues.serializers.reservation_representation_serializer import ReservationRepresentationSerializer

class ReservationRepresentationListCreateView(generics.ListCreateAPIView):
    queryset = ReservationRepresentation.objects.all()
    serializer_class = ReservationRepresentationSerializer

class ReservationRepresentationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReservationRepresentation.objects.all()
    serializer_class = ReservationRepresentationSerializer
