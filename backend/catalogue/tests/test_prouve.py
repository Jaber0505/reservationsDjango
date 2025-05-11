from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from catalogue.models import Artist

class TestPagination(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Crée 15 artistes
        for i in range(15):
            Artist.objects.create(firstname=f"A{i}", lastname="Test")

    def test_page_size_returns_exactly_10(self):
        response = self.client.get('/catalogue/api/artists/')
        self.assertEqual(response.status_code, 200)

        firstnames = [a['firstname'] for a in response.data['results']]
        print("===> NOMBRE D'ARTISTES RETOURNÉS :", len(firstnames))
        print("===> PRENOMS :", firstnames)

        self.assertEqual(len(firstnames), 10)
