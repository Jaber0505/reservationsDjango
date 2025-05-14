from rest_framework import generics
from catalogues.models.artist_type import ArtistType
from catalogues.serializers.artist_type_serializer import ArtistTypeSerializer

# Vue pour lister et créer des relations entre artistes et types
class ArtistTypeListCreateView(generics.ListCreateAPIView):
    queryset = ArtistType.objects.all()  # Récupérer toutes les relations entre artistes et types
    serializer_class = ArtistTypeSerializer  # Utiliser le sérialiseur ArtistTypeSerializer
