from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

# Tests de l'API de déconnexion sécurisée (blacklist du refresh token)
class LogoutViewTests(APITestCase):

    # Crée un utilisateur et génère un access + refresh token pour l'authentification
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.refresh = RefreshToken.for_user(self.user)
        self.access = self.refresh.access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access}')

    # Vérifie que la déconnexion réussit et que le refresh token est blacklisté
    def test_logout_success(self):
        response = self.client.post('/accounts/api/token/logout/', {
            'refresh': str(self.refresh)
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Déconnexion réussie.')
        self.assertTrue(
            BlacklistedToken.objects.filter(token__jti=self.refresh['jti']).exists()
        )

    # Vérifie que l'API retourne 400 si le token est manquant
    def test_logout_missing_token(self):
        response = self.client.post('/accounts/api/token/logout/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("refresh", response.data['error'])

    # Vérifie que l'API retourne 400 si le token est invalide
    def test_logout_invalid_token(self):
        response = self.client.post('/accounts/api/token/logout/', {
            'refresh': 'invalidtokenvalue'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Token invalide", response.data['error'])
