from rest_framework import serializers
from catalogues.models.representation import Representation
from catalogues.serializers.show_serializer import ShowSerializer
from catalogues.serializers.location_serializer import LocationSerializer

class RepresentationSerializer(serializers.ModelSerializer):
    show = ShowSerializer()  # Serialisation de l'objet Show
    location = LocationSerializer()  # Serialisation de l'objet Location

    class Meta:
        model = Representation
        fields = ['id', 'show', 'schedule', 'location']
