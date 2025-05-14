from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context['request'].user

        # Vérifie que l'ancien mot de passe est correct
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({'old_password': 'Ancien mot de passe incorrect.'})

        # Vérifie que les deux nouveaux mots de passe correspondent
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': 'Les mots de passe ne correspondent pas.'})

        # Applique les règles de sécurité de Django (longueur, complexité, etc.)
        try:
            validate_password(data['new_password'], user=user)
        except DjangoValidationError as e:
            raise serializers.ValidationError({'new_password': e.messages})

        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
