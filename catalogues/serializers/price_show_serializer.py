from rest_framework import serializers
from catalogues.models.price_show import PriceShow
from catalogues.serializers.show_serializer import ShowSerializer  # Serializer pour Show
from catalogues.serializers.price_serializer import PriceSerializer  # Serializer pour Price

class PriceShowSerializer(serializers.ModelSerializer):
    show = ShowSerializer()  # Inclure les informations de Show dans la réponse
    price = PriceSerializer()  # Inclure les informations de Price dans la réponse

    class Meta:
        model = PriceShow
        fields = ['id', 'show', 'price']
