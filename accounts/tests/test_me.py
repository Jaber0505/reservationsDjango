from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse

from django.contrib.auth.models import User
from accounts.serializers.user import UserUpdateSerializer

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Voir son profil utilisateur",
        responses={200: UserUpdateSerializer},
        description="Retourne le profil (username et email) de l'utilisateur connecté."
    )
    def get(self, request):
        serializer = UserUpdateSerializer(request.user)
        return Response(serializer.data)

    @extend_schema(
        summary="Modifier son profil",
        request=UserUpdateSerializer,
        responses={
            200: UserUpdateSerializer,
            400: OpenApiResponse(description="Données invalides")
        },
        description="Met à jour le username et l'email de l'utilisateur connecté."
    )
    def put(self, request):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Supprimer son compte",
        responses={
            204: OpenApiResponse(description="Compte supprimé avec succès"),
        },
        description="Supprime définitivement le compte de l'utilisateur connecté."
    )
    def delete(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
