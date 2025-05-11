from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from catalogue.models import Artist

class TestArtistAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_artist(self):
        response = self.client.post('/catalogue/api/artists/', {
            'firstname': 'Amy',
            'lastname': 'Winehouse'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_filter_artist_by_firstname(self):
        # Setup: 2 artistes
        Artist.objects.create(firstname='Amy', lastname='Winehouse')
        Artist.objects.create(firstname='Kurt', lastname='Cobain')

        # Appel filtré
        response = self.client.get('/catalogue/api/artists/?firstname=Amy')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['firstname'], 'Amy')
