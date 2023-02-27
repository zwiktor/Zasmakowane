import django_filters
from .models  import Recipe, Category, Tag, Cuisine
from django.db import models
from django import forms

class RecipeFilter(django_filters.FilterSet):
    categories = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        label='Kategorie',
        widget=forms.CheckboxSelectMultiple
    )
    tags = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        label='Tagi',
        widget=forms.CheckboxSelectMultiple
    )
    cuisines = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Cuisine.objects.all(),
        label='Kuchnia',
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Recipe
        fields = ['categories', 'tags', 'cuisines', 'title']

