from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from catalogues.models.artist import Artist

class ArtistListCreateAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="testpass")
        cls.admin = User.objects.create_user(username="adminuser", password="adminpass", is_staff=True)

        cls.artist1 = Artist.objects.create(firstname="Alice", lastname="Smith")
        cls.artist2 = Artist.objects.create(firstname="Bob", lastname="Johnson")
        cls.artist3 = Artist.objects.create(firstname="Charlie", lastname="Brown")

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_artists(self):
        url = reverse('catalogues_api:artist-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 3)

    def test_search_artist(self):
        url = reverse('catalogues_api:artist-list') + '?search=Alice'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["firstname"], "Alice")

    def test_ordering_artists(self):
        url = reverse('catalogues_api:artist-list') + '?ordering=firstname'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["firstname"], "Alice")

    def test_create_artist_success(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('catalogues_api:artist-list')
        data = {"firstname": "David", "lastname": "Martin"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 4)

    def test_create_artist_missing_field(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('catalogues_api:artist-list')
        data = {"firstname": ""}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthenticated_create(self):
        self.client.force_authenticate(user=None)
        url = reverse('catalogues_api:artist-list')
        data = {"firstname": "Eve", "lastname": "White"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_hypermedia_links_present(self):
        url = reverse('catalogues_api:artist-list')
        response = self.client.get(url)
        self.assertIn("url", response.data["results"][0])

    def test_update_artist_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        artist = Artist.objects.first()
        url = reverse('catalogues_api:artist-detail', args=[artist.pk])
        data = {"firstname": "Updated", "lastname": artist.lastname}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_artist_as_user_denied(self):
        artist = Artist.objects.first()
        url = reverse('catalogues_api:artist-detail', args=[artist.pk])
        data = {"firstname": "Hack", "lastname": "Trick"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_artist_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        artist = Artist.objects.first()
        url = reverse('catalogues_api:artist-detail', args=[artist.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_artist_as_user_denied(self):
        artist = Artist.objects.first()
        url = reverse('catalogues_api:artist-detail', args=[artist.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
