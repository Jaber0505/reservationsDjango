from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# Tests de l'endpoint /accounts/api/token/refresh/
class TokenRefreshTests(APITestCase):

    # Crée un utilisateur avec refresh token
    def setUp(self):
        self.user = User.objects.create_user(username='jaber', password='secure123')
        self.refresh_token = str(RefreshToken.for_user(self.user))

    # Vérifie que le refresh token retourne un nouveau access token
    def test_refresh_token_valid(self):
        response = self.client.post('/accounts/api/token/refresh/', {
            'refresh': self.refresh_token
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    # Vérifie que l'API retourne une erreur si le token est manquant
    def test_refresh_token_missing(self):
        response = self.client.post('/accounts/api/token/refresh/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Vérifie que l'API retourne une erreur si le token est invalide
    def test_refresh_token_invalid(self):
        response = self.client.post('/accounts/api/token/refresh/', {
            'refresh': 'invalid.token.value'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
