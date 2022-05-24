from django.test import TestCase, Client

class UrlTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_list = [
            '',
            '/przepisy'
        ]

    def test_200_status_for_get_requests(self):
        for url in self.url_list:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    # def test_template_name(self):
    #     for url in self.url_list:
    #         response = self.client.get(url)
    #         self.assertEqual(response.templates, 200)