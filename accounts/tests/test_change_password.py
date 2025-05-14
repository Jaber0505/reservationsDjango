from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Tests de l'API de changement de mot de passe (/accounts/api/change-password/)
class ChangePasswordTests(APITestCase):

    # Initialise un utilisateur et l'authentifie avec un token JWT
    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@test.com', password='oldpass')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    # Vérifie que le mot de passe est changé correctement avec les bonnes données
    def test_change_password_success(self):
        response = self.client.post('/accounts/api/change-password/', {
            'old_password': 'oldpass',
            'new_password': 'newpass123',
            'new_password2': 'newpass123',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Vérifie que l'ancien mot de passe incorrect renvoie une erreur 400
    def test_change_password_invalid_old(self):
        response = self.client.post('/accounts/api/change-password/', {
            'old_password': 'wrongpass',
            'new_password': 'newpass123',
            'new_password2': 'newpass123',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
