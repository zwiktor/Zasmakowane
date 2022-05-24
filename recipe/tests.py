from django.test import TestCase, Client
from recipe.models import Recipe


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


class RecipeModelTestCase(TestCase):

    def test_default_recipe(self):
        recipe = Recipe()
        self.assertEqual(recipe.title, 'Przepis')
        self.assertEqual(recipe.description, 'krotki opis')
