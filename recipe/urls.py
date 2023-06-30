from django.contrib import admin
from django.urls import path, include
from recipe.views import HomeView, CookBook, RecipeView, RecipeEdit, RecipeCreate, RecipeDelete, \
    AboutMe, BlogView, PostView

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
    path('blog', BlogView.as_view(), name='blog_page'),
    path('blog/<int:id>', PostView.as_view(), name='recipe_post'),
    path('ckeditor', include('ckeditor_uploader.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)