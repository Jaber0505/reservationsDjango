from rest_framework import serializers
from catalogues.models.price import Price

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'type', 'price', 'description', 'start_date', 'end_date']
