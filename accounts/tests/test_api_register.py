from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Tests de l'API d'inscription utilisateur (/accounts/api/register/)
class RegisterAPITests(APITestCase):

    # Vérifie qu'un utilisateur peut s'inscrire avec des données valides
    def test_user_can_register(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "secure123"
        }
        response = self.client.post('/accounts/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    # Vérifie que l'API retourne 400 si le champ username est manquant
    def test_missing_username_returns_400(self):
        data = {
            "email": "incomplete@example.com",
            "password": "test123"
        }
        response = self.client.post('/accounts/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Vérifie que l'API rejette une adresse e-mail déjà utilisée
    def test_email_already_used(self):
        User.objects.create_user(username="existing", email="used@example.com", password="123456")
        data = {
            "username": "otheruser",
            "email": "used@example.com",
            "password": "testpass"
        }
        response = self.client.post('/accounts/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    # Vérifie que l'API rejette un nom d'utilisateur déjà utilisé
    def test_username_already_used(self):
        User.objects.create_user(username="duplicate", email="u1@example.com", password="123456")
        data = {
            "username": "duplicate",
            "email": "u2@example.com",
            "password": "testpass"
        }
        response = self.client.post('/accounts/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)

    # Vérifie que l'API rejette un mot de passe trop court
    def test_short_password_rejected(self):
        data = {
            "username": "badpass",
            "email": "badpass@example.com",
            "password": "12"
        }
        response = self.client.post('/accounts/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
