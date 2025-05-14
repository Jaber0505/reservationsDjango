from rest_framework import serializers
from catalogues.models.artist_type import ArtistType
from catalogues.models.artist import Artist
from catalogues.models.type import Type

# Serializer pour le modèle Artist
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'firstname', 'lastname']

# Serializer pour le modèle Type
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'type']

# Serializer pour le modèle ArtistType
class ArtistTypeSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()  # Sérialisation de l'artiste
    type = TypeSerializer()  # Sérialisation du type

    class Meta:
        model = ArtistType
        fields = ['id', 'artist', 'type']
