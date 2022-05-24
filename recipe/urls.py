from django.contrib import admin
from django.urls import path
from recipe.views import HomeView, CookBook


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('przepisy', CookBook.as_view(), name='recpies')
]