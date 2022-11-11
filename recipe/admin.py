from django.contrib import admin
from recipe.models import Recipe, Ingredient, Category, Cuisine, Tag, Step

# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    exclude = ('slug',)

@admin.register(Step)
class RecipeAdmin(admin.ModelAdmin):
    exclude = ('number',)

admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Tag)