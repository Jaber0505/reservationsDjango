from rest_framework import generics
from catalogues.models.location import Location
from catalogues.serializers.location_serializer import LocationSerializer

# Vue pour lister et créer des locations
class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()  # Récupérer toutes les locations
    serializer_class = LocationSerializer  # Utiliser le serializer LocationSerializer
