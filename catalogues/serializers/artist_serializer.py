# catalogues/serializers/artist_serializer.py
from rest_framework import serializers
from catalogues.models.artist import Artist
from catalogues.models.type import Type

class ArtistTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'type']

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    # Lecture : liste des types avec leurs détails
    types = ArtistTypeSerializer(many=True, read_only=True)
    # Écriture : envoi d'une liste d'IDs
    type_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Type.objects.all(),
        write_only=True,
        source='types'  # Lie à la relation ManyToMany "types"
    )

    class Meta:
        model = Artist
        fields = ['url', 'id', 'firstname', 'lastname', 'types', 'type_ids']
        extra_kwargs = {
            'url': {'view_name': 'catalogues_api:artist-detail', 'lookup_field': 'pk'}
        }
