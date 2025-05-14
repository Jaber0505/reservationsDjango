from rest_framework import generics
from catalogues.models.locality import Locality
from catalogues.serializers.locality_serializer import LocalitySerializer

# Vue pour lister et créer des localités
class LocalityListCreateView(generics.ListCreateAPIView):
    queryset = Locality.objects.all()  # Récupérer toutes les localités
    serializer_class = LocalitySerializer  # Utiliser le sérialiseur LocalitySerializer
