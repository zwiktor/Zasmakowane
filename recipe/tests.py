from django.test import TestCase, Client
from recipe.models import Recipe, Cuisine, Tag, Category


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


class CuisineModelTestCase(TestCase):

    def test_cuisine_model(self):
        cuisine = Cuisine(name='Włoska')
        self.assertIsInstance(cuisine, Cuisine)
        self.assertEqual(cuisine.name, 'Włoska')
        self.assertEqual(str(cuisine), 'Włoska')

class TagModelTestCase(TestCase):

    def test_tag_model(self):
        tag = Tag(name='Vege')
        self.assertIsInstance(tag, Tag)
        self.assertEqual(tag.name, 'Vege')
        self.assertEqual(str(tag), 'Vege')

class CategoryModelTestCase(TestCase):

    def test_category_model(self):
        cat = Category(name='Obiad')
        self.assertIsInstance(cat, Category)
        self.assertEqual(cat.name, 'Obiad')
        self.assertEqual(str(cat), 'Obiad')
