from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Recipe, Comment, Ingredient, Step, Tag
from .forms import CommentForm
from .filters import RecipeFilter
# Create your views here.


class HomeView(View):
    def get(self, request):
        newest_recipes = Recipe.objects.all().order_by('create_date')[:4]
        fit_recipes = Recipe.objects.filter(tags=2)
        context = {'newest_recipes': newest_recipes, 'fit_recipes': fit_recipes}
        return render(request, 'Home.html', context)

    def post(self, requeset):
        pass


class CookBook(View):
    def get(self, request):
        newest_recipes = Recipe.objects.all()
        recipe_filter = RecipeFilter(request.GET, queryset=newest_recipes)
        print(recipe_filter.form)
        context = {'new_recipes': newest_recipes, 'recipe_filter': recipe_filter}
        return render(request, 'Cookbook.html', context)

    def post(self, requeset):
        pass


class AboutMe(View):
    def get(self, request):
        context = {}
        return render(request, 'About.html', context)

    def post(self, requeset):
        pass


class RecipeView(View):
    def get(self, request, slug):
        recipe = Recipe.objects.get(slug=slug)
        ingredients = Ingredient.objects.filter(recipe=recipe)
        steps = Step.objects.filter(recipe=recipe)
        tags = Tag.objects.filter(recipe=recipe)
        form = CommentForm()
        comments = Comment.objects.filter(recipe__slug=slug)
        context = {'recipe': recipe, 'form': form, 'comments': comments, 'ingredients':
            ingredients, 'steps': steps, 'tags': tags}
        return render(request, 'Recipe.html', context)

    def post(self, requeset):
        form_data = CommentForm(request.POST)
        if form_data.is_valid():
            pass
        pass


class RecipeCreate(View):
    def get(self, request):
        context = {}
        return render(request, 'Recipe_create.html', context)

    def post(self, requeset):
        pass


class RecipeEdit(View):
    def get(self, request, slug):
        context = {}
        return render(request, 'Recipe_edit.html', context)

    def post(self, requeset):
        pass


class RecipeDelete(View):
    def get(self, request, slug):
        context = {}
        return render(request, 'Recipe_delete.html', context)

    def post(self, requeset):
        pass