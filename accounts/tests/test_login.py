from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


# Tests de l'endpoint /accounts/api/token/ (connexion)
class LoginTests(APITestCase):

    # Crée un utilisateur avec un mot de passe connu
    def setUp(self):
        self.user = User.objects.create_user(username='jaber', password='secure123')

    # Vérifie qu'un utilisateur peut se connecter avec ses identifiants
    def test_login_success(self):
        data = {
            "username": "jaber",
            "password": "secure123"
        }
        response = self.client.post('/accounts/api/token/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    # Vérifie que l'API retourne une erreur si le mot de passe est incorrect
    def test_login_wrong_password(self):
        data = {
            "username": "jaber",
            "password": "wrongpassword"
        }
        response = self.client.post('/accounts/api/token/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Vérifie que l'API retourne une erreur si les champs sont manquants
    def test_login_missing_fields(self):
        response = self.client.post('/accounts/api/token/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
