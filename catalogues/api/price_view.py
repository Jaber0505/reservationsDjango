from rest_framework import generics
from catalogues.models.price import Price
from catalogues.serializers.price_serializer import PriceSerializer

# Vue pour lister, créer, mettre à jour et supprimer les Price
class PriceListCreateView(generics.ListCreateAPIView):
    queryset = Price.objects.all()  # Récupérer tous les prix
    serializer_class = PriceSerializer  # Utiliser le serializer PriceSerializer

class PriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()  # Récupérer un seul prix pour la mise à jour ou suppression
    serializer_class = PriceSerializer  # Utiliser le serializer PriceSerializer
