from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Déconnexion de l'utilisateur",
        request=None,
        responses={
            200: OpenApiResponse(description="Déconnexion réussie"),
            400: OpenApiResponse(description="Token invalide"),
            401: OpenApiResponse(description="Non authentifié"),
        },
        description="Blacklist le refresh token pour invalider la session de l'utilisateur.",
    )
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Déconnexion réussie."}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"error": "Le champ 'refresh' est requis."}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"error": "Token invalide ou déjà blacklisté."}, status=status.HTTP_400_BAD_REQUEST)
