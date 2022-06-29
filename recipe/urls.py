from django.contrib import admin
from django.urls import path
from recipe.views import HomeView, CookBook, RecipeView, RecipeEdit, RecipeCreate, RecipeDelete, \
    AboutMe


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('przepisy', CookBook.as_view(), name='recpies'),
    path('omnie', AboutMe.as_view(), name='about'),
    path('przepisy/new', RecipeCreate.as_view(), name='recpie_new'),
    path('przepisy/<slug:slug>', RecipeView.as_view(), name='recpie'),
    path('przepisy/<slug:slug>/edit', RecipeEdit.as_view(), name='recpie_edit'),
    path('przepisy/<slug:slug>/delete', RecipeDelete.as_view(), name='recpie_delete'),

]