from rest_framework import serializers
from django.contrib.auth.models import User

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context['request'].user

        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({'old_password': 'Ancien mot de passe incorrect.'})

        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': 'Les mots de passe ne correspondent pas.'})

        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
