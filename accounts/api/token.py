from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from accounts.serializers.token import CustomTokenObtainPairSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse

# Serializer pour documenter l'entrée attendue
class LogoutTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

@extend_schema(
    summary="Déconnexion (blacklist du refresh token)",
    operation_id="logout_user",
    description="Blacklist le refresh token de l'utilisateur afin de l'invalider après sa déconnexion.",
    request=LogoutTokenSerializer,
    responses={
        200: OpenApiResponse(description="Déconnexion réussie"),
        400: OpenApiResponse(description="Refresh token invalide ou déjà blacklisté"),
        401: OpenApiResponse(description="Non authentifié"),
    }
)
class LogoutTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Déconnexion réussie"}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"error": "Le champ 'refresh' est requis."}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"error": "Token invalide ou déjà blacklisté."}, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    summary="Connexion",
    operation_id="login_user",
    description="Authentifie un utilisateur et retourne les tokens JWT (access + refresh), ainsi que son nom d'utilisateur.",
    responses={
        200: OpenApiResponse(description="Connexion réussie (access + refresh tokens retournés)"),
        401: OpenApiResponse(description="Identifiants invalides"),
    }
)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@extend_schema(
    summary="Renouvellement du token d'accès",
    operation_id="refresh_token",
    description="Utilise un refresh token JWT valide pour retourner un nouveau access token.",
    request=TokenRefreshSerializer,
    responses={
        200: OpenApiResponse(description="Access token renouvelé"),
        401: OpenApiResponse(description="Refresh token invalide ou expiré"),
    }
)
class CustomTokenRefreshView(TokenRefreshView):
    pass