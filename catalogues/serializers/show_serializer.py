from rest_framework import serializers
from catalogues.models.show import Show
from catalogues.models.location import Location
from catalogues.models.price import Price

class ShowSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField()  # Affiche la représentation de la localisation
    prices = serializers.StringRelatedField(many=True)  # Affiche les prix associés au show

    class Meta:
        model = Show
        fields = ['id', 'slug', 'title', 'description', 'poster_url', 'duration', 'created_in', 'location', 'bookable', 'prices', 'created_at', 'updated_at']
