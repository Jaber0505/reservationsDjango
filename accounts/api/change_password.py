from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse

from accounts.serializers.password import PasswordChangeSerializer

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Changer son mot de passe",
        request=PasswordChangeSerializer,
        responses={
            200: OpenApiResponse(description="Mot de passe modifié avec succès"),
            400: OpenApiResponse(description="Erreur de validation"),
            401: OpenApiResponse(description="Non authentifié"),
        },
        description="Permet à l'utilisateur connecté de modifier son mot de passe.",
    )
    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Mot de passe modifié avec succès."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)