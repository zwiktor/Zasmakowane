from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Recipe
# Create your views here.


class HomeView(View):
    def get(self, request):
        newest_recipes = Recipe.objects.all()
        context = {'new_recipes': newest_recipes}
        return render(request, 'Home.html', context)

    def post(self, requeset):
        pass


class CookBook(View):
    def get(self, request):
        newest_recipes = Recipe.objects.all()
        context = {'new_recipes': newest_recipes}
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
        context = {'recipe': recipe}
        return render(request, 'Recipe.html', context)

    def post(self, requeset):
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