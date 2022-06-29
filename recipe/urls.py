from django.contrib import admin
from django.urls import path
from recipe.views import HomeView, CookBook, RecipeView, RecipeEdit, RecipeCreate, RecipeDelete, \
    AboutMe

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('przepisy', CookBook.as_view(), name='recipes'),
    path('omnie', AboutMe.as_view(), name='about'),
    path('przepisy/new', RecipeCreate.as_view(), name='recipe_new'),
    path('przepisy/<slug:slug>', RecipeView.as_view(), name='recipe'),
    path('przepisy/<slug:slug>/edit', RecipeEdit.as_view(), name='recipe_edit'),
    path('przepisy/<slug:slug>/delete', RecipeDelete.as_view(), name='recipe_delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)