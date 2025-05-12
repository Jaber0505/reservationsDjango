from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class RegisterAPITests(APITestCase):
    def test_user_can_register(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "secure123"
        }
        response = self.client.post('/accounts/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_missing_username_returns_400(self):
        data = {
            "email": "incomplete@example.com",
            "password": "test123"
        }
        response = self.client.post('/accounts/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
