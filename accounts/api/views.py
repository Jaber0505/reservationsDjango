from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers.register import RegisterSerializer
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

@extend_schema(
    request=RegisterSerializer,
    responses={201: dict, 400: dict},
    description="Créer un nouvel utilisateur et retourner les tokens JWT"
)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Utilisateur créé avec succès.",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "username": user.username
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "username": user.username})
        return Response({"error": "Identifiants invalides"}, status=status.HTTP_401_UNAUTHORIZED)