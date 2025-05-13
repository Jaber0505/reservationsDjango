from django.contrib.auth.models import User
from rest_framework import serializers
import re

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def validate_email(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError("Cette adresse email est déjà utilisée.")
        return value

    def validate_username(self, value):
        user = self.context["request"].user
        if len(value) < 4:
            raise serializers.ValidationError("Le nom d'utilisateur doit contenir au moins 4 caractères.")
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà utilisé.")
        return value

    def validate_first_name(self, value):
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ \-]+$", value):
            raise serializers.ValidationError("Le prénom ne doit contenir que des lettres, espaces ou tirets.")
        return value

    def validate_last_name(self, value):
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ \-]+$", value):
            raise serializers.ValidationError("Le nom ne doit contenir que des lettres, espaces ou tirets.")
        return value

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
        )
        read_only_fields = fields