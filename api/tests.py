from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from accounts.models import UserProfile
from django.test import TestCase

class MyAPITest(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_authenticated_request(self):
        response = self.client.get('/api/some-endpoint/')
        self.assertEqual(response.status_code, 200)
