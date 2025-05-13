from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class ChangePasswordTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@test.com', password='oldpass')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_change_password_success(self):
        response = self.client.post('/accounts/api/change-password/', {
            'old_password': 'oldpass',
            'new_password': 'newpass123',
            'new_password2': 'newpass123',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_password_invalid_old(self):
        response = self.client.post('/accounts/api/change-password/', {
            'old_password': 'wrongpass',
            'new_password': 'newpass123',
            'new_password2': 'newpass123',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
