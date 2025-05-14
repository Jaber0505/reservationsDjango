from rest_framework import generics
from catalogues.models.price_show import PriceShow
from catalogues.serializers.price_show_serializer import PriceShowSerializer

# Vue pour lister et créer des PriceShow
class PriceShowListCreateView(generics.ListCreateAPIView):
    queryset = PriceShow.objects.all()  # Récupérer tous les PriceShow
    serializer_class = PriceShowSerializer  # Utiliser le serializer PriceShowSerializer
