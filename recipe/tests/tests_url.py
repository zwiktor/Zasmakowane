from django.test import TestCase, Client
from recipe.models import Recipe


class UrlTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        recipe = Recipe(title='Tytul Przepisu', description='krotki opis przepisu')
        recipe.save()

        self.url_list = [
            '',
            '/przepisy',
            '/omnie',
            f'/przepisy/{recipe.slug}',
            f'/przepisy/{recipe.slug}/edit',
            f'/przepisy/{recipe.slug}/delete',
            '/przepisy/new'
        ]

    def test_200_status_for_get_requests(self):
        for url in self.url_list:
            print(url)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

class HomePageTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.response = self.client.get('')

    def test_template(self):
        self.assertTemplateUsed(self.response, 'Home.html')

    def test_form(self):
        pass

    def test_html(self):
        self.assertContains(self.response, 'Przepisy')

    def test_csrf(self):
        pass