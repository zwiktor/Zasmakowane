from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from .models import Recipe, Comment, Ingredient, Step, Tag, Cuisine, Category, Ingedient_group, Post
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
        groups = Ingedient_group.objects.filter(recipe=recipe)
        steps = Step.objects.filter(recipe=recipe)
        steps = sorted(steps, key=lambda x: x.number)
        tags = Tag.objects.filter(recipe=recipe)
        cuisines = Cuisine.objects.filter(recipe=recipe)
        categories = Category.objects.filter(recipe=recipe)
        form = CommentForm()
        comments = Comment.objects.filter(recipe__slug=slug)
        context = {'recipe': recipe, 'form': form, 'comments': comments, 'groups':
            groups, 'steps': steps, 'tags': tags, 'cuisines':cuisines, 'categories':categories}
        return render(request, 'Recipe.html', context)

    def post(self, requeset, slug):
        recipe = Recipe.objects.get(slug=slug)
        form_data = CommentForm(requeset.POST, instance=recipe)
        if form_data.is_valid():
            obj = Comment(**form_data.cleaned_data)
            obj.recipe = recipe
            obj.save()

        return redirect('recipe', recipe.slug)


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


class BlogView(View):
    def get(self, request):
        posts = Post.objects.all()
        posts = posts.order_by('-create_date')
        context = {'posts': posts}
        return render(request, 'Blog.html', context)

    def post(self, requeset):
        pass


class PostView(View):
    def get(self, request, id):
        post_obj = Post.objects.get(id=id)
        context = {'post': post_obj}
        return render(request, 'Post.html', context)

    def post(self, requeset):
        pass