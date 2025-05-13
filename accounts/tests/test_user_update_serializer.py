from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from accounts.serializers.user import UserUpdateSerializer

class UserUpdateSerializerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            first_name='Jean',
            last_name='Dupont',
            password='testpass'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='testpass'
        )

    def test_valid_update(self):
        data = {
            'username': 'user1',
            'email': 'user1@example.com',
            'first_name': 'Jean',
            'last_name': 'Dupont'
        }
        serializer = UserUpdateSerializer(instance=self.user, data=data, context={'request': self.request_mock()}, partial=True)
        self.assertTrue(serializer.is_valid())

    def test_duplicate_email(self):
        data = {
            'email': 'other@example.com'
        }
        serializer = UserUpdateSerializer(instance=self.user, data=data, context={'request': self.request_mock()}, partial=True)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_duplicate_username(self):
        data = {
            'username': 'otheruser'
        }
        serializer = UserUpdateSerializer(instance=self.user, data=data, context={'request': self.request_mock()}, partial=True)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_short_username(self):
        data = {
            'username': 'ab'
        }
        serializer = UserUpdateSerializer(instance=self.user, data=data, context={'request': self.request_mock()}, partial=True)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_invalid_first_name(self):
        data = {
            'first_name': 'Jean123'
        }
        serializer = UserUpdateSerializer(instance=self.user, data=data, context={'request': self.request_mock()}, partial=True)
        self.assertFalse(serializer.is_valid())
        self.assertIn('first_name', serializer.errors)

    def test_invalid_last_name(self):
        data = {
            'last_name': '@Dupont!'
        }
        serializer = UserUpdateSerializer(instance=self.user, data=data, context={'request': self.request_mock()}, partial=True)
        self.assertFalse(serializer.is_valid())
        self.assertIn('last_name', serializer.errors)

    def request_mock(self):
        class DummyRequest:
            user = self.user
        return DummyRequest()
