from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse

from django.contrib.auth.models import User
from accounts.serializers.user import UserDetailSerializer, UserUpdateSerializer


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Voir son profil utilisateur",
        responses={
            200: UserDetailSerializer,
            401: OpenApiResponse(description="Non authentifié"),
        },
        description="Retourne le prénom, nom, email, username et la date d'inscription de l'utilisateur connecté.",
    )
    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

    @extend_schema(
        summary="Modifier son profil",
        request=UserUpdateSerializer,
        responses={
            200: UserUpdateSerializer,
            400: OpenApiResponse(description="Erreur de validation"),
            401: OpenApiResponse(description="Non authentifié"),
        },
        description="Permet de modifier le nom, prénom, nom d'utilisateur et adresse email du compte connecté.",
    )
    def put(self, request):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Supprimer son compte utilisateur",
        responses={
            204: OpenApiResponse(description="Compte supprimé avec succès"),
            401: OpenApiResponse(description="Non authentifié"),
        },
        description="Supprime définitivement le compte de l'utilisateur connecté.",
    )
    def delete(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
