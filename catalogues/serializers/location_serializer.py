from rest_framework import serializers
from catalogues.models.location import Location
from catalogues.serializers.locality_serializer import LocalitySerializer  # On inclut aussi le serializer pour Locality

class LocationSerializer(serializers.ModelSerializer):
    locality = LocalitySerializer()  # Inclure les informations de Locality dans la réponse

    class Meta:
        model = Location
        fields = ['id', 'slug', 'designation', 'address', 'locality', 'website', 'phone']
