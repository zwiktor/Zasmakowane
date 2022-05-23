from django.contrib import admin
from django.urls import path
from recipe.views import home_view


urlpatterns = [
    path('', home_view),
]