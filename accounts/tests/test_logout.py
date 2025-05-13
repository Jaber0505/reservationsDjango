from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

class LogoutViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.refresh = RefreshToken.for_user(self.user)
        self.access = self.refresh.access_token

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access}')

    def test_logout_success(self):
        response = self.client.post('/accounts/api/logout/', {
            'refresh': str(self.refresh)
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Déconnexion réussie.')

        # Vérifie que le token est bien blacklisté
        self.assertTrue(
            BlacklistedToken.objects.filter(token__jti=self.refresh['jti']).exists()
        )

    def test_logout_missing_token(self):
        response = self.client.post('/accounts/api/logout/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("refresh", response.data['error'])

    def test_logout_invalid_token(self):
        response = self.client.post('/accounts/api/logout/', {
            'refresh': 'invalidtokenvalue'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Token invalide", response.data['error'])
