from django.test import TestCase, Client

class HomePageTestCase(TestCase):

    def test_open_home_page(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hi')