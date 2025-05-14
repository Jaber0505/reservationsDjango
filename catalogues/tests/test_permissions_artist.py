from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User, Group
from django.urls import reverse
from catalogues.models.artist import Artist


class ArtistPermissionsAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Création des utilisateurs
        cls.user = User.objects.create_user(username="user", password="pass")
        cls.admin = User.objects.create_user(username="admin", password="adminpass", is_staff=True)
        cls.organizer = User.objects.create_user(username="organizer", password="organizerpass")

        # Création du groupe "Organisateur" et ajout de l’utilisateur dedans
        group = Group.objects.create(name="Organisateur")
        cls.organizer.groups.add(group)

        # Un artiste pour les tests de modification/suppression
        cls.artist = Artist.objects.create(firstname="Jean", lastname="Dupont")

    def setUp(self):
        self.client = APIClient()

    def test_authenticated_user_cannot_create_artist(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("catalogues_api:artist-list")
        data = {"firstname": "Paul", "lastname": "Martin"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_organizer_can_create_artist(self):
        self.client.force_authenticate(user=self.organizer)
        url = reverse("catalogues_api:artist-list")
        data = {"firstname": "Paul", "lastname": "Martin"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_can_create_artist(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse("catalogues_api:artist-list")
        data = {"firstname": "Paul", "lastname": "Martin"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authenticated_user_can_view_artists(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("catalogues_api:artist-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_organizer_can_update_artist(self):
        self.client.force_authenticate(user=self.organizer)
        url = reverse("catalogues_api:artist-detail", args=[self.artist.id])
        data = {"firstname": "Jean-Modif", "lastname": "Dupont"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_can_delete_artist(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse("catalogues_api:artist-detail", args=[self.artist.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_cannot_view_artists(self):
        url = reverse("catalogues_api:artist-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
