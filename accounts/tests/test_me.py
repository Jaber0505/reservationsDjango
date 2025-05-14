from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# Tests pour la vue /accounts/api/me/ (profil utilisateur connecté)
class MeViewTests(APITestCase):

    # Crée un utilisateur et l'authentifie avec un token JWT
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            first_name="Jean",
            last_name="Dupont"
        )
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    # Vérifie que le profil est bien retourné pour l'utilisateur connecté
    def test_get_profile(self):
        response = self.client.get('/accounts/api/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['email'], self.user.email)

    # Vérifie que l'utilisateur peut modifier son prénom et email
    def test_update_profile(self):
        data = {
            "first_name": "Nouveau",
            "last_name": "Nom",
            "email": "new@example.com"
        }
        response = self.client.put('/accounts/api/me/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Nouveau")
        self.assertEqual(self.user.email, "new@example.com")

    # Vérifie que l'utilisateur peut supprimer son compte
    def test_delete_account(self):
        response = self.client.delete('/accounts/api/me/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
