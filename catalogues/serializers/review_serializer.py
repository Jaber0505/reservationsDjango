from rest_framework import serializers
from catalogues.models.review import Review
from catalogues.serializers.show_serializer import ShowSerializer
from accounts.serializers.user import UserDetailSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    show = ShowSerializer()

    class Meta:
        model = Review
        fields = ['id', 'user', 'show', 'review', 'stars', 'validated', 'created_at', 'updated_at']
