from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# Tests des erreurs courantes de l'endpoint /accounts/api/change-password/
class ChangePasswordErrorTests(APITestCase):

    # Crée un utilisateur et le connecte via JWT
    def setUp(self):
        self.user = User.objects.create_user(username='jaber', password='secure123')
        token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    # Vérifie que si les nouveaux mots de passe ne correspondent pas, l'API retourne une erreur
    def test_new_passwords_do_not_match(self):
        response = self.client.post('/accounts/api/change-password/', {
            'old_password': 'secure123',
            'new_password': 'abc123456',
            'new_password2': 'xyz123456',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("new_password2", response.data)

    # Vérifie que l'API retourne une erreur si un champ est manquant
    def test_missing_fields(self):
        response = self.client.post('/accounts/api/change-password/', {
            'old_password': 'secure123',
            'new_password': 'abc123456'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
