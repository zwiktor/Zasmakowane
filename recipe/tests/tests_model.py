from django.test import TestCase, Client
from recipe.models import Recipe, Cuisine, Tag, Category, Ingredient, Step


class RecipeModelTestCase(TestCase):

    def test_default_recipe(self):
        recipe = Recipe()
        self.assertEqual(recipe.title, 'Przepis')
        self.assertEqual(recipe.description, 'krotki opis')


class CuisineModelTestCase(TestCase):

    def setUp(self):
        self.recipe = Recipe(title='Tytul Przepisu', description='krotki opis przepisu')
        self.cuisine = Cuisine(name='Wloska')
        self.cuisine2 = Cuisine(name='Fusion')
        self.recipe.save()
        self.cuisine.save()
        self.cuisine2.save()

    def test_cuisine_model(self):
        cuisine = Cuisine.objects.get(id=1)
        self.assertIsInstance(cuisine, Cuisine)
        self.assertEqual(cuisine.name, 'Wloska')
        self.assertEqual(str(cuisine), 'Wloska')

    def test_relation_with_recipie(self):
        cuisine = Cuisine.objects.get(id=1)
        cuisine2 = Cuisine.objects.get(id=2)
        recipe = Recipe.objects.get(id=1)
        recipe.cuisines.add(cuisine, cuisine2)
        recipe.save()
        self.assertIsInstance(recipe, Recipe)
        self.assertEqual(len(recipe.cuisines.all()), 2)
        self.assertEqual(recipe.cuisines.get(id=1).name, 'Wloska')
        self.assertEqual(Recipe.objects.get(cuisines__name='Fusion').title, 'Tytul Przepisu')
        self.assertEqual(len(Cuisine.objects.filter(recipe__title='Tytul Przepisu')), 2)


class TagModelTestCase(TestCase):

    def setUp(self):
        tag = Tag(name='Vege')
        tag1 = Tag(name='Fast')
        recipe = Recipe(title='Przepis1')
        recipe1 = Recipe(title='Przepis2')
        tag.save()
        tag1.save()
        recipe.save()
        recipe1.save()

    def test_tag_model(self):
        tag = Tag.objects.get(name='Vege')
        self.assertIsInstance(tag, Tag)
        self.assertEqual(tag.name, 'Vege')
        self.assertEqual(str(tag), 'Vege')

    def test_relation_with_recipe(self):
        recipe = Recipe.objects.get(id=1)
        recipe1 = Recipe.objects.get(title='Przepis2')
        tag = Tag.objects.get(id=1)
        tags = Tag.objects.all()
        recipe.tags.add(tag)
        for t in tags:
            recipe1.tags.add(t)
        self.assertEqual(recipe.tags.filter(name='Vege').get().id, 1)
        self.assertEqual(len(Recipe.objects.all()), 2)
#       sprwdzic czy recipe1 posiada 2 tagi
        self.assertEqual(len(Recipe.objects.get(id=2).tags.all()), 2)

class CategoryModelTestCase(TestCase):

    def setUp(self):
        cat = Category(name='Obiad')
        cat1 = Category(name='Kolacja')
        recipe = Recipe(title='Przepis1')
        recipe1 = Recipe(title='Przepis2')
        cat.save()
        cat1.save()
        recipe.save()
        recipe1.save()

    def test_category_model(self):
        cat = Category(name='Obiad')
        self.assertIsInstance(cat, Category)
        self.assertEqual(cat.name, 'Obiad')
        self.assertEqual(str(cat), 'Obiad')

    def test_relation_with_recipe(self):
        recipe = Recipe.objects.get(id=1)
        recipe1 = Recipe.objects.get(title='Przepis2')
        cat = Category.objects.get(id=1)
        cats = Category.objects.all()
        recipe.categories.add(cat)
        for c in cats:
            recipe1.categories.add(c)
        self.assertEqual(Recipe.objects.filter(categories__name=cat.name).first().title, 'Przepis1')
        self.assertEqual(len(Category.objects.all()), 2)


class IngredientModelTestCase(TestCase):

    def setUp(self):
        recipe = Recipe(title='przepis', description='opis przykładowego przepisu')
        recipe.save()
        milk = Ingredient(name='Mleko', measure='ML', quantity=300, recipe=recipe)
        nuddles = Ingredient(name='Makaron', measure='GR', quantity=100, recipe=recipe)
        milk.save()
        nuddles.save()

    def test_ingredients_model(self):
        ing = Ingredient(name='Mleko', measure='GR', quantity=100)
        self.assertIsInstance(ing, Ingredient)
        self.assertEqual(ing.name, 'Mleko')
        self.assertEqual(ing.measure, 'GR')
        self.assertEqual(ing.quantity, 100)
        self.assertEqual(str(ing), 'Mleko 100 GR')

    def test_relation_with_recipe(self):
        # relation OneToMany
        recipe = Recipe.objects.get(id=1)
        # znajdz wszystkie składniki dla wybranego pzepisu
        recipe_ing = Ingredient.objects.filter(recipe=recipe)
        recipe_ing2 = Ingredient.objects.filter(recipe__title='przepis')
        recipe_ing3 = Recipe.objects.get(ingredient__name='Mleko').title
        self.assertEqual(list(recipe_ing), list(recipe_ing2))
        self.assertEqual(recipe_ing3, 'przepis')
        # usunięcie składniku i sprawdzenie długości skladników
        recipe_ing2.first().delete()
        recipe_ing2 = Ingredient.objects.filter(recipe__title='przepis')
        self.assertEqual(len(recipe_ing2), 1)

class StepModelTestCase(TestCase):

    def setUp(self):
        recipe = Recipe(title='przepis', description='opis przykładowego przepisu')
        step = Step(number=1, description='opis pierwszego kroku', recipe=recipe)
        step2 = Step(number=4, description='opis drugiego', recipe=recipe)
        step3 = Step(number=2, description='opis trzeciego', recipe=recipe)
        recipe.save()
        step.save()
        step2.save()
        step3.save()

    def test_step_model(self):
        step = Step(number=1, description='lorem ipsum lorem ipsum')
        self.assertIsInstance(step, Step)
        self.assertEqual(step.number, 1)
        self.assertEqual(step.description, 'lorem ipsum lorem ipsum')
        self.assertEqual(str(step), str(1)+' Krok')

    def test_relation_with_recipe(self):
        recipe = Recipe.objects.get(id=1)
        step1 = Step.objects.get(description='opis pierwszego kroku')
        step2 = Step.objects.get(description='opis drugiego')
        step3 = Step.objects.get(description='opis trzeciego')
        self.assertEqual(step1.number, 1)
        self.assertEqual(step2.number, 3)
        self.assertEqual(step3.number, 2)
        self.assertEqual(list(Step.objects.filter(recipe=recipe)), [step1, step2, step3])