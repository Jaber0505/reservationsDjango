from rest_framework import serializers
from catalogues.models.type import Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'type']
